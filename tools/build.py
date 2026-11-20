#!/usr/bin/env python3
"""Builds the District 2 Media pages in public/ from one shared header, menu and footer.

Edit the content below, then run:  python3 tools/build.py
Commit the regenerated files in public/. Cloudflare serves public/ as-is (no build step there).
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent / "public"
SITE = "https://district2media.com"
EMAIL = "info@district2media.com"
TAGLINE = "Strategic Content. Measurable Growth."
CTA_PRIMARY = "Let's grow your brand"
CTA_SECONDARY = "Explore our work"

# ---------------------------------------------------------------- content
# The five content pillars. Every monthly plan balances them around the client's goals.
PILLARS = [
    {
        "id": "appetite", "n": "01", "name": "Appetite", "img": "/assets/img/pillar-appetite.jpg",
        "alt": "Plated shaking beef with fries and pickled vegetables",
        "line": "Make people crave it.",
        "short": "Food photography and video that make customers crave what you serve.",
        "body": "The first job of restaurant content is simple: make someone hungry enough to stop scrolling. We plan and shoot the dishes, textures and moments that sell the plate before anyone reads the menu.",
        "looks": ["Hero dish photography", "Sizzle, pour and plating moments", "Menu and new-item launches"],
        "goal": "Discovery, cravings and orders of the items that matter most to your margins.",
    },
    {
        "id": "authority", "n": "02", "name": "Authority", "img": "/assets/img/pillar-authority.jpg",
        "alt": "Hot broth poured over a bowl of pho",
        "line": "Show why you're the real thing.",
        "short": "Content that establishes credibility, quality and a recognizable brand identity.",
        "body": "Guests choose places they trust. Authority content shows the standards behind the food: ingredients, technique, consistency and a visual identity people recognize at a glance.",
        "looks": ["Ingredients, sourcing and technique", "Signature dishes and house methods", "A consistent look across every channel"],
        "goal": "Trust, premium perception and standing out from the place down the street.",
    },
    {
        "id": "experience", "n": "03", "name": "Experience", "img": "/assets/img/pillar-experience.jpg",
        "alt": "Restaurant kitchen team cooking during service",
        "line": "Sell the visit, not just the plate.",
        "short": "The atmosphere, people, service and everything that makes a visit worth it.",
        "body": "People don't only buy food; they choose an evening, a lunch break, a celebration. Experience content shows the room, the energy and the service so guests can picture themselves there.",
        "looks": ["Atmosphere, interiors and the room at its best", "Service, hospitality and the team at work", "Events, private dining and occasions"],
        "goal": "Reservations, group bookings and being the obvious choice for an occasion.",
    },
    {
        "id": "connection", "n": "04", "name": "Connection", "img": "/assets/img/pillar-connection.jpg",
        "alt": "Cook working at the stove in a restaurant kitchen",
        "line": "Introduce the people behind it.",
        "short": "Storytelling about the people, history and personality behind the business.",
        "body": "The story behind a restaurant is something no competitor can copy. Connection content introduces the owners, the cooks, the family recipes and the regulars, and gives people a reason to care.",
        "looks": ["Founder, family and chef stories", "Behind-the-scenes and the team's personalities", "Community, regulars and local partners"],
        "goal": "Loyalty, word of mouth and followers who feel like regulars.",
    },
    {
        "id": "conversion", "n": "05", "name": "Conversion", "img": "/assets/img/pillar-conversion.jpg",
        "alt": "Styled overhead shot of a bowl of pho held on a white table",
        "line": "Turn attention into visits.",
        "short": "Promotional content designed to drive inquiries, visits, reservations and sales.",
        "body": "Awareness only matters if it leads somewhere. Conversion content gives people a clear reason and a clear next step, and we track how it performs so the next campaign is sharper than the last.",
        "looks": ["Limited-time items, launches and seasonal campaigns", "Event, catering and private-dining promotion", "Clear calls to reserve, order or visit"],
        "goal": "Inquiries, reservations, orders and visits you can track.",
    },
]

# Services, grouped as one system: plan it, make it, share it, measure it.
STAGES = [
    ("plan", "Plan", "Strategy before production", [
        {
            "id": "strategy", "title": "Content strategy & planning", "menu": "Goals, audience and the pillar mix",
            "body": "We start with your business, not a shot list: who you want to reach, what you want them to do and what your current content is and isn't doing.",
            "inc": ["Content audit of your current channels", "Audience, competitor and goal review",
                    "Your pillar mix and content priorities", "The measures we'll report on each month"],
        },
        {
            "id": "storytelling", "title": "Brand storytelling", "menu": "Your story, told consistently",
            "body": "We find the stories that make your business yours and turn them into messages and recurring formats your audience will recognize.",
            "inc": ["Story discovery session with owners and team", "Key messages and brand voice",
                    "Recurring story formats and series"],
        },
        {
            "id": "calendar", "title": "Content calendar & campaigns", "menu": "Monthly plans, launches and seasons",
            "body": "A month-by-month plan that ties content to what's happening in the business: menu changes, seasons, events and slow days.",
            "inc": ["Monthly content calendar you approve", "Seasonal and menu-launch campaigns",
                    "Event, catering and holiday pushes"],
        },
    ]),
    ("make", "Make", "Production with a purpose", [
        {
            "id": "production", "title": "Photography & videography", "menu": "Food, space, people and brand film",
            "body": "Planned shoot days that capture what the strategy calls for: dishes, the room, the team and cinematic brand video.",
            "inc": ["Scheduled shoot days around service hours", "Food, drink and menu photography",
                    "Atmosphere, team and portrait photography", "Cinematic brand and feature video"],
        },
        {
            "id": "short-form", "title": "Short-form video production", "menu": "Reels, TikTok and Shorts",
            "body": "Vertical video built for how people actually watch, with hooks, pacing and formats chosen for each platform.",
            "inc": ["Concepts and hooks for each video", "Editing with captions, music and on-brand text",
                    "Repeatable series your audience follows"],
        },
    ]),
    ("share", "Share", "Content that shows up consistently", [
        {
            "id": "social", "title": "Social media content development", "menu": "Platform-ready posts and captions",
            "body": "Every piece is adapted for where it will live, written in your voice and scheduled so your presence stays consistent.",
            "inc": ["Platform-specific formats and cutdowns", "Captions written in your brand voice",
                    "Scheduling and publishing"],
        },
    ]),
    ("measure", "Measure", "Learn what works, do more of it", [
        {
            "id": "analytics", "title": "Performance tracking & analytics", "menu": "Monthly reporting and insights",
            "body": "Each month we review what the content did and use it to shape the next plan. You see the numbers and what we're changing because of them.",
            "inc": ["Monthly performance report", "Reach, engagement, saves and profile visits",
                    "Website, reservation and order-link clicks where available", "Recommendations for next month's plan"],
        },
    ]),
]
SERVICES = [s for _, _, _, items in STAGES for s in items]

MONTH = [
    ("Plan", "We set the month's priorities with you: goals, campaigns and the pillar mix."),
    ("Create", "Shoot days and editing produce the month's photos, videos and stories."),
    ("Publish", "Content goes out on schedule, adapted for each platform."),
    ("Measure", "We report on what it did and use it to shape next month's plan."),
]

WORK = [
    {
        "id": "pho-sapa", "name": "Pho Sapa", "label": "Restaurant · Manassas, VA",
        "img": "/assets/img/work-phosapa.jpg", "alt": "Pho Sapa website homepage with a bowl of pho",
        "tag": '<span class="rec"></span>In production', "menu": "Vietnamese restaurant, digital presence",
        "summary": "A Vietnamese restaurant serving Manassas since 2012. The goal: a digital presence the restaurant owns and controls, and a smoother path from discovering them to ordering. We're moving their website onto a fast site they own and building scan-to-order table ordering that sends each round straight to the kitchen.",
        "items": ["Website rebuild, off a monthly platform", "QR table ordering with one open bill per table",
                  "Menu cleanup and online ordering links"],
        "link": None, "hospitality": True,
    },
    {
        "id": "dustin-transforms", "name": "Dustin Transforms", "label": "Personal brand · Online coaching",
        "img": "/assets/img/work-dustintransforms.jpg", "alt": "Dustin Transforms website hero: Lasting results, no restarts",
        "tag": "Live", "menu": "Coaching brand, lead generation",
        "summary": "A brand site for an online fitness coach, built around one business goal: turn visitors into booked consultation calls. A video hero tells the story, and a short application qualifies every lead before it books the call.",
        "items": ["Brand website with video hero", "4-step application that emails every lead",
                  "Calendly booking built into the final step"],
        "link": "https://dustintransforms.com", "hospitality": False,
    },
]

WHO = [
    ("Core", "Restaurants", "Independent restaurants and small groups that want to be the first place people think of.", True),
    ("Daytime", "Cafés & bakeries", "Daily favorites where the product, the space and the regulars are the brand.", False),
    ("Night", "Bars & lounges", "Places that sell an atmosphere and an occasion as much as a menu.", False),
    ("Stay", "Hotels & hospitality", "Hospitality brands where food, service and experience shape the stay.", False),
]

# ---------------------------------------------------------------- shared parts
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
LOGO = ('<a class="logo" href="/" aria-label="District 2 Media home"><img src="/assets/img/logo.png" '
        'srcset="/assets/img/logo.png 1x, /assets/img/logo@2x.png 2x" alt="District 2 Media" width="92" height="34"></a>')


def e(s):
    return escape(s, quote=True)


def head(title, desc, path, extra=""):
    full = f"{title} | District 2 Media" if title else "District 2 Media | Content Marketing for Restaurants & Hospitality"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(full)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="{SITE}{path}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(title or 'District 2 Media')}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{SITE}{path}">
  <meta property="og:image" content="{SITE}/assets/img/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#0b0b0c">
  <link rel="icon" href="/assets/img/favicon-64.png" type="image/png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="preload" href="/assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/style.css">{extra}
  <script>document.documentElement.classList.add('js')</script>
</head>
<body>
"""


