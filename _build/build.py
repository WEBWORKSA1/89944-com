#!/usr/bin/env python3
"""Builds every static page of 89944.com. Run: python3 _build/build.py"""
import os, sys, json, datetime, html as H
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, foot, ad, lead_box, SITE
from tools import TOOLS
from guides import GUIDES

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PAGES = []


def write(path, content, prio="0.7"):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
    if path != "404.html":
        PAGES.append((path, prio))


def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def tool_card(t, root):
    tag = f'<span class="pill {t["tag"]}">{"Popular" if t["tag"]=="hot" else "New"}</span>' if t["tag"] else f'<span class="pill">{t["cat"]}</span>'
    return f'<a class="card" data-tool-card href="{root}tools/{t["slug"]}.html"><div class="ico">{t["icon"]}</div>{tag}<h3 style="margin-top:8px">{t["name"]}</h3><p>{t["short"]}</p></a>'


def guide_card(g, root):
    return f'<a class="card" href="{root}guides/{g["slug"]}.html"><div class="ico">{g["icon"]}</div><span class="pill">{g["cat"]} · {g["mins"]} min</span><h3 style="margin-top:8px">{g["title"]}</h3><p>{g["desc"]}</p></a>'


def page_hero(crumb, h1, sub, root, eyebrow=None):
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f'<section class="page-hero"><div class="wrap"><div class="breadcrumb"><a href="{root}index.html">Home</a> / {crumb}</div>{eb}<h1>{h1}</h1><p>{sub}</p></div></section>'


# ------------------------------------------------------------------ HOME
def home():
    r = ""
    cards = "".join(tool_card(t, r) for t in TOOLS[:8])
    gcards = "".join(guide_card(g, r) for g in GUIDES[:3])
    faq = [("Is everything on 89944.com free?", "Yes. All calculators, guides and the Price Machine are free to use with no sign-up. The site is supported by advertising, sponsors and voluntary donations."),
           ("Who are the tools for?", "Founders, e-commerce sellers, SaaS and AI builders, freelancers, students and everyday shoppers who want to make better pricing decisions."),
           ("Is my data stored?", "Calculator inputs stay in your browser. We only receive information you choose to send through a form."),
           ("What is the free pricing audit?", "A pricing analyst reviews your offer and sends back three concrete, testable recommendations. It's free with no obligation.")]
    body = head("89944 Price Lab — Free Pricing Calculators, Charm Pricing & Price Psychology",
                "Price smarter with free calculators for charm pricing, margin vs markup, discounts, break-even, AI API costs and inflation — plus expert pricing guides and a free audit.",
                "index.html", r, faq_ld(faq))
    body += f"""
<section class="hero"><div class="wrap hero-grid">
 <div>
  <span class="eyebrow">8 · 99 · 44 — every price tells a story</span>
  <h1>Price smarter. <em>Sell more.</em> Spend less.</h1>
  <p class="lead">Free, instant calculators and plain-English guides on the psychology and math of prices — for founders, sellers, AI builders, freelancers and smart shoppers.</p>
  <form class="hero-search" id="toolSearchForm" role="search"><input id="toolSearch" placeholder="Try “margin”, “AI cost”, “discount”…" aria-label="Search tools"><button class="btn btn-primary" type="submit">Find tool</button></form>
  <div class="hero-actions"><a class="btn btn-dark" href="tools/index.html">Browse all tools</a><a class="btn btn-ghost" href="audit.html">Get a free pricing audit</a></div>
  <div class="stats"><div><b>11</b>free calculators</div><div><b>8</b>in-depth guides</div><div><b>Daily</b>inflation data refresh</div></div>
 </div>
 <div class="tag-visual" aria-hidden="true">
  <div class="ptag t1"><span class="old">$10.00</span><span class="new">$9.99</span></div>
  <div class="ptag t2"><span class="old">cost $40 · +40% markup</span><span class="new">28.6%</span><div style="font-size:.8rem;color:var(--muted)">real margin</div></div>
  <div class="ptag t3"><span class="old">$8.99 in 1990</span><span class="new">≈ today?</span></div>
 </div>
</div></section>
<div class="marquee"><div class="marquee-track" id="pulse"><span>Charm pricing · <b>~60%</b> of advertised prices end in 9</span><span>20% + 10% off = <b>28%</b>, not 30%</span><span>40% markup = <b>28.6%</b> margin</span><span>Charm pricing · <b>~60%</b> of advertised prices end in 9</span><span>20% + 10% off = <b>28%</b>, not 30%</span><span>40% markup = <b>28.6%</b> margin</span></div></div>
<section><div class="wrap">
 <div class="section-head"><div><span class="eyebrow">Calculators</span><h2>Tools that pay for themselves</h2></div><p>Every tool runs instantly in your browser. No sign-up, no data stored.</p></div>
 <div class="grid g4">{cards}</div>
 <p class="center mt"><a class="btn btn-ghost" href="tools/index.html">See all 11 tools →</a></p>
</div></section>
{ad()}
<section class="alt"><div class="wrap">
 <div class="section-head"><div><span class="eyebrow">Who it's for</span><h2>Built for people who set — or pay — prices</h2></div></div>
 <div class="grid g4">
  <div class="card"><div class="ico">🚀</div><h3>Founders & SaaS</h3><p>Tiering, LTV:CAC, price increases and packaging that scale.</p><a href="tools/saas-ltv-cac-calculator.html">LTV:CAC tool →</a></div>
  <div class="card"><div class="ico">🤖</div><h3>AI builders</h3><p>Turn token costs into a price with healthy gross margin.</p><a href="tools/ai-api-cost-calculator.html">AI cost tool →</a></div>
  <div class="card"><div class="ico">🛍️</div><h3>E-commerce sellers</h3><p>Charm endings, promo math and margin that survives fees.</p><a href="tools/discount-calculator.html">Promo profit check →</a></div>
  <div class="card"><div class="ico">🧾</div><h3>Smart shoppers</h3><p>Unit prices, subscription audits and inflation context.</p><a href="tools/unit-price-calculator.html">Unit price tool →</a></div>
 </div>
</div></section>
{lead_box(r, src="home")}
<section><div class="wrap">
 <div class="section-head"><div><span class="eyebrow">Guides</span><h2>The psychology & math of price</h2></div><a class="btn btn-ghost btn-sm" href="guides/index.html">All guides →</a></div>
 <div class="grid g3">{gcards}</div>
</div></section>
<section class="dark"><div class="wrap grid g2" style="align-items:center">
 <div><span class="eyebrow" style="background:rgba(255,255,255,.1)">The Price Machine</span><h2 style="color:#fff">What did $8.99 cost in 1990?</h2><p>Our inflation calculator uses official U.S. CPI data, refreshed automatically every day. See what any past price means in today's dollars — and why "the good old days" weren't as cheap as they look.</p><a class="btn btn-primary" href="inflation.html">Open the Price Machine →</a></div>
 <div class="grid g2"><div class="card"><h3>📊 Official data</h3><p>U.S. Bureau of Labor Statistics CPI-U via FRED.</p></div><div class="card"><h3>🔄 Auto-refreshed</h3><p>Updated daily by an automated workflow.</p></div><div class="card"><h3>🎯 Any year</h3><p>Back to 1913.</p></div><div class="card"><h3>🧮 Annual rate</h3><p>See the compound yearly inflation rate.</p></div></div>
</div></section>
<section><div class="wrap grid g3">
 <a class="card" href="contests.html"><div class="ico">🏆</div><span class="pill hot">Monthly</span><h3 style="margin-top:8px">The $8.99 Challenge</h3><p>Submit a pricing teardown, win cash prizes and a feature on the site.</p></a>
 <a class="card" href="advertise.html"><div class="ico">📣</div><span class="pill">Partners</span><h3 style="margin-top:8px">Sponsor a calculator</h3><p>Put your brand in front of founders and sellers at the moment they make pricing decisions.</p></a>
 <a class="card" href="support.html"><div class="ico">💛</div><span class="pill new">Community</span><h3 style="margin-top:8px">Keep the tools free</h3><p>Support from $8.99 funds new tools, data and contest prizes.</p></a>
</div></section>
<section class="alt"><div class="wrap" style="max-width:860px"><h2 class="center">Frequently asked questions</h2>{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)}</div></section>
"""
    body += foot(r)
    write("index.html", body, "1.0")


