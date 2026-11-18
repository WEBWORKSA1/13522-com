"""Product + content pages: home, planner, tools, guide, templates, videos, AI tools."""
from layout import hp, consent


def planner_block(r=""):
    return f"""<div id="planner" class="planner">
<div>
  <div class="card" style="margin-bottom:18px">
    <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap"><div><span class="tag">Today</span><h3 id="plan-date" style="margin:0">Your day</h3></div>
    <div class="noprint" style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn btn-ghost btn-sm" data-act="copy">Copy</button><button class="btn btn-ghost btn-sm" data-act="txt">Download</button><button class="btn btn-ghost btn-sm" data-act="print">Print</button><button class="btn btn-ghost btn-sm" data-act="clear">Clear</button></div></div>
  </div>
  <details class="card noprint" style="margin-bottom:18px"><summary style="cursor:pointer;font-weight:700;font-family:var(--display)">⚡ Smart Sort — paste your brain dump, get a 1·3·5 in one click</summary>
    <p style="margin-top:12px">One task per line. Add a time if you know it (e.g. "Write proposal 2h", "Pay invoice 5m"). Sorting runs in your browser; nothing is uploaded.</p>
    <textarea id="brain" rows="6" style="width:100%;border:1.5px solid var(--line);border-radius:12px;padding:12px;background:var(--bg);color:var(--ink)" placeholder="Finish Q3 report 2h&#10;Reply to Priya&#10;Record product demo&#10;Book flights 10m&#10;Review pull request 45m"></textarea>
    <button class="btn btn-dark btn-sm" id="sort-btn" type="button" style="margin-top:10px">Sort into 1 · 3 · 5</button><p id="parked" style="font-size:.9rem;color:var(--muted);margin-top:10px"></p>
  </details>
  <div id="slots"></div>
  <div class="grid-2" style="margin-top:8px">
    <div class="field"><label for="rev-am">🌅 Review 1 — morning intention</label><textarea id="rev-am" rows="3" placeholder="What will make today a win? What could get in the way?"></textarea></div>
    <div class="field"><label for="rev-pm">🌙 Review 2 — evening reflection</label><textarea id="rev-pm" rows="3" placeholder="What got done? What moves to tomorrow? What did I learn?"></textarea></div>
  </div>
</div>
<aside class="side">
  <div class="card" style="text-align:center"><span class="tag">Day score</span><div id="ring"></div><p id="planned" style="font-size:.9rem;color:var(--muted);margin:0"></p></div>
  <div class="card" style="text-align:center"><span class="tag">2 Focus sprints</span><div class="timer" id="timer">25:00</div>
    <div class="seg"><button type="button" data-min="25">25m</button><button type="button" data-min="50">50m</button><button type="button" data-min="90">90m</button></div>
    <div style="display:flex;gap:8px;justify-content:center"><button class="btn btn-primary btn-sm" id="t-start" type="button">Start sprint</button><button class="btn btn-ghost btn-sm" id="t-reset" type="button">Reset</button></div>
    <div class="seg" style="margin-top:14px"><button type="button" data-sprint>Sprint 1</button><button type="button" data-sprint>Sprint 2</button></div></div>
  <div class="card"><span class="tag">Streak</span><div class="stat" id="streak">0 days</div><p style="font-size:.88rem;margin:0 0 10px">Days scoring 60%+. Last 14 days:</p><div id="hist"></div></div>
</aside>
</div>"""


