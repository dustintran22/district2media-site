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

# ---------------------------------------------------------------- content
SERVICES = [
    {
        "id": "video", "label": "Video", "title": "Short-form video",
        "menu": "Reels, TikToks and Shorts",
        "tile": "Vertical video for Reels, TikTok and Shorts, made to stop the scroll.",
        "intro": "Vertical videos for Reels, TikTok and YouTube Shorts. Planned around what your customers care about, shot at your business and edited to hold attention from the first second.",
        "included": ["A concept and shot list for every shoot", "Filming on location at your business",
                     "Editing with captions, music and on-brand text", "Cuts sized for each platform",
                     "Extra clips you can reuse later"],
        "good": "Menu launches, behind-the-scenes, promos, staff and owner stories.",
    },
    {
        "id": "photo", "label": "Photo", "title": "Photography",
        "menu": "Food, product, space and team",
        "tile": "Food, product, space and team photos for every place customers look.",
        "intro": "Photos for your menu, website, delivery apps and Google listing, styled and lit so the real thing looks as good as it tastes, feels or works.",
        "included": ["Menu and dish photos, styled and lit", "Interior, exterior and atmosphere shots",
                     "Team and owner portraits", "Edited, web-ready files sized for each platform",
                     "Uploads to delivery apps and your Google listing"],
        "good": "New menus, openings, refreshes and delivery apps.",
    },
    {
        "id": "social", "label": "Social", "title": "Social media management",
        "menu": "Calendar, posting and replies",
        "tile": "A monthly plan, posting and replies, so your feed stays active without you.",
        "intro": "We plan, post and keep the conversation going every month, so your accounts stay active while you run the business.",
        "included": ["A monthly content calendar you approve", "Captions, hashtags and scheduled posting",
                     "Stories and highlights", "Replies to comments and messages",
                     "A short monthly report on what worked"],
        "good": "Owners who know they should post more but don't have the time.",
    },
    {
        "id": "web", "label": "Web", "title": "Websites & ordering",
        "menu": "Sites, booking and QR ordering",
        "tile": "Fast websites you own, with menus, booking, ordering and forms.",
        "intro": "Mobile-first websites that load fast and send people to the next step: call, book, order or visit. You own the site and the domain, with no monthly platform holding it hostage.",
        "included": ["Design, copy and build, made for phones first", "Menus, booking, contact and lead forms",
                     "Online ordering and QR table ordering", "Hosting on Cloudflare: fast and secure",
                     "You own the site and the domain"],
        "good": "Replacing an outdated site or an expensive monthly platform.",
    },
    {
        "id": "local", "label": "Local", "title": "Google & local search",
        "menu": "Google Business Profile and Maps",
        "tile": "A Google profile that's complete and current, so you show up nearby.",
        "intro": "Most customers find you on Google and Maps before they ever see your website. We make sure what they find is complete, current and full of good photos.",
        "included": ["Google Business Profile setup or cleanup", "Photos, hours, menu and services kept current",
                     "Regular posts and updates", "A simple way to ask happy customers for reviews",
                     "Local search basics on your website"],
        "good": "Showing up when people search “near me”.",
    },
    {
        "id": "ads", "label": "Ads", "title": "Paid ads",
        "menu": "Meta and Google ads",
        "tile": "Meta and Google ads built from content that already works.",
        "intro": "Ads on Instagram, Facebook and Google, built from the content your audience already responds to and aimed at people close enough to visit.",
        "included": ["Campaign setup on Meta and Google", "Ads made from your best-performing content",
                     "Targeting by distance from your business", "Offers and promos for slow days",
                     "A monthly report on spend and results"],
        "good": "Launches, events, new locations and filling slow days.",
    },
]

WORK = [
    {
        "id": "pho-sapa", "name": "Pho Sapa", "label": "Restaurant · Manassas, VA",
        "img": "/assets/img/work-phosapa.jpg", "alt": "Pho Sapa website homepage with a bowl of pho",
        "tag": '<span class="rec"></span>In production', "menu": "Restaurant website + QR ordering",
        "summary": "A Vietnamese restaurant serving Manassas since 2012. We're moving their website onto a fast site they own and building scan-to-order table ordering that sends each round straight to the kitchen.",
        "items": ["Website rebuild, off a monthly platform", "QR table ordering with one open bill per table",
                  "Menu cleanup and online ordering links"],
        "link": None,
    },
    {
        "id": "dustin-transforms", "name": "Dustin Transforms", "label": "Fitness coaching · Online",
        "img": "/assets/img/work-dustintransforms.jpg", "alt": "Dustin Transforms website hero: Lasting results, no restarts",
        "tag": "Live", "menu": "Coaching brand site + booking",
        "summary": "A bold black, white and red brand site for an online fitness coach, built around a video hero and a coaching application that books the call automatically.",
        "items": ["Brand website with video hero", "4-step application that emails every lead",
                  "Calendly booking built into the final step"],
        "link": "https://dustintransforms.com",
    },
]