# ------------------------------------------------------------------ TOOLS
def tools_pages():
    r = "../"
    for t in TOOLS:
        related = [x for x in TOOLS if x["slug"] != t["slug"] and x["cat"] == t["cat"]][:2] + [x for x in TOOLS if x["cat"] != t["cat"]][:3]
        related = related[:3]
        ld = faq_ld(t["faq"])
        app = {"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "applicationCategory": "BusinessApplication",
               "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": f"{SITE}/tools/{t['slug']}.html"}
        guide = next((g for g in GUIDES if g["tool"] == t["slug"]), None)
        b = head(t["title"], t["desc"], f"tools/{t['slug']}.html", r, ld, tool=t["key"])
        b = b.replace("</head>", f'<script type="application/ld+json">{json.dumps(app)}</script>\n</head>', 1)
        b += page_hero(f'<a href="index.html">Tools</a> / {t["name"]}', f'{t["icon"]} {t["name"]}', t["short"], r, t["cat"])
        b += f"""<section style="padding-top:0"><div class="wrap tool-layout">
 <form class="panel" onsubmit="return false" aria-label="{H.escape(t['name'])} inputs">{t['form']}</form>
 <aside class="panel result-panel" aria-live="polite">{t['result']}
  <div class="mt"><a class="btn btn-primary btn-sm" href="../audit.html">Get expert help with this →</a> <button class="btn btn-sm" style="background:transparent;color:#fbf7ef;border-color:#fbf7ef" type="button" onclick="navigator.share?navigator.share({{title:document.title,url:location.href}}):navigator.clipboard.writeText(location.href)">Share</button></div>
 </aside>
</div></section>
{ad()}
<section style="padding-top:20px"><div class="wrap article-grid"><article class="prose">{t['body']}
<h2>FAQ</h2>{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t['faq'])}
</article>
<aside class="sidebar">
 {f'<div class="panel"><span class="pill">Read next</span><h3 style="margin-top:8px"><a href="../guides/{guide["slug"]}.html">{guide["title"]}</a></h3><p class="muted">{guide["desc"]}</p></div>' if guide else ''}
 <div class="panel"><h3>Related tools</h3>{''.join(f'<p><a href="{x["slug"]}.html">{x["icon"]} {x["name"]}</a></p>' for x in related)}</div>
 <div class="panel"><h3>💛 Find this useful?</h3><p class="muted">Help keep every tool free.</p><a class="btn btn-primary btn-sm" href="../support.html">Support 89944</a></div>
</aside></div></section>
{lead_box(r, "Want a pricing expert to check your numbers?", src=t['key'])}
"""
        b += foot(r)
        write(f"tools/{t['slug']}.html", b, "0.9")

    # hub
    cats = []
    for t in TOOLS:
        if t["cat"] not in cats:
            cats.append(t["cat"])
    b = head("All Free Pricing Calculators & Tools | 89944 Price Lab", "Every free pricing tool in one place: charm price, margin & markup, discounts, break-even, unit price, subscriptions, AI API cost, freelance rate, SaaS LTV:CAC and inflation.", "tools/index.html", r)
    b += page_hero("Tools", "Pricing calculators", "Eleven free tools covering psychology, profit, promotions, AI, SaaS and smart shopping. Everything runs in your browser.", r, "11 tools · 0 sign-ups")
    b += f'<section style="padding-top:0"><div class="wrap"><form class="hero-search" id="toolSearchForm" role="search" style="margin-bottom:28px"><input id="toolSearch" placeholder="Search tools…" aria-label="Search tools"><button class="btn btn-primary" type="submit">Go</button></form>'
    for c in cats:
        b += f'<h2 style="margin-top:24px">{c}</h2><div class="grid g3">' + "".join(tool_card(t, r) for t in TOOLS if t["cat"] == c) + "</div>"
    b += f'<h2 style="margin-top:24px">Data</h2><div class="grid g3"><a class="card" data-tool-card href="../inflation.html"><div class="ico">⏳</div><span class="pill new">Daily data</span><h3 style="margin-top:8px">The Price Machine (inflation)</h3><p>What any past price is worth today using official CPI data.</p></a></div>'
    b += "</div></section>" + ad() + "<script>try{const q=new URLSearchParams(location.search).get('q');if(q){const s=document.getElementById('toolSearch');s.value=q;setTimeout(()=>s.dispatchEvent(new Event('input')),50)}}catch(e){}</script>"
    b += lead_box(r, src="tools-hub") + foot(r)
    write("tools/index.html", b, "0.9")