def menu_item(key, label, href, active, links, wide=False):
    cur = ' aria-current="page"' if active == key else ""
    items = "".join(
        f'<a href="{e(h)}"><span class="sm-title">{e(t)}</span>'
        + (f'<span class="sm-desc">{e(d)}</span>' if d else "") + "</a>"
        for t, d, h in links)
    return f"""      <div class="nav-item has-menu">
        <a class="nav-link" href="{href}"{cur}>{label}</a>
        <button class="sub-toggle" type="button" aria-expanded="false" aria-controls="sm-{key}" aria-label="Show {label} pages">{CHEV}</button>
        <div class="submenu{' wide' if wide else ''}" id="sm-{key}">
          <div class="submenu-inner">{items}</div>
        </div>
      </div>
"""


def header(active):
    app = [(f"{p['name']}", p["line"], f"/approach/#{p['id']}") for p in PILLARS] + \
          [("How a partnership works", "Plan, create, publish, measure", "/approach/#partnership"),
           ("Our approach", "", "/approach/")]
    svc = [(s["title"][0].upper() + s["title"][1:], s["menu"], f"/services/#{s['id']}") for s in SERVICES] + \
          [("Monthly partnerships", "How we work together", "/services/#partnerships")]
    wrk = [(w["name"], w["menu"], f"/work/#{w['id']}") for w in WORK] + [("All work", "", "/work/")]
    abt = [("About District 2 Media", "Founder-led, strategy first", "/about/"),
           ("Who we work with", "Restaurants and hospitality", "/about/#who")]
    cur_contact = ' aria-current="page"' if active == "contact" else ""
    return f"""<header class="header">
  <div class="wrap">
    {LOGO}
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Main">
{menu_item('approach', 'Approach', '/approach/', active, app, wide=True)}{menu_item('services', 'Services', '/services/', active, svc, wide=True)}{menu_item('work', 'Work', '/work/', active, wrk)}{menu_item('about', 'About', '/about/', active, abt)}      <div class="nav-item"><a class="nav-link" href="/contact/"{cur_contact}>Contact</a></div>
      <a class="btn nav-cta" href="/contact/">{CTA_PRIMARY}</a>
    </nav>
  </div>
</header>
"""


