"""Shared layout for every 13522.com page."""
import html
import json

SITE = "https://13522.com"
NAME = "13522"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
INQUIRY_URL = "https://web.works/contact"

NAV = [
    ("index.html", "Home"),
    ("planner.html", "Planner"),
    ("tools.html", "Tools"),
    ("guide.html", "Guide"),
    ("blog/index.html", "Blog"),
    ("videos.html", "Videos"),
    ("ai-tools.html", "AI Tools"),
]
MORE = [
    ("templates.html", "Printable templates"),
    ("contests.html", "Monthly challenge & prizes"),
    ("careers.html", "Careers — we're hiring"),
    ("support.html", "Support 13522"),
    ("advertise.html", "Advertise & sponsor"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]


def esc(s):
    return html.escape(s, quote=True)


def page(path, title, desc, body, *, js=(), schema=None, no_popup=False, og_type="website"):
    depth = path.count("/")
    r = "../" * depth
    canon = SITE + "/" + ("" if path == "index.html" else path)
    full_title = title if NAME in title else f"{title} | {NAME}"

    def nav_link(p, label):
        cur = ' aria-current="page"' if p == path else ""
        return f'<a href="{r}{p}"{cur}>{label}</a>'

    nav = "".join(nav_link(p, l) for p, l in NAV)
    more = "".join(nav_link(p, l) for p, l in MORE)
    ld = [{
        "@context": "https://schema.org", "@type": "WebSite", "name": "13522 — The 1·3·5·2·2 Day",
        "url": SITE + "/", "potentialAction": {"@type": "SearchAction", "target": SITE + "/ai-tools.html?q={q}", "query-input": "required name=q"},
    }, {
        "@context": "https://schema.org", "@type": "Organization", "name": "13522", "url": SITE + "/",
        "logo": SITE + "/assets/img/icon-512.png",
    }]
    if schema:
        ld.append(schema)
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    scripts = "".join(f'<script src="{r}assets/js/{j}" defer></script>' for j in js)
    np = " data-no-popup" if no_popup else ""
    return f"""<!DOCTYPE html>
<html lang="en" data-root="{r}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#15151f">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="13522">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
{ADSENSE}
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/icon-192.png">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{ld_html}
</head>
<body{np}>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><span class="dot" aria-hidden="true"></span><a href="{INQUIRY_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="header"><div class="wrap">
<a class="logo" href="{r}index.html" aria-label="13522 home"><span class="mark" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>13522</a>
<button class="iconbtn menu-btn" aria-label="Menu" aria-expanded="false">☰</button>
<nav class="nav" aria-label="Main">{nav}<div class="more"><button type="button" aria-expanded="false">More ▾</button><div class="drop">{more}</div></div>
<a class="cta" href="{r}teams.html">For Teams</a>
<button class="iconbtn" data-theme-toggle aria-label="Toggle dark mode">◐</button></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="footer"><div class="wrap">
<div class="cols">
<div><a class="logo" href="{r}index.html"><span class="mark" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>13522</a>
<p style="margin-top:12px">1 big · 3 medium · 5 small · 2 focus sprints · 2 reviews. A free planner, tools and guides for doing what matters every day.</p>
<form class="newsletter" data-form="newsletter" data-subject="Newsletter signup" data-ok="You're in. Watch your inbox for the 13522 starter kit.">
<label class="sr" for="nl-email">Email</label><input id="nl-email" type="email" name="email" placeholder="you@email.com" required><input class="hp" name="_honey" tabindex="-1" autocomplete="off"><button class="btn btn-primary btn-sm" type="submit">Join</button><div class="form-msg" role="status"></div></form></div>
<div><h4>Plan</h4><ul><li><a href="{r}planner.html">Daily planner</a></li><li><a href="{r}tools.html">Calculators</a></li><li><a href="{r}templates.html">Printables</a></li><li><a href="{r}guide.html">The 13522 guide</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{r}blog/index.html">Blog</a></li><li><a href="{r}videos.html">Videos</a></li><li><a href="{r}ai-tools.html">AI tools directory</a></li><li><a href="{r}contests.html">Monthly challenge</a></li></ul></div>
<div><h4>Work with us</h4><ul><li><a href="{r}teams.html">13522 for Teams</a></li><li><a href="{r}advertise.html">Advertise & sponsor</a></li><li><a href="{r}careers.html">Careers</a></li><li><a href="{r}support.html">Support / donate</a></li><li><a href="{r}contact.html">Contact</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="{r}privacy.html">Privacy policy</a></li><li><a href="{r}terms.html">Terms of use</a></li><li><a href="{r}cookies.html">Cookie policy</a></li><li><a href="{r}disclaimer.html">Disclaimer</a></li><li><a href="{r}trademark.html">Trademark & copyright</a></li></ul></div>
</div>
<div class="legal">© <span data-year>2026</span> 13522.com. All original content and code © 13522.com. "13522" is used solely as this website's domain name; no trademark rights in the number are claimed and no affiliation with any other organisation using the same number is implied. Third-party names and trademarks belong to their respective owners and appear for identification only. This site uses cookies and shows ads served by Google. See our <a href="{r}trademark.html">trademark & copyright disclosure</a> and <a href="{r}privacy.html">privacy policy</a>.</div>
</div></footer>
<div class="cookie" role="dialog" aria-label="Cookie notice"><strong>Cookies & ads.</strong> We use cookies to remember your planner and preferences, and Google uses cookies to serve and measure ads. <a href="{r}cookies.html">Learn more</a>.<div class="row"><button class="btn btn-primary btn-sm" data-consent="all">Accept</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div></div>
<div class="modal" id="kit-modal" role="dialog" aria-modal="true" aria-labelledby="kit-h"><div class="card"><button class="x" data-close aria-label="Close">×</button>
<span class="tag">Free</span><h3 id="kit-h">Get the 13522 Starter Kit</h3><p>A 7-day email course, printable planner pages and the team rollout checklist. One email a week after that. Unsubscribe any time.</p>
<form data-form="starter-kit" data-subject="Starter kit request" data-ok="Done — your starter kit is on its way.">
<div class="field"><label for="k-name">First name</label><input id="k-name" name="name" required autocomplete="given-name"></div>
<div class="field"><label for="k-email">Email</label><input id="k-email" type="email" name="email" required autocomplete="email"></div>
<input class="hp" name="_honey" tabindex="-1" autocomplete="off">
<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Send me the kit</button><div class="form-msg" role="status"></div>
<p class="form-note">By subscribing you agree to our <a href="{r}privacy.html">privacy policy</a>.</p></form></div></div>
<div class="sticky-cta noprint"><a class="btn btn-primary btn-sm" href="{r}planner.html">Plan my day</a><a class="btn btn-ghost btn-sm" style="color:#fff;border-color:#444" href="{r}teams.html">For teams</a></div>
<script src="{r}assets/js/main.js" defer></script>{scripts}
</body>
</html>
"""


def hp():
    return '<input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'


def consent(r=""):
    return f'<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this request and accept the <a href="{r}privacy.html">privacy policy</a>.</label>'