def home():
    body = f"""
<section class="hero"><div class="wrap grid">
<div>
<span class="eyebrow">Free daily planner · no sign-up</span>
<h1>Do what matters.<br><span class="c-big">1</span>·<span class="c-med">3</span>·<span class="c-small">5</span>·<span class="c-sprint">2</span>·<span class="c-review">2</span> every day.</h1>
<p class="lede">13522 is a simple daily system: <strong>1 big</strong> task, <strong>3 medium</strong>, <strong>5 small</strong>, <strong>2 focus sprints</strong> to get them done and <strong>2 short reviews</strong> to start and close the day. Plan it in 3 minutes with the free planner below.</p>
<div class="actions"><a class="btn btn-primary" href="#plan">Plan my day →</a><a class="btn btn-ghost" href="teams.html">Roll it out to my team</a></div>
<div class="trust"><span>Works offline in your browser</span><span>No account needed</span><span>Free forever</span></div>
</div>
<div class="stack reveal" aria-label="The 13522 day">
<div class="row"><span class="n c-big">1</span><div style="flex:1"><strong>Big task</strong><small>The one that makes today a win · ~2h</small><div class="bars"><i style="background:var(--big)"></i></div></div></div>
<div class="row"><span class="n c-med">3</span><div style="flex:1"><strong>Medium tasks</strong><small>Meaningful, 30–90 min each</small><div class="bars"><i style="background:var(--med)"></i><i style="background:var(--med)"></i><i style="background:var(--med)"></i></div></div></div>
<div class="row"><span class="n c-small">5</span><div style="flex:1"><strong>Small tasks</strong><small>Quick wins under 15 min</small><div class="bars"><i style="background:var(--small)"></i><i style="background:var(--small)"></i><i style="background:var(--small)"></i><i style="background:var(--small)"></i><i style="background:var(--small)"></i></div></div></div>
<div class="row"><span class="n c-sprint">2</span><div style="flex:1"><strong>Focus sprints</strong><small>25, 50 or 90 minutes, no notifications</small><div class="bars"><i style="background:var(--sprint)"></i><i style="background:var(--sprint)"></i></div></div></div>
<div class="row"><span class="n c-review">2</span><div style="flex:1"><strong>Reviews</strong><small>3-minute morning intention, 5-minute evening close</small><div class="bars"><i style="background:var(--review)"></i><i style="background:var(--review)"></i></div></div></div>
</div>
</div></section>

<section style="padding-top:10px"><div class="wrap"><div class="daily" data-daily><span class="badge">Tip of the day</span><div><strong data-daily-tip>Pick tomorrow's Big task before you close your laptop tonight — mornings go to doing, not deciding.</strong><div style="font-size:.9rem;color:var(--muted)">Today's challenge: <span data-daily-ch>Finish your Big task before noon.</span> · <span data-daily-date></span></div></div></div></div></section>

<section id="plan"><div class="wrap">
<div class="sec-head"><span class="eyebrow">The planner</span><h2>Plan today in three minutes</h2><p>Type your tasks, tick them off, run two focus sprints. Everything saves automatically in this browser; unfinished items carry over to tomorrow.</p></div>
{planner_block()}
</div></section>

<section class="alt"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Why it works</span><h2>Nine tasks you can actually finish beats thirty you won't</h2><p>Long to-do lists create decision fatigue and a permanent sense of being behind. A fixed shape forces the hard choice up front: what matters most today?</p></div>
<div class="grid-3">
<div class="card reveal"><div class="icon">🎯</div><h3>Forced prioritisation</h3><p>One Big slot means you must decide what the day is for. Everything else is supporting cast.</p></div>
<div class="card reveal"><div class="icon">⚖️</div><h3>Realistic load</h3><p>Roughly 2h + 3h + 1h of work fits a real day with meetings, breaks and interruptions.</p></div>
<div class="card reveal"><div class="icon">⏱️</div><h3>Protected focus</h3><p>Two timed sprints turn intentions into output. Most people get their Big task done in sprint one.</p></div>
<div class="card reveal"><div class="icon">🔁</div><h3>Built-in learning</h3><p>Morning and evening reviews close the loop, so tomorrow's plan is better than today's.</p></div>
<div class="card reveal"><div class="icon">📈</div><h3>Visible progress</h3><p>A daily score and streak make consistency tangible — 60% or more counts as a winning day.</p></div>
<div class="card reveal"><div class="icon">🤝</div><h3>Team-ready</h3><p>Everyone shares their one Big task at stand-up. Alignment in 60 seconds per person.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="sec-head"><span class="eyebrow">Free tools</span><h2>Calculators that change how you plan</h2></div>
<div class="grid-3">
<a class="card reveal" href="tools.html#meeting"><div class="icon">💸</div><h3>Meeting cost calculator</h3><p>See what a recurring meeting really costs per week and per year.</p></a>
<a class="card reveal" href="tools.html#hourly"><div class="icon">⌛</div><h3>What is my hour worth?</h3><p>Turn income into an hourly value and decide what to delegate.</p></a>
<a class="card reveal" href="tools.html#estimate"><div class="icon">📐</div><h3>Task time estimator</h3><p>Correct for the planning fallacy and size a task as Big, Medium or Small.</p></a>
<a class="card reveal" href="tools.html#capacity"><div class="icon">📅</div><h3>Daily capacity check</h3><p>Does a full 13522 day fit around today's meetings?</p></a>
<a class="card reveal" href="tools.html#procrast"><div class="icon">🐢</div><h3>Cost of procrastination</h3><p>The yearly value of the minutes that drift away each day.</p></a>
<a class="card reveal" href="tools.html#team"><div class="icon">👥</div><h3>Team focus cost</h3><p>Estimate what unclear priorities cost your whole team.</p></a>
</div></div></section>

<section class="alt"><div class="wrap">
<div class="lead reveal">
<div><span class="eyebrow" style="background:#ffffff14;color:#fff;border-color:#ffffff30">For teams & managers</span>
<h2>Get your team's free Focus Plan</h2>
<p>Answer five quick questions and get a one-page rollout plan for your team, with an estimate of the hours lost to unclear priorities each week.</p>
<ul><li>Takes 60 seconds</li><li>Personalised to team size and meeting load</li><li>Includes stand-up script and weekly review agenda</li><li>Optional 30-minute call, no obligation</li></ul>
</div>
<div class="card"><h3>Start here</h3><p>Prefer to skip the questions? Leave your details and we'll send the plan.</p>
<form data-form="team-lead-quick" data-subject="Team focus plan (quick)" data-ok="Thanks! Your team focus plan is on its way within 1 business day.">
<div class="row2"><div class="field"><label for="hl-name">Name</label><input id="hl-name" name="name" required></div><div class="field"><label for="hl-email">Work email</label><input id="hl-email" type="email" name="email" required></div></div>
<div class="field"><label for="hl-size">Team size</label><select id="hl-size" name="team_size" required><option value="">Choose…</option><option>1–5</option><option>6–20</option><option>21–50</option><option>51–200</option><option>200+</option></select></div>
{hp()}{consent()}
<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Send my team plan →</button><div class="form-msg" role="status"></div></form>
<p class="form-note">Or take the <a href="teams.html#assessment">60-second assessment</a>.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="sec-head"><span class="eyebrow">Watch & learn</span><h2>Videos on focus and planning</h2><p>Curated topics to go deeper. <a href="videos.html">See all videos →</a></p></div>
<div class="grid-3" id="videos" data-limit="3"></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="sec-head"><span class="eyebrow">From the blog</span><h2>Guides worth your time</h2></div>
<div class="grid-3">
<a class="card reveal" href="blog/1-3-5-rule-explained.html"><span class="tag">Method</span><h3>The 1-3-5 rule, explained properly</h3><p>Where it comes from, why nine tasks is the sweet spot, and how to size tasks honestly.</p></a>
<a class="card reveal" href="blog/ai-daily-planning.html"><span class="tag">AI</span><h3>Using AI to plan your day without losing control</h3><p>Prompts and workflows that let AI sort the list while you keep the judgement.</p></a>
<a class="card reveal" href="blog/1-3-5-for-teams.html"><span class="tag">Teams</span><h3>Running a team on 1-3-5</h3><p>Stand-ups, async check-ins and how managers protect everyone's Big task.</p></a>
</div></div></section>

<section><div class="wrap"><div class="grid-3">
<div class="card reveal"><span class="tag">Monthly challenge</span><h3>Win prizes for consistency</h3><p>Log 20 winning days this month and enter the prize draw. Free to enter.</p><a class="btn btn-dark btn-sm" href="contests.html">See this month's challenge</a></div>
<div class="card reveal"><span class="tag">Support</span><h3>Keep 13522 free</h3><p>Donations fund hosting, new tools, contest prizes and paying contributors.</p><a class="btn btn-dark btn-sm" href="support.html">Support the project</a></div>
<div class="card reveal"><span class="tag">Sponsor</span><h3>Reach focused professionals</h3><p>Sponsor the planner, the newsletter or a monthly challenge.</p><a class="btn btn-dark btn-sm" href="advertise.html">Advertising options</a></div>
</div></div></section>

<section class="alt"><div class="wrap narrow faq">
<h2>Questions</h2>
<details><summary>What does 13522 stand for?</summary><p>1 big task, 3 medium tasks, 5 small tasks, 2 focus sprints and 2 reviews. It extends the well-known 1-3-5 to-do list with the two habits that make it stick: protected focus time and a short daily review.</p></details>
<details><summary>Is the planner really free? Where is my data stored?</summary><p>Yes. The planner runs entirely in your browser and saves to your device's local storage. We don't have an account system and never see your tasks.</p></details>
<details><summary>What if I have more than nine tasks?</summary><p>You almost always do. The rest stay on a master list (or in "Parked" after Smart Sort). The point is to choose the nine that make today count — new urgent work replaces a medium task rather than growing the list.</p></details>
<details><summary>How long should focus sprints be?</summary><p>Start with 25 minutes if focus is hard right now, 50 minutes for most knowledge work, and 90 minutes for deep creative or technical work. Two sprints a day is the minimum that reliably moves a Big task.</p></details>
<details><summary>Can I use this with Todoist, Notion or Trello?</summary><p>Yes — see the <a href="ai-tools.html">tools directory</a> for setup ideas in each app, and the <a href="templates.html">printable templates</a> if you prefer paper.</p></details>
</div></section>
"""
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "What does 13522 stand for?", "acceptedAnswer": {"@type": "Answer", "text": "1 big task, 3 medium tasks, 5 small tasks, 2 focus sprints and 2 reviews each day."}},
        {"@type": "Question", "name": "Is the planner free and private?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. It runs in your browser and stores tasks only on your device."}},
    ]}
    return ("index.html", "13522 — Free 1-3-5 Daily Planner, Focus Timer & Productivity Tools",
            "Plan your day with the 13522 method: 1 big, 3 medium and 5 small tasks, 2 focus sprints and 2 reviews. Free planner, calculators, guides and AI tools directory.",
            body, ("planner.js", "pages.js"), faq)


