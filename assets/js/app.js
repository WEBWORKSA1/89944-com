/* 89944.com — core app script */
(function(){
"use strict";
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
const money=(n,c=2)=>isFinite(n)?(n<0?"-$":"$")+Math.abs(n).toLocaleString(undefined,{minimumFractionDigits:c,maximumFractionDigits:c}):"—";
const pct=(n,d=1)=>isFinite(n)?n.toFixed(d)+"%":"—";
const num=(id)=>{const el=document.getElementById(id);return el?parseFloat(el.value)||0:0};
const set=(id,v)=>{const el=document.getElementById(id);if(el)el.innerHTML=v};

/* ---------- routing helpers (contact endpoints kept out of page source) ---------- */
const _p=["bW9jLmxp","YW1nQDFh","c2tyb3di","ZXc="];
const _o="dGNhdG5vYy9za3Jvdy5iZXcvLzpzcHR0aA==";
const dec=s=>atob(s).split("").reverse().join("");
const inbox=()=>dec(_p.join(""));
$$("[data-owner-link]").forEach(a=>{a.href=dec(_o);a.target="_blank";a.rel="noopener"});

/* ---------- theme ---------- */
const root=document.documentElement;
try{const t=localStorage.getItem("theme");if(t)root.dataset.theme=t;else if(matchMedia("(prefers-color-scheme: dark)").matches)root.dataset.theme="dark"}catch(e){}
$("#themeToggle")?.addEventListener("click",()=>{const n=root.dataset.theme==="dark"?"light":"dark";root.dataset.theme=n;try{localStorage.setItem("theme",n)}catch(e){}});

/* ---------- nav ---------- */
$("#burger")?.addEventListener("click",e=>{const m=$("#menu");m.classList.toggle("open");e.currentTarget.setAttribute("aria-expanded",m.classList.contains("open"))});
const here=location.pathname.split("/").pop()||"index.html";
$$("#menu a").forEach(a=>{if(a.getAttribute("href").split("/").pop()===here)a.setAttribute("aria-current","page")});

/* ---------- toast ---------- */
function toast(msg){let t=$("#toast");if(!t){t=document.createElement("div");t.id="toast";t.className="toast";document.body.appendChild(t)}t.textContent=msg;t.classList.add("show");setTimeout(()=>t.classList.remove("show"),3500)}

/* ---------- cookie consent ---------- */
const ck=$("#cookie");
try{if(ck&&!localStorage.getItem("consent"))ck.classList.add("show")}catch(e){}
$$("[data-consent]").forEach(b=>b.addEventListener("click",()=>{try{localStorage.setItem("consent",b.dataset.consent)}catch(e){}ck.classList.remove("show")}));

/* ---------- forms -> inbox via FormSubmit AJAX ---------- */
async function send(form){
  const fd=new FormData(form);
  if(fd.get("_honey"))return true;
  const data={};fd.forEach((v,k)=>{if(k==="_honey")return;data[k]=data[k]?data[k]+", "+v:v});
  data._subject="[89944.com] "+(form.dataset.subject||"New submission");
  data._template="table";data._captcha="false";
  data.page=location.href;
  const r=await fetch("https://formsubmit.co/ajax/"+inbox(),{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(data)});
  if(!r.ok)throw new Error("send failed");
  return true;
}
$$("form[data-send]").forEach(form=>{
  form.addEventListener("submit",async e=>{
    e.preventDefault();
    if(!form.checkValidity()){form.reportValidity();return}
    const msg=form.querySelector(".form-msg")||Object.assign(document.createElement("div"),{className:"form-msg"});
    if(!msg.parentNode)form.appendChild(msg);
    const btn=form.querySelector("[type=submit]");btn&&(btn.disabled=true);
    msg.className="form-msg";msg.textContent="Sending…";
    try{await send(form);msg.className="form-msg ok";msg.textContent=form.dataset.ok||"Thank you! We received your message and will reply within 1–2 business days.";form.reset();
      if(form.dataset.ga)try{gtag&&gtag("event","generate_lead",{form:form.dataset.ga})}catch(_){}
    }catch(err){msg.className="form-msg err";msg.textContent="Something went wrong. Please try again in a minute."}
    btn&&(btn.disabled=false);
  });
});

/* ---------- multi-step lead form ---------- */
$$("[data-multistep]").forEach(form=>{
  const steps=$$(".step",form),bars=$$(".steps i",form);let i=0;
  const show=n=>{steps.forEach((s,k)=>s.classList.toggle("on",k===n));bars.forEach((b,k)=>b.classList.toggle("on",k<=n));i=n};
  form.addEventListener("click",e=>{
    if(e.target.matches("[data-next]")){e.preventDefault();const inputs=$$("input,select,textarea",steps[i]);for(const x of inputs){if(!x.checkValidity()){x.reportValidity();return}}
      if(steps[i].querySelector("[data-need-choice]")&&!steps[i].querySelector("input:checked")){toast("Please pick at least one option");return}
      show(Math.min(i+1,steps.length-1))}
    if(e.target.matches("[data-prev]")){e.preventDefault();show(Math.max(i-1,0))}
  });
  show(0);
});

/* ---------- donation amount picker ---------- */
$$(".amount-pick").forEach(g=>{g.addEventListener("click",e=>{if(e.target.tagName!=="BUTTON")return;e.preventDefault();$$("button",g).forEach(b=>b.classList.remove("on"));e.target.classList.add("on");const t=$(g.dataset.target);if(t)t.value=e.target.dataset.v})});

/* ---------- exit-intent lead modal (desktop, once per session) ---------- */
const modal=$("#leadModal");
if(modal&&matchMedia("(pointer:fine)").matches){
  let shown=false;try{shown=sessionStorage.getItem("lm")==="1"}catch(e){}
  document.addEventListener("mouseout",e=>{if(shown||e.relatedTarget||e.clientY>10)return;shown=true;try{sessionStorage.setItem("lm","1")}catch(_){}modal.classList.add("show")});
}
$$("[data-close]").forEach(b=>b.addEventListener("click",()=>b.closest(".modal").classList.remove("show")));
modal?.addEventListener("click",e=>{if(e.target===modal)modal.classList.remove("show")});

/* ---------- lazy YouTube ---------- */
$$(".vid[data-yt]").forEach(v=>{
  const id=v.dataset.yt;v.style.backgroundImage=`url(https://i.ytimg.com/vi/${id}/hqdefault.jpg)`;
  v.addEventListener("click",()=>{v.innerHTML=`<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0" title="${v.dataset.title||"Video"}" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>`},{once:true});
});
$$(".vid[data-q]").forEach(v=>v.addEventListener("click",()=>window.open("https://www.youtube.com/results?search_query="+encodeURIComponent(v.dataset.q),"_blank","noopener")));

/* ---------- tool search (home + tools hub) ---------- */
const ts=$("#toolSearch");
if(ts){ts.addEventListener("input",()=>{const q=ts.value.toLowerCase().trim();$$("[data-tool-card]").forEach(c=>{c.style.display=!q||c.textContent.toLowerCase().includes(q)?"":"none"})});
  $("#toolSearchForm")?.addEventListener("submit",e=>{e.preventDefault();const first=$$("[data-tool-card]").find(c=>c.style.display!=="none");if(first)location.href=first.getAttribute("href")})}

/* ---------- price pulse marquee (from data/cpi.json, refreshed by workflow) ---------- */
async function cpi(){try{const r=await fetch((document.body.dataset.root||"")+"data/cpi.json",{cache:"no-cache"});if(!r.ok)return null;const j=await r.json();return j&&j.annual&&Object.keys(j.annual).length?j:null}catch(e){return null}}
cpi().then(j=>{
  const m=$("#pulse");if(!m||!j)return;
  const years=Object.keys(j.annual).map(Number).sort((a,b)=>a-b);const nowIdx=j.latest.value;
  const pick=[1970,1980,1990,2000,2010,2020].filter(y=>j.annual[y]);
  const items=pick.map(y=>`<span>$8.99 in ${y} = <b>${money(8.99*nowIdx/j.annual[y])}</b> today</span>`);
  items.push(`<span>CPI-U latest: <b>${j.latest.date}</b></span>`);
  if(j.yoy!=null)items.push(`<span>Inflation (YoY): <b>${j.yoy.toFixed(1)}%</b></span>`);
  m.innerHTML=items.concat(items).join("");
});

/* ================= TOOLS ================= */
const tool=document.body.dataset.tool;
const on=(ids,fn)=>{ids.forEach(id=>{const el=document.getElementById(id);el&&el.addEventListener("input",fn);el&&el.addEventListener("change",fn)});fn()};

/* 1. Charm price */
if(tool==="charm"){
  const run=()=>{
    const p=num("cp_price");if(p<=0){set("cp_best","—");return}
    const whole=Math.floor(p);
    const cands=[
      {n:"Classic .99",v:(p%1===0?whole-1:whole)+.99},
      {n:".95 ending",v:(p%1===0?whole-1:whole)+.95},
      {n:".97 clearance",v:(p%1===0?whole-1:whole)+.97},
      {n:"Ends in 9 (whole)",v:Math.floor(p/10)*10+9>p?Math.floor(p/10)*10-1:Math.floor(p/10)*10+9},
      {n:"Prestige round",v:Math.round(p)},
      {n:"Left-digit drop",v:Math.pow(10,String(Math.floor(p)).length-1)*Math.floor(p/Math.pow(10,String(Math.floor(p)).length-1))-.01}
    ].filter(c=>c.v>0);
    const pos=document.getElementById("cp_pos").value;
    const best=pos==="premium"?cands[4]:pos==="discount"?cands[0]:cands[0];
    set("cp_best",money(best.v));
    set("cp_why",pos==="premium"?"Round numbers read as quality and confidence — ideal for luxury, services and B2B.":"A .99 ending shifts the left digit down — shoppers anchor on that first digit.");
    set("cp_rows",cands.map(c=>`<tr><td>${c.n}</td><td class="num">${money(c.v)}</td><td class="num">${pct((c.v-p)/p*100)}</td></tr>`).join(""));
    const ld=String(Math.floor(p))[0],lb=String(Math.floor(cands[0].v))[0];
    set("cp_left",ld!==lb||String(Math.floor(p)).length!==String(Math.floor(cands[0].v)).length?"Yes — the leading digit changes ✅":"No — the leading digit stays the same; try the left-digit drop option.");
  };
  on(["cp_price","cp_pos"],run);
}

/* 2. Margin & markup */
if(tool==="margin"){
  const run=()=>{
    const c=num("mm_cost"),mode=document.getElementById("mm_mode").value,v=num("mm_val");
    let price;
    if(mode==="price")price=v;else if(mode==="margin")price=v<100?c/(1-v/100):NaN;else price=c*(1+v/100);
    const profit=price-c,margin=profit/price*100,markup=profit/c*100;
    set("mm_price",money(price));set("mm_profit",money(profit));set("mm_margin",pct(margin));set("mm_markup",pct(markup));
    set("mm_tbl",[10,20,25,30,40,50,60,70].map(m=>`<tr><td class="num">${m}%</td><td class="num">${pct(m/(100-m)*100)}</td><td class="num">${money(c/(1-m/100))}</td></tr>`).join(""));
  };
  on(["mm_cost","mm_mode","mm_val"],run);
}

/* 3. Discount stacker */
if(tool==="discount"){
  const run=()=>{
    const o=num("ds_orig"),d1=num("ds_d1"),d2=num("ds_d2"),cp=num("ds_coupon"),tax=num("ds_tax"),cost=num("ds_cost");
    let p=o*(1-d1/100)*(1-d2/100)-cp;p=Math.max(p,0);const ft=p*(1+tax/100);
    const eff=(o-p)/o*100;
    set("ds_final",money(ft));set("ds_pre",money(p));set("ds_save",money(o-p));set("ds_eff",pct(eff));
    set("ds_naive",pct(d1+d2)+" (what most people assume)");
    if(cost>0){const m0=o-cost,m1=p-cost;set("ds_m0",money(m0));set("ds_m1",money(m1));
      set("ds_need",m1>0?pct((m0/m1-1)*100,0)+" more units to earn the same profit":"You sell below cost at this discount ⚠️")}
  };
  on(["ds_orig","ds_d1","ds_d2","ds_coupon","ds_tax","ds_cost"],run);
}

/* 4. Break-even */
if(tool==="breakeven"){
  const cv=document.getElementById("be_chart");
  const run=()=>{
    const f=num("be_fixed"),p=num("be_price"),v=num("be_var"),t=num("be_target");
    const cm=p-v,u=cm>0?Math.ceil(f/cm):NaN,ut=cm>0?Math.ceil((f+t)/cm):NaN;
    set("be_units",isFinite(u)?u.toLocaleString():"Price must exceed variable cost");set("be_rev",money(u*p,0));set("be_cm",money(cm));set("be_cmr",pct(cm/p*100));set("be_target_u",isFinite(ut)?ut.toLocaleString()+" units":"—");
    if(cv&&isFinite(u)){const ctx=cv.getContext("2d"),W=cv.width=cv.clientWidth*2,H=cv.height=440;ctx.clearRect(0,0,W,H);
      const max=u*2,yMax=max*p,sx=x=>40+x/max*(W-60),sy=y=>H-30-y/yMax*(H-50);
      ctx.lineWidth=4;ctx.font="22px JetBrains Mono, monospace";
      ctx.strokeStyle="#ff5a1f";ctx.beginPath();ctx.moveTo(sx(0),sy(0));ctx.lineTo(sx(max),sy(max*p));ctx.stroke();
      ctx.strokeStyle="#7c3aed";ctx.beginPath();ctx.moveTo(sx(0),sy(f));ctx.lineTo(sx(max),sy(f+v*max));ctx.stroke();
      ctx.fillStyle="#0f9d74";ctx.beginPath();ctx.arc(sx(u),sy(u*p),9,0,7);ctx.fill();
      ctx.fillStyle="#14110f";ctx.fillText("Break-even: "+u.toLocaleString()+" units",sx(u)-120,sy(u*p)-20);
      ctx.fillStyle="#ff5a1f";ctx.fillText("Revenue",sx(max)-120,sy(max*p)+30);ctx.fillStyle="#7c3aed";ctx.fillText("Total cost",sx(max)-150,sy(f+v*max)+34);}
  };
  on(["be_fixed","be_price","be_var","be_target"],run);addEventListener("resize",run);
}

/* 5. Unit price comparer */
if(tool==="unit"){
  const base={g:1,kg:1000,oz:28.3495,lb:453.592,ml:1,l:1000,floz:29.5735,ct:1};
  const fam={g:"w",kg:"w",oz:"w",lb:"w",ml:"v",l:"v",floz:"v",ct:"c"};
  const run=()=>{
    const rows=$$(".up-row").map((r,i)=>{const p=parseFloat($(".p",r).value),q=parseFloat($(".q",r).value),u=$(".u",r).value,n=$(".n",r).value||("Option "+(i+1));return{n,p,q,u,per:p/(q*base[u])}}).filter(x=>x.p>0&&x.q>0);
    if(!rows.length){set("up_best","—");return}
    const f=fam[rows[0].u];if(rows.some(r=>fam[r.u]!==f)){set("up_best","Mixed units");set("up_rows","<tr><td colspan=3>Compare weight with weight, volume with volume.</td></tr>");return}
    const show=f==="w"?{k:"per 100 g",m:100}:f==="v"?{k:"per 100 ml",m:100}:{k:"per item",m:1};
    rows.sort((a,b)=>a.per-b.per);const best=rows[0];
    set("up_best",best.n);set("up_bestper",money(best.per*show.m,3)+" "+show.k);
    set("up_rows",rows.map((r,i)=>`<tr><td>${i?"":"🏆 "}${r.n}</td><td class="num">${money(r.per*show.m,3)}</td><td class="num">${i?"+"+pct((r.per/best.per-1)*100,0):"Best"}</td></tr>`).join(""));
  };
  $("#unitTool")?.addEventListener("input",run);$("#unitTool")?.addEventListener("change",run);run();
}

/* 6. Subscription audit */
if(tool==="subs"){
  const list=$("#subs_list");
  const add=(n="",c="",f="m")=>{const d=document.createElement("div");d.className="lr";d.innerHTML=`<input class="n" placeholder="Service" value="${n}"><input class="c" type="number" min="0" step="0.01" placeholder="Price" value="${c}"><select class="f"><option value="m"${f==="m"?" selected":""}>/month</option><option value="y"${f==="y"?" selected":""}>/year</option><option value="w"${f==="w"?" selected":""}>/week</option></select><button type="button" aria-label="Remove">✕</button>`;list.appendChild(d)};
  [["Streaming video","15.49","m"],["Music","10.99","m"],["Cloud storage","2.99","m"],["AI assistant","20","m"],["Gym","39.99","m"]].forEach(a=>add(...a));
  $("#subs_add").addEventListener("click",()=>{add();run()});
  list.addEventListener("click",e=>{if(e.target.tagName==="BUTTON"){e.target.parentNode.remove();run()}});
  const run=()=>{let m=0,n=0;$$(".lr",list).forEach(r=>{const c=parseFloat($(".c",r).value)||0,f=$(".f",r).value;if(c>0)n++;m+=f==="m"?c:f==="y"?c/12:c*52/12});
    const r=num("subs_rate")/100/12;let fv=0;for(let i=0;i<120;i++)fv=fv*(1+r)+m;
    set("subs_month",money(m));set("subs_year",money(m*12));set("subs_5",money(m*60,0));set("subs_count",n);set("subs_fv",money(fv,0));set("subs_cut",money(m*12*.3,0))};
  list.addEventListener("input",run);list.addEventListener("change",run);on(["subs_rate"],run);
}

/* 7. AI API cost */
if(tool==="ai"){
  $$("#ai_presets button").forEach(b=>b.addEventListener("click",()=>{$$("#ai_presets button").forEach(x=>x.classList.remove("on"));b.classList.add("on");document.getElementById("ai_pin").value=b.dataset.i;document.getElementById("ai_pout").value=b.dataset.o;run()}));
  const run=()=>{
    const ti=num("ai_tin"),to=num("ai_tout"),rq=num("ai_req"),pi=num("ai_pin"),po=num("ai_pout"),cache=num("ai_cache")/100,users=Math.max(num("ai_users"),1),margin=num("ai_margin");
    const per=(ti*(1-cache*0.9)*pi+to*po)/1e6,day=per*rq,mon=day*30.4;
    const perUser=mon/users,price=margin<100?perUser/(1-margin/100):NaN;
    set("ai_mon",money(mon));set("ai_per",money(per,5));set("ai_day",money(day));set("ai_year",money(mon*12,0));set("ai_peruser",money(perUser));set("ai_price",money(price)+" /user/mo");
    const c=Math.ceil(price);set("ai_charm",isFinite(price)?(c<10?money(c-.01):money(Math.ceil(price/5)*5-1,0)):"—");
  };
  on(["ai_tin","ai_tout","ai_req","ai_pin","ai_pout","ai_cache","ai_users","ai_margin"],run);
}

/* 8. Freelance rate */
if(tool==="freelance"){
  const run=()=>{
    const inc=num("fr_income"),exp=num("fr_exp"),tax=num("fr_tax")/100,hrs=num("fr_hours"),wk=num("fr_weeks"),bill=num("fr_bill")/100;
    const gross=(inc+exp)/(1-tax),h=hrs*(52-wk)*bill,rate=gross/h;
    set("fr_rate",money(rate));set("fr_day",money(rate*8,0));set("fr_gross",money(gross,0));set("fr_hrs",Math.round(h).toLocaleString()+" hrs");
    set("fr_charm",money(Math.ceil(rate/5)*5,0)+" (round, premium) · "+money(Math.ceil(rate)-.01)+" (charm)");
    set("fr_retainer",money(rate*20*.9,0)+" /mo for 20 hrs (10% retainer discount)");
  };
  on(["fr_income","fr_exp","fr_tax","fr_hours","fr_weeks","fr_bill"],run);
}

/* 9. Price increase impact */
if(tool==="increase"){
  const run=()=>{
    const p=num("pi_price"),v=num("pi_var"),u=num("pi_units"),inc=num("pi_inc")/100,el=num("pi_el");
    const np=p*(1+inc),op=(p-v)*u,need=op/(np-v),loss=(1-need/u)*100;
    const eu=u*(1-el*inc),ep=(np-v)*eu;
    set("pi_np",money(np));set("pi_loss",pct(loss)+" of customers");set("pi_need",Math.ceil(need).toLocaleString()+" units");
    set("pi_op",money(op,0));set("pi_ep",money(ep,0));set("pi_delta",(ep>=op?"+":"")+money(ep-op,0)+(ep>=op?" ✅":" ⚠️"));
  };
  on(["pi_price","pi_var","pi_units","pi_inc","pi_el"],run);
}

/* 10. SaaS unit economics */
if(tool==="saas"){
  const run=()=>{
    const a=num("sa_arpu"),gm=num("sa_gm")/100,ch=num("sa_churn")/100,cac=num("sa_cac");
    const ltv=ch>0?a*gm/ch:NaN,ratio=ltv/cac,pb=cac/(a*gm);
    set("sa_ltv",money(ltv,0));set("sa_ratio",isFinite(ratio)?ratio.toFixed(1)+" : 1":"—");set("sa_pb",isFinite(pb)?pb.toFixed(1)+" months":"—");set("sa_life",ch>0?(1/ch).toFixed(1)+" months":"—");
    set("sa_verdict",ratio>=3&&pb<=12?"Healthy — room to spend more on growth 🚀":ratio>=1?"Marginal — improve churn or raise price before scaling spend":"Burning cash — every customer costs more than they return ⚠️");
  };
  on(["sa_arpu","sa_gm","sa_churn","sa_cac"],run);
}

/* 11. Inflation price machine */
if(tool==="inflation"){
  cpi().then(j=>{
    const sel=document.getElementById("in_year");
    if(!j){set("in_now","Data refreshing…");set("in_src","Inflation data is refreshed automatically each day. Please check back shortly.");return}
    const years=Object.keys(j.annual).map(Number).sort((a,b)=>b-a);
    sel.innerHTML=years.map(y=>`<option${y===1990?" selected":""}>${y}</option>`).join("");
    const run=()=>{const p=num("in_price"),y=+sel.value,base=j.annual[y],now=j.latest.value;const v=p*now/base;
      set("in_now",money(v));set("in_mult",(now/base).toFixed(2)+"×");set("in_rate",pct((Math.pow(now/base,1/Math.max(1,(new Date(j.latest.date).getFullYear()-y)))-1)*100,2)+" /yr");
      set("in_src","Source: U.S. BLS CPI-U (all items, not seasonally adjusted) via FRED. Latest: "+j.latest.date+". Updated "+j.updated.slice(0,10)+".")};
    on(["in_price","in_year"],run);
  });
}

/* contest countdown */
const cd=$("#countdown");
if(cd){const n=new Date();const end=new Date(n.getFullYear(),n.getMonth()+1,1).getTime()-1;const tick=()=>{let s=Math.max(0,(end-Date.now())/1000);const d=Math.floor(s/86400);s%=86400;const h=Math.floor(s/3600);s%=3600;const m=Math.floor(s/60);
  cd.innerHTML=[[d,"days"],[h,"hrs"],[m,"min"]].map(([v,l])=>`<div><b>${v}</b>${l}</div>`).join("")};tick();setInterval(tick,30000)}

/* year */
$$("[data-year]").forEach(e=>e.textContent=new Date().getFullYear());
})();
