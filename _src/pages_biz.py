"""Revenue + trust pages: teams (lead gen), contests, careers, support, advertise, about, contact, legal, 404."""
from layout import hp, consent, INQUIRY_URL


def opts(items):
    return "".join(f'<button type="button" data-v="{v}">{t}</button>' for t, v in items)


def teams():
    qs = [
        ("size", "How big is your team?", [("1–10 people", 0), ("11–25", 1), ("26–75", 2), ("76–200", 3), ("200+", 4)]),
        ("clarity", "Could everyone on your team name today's single most important task?", [("Yes, always", 0), ("Mostly", 1), ("Sometimes", 3), ("Rarely", 5)]),
        ("meetings", "How many hours of meetings does a typical person have per day?", [("Under 1 hour", 0), ("1–2 hours", 1), ("2–4 hours", 3), ("4+ hours", 5)]),
        ("switching", "How often is focused work interrupted by messages or urgent requests?", [("Rarely", 0), ("A few times a day", 2), ("Hourly", 3), ("Constantly", 5)]),
        ("carry", "How often do planned tasks slip to the next week?", [("Almost never", 0), ("Sometimes", 1), ("Often", 3), ("It's normal here", 4)]),
    ]
    qhtml = ""
    for k, q, o in qs:
        qhtml += f'<div class="q" data-key="{k}"><h3>{q}</h3><div class="opts">{opts(o)}</div><button type="button" class="btn btn-ghost btn-sm" data-back>← Back</button></div>'
    body = f"""
<section class="hero"><div class="wrap grid">
<div>
<span class="eyebrow">13522 for Teams</span>
<h1>Give your team one clear priority every day.</h1>
<p class="lede">Teams lose hours every week to unclear priorities, context switching and status-chasing. The 13522 rollout gives every person one Big task, protected focus time and a 60-second stand-up — with no new software to buy.</p>
<div class="actions"><a class="btn btn-primary" href="#assessment">Take the 60-second assessment →</a><a class="btn btn-ghost" href="#packages">See packages</a></div>
<div class="trust"><span>Free focus plan</span><span>Works with your existing tools</span><span>Remote & hybrid friendly</span></div>
</div>
<div class="card" id="assessment" style="scroll-margin-top:90px">
<div class="steps">{"".join("<i></i>" for _ in range(len(qs)+1))}</div>
{qhtml}
<div class="q" data-key="done"><div id="q-result"></div>
<form id="lead-form" data-form="team-assessment" data-subject="Team focus assessment lead" data-ok="Thank you! Your team focus plan will arrive within 1 business day.">
<div class="row2"><div class="field"><label for="tl-name">Name</label><input id="tl-name" name="name" required autocomplete="name"></div><div class="field"><label for="tl-email">Work email</label><input id="tl-email" type="email" name="email" required autocomplete="email"></div></div>
<div class="row2"><div class="field"><label for="tl-co">Company</label><input id="tl-co" name="company" autocomplete="organization"></div><div class="field"><label for="tl-role">Your role</label><select id="tl-role" name="role"><option>Founder / CEO</option><option>Manager / team lead</option><option>HR / People</option><option>Operations</option><option>Individual contributor</option></select></div></div>
<div class="field"><label for="tl-want">What would help most?</label><select id="tl-want" name="interest"><option>Just the free plan</option><option>Free plan + 30-minute call</option><option>Team workshop (remote or on-site)</option><option>Custom templates / internal training</option></select></div>
{hp()}{consent()}
<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Send my team focus plan →</button><div class="form-msg" role="status"></div>
<p class="form-note">We reply personally. No spam, no sharing your details.</p></form>
<button type="button" class="btn btn-ghost btn-sm" data-back>← Back</button></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="sec-head"><h2>What changes in the first two weeks</h2></div>
<div class="grid-4">
<div class="card"><div class="stat c-big">1</div><h3>Big task each</h3><p>Every person names one outcome for the day. Managers see priorities, not activity.</p></div>
<div class="card"><div class="stat c-med">60s</div><h3>Stand-ups</h3><p>Each person says their Big task and one blocker. That's it.</p></div>
<div class="card"><div class="stat c-sprint">2</div><h3>Focus sprints</h3><p>Shared no-meeting windows so deep work actually happens.</p></div>
<div class="card"><div class="stat c-review">5m</div><h3>Daily close</h3><p>Five-minute async review: done, carried, blocked, tomorrow's Big.</p></div>
</div></div></section>

<section id="packages"><div class="wrap">
<div class="sec-head"><h2>Ways we can help</h2><p>Start free. Upgrade only if you want hands-on help.</p></div>
<div class="grid-3">
<div class="card"><span class="tag">Free</span><h3>Team Focus Plan</h3><p>A one-page rollout plan based on your assessment: stand-up script, sprint windows, weekly review agenda and templates for your tools.</p><a class="btn btn-dark btn-sm" href="#assessment">Get the plan</a></div>
<div class="card" style="border:2px solid var(--accent)"><span class="tag" style="background:var(--accent);color:#fff">Most popular</span><h3>Live workshop</h3><p>A 90-minute interactive session (remote or on-site) where your team sets up 13522 in the tools you already use and plans their first week together.</p><a class="btn btn-primary btn-sm" href="#assessment">Request a workshop</a></div>
<div class="card"><span class="tag">Custom</span><h3>Rollout & training</h3><p>Branded templates, manager training, a 30-day check-in and an internal champion programme for larger organisations.</p><a class="btn btn-dark btn-sm" href="contact.html">Talk to us</a></div>
</div></div></section>

<section class="alt"><div class="wrap narrow faq">
<h2>Team FAQ</h2>
<details><summary>Do we need new software?</summary><p>No. 13522 works in Asana, ClickUp, Notion, Trello, Todoist, Microsoft To Do, or a shared doc. The free plan includes setup notes for common tools.</p></details>
<details><summary>Is this surveillance?</summary><p>No. People share one priority, not their screen time. The method is built on trust and clarity, not monitoring.</p></details>
<details><summary>How long does a rollout take?</summary><p>Most teams are running it within a week. Two weeks of daily use is enough to see whether carry-overs and meeting load are improving.</p></details>
<details><summary>What does a workshop cost?</summary><p>It depends on team size and format. Request one through the form and we'll send a quote with no obligation.</p></details>
</div></section>
"""
    return ("teams.html", "13522 for Teams — Free Team Focus Plan & Workshops",
            "Give every person on your team one clear priority a day. Take the 60-second team focus assessment and get a free rollout plan, or book a workshop.",
            body, ("pages.js",), None, True)