# ------------------------------------------------------------------ GUIDES
def guides_pages():
    r = "../"
    for g in GUIDES:
        import re
        heads = re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>', g["body"])
        toc = '<nav class="toc"><b>On this page</b><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in heads) + "</ol></nav>"
        t = next(x for x in TOOLS if x["slug"] == g["tool"])
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "author": {"@type": "Organization", "name": "89944 Price Lab Editorial"},
               "publisher": {"@type": "Organization", "name": "89944 Price Lab"}, "datePublished": "2026-11-23", "dateModified": datetime.date.today().isoformat(), "mainEntityOfPage": f"{SITE}/guides/{g['slug']}.html"}
        # split body after 3rd paragraph-ish for mid-article ad
        body = g["body"]
        parts = body.split("<h2", 3)
        if len(parts) == 4:
            body = parts[0] + "<h2" + parts[1] + "<h2" + parts[2] + ad() + "<h2" + parts[3]
        b = head(g["title"] + " | 89944", g["desc"], f"guides/{g['slug']}.html", r, art)
        b += f"""<section class="page-hero"><div class="wrap" style="max-width:860px"><div class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Guides</a> / {g['cat']}</div>
<span class="eyebrow">{g['cat']} · {g['mins']} min read</span><h1 style="font-size:clamp(1.9rem,4vw,2.8rem)">{g['title']}</h1><p>{g['desc']}</p><p class="muted" style="font-size:.9rem">By 89944 Price Lab Editorial · Updated <time>{datetime.date.today().strftime('%B %Y')}</time></p></div></section>
<section style="padding-top:0"><div class="wrap article-grid"><article class="prose">{toc}{body}
<div class="panel mt" style="background:var(--paper-2)"><h3>{t['icon']} Try it: {t['name']}</h3><p class="muted">{t['short']}</p><a class="btn btn-primary btn-sm" href="../tools/{t['slug']}.html">Open the calculator →</a></div>
<p class="muted mt" style="font-size:.85rem">This guide is educational and general in nature. It is not financial, tax or legal advice. Figures cited are illustrative; verify against your own data.</p>
</article><aside class="sidebar">
<div class="panel"><h3>📬 The Price Letter</h3><p class="muted">One sharp pricing idea every week.</p><form data-send data-subject="Newsletter signup (guide)" data-ok="Subscribed!"><div class="field"><input type="email" name="email" placeholder="you@email.com" required aria-label="Email"></div><input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true"><button class="btn btn-primary btn-block btn-sm" type="submit">Subscribe</button></form></div>
<div class="panel"><h3>More guides</h3>{''.join(f'<p><a href="{x["slug"]}.html">{x["icon"]} {x["title"]}</a></p>' for x in GUIDES if x['slug'] != g['slug'])}</div>
</aside></div></section>
{lead_box(r, src='guide-' + g['slug'][:20])}"""
        b += foot(r)
        write(f"guides/{g['slug']}.html", b, "0.8")
    b = head("Pricing Guides — Psychology, Profit, AI & Shopping | 89944", "In-depth, plain-English guides on charm pricing, margin vs markup, AI product pricing, discounts, price increases, freelance rates and smart shopping.", "guides/index.html", r)
    b += page_hero("Guides", "Pricing guides", "Original, practical guides on the psychology and math of prices. Each one links to a free calculator so you can apply it immediately.", r, f"{len(GUIDES)} guides")
    b += '<section style="padding-top:0"><div class="wrap grid g3">' + "".join(guide_card(g, r) for g in GUIDES) + "</div></section>" + ad() + lead_box(r, src="guides-hub") + foot(r)
    write("guides/index.html", b, "0.8")


# ------------------------------------------------------------------ SIMPLE PAGE helper
def simple(path, title, desc, crumb, h1, sub, inner, prio="0.6", eyebrow=None, tool=None, lead=True):
    r = ""
    b = head(title, desc, path, r, tool=tool) + page_hero(crumb, h1, sub, r, eyebrow) + inner
    if lead:
        b += lead_box(r, src=path.replace(".html", ""))
    b += foot(r)
    write(path, b, prio)


def hp():
    return '<input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'


# ------------------------------------------------------------------ INFLATION
def inflation():
    inner = f"""<section style="padding-top:0"><div class="wrap tool-layout">
<form class="panel" onsubmit="return false"><div class="field"><label for="in_price">Price then ($)</label><input id="in_price" type="number" step="any" value="8.99"></div>
<div class="field"><label for="in_year">Year</label><select id="in_year"><option>Loading…</option></select></div>
<p class="hint" id="in_src"></p></form>
<aside class="panel result-panel" aria-live="polite"><h3>Worth today</h3><div class="big-num" id="in_now">—</div><div class="kv"><span>Price multiplier</span><span id="in_mult">—</span></div><div class="kv"><span>Avg. inflation rate</span><span id="in_rate">—</span></div><p class="note">CPI measures an average basket. Your personal inflation depends on what you buy.</p></aside>
</div></section>{ad()}
<section><div class="wrap prose"><h2>How the Price Machine works</h2><p>The Consumer Price Index for All Urban Consumers (CPI-U), published by the U.S. Bureau of Labor Statistics, tracks the average change in prices paid for a broad basket of goods and services. To convert a past price to today's dollars we multiply it by the ratio of the latest CPI value to the average CPI of the year you choose.</p>
<div class="formula">Today's equivalent = Past price × (Latest CPI ÷ CPI in chosen year)</div>
<p>An automated job refreshes the data every day from the Federal Reserve Bank of St. Louis (FRED) series CPIAUCNS, so the "today" figure always reflects the most recently published month.</p>
<h2>Why this matters for pricing</h2><p>If you haven't raised a price in five years, inflation has quietly cut it in real terms. Use the Price Machine to see how far your price has drifted, then model a correction with the <a href="tools/price-increase-calculator.html">price increase calculator</a>.</p></div></section>"""
    simple("inflation.html", "Inflation Calculator — What Was $8.99 Worth? The Price Machine | 89944",
           "Convert any past U.S. price into today's dollars using official CPI-U data, refreshed daily. See the multiplier and average annual inflation rate.",
           "Price Machine", "⏳ The Price Machine", "What would a past price cost today? Official CPI data, refreshed automatically every day.", inner, "0.9", "Inflation calculator", tool="inflation")