def planner():
    body = f"""
<section class="hero" style="padding-bottom:10px"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Planner</div>
<h1>The 13522 Daily Planner</h1>
<p class="lede">1 big · 3 medium · 5 small · 2 sprints · 2 reviews. Free, private and saved in your browser.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap">{planner_block()}</div></section>
<section class="alt"><div class="wrap narrow">
<h2>How to use the planner</h2>
<ol>
<li><strong>Brain dump (2 min).</strong> Paste everything on your mind into Smart Sort, or type directly into the slots. Add minutes where you know them.</li>
<li><strong>Choose your Big task.</strong> Ask: "If I only finish one thing today, which one makes the biggest difference?" Write it as a finish line, not an activity.</li>
<li><strong>Fill three Medium and five Small.</strong> Medium tasks are 30–90 minutes; small ones are under 15. Anything that doesn't fit is parked, not lost.</li>
<li><strong>Morning review.</strong> Write one sentence: what will make today a win, and what might get in the way.</li>
<li><strong>Run sprint one on the Big task.</strong> Notifications off, one tab open. Choose 25, 50 or 90 minutes.</li>
<li><strong>Batch the small tasks.</strong> Clear all five in one block, ideally after lunch when energy dips.</li>
<li><strong>Sprint two</strong> on the Big task if unfinished, otherwise on your most important Medium task.</li>
<li><strong>Evening review.</strong> Tick what's done, note what carries over and why. The planner moves unfinished items to tomorrow automatically.</li>
</ol>
<div class="callout"><strong>Scoring:</strong> Big task = 40 points, each Medium = 10, each Small = 4, each sprint = 5. A day of 60% or more counts toward your streak — that's the Big task plus two Medium tasks, for example.</div>
<p>Prefer paper? Print today's plan with the Print button, or grab a blank sheet from the <a href="templates.html">printable templates</a>.</p>
</div></section>
"""
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "13522 Daily Planner", "applicationCategory": "ProductivityApplication", "operatingSystem": "Any (web browser)", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": "https://13522.com/planner.html"}
    return ("planner.html", "Free 1-3-5 Daily Planner with Focus Timer",
            "A free online 1-3-5 planner: one big, three medium and five small tasks, two focus sprints with a timer, morning and evening reviews, day score and streaks.",
            body, ("planner.js",), app)