def contests():
    body = f"""
<section class="hero"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Monthly challenge</div>
<span class="eyebrow">Free to enter</span>
<h1>The 13522 Monthly Challenge</h1>
<p class="lede">Plan with 13522 every day this month. Log 20 or more winning days (score 60%+) and enter the prize draw. Bonus categories for the best evening reviews and the most creative setups.</p>
<div class="actions"><a class="btn btn-primary" href="#enter">Enter this month</a><a class="btn btn-ghost" href="planner.html">Open the planner</a></div>
</div></section>
<section class="alt"><div class="wrap">
<div class="grid-3">
<div class="card"><div class="icon">🏆</div><h3>Consistency draw</h3><p>Everyone with 20+ winning days is entered into a random draw for the main prize of the month.</p></div>
<div class="card"><div class="icon">✍️</div><h3>Best reflection</h3><p>Share your best evening-review insight (anonymised if you like). Chosen by the editors.</p></div>
<div class="card"><div class="icon">🛠️</div><h3>Best setup</h3><p>Show how you run 13522 in your favourite app, on paper or with your team.</p></div>
</div>
<p style="margin-top:22px">Prizes are funded by sponsors and community support and are announced at the start of each month (typically gift cards, productivity app subscriptions or books). Want to put up a prize? <a href="advertise.html">Sponsor a challenge</a>.</p>
</div></section>
<section id="enter"><div class="wrap narrow">
<h2>Enter the challenge</h2>
<form class="card" data-form="contest-entry" data-subject="Monthly challenge entry" data-ok="You're entered! Keep planning — we'll email you at the end of the month.">
<div class="row2"><div class="field"><label for="c-name">Name</label><input id="c-name" name="name" required></div><div class="field"><label for="c-email">Email</label><input id="c-email" type="email" name="email" required></div></div>
<div class="row2"><div class="field"><label for="c-cat">Category</label><select id="c-cat" name="category"><option>Consistency draw</option><option>Best reflection</option><option>Best setup</option></select></div><div class="field"><label for="c-days">Winning days so far</label><input id="c-days" type="number" name="winning_days" min="0" max="31"></div></div>
<div class="field"><label for="c-entry">Your entry (reflection, setup description or link)</label><textarea id="c-entry" name="entry" rows="4"></textarea></div>
<div class="field"><label for="c-country">Country</label><input id="c-country" name="country" required></div>
<label class="check"><input type="checkbox" name="age_confirm" value="18+" required> I confirm I am 18 or older (or the age of majority where I live) and I accept the official rules below.</label>
{hp()}<button class="btn btn-primary" type="submit">Submit entry</button><div class="form-msg" role="status"></div></form>
<h2 style="margin-top:40px">Official rules (summary)</h2>
<ul style="color:var(--ink2)">
<li><strong>No purchase necessary.</strong> Purchasing or donating does not improve your chances of winning.</li>
<li>Open to individuals 18+ (or the age of majority in their jurisdiction). Void where prohibited or restricted by law.</li>
<li>Each challenge runs from the first to the last day of the calendar month. One entry per person per category.</li>
<li>Consistency-draw winners are chosen at random from eligible entries; reflection and setup winners are chosen by editors on originality, usefulness and clarity.</li>
<li>Winning-day counts are self-reported; we may ask for a screenshot or exported plan to verify.</li>
<li>Winners are notified by email within 14 days of the month's end and must reply within 14 days or an alternate winner may be selected.</li>
<li>Prizes are non-transferable and have no cash alternative unless stated. Winners are responsible for any taxes.</li>
<li>By entering a reflection or setup, you grant 13522.com permission to publish it (with or without your name, as you choose).</li>
<li>13522.com may modify or cancel a challenge if it cannot run as planned. The challenge is not sponsored, endorsed or administered by Google or any app mentioned on this site.</li>
</ul>
</div></section>
"""
    return ("contests.html", "13522 Monthly Challenge — Plan Daily, Win Prizes",
            "Join the free 13522 monthly productivity challenge: log 20 winning days to enter the prize draw, plus awards for best reflection and best setup.",
            body, (), None)