# ------------------------------------------------------------------ VIDEOS
def videos():
    topics = [("Charm pricing explained", "charm pricing psychology explained"), ("Price anchoring", "price anchoring marketing explained"), ("Decoy effect", "decoy effect pricing"),
              ("Margin vs markup", "margin vs markup explained"), ("Break-even analysis", "break even analysis explained"), ("SaaS pricing strategy", "saas pricing strategy"),
              ("Pricing AI products", "how to price an AI product"), ("Value-based pricing", "value based pricing explained"), ("Raising your prices", "how to raise prices without losing customers"),
              ("Freelance rates", "how to set freelance rates"), ("Unit price shopping", "unit price grocery shopping tips"), ("Inflation & CPI", "how CPI inflation is measured")]
    cards = "".join(f'<div class="card"><div class="vid search" data-q="{q}" role="button" tabindex="0" aria-label="Watch videos about {n} on YouTube"></div><h3 style="margin-top:12px">{n}</h3><p>Hand-picked topic playlist on YouTube.</p></div>' for n, q in topics)
    inner = f"""<section style="padding-top:0"><div class="wrap"><div class="grid g3">{cards}</div>
<p class="muted mt">Videos open on YouTube and are owned by their creators. 89944.com is not affiliated with YouTube or the channels shown.</p></div></section>{ad()}
<section class="alt"><div class="wrap grid g2" style="align-items:center"><div><span class="eyebrow">Creators</span><h2>Make pricing videos? Get featured.</h2><p class="muted">We feature the best explainers on pricing, business math and smart shopping. Featured creators get a backlink and a spot in The Price Letter.</p></div>
<form class="panel" data-send data-subject="Video creator submission" data-ok="Thanks! We review submissions weekly."><div class="field"><label for="vc_name">Channel name</label><input id="vc_name" name="channel" required></div><div class="field"><label for="vc_url">Video URL</label><input id="vc_url" name="video_url" type="url" required></div><div class="field"><label for="vc_email">Email</label><input id="vc_email" name="email" type="email" required></div>{hp()}<button class="btn btn-primary btn-block" type="submit">Submit video</button></form></div></section>"""
    simple("videos.html", "Pricing Strategy Videos — Learn Price Psychology | 89944", "Curated video topics on charm pricing, anchoring, SaaS and AI pricing, break-even analysis and smart shopping, plus creator submissions.",
           "Videos", "🎬 Learn pricing by video", "Curated topics from the best explainers on price psychology, business math and smart shopping.", inner, "0.6", "Video library")


# ------------------------------------------------------------------ AUDIT (lead gen)
def audit():
    def chk(name, opts):
        return '<div class="choice-grid" data-need-choice>' + "".join(f'<label><input type="checkbox" name="{name}" value="{o}">{o}</label>' for o in opts) + "</div>"
    inner = f"""<section style="padding-top:0"><div class="wrap grid g2" style="align-items:start">
<div>
 <div class="grid g2">
  <div class="card"><div class="ico">🔍</div><h3>Price-point review</h3><p>Endings, anchors and left-digit opportunities on your top products.</p></div>
  <div class="card"><div class="ico">💸</div><h3>Promo leak check</h3><p>Where discounts give away margin without adding sales.</p></div>
  <div class="card"><div class="ico">📦</div><h3>Packaging & tiers</h3><p>Good-better-best tiers, bundles and annual plans.</p></div>
  <div class="card"><div class="ico">🤖</div><h3>AI / SaaS unit economics</h3><p>Token costs, fair-use caps and margin protection.</p></div>
 </div>
 <h2 class="mt">How it works</h2>
 <ol class="prose"><li><b>Tell us about your business</b> — 60 seconds, 3 short steps.</li><li><b>We review</b> your site, prices and offer.</li><li><b>You get 3 specific changes</b> to test, by email within 48 hours.</li><li><b>Optional:</b> a call to discuss a deeper engagement — no pressure.</li></ol>
 <details><summary>Is it really free?</summary><p>Yes. The audit is free and carries no obligation. Some businesses choose to hire us or a partner for implementation afterwards.</p></details>
 <details><summary>What do you do with my information?</summary><p>We use it only to prepare your audit and reply to you. We never sell your data. See our privacy policy.</p></details>
 <details><summary>Who reviews my pricing?</summary><p>An analyst from the 89944 Price Lab network with experience in e-commerce, SaaS and services pricing.</p></details>
</div>
<form class="panel" data-send data-multistep data-subject="FULL pricing audit request" data-ga="audit" data-ok="🎉 Request received! Your audit will arrive within 48 hours. Check your inbox (and spam folder).">
 <div class="steps"><i></i><i></i><i></i></div>
 <div class="step"><h3>1. Your business</h3>
  <div class="field"><label>Business type</label><select name="business_type" required><option value="">Choose…</option><option>E-commerce / DTC</option><option>SaaS / software</option><option>AI product / API</option><option>Agency / services / freelance</option><option>Restaurant / local retail</option><option>Courses / digital products</option><option>Marketplace seller</option><option>Other</option></select></div>
  <div class="field"><label>Monthly revenue</label><select name="monthly_revenue" required><option value="">Choose…</option><option>Pre-revenue</option><option>Under $5k</option><option>$5k – $25k</option><option>$25k – $100k</option><option>$100k – $500k</option><option>$500k+</option></select></div>
  <div class="field"><label>Website / store URL</label><input name="website" placeholder="https://"></div>
  <button class="btn btn-primary btn-block" data-next>Next →</button></div>
 <div class="step"><h3>2. Your pricing challenge</h3><p class="muted">Pick all that apply</p>
  {chk("challenges", ["Not sure what to charge", "Margins too thin", "Discounts not working", "Need to raise prices", "Designing tiers / plans", "AI costs eating margin", "Competitors undercut us", "Low conversion rate"])}
  <div class="field mt"><label>Anything else we should know?</label><textarea name="details" rows="3"></textarea></div>
  <div class="row"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" data-next>Next →</button></div></div>
 <div class="step"><h3>3. Where should we send it?</h3>
  <div class="field"><label>Full name</label><input name="name" required autocomplete="name"></div>
  <div class="field"><label>Email</label><input name="email" type="email" required autocomplete="email"></div>
  <div class="field"><label>Phone / WhatsApp (optional)</label><input name="phone" type="tel" autocomplete="tel"></div>
  <div class="field"><label>Interested in hands-on help afterwards?</label><select name="interest"><option>Just the free audit for now</option><option>Yes — send me options</option><option>Yes — book a call</option></select></div>
  <label style="font-weight:400;display:flex;gap:8px;align-items:start"><input type="checkbox" name="consent" value="yes" required style="width:auto;margin-top:5px"> I agree to be contacted about my audit and accept the privacy policy.</label>
  {hp()}
  <div class="row mt"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" type="submit">Get my free audit 🎯</button></div></div>
</form></div></section>
<section class="alt"><div class="wrap center"><h2>Prefer to talk first?</h2><p class="muted">Send a quick message and we'll reply within one business day.</p><a class="btn btn-dark" href="contact.html">Contact us</a></div></section>"""
    simple("audit.html", "Free Pricing Audit — 3 Changes to Boost Profit in 48h | 89944", "Get a free, no-obligation pricing audit: price points, discounts, tiers and AI/SaaS unit economics reviewed by a pricing analyst, with 3 actionable changes in 48 hours.",
           "Free pricing audit", "Get a free pricing audit", "Three specific, testable changes to your prices, promotions or packaging — delivered within 48 hours. No cost, no obligation.", inner, "0.9", "Free · 48h · no obligation", lead=False)