def field(i, label, val, step="1", suffix=""):
    return f'<div class="field"><label for="{i}">{label}</label><input id="{i}" type="number" min="0" step="{step}" value="{val}">{suffix}</div>'


def tools():
    body = f"""
<section class="hero" style="padding-bottom:10px"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Tools</div>
<h1>Free productivity calculators</h1>
<p class="lede">Put real numbers on time, meetings and focus — then plan your 13522 day around them.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap">
<div class="tabs" data-tabs role="tablist">
<button data-tab="meeting" role="tab">💸 Meeting cost</button><button data-tab="hourly" role="tab">⌛ Hourly value</button><button data-tab="estimate" role="tab">📐 Task estimator</button><button data-tab="capacity" role="tab">📅 Capacity</button><button data-tab="procrast" role="tab">🐢 Procrastination</button><button data-tab="team" role="tab">👥 Team cost</button>
</div>
<div class="tool card" id="meeting"><h2>Meeting cost calculator</h2><form data-calc="meeting"><div class="grid-4">{field("m-people","Attendees",6)}{field("m-rate","Avg hourly cost ($)",55)}{field("m-mins","Length (minutes)",60)}{field("m-week","Times per week",2)}</div><div class="out"></div></form>
<p>Meetings are the most expensive line item that never appears on a budget. Multiply people × hourly cost × duration and the number usually surprises. In a 13522 day, a 60-minute meeting occupies a Medium slot — so plan it honestly, and send an agenda so it ends early.</p></div>
<div class="tool card" id="hourly"><h2>What is my hour worth?</h2><form data-calc="hourly"><div class="grid-3">{field("h-income","Annual income or revenue ($)",85000,"1000")}{field("h-hours","Working hours per week",40)}{field("h-weeks","Working weeks per year",48)}</div><div class="out"></div></form>
<p>Knowing your hourly value makes delegation decisions obvious. If a small task costs you more than it would cost to automate or outsource, move it off your list permanently.</p></div>
<div class="tool card" id="estimate"><h2>Task time estimator</h2><form data-calc="estimate"><div class="grid-2">{field("e-base","Your gut estimate (minutes)",45)}<div class="field"><label for="e-conf">How confident are you? (%)</label><input id="e-conf" type="range" min="10" max="100" value="60"></div></div><div class="out"></div></form>
<p>People consistently underestimate how long their own tasks take — psychologists call it the planning fallacy. A simple buffer based on your confidence gets you closer to reality and tells you which tier the task belongs in.</p></div>
<div class="tool card" id="capacity"><h2>Daily capacity check</h2><form data-calc="capacity"><div class="grid-2">{field("c-hours","Working hours today",8,"0.5")}{field("c-mtg","Hours of meetings today",2,"0.5")}</div><div class="out"></div></form>
<p>On meeting-heavy days a full 13522 won't fit. Scale down to a 1·2·3 (one big, two medium, three small) rather than carrying over half your list.</p></div>
<div class="tool card" id="procrast"><h2>Cost of procrastination</h2><form data-calc="procrast"><div class="grid-3">{field("p-mins","Minutes lost per day",45)}{field("p-rate","Your hourly value ($)",40)}{field("p-days","Working days per week",5)}</div><div class="out"></div></form>
<p>Drift rarely feels expensive in the moment. Annualised, it often equals a holiday, a course or a new laptop. The fix isn't more willpower — it's a pre-decided first task and a timer.</p></div>
<div class="tool card" id="team"><h2>Team focus cost</h2><form data-calc="team"><div class="grid-3">{field("t-size","Team size",12)}{field("t-lost","Hours lost per person per week",4,"0.5")}{field("t-rate","Blended hourly cost ($)",50)}</div><div class="out"></div></form>
<p>Unclear priorities, context switching and status-chasing add up across a team. Shared daily Big tasks and short reviews recover a meaningful share of that time.</p></div>
</div></section>
"""
    return ("tools.html", "Free Productivity Calculators — Meeting Cost, Hourly Value, Capacity",
            "Free calculators: meeting cost, what your hour is worth, task time estimator, daily capacity, cost of procrastination and team focus cost.",
            body, ("pages.js",), None)