WHO = [
    ("Specialty", "Restaurants & cafés", "Menu photos, crave-worthy reels, websites and table or online ordering.", True),
    ("Book", "Salons & studios", "Before-and-afters, booking-ready pages and a feed that fills the calendar.", False),
    ("Train", "Fitness & wellness", "Coach brands, transformation stories and sites that turn followers into clients.", False),
    ("Shop", "Shops & services", "Product content, Google presence and simple sites that bring in calls and visits.", False),
]

STEPS = [
    ("Call", "A 20-minute chat about your business, your customers and what's not working."),
    ("Plan", "A content and channel plan with clear deliverables and a fixed monthly or project price."),
    ("Shoot & build", "One shoot day turns into weeks of content. Websites go live on a preview link first."),
    ("Post & grow", "We publish, watch what works and do more of it, with a short report each month."),
]

# ---------------------------------------------------------------- shared parts
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
LOGO = ('<a class="logo" href="/" aria-label="District 2 Media home"><img src="/assets/img/logo.png" '
        'srcset="/assets/img/logo.png 1x, /assets/img/logo@2x.png 2x" alt="District 2 Media" width="92" height="34"></a>')


def e(s):
    return escape(s, quote=True)


def head(title, desc, path, extra=""):
    full = f"{title} | District 2 Media" if title else "District 2 Media | Content, Social & Websites for Local Businesses"
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
    svc = [(s["title"], s["menu"], f"/services/#{s['id']}") for s in SERVICES] + [("All services", "", "/services/")]
    wrk = [(w["name"], w["menu"], f"/work/#{w['id']}") for w in WORK] + [("All work", "", "/work/")]
    abt = [("About District 2 Media", "Founder-led, hands-on", "/about/"),
           ("Who we work with", "Restaurants and local brands", "/about/#who"),
           ("How it works", "From first call to monthly report", "/about/#process")]
    cur_contact = ' aria-current="page"' if active == "contact" else ""
    return f"""<header class="header">
  <div class="wrap">
    {LOGO}
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Main">
{menu_item('services', 'Services', '/services/', active, svc, wide=True)}{menu_item('work', 'Work', '/work/', active, wrk)}{menu_item('about', 'About', '/about/', active, abt)}      <div class="nav-item"><a class="nav-link" href="/contact/"{cur_contact}>Contact</a></div>
      <a class="btn nav-cta" href="/contact/">Start a project</a>
    </nav>
  </div>
</header>
"""


def footer(scripts=""):
    cols = [
        ("Services", [(s["title"], f"/services/#{s['id']}") for s in SERVICES]),
        ("Work", [(w["name"], f"/work/#{w['id']}") for w in WORK] + [("All work", "/work/")]),
        ("Company", [("About", "/about/"), ("Who we work with", "/about/#who"), ("How it works", "/about/#process"), ("Contact", "/contact/")]),
    ]
    colhtml = "".join(
        f'<div class="f-col"><h2 class="label">{t}</h2><ul>' + "".join(f'<li><a href="{h}">{e(n)}</a></li>' for n, h in links) + "</ul></div>"
        for t, links in cols)
    return f"""<footer class="footer">
  <div class="wrap f-grid">
    <div class="f-brand">
      {LOGO}
      <p>Every brand has a story. Let's tell yours through our lens.</p>
      <a class="text-link" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    {colhtml}
  </div>
  <div class="wrap f-bottom"><span>© <span id="year">2026</span> District 2 Media</span><a href="/contact/">Start a project →</a></div>
  <div class="wrap"><div class="big-sign" aria-hidden="true"><img src="/assets/img/logo@2x.png" alt="" width="1200" height="445" loading="lazy"></div></div>
</footer>
<script src="/assets/js/site.js" defer></script>
{scripts}</body>
</html>
"""