def careers():
    roles = [
        ("Freelance productivity writer", "Content", "Write practical, original guides on planning, focus and tools. Research-backed, no fluff."),
        ("Video creator / editor", "Video", "Produce short explainers and tool walkthroughs for YouTube and social."),
        ("Front-end developer (contract)", "Engineering", "Build new interactive tools and improve performance and accessibility on a static stack."),
        ("Community & contest coordinator", "Community", "Run the monthly challenge, review entries and manage prizes and sponsors."),
        ("Partnerships & ad sales (commission)", "Growth", "Bring in sponsors for the planner, newsletter and challenges."),
        ("Productivity coach / workshop facilitator", "Teams", "Lead 13522 workshops for client teams, remote or on-site."),
    ]
    cards = "".join(f'<div class="card"><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p><p style="font-size:.88rem;color:var(--muted)">Remote · flexible · paid per project</p></div>' for n, t, d in roles)
    ropts = "".join(f"<option>{n}</option>" for n, _, _ in roles)
    body = f"""
<section class="hero"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Careers</div>
<span class="eyebrow">We're hiring</span>
<h1>Help millions of people do what matters</h1>
<p class="lede">13522 is a small, remote-first project. We work with independent writers, creators, developers and coaches on paid, flexible projects.</p>
</div></section>
<section class="alt"><div class="wrap"><div class="grid-3">{cards}</div></div></section>
<section><div class="wrap narrow">
<h2>Apply or introduce yourself</h2>
<form class="card" data-form="job-application" data-subject="Career application" data-ok="Thanks for applying — we read every application and reply within two weeks.">
<div class="row2"><div class="field"><label for="j-name">Full name</label><input id="j-name" name="name" required></div><div class="field"><label for="j-email">Email</label><input id="j-email" type="email" name="email" required></div></div>
<div class="row2"><div class="field"><label for="j-role">Role</label><select id="j-role" name="role">{ropts}<option>Other</option></select></div><div class="field"><label for="j-loc">Location / time zone</label><input id="j-loc" name="location"></div></div>
<div class="field"><label for="j-port">Portfolio, LinkedIn or work samples (URL)</label><input id="j-port" type="url" name="portfolio" placeholder="https://"></div>
<div class="row2"><div class="field"><label for="j-rate">Expected rate</label><input id="j-rate" name="rate" placeholder="e.g. $40/h or per project"></div><div class="field"><label for="j-avail">Availability</label><select id="j-avail" name="availability"><option>A few hours a week</option><option>Part-time</option><option>Project-based</option></select></div></div>
<div class="field"><label for="j-msg">Why 13522? What would you build or write first?</label><textarea id="j-msg" name="message" rows="5" required></textarea></div>
{hp()}{consent()}<button class="btn btn-primary" type="submit">Send application</button><div class="form-msg" role="status"></div></form>
<p class="form-note">We're an equal-opportunity collaborator and welcome applicants from every background.</p>
</div></section>
"""
    return ("careers.html", "Careers at 13522 — Remote Writers, Creators, Developers, Coaches",
            "Join 13522 as a freelance productivity writer, video creator, front-end developer, community coordinator, partnerships lead or workshop facilitator.",
            body, (), None)


