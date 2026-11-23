#!/usr/bin/env python3
"""Refresh data/cpi.json from FRED (CPIAUCNS), falling back to the BLS public API.
Keeps the previous file if every source fails, so the site never breaks."""
import csv, io, json, os, sys, datetime, urllib.request
from collections import defaultdict

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "cpi.json")
UA = {"User-Agent": "89944.com data refresher (+https://89944.com)"}


def get(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8")


def from_fred():
    rows = list(csv.reader(io.StringIO(get("https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCNS"))))
    monthly = []
    for d, v in rows[1:]:
        try:
            monthly.append((d[:7], float(v)))
        except ValueError:
            pass
    return monthly


def from_bls():
    monthly = []
    this = datetime.date.today().year
    for start in range(1913, this + 1, 10):
        body = json.dumps({"seriesid": ["CUUR0000SA0"], "startyear": str(start), "endyear": str(min(start + 9, this))}).encode()
        j = json.loads(get("https://api.bls.gov/publicAPI/v1/timeseries/data/", body, {"Content-Type": "application/json"}))
        for s in j["Results"]["series"]:
            for p in s["data"]:
                if p["period"].startswith("M") and p["period"] != "M13":
                    monthly.append((f'{p["year"]}-{p["period"][1:]}', float(p["value"])))
    return sorted(set(monthly))


def main():
    monthly = None
    for src in (from_fred, from_bls):
        try:
            monthly = src()
            if len(monthly) > 100:
                source = src.__name__
                break
        except Exception as e:
            print("source failed:", src.__name__, e, file=sys.stderr)
    if not monthly:
        print("all sources failed; keeping existing data")
        return
    monthly.sort()
    by_year = defaultdict(list)
    for ym, v in monthly:
        by_year[int(ym[:4])].append(v)
    annual = {y: round(sum(v) / len(v), 3) for y, v in by_year.items() if len(v) == 12}
    latest_ym, latest_v = monthly[-1]
    prev = dict(monthly).get(f"{int(latest_ym[:4]) - 1}{latest_ym[4:]}")
    out = {"series": "CPI-U, all items, U.S. city average, NSA (CPIAUCNS / CUUR0000SA0)", "source": source,
           "updated": datetime.datetime.utcnow().isoformat() + "Z", "latest": {"date": latest_ym, "value": latest_v},
           "yoy": round((latest_v / prev - 1) * 100, 2) if prev else None, "annual": annual}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(out, fh, separators=(",", ":"))
    print(f"CPI updated via {source}: latest {latest_ym} = {latest_v}, {len(annual)} years")


if __name__ == "__main__":
    main()