def guide():
    body = """
<article class="article"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Guide</div>
<h1>The complete guide to the 13522 method</h1>
<p class="meta">Updated regularly · 12-minute read</p>
<p class="lede">The 13522 method is a daily planning system built on the popular 1-3-5 to-do list: one big task, three medium tasks and five small tasks. It adds two habits that make the list actually get done — two protected focus sprints and two short reviews.</p>
<div class="toc"><strong>Contents</strong><ol><li><a href="#what">What the 1-3-5 list is</a></li><li><a href="#why">Why a fixed shape works</a></li><li><a href="#sizing">Sizing tasks honestly</a></li><li><a href="#sprints">The two focus sprints</a></li><li><a href="#reviews">The two reviews</a></li><li><a href="#day">A sample 13522 day</a></li><li><a href="#adapt">Adapting it to your life</a></li><li><a href="#mistakes">Common mistakes</a></li><li><a href="#start">Start today</a></li></ol></div>
<h2 id="what">1. What the 1-3-5 list is</h2>
<p>The 1-3-5 rule is a widely shared productivity technique: each day you commit to one major task, three medium tasks and five small tasks. That's nine items — enough to feel productive, few enough to finish. It has been written about by productivity apps, time-tracking companies and business coaches for years because it solves the most common planning problem: lists that are too long to ever complete.</p>
<p>The method doesn't tell you <em>what</em> to work on. It forces you to choose. When there is only one Big slot, you can't pretend that ten things are top priority.</p>
<h2 id="why">2. Why a fixed shape works</h2>
<p><strong>Decision fatigue.</strong> Every time you look at a 30-item list you re-decide what to do next. A short, pre-sorted list removes those micro-decisions so energy goes into the work.</p>
<p><strong>Completion bias.</strong> Finishing things feels good, and that feeling fuels the next task. Five small tasks give you guaranteed wins; the Big task gives the day meaning.</p>
<p><strong>Honest capacity.</strong> A typical knowledge worker has three to five hours of genuinely focused time per day once meetings, messages and breaks are accounted for. One big task (about two hours), three medium (about three hours) and five small (about one hour) is ambitious but realistic.</p>
<p><strong>Context switching.</strong> Grouping similar-sized tasks lets you batch: deep work in sprints, small admin in a single block.</p>
<h2 id="sizing">3. Sizing tasks honestly</h2>
<table><tr><th>Tier</th><th>Typical length</th><th>Examples</th></tr>
<tr><td><strong class="c-big">Big (1)</strong></td><td>90 min – 3 h</td><td>Write a proposal, ship a feature, record a video, study a chapter</td></tr>
<tr><td><strong class="c-med">Medium (3)</strong></td><td>30 – 90 min</td><td>Review a document, prepare a meeting, edit a draft, plan a campaign</td></tr>
<tr><td><strong class="c-small">Small (5)</strong></td><td>under 15 min</td><td>Reply to a message, pay a bill, book an appointment, file a receipt</td></tr></table>
<p>Two rules keep sizing honest. First, anything over three hours isn't a task — it's a project, and today's Big task is its next meaningful chunk. Second, write tasks as outcomes ("Send v1 of the pricing page to Alex") rather than activities ("Work on pricing"). Outcomes have finish lines; activities expand to fill the day.</p>
<p>If you aren't sure, use the <a href="tools.html#estimate">task time estimator</a>. It applies a buffer for the planning fallacy — our tendency to underestimate our own tasks — and tells you which tier the task belongs in.</p>
<h2 id="sprints">4. The two focus sprints</h2>
<p>A list without protected time is a wish list. The 13522 method schedules two focus sprints: uninterrupted blocks of 25, 50 or 90 minutes with notifications off and only the relevant window open.</p>
<ul><li><strong>Sprint one</strong> goes to the Big task, ideally in the first half of the day.</li><li><strong>Sprint two</strong> finishes the Big task or tackles the most important Medium task.</li><li>Take a real break between sprints — stand up, walk, get water. Screens don't count.</li></ul>
<p>Twenty-five minutes suits days when focus is hard. Fifty minutes suits most knowledge work. Ninety minutes suits deep creative or technical work once you're practised. The <a href="planner.html">planner</a> includes a timer that marks each sprint complete automatically.</p>
<h2 id="reviews">5. The two reviews</h2>
<p><strong>Morning (3 minutes).</strong> Check your calendar, confirm the nine tasks, and write one sentence: "Today is a win if…". Add one line about what might get in the way and what you'll do if it happens.</p>
<p><strong>Evening (5 minutes).</strong> Tick off what's done. For anything unfinished, decide: carry over, delegate, or drop. Then choose tomorrow's Big task. This single habit — deciding tomorrow's Big task tonight — is the highest-leverage part of the system.</p>
<p>On Fridays, extend the evening review into a weekly review: look at the week's scores, notice what keeps carrying over, and pick next week's five Big tasks.</p>
<h2 id="day">6. A sample 13522 day</h2>
<table><tr><th>Time</th><th>Block</th></tr>
<tr><td>8:45</td><td>Morning review (3 min)</td></tr><tr><td>8:50 – 9:40</td><td>Sprint 1 — Big task</td></tr><tr><td>9:40 – 10:00</td><td>Break, messages</td></tr><tr><td>10:00 – 11:00</td><td>Medium task 1 / meetings</td></tr><tr><td>11:00 – 11:50</td><td>Sprint 2 — finish Big task</td></tr><tr><td>13:30 – 14:15</td><td>Batch all 5 small tasks</td></tr><tr><td>14:15 – 16:30</td><td>Medium tasks 2 and 3, meetings</td></tr><tr><td>17:00</td><td>Evening review, pick tomorrow's Big (5 min)</td></tr></table>
<h2 id="adapt">7. Adapting it to your life</h2>
<ul><li><strong>Meeting-heavy days:</strong> scale to 1·2·3. The Big task stays.</li><li><strong>Students:</strong> the Big task is one study session with a clear target ("practice exam section B").</li><li><strong>Parents and caregivers:</strong> run a lighter home list in parallel, or use the five small slots for household admin.</li><li><strong>Shift workers:</strong> plan per shift rather than per calendar day; the evening review becomes your end-of-shift handover.</li><li><strong>Teams:</strong> each person shares only their Big task at stand-up. See <a href="blog/1-3-5-for-teams.html">running a team on 1-3-5</a>.</li></ul>
<h2 id="mistakes">8. Common mistakes</h2>
<ul><li><strong>Two Big tasks.</strong> If both feel essential, one of them is tomorrow's.</li><li><strong>Inflated small tasks.</strong> "Clean up the inbox" is not small. "Reply to the three client emails" is.</li><li><strong>No minutes.</strong> Without estimates you can't see when the plan is impossible.</li><li><strong>Skipping the evening review.</strong> The next morning starts with decisions instead of work.</li><li><strong>Treating carry-overs as failure.</strong> They're data. Three in a row means the task needs redefining, delegating or dropping.</li></ul>
<h2 id="start">9. Start today</h2>
<p>Open the <a href="planner.html">free planner</a>, paste your list into Smart Sort, and choose your Big task. Run one sprint before lunch. Tonight, do the five-minute review and pick tomorrow's Big task. That's the whole system.</p>
<div class="callout">Want this for your whole team? <a href="teams.html">Get a free team focus plan →</a></div>
</div></article>
"""
    art = {"@context": "https://schema.org", "@type": "Article", "headline": "The complete guide to the 13522 method", "author": {"@type": "Organization", "name": "13522"}, "publisher": {"@type": "Organization", "name": "13522"}, "mainEntityOfPage": "https://13522.com/guide.html"}
    return ("guide.html", "The 1-3-5 Rule Guide: The Complete 13522 Method",
            "A complete guide to the 1-3-5 rule and the 13522 method: task sizing, two focus sprints, morning and evening reviews, a sample day and common mistakes.",
            body, (), art)