def footer():
    cols = [
        ("Approach", [(p["name"], f"/approach/#{p['id']}") for p in PILLARS] + [("Partnerships", "/approach/#partnership")]),
        ("Services", [(s["title"][0].upper() + s["title"][1:], f"/services/#{s['id']}") for s in SERVICES]),
        ("Company", [("Work", "/work/"), ("About", "/about/"), ("Who we work with", "/about/#who"), ("Contact", "/contact/")]),
    ]
    colhtml = "".join(
        f'<div class="f-col"><h2 class="label">{t}</h2><ul>' + "".join(f'<li><a href="{h}">{e(n)}</a></li>' for n, h in links) + "</ul></div>"
        for t, links in cols)
    return f"""<footer class="footer">
  <div class="wrap f-grid">
    <div class="f-brand">
      {LOGO}
      <p class="f-tag">{TAGLINE}</p>
      <p>Strategic content marketing for restaurants and hospitality brands.</p>
      <a class="text-link" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    {colhtml}
  </div>
  <div class="wrap f-bottom"><span>© <span id="year">2026</span> District 2 Media</span><a href="/contact/">{CTA_PRIMARY} →</a></div>
  <div class="wrap"><div class="big-sign" aria-hidden="true"><img src="/assets/img/logo@2x.png" alt="" width="1200" height="445" loading="lazy"></div></div>
</footer>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def page_hero(eyebrow, title_html, lead):
    return f"""  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow label"><span class="rec"></span>{eyebrow}</div>
      <h1 class="display h1 page-title">{title_html}</h1>
      <p class="lead">{lead}</p>
    </div>
  </section>