# ------------------------------------------------------------------ SUPPORT / DONATE
def support():
    inner = f"""<section style="padding-top:0"><div class="wrap">
<div class="grid g3">
 <div class="card tier"><span class="pill">Supporter</span><div class="amt">$8.99</div><p>Buy the lab a coffee. Your name on the Supporters wall.</p></div>
 <div class="card tier featured"><span class="pill hot">Most chosen</span><div class="amt">$44</div><p>Funds one new calculator feature. Supporter wall + early access to new tools.</p></div>
 <div class="card tier"><span class="pill">Patron</span><div class="amt">$99</div><p>Funds a month of contest prizes. Patron listing with link + thank-you in The Price Letter.</p></div>
</div>
<div class="grid g2 mt" style="align-items:start">
 <div class="prose"><h2>Where your support goes</h2>
  <ul><li><b>Operations</b> — hosting, data feeds and tool maintenance.</li><li><b>New tools & content</b> — hiring writers, analysts and developers.</li><li><b>Contests & prizes</b> — funding the monthly $8.99 Challenge.</li><li><b>Promotion & marketing</b> — reaching more founders and shoppers.</li></ul>
  <p>Donations are voluntary support for a free resource and are <b>not tax-deductible</b>. 89944.com is not a registered charity.</p>
  <h3>Other ways to help</h3><ul><li>Share a tool with someone who sets prices.</li><li>Link to us from your blog or resource page.</li><li><a href="contests.html">Enter</a> or <a href="advertise.html">sponsor</a> a contest.</li></ul></div>
 <form class="panel" data-send data-subject="Donation / support pledge" data-ok="Thank you! 💛 We'll email you a secure payment link within 24 hours.">
  <h3>Make a pledge</h3><p class="muted">Choose an amount — we'll send you a secure payment link (card, PayPal or bank transfer).</p>
  <div class="amount-pick" data-target="#don_amt"><button data-v="8.99">$8.99</button><button data-v="25">$25</button><button class="on" data-v="44">$44</button><button data-v="99">$99</button><button data-v="250">$250</button></div>
  <div class="field mt"><label for="don_amt">Amount (USD)</label><input id="don_amt" name="amount" type="number" min="1" step="any" value="44" required></div>
  <div class="field"><label>Frequency</label><select name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div>
  <div class="field"><label>Purpose</label><select name="purpose"><option>General support / operations</option><option>Contest prizes</option><option>New tools & hiring</option><option>Promotion & marketing</option></select></div>
  <div class="row"><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input name="email" type="email" required></div></div>
  <div class="field"><label>Name on Supporters wall</label><input name="display_name" placeholder="Or leave blank to stay anonymous"></div>
  {hp()}<button class="btn btn-primary btn-block" type="submit">Pledge support 💛</button></form>
</div></div></section>"""
    simple("support.html", "Support 89944 Price Lab — Donate to Keep Pricing Tools Free", "Support free pricing tools with a one-time or monthly contribution that funds operations, new tools, hiring, promotion and contest prizes.",
           "Support", "💛 Keep the tools free", "89944 Price Lab is free for everyone. Your support pays for operations, new tools, talent, promotion and contest prizes.", inner, "0.6", "Support & donations")


# ------------------------------------------------------------------ ADVERTISE
def advertise():
    pk = [("Tool Sponsor", "Exclusive 'Sponsored by' placement on one calculator + result panel CTA.", "From $299/mo"),
          ("Newsletter Feature", "Primary sponsor slot in The Price Letter, sent weekly.", "From $149/issue"),
          ("Guide Partner", "Sponsored, clearly-labelled section in a relevant guide.", "From $399/mo"),
          ("Contest Sponsor", "Fund a monthly $8.99 Challenge prize pool; logo on contest & winners pages.", "From $250/round"),
          ("Domain / Site Partnership", "Joint venture, white-label tools, or acquisition of 89944.com.", "Let's talk"),
          ("Custom Calculator", "We build a branded pricing calculator for your product audience.", "From $1,500")]
    cards = "".join(f'<div class="card"><h3>{n}</h3><p>{d}</p><p class="mono" style="color:var(--tag);font-weight:700">{p}</p></div>' for n, d, p in pk)
    inner = f"""<section style="padding-top:0"><div class="wrap"><div class="grid g3">{cards}</div>
<div class="grid g2 mt" style="align-items:start"><div class="prose"><h2>Why sponsor 89944?</h2><ul><li><b>High-intent audience:</b> people actively setting prices, building products and comparing costs.</li><li><b>Contextual placement:</b> your offer appears next to the exact decision it helps with.</li><li><b>Brand-safe:</b> original, educational content; every sponsorship is clearly labelled.</li></ul><p>All sponsored content is labelled "Sponsored" and complies with advertising disclosure rules and Google publisher policies.</p></div>
<form class="panel" data-send data-subject="Advertising / sponsorship inquiry" data-ga="advertise" data-ok="Thanks! Our partnerships team will reply within 1 business day with availability and a media kit.">
<h3>Request the media kit</h3>
<div class="row"><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Company</label><input name="company" required></div></div>
<div class="field"><label>Email</label><input name="email" type="email" required></div>
<div class="field"><label>Interested in</label><select name="package">{''.join(f'<option>{n}</option>' for n, _, _ in pk)}<option>Something else</option></select></div>
<div class="field"><label>Budget (monthly)</label><select name="budget"><option>Under $500</option><option>$500 – $2,000</option><option>$2,000 – $10,000</option><option>$10,000+</option></select></div>
<div class="field"><label>Message</label><textarea name="message" rows="3"></textarea></div>{hp()}
<button class="btn btn-primary btn-block" type="submit">Send inquiry</button></form></div></div></section>"""
    simple("advertise.html", "Advertise, Sponsor or Partner with 89944 Price Lab", "Sponsor calculators, newsletters, guides and contests to reach founders, sellers and smart shoppers. Partnership and domain inquiries welcome.",
           "Advertise", "📣 Advertise & partner", "Reach founders, sellers, AI builders and shoppers at the moment they make pricing decisions.", inner, "0.6", "Sponsorship · Ads · Partnerships", lead=False)