def page_hero(eyebrow, title_html, lead, fit=False):
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


def cta_band(title="Have a story worth telling?", text="Tell us about your business and what you need. We'll reply within one business day."):
    return f"""  <section class="cta-band">
    <div class="wrap cta-inner">
      <div>
        <h2 class="display h2">{title}</h2>
        <p class="lead">{text}</p>
      </div>
      <a class="btn" href="/contact/">Start a project <span class="arrow">→</span></a>
    </div>
  </section>
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
    tiles = "".join(f"""        <a class="tile" href="/services/#{s['id']}">
          <span class="label">{s['label']}</span>
          <h3 class="display h3">{e(s['title'])}</h3>
          <p>{e(s['tile'])}</p>
          <span class="tile-go" aria-hidden="true">→</span>
        </a>
""" for s in SERVICES)
    work = "".join(f"""        <a class="work-card" href="/work/#{w['id']}">
          <div class="case-media"><img src="{w['img']}" alt="{e(w['alt'])}" width="1200" height="675" loading="lazy"><span class="tag">{w['tag']}</span></div>
          <div class="work-meta"><span class="label">{e(w['label'])}</span><h3 class="display h3">{e(w['name'])}</h3><span class="tile-go" aria-hidden="true">→</span></div>
        </a>
""" for w in WORK)
    body = f"""<main>
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <div class="eyebrow label"><span class="rec"></span>Content · Social · Websites</div>
        <h1 class="display h1"><span class="phrase">Every brand</span> <span class="phrase">has a <span class="hl">story.</span></span></h1>
        <p class="tagline display">Let's tell yours through our lens.</p>
        <p class="lead">Short-form video, photos, social content and websites for restaurants and local brands.</p>
        <div class="actions">
          <a class="btn" href="/contact/">Start a project <span class="arrow">→</span></a>
          <a class="btn btn-ghost" href="/work/">See the work</a>
        </div>
      </div>
      <div class="viewfinder">
        <video id="promo" src="/assets/img/promo.mp4" poster="/assets/img/promo-poster.jpg" width="720" height="1280" autoplay muted loop playsinline preload="auto" aria-label="District 2 Media promo: behind the scenes at restaurant shoots"></video>
        <div class="vf-corner tl" aria-hidden="true"></div><div class="vf-corner tr" aria-hidden="true"></div><div class="vf-corner bl" aria-hidden="true"></div><div class="vf-corner br" aria-hidden="true"></div>
        <div class="vf-top" aria-hidden="true"><span class="vf-rec"><span class="rec"></span>REC</span><span>4K · 24 FPS</span></div>
        <div class="vf-bottom"><span id="timecode" aria-hidden="true">00:00:00:00</span><button type="button" class="vf-sound" id="vf-sound" aria-pressed="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path id="vf-sound-waves" d="M23 9l-6 6M17 9l6 6"/></svg><span id="vf-sound-label">Sound</span></button></div>
      </div>
    </div>
  </section>

  <div class="ticker" aria-hidden="true">
    <div class="ticker-track">
      <span>Short-form video</span><span>Food photography</span><span>Social media</span><span>Websites</span><span>Online ordering</span><span>Google Business Profile</span><span>Paid ads</span>
      <span>Short-form video</span><span>Food photography</span><span>Social media</span><span>Websites</span><span>Online ordering</span><span>Google Business Profile</span><span>Paid ads</span>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="row-head reveal">
        <h2 class="display h2">What we do</h2>
        <a class="text-link" href="/services/">All services →</a>
      </div>
      <div class="tiles reveal">
{tiles}      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="row-head reveal">
        <h2 class="display h2">Selected work</h2>
        <a class="text-link" href="/work/">All work →</a>
      </div>
      <div class="work-cards reveal">
{work}      </div>
    </div>
  </section>

{cta_band()}</main>
"""
    return head("", "Every brand has a story. District 2 Media tells yours through short-form video, photos, social content and websites for restaurants and local brands.", "/") + header("home") + body + footer()


def services():
    sections = ""
    for s in SERVICES:
        inc = "".join(f"<li>{e(i)}</li>" for i in s["included"])
        sections += f"""  <section class="svc" id="{s['id']}">
    <div class="wrap svc-grid">
      <div class="svc-head reveal">
        <span class="label">{s['label']}</span>
        <h2 class="display h2">{e(s['title'])}</h2>
      </div>
      <div class="svc-body reveal">
        <p class="lead">{e(s['intro'])}</p>
        <h3 class="label svc-sub">What's included</h3>
        <ul class="deliverables">{inc}</ul>
        <p class="good"><span class="label">Good for</span> {e(s['good'])}</p>
        <a class="text-link" href="/contact/">Ask about {e(s['title'].lower())} →</a>
      </div>
    </div>
  </section>
