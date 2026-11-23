# 89944.com: 89944 Price Lab

Free pricing calculators, guides and live inflation data. This is a static site, hosted on GitHub Pages from the root of the `main` branch.

- **Build:** `python3 _build/build.py` regenerates every page and the sitemap. Edit content in `_build/tools.py`, `_build/guides.py` and `_build/build.py`.
- **Data:** `.github/workflows/refresh.yml` runs daily. It refreshes `data/cpi.json` from FRED, falling back to BLS, then rebuilds the site and commits the changes.
- **Forms:** forms are sent through FormSubmit AJAX. The destination inbox is assembled at runtime in `assets/js/app.js` and is never shown in the page source.
- **AdSense:** the head script is on every page, auto ads are enabled, and in-content slots are in place. `ads.txt` is at the site root.
- **Docs:** `PROMPTS.md` (phase-wise build prompts) and `RESEARCH.md` (research and the 25-site audit).

© 89944.com. "89944" is used only as a domain name. The site is not affiliated with any brand that uses similar numbers or slogans.
