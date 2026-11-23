# 89944.com: phase-wise build prompts

Concept: **89944 Price Lab**, a pricing-intelligence hub built around the digits "8 · 99 · 44". The 99 ending is the most common price ending in retail. The site offers free calculators, original guides, live inflation data, a B2B lead funnel (free pricing audits), sponsorships, donations, contests and hiring.

Each phase below is a self-contained prompt. Run them in order to rebuild the site, or to extend it.

---

## Phase 1: Research and positioning
> Research the number "89944" and the patterns inside it ("8", "99", "44", "8.99", "99.44") across commerce, business, AI, the economy and people. Identify trademark risks, including P&G Ivory's "99 and 44/100% pure" slogan, which must be avoided. Pick the website concept with the highest AdSense RPM and lead value that the domain can credibly own. Output: the concept, target audiences, revenue model and a list of 25 benchmark sites with their key features.

**Decision:** pricing calculators and price psychology. This niche has high commercial intent and attracts advertisers in finance, SaaS and e-commerce. B2B pricing audits make a valuable lead product.

## Phase 2: Information architecture and design system
> Design a static, GitHub-Pages-compatible site for 89944.com titled "89944 Price Lab". Use a "price tag" visual identity: ink black (#14110f), receipt cream (#fbf7ef) and tag orange (#ff5a1f). Fonts: Space Grotesk for display, Inter for body, JetBrains Mono for numbers. Support dark mode.
>
> Navigation: Tools, Guides, Price Machine, Videos, Contests, Free Audit, Support.
>
> Every page carries:
> - a top bar reading "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linked to web.works/contact (the URL is set at runtime and never shown as text);
> - the AdSense head script for ca-pub-6620975821265271;
> - a cookie consent banner;
> - a footer with legal links and a trademark notice.

## Phase 3: Calculators (vanilla JS, no backend)
> Build 11 instant, private, client-side tools, each on its own SEO page:
> 1. Charm price calculator
> 2. Margin and markup calculator
> 3. Stacked discount calculator with a promo profit check
> 4. Break-even calculator with a canvas chart
> 5. Unit price comparer with unit normalisation
> 6. Subscription audit
> 7. AI API token cost calculator with margin-based pricing
> 8. Freelance rate calculator
> 9. Price increase impact calculator
> 10. SaaS LTV:CAC calculator
> 11. Inflation "Price Machine" using CPI data
>
> Each tool page needs:
> - an input panel and a sticky results panel;
> - the formula shown on the page;
> - an original explainer of 300+ words;
> - a FAQ with FAQPage schema;
> - related tools;
> - a lead capture box.

## Phase 4: Original content for AdSense approval
> Write 8 original long-form guides of 600–900 words each, with table-of-contents anchors, Article schema, one mid-article ad slot, a tool call-to-action and an educational disclaimer. Topics:
> - charm pricing
> - margin vs markup
> - pricing AI products
> - discounts
> - unit pricing
> - raising prices
> - subscription creep
> - freelance pricing
>
> Also add a glossary of 22 terms with DefinedTermSet schema, plus About, Privacy, Terms and Disclaimer pages. The Privacy page must include the required Google advertising-cookie disclosures and opt-out links. The Disclaimer must include the trademark/copyright disclosure for "89944". Avoid thin, duplicate or scraped content.

## Phase 5: Monetisation and conversion
> Add:
> - **Lead generation:** a 3-step free pricing audit form (business type and revenue, then challenges, then contact details and consent). Add an inline audit box on every page, an exit-intent checklist modal shown once per session on desktop, and newsletter capture.
> - **Support:** donation tiers ($8.99 / $44 / $99) and a pledge form whose purpose can be operations, prizes, hiring or promotion.
> - **Advertise:** sponsorship packages and a media-kit request form.
> - **Contests:** "The $8.99 Challenge" with a countdown, prizes ($89.44 / $44 / $8.99), judging criteria and official rules (no purchase necessary).
> - **Careers:** 6 remote roles and an application form.
> - **Videos:** curated topic cards that open YouTube, plus a creator submission form.
>
> All forms post through FormSubmit AJAX to a single inbox. The email address is assembled at runtime from encoded fragments, so it never appears in the HTML, JS or sitemap as plain text.

## Phase 6: SEO, performance and compliance
> Add:
> - canonical tags, Open Graph tags and a 1200×630 OG image;
> - WebSite, FAQPage, Article and WebApplication JSON-LD;
> - sitemap.xml, robots.txt and ads.txt (`google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0`);
> - CNAME, .nojekyll, a 404 page and a web manifest;
> - lazy, privacy-friendly embeds and support for reduced motion.
>
> Requirements: no layout overflow at 390px width, every sponsored item labelled, and no deceptive ad placement next to buttons.

## Phase 7: Automation
> Add a GitHub Actions workflow that runs daily and on push. It should:
> 1. refresh `data/cpi.json` from FRED (series CPIAUCNS), falling back to the BLS public API;
> 2. rebuild every page (dates and sitemap) with `_build/build.py`;
> 3. commit any changes.
>
> GitHub Pages then serves the main branch from the root folder.

## Phase 8: Deploy and grow
> Push to webworksa1/89944-com, enable GitHub Pages (main branch, root) and point the 89944.com DNS records:
> - A records: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
> - CNAME: www → webworksa1.github.io
>
> Then enforce HTTPS, submit the sitemap to Google Search Console and apply for AdSense once the domain resolves.
>
> Growth roadmap:
> - one new calculator a month (candidates: shipping cost, tip and split, sales tax/VAT, Van Westendorp survey, bundle builder);
> - a weekly Price Letter issue;
> - backlinks from contest entries and creator features.