# ------------------------------------------------------------------ CONTESTS
def contests():
    inner = f"""<section style="padding-top:0"><div class="wrap grid g2" style="align-items:start">
<div><div class="panel" style="background:var(--ink);color:#fbf7ef"><span class="pill hot">Round open</span><h2 style="color:#fff;margin-top:10px">The $8.99 Challenge</h2><p style="color:#e8ddcc">Pick any real product or service. Write a pricing teardown: what it charges, why, and how you'd improve it. Best teardowns win.</p><p style="color:#e8ddcc">This round closes in:</p><div class="countdown" id="countdown"></div></div>
<div class="grid g3 mt"><div class="card tier"><span class="pill">1st</span><div class="amt">$89.44</div><p>+ featured guide</p></div><div class="card tier"><span class="pill">2nd</span><div class="amt">$44</div><p>+ newsletter feature</p></div><div class="card tier"><span class="pill">3rd</span><div class="amt">$8.99</div><p>+ shout-out</p></div></div>
<div class="prose mt"><h3>Judging criteria</h3><ul><li>Insight (40%) — does it reveal something non-obvious?</li><li>Use of numbers (30%) — margins, anchors, comparisons.</li><li>Actionability (20%) — clear, testable recommendations.</li><li>Clarity (10%).</li></ul>
<h3>Official rules (summary)</h3><ul><li>No purchase or payment necessary to enter or win. A donation does not improve your chances.</li><li>Open to individuals aged 18+ where legally permitted; void where prohibited.</li><li>One entry per person per round; entries must be original and under 1,500 words.</li><li>Winners are chosen by a judging panel within 14 days of the round closing and notified by email; prizes are paid digitally.</li><li>By entering, you grant 89944.com a non-exclusive licence to publish your entry with credit.</li><li>Prize pools may be funded by sponsors, who are named on this page.</li></ul></div></div>
<form class="panel" data-send data-subject="Contest entry: $8.99 Challenge" data-ga="contest" data-ok="Entry received! Good luck 🍀 Winners are announced within 14 days after the round closes.">
<h3>Submit your entry</h3>
<div class="row"><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input name="email" type="email" required></div></div>
<div class="field"><label>Product / company analysed</label><input name="subject" required></div>
<div class="field"><label>Link to your teardown (Doc, blog, PDF) or paste below</label><input name="link" type="url" placeholder="https://"></div>
<div class="field"><label>Teardown (optional if linked)</label><textarea name="teardown" rows="7"></textarea></div>
<label style="font-weight:400;display:flex;gap:8px;align-items:start"><input type="checkbox" required style="width:auto;margin-top:5px" name="rules" value="accepted"> I'm 18+ and accept the official rules.</label>{hp()}
<button class="btn btn-primary btn-block mt" type="submit">Enter the challenge 🏆</button>
<p class="hint">Want to sponsor a prize pool? <a href="advertise.html">Become a contest sponsor</a>.</p></form>
</div></section>"""
    simple("contests.html", "The $8.99 Challenge — Monthly Pricing Contest with Prizes | 89944", "Enter the monthly $8.99 Challenge: write a pricing teardown and win cash prizes and features. Free entry, official rules, sponsor opportunities.",
           "Contests", "🏆 Contests & prizes", "Free monthly competitions for sharp pricing minds. Win cash, features and backlinks.", inner, "0.6", "Free entry · monthly")


# ------------------------------------------------------------------ CAREERS
def careers():
    roles = [("Contributing Pricing Writer", "Remote · freelance", "Write original guides on pricing psychology, SaaS and e-commerce."),
             ("Pricing Analyst (audits)", "Remote · contract", "Deliver free and paid pricing audits for inbound leads."),
             ("Front-end Developer", "Remote · project", "Build new calculators in vanilla JS with accessibility in mind."),
             ("Video Creator / Editor", "Remote · freelance", "Produce short explainers for YouTube and social."),
             ("Community & Contest Manager", "Remote · part-time", "Run the $8.99 Challenge, judge entries, grow the newsletter."),
             ("Partnerships & Ad Sales", "Remote · commission", "Sell sponsorships to SaaS, fintech and e-commerce brands.")]
    cards = "".join(f'<div class="card"><span class="pill">{t}</span><h3 style="margin-top:8px">{n}</h3><p>{d}</p></div>' for n, t, d in roles)
    inner = f"""<section style="padding-top:0"><div class="wrap"><div class="grid g3">{cards}</div>
<div class="grid g2 mt" style="align-items:start"><div class="prose"><h2>How we work</h2><ul><li>Fully remote, async-first.</li><li>Paid per project or on contract; top contributors get ongoing work.</li><li>We value clear thinking, real numbers and plain English.</li></ul><p>Don't see your role? Apply anyway and tell us what you'd build.</p></div>
<form class="panel" data-send data-subject="Job application" data-ga="careers" data-ok="Application received! We review applications weekly and reply to shortlisted candidates.">
<h3>Apply</h3><div class="row"><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input name="email" type="email" required></div></div>
<div class="field"><label>Role</label><select name="role" required>{''.join(f'<option>{n}</option>' for n, _, _ in roles)}<option>Other</option></select></div>
<div class="field"><label>Portfolio / LinkedIn / GitHub</label><input name="portfolio" type="url" placeholder="https://" required></div>
<div class="field"><label>Why you? (short)</label><textarea name="pitch" rows="4" required></textarea></div>
<div class="field"><label>Rate / expectations</label><input name="rate"></div>{hp()}
<button class="btn btn-primary btn-block" type="submit">Send application</button></form></div></div></section>"""
    simple("careers.html", "Careers at 89944 Price Lab — Remote Writing, Analyst & Dev Roles", "Join 89944 Price Lab: remote roles for pricing writers, analysts, front-end developers, video creators, community managers and ad sales.",
           "Careers", "🧑‍🤝‍🧑 Work with us", "We're hiring remote talent to build the best free pricing resource on the web.", inner, "0.5", "Hiring · remote", lead=False)


