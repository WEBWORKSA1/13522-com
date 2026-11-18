# 13522.com — Phase-wise build prompts

Reusable prompts to rebuild or extend this site. Each phase is self-contained; run in order.

---

## Phase 1 — Concept & brand
> Build a website for the domain **13522.com**, branded as "13522 — The 1·3·5·2·2 Day": 1 big task, 3 medium tasks, 5 small tasks, 2 focus sprints, 2 reviews. Audience: knowledge workers, founders, students and team managers. Tone: practical, confident, no hype. Palette: warm off-white #f6f3ec, ink #15151f, tier colours big #ff5a36, medium #f2a516, small #12a594, sprint #6d5efc, review #e0479e. Fonts: Space Grotesk (display) + Inter (body). Logo: five vertical bars in the tier colours. Include dark mode.

## Phase 2 — Static architecture (GitHub Pages free plan)
> Create a dependency-free static site deployable from the `main` branch of a GitHub repo. Use a small Python generator (`_src/build.py`) with a shared layout (`_src/layout.py`) so header, footer, SEO meta, Open Graph, JSON-LD (WebSite, Organization, FAQPage, WebApplication, Article/BlogPosting) and the AdSense tag are identical on every page. All links relative so the site works on `username.github.io/repo/` and on the custom domain. Add `.nojekyll`, `robots.txt`, `sitemap.xml` (generated), `ads.txt` (`google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0`), `manifest.webmanifest`, favicon, icons and a 1200×630 OG image, and a `404.html` that works at any path depth.

## Phase 3 — Global UI on every page
> On top of every page show a full-width bar: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership" linking to `https://web.works/contact` (new tab; the URL is never shown as text). Sticky header with nav (Home, Planner, Tools, Guide, Blog, Videos, AI Tools, More▾, For Teams CTA, theme toggle), responsive hamburger menu. Footer with newsletter form, 4 link columns and a trademark/copyright notice. Cookie notice, one-time starter-kit pop-up (after 40 s or 60 % scroll, never on lead pages), sticky mobile CTA, scroll-reveal animations, reduced-motion support, print styles.

## Phase 4 — Core product: the planner
> Build a client-side planner (`assets/js/planner.js`, localStorage only): 1 big / 3 medium / 5 small slots with checkbox, text and minutes; morning and evening review boxes; day score (big 40, medium 10 each, small 4 each, sprint 5 each); streak of days ≥ 60 %; 14-day history bars; auto carry-over of unfinished tasks to the next day; Smart Sort that turns a pasted brain dump into 1·3·5 using time cues and keyword heuristics and parks the overflow; focus-sprint timer with 25/50/90-minute presets, sound and auto-tick of sprint 1/2; copy, download .txt, print and clear. Embed it on the home page and on planner.html.

## Phase 5 — Tools & data-driven sections
> Create tools.html with tabbed calculators (meeting cost, hourly value, task estimator with planning-fallacy buffer, daily capacity, cost of procrastination, team focus cost) each with explanatory copy. Create ai-tools.html rendering `data/tools.json` (30 tools, category filters, search, `?q=` support, "13522 fit" tip, rel="nofollow sponsored" links, disclosure). Create videos.html rendering `data/videos.json` — click-to-play youtube-nocookie lite embeds when an `id` is set, otherwise a YouTube search card — plus a video-submission form.

## Phase 6 — Content for AdSense approval
> Write original, substantial content: a 2,000-word guide (guide.html) with TOC, tables and sample day; at least 8 blog articles (600–900 words each) on the 1-3-5 rule, AI planning, teams, focus sprints, evening reviews, 1-3-5 vs Eisenhower, students, meeting costs; printable templates page; About page with editorial standards and how the site makes money. No copied text, no thin pages, no misleading ad placement, auto ads only via the head tag.

## Phase 7 — Lead generation (highest-converting section)
> Build teams.html: hero with value proposition, 5-question multi-step assessment with progress bar (team size, clarity, meetings, interruptions, carry-overs) that computes "focus leakage", hours lost per person per week and annual cost, then reveals a lead form (name, work email, company, role, interest: free plan / call / workshop / custom) — quiz answers and results are attached to the submission. Add packages (Free plan, Live workshop "Most popular", Custom rollout), FAQ, and repeat lead CTAs on the home page and in every article.

## Phase 8 — Monetisation beyond ads
> support.html: donation tiers ($5, $22, $135, custom), allocation bars (operations, tools, prizes, hiring, marketing), pledge form with frequency and purpose (operations, promotions, marketing, hiring talent, contests, prizes). contests.html: monthly challenge with three categories, entry form, age confirmation and official rules (no purchase necessary, void where prohibited, not sponsored by Google). careers.html: six remote roles + application form. advertise.html: six sponsorship/partnership packages + inquiry form with budget and a domain-acquisition option.

## Phase 9 — Private form relay
> All forms post via fetch to FormSubmit's AJAX endpoint. The destination address must never appear in HTML, visible text or plain strings: store it as reversed base64 segments in `main.js`, decode at submit time. Include honeypot, consent checkbox, subject per form, success/error messages and a `lead135` flag that suppresses pop-ups after conversion. (First live submission triggers a one-time FormSubmit activation email that must be confirmed.)

## Phase 10 — Legal & compliance
> Privacy policy (forms, local storage, Google AdSense cookie wording, opt-out links, EEA consent, user rights), terms, cookie policy table, disclaimer (calculators, affiliate/sponsored, wellbeing), and a trademark & copyright disclosure stating no rights are claimed in the number 13522, no affiliation with others using it, the 1-3-5 rule is a generic method, third-party marks are nominative use.

## Phase 11 — Automation & deploy
> Add `.github/workflows/deploy.yml`: on push to main, daily cron and manual dispatch → (on schedule) run `_src/refresh.py` to rotate `data/daily.json` (tip + challenge of the day) and stamp sitemap lastmod, commit, then configure-pages (enablement: true), upload-pages-artifact and deploy-pages.

## Phase 12 — QA & launch
> Render every page at 1366 px and 390 px in a headless browser; check no JS errors; run the planner, Smart Sort, assessment funnel and a form submission with the network call intercepted; grep the repo to confirm the email address never appears; validate sitemap and internal links. Then point 13522.com DNS at GitHub Pages, add a `CNAME` file, enable HTTPS, submit the sitemap to Search Console and apply to AdSense.