def support():
    tiers = [("Coffee", 5, "Covers a day of hosting and tools"), ("Sprint", 22, "Funds a new printable or calculator"), ("Champion", 135, "Sponsors a month of challenge prizes"), ("Custom", "", "Choose any amount")]
    tb = "".join(f'<div class="card tierbtn" data-amt="{a}" data-name="{n}" role="button" tabindex="0"><span class="tag">{n}</span><div class="amt">{("$"+str(a)) if a else "Any"}</div><p>{d}</p></div>' for n, a, d in tiers)
    alloc = [("Operations & hosting", 30, "var(--small)"), ("New tools & content", 25, "var(--sprint)"), ("Contest prizes", 15, "var(--med)"), ("Hiring contributors", 15, "var(--big)"), ("Promotion & marketing", 15, "var(--review)")]
    ah = "".join(f'<div><div style="display:flex;justify-content:space-between;font-size:.92rem"><span>{n}</span><strong>{p}%</strong></div><div class="bar"><i style="width:{p}%;background:{c}"></i></div></div>' for n, p, c in alloc)
    body = f"""
<section class="hero"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Support</div>
<span class="eyebrow">Support the project</span>
<h1>Keep 13522 free for everyone</h1>
<p class="lede">The planner, tools and guides are free with no account. Your support pays for operations, new tools, promotion, contributors and the monthly challenge prizes.</p>
</div></section>
<section style="padding-top:10px"><div class="wrap">
<div class="tiers" id="tiers">{tb}</div>
<div class="grid-2" style="margin-top:34px">
<div class="card"><h2>Where your support goes</h2><div class="alloc">{ah}</div><p class="form-note" style="margin-top:14px">Target allocation; we publish a short update on how funds were used each quarter.</p></div>
<div class="card" id="support-form" style="scroll-margin-top:90px"><h2>Make a pledge</h2>
<p>Choose an amount and purpose. We'll email you a secure payment link (card or PayPal) and a receipt. Prefer to sponsor something bigger? <a href="advertise.html">See sponsorships</a>.</p>
<form data-form="donation-pledge" data-subject="Donation / support pledge" data-ok="Thank you! We'll email your secure payment link shortly.">
<input type="hidden" id="d-tier" name="tier" value="">
<div class="row2"><div class="field"><label for="d-amount">Amount (USD)</label><input id="d-amount" type="number" name="amount" min="1" required></div><div class="field"><label for="d-freq">Frequency</label><select id="d-freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="field"><label for="d-purpose">Direct my support to</label><select id="d-purpose" name="purpose"><option>Wherever it's most needed</option><option>Ongoing operations & hosting</option><option>Promotions & marketing</option><option>Hiring talent / contributors</option><option>Running contests</option><option>Prizes for winners</option></select></div>
<div class="row2"><div class="field"><label for="d-name">Name</label><input id="d-name" name="name" required></div><div class="field"><label for="d-email">Email</label><input id="d-email" type="email" name="email" required></div></div>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters list</label>
{hp()}<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Pledge support →</button><div class="form-msg" role="status"></div>
<p class="form-note">13522.com is not a registered charity; contributions are not tax-deductible.</p></form></div>
</div>
<div class="grid-3" style="margin-top:34px">
<div class="card"><h3>Other ways to help</h3><p>Share the planner with a friend or team, link to a guide from your blog, or suggest a tool we should build.</p></div>
<div class="card"><h3>Contribute work</h3><p>Writers, creators and developers can join paid projects on the <a href="careers.html">careers page</a>.</p></div>
<div class="card"><h3>Fund a prize</h3><p>Businesses can sponsor a monthly challenge and get featured to every participant. <a href="advertise.html">Details</a>.</p></div>
</div>
</div></section>
"""
    return ("support.html", "Support 13522 — Donate to Keep the Planner Free",
            "Support 13522 with a one-time or monthly contribution. Funds operations, new tools, promotion, hiring contributors, contests and prizes.",
            body, ("pages.js",), None)


