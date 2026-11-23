"""Shared layout for 89944.com static pages."""
import json, html as H

SITE = "https://89944.com"
BRAND = "89944 Price Lab"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'

NAV = [
    ("tools/index.html", "Tools"),
    ("guides/index.html", "Guides"),
    ("inflation.html", "Price Machine"),
    ("videos.html", "Videos"),
    ("contests.html", "Contests"),
    ("audit.html", "Free Audit"),
    ("support.html", "Support"),
]


def head(title, desc, path, root, extra_ld=None, tool=None):
    url = f"{SITE}/{path}".replace("/index.html", "/")
    ld = [{
        "@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE + "/",
        "potentialAction": {"@type": "SearchAction", "target": SITE + "/tools/?q={q}", "query-input": "required name=q"}
    }]
    if extra_ld:
        ld.append(extra_ld)
    ldj = "\n".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in ld)
    t = H.escape(title)
    d = H.escape(desc)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#ff5a1f">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
{ADSENSE}
{ldj}
</head>
<body data-root="{root}"{f' data-tool="{tool}"' if tool else ''}>
<a class="skip" href="#main">Skip to content</a>
<div class="owner-bar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a data-owner-link href="{root}contact.html">Contact us →</a></div>
<header class="site-header">
 <div class="wrap nav">
  <a class="logo" href="{root}index.html" aria-label="{BRAND} home"><span class="tagmark">8·99·44</span><span>Price Lab<small>price smarter</small></span></a>
  <ul class="menu" id="menu">{''.join(f'<li><a href="{root}{h}">{n}</a></li>' for h, n in NAV)}</ul>
  <div class="nav-cta">
   <button class="icon-btn" id="themeToggle" aria-label="Toggle dark mode">◐</button>
   <a class="btn btn-primary btn-sm" href="{root}audit.html">Get a free audit</a>
   <button class="icon-btn burger" id="burger" aria-label="Open menu" aria-expanded="false">☰</button>
  </div>
 </div>
</header>
<main id="main">
"""


def ad(label=True):
    """Responsive in-content ad container (Auto ads also enabled via head script)."""
    return ('<div class="wrap ad-slot">' + ('<div class="ad-label">Advertisement</div>' if label else '') +
            '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6620975821265271" data-ad-format="auto" data-full-width-responsive="true"></ins>'
            '<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div>')


def lead_box(root, heading="Is your pricing leaving money on the table?", sub=None, src="inline"):
    sub = sub or "Get a free, no-obligation pricing audit. A pricing analyst reviews your offer, price points, discounts and packaging — and sends back 3 specific changes you can test this month."
    return f"""
<section><div class="wrap"><div class="lead-box">
 <div>
  <span class="eyebrow" style="background:rgba(255,255,255,.1);color:#f5b700">Free · 48-hour turnaround</span>
  <h2>{heading}</h2>
  <p>{sub}</p>
  <ul><li>Price-point & charm-ending review</li><li>Discount and promo leak check</li><li>Tier / bundle / subscription recommendations</li><li>AI & SaaS cost-to-price sanity check</li></ul>
 </div>
 <form class="panel" data-send data-subject="Quick audit request ({src})" data-ga="{src}" data-ok="Request received! Expect your audit within 48 hours.">
  <h3>Claim your free audit</h3>
  <div class="field"><label for="lb_name_{src}">Name</label><input id="lb_name_{src}" name="name" required autocomplete="name"></div>
  <div class="field"><label for="lb_email_{src}">Work email</label><input id="lb_email_{src}" type="email" name="email" required autocomplete="email"></div>
  <div class="field"><label for="lb_url_{src}">Website or store URL</label><input id="lb_url_{src}" name="website" placeholder="https://"></div>
  <div class="field"><label for="lb_type_{src}">What do you sell?</label><select id="lb_type_{src}" name="business_type" required><option value="">Choose…</option><option>E-commerce / DTC products</option><option>SaaS / software</option><option>AI product or API</option><option>Services / agency / freelance</option><option>Restaurant / local retail</option><option>Courses / digital products</option><option>Other</option></select></div>
  <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="btn btn-primary btn-block" type="submit">Send me my free audit →</button>
  <div class="trust"><span>🔒 No spam</span><span>✓ No credit card</span><span>⏱ 48h</span></div>
 </form>