def templates():
    def sheet(title, rows):
        lines = "".join(f'<tr><td style="width:34px;font-weight:700;color:{c}">{n}</td><td style="height:30px;border-bottom:1px solid var(--line)"></td><td style="width:60px;border-bottom:1px solid var(--line)"></td></tr>' for n, c in rows)
        return lines
    rows = [("1", "var(--big)")] + [("3", "var(--med)")] * 3 + [("5", "var(--small)")] * 5
    day = sheet("Daily", rows)
    body = f"""
<section class="hero" style="padding-bottom:10px"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Templates</div>
<h1>Printable 1-3-5 planner templates</h1>
<p class="lede">Free paper templates for daily, weekly and team planning. Click print — the page prints just the sheet.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap">
<div class="grid-2">
<div class="card"><span class="tag">Daily</span><h2>13522 daily sheet</h2>
<p><strong>Date:</strong> ____________ &nbsp; <strong>Today is a win if:</strong> ______________________</p>
<table><tr><th></th><th>Task</th><th>Min</th></tr>{day}</table>
<p><strong>Sprint 1</strong> ☐ &nbsp; <strong>Sprint 2</strong> ☐</p>
<p><strong>Evening review:</strong> done / carry / drop · tomorrow's Big: ______________________</p>
<button class="btn btn-dark btn-sm noprint" onclick="window.print()">Print</button></div>
<div class="card"><span class="tag">Weekly</span><h2>Weekly Big-task planner</h2>
<table><tr><th>Day</th><th>Big task</th><th>Score</th></tr>{"".join(f"<tr><td>{d}</td><td style='height:34px;border-bottom:1px solid var(--line)'></td><td style='width:60px;border-bottom:1px solid var(--line)'></td></tr>" for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])}</table>
<p><strong>Weekly review:</strong> What kept carrying over? What will I drop or delegate? Next week's five Big tasks:</p>
<button class="btn btn-dark btn-sm noprint" onclick="window.print()">Print</button></div>
<div class="card"><span class="tag">Team</span><h2>Stand-up board</h2>
<table><tr><th>Name</th><th>Today's Big task</th><th>Blocker?</th></tr>{"".join("<tr><td style='height:34px;border-bottom:1px solid var(--line)'></td><td style='border-bottom:1px solid var(--line)'></td><td style='width:90px;border-bottom:1px solid var(--line)'></td></tr>" for _ in range(8))}</table>
<button class="btn btn-dark btn-sm noprint" onclick="window.print()">Print</button></div>
<div class="card"><span class="tag">Study</span><h2>Student exam-week sheet</h2>
<p>Big = one focused study session with a target. Medium = practice sets or readings. Small = admin, flashcards, emails.</p>
<table><tr><th></th><th>Target</th><th>Done</th></tr>{day}</table>
<button class="btn btn-dark btn-sm noprint" onclick="window.print()">Print</button></div>
</div>
<div class="callout" style="margin-top:28px">Prefer digital? The <a href="planner.html">online planner</a> saves automatically and carries unfinished tasks to tomorrow. Want branded templates for your company? <a href="teams.html">Ask us</a>.</div>
</div></section>
"""
    return ("templates.html", "Printable 1-3-5 Planner Templates (Free)",
            "Free printable 1-3-5 planner templates: daily 13522 sheet, weekly Big-task planner, team stand-up board and student exam-week sheet.",
            body, (), None)