def advertise():
    pk = [("Planner sponsor", "Logo and one-line message beside the daily planner — our most-used page.", "Monthly"), ("Newsletter sponsor", "Featured slot in the weekly email with a short native write-up.", "Per issue"), ("Challenge sponsor", "Fund the monthly prize and get featured to every participant.", "Monthly"), ("Featured tool listing", "Highlighted placement in the AI & productivity tools directory, labelled Sponsored.", "Quarterly"), ("Sponsored guide or video", "A clearly labelled, editorially reviewed guide or video about your product.", "Per piece"), ("Partnerships", "Integrations, co-branded templates, workshops or licensing the 13522 method content.", "Custom")]
    cards = "".join(f'<div class="card"><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for n, d, t in pk)
    po = "".join(f"<option>{n}</option>" for n, _, _ in pk)
    body = f"""
<section class="hero"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Advertise</div>
<span class="eyebrow">Advertise · Sponsor · Partner</span>
<h1>Reach people at the moment they plan their day</h1>
<p class="lede">13522 visitors are professionals, founders, students and team leads actively choosing how to spend their time — the ideal audience for productivity, SaaS, education and wellbeing brands.</p>
<div class="actions"><a class="btn btn-primary" href="#inquire">Request the media kit</a><a class="btn btn-ghost" href="{INQUIRY_URL}" target="_blank" rel="noopener">Domain / website acquisition inquiries ↗</a></div>
</div></section>
<section class="alt"><div class="wrap"><div class="grid-3">{cards}</div>
<p style="margin-top:20px;color:var(--ink2)">All sponsored content is clearly labelled. We only accept brands relevant and useful to our audience and reserve the right to decline any placement.</p></div></section>
<section id="inquire"><div class="wrap narrow">
<h2>Advertising & partnership inquiry</h2>
<form class="card" data-form="advertising-inquiry" data-subject="Advertising / sponsorship / partnership inquiry" data-ok="Thanks — we'll send the media kit and availability within 1–2 business days.">
<div class="row2"><div class="field"><label for="a-name">Name</label><input id="a-name" name="name" required></div><div class="field"><label for="a-email">Work email</label><input id="a-email" type="email" name="email" required></div></div>
<div class="row2"><div class="field"><label for="a-co">Company / brand</label><input id="a-co" name="company" required></div><div class="field"><label for="a-site">Website</label><input id="a-site" type="url" name="website" placeholder="https://"></div></div>
<div class="row2"><div class="field"><label for="a-type">Interested in</label><select id="a-type" name="interest">{po}<option>Buying the 13522.com domain / website</option></select></div><div class="field"><label for="a-budget">Budget range</label><select id="a-budget" name="budget"><option>Under $500</option><option>$500 – $2,000</option><option>$2,000 – $10,000</option><option>$10,000+</option><option>Not sure yet</option></select></div></div>
<div class="field"><label for="a-msg">Goals and timing</label><textarea id="a-msg" name="message" rows="4"></textarea></div>
{hp()}{consent()}<button class="btn btn-primary" type="submit">Send inquiry</button><div class="form-msg" role="status"></div></form>
</div></section>
"""
    return ("advertise.html", "Advertise, Sponsor or Partner with 13522",
            "Sponsor the 13522 planner, newsletter or monthly challenge, get a featured tool listing, or propose a partnership. Request the media kit.",
            body, (), None)


def about():
    body = """
<article class="article"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › About</div>
<h1>About 13522</h1>
<p class="lede">13522 is an independent website that helps people decide what matters each day and actually get it done.</p>
<p>The name is the method: <strong>1</strong> big task, <strong>3</strong> medium tasks, <strong>5</strong> small tasks, <strong>2</strong> focus sprints and <strong>2</strong> reviews. It builds on the widely used 1-3-5 to-do list and adds the two habits that, in our experience, make the biggest difference: protecting time for focused work and closing each day with a short review.</p>
<h2>What we publish</h2>
<ul><li>A free, private <a href="planner.html">daily planner</a> that runs in your browser.</li><li>Free <a href="tools.html">calculators</a> for meetings, time value and capacity.</li><li>Original <a href="blog/index.html">guides</a> and a curated <a href="ai-tools.html">tools directory</a>.</li><li>A <a href="contests.html">monthly challenge</a> with prizes, and <a href="teams.html">resources for teams</a>.</li></ul>
<h2>How we make money</h2>
<p>The site is supported by advertising (served by Google AdSense), clearly labelled sponsorships, optional team workshops and voluntary <a href="support.html">contributions</a>. Advertisers never influence our editorial content or rankings.</p>
<h2>Editorial standards</h2>
<p>Our guides are written from practical experience and widely accepted research on attention, planning and habits. We avoid exaggerated claims, correct mistakes quickly and update articles regularly. Spotted an error? <a href="contact.html">Tell us</a>.</p>
<h2>Independence</h2>
<p>13522 is not affiliated with any app, company or organisation mentioned on the site, or with any other entity that uses the number 13522. See our <a href="trademark.html">trademark & copyright disclosure</a>.</p>
</div></article>
"""
    return ("about.html", "About 13522", "About 13522: an independent website with a free daily planner, tools and guides built on the 1-3-5 method plus focus sprints and reviews.", body, (), None)


def contact():
    body = f"""
<section class="hero"><div class="wrap narrow">
<div class="crumbs"><a href="index.html">Home</a> › Contact</div>
<h1>Contact us</h1>
<p class="lede">Questions, feedback, corrections, partnerships or press — send a message and we'll reply within 1–2 business days.</p>
<form class="card" data-form="contact" data-subject="Contact form" data-ok="Thanks — your message has been sent. We'll reply within 1–2 business days.">
<div class="row2"><div class="field"><label for="ct-name">Name</label><input id="ct-name" name="name" required autocomplete="name"></div><div class="field"><label for="ct-email">Email</label><input id="ct-email" type="email" name="email" required autocomplete="email"></div></div>
<div class="field"><label for="ct-topic">Topic</label><select id="ct-topic" name="topic"><option>General question</option><option>Feedback / feature idea</option><option>Correction</option><option>Teams & workshops</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Website or domain acquisition</option><option>Press</option><option>Privacy request</option></select></div>
<div class="field"><label for="ct-msg">Message</label><textarea id="ct-msg" name="message" rows="6" required></textarea></div>
{hp()}{consent()}<button class="btn btn-primary" type="submit">Send message</button><div class="form-msg" role="status"></div></form>
<p class="form-note" style="margin-top:18px">Interested in this website, the domain name, sponsorship, advertising or partnership? You can also use our <a href="{INQUIRY_URL}" target="_blank" rel="noopener">business inquiry page ↗</a>.</p>
</div></section>
"""
    return ("contact.html", "Contact 13522", "Contact 13522 for questions, feedback, corrections, teams, advertising, partnerships or press.", body, (), None)


def legal(path, title, desc, inner):
    body = f'<article class="article"><div class="wrap narrow"><div class="crumbs"><a href="index.html">Home</a> › {title}</div><h1>{title}</h1><p class="meta">Last updated: November 2026</p>{inner}</div></article>'
    return (path, title, desc, body, (), None)


def privacy():
    return legal("privacy.html", "Privacy policy", "How 13522.com collects, uses and protects information, including cookies and Google AdSense advertising.", """
<p>This policy explains what information 13522.com ("we", "us") collects and how it is used. By using the site you agree to this policy.</p>
<h2>Information you give us</h2>
<p>When you submit a form (contact, newsletter, team assessment, donation pledge, contest entry, job application, advertising inquiry or video submission) we receive the details you enter, such as your name, email address and message. Form submissions are delivered to us by a third-party form-processing service (FormSubmit). We use this information only to respond to you and provide what you requested. We do not sell your personal information.</p>
<h2>Planner data</h2>
<p>Tasks, reviews, timer settings and scores you enter in the planner are stored only in your browser's local storage on your device. We cannot see or access them. Clearing your browser data deletes them.</p>
<h2>Cookies and advertising</h2>
<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visits to this and/or other sites on the Internet.</p>
<p>You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>, or opt out of some third-party vendors' use of cookies at <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">www.aboutads.info</a>. Learn more in <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>.</p>
<p>Visitors in the EEA, UK and Switzerland will be asked for consent where required by law before personalised ads are shown.</p>
<h2>Embedded content</h2>
<p>Videos open on YouTube or play via youtube-nocookie.com embeds only after you click. Fonts are loaded from Google Fonts. These services may collect technical data such as your IP address under their own privacy policies.</p>
<h2>Analytics and logs</h2>
<p>Our host (GitHub Pages) may keep standard server logs, including IP addresses, for security and operations.</p>
<h2>Your rights</h2>
<p>Depending on where you live (for example under GDPR, UK GDPR, PIPEDA or CCPA/CPRA) you may have rights to access, correct or delete personal information we hold and to object to certain processing. Use the <a href="contact.html">contact form</a> and choose "Privacy request".</p>
<h2>Children</h2>
<p>This site is not directed to children under 13 and we do not knowingly collect their personal information.</p>
<h2>Retention and security</h2>
<p>We keep form submissions only as long as needed to respond and for legitimate record-keeping, then delete them. We use reasonable safeguards, but no method of transmission over the Internet is completely secure.</p>
<h2>Changes</h2>
<p>We may update this policy and will change the date above when we do.</p>
""")


def terms():
    return legal("terms.html", "Terms of use", "Terms of use for 13522.com, its planner, tools, contests and content.", """
<p>By accessing 13522.com you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Use of the site</h2><p>The planner, calculators and content are provided free for personal and internal business use. You may not copy, republish or resell the site's content or code in bulk, scrape it, or use it in a way that harms the site or other users.</p>
<h2>No professional advice</h2><p>Content is for general information only and is not professional, financial, legal, medical or psychological advice. Calculator results are estimates.</p>
<h2>User submissions</h2><p>You are responsible for what you submit. By submitting content (for example a contest entry or video suggestion) you confirm you have the right to share it and grant us a non-exclusive licence to use it as described on the relevant page.</p>
<h2>Contests</h2><p>Contests are governed by the official rules on the <a href="contests.html">challenge page</a>.</p>
<h2>Donations and services</h2><p>Contributions are voluntary and non-refundable except where required by law. Paid services such as workshops are governed by a separate written agreement.</p>
<h2>Third-party links</h2><p>We link to third-party sites and tools for convenience. We are not responsible for their content, products or policies.</p>
<h2>Disclaimer of warranties and limitation of liability</h2><p>The site is provided "as is" without warranties of any kind. To the maximum extent permitted by law, 13522.com is not liable for any indirect, incidental or consequential damages, including loss of data stored in your browser.</p>
<h2>Changes</h2><p>We may update these terms at any time. Continued use after changes means you accept them.</p>
<h2>Contact</h2><p>Questions about these terms? Use the <a href="contact.html">contact form</a>.</p>
""")


def cookies():
    return legal("cookies.html", "Cookie policy", "Which cookies and local storage 13522.com and its partners use.", """
<p>Cookies are small text files stored by your browser. We also use local storage, which works similarly but stays on your device.</p>
<table><tr><th>Name / type</th><th>Set by</th><th>Purpose</th></tr>
<tr><td>p135, h135, sm135 (local storage)</td><td>13522.com</td><td>Your planner tasks, history and timer setting — never leave your device</td></tr>
<tr><td>t135, c135, kit135, lead135 (local storage)</td><td>13522.com</td><td>Theme, cookie choice, and whether to show the starter-kit pop-up</td></tr>
<tr><td>Advertising cookies</td><td>Google and partners</td><td>Serve, personalise and measure ads (Google AdSense)</td></tr>
<tr><td>Embed cookies</td><td>YouTube (only after you click a video)</td><td>Play videos and measure playback</td></tr></table>
<p>You can control cookies in your browser settings and manage ad personalisation at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>. Blocking all cookies may stop the planner from saving.</p>
""")


def disclaimer():
    return legal("disclaimer.html", "Disclaimer", "Disclaimer for 13522.com content, calculators, affiliate links and advertising.", """
<p>All information on 13522.com is published in good faith for general information only. We make no warranties about its completeness, reliability or accuracy, and any action you take based on it is at your own risk.</p>
<h2>Calculators</h2><p>Calculator outputs are simplified estimates based on the numbers you enter and should not be used as the sole basis for business, financial or employment decisions.</p>
<h2>Advertising, sponsorship and affiliate links</h2><p>The site displays ads served by Google AdSense. Some links may in future be affiliate or sponsored links that earn us a commission at no extra cost to you; sponsored placements are labelled. This never affects our editorial opinions.</p>
<h2>Health and wellbeing</h2><p>Productivity content is not a substitute for professional medical or mental-health advice. If you are struggling with stress, burnout or focus, please speak to a qualified professional.</p>
<h2>External links</h2><p>We have no control over the content of external sites and do not endorse every view expressed on them.</p>
""")


def trademark():
    return legal("trademark.html", "Trademark & copyright disclosure", "Trademark and copyright disclosure for 13522.com.", """
<h2>About the name "13522"</h2>
<p>"13522" is used on this website solely as its domain name and as shorthand for this site's own daily-planning format (1 big task, 3 medium tasks, 5 small tasks, 2 focus sprints, 2 reviews). Numbers are generally not distinctive on their own, and <strong>13522.com does not claim any trademark rights in the number 13522</strong>.</p>
<p>13522.com is <strong>not affiliated with, endorsed by or connected to</strong> any company, product, postal area, part number, registration or other organisation that uses the number 13522 or any similar number. Any such use by third parties belongs to them.</p>
<h2>The 1-3-5 rule</h2>
<p>The "1-3-5" to-do list is a widely published, generic productivity technique that is not owned by us. Our explanations, the "13522" extension, the planner software, calculators, templates and articles are our original work.</p>
<h2>Third-party trademarks</h2>
<p>Product and company names mentioned on this site — including Google, YouTube, AdSense and the apps listed in our tools directory — are trademarks or registered trademarks of their respective owners. They are used only to identify those products (nominative fair use) and do not imply endorsement or partnership.</p>
<h2>Copyright</h2>
<p>© 2026 13522.com. Unless otherwise stated, all text, graphics, design, code and templates on this site are protected by copyright. You may print templates and share links freely; you may quote short excerpts with attribution and a link. Republishing full articles or copying the site's code or design requires written permission.</p>
<p>Videos shown on the site are hosted by YouTube and remain the property of their creators. Fonts are licensed under the SIL Open Font License.</p>
<h2>Copyright complaints</h2>
<p>If you believe content on this site infringes your copyright or trademark, please use the <a href="contact.html">contact form</a> (topic: "Correction") with the URL, a description of the work, your contact details and a statement of good-faith belief. We will review and respond promptly.</p>
""")


def notfound():
    body = """<section class="hero"><div class="wrap narrow" style="text-align:center"><div class="stat" style="font-size:5rem"><span class="c-big">4</span><span class="c-med">0</span><span class="c-small">4</span></div><h1>This page isn't on today's list</h1><p class="lede" style="margin:0 auto">The page you're looking for moved or never existed.</p><div class="actions" style="justify-content:center"><a class="btn btn-primary" href="index.html">Go home</a></div></div></section>"""
    return ("404.html", "Page not found", "Page not found on 13522.com.", body, (), None)