</div></div></section>"""


def foot(root):
    return f"""</main>
<footer class="site-footer">
 <div class="wrap">
  <div class="foot-grid">
   <div>
    <a class="logo" href="{root}index.html" style="color:#fff"><span class="tagmark">8·99·44</span><span>Price Lab</span></a>
    <p style="margin-top:14px;font-size:.92rem">Free pricing calculators, guides and data for founders, sellers, freelancers and smart shoppers.</p>
    <form class="news-form" data-send data-subject="Newsletter signup" data-ok="You're in! Watch your inbox for The Price Letter.">
     <input type="email" name="email" placeholder="Your email" required aria-label="Email for newsletter">
     <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
     <button class="btn btn-primary btn-sm" type="submit">Join</button>
    </form>
    <p style="font-size:.8rem;margin-top:6px">The Price Letter · weekly · unsubscribe anytime</p>
   </div>
   <div><h4>Tools</h4><ul>
    <li><a href="{root}tools/charm-price-calculator.html">Charm price</a></li>
    <li><a href="{root}tools/margin-markup-calculator.html">Margin & markup</a></li>
    <li><a href="{root}tools/break-even-calculator.html">Break-even</a></li>
    <li><a href="{root}tools/ai-api-cost-calculator.html">AI API cost</a></li>
    <li><a href="{root}tools/index.html">All tools →</a></li></ul></div>
   <div><h4>Learn</h4><ul>
    <li><a href="{root}guides/index.html">Pricing guides</a></li>
    <li><a href="{root}inflation.html">Price Machine</a></li>
    <li><a href="{root}videos.html">Videos</a></li>
    <li><a href="{root}glossary.html">Glossary</a></li></ul></div>
   <div><h4>Get involved</h4><ul>
    <li><a href="{root}audit.html">Free pricing audit</a></li>
    <li><a href="{root}support.html">Support / donate</a></li>
    <li><a href="{root}advertise.html">Advertise & sponsor</a></li>
    <li><a href="{root}contests.html">Contests & prizes</a></li>
    <li><a href="{root}careers.html">Careers</a></li></ul></div>
   <div><h4>Company</h4><ul>
    <li><a href="{root}about.html">About</a></li>
    <li><a href="{root}contact.html">Contact</a></li>
    <li><a href="{root}privacy.html">Privacy</a></li>
    <li><a href="{root}terms.html">Terms</a></li>
    <li><a href="{root}disclaimer.html">Disclaimer & trademarks</a></li></ul></div>
  </div>
  <div class="legal">
   <p>© <span data-year>2026</span> 89944.com. All rights reserved. Calculators and content are for educational purposes and are not financial, tax or legal advice.
   "89944" is used here only as a domain name; no trademark rights in the number are claimed, and this site is not affiliated with, endorsed by or sponsored by any company, brand or product that uses similar numbers or slogans. All third-party trademarks belong to their respective owners. <a href="{root}disclaimer.html">Full disclosure</a>.</p>
  </div>
 </div>
</footer>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent">
 <p>We use cookies for essential features, analytics and to show ads (including personalised ads from Google). See our <a href="{root}privacy.html">Privacy Policy</a>.</p>
 <button class="btn btn-primary btn-sm" data-consent="all">Accept</button> <button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button>
</div>
<div class="modal" id="leadModal" aria-hidden="true"><div class="panel">
 <button class="close" data-close aria-label="Close">×</button>
 <span class="eyebrow">Before you go</span>
 <h3>Get the 9-point Pricing Checklist</h3>
 <p class="muted">The exact checklist we use in pricing audits — free, plus The Price Letter weekly.</p>
 <form data-send data-subject="Checklist request (exit intent)" data-ga="exit" data-ok="Sent! Check your inbox shortly.">
  <div class="field"><input type="email" name="email" placeholder="you@company.com" required aria-label="Email"></div>
  <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="btn btn-primary btn-block" type="submit">Send me the checklist</button>
 </form>
</div></div>
<script src="{root}assets/js/app.js" defer></script>
</body>
</html>
"""
