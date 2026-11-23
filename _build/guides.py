"""Original long-form guides."""

GUIDES = [
dict(slug="why-prices-end-in-99", icon="🧠", cat="Psychology", mins=7,
 title="Why Prices End in .99: The Psychology Behind Charm Pricing",
 desc="How the left-digit effect, price-image signals and reference prices make $9.99 outsell $10 — and when round prices win instead.",
 tool="charm-price-calculator",
 body="""<p>Walk into almost any store and you will see the same thing: $4.99, $19.99, $899. Prices that end in 9 are so common that most shoppers stop noticing them. That's exactly why they work. This guide explains the three mechanisms behind charm pricing, the evidence for it, and the situations where it backfires.</p>
<h2 id="left-digit">1. The left-digit effect</h2>
<p>We read numbers left to right and we are lazy about it. When you glance at $2.99, your brain encodes "two dollars and something" before it processes the rest. The first digit acts as an anchor, so $2.99 is perceived as much closer to $2 than to $3 — even though it is a penny away from $3.</p>
<p>The effect is strongest when the leftmost digit changes. Going from $3.00 to $2.99 changes the anchor from 3 to 2. Going from $3.60 to $3.59 changes nothing that matters. That's why the calculator on this site flags whether your charm price actually drops the left digit.</p>
<h2 id="price-image">2. Price image: 9 means "deal"</h2>
<p>Decades of exposure have taught shoppers that prices ending in 9 usually signal a sale or a value-focused retailer. The ending itself carries meaning. A widely cited mail-order experiment found that a women's clothing item sold better at $39 than at either $34 or $44 — the 9-ending beat a <em>lower</em> price. The ending signalled "good deal" more strongly than the actual price difference did.</p>
<h2 id="frequency">3. How common is it?</h2>
<p>Very. Research reported in the <em>Marketing Bulletin</em> found that roughly 60% of advertised prices end in 9, about 30% end in 5, and only around 7% end in 0. When a pricing convention is that universal, deviating from it is itself a signal.</p>
<h2 id="when-round">When round prices win</h2>
<p>Round prices — $100, $2,000, $50 — feel complete, confident and premium. They are processed fluently, which people associate with feeling right. Use them when:</p>
<ul><li>You sell on quality or status (luxury goods, fine dining, premium services).</li><li>The purchase is emotional rather than analytical (gifts, experiences).</li><li>You sell B2B or high-ticket services, where .99 can look like a retail gimmick.</li><li>You want to simplify mental math, for example in subscription tiers or bundles.</li></ul>
<h2 id="variants">.99 vs .95 vs .97</h2>
<p>Within charm pricing, the specific ending also signals something. <strong>.99</strong> is the classic everyday price. <strong>.95</strong> feels slightly softer and is common in apparel and grocery. <strong>.97</strong> and <strong>.98</strong> are used by some big-box retailers internally to mark clearance or manager markdowns, and deal hunters know it. Pick an ending and use it consistently so shoppers learn what your prices mean.</p>
<h2 id="online">Does it still work online?</h2>
<p>Yes, with nuance. On comparison sites and marketplaces, shoppers sort by price, so a $19.99 product lists below a $20 product — a practical advantage on top of the psychological one. But when buyers compare on a calculated metric (price per seat, price per kilogram, cost per month) the headline ending matters less than the metric.</p>
<h2 id="test">How to test it properly</h2>
<ol><li>Pick one high-traffic product and two price points (e.g., $49 vs $49.99, or $50 vs $49).</li><li>Split traffic randomly, not by day of week.</li><li>Measure revenue per visitor, not just conversion rate.</li><li>Run until you have statistical confidence — usually at least a few hundred conversions per variant.</li></ol>
<blockquote>Bottom line: charm pricing is a reliable default for value-positioned, impulse and comparison-shopped products. Round pricing is the better choice when your brand sells quality, confidence or simplicity.</blockquote>"""),

dict(slug="margin-vs-markup", icon="📐", cat="Profit", mins=6,
 title="Margin vs Markup: The Pricing Mistake That Quietly Kills Profit",
 desc="Clear definitions, formulas, a conversion table and real examples showing why a 40% markup is only a 28.6% margin.",
 tool="margin-markup-calculator",
 body="""<p>Ask ten small-business owners what margin they make and you'll get ten answers — and at least a few of them will actually be quoting markup. The two numbers describe the same profit from different angles, and confusing them can wipe out your planned profit without anyone noticing.</p>
<h2 id="definitions">The definitions</h2>
<p><strong>Markup</strong> compares profit to <em>cost</em>. <strong>Margin</strong> compares profit to <em>selling price</em>. Same dollars of profit, different denominator.</p>
<div class="formula">Markup = (Price − Cost) ÷ Cost<br>Margin = (Price − Cost) ÷ Price</div>
<p>Example: you buy a lamp for $40 and sell it for $60. Profit is $20. Markup is $20 ÷ $40 = 50%. Margin is $20 ÷ $60 = 33.3%.</p>
<h2 id="trap">The trap</h2>
<p>Suppose your business plan needs a 40% gross margin to cover rent, staff and marketing. A new employee prices products at "cost plus 40%". That's a 40% <em>markup</em>, which gives a 28.6% <em>margin</em>. You're 11.4 percentage points short on every sale — and the shortfall shows up only months later in the accounts.</p>
<h2 id="table">Quick conversion table</h2>
<table class="data"><thead><tr><th>Margin</th><th>Equivalent markup</th></tr></thead><tbody>
<tr><td>20%</td><td>25%</td></tr><tr><td>25%</td><td>33.3%</td></tr><tr><td>33.3%</td><td>50%</td></tr><tr><td>40%</td><td>66.7%</td></tr><tr><td>50%</td><td>100%</td></tr><tr><td>60%</td><td>150%</td></tr><tr><td>75%</td><td>300%</td></tr></tbody></table>
<div class="formula">Markup = Margin ÷ (1 − Margin) &nbsp;·&nbsp; Margin = Markup ÷ (1 + Markup)</div>
<h2 id="cost">Get the cost right first</h2>
<p>Both numbers are only as good as the cost you plug in. Use <strong>landed cost</strong>: purchase price plus inbound shipping, duties, packaging, payment processing and an allowance for returns and damage. For services, include the fully-loaded cost of the hours delivered, not just wages.</p>
<h2 id="which">Which one should your team use?</h2>
<p>Standardise on margin for targets and reporting — that's how your accountant, lender and investors think. If your staff price with markup for speed, give them a cheat sheet that converts your target margin into the correct markup multiplier. Or simply link them to the calculator on this site.</p>
<h2 id="benchmarks">Typical gross margins by model</h2>
<p>Ranges vary widely, but as rough orientation: software businesses often operate at 70–85% gross margin, specialty retail and DTC brands at 40–60%, grocery at much lower levels, and AI-heavy products somewhere in between depending on model costs. Compare yourself with businesses that share your cost structure, not with the average.</p>"""),

dict(slug="how-to-price-an-ai-product", icon="🤖", cat="AI & SaaS", mins=8,
 title="How to Price an AI Product (Without Losing Money on Power Users)",
 desc="Token economics, gross-margin targets, and the five pricing models that work for AI apps and APIs — with a worked example.",
 tool="ai-api-cost-calculator",
 body="""<p>Traditional software has near-zero marginal cost: one more user barely changes your bill. AI products are different. Every request calls a model, and every model call costs money. Price an AI product like classic SaaS and your heaviest users can turn your best customers into your biggest losses.</p>
<h2 id="cost">Step 1: Know your cost per request</h2>
<p>Model APIs typically bill per token — roughly a word fragment — with separate rates for input and output. Your real input includes far more than the user's message: the system prompt, conversation history, retrieved documents and tool results are all sent with every call. Measure actual token counts from logs rather than estimating from the visible text.</p>
<div class="formula">Cost per request = (input tokens × input rate + output tokens × output rate) ÷ 1,000,000</div>
<h2 id="distribution">Step 2: Look at the distribution, not the average</h2>
<p>AI usage is usually heavily skewed: a small share of users generates a large share of requests. Plot cost per user per month and look at the 90th and 99th percentiles. Your pricing must survive those users, not just the median one.</p>
<h2 id="margin">Step 3: Set a gross-margin target</h2>
<p>Buyers and investors judge software businesses on gross margin. Many AI companies aim for 60–80% after model costs. Work backwards: if the 90th-percentile user costs $6 a month in API fees and you target 75% margin, that user's plan needs to be at least $24.</p>
<h2 id="models">Step 4: Pick a pricing model</h2>
<ol>
<li><strong>Flat seat price with a fair-use cap.</strong> Simple for buyers. Add a soft limit and an overage or upgrade path for power users.</li>
<li><strong>Tiered plans by usage.</strong> Starter, Pro and Business tiers with increasing request or credit allowances.</li>
<li><strong>Credits.</strong> Users prepay for credits that map to your costs. Transparent and margin-safe, but adds friction.</li>
<li><strong>Usage-based (metered).</strong> Pay per request, per document or per minute. Fits APIs and developer tools.</li>
<li><strong>Outcome-based.</strong> Charge per resolved ticket, qualified lead or completed task. Captures value directly and is increasingly popular for AI agents.</li></ol>
<h2 id="cut-costs">Step 5: Engineer the cost down</h2>
<ul><li><strong>Route by difficulty:</strong> send simple tasks to a smaller, cheaper model.</li><li><strong>Cache:</strong> reuse long, repeated prompts; many providers discount cached input heavily.</li><li><strong>Trim context:</strong> summarise long histories instead of resending them.</li><li><strong>Cap output length:</strong> output tokens are typically the most expensive.</li><li><strong>Batch:</strong> non-urgent jobs can often run at a discount.</li></ul>
<h2 id="example">Worked example</h2>
<p>An AI writing tool averages 1,500 input and 500 output tokens per request. At example mid-tier rates of $3 and $15 per million tokens, each request costs about $0.012. With 5,000 requests a day across 400 paying users, monthly API spend is roughly $1,820, or about $4.56 per user (before any caching discount). At an 80% margin target the plan needs to be about $23 — so a $24 or $29 plan works, a $9 plan doesn't. Plug your own numbers into the calculator to check.</p>
<blockquote>Rule of thumb: cost sets your floor, value sets your ceiling, and usage limits protect the space between them.</blockquote>"""),

dict(slug="discounts-without-killing-profit", icon="✂️", cat="Promotions", mins=6,
 title="How to Run Discounts Without Killing Your Profit",
 desc="The math of promotions, why 20% off can require 67% more sales, and smarter alternatives like bundles and thresholds.",
 tool="discount-calculator",
 body="""<p>Discounts are the easiest growth lever to pull and the hardest to undo. Done well, they clear inventory, win new customers and lift order value. Done badly, they train customers to wait for sales and quietly hand your profit to people who would have paid full price anyway.</p>
<h2 id="math">The math nobody checks</h2>
<p>Say a product sells for $100, costs $50 and earns $50 profit per unit. Run a 20% discount and you earn $30 per unit. To make the same total profit you now need 50 ÷ 30 = 1.67 times the volume — <strong>67% more sales</strong>. At 30% off you need double. Very few promotions deliver that lift.</p>
<div class="formula">Required sales lift = Old profit per unit ÷ New profit per unit − 1</div>
<h2 id="stacking">Stacking discounts</h2>
<p>Percentages multiply. 20% off plus an extra 10% is 28%, not 30%. Fixed-dollar coupons hit low-priced items much harder in percentage terms, so set minimum order values on them.</p>
<h2 id="alternatives">Better than a straight discount</h2>
<ul><li><strong>Free-shipping thresholds:</strong> set the threshold 20–30% above your average order value.</li><li><strong>Bundles:</strong> pair a hero product with a high-margin accessory at a combined price.</li><li><strong>Gift with purchase:</strong> a perceived value of $20 that costs you $4.</li><li><strong>Tiered offers:</strong> "Save $10 on $75, $25 on $150."</li><li><strong>Loyalty pricing:</strong> reward repeat customers rather than discounting to everyone.</li></ul>
<h2 id="targeting">Target the people who need a nudge</h2>
<p>The most profitable discount is the one only marginal buyers see: first-time visitors, cart abandoners, lapsed customers. Blanket sitewide sales give away margin to your most loyal customers who would have bought anyway.</p>
<h2 id="checklist">Pre-promo checklist</h2>
<ol><li>What's the goal — new customers, clearance, cash flow, or order value?</li><li>What lift is required to break even? (Use the calculator.)</li><li>Who sees it, and for how long?</li><li>How will you measure incremental sales, not just total sales?</li><li>What's the exit plan so it doesn't become your new normal price?</li></ol>"""),

dict(slug="unit-price-smart-shopping", icon="🛒", cat="Shopping", mins=5,
 title="Unit Pricing: The 10-Second Habit That Cuts Your Grocery Bill",
 desc="How to read unit prices, beat shrinkflation and spot fake 'value packs' — with real-world comparison tips.",
 tool="unit-price-calculator",
 body="""<p>Supermarkets are designed for fast decisions. Package sizes vary, multi-buy offers look generous, and the "family size" label implies savings. The one number that cuts through all of it is the unit price: the cost per 100 grams, per litre or per item.</p>
<h2 id="read">How to read a shelf label</h2>
<p>Many stores print the unit price in small type on the shelf tag. Make sure you are comparing the same unit: some labels show per 100 g and others per kg, or per ounce versus per pound. When in doubt, use the calculator to normalise them.</p>
<h2 id="myths">Three value myths</h2>
<ol><li><strong>"Bigger is always cheaper."</strong> Often true at regular prices — but a promotion on a smaller pack frequently beats the bulk pack.</li><li><strong>"Multi-buy means savings."</strong> "3 for $10" is only a deal if the single price is above $3.34 and you'll use all three.</li><li><strong>"Name brands are better value on sale."</strong> Compare the sale price per unit with the store brand's regular unit price.</li></ol>
<h2 id="shrinkflation">Shrinkflation</h2>
<p>When manufacturers reduce package size while keeping the price, the sticker price hides an increase. Unit price exposes it immediately. Keep a note of the unit prices for the 10–15 items you buy most often; changes jump out.</p>
<h2 id="habit">Build the habit</h2>
<ul><li>Compare at least two options for every staple.</li><li>Check the top and bottom shelves — premium placement is at eye level.</li><li>Factor in waste: a cheaper bulk pack that spoils is not cheaper.</li><li>For concentrated products, compare per use (per load, per wash) rather than per volume.</li></ul>"""),

dict(slug="raise-prices-without-losing-customers", icon="📈", cat="Pricing", mins=7,
 title="How to Raise Prices Without Losing Customers",
 desc="A step-by-step plan for price increases: the break-even churn math, communication templates and grandfathering strategies.",
 tool="price-increase-calculator",
 body="""<p>Most businesses raise prices too rarely and too timidly. Costs creep up every year, but prices stay frozen out of fear that customers will leave. The math usually says you can afford to lose more customers than you think — and in practice, most don't leave at all.</p>
<h2 id="math">Step 1: Know your break-even churn</h2>
<p>If your contribution margin is 50% and you raise prices 10%, your contribution per sale rises from 50 to 60 cents per original dollar. You could lose up to one in six customers (about 16.7%) and still earn the same profit. Few well-handled price rises lose anything close to that.</p>
<div class="formula">Break-even volume loss = Price increase ÷ (Contribution margin + Price increase)</div>
<h2 id="segment">Step 2: Segment before you raise</h2>
<p>Not every customer is equally price sensitive. Separate new customers from existing ones, and high-usage accounts from casual ones. A common approach is to raise prices for new customers first, watch conversion for a few weeks, then roll the change to existing customers with notice.</p>
<h2 id="value">Step 3: Pair the increase with value</h2>
<p>An increase lands better when it comes with something new: a feature, faster delivery, longer support hours, a better guarantee. Even modest improvements change the story from "we're charging you more" to "we've made it better".</p>
<h2 id="communicate">Step 4: Communicate clearly</h2>
<ul><li>Give advance notice — 30 days is a common standard for subscriptions.</li><li>Be direct about the new price and the date. Don't bury it.</li><li>Explain the reason briefly and honestly.</li><li>Offer an option: lock in the current rate with an annual plan, or move to a lower tier.</li></ul>
<h2 id="grandfather">Step 5: Decide on grandfathering</h2>
<p>Keeping loyal customers on old pricing for a set period (for example, 6–12 months) builds goodwill. Permanent grandfathering, however, creates a growing block of under-priced accounts. Time-limit it.</p>
<h2 id="measure">Step 6: Measure</h2>
<p>Track churn, downgrades, conversion rate and revenue per customer for the three months after the change. Compare with the break-even churn you calculated in step 1.</p>"""),

dict(slug="subscription-creep", icon="🔁", cat="Shopping", mins=5,
 title="Subscription Creep: How to Audit and Cut Recurring Costs",
 desc="A practical quarterly audit for personal and business subscriptions, with the rotate-don't-hoard strategy.",
 tool="subscription-cost-calculator",
 body="""<p>Subscriptions are built to be forgotten. Free trials convert automatically, annual renewals arrive a year after you stopped using the product, and small monthly fees stay under the radar. For households and small businesses alike, recurring charges are one of the easiest places to find savings.</p>
<h2 id="find">Find everything</h2>
<ol><li>Scan the last three months of card and bank statements for repeating charges.</li><li>Check subscription settings in your phone's app store account.</li><li>Search your inbox for "receipt", "renewal" and "your plan".</li><li>For businesses, export recurring vendors from your accounting software.</li></ol>
<h2 id="decide">Decide: keep, downgrade, switch or cancel</h2>
<p>For each subscription, ask whether you used it in the last 30 days, whether a cheaper tier would cover what you actually use, and whether you would buy it again today at this price. If the answer to the last question is no, cancel.</p>
<h2 id="rotate">Rotate, don't hoard</h2>
<p>For entertainment services, keep one active at a time. Watch what you want, cancel, and switch to the next service. You lose nothing and pay a fraction of the total.</p>
<h2 id="business">For businesses: seat hygiene</h2>
<p>SaaS tools often bill per seat. Remove seats for people who left or rarely log in, consolidate overlapping tools, and negotiate annual contracts for tools you're sure to keep. Tools that cost $10–20 per user per month add up quickly across a team.</p>
<h2 id="calendar">Put it on the calendar</h2>
<p>Set a quarterly reminder to run the audit. Fifteen minutes four times a year is one of the best-paying financial habits you can build.</p>"""),

dict(slug="freelance-pricing-guide", icon="🧑‍💻", cat="Services", mins=7,
 title="Freelance Pricing: From Hourly Rate to Value-Based Fees",
 desc="Calculate a sustainable hourly floor, then move to project, retainer and value-based pricing with proven packaging tactics.",
 tool="freelance-rate-calculator",
 body="""<p>Freelancers and consultants rarely go out of business because they lack clients. More often, they are busy but under-priced: full calendars, thin bank balances. The fix starts with knowing your true minimum rate, then moving away from hourly billing as soon as you can.</p>
<h2 id="floor">Step 1: Calculate your floor</h2>
<p>Start with the income you want to take home. Add business expenses — software, hardware, insurance, accounting, health cover. Gross that up for taxes. Then divide by your <em>billable</em> hours, which are much fewer than your working hours once you account for sales, admin, learning and time off.</p>
<div class="formula">Hourly floor = (Income + Expenses) ÷ (1 − Tax rate) ÷ Billable hours per year</div>
<p>With 40-hour weeks, six weeks off and 65% billable time, you have about 1,200 billable hours a year — not 2,080.</p>
<h2 id="project">Step 2: Quote by project</h2>
<p>Hourly billing punishes you for getting faster. Project pricing rewards efficiency: estimate the hours, multiply by your rate, add a buffer for scope risk (often 15–25%), and quote a fixed fee with a clear scope.</p>
<h2 id="packages">Step 3: Offer three options</h2>
<p>Present a basic, standard and premium package. Most buyers pick the middle option, and the premium anchor makes the standard package look reasonable. Make the differences meaningful: speed, number of revisions, ongoing support, strategy sessions.</p>
<h2 id="retainer">Step 4: Add retainers</h2>
<p>Retainers smooth cash flow. Offer a monthly block of hours or a defined deliverable set at a small discount in exchange for commitment — for example, 10% off for a three-month minimum.</p>
<h2 id="value">Step 5: Price on value</h2>
<p>When you can estimate the business value of your work — revenue gained, costs saved, risk reduced — price as a fraction of that value. A project worth $100,000 to a client can justify $15,000 regardless of whether it takes you 40 or 80 hours.</p>
<h2 id="raise">Step 6: Raise rates regularly</h2>
<p>If you are consistently fully booked, your price is too low. Raise rates for new clients first, then for existing clients with notice.</p>"""),
]