"""


def subnav(items, label):
    links = "".join(f'<a href="#{i}">{e(t)}</a>' for i, t in items)
    return f"""  <nav class="subnav" aria-label="{label}">
    <div class="wrap"><div class="subnav-track">{links}</div></div>
  </nav>
"""


def cta_band(title="Let's grow your brand.", text="Tell us about your business and your goals. We'll reply within one business day to set up a strategy conversation."):
    return f"""  <section class="cta-band">
    <div class="wrap cta-inner">
      <div>
        <h2 class="display h2">{title}</h2>
        <p class="lead">{text}</p>
      </div>
      <a class="btn" href="/contact/">{CTA_PRIMARY} <span class="arrow">→</span></a>
    </div>
  </section>
"""


def month_loop():
    steps = "".join(f'        <div class="step"><div class="num">{i:02d}</div><h3 class="display h3">{e(t)}</h3><p>{e(d)}</p></div>\n'
                    for i, (t, d) in enumerate(MONTH, 1))
    return f"""      <div class="steps loop reveal">
{steps}      </div>
      <p class="loop-note label reveal">↻ Repeats every month, sharper each time</p>
"""


def compare():
    return """      <div class="compare reveal">
        <div class="cmp cmp-them">
          <span class="label">A typical production agency</span>
          <ul>
            <li>Delivers photos, videos and posts</li>
            <li>Shoots what looks good on the day</li>
            <li>Hands over files and moves on</li>
            <li>Measures success in deliverables</li>
          </ul>
        </div>
        <div class="cmp cmp-us">
          <span class="label">District 2 Media</span>
          <ul>
            <li>Starts with your business goals</li>
            <li>Plans content across five pillars</li>
            <li>Creates and publishes it every month</li>
            <li>Tracks what works and adjusts the plan</li>
          </ul>
        </div>
      </div>
"""


def case_html(w):
    link = f'<a class="text-link" href="{w["link"]}" target="_blank" rel="noopener">Visit the site ↗</a>' if w["link"] else ""
    items = "".join(f"<li>{e(i)}</li>" for i in w["items"])
    return f"""        <article class="case reveal" id="{w['id']}">
          <div class="case-media">
            <img src="{w['img']}" alt="{e(w['alt'])}" width="1200" height="675" loading="lazy">
            <span class="tag">{w['tag']}</span>
          </div>
          <div>
            <span class="label">{e(w['label'])}</span>
            <h2 class="display case-title">{e(w['name'])}</h2>
            <p>{e(w['summary'])}</p>
            <ul class="deliverables">{items}</ul>
            {link}
          </div>
        </article>
"""


# ---------------------------------------------------------------- pages
def home():
    pillars = "".join(f"""        <a class="pillar-card" href="/approach/#{p['id']}">
          <div class="pc-media"><img src="{p['img']}" alt="{e(p['alt'])}" width="720" height="900" loading="lazy"></div>
          <div class="pc-body">
            <span class="label">{p['n']}</span>
            <h3 class="display h3">{p['name']}</h3>
            <p>{e(p['short'])}</p>
          </div>
        </a>