def videos():
    body = f"""
<section class="hero" style="padding-bottom:10px"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Videos</div>
<h1>Productivity videos: focus, planning & AI</h1>
<p class="lede">Curated topics with the best explainers on YouTube. Click a card to watch.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap"><div class="grid-3" id="videos"></div></div></section>
<section class="alt"><div class="wrap narrow">
<h2>Suggest a video or feature yours</h2>
<p>Made a great video about focus, planning or productivity tools? Send it in. Selected creators are featured here and in the newsletter. Sponsored placements are clearly labelled.</p>
<form class="card" data-form="video-submission" data-subject="Video submission" data-ok="Thanks — we review submissions every week.">
<div class="row2"><div class="field"><label for="v-name">Your name</label><input id="v-name" name="name" required></div><div class="field"><label for="v-email">Email</label><input id="v-email" type="email" name="email" required></div></div>
<div class="field"><label for="v-url">YouTube URL</label><input id="v-url" type="url" name="video_url" required placeholder="https://www.youtube.com/watch?v=…"></div>
<div class="field"><label for="v-why">Why it's useful (one or two sentences)</label><textarea id="v-why" name="message" rows="3"></textarea></div>
<div class="field"><label for="v-type">Submission type</label><select id="v-type" name="submission_type"><option>Free suggestion</option><option>I'm the creator — feature request</option><option>Paid sponsored placement</option></select></div>
{hp()}{consent()}<button class="btn btn-primary" type="submit">Submit video</button><div class="form-msg" role="status"></div></form>
</div></section>
"""
    return ("videos.html", "Productivity Videos — Focus, Planning, 1-3-5 Rule & AI",
            "Curated productivity videos on the 1-3-5 rule, deep work focus sprints, weekly reviews, time blocking, procrastination and AI planning tools.",
            body, ("pages.js",), None)