"""
    body = f"""<main>
{page_hero('Services', 'What we <span class="hl">make</span>', 'One team for the content, the channels it runs on and the website it sends people to. Monthly plans or one-off projects.')}{subnav([(s['id'], s['title']) for s in SERVICES], 'Services on this page')}{sections}{cta_band('Not sure what you need?', "Tell us what's going on and we'll suggest where to start. Most clients begin with one shoot and a plan.")}</main>
"""
    return head("Services", "Short-form video, photography, social media management, websites and ordering, Google and local search, and paid ads for restaurants and local brands.", "/services/") + header("services") + body + footer()


def work():
    cases = "".join(case_html(w) for w in WORK)
    body = f"""<main>
{page_hero('Work', 'Selected <span class="hl">work</span>', 'Real projects, real businesses. More case studies are on the way.')}  <section class="section flush">
    <div class="wrap work">
{cases}    </div>
  </section>
{cta_band('Want results like these?')}</main>
"""
    return head("Work", "Case studies from District 2 Media: Pho Sapa restaurant website and QR ordering, and the Dustin Transforms coaching brand site.", "/work/") + header("work") + body + footer()


def about():
    who = "".join(f"""        <div class="who-card{' lead-card' if lead else ''}">
          <span class="label">{lab}</span>
          <h3 class="display h3">{e(t)}</h3>
          <p>{e(d)}</p>
        </div>