""" for p in PILLARS)
    stage_cards = "".join(f"""        <a class="stage-card" href="/services/#{key}">
          <span class="label">{e(sub)}</span>
          <h3 class="display h3">{name}</h3>
          <ul>{''.join(f'<li>{e(s["title"][0].upper() + s["title"][1:])}</li>' for s in items)}</ul>
          <span class="tile-go" aria-hidden="true">→</span>
        </a>
""" for key, name, sub, items in STAGES)
    feat = WORK[0]
    body = f"""<main>
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <div class="eyebrow label"><span class="rec"></span>Content marketing for restaurants &amp; hospitality</div>
        <h1 class="display h1"><span class="phrase">More than</span> <span class="phrase">content.</span> <span class="phrase">A strategy</span> <span class="phrase">for <span class="hl">growth.</span></span></h1>
        <p class="lead hero-lead">We help restaurants and hospitality brands turn their stories into strategic content that builds visibility, attracts customers, and grows their business.</p>
        <div class="actions">
          <a class="btn" href="/contact/">{CTA_PRIMARY} <span class="arrow">→</span></a>
          <a class="btn btn-ghost" href="/work/">{CTA_SECONDARY}</a>
        </div>
      </div>
      <div class="viewfinder">
        <video id="promo" src="/assets/img/promo.mp4" poster="/assets/img/promo-poster.jpg" width="720" height="1280" autoplay muted loop playsinline preload="auto" aria-label="District 2 Media at work on restaurant shoots"></video>
        <div class="vf-corner tl" aria-hidden="true"></div><div class="vf-corner tr" aria-hidden="true"></div><div class="vf-corner bl" aria-hidden="true"></div><div class="vf-corner br" aria-hidden="true"></div>
        <div class="vf-top" aria-hidden="true"><span class="vf-rec"><span class="rec"></span>REC</span><span>4K · 24 FPS</span></div>
        <div class="vf-bottom"><span id="timecode" aria-hidden="true">00:00:00:00</span><button type="button" class="vf-sound" id="vf-sound" aria-pressed="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path id="vf-sound-waves" d="M23 9l-6 6M17 9l6 6"/></svg><span id="vf-sound-label">Sound</span></button></div>
      </div>
    </div>
  </section>

  <div class="ticker" aria-hidden="true">
    <div class="ticker-track">
      <span>Appetite</span><span>Authority</span><span>Experience</span><span>Connection</span><span>Conversion</span><span>{TAGLINE}</span>
      <span>Appetite</span><span>Authority</span><span>Experience</span><span>Connection</span><span>Conversion</span><span>{TAGLINE}</span>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <h2 class="display h2">Not a production<br>company.</h2>
        <p class="lead">Most agencies deliver files. We deliver a plan, the content to carry it out, and the numbers that show what's working.</p>
      </div>
{compare()}    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="row-head reveal">
        <div>
          <span class="label">Our approach</span>
          <h2 class="display h2 row-title">Five pillars of<br>restaurant content</h2>
        </div>
        <a class="text-link" href="/approach/">See how it works →</a>
      </div>
      <div class="pillar-grid reveal">
{pillars}      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="row-head reveal">
        <div>
          <span class="label">Services</span>
          <h2 class="display h2 row-title">One system,<br>not separate services</h2>
        </div>
        <a class="text-link" href="/services/">Explore services →</a>
      </div>
      <div class="stage-grid reveal">
{stage_cards}      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <h2 class="display h2">Built for<br>partnership</h2>
        <p class="lead">Consistency is what builds a brand online. We work with clients month to month, with a plan, production and a report every cycle.</p>
      </div>
{month_loop()}    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="row-head reveal">
        <div><span class="label">Selected work</span><h2 class="display h2 row-title">{e(feat['name'])}</h2></div>
        <a class="text-link" href="/work/">{CTA_SECONDARY} →</a>
      </div>
      <a class="feature-case reveal" href="/work/#{feat['id']}">
        <div class="case-media"><img src="{feat['img']}" alt="{e(feat['alt'])}" width="1200" height="675" loading="lazy"><span class="tag">{feat['tag']}</span></div>
        <div class="fc-body"><span class="label">{e(feat['label'])}</span><p>{e(feat['summary'])}</p><span class="text-link">Read the case study →</span></div>
      </a>
    </div>
  </section>

