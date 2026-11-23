"""Tool page definitions: slug, key, meta, input form, result panel, explainer, faq."""

def f(id, label, val, hint="", step="any", typ="number", extra=""):
    h = f'<div class="hint">{hint}</div>' if hint else ""
    return f'<div class="field"><label for="{id}">{label}</label><input id="{id}" type="{typ}" step="{step}" value="{val}" inputmode="decimal" {extra}>{h}</div>'

def kv(label, id):
    return f'<div class="kv"><span>{label}</span><span id="{id}">—</span></div>'

TOOLS = [
dict(slug="charm-price-calculator", key="charm", icon="🏷️", tag="hot", cat="Pricing",
 name="Charm Price Calculator", short="Turn any price into proven .99, .95, .97 or prestige endings — and see if the left digit drops.",
 title="Charm Price Calculator — Find the Best .99 Price Ending | 89944",
 desc="Free charm pricing calculator. Enter any price and get .99, .95, .97, left-digit-drop and prestige round suggestions with the % change for each.",
 form=f('cp_price', 'Your current or planned price ($)', '20', 'Try 10, 45, 100 or 2000 to see left-digit effects.') +
  '<div class="field"><label for="cp_pos">Brand positioning</label><select id="cp_pos"><option value="value">Value / mass market</option><option value="discount">Discount / promo</option><option value="premium">Premium / luxury / B2B</option></select></div>',
 result='<h3>Recommended price</h3><div class="big-num" id="cp_best">—</div><p class="note" id="cp_why"></p>' + kv('Left digit drops?', 'cp_left') +
  '<table class="data mt"><thead><tr><th>Strategy</th><th>Price</th><th>Change</th></tr></thead><tbody id="cp_rows"></tbody></table>',
 body="""<h2>What is charm pricing?</h2>
<p>Charm pricing means setting a price just below a round number: $9.99 instead of $10, $199 instead of $200. The tiny gap in money creates an outsized gap in perception because shoppers read prices left to right and anchor on the first digit. A study summarised in the <em>Marketing Bulletin</em> found roughly six in ten advertised prices end in 9 — retailers use it because it keeps working.</p>
<h2>How this calculator decides</h2>
<ul><li><strong>Classic .99</strong> — the default for mass-market goods and impulse buys.</li>
<li><strong>.95 ending</strong> — reads slightly friendlier and is common in apparel and groceries.</li>
<li><strong>.97 ending</strong> — many shoppers associate it with clearance, so use it for markdowns.</li>
<li><strong>Left-digit drop</strong> — the biggest psychological jump happens when the first digit changes ($100 → $99.99, $2,000 → $1,999.99).</li>
<li><strong>Prestige round</strong> — whole numbers signal quality; luxury brands, consultants and B2B software often avoid .99 on purpose.</li></ul>
<h2>When <em>not</em> to use .99</h2>
<p>If you sell on trust and quality — fine dining, premium services, enterprise contracts — a charm ending can make you look cheap. Test round pricing there. Charm prices also matter less when the customer compares on a calculated metric (price per unit, price per seat) instead of the headline price.</p>
<h2>Test it, don't guess</h2>
<p>Run an A/B test for two to four weeks with enough traffic to reach significance. Track conversion rate <em>and</em> revenue per visitor: a lower price that converts slightly better can still earn less overall.</p>""",
 faq=[("Does $9.99 really sell better than $10?", "Often yes for consumer goods, because of the left-digit effect. The lift varies by category and audience, so test it on your own store."),
      ("Should SaaS pricing end in 9?", "Self-serve tiers often use $9, $19, $49. Sales-led and enterprise plans usually use round numbers to signal value."),
      ("What about $8.99 vs $9.99?", "Same left digit logic: $8.99 feels like 'eight-something'. Use the tool to compare the margin cost of each step down.")]),

dict(slug="margin-markup-calculator", key="margin", icon="📐", tag="hot", cat="Profit",
 name="Margin & Markup Calculator", short="Convert margin ↔ markup, set a price from a target margin, and stop the most expensive pricing mistake.",
 title="Margin vs Markup Calculator — Price From Target Margin | 89944",
 desc="Free margin and markup calculator. Enter cost and a price, target margin or markup to get selling price, profit, margin % and markup % instantly.",
 form=f('mm_cost', 'Unit cost ($)', '40', 'Include landed cost: product, shipping-in, packaging, payment fees.') +
  '<div class="field"><label for="mm_mode">I know my…</label><select id="mm_mode"><option value="margin">Target margin %</option><option value="markup">Target markup %</option><option value="price">Selling price $</option></select></div>' +
  f('mm_val', 'Value', '40'),
 result='<h3>Selling price</h3><div class="big-num" id="mm_price">—</div>' + kv('Profit per unit', 'mm_profit') + kv('Gross margin', 'mm_margin') + kv('Markup', 'mm_markup') +
  '<table class="data mt"><thead><tr><th>Margin</th><th>= Markup</th><th>Price</th></tr></thead><tbody id="mm_tbl"></tbody></table>',
 body="""<h2>Margin and markup are not the same number</h2>
<p><strong>Markup</strong> is profit divided by <em>cost</em>. <strong>Margin</strong> is profit divided by <em>price</em>. A product that costs $40 and sells for $60 has a 50% markup but only a 33.3% margin. Confusing the two is one of the most common — and most expensive — small-business pricing errors, because a "40% markup" quietly delivers only a 28.6% margin.</p>
<div class="formula">Margin % = (Price − Cost) ÷ Price × 100<br>Markup % = (Price − Cost) ÷ Cost × 100<br>Price from margin = Cost ÷ (1 − Margin)</div>
<h2>Which one should you use?</h2>
<p>Use <strong>margin</strong> for planning and reporting: your income statement, investors and lenders think in margin. Use <strong>markup</strong> on the shop floor when you multiply cost to get a shelf price quickly. Just never mix them in the same conversation.</p>
<h2>Use fully-loaded cost</h2>
<p>Add inbound freight, packaging, payment processing (often 2.5–3.5%), marketplace fees, returns allowance and fulfilment. A healthy-looking markup on raw product cost can become a loss once these are included.</p>""",
 faq=[("Can margin be more than 100%?", "No. Margin is capped below 100% because profit can never exceed the price. Markup has no cap."),
      ("What's a good gross margin?", "It depends on the model: many software businesses run 70–85%, retail often 25–50%, restaurants commonly 60–70% on food cost but far less after labour.")]),

dict(slug="discount-calculator", key="discount", icon="✂️", tag="", cat="Promotions",
 name="Discount Stacker & Profit Check", short="Stack % discounts, coupons and tax — and see how many extra sales a promo needs to break even.",
 title="Stacked Discount Calculator + Promo Profit Check | 89944",
 desc="Calculate stacked discounts (20% + 10% isn't 30%), coupons and sales tax, plus the extra sales volume a promotion needs to keep the same profit.",
 form='<div class="row">' + f('ds_orig', 'Original price ($)', '89.99') + f('ds_tax', 'Sales tax %', '8') + '</div><div class="row">' + f('ds_d1', 'Discount 1 %', '20') + f('ds_d2', 'Discount 2 % (stacked)', '10') + '</div>' + f('ds_coupon', 'Coupon ($ off, applied after %)', '5') + f('ds_cost', 'Seller: your unit cost ($, optional)', '35', 'Fill this to see the promo profit check.'),
 result='<h3>Final price (incl. tax)</h3><div class="big-num" id="ds_final">—</div>' + kv('Before tax', 'ds_pre') + kv('You save', 'ds_save') + kv('Effective discount', 'ds_eff') + kv('Naive sum', 'ds_naive') +
  '<h3 class="mt">Seller profit check</h3>' + kv('Profit / unit before', 'ds_m0') + kv('Profit / unit after', 'ds_m1') + '<p class="note" id="ds_need"></p>',
 body="""<h2>Why 20% + 10% isn't 30%</h2>
<p>Stacked discounts multiply, they don't add. 20% off and then 10% off leaves you paying 0.8 × 0.9 = 72% of the price — a 28% discount, not 30%. Coupons with a fixed dollar amount are usually applied after percentage discounts, and sales tax is calculated on the discounted price in most jurisdictions.</p>
<h2>The seller's hidden cost of a promo</h2>
<p>A discount cuts straight into profit per unit, so you must sell disproportionately more to stand still. If you earn $50 per unit and a promotion cuts that to $25, you need <strong>twice</strong> the units just to earn the same profit. This is why many brands prefer value-adds (free shipping thresholds, bundles, bonus items) over deep percentage cuts.</p>
<div class="formula">Extra volume needed = (Old profit per unit ÷ New profit per unit) − 1</div>
<h2>Better promo patterns</h2>
<ul><li>Bundle a high-margin item with a hero product instead of discounting the hero.</li><li>Use tiered thresholds: "Spend $75, save $10" lifts order value.</li><li>Limit by time and audience — loyalty members, first orders, cart abandoners.</li></ul>""",
 faq=[("Is tax applied before or after a coupon?", "In most U.S. states manufacturer coupons don't reduce the taxable amount but store coupons do. Check your local rules."),
      ("What's a safe promo depth?", "Run the profit check above. If the required extra volume is more than you can realistically sell, the promo destroys value.")]),

dict(slug="break-even-calculator", key="breakeven", icon="⚖️", tag="", cat="Profit",
 name="Break-Even Calculator", short="Units and revenue to cover fixed costs, contribution margin, and units needed for a profit goal — with a chart.",
 title="Break-Even Point Calculator (Units & Revenue) with Chart | 89944",
 desc="Find your break-even point in units and revenue, contribution margin, and how many sales you need to hit a profit target. Free, with a live chart.",
 form=f('be_fixed', 'Fixed costs per month ($)', '8999', 'Rent, salaries, software, insurance…') + '<div class="row">' + f('be_price', 'Price per unit ($)', '44') + f('be_var', 'Variable cost per unit ($)', '18') + '</div>' + f('be_target', 'Profit target per month ($)', '5000'),
 result='<h3>Break-even units</h3><div class="big-num" id="be_units">—</div>' + kv('Break-even revenue', 'be_rev') + kv('Contribution margin / unit', 'be_cm') + kv('Contribution margin ratio', 'be_cmr') + kv('Units for profit target', 'be_target_u') + '<canvas id="be_chart" height="220" style="width:100%;margin-top:16px;background:#fff;border-radius:10px"></canvas>',
 body="""<h2>The break-even formula</h2>
<div class="formula">Break-even units = Fixed costs ÷ (Price − Variable cost per unit)</div>
<p>The denominator is your <strong>contribution margin</strong>: what each sale contributes toward fixed costs after paying for itself. Once fixed costs are covered, every additional unit's contribution margin is profit.</p>
<h2>Three levers to lower break-even</h2>
<ol><li><strong>Raise price</strong> — usually the fastest lever, because it flows 100% to contribution margin.</li><li><strong>Cut variable cost</strong> — negotiate suppliers, reduce packaging, lower payment fees.</li><li><strong>Cut fixed cost</strong> — the slowest lever, but it lowers risk permanently.</li></ol>
<h2>Use it for launches and campaigns</h2>
<p>Treat a marketing campaign's spend as a fixed cost and divide by contribution margin to find how many sales the campaign must drive to pay for itself. That number is your minimum acceptable result before you launch.</p>""",
 faq=[("What counts as a fixed cost?", "Costs that don't change with volume in the short term: rent, base salaries, subscriptions, insurance, loan payments."),
      ("Is break-even the same as payback period?", "No. Break-even is about volume per period; payback is how long it takes to recover an upfront investment.")]),

dict(slug="unit-price-calculator", key="unit", icon="🛒", tag="", cat="Shopping",
 name="Unit Price Comparer", short="Compare up to 4 sizes or brands by price per 100 g, 100 ml or item — find the real best deal.",
 title="Unit Price Calculator — Compare Price per Ounce, Gram, Item | 89944",
 desc="Compare grocery and household products by unit price. Enter price and size in g, kg, oz, lb, ml, L or count to find the cheapest per unit.",
 form='<div id="unitTool">' + ''.join(f'''<div class="up-row panel" style="padding:14px;margin-bottom:10px;box-shadow:none"><div class="row3"><div><label>Name</label><input class="n" value="{n}"></div><div><label>Price ($)</label><input class="p" type="number" step="any" value="{p}"></div><div><label>Size</label><div style="display:flex;gap:6px"><input class="q" type="number" step="any" value="{q}"><select class="u" style="width:90px">{''.join(f'<option{" selected" if u==x else ""}>{x}</option>' for x in ["g","kg","oz","lb","ml","l","floz","ct"])}</select></div></div></div></div>''' for n, p, q, u in [("Small pack", "4.49", "300", "g"), ("Family size", "8.99", "750", "g"), ("Bulk", "15.99", "1.5", "kg"), ("Store brand", "", "", "g")]) + '</div>',
 result='<h3>Best value</h3><div class="big-num" id="up_best">—</div><p class="note" id="up_bestper"></p><table class="data mt"><thead><tr><th>Option</th><th>Unit price</th><th>vs best</th></tr></thead><tbody id="up_rows"></tbody></table>',
 body="""<h2>Why unit price beats sticker price</h2>
<p>Packaging sizes are designed to make comparison hard. "Family size" is not always cheaper per gram, and promotional multi-buys can be worse value than the regular large pack. Unit price — the cost per 100 g, per litre or per item — is the only fair comparison.</p>
<h2>Watch out for shrinkflation</h2>
<p>When a pack shrinks but the price stays the same, the sticker price hides a price increase. Re-check unit prices on products you buy often, and compare against the store brand.</p>
<h2>Tips</h2><ul><li>Bulk only wins if you'll use it before it expires.</li><li>Compare like with like: concentrated detergents need "per load", not per ml.</li><li>Shelf-label unit prices sometimes use different units across products — this tool normalises them.</li></ul>""",
 faq=[("Can I compare ounces with grams?", "Yes. The tool converts weight units (g, kg, oz, lb) and volume units (ml, L, fl oz) to a common base."),
      ("Is bigger always cheaper?", "No — sale prices on small packs often beat regular prices on big packs. That's exactly what this tool catches.")]),

dict(slug="subscription-cost-calculator", key="subs", icon="🔁", tag="new", cat="Shopping",
 name="Subscription Audit", short="Add up every subscription, see the yearly and 5-year cost, and what that money could grow to.",
 title="Subscription Cost Calculator — Audit Your Monthly Subscriptions | 89944",
 desc="List your subscriptions to see monthly, yearly and 5-year totals, plus what the money could grow to if invested instead. Free subscription audit tool.",
 form='<div class="list-rows" id="subs_list"></div><button type="button" class="btn btn-ghost btn-sm" id="subs_add">+ Add subscription</button>' + f('subs_rate', 'Alternative: annual return if invested (%)', '7', 'For illustration only — not investment advice.'),
 result='<h3>Monthly total</h3><div class="big-num" id="subs_month">—</div>' + kv('Active subscriptions', 'subs_count') + kv('Per year', 'subs_year') + kv('Over 5 years', 'subs_5') + kv('Invested for 10 yrs instead', 'subs_fv') + kv('Cutting 30% saves / yr', 'subs_cut'),
 body="""<h2>Subscription creep is real</h2>
<p>Small recurring charges are easy to forget: a streaming service here, a cloud plan there, an app trial that quietly converted. Individually they look like the cost of a coffee; together they can rival a car payment. An audit every quarter keeps them honest.</p>
<h2>The 4-question audit</h2><ol><li>Did I use it in the last 30 days?</li><li>Is there an annual plan that's cheaper (often 15–20% off)?</li><li>Am I paying twice for the same thing (two music services, two cloud drives)?</li><li>Would I sign up again today at this price?</li></ol>
<h2>Rotate, don't hoard</h2><p>For entertainment services, subscribe to one at a time, binge what you want, cancel, and rotate to the next. You keep the content and cut the cost by half or more.</p>""",
 faq=[("How do I find all my subscriptions?", "Search your card and bank statements for recurring charges, and check the subscription settings in your phone's app store account."),
      ("Are annual plans worth it?", "Only for services you're certain to use all year. Otherwise monthly gives you the option to cancel.")]),

dict(slug="ai-api-cost-calculator", key="ai", icon="🤖", tag="hot", cat="AI & SaaS",
 name="AI API Cost & Pricing Calculator", short="Estimate LLM token costs per request, per user and per month — then get a price that protects your margin.",
 title="AI API Cost Calculator — LLM Token Cost & SaaS Pricing | 89944",
 desc="Estimate AI/LLM API costs from input and output tokens, requests per day and cache rate, then calculate a per-user price that hits your target gross margin.",
 form='<div class="field"><label>Rate preset (example tiers — always check your provider\'s current price list)</label><div class="seg" id="ai_presets"><button type="button" data-i="0.15" data-o="0.6">Budget tier</button><button type="button" data-i="3" data-o="15" class="on">Mid tier</button><button type="button" data-i="15" data-o="75">Premium tier</button></div></div>' +
  '<div class="row">' + f('ai_pin', 'Price per 1M input tokens ($)', '3') + f('ai_pout', 'Price per 1M output tokens ($)', '15') + '</div><div class="row">' + f('ai_tin', 'Input tokens per request', '1500') + f('ai_tout', 'Output tokens per request', '500') + '</div><div class="row">' + f('ai_req', 'Requests per day (total)', '5000') + f('ai_cache', 'Cached input share %', '30', 'Cached input billed at ~10% in this model.') + '</div><div class="row">' + f('ai_users', 'Paying users', '400') + f('ai_margin', 'Target gross margin %', '80') + '</div>',
 result='<h3>Monthly API cost</h3><div class="big-num" id="ai_mon">—</div>' + kv('Cost per request', 'ai_per') + kv('Per day', 'ai_day') + kv('Per year', 'ai_year') + kv('AI cost per user / mo', 'ai_peruser') + kv('Price for target margin', 'ai_price') + kv('Suggested charm price', 'ai_charm') + '<p class="note">Rates are user-editable examples. Real costs vary by model, provider, region and discounts.</p>',
 body="""<h2>How AI products are billed</h2>
<p>Most large-language-model APIs charge per token, with separate rates for <strong>input</strong> (your prompt, context and documents) and <strong>output</strong> (the model's reply). Output tokens usually cost several times more than input tokens. Many providers also discount cached or repeated input and offer cheaper batch processing.</p>
<div class="formula">Cost per request = (input tokens × input rate + output tokens × output rate) ÷ 1,000,000</div>
<h2>Price on value, floor on cost</h2>
<p>Your AI cost per user sets the <em>floor</em>; customer value sets the <em>ceiling</em>. Software buyers expect SaaS-like gross margins, so many AI startups target 60–80% after model costs. If the tool shows you can't hit that at a price customers accept, you have four levers: smaller models for easy tasks, aggressive caching, shorter outputs, or usage-based pricing above a fair-use cap.</p>
<h2>Pricing models that work for AI</h2><ul><li><strong>Seat + fair-use cap</strong> — predictable for buyers; protects you from power users.</li><li><strong>Credits</strong> — prepaid usage that maps to your token cost.</li><li><strong>Outcome-based</strong> — charge per resolved ticket, document or lead; captures value directly.</li></ul>""",
 faq=[("How many tokens is a word?", "In English, a common rule of thumb is roughly 0.75 words per token (about 4 characters). Code and other languages vary."),
      ("Why are my real costs higher than the estimate?", "Hidden tokens: system prompts, chat history re-sent every turn, retrieved documents and retries. Measure real token counts from your logs and plug them in.")]),

dict(slug="freelance-rate-calculator", key="freelance", icon="🧑‍💻", tag="", cat="Services",
 name="Freelance Hourly Rate Calculator", short="Work back from your target income, taxes, expenses and real billable hours to a rate that actually pays.",
 title="Freelance Rate Calculator — What Hourly Rate Should I Charge? | 89944",
 desc="Calculate your freelance or consulting hourly rate from target income, business expenses, taxes, time off and billable utilisation. Includes day and retainer rates.",
 form=f('fr_income', 'Target take-home income / year ($)', '85000') + f('fr_exp', 'Business expenses / year ($)', '9000', 'Software, hardware, insurance, accounting, health cover…') + '<div class="row">' + f('fr_tax', 'Effective tax rate %', '28') + f('fr_hours', 'Working hours / week', '40') + '</div><div class="row">' + f('fr_weeks', 'Weeks off / year', '6') + f('fr_bill', 'Billable share of time %', '65', 'Sales, admin and learning are unbillable.') + '</div>',
 result='<h3>Minimum hourly rate</h3><div class="big-num" id="fr_rate">—</div>' + kv('Day rate (8h)', 'fr_day') + kv('Gross revenue needed', 'fr_gross') + kv('Billable hours / year', 'fr_hrs') + '<p class="note" id="fr_charm"></p><p class="note" id="fr_retainer"></p>',
 body="""<h2>Why freelancers undercharge</h2>
<p>Most people divide their old salary by 2,080 hours. But freelancers pay their own taxes, benefits and tools, take unpaid time off, and spend a third or more of their time on sales and admin. The result: a rate that looks fine but produces a salary far below target.</p>
<div class="formula">Rate = (Income + Expenses) ÷ (1 − Tax rate) ÷ (Hours/week × Working weeks × Billable %)</div>
<h2>Then price above the minimum</h2><p>This calculator gives you a <strong>floor</strong>. Move toward value-based pricing — per project, per outcome or on retainer — as soon as you can estimate the value you deliver. A website that brings a client $200,000 a year is not worth "40 hours × rate".</p>""",
 faq=[("Should I show my hourly rate?", "Many consultants quote per project instead, so clients judge the outcome rather than the hours."),
      ("How often should I raise my rate?", "Review at least yearly, and for every new client once your calendar is consistently full.")]),

dict(slug="price-increase-calculator", key="increase", icon="📈", tag="new", cat="Pricing",
 name="Price Increase Impact Calculator", short="How many customers can you lose after a price rise and still make more profit? Find out before you announce it.",
 title="Price Increase Calculator — Customers You Can Lose & Still Profit | 89944",
 desc="Model a price increase: how many customers or units you can lose before profit falls, plus expected profit using a price-elasticity estimate.",
 form='<div class="row">' + f('pi_price', 'Current price ($)', '44') + f('pi_var', 'Variable cost / unit ($)', '20') + '</div><div class="row">' + f('pi_units', 'Units sold / month', '1000') + f('pi_inc', 'Planned increase %', '10') + '</div>' + f('pi_el', 'Price elasticity estimate', '1.2', 'Rough guide: 0.5 = loyal/necessity, 1 = average, 2+ = very price sensitive.'),
 result='<h3>You can lose up to</h3><div class="big-num" id="pi_loss">—</div><p class="note">…and still earn the same profit.</p>' + kv('New price', 'pi_np') + kv('Units needed for same profit', 'pi_need') + kv('Profit now / mo', 'pi_op') + kv('Expected profit after', 'pi_ep') + kv('Change', 'pi_delta'),
 body="""<h2>Price increases are asymmetric</h2>
<p>Because a price increase flows straight to profit per unit, you can usually afford to lose more customers than you'd expect. At a 54% contribution margin, a 10% price increase can absorb roughly a 16% drop in volume before profit falls.</p>
<div class="formula">Max volume loss = 1 − (Old contribution ÷ New contribution)</div>
<h2>How to raise prices without a revolt</h2><ol><li>Give notice (30 days is common) and explain what improved.</li><li>Grandfather loyal customers for a period, or offer an annual lock-in at the old rate.</li><li>Add value alongside the increase — a feature, faster delivery, better support.</li><li>Raise for new customers first and measure conversion before touching existing ones.</li></ol>""",
 faq=[("What is price elasticity?", "The % change in quantity demanded for a 1% change in price. An elasticity of 1.2 means a 10% price rise is expected to reduce volume by about 12%."),
      ("Where do I get my elasticity?", "From past price changes, A/B tests, or surveys like Van Westendorp. If unsure, model a range (0.5–2).")]),

dict(slug="saas-ltv-cac-calculator", key="saas", icon="🧮", tag="", cat="AI & SaaS",
 name="SaaS LTV : CAC Calculator", short="Customer lifetime value, LTV:CAC ratio and CAC payback months — with a plain-English verdict.",
 title="LTV to CAC Ratio Calculator & CAC Payback for SaaS | 89944",
 desc="Calculate customer lifetime value, LTV:CAC ratio, CAC payback period and average customer lifetime from ARPU, gross margin, churn and acquisition cost.",
 form='<div class="row">' + f('sa_arpu', 'ARPU — revenue per customer / month ($)', '49') + f('sa_gm', 'Gross margin %', '78') + '</div><div class="row">' + f('sa_churn', 'Monthly churn %', '3') + f('sa_cac', 'Customer acquisition cost ($)', '390') + '</div>',
 result='<h3>Lifetime value (LTV)</h3><div class="big-num" id="sa_ltv">—</div>' + kv('LTV : CAC', 'sa_ratio') + kv('CAC payback', 'sa_pb') + kv('Avg customer lifetime', 'sa_life') + '<p class="note" id="sa_verdict"></p>',
 body="""<h2>The two numbers investors check first</h2>
<div class="formula">LTV = ARPU × Gross margin ÷ Monthly churn<br>CAC payback (months) = CAC ÷ (ARPU × Gross margin)</div>
<p>A common rule of thumb is LTV:CAC of at least 3:1 and payback under 12 months for SMB-focused SaaS. Below 1:1 you lose money on every customer you acquire.</p>
<h2>Pricing is the fastest LTV lever</h2><p>Reducing churn is slow work; raising ARPU through better packaging, annual plans and add-ons often moves LTV within a single quarter. Use the <a href="price-increase-calculator.html">price increase calculator</a> to check the downside first.</p>""",
 faq=[("Should I use revenue or margin in LTV?", "Margin. Revenue-based LTV overstates value, especially for AI products with significant model costs."),
      ("What churn should I use?", "Logo churn for customer counts; for LTV, net revenue churn is more accurate if you have expansion revenue.")]),
]