def ai_tools():
    body = """
<section class="hero" style="padding-bottom:10px"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › AI tools</div>
<h1>AI & productivity tools directory</h1>
<p class="lede">30 tools that work well with the 13522 method — task managers, AI schedulers, assistants, focus apps and automation — with a tip for using each one.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap">
<input class="search" id="dir-search" type="search" placeholder="Search tools (e.g. calendar, timer, notes)…" aria-label="Search tools">
<div class="filters" id="dir-filters"></div><p id="dir-count" style="color:var(--muted);font-size:.9rem"></p>
<div class="grid-3" id="directory"></div>
<div class="callout" style="margin-top:28px"><strong>Disclosure:</strong> listings are editorial and not endorsements. Some outbound links may become affiliate or sponsored links in future; any paid placement will be labelled "Sponsored". Product names are trademarks of their owners. <a href="advertise.html">Want your tool featured?</a></div>
</div></section>
<script>(function(){var q=new URLSearchParams(location.search).get("q");if(q)document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){var s=document.getElementById("dir-search");if(s){s.value=q;s.dispatchEvent(new Event("input"));}},400);});})();</script>
"""
    return ("ai-tools.html", "AI Productivity Tools Directory — Planners, Schedulers, Focus Apps",
            "A curated directory of 30 AI and productivity tools — task managers, AI calendars, assistants, note-takers, focus and automation apps — with 1-3-5 setup tips.",
            body, ("pages.js",), None)