{cta_band()}</main>
"""
    return head("", "District 2 Media is a strategic content marketing agency for restaurants and hospitality brands. Strategy, content and measurement in one monthly partnership.", "/") + header("home") + body + footer()


def approach():
    sections = ""
    for i, p in enumerate(PILLARS):
        looks = "".join(f"<li>{e(x)}</li>" for x in p["looks"])
        sections += f"""  <section class="pillar-row{' flip' if i % 2 else ''}" id="{p['id']}">
    <div class="wrap pr-grid">
      <div class="pr-media reveal"><img src="{p['img']}" alt="{e(p['alt'])}" width="720" height="900" loading="lazy"><span class="pr-num">{p['n']}</span></div>
      <div class="pr-body reveal">
        <span class="label">Pillar {p['n']}</span>
        <h2 class="display h2">{p['name']}</h2>
        <p class="pr-line">{e(p['line'])}</p>
        <p class="lead">{e(p['body'])}</p>
        <h3 class="label svc-sub">What it looks like</h3>
        <ul class="deliverables">{looks}</ul>
        <p class="good"><span class="label">Supports</span> {e(p['goal'])}</p>
      </div>
    </div>
  </section>
"""
    body = f"""<main>
{page_hero('Our approach', '<span class="phrase">Five pillars.</span> <span class="phrase">One <span class="hl">strategy.</span></span>', 'Great restaurant content does five different jobs. We plan every month around the right balance of them, based on your goals and what the numbers tell us.')}{subnav([(p['id'], p['name']) for p in PILLARS] + [('partnership', 'Partnership')], 'Pillars on this page')}{sections}  <section class="section" id="partnership">
    <div class="wrap">
      <div class="section-head reveal">
        <h2 class="display h2">How a<br>partnership works</h2>
        <p class="lead">Every month follows the same cycle, so your presence stays consistent and every month builds on what the last one taught us.</p>
      </div>
{month_loop()}    </div>
  </section>
{cta_band()}</main>
"""
    return head("Our approach", "The five content pillars District 2 Media plans around: Appetite, Authority, Experience, Connection and Conversion.", "/approach/") + header("approach") + body + footer()


def services():
    groups = ""
    for key, name, sub, items in STAGES:
        cards = ""
        for s in items:
            inc = "".join(f"<li>{e(i)}</li>" for i in s["inc"])
            cards += f"""        <article class="svc-card" id="{s['id']}">
          <h3 class="display h3">{e(s['title'])}</h3>
          <p>{e(s['body'])}</p>
          <ul class="deliverables">{inc}</ul>
        </article>
"""
        groups += f"""  <section class="stage" id="{key}">
    <div class="wrap stage-wrap">
      <div class="stage-head reveal">
        <span class="label">{e(sub)}</span>
        <h2 class="display h2">{name}</h2>
      </div>
      <div class="svc-cards reveal">
{cards}      </div>
    </div>
  </section>
"""
    body = f"""<main>
{page_hero('Services', '<span class="phrase">One system,</span> <span class="phrase">built for <span class="hl">growth.</span></span>', "We don't sell photos, videos and posts as separate jobs. Strategy, production, publishing and measurement work together, so every piece of content has a purpose.")}{subnav([(k, n) for k, n, _, _ in STAGES] + [('partnerships', 'Partnerships')], 'Service stages')}{groups}  <section class="section" id="partnerships">
    <div class="wrap partner">
      <div class="reveal">
        <span class="label">How we work together</span>
        <h2 class="display h2 row-title">Monthly<br>partnerships</h2>
        <p class="lead">Content works when it's consistent. Our clients work with us month to month: a plan, the production to carry it out, and a review of what it achieved.</p>
      </div>
      <div class="partner-box reveal">
        <h3 class="label">Every month includes</h3>
        <ul class="deliverables">
          <li>A planning session and an approved content calendar</li>
          <li>Shoot days scheduled around your service hours</li>
          <li>Edited photos, videos and posts, published on schedule</li>
          <li>A performance report and recommendations</li>
        </ul>
        <h3 class="label">Getting started</h3>
        <p>Every partnership starts with a strategy session and a review of your current content, so the first month is built on your goals, not guesses. Launches and events can also be planned as stand-alone campaigns.</p>
        <a class="btn" href="/contact/">{CTA_PRIMARY} <span class="arrow">→</span></a>
      </div>
    </div>
  </section>