""" for lab, t, d, lead in WHO)
    steps = "".join(f'        <div class="step"><div class="num">{i:02d}</div><h3 class="display h3">{e(t)}</h3><p>{e(d)}</p></div>\n'
                    for i, (t, d) in enumerate(STEPS, 1))
    body = f"""<main>
{page_hero('About', '<span class="phrase">Founder-led.</span> <span class="phrase hl">Hands-on.</span>', 'District 2 Media is led by founder Dustin Tran, a creator and entrepreneur who works on both sides of your marketing: the content that makes people stop scrolling, and the website and tools that turn them into customers.')}{subnav([('story', 'Our approach'), ('who', 'Who we work with'), ('process', 'How it works')], 'About sections')}  <section class="section" id="story">
    <div class="wrap about">
      <div class="reveal">
        <h2 class="display h2">Our approach</h2>
      </div>
      <div class="reveal">
        <p class="lead">Every project gets senior attention. Dustin sets the creative direction, plans every shoot and personally reviews every edit, post and page before it goes out.</p>
        <p>You get one point of contact and the same standard on every project, from the first call to the monthly report.</p>
        <dl class="facts">
          <div><dt>Content</dt><dd>Short-form video, photography, social media</dd></div>
          <div><dt>Web</dt><dd>Websites, ordering, booking and forms, hosted on Cloudflare</dd></div>
          <div><dt>Work with</dt><dd>Restaurants, local businesses and personal brands</dd></div>
          <div><dt>Your contact</dt><dd>Dustin, directly, from the first call to the monthly report</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <section class="section" id="who">
    <div class="wrap">
      <div class="section-head reveal">
        <h2 class="display h2">Who we<br>work with</h2>
        <p class="lead">Restaurants, salons, gyms and neighborhood shops. If people can walk in, book a visit or order from you, we'll help more of them find you.</p>
      </div>
      <div class="who reveal">
{who}      </div>
    </div>
  </section>

  <section class="section" id="process">
    <div class="wrap">
      <div class="section-head reveal">
        <h2 class="display h2">How it<br>works</h2>
        <p class="lead">Simple, fast and on your schedule. Shoots fit around service hours.</p>
      </div>
      <div class="steps reveal">
{steps}      </div>
    </div>
  </section>
{cta_band()}</main>
"""
    return head("About", "District 2 Media is a founder-led content and web studio for restaurants and local brands, led by Dustin Tran.", "/about/") + header("about") + body + footer()


def contact():
    body = f"""<main>
  <section class="page-hero contact-page">
    <div class="wrap contact">
      <div>
        <div class="eyebrow label"><span class="rec"></span>Now booking</div>
        <h1 class="display h2">Let's make<br>something.</h1>
        <p class="lead">Tell us about your business and what you need. We'll reply within one business day with next steps.</p>
        <div class="contact-alt">
          <span>Prefer email? <a class="text-link" id="email-link" href="mailto:{EMAIL}">{EMAIL}</a></span>
        </div>
      </div>
      <form class="form" id="contact-form" novalidate>
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
        <div class="row2">
          <div class="field"><label for="c-name">Your name</label><input class="input" id="c-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="c-biz">Business</label><input class="input" id="c-biz" name="business" autocomplete="organization" required></div>
        </div>
        <div class="row2">
          <div class="field"><label for="c-email">Email</label><input class="input" id="c-email" name="email" type="email" autocomplete="email" inputmode="email" required></div>
          <div class="field"><label for="c-phone">Phone <span class="opt">(optional)</span></label><input class="input" id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
        </div>
        <fieldset class="field">
          <legend>What do you need?</legend>
          <div class="chips">
            <label class="chip"><input type="checkbox" name="needs" value="Short-form video"><span>Video</span></label>
            <label class="chip"><input type="checkbox" name="needs" value="Photography"><span>Photos</span></label>
            <label class="chip"><input type="checkbox" name="needs" value="Social media management"><span>Social media</span></label>
            <label class="chip"><input type="checkbox" name="needs" value="Website"><span>Website</span></label>
            <label class="chip"><input type="checkbox" name="needs" value="Online / table ordering"><span>Ordering</span></label>
            <label class="chip"><input type="checkbox" name="needs" value="Google Business Profile"><span>Google profile</span></label>
            <label class="chip"><input type="checkbox" name="needs" value="Paid ads"><span>Ads</span></label>
          </div>
        </fieldset>
        <div class="row2">
          <div class="field"><label for="c-budget">Monthly budget</label>
            <select class="input" id="c-budget" name="budget">
              <option value="Not sure yet">Not sure yet</option>
              <option value="Under $500">Under $500</option>
              <option value="$500 - $1,000">$500 – $1,000</option>
              <option value="$1,000 - $2,500">$1,000 – $2,500</option>
              <option value="$2,500+">$2,500+</option>
              <option value="One-off project">One-off project</option>
            </select>
          </div>
          <div class="field"><label for="c-site">Website or Instagram <span class="opt">(optional)</span></label><input class="input" id="c-site" name="link" placeholder="@yourbusiness"></div>
        </div>
        <div class="field"><label for="c-msg">Tell us more</label><textarea class="input" id="c-msg" name="message" required placeholder="What you do, who your customers are, and what you'd like to change."></textarea></div>
        <div class="send-row">
          <button class="btn" type="submit" id="c-send">Send <span class="arrow">→</span></button>
          <span class="form-status" id="c-status" role="status"></span>
        </div>
      </form>
    </div>
  </section>
</main>
"""
    return head("Contact", "Start a project with District 2 Media. Tell us about your business and we'll reply within one business day.", "/contact/") + header("contact") + body + footer()


def not_found():
    body = """<main>
  <section class="page-hero nf">
    <div class="wrap">
      <div class="eyebrow label"><span class="rec"></span>404 · Scene missing</div>
      <h1 class="display h1 page-title">Cut. <span class="hl">Wrong take.</span></h1>
      <p class="lead">This page doesn't exist. Try one of these instead.</p>
      <div class="actions"><a class="btn" href="/">Home <span class="arrow">→</span></a><a class="btn btn-ghost" href="/services/">Services</a><a class="btn btn-ghost" href="/contact/">Contact</a></div>
    </div>
  </section>
</main>
"""
    return head("Page not found", "This page doesn't exist.", "/404", '\n  <meta name="robots" content="noindex">') + header("") + body + footer()


PAGES = {
    "index.html": home, "services/index.html": services, "work/index.html": work,
    "about/index.html": about, "contact/index.html": contact, "404.html": not_found,
}

if __name__ == "__main__":
    for rel, fn in PAGES.items():
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fn())
        print("wrote", out.relative_to(ROOT.parent))
    urls = "".join(f"  <url><loc>{SITE}{p}</loc></url>\n" for p in ["/", "/services/", "/work/", "/about/", "/contact/"])
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print("wrote public/sitemap.xml")