# ------------------------------------------------------------------ CONTACT
def contact():
    inner = f"""<section style="padding-top:0"><div class="wrap grid g2" style="align-items:start">
<div class="prose"><h2>How can we help?</h2><ul><li><b>Pricing help</b> — <a href="audit.html">request a free audit</a>.</li><li><b>Advertising & sponsorship</b> — <a href="advertise.html">see packages</a>.</li><li><b>Domain / website / partnership</b> — use the form and choose the topic.</li><li><b>Corrections</b> — spotted an error in a tool or guide? Tell us and we'll fix it.</li></ul><p>We reply to every genuine message within 1–2 business days.</p></div>
<form class="panel" data-send data-subject="Contact form" data-ga="contact">
<div class="row"><div class="field"><label for="c_name">Name</label><input id="c_name" name="name" required></div><div class="field"><label for="c_email">Email</label><input id="c_email" name="email" type="email" required></div></div>
<div class="field"><label for="c_topic">Topic</label><select id="c_topic" name="topic"><option>General question</option><option>Pricing help / audit</option><option>Advertising / sponsorship</option><option>Domain name / website acquisition</option><option>Partnership</option><option>Correction / feedback</option><option>Press</option></select></div>
<div class="field"><label for="c_msg">Message</label><textarea id="c_msg" name="message" rows="6" required></textarea></div>{hp()}
<button class="btn btn-primary btn-block" type="submit">Send message</button></form></div></section>"""
    simple("contact.html", "Contact 89944 Price Lab", "Contact 89944 Price Lab about pricing help, advertising, sponsorship, partnerships, domain inquiries or corrections.",
           "Contact", "Contact us", "Questions, partnerships, sponsorships or feedback — send us a message.", inner, "0.5", lead=False)


# ------------------------------------------------------------------ ABOUT / LEGAL / GLOSSARY
def about():
    inner = """<section style="padding-top:0"><div class="wrap prose">
<h2>Our mission</h2><p>Prices are the most powerful — and most neglected — number in any business. A single percentage point of price improvement typically has a larger effect on profit than the same improvement in volume or costs. Yet most founders set prices once, copy a competitor and never revisit them. Shoppers, meanwhile, face package sizes and promotions engineered to blur comparison.</p>
<p>89944 Price Lab exists to make pricing clear. We build free, private, instant calculators and write plain-English guides grounded in established marketing and finance principles.</p>
<h2>Why "8 · 99 · 44"?</h2><p>The domain's digits read like a price tag: an 8, a 99 ending and a 44. The 99 ending is the most common in retail. We use the number as a memorable name, not a claim to any product, slogan or brand.</p>
<h2>Editorial standards</h2><ul><li>Every formula is shown so you can check our math.</li><li>Examples are illustrative and labelled as such.</li><li>Rates that change frequently (such as AI model prices) are user-editable rather than hard-coded.</li><li>Sponsored content is always clearly labelled and never changes a tool's output.</li><li>We correct errors promptly — <a href="contact.html">tell us</a> if you find one.</li></ul>
<h2>How we're funded</h2><p>Advertising (including Google AdSense), clearly-labelled sponsorships, optional paid pricing services and voluntary <a href="support.html">support</a> from users.</p></div></section>"""
    simple("about.html", "About 89944 Price Lab", "About 89944 Price Lab: our mission to make pricing clear with free calculators and plain-English guides, editorial standards and funding.",
           "About", "About 89944 Price Lab", "Free tools and plain-English guides that make the psychology and math of prices clear.", inner, "0.5")


def legal():
    upd = datetime.date.today().strftime("%B %d, %Y")
    privacy = f"""<section style="padding-top:0"><div class="wrap prose"><p><i>Last updated: {upd}</i></p>
<h2>Overview</h2><p>This Privacy Policy explains how 89944.com ("we", "us") collects, uses and protects information when you use this website.</p>
<h2>Information we collect</h2><ul><li><b>Information you submit</b> — name, email and other details you enter into forms (audit requests, contact, newsletter, contest entries, job applications, pledges). Forms are delivered to us by email via a third-party form-processing service (FormSubmit).</li><li><b>Calculator inputs</b> — processed in your browser only and not sent to us.</li><li><b>Usage data</b> — standard log data and cookies used by our hosting provider and advertising partners.</li></ul>
<h2>Cookies and advertising</h2><p>We use Google AdSense to display ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the Internet.</p>
<p>You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" rel="nofollow noopener" target="_blank">Google Ads Settings</a>, or opt out of some third-party vendors' use of cookies at <a href="https://www.aboutads.info/choices/" rel="nofollow noopener" target="_blank">aboutads.info</a>. Learn more about <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener" target="_blank">how Google uses data from partner sites</a>.</p>
<p>Visitors in the EEA, UK and Switzerland are shown a consent message where required, and we use a Google-certified consent management platform for ad personalisation consent where applicable.</p>
<h2>Embedded content</h2><p>Video links open on YouTube, which is governed by Google's privacy policy.</p>
<h2>How we use information</h2><ul><li>To respond to inquiries and deliver requested audits, newsletters or payment links.</li><li>To administer contests and evaluate applications.</li><li>To improve the website and prevent abuse.</li></ul><p>We do not sell personal information.</p>
<h2>Retention & your rights</h2><p>We keep submissions only as long as needed for the purpose they were sent. You can request access, correction or deletion at any time via the <a href="contact.html">contact form</a>. Depending on where you live (e.g., GDPR, UK GDPR, CCPA/CPRA, PIPEDA, Québec Law 25) you may have additional rights.</p>
<h2>Children</h2><p>This site is not directed to children under 13 (or 16 in the EEA), and we do not knowingly collect their data.</p>
<h2>Changes</h2><p>We may update this policy; the date above shows the latest revision.</p></div></section>"""
    simple("privacy.html", "Privacy Policy | 89944 Price Lab", "Privacy policy for 89944.com covering forms, cookies, Google AdSense advertising, opt-out choices and your data rights.",
           "Privacy", "Privacy Policy", "How we collect, use and protect your information.", privacy, "0.3", lead=False)
    terms = f"""<section style="padding-top:0"><div class="wrap prose"><p><i>Last updated: {upd}</i></p>
<h2>Acceptance</h2><p>By using 89944.com you agree to these Terms. If you do not agree, please do not use the site.</p>
<h2>Educational use only</h2><p>Calculators, guides and data are provided for general educational purposes. They are not financial, investment, tax, accounting or legal advice. Results depend on the inputs you provide; always verify important decisions with a qualified professional.</p>
<h2>No warranty</h2><p>The site is provided "as is" without warranties of any kind. We do not guarantee accuracy, completeness or availability.</p>
<h2>Limitation of liability</h2><p>To the fullest extent permitted by law, 89944.com is not liable for any loss arising from use of the site or reliance on its content.</p>
<h2>User submissions</h2><p>You are responsible for content you submit. By submitting contest entries, videos or feedback, you grant us a non-exclusive, worldwide, royalty-free licence to use, display and publish it with attribution.</p>
<h2>Contests</h2><p>Contests are governed by the official rules on the <a href="contests.html">Contests page</a>. No purchase necessary.</p>
<h2>Donations</h2><p>Support payments are voluntary, non-refundable except where required by law, and not tax-deductible.</p>
<h2>Intellectual property</h2><p>Original site content, design and code are © 89944.com. You may link to and share pages; you may not republish content in bulk without permission.</p>
<h2>Third-party links</h2><p>We are not responsible for content on external sites we link to.</p>
<h2>Changes</h2><p>We may update these Terms at any time. Continued use means acceptance.</p></div></section>"""
    simple("terms.html", "Terms of Use | 89944 Price Lab", "Terms of use for 89944.com: educational use, no warranty, limitation of liability, submissions, contests and donations.",
           "Terms", "Terms of Use", "The rules for using 89944.com.", terms, "0.3", lead=False)
    disc = f"""<section style="padding-top:0"><div class="wrap prose"><p><i>Last updated: {upd}</i></p>
<h2>General disclaimer</h2><p>All tools and articles on 89944.com are for informational and educational purposes only and do not constitute professional advice. Example rates, benchmarks and figures are illustrative and may not reflect current market conditions.</p>
<h2>Trademark disclosure</h2><p>"89944" is used on this website solely as a domain name and a descriptive site identifier. We claim no trademark rights in the number 89944 or in any combination of its digits. 89944.com is an independent website and is <b>not affiliated with, endorsed by, sponsored by or connected to</b> any company, brand, product, service, slogan, ZIP/postal code, phone number, model number or other identifier that uses the same or similar numbers — including any well-known product slogans that reference a "99 and 44/100" figure, which are the property of their respective owners.</p>
<p>All product names, logos, brands and trademarks mentioned on this site (including Google, AdSense, YouTube and others) are the property of their respective owners. Their use is for identification and reference only and does not imply endorsement.</p>
<h2>Copyright disclosure</h2><p>© {datetime.date.today().year} 89944.com. Original text, calculators, code and design on this site are protected by copyright. Facts, formulas and public data (such as U.S. government CPI statistics, which are in the public domain) are not claimed as our property. Third-party videos and linked materials remain the property of their creators.</p>
<p>If you believe content on this site infringes your copyright or trademark, please use the <a href="contact.html">contact form</a> with details of the work, its location on our site and your contact information. We respond promptly to valid notices.</p>
<h2>Advertising & affiliate disclosure</h2><p>This site displays advertising via Google AdSense and may feature clearly-labelled sponsorships. Advertisers do not influence calculator outputs or editorial content.</p></div></section>"""
    simple("disclaimer.html", "Disclaimer, Trademark & Copyright Disclosure | 89944", "Disclaimer and trademark/copyright disclosure for 89944.com: independent site, no affiliation with any brand using similar numbers, educational use only.",
           "Disclaimer", "Disclaimer & trademark/copyright disclosure", "Independent, educational and transparent.", disc, "0.3", lead=False)