</main>
"""
    return head("Services", "Content strategy, photography and videography, short-form video, social content, brand storytelling, campaign planning and performance tracking for restaurants and hospitality brands.", "/services/") + header("services") + body + footer()


def work():
    hosp = "".join(case_html(w) for w in WORK if w["hospitality"])
    other = "".join(case_html(w) for w in WORK if not w["hospitality"])
    body = f"""<main>
{page_hero('Work', 'Selected <span class="hl">work</span>', 'Every project starts with a business goal. Here is what we set out to do and what we built to get there. More hospitality case studies are on the way.')}  <section class="section flush">
    <div class="wrap work">
{hosp}    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="section-head reveal"><h2 class="display h2">Beyond<br>hospitality</h2><p class="lead">The same goal-first approach, applied to a personal brand.</p></div>
      <div class="work">
{other}      </div>
    </div>
  </section>
{cta_band()}</main>
"""
    return head("Work", "District 2 Media case studies: Pho Sapa restaurant in Manassas, VA, and the Dustin Transforms coaching brand.", "/work/") + header("work") + body + footer()


def about():
    who = "".join(f"""        <div class="who-card{' lead-card' if lead else ''}">
          <span class="label">{lab}</span>
          <h3 class="display h3">{e(t)}</h3>
          <p>{e(d)}</p>
        </div>
""" for lab, t, d, lead in WHO)
    body = f"""<main>
{page_hero('About', '<span class="phrase">The business</span> <span class="phrase">behind the <span class="hl">brand.</span></span>', 'District 2 Media is a content marketing agency for restaurants and hospitality brands. We understand the business behind the brand, develop the strategy, create the content and measure how well it works.')}{subnav([('story', 'Who we are'), ('who', 'Who we work with')], 'About sections')}  <section class="section" id="story">
    <div class="wrap about">
      <div class="reveal fit-box">
        <h2 class="display h2 fit"><span class="phrase">Founder-led.</span> <span class="phrase hl">Strategy first.</span></h2>
      </div>
      <div class="reveal">
        <p class="lead">District 2 Media is led by founder Dustin Tran, a creator and entrepreneur who works on both sides of marketing: the content that makes people stop scrolling, and the business results it's meant to drive.</p>
        <p>Every partnership gets senior attention. Dustin sets the strategy and creative direction, plans every shoot and reviews every piece of content and every report before it reaches you.</p>
        <dl class="facts">
          <div><dt>Specialty</dt><dd>Restaurants and hospitality brands</dd></div>
          <div><dt>Approach</dt><dd>Strategy, production and measurement in one plan</dd></div>
          <div><dt>Model</dt><dd>Monthly partnerships, plus campaigns for launches and events</dd></div>
          <div><dt>Your contact</dt><dd>Dustin, directly, from the first call to the monthly report</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <section class="section" id="who">
    <div class="wrap">
      <div class="section-head reveal">
        <h2 class="display h2">Who we<br>work with</h2>
        <p class="lead">Hospitality businesses where the food, the people and the experience are what bring guests back.</p>
      </div>
      <div class="who reveal">
{who}      </div>
    </div>
  </section>
{cta_band()}</main>
"""
    return head("About", "District 2 Media is a founder-led content marketing agency for restaurants and hospitality brands, led by Dustin Tran.", "/about/") + header("about") + body + footer()


def chips(name, options):
    return "".join(f'<label class="chip"><input type="checkbox" name="{name}" value="{e(v)}"><span>{e(t)}</span></label>' for v, t in options)


def contact():
    looking = [("Monthly content partnership", "Monthly partnership"), ("Content strategy", "Content strategy"),
               ("Photo and video production", "Photo & video"), ("Short-form video", "Short-form video"),
               ("Social media content", "Social content"), ("Campaign for a launch or event", "Launch or event campaign"),
               ("Not sure yet", "Not sure yet")]
    goals = [("More visibility online", "More visibility"), ("More visits and reservations", "More visits & reservations"),
             ("Stronger brand", "Stronger brand"), ("Consistent posting", "Consistent posting"),
             ("Launch something new", "Launch something new")]
    types = ["Restaurant", "Café or bakery", "Bar or lounge", "Hotel or hospitality group", "Food or beverage brand", "Other"]
    type_opts = "".join(f'<option value="{e(t)}">{e(t)}</option>' for t in types)
    body = f"""<main>
  <section class="page-hero contact-page">
    <div class="wrap contact">
      <div>
        <div class="eyebrow label"><span class="rec"></span>Now booking strategy sessions</div>
        <h1 class="display h2">Let's grow<br>your brand.</h1>
        <p class="lead">Tell us about your business and what you want to achieve. We'll reply within one business day to set up a strategy conversation.</p>
        <div class="contact-alt">
          <span>Prefer email? <a class="text-link" id="email-link" href="mailto:{EMAIL}">{EMAIL}</a></span>
        </div>
      </div>
      <form class="form" id="contact-form" novalidate>
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
        <div class="row2">
          <div class="field"><label for="c-name">Your name</label><input class="input" id="c-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="c-biz">Business name</label><input class="input" id="c-biz" name="business" autocomplete="organization" required></div>
        </div>
        <div class="row2">
          <div class="field"><label for="c-email">Email</label><input class="input" id="c-email" name="email" type="email" autocomplete="email" inputmode="email" required></div>
          <div class="field"><label for="c-phone">Phone <span class="opt">(optional)</span></label><input class="input" id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
        </div>
        <div class="row2">
          <div class="field"><label for="c-type">Type of business</label><select class="input" id="c-type" name="btype">{type_opts}</select></div>
          <div class="field"><label for="c-site">Website or Instagram <span class="opt">(optional)</span></label><input class="input" id="c-site" name="link" placeholder="@yourbusiness"></div>
        </div>
        <fieldset class="field">
          <legend>What are you looking for?</legend>
          <div class="chips">{chips('needs', looking)}</div>
        </fieldset>
        <fieldset class="field">
          <legend>Main goals <span class="opt">(optional)</span></legend>
          <div class="chips">{chips('goals', goals)}</div>
        </fieldset>
        <div class="field"><label for="c-budget">Monthly marketing budget</label>
          <select class="input" id="c-budget" name="budget">
            <option value="Not sure yet">Not sure yet</option>
            <option value="Under $1,000">Under $1,000</option>
            <option value="$1,000 - $2,500">$1,000 – $2,500</option>
            <option value="$2,500 - $5,000">$2,500 – $5,000</option>
            <option value="$5,000+">$5,000+</option>
            <option value="One-off campaign">One-off campaign</option>
          </select>
        </div>
        <div class="field"><label for="c-msg">Tell us about your business</label><textarea class="input" id="c-msg" name="message" required placeholder="What makes your place special, who your guests are, and what you'd like to change."></textarea></div>
        <div class="send-row">
          <button class="btn" type="submit" id="c-send">Send <span class="arrow">→</span></button>
          <span class="form-status" id="c-status" role="status"></span>
        </div>
      </form>
    </div>
  </section>
</main>
"""
    return head("Contact", "Start a conversation with District 2 Media about content marketing for your restaurant or hospitality brand.", "/contact/") + header("contact") + body + footer()


def not_found():
    body = f"""<main>
  <section class="page-hero nf">
    <div class="wrap">
      <div class="eyebrow label"><span class="rec"></span>404 · Scene missing</div>
      <h1 class="display h1 page-title">Cut. <span class="hl">Wrong take.</span></h1>
      <p class="lead">This page doesn't exist. Try one of these instead.</p>
      <div class="actions"><a class="btn" href="/">Home <span class="arrow">→</span></a><a class="btn btn-ghost" href="/approach/">Our approach</a><a class="btn btn-ghost" href="/contact/">Contact</a></div>
    </div>
  </section>
</main>
"""
    return head("Page not found", "This page doesn't exist.", "/404", '\n  <meta name="robots" content="noindex">') + header("") + body + footer()


PAGES = {
    "index.html": home, "approach/index.html": approach, "services/index.html": services,
    "work/index.html": work, "about/index.html": about, "contact/index.html": contact, "404.html": not_found,
}

if __name__ == "__main__":
    for rel, fn in PAGES.items():
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fn())
        print("wrote", out.relative_to(ROOT.parent))
    urls = "".join(f"  <url><loc>{SITE}{p}</loc></url>\n" for p in ["/", "/approach/", "/services/", "/work/", "/about/", "/contact/"])
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print("wrote public/sitemap.xml")