def glossary():
    terms = [("Anchoring", "Using a reference price (e.g., a crossed-out original or premium tier) to make another price feel reasonable."),
             ("Break-even point", "The sales volume at which total revenue equals total costs."), ("CAC", "Customer acquisition cost — total sales & marketing spend divided by new customers."),
             ("Charm pricing", "Setting prices just below a round number, such as $9.99."), ("Contribution margin", "Price minus variable cost per unit."),
             ("CPI", "Consumer Price Index — a measure of the average change in prices paid by consumers."), ("Decoy effect", "Adding a less attractive option to steer buyers toward a target option."),
             ("Dynamic pricing", "Adjusting prices in real time based on demand, inventory or competitors."), ("Elasticity", "How strongly demand responds to a price change."),
             ("Freemium", "A free tier with paid upgrades."), ("Gross margin", "(Revenue − cost of goods sold) ÷ revenue."), ("Left-digit effect", "The tendency to judge a number mainly by its first digit."),
             ("LTV", "Customer lifetime value — gross profit expected from a customer over their lifetime."), ("Markup", "(Price − cost) ÷ cost."), ("Penetration pricing", "Launching at a low price to win share quickly."),
             ("Prestige pricing", "Using round, higher prices to signal quality."), ("Price skimming", "Launching high and lowering the price over time."), ("Shrinkflation", "Reducing product size while keeping the price the same."),
             ("Token (AI)", "A chunk of text, roughly ¾ of an English word, used to bill LLM usage."), ("Unit price", "Price per standard unit (100 g, litre, item) for fair comparison."),
             ("Value-based pricing", "Setting price according to the value delivered to the customer rather than cost."), ("Van Westendorp", "A survey method that finds an acceptable price range by asking four price questions.")]
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Pricing Glossary", "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in terms]}
    inner = '<section style="padding-top:0"><div class="wrap"><div class="chips" style="margin-bottom:20px">' + "".join(f'<a href="#{t.split()[0].lower()}">{t}</a>' for t, _ in terms) + '</div><div class="grid g2">' + "".join(f'<div class="card" id="{t.split()[0].lower()}"><h3>{t}</h3><p>{d}</p></div>' for t, d in terms) + "</div></div></section>" + ad()
    r = ""
    b = head("Pricing Glossary — 22 Terms Every Seller Should Know | 89944", "Plain-English definitions of pricing terms: charm pricing, anchoring, elasticity, contribution margin, LTV, CAC, shrinkflation, AI tokens and more.", "glossary.html", r, ld)
    b += page_hero("Glossary", "📖 Pricing glossary", "The language of pricing in plain English.", r) + inner + lead_box(r, src="glossary") + foot(r)
    write("glossary.html", b, "0.5")


def notfound():
    r = "/"
    b = head("Page not found | 89944", "The page you're looking for doesn't exist.", "404.html", r)
    b += f'<section class="page-hero center"><div class="wrap"><div class="ptag" style="position:relative;display:inline-block;margin:20px auto"><span class="old">$404.00</span><span class="new">$0.00</span></div><h1>This page is out of stock.</h1><p style="margin:0 auto">Try one of our free tools instead.</p><p class="mt"><a class="btn btn-primary" href="/tools/">Browse tools</a> <a class="btn btn-ghost" href="/">Home</a></p></div></section>'
    b += foot(r)
    write("404.html", b)


def sitemap():
    today = datetime.date.today().isoformat()
    urls = "".join(f"<url><loc>{SITE}/{p.replace('index.html','')}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>" for p, pr in PAGES)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')


if __name__ == "__main__":
    home(); tools_pages(); guides_pages(); inflation(); videos(); audit(); support(); advertise(); contests(); careers(); contact(); about(); legal(); glossary(); notfound(); sitemap()
    print(f"Built {len(PAGES)} pages")
