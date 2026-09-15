# -*- coding: utf-8 -*-
"""Builds the multi-page Digital Group Media redesign as standalone
static HTML files sharing assets/css/styles.css and assets/js/main.js.

Run this from anywhere with:  python3 dev/build_pages.py
It writes the generated .html pages into the repo root (one level up
from this dev/ folder) so the site keeps working with GitHub Pages /
Cloudflare Pages, which expect index.html at the repo root."""
import os

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

NAV_ITEMS = [
    ("web-design.html", "Web Design"),
    ("digital-marketing-services.html", "Digital Marketing"),
    ("videography-services.html", "Video Production"),
    ("success-stories.html", "Success Stories"),
    ("about-us.html", "About Us"),
    ("contact.html", "Contact"),
]

# Real site navigation: two top-level items carry a dropdown of real
# sub-pages. (href, label, children | None) — children is a list of
# (href, label) tuples rendered as a dropdown on desktop and an
# indented sub-list on mobile.
NAV_STRUCTURE = [
    ("index.html", "Home", None),
    ("web-design.html", "Web Design", [
        ("web-design.html", "Website Development"),
        ("support.html", "WordPress Support"),
    ]),
    ("digital-marketing-services.html", "Digital Marketing Services", [
        ("ppc-management.html", "PPC Management"),
        ("sales-and-marketing-roadmap.html", "Sales and Marketing Roadmap"),
    ]),
    ("videography-services.html", "Video Production", None),
    ("success-stories.html", "Success Stories", None),
    ("about-us.html", "About Us", None),
    ("contact.html", "Contact", None),
]

BRAND_MARK = '''<img class="brand-mark" src="assets/images/logo-dgm.png" alt="" width="237" height="123">'''

ICON_DEFS = '''<svg class="icon-defs" aria-hidden="true">
  <symbol id="ic-arrow" viewBox="0 0 16 16"><path d="M2 8h11M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="ic-arrow-up" viewBox="0 0 16 16"><path d="M2 14 14 2M6 2h8v8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
  <symbol id="ic-chevron" viewBox="0 0 16 16"><path d="M4 6l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</svg>'''


def _active_in(href, children):
    return bool(children) and any(h == href for h, _ in children)


def header_block(active_href):
    desktop_items = []
    mobile_items = []
    dd_id = 0
    for href, label, children in NAV_STRUCTURE:
        if label == "Home":
            # Home is represented by the logo; still list it explicitly
            # on mobile, where the logo isn't part of the nav column.
            current = ' aria-current="page"' if href == active_href else ''
            mobile_items.append('<a href="%s"%s>%s</a>' % (href, current, label))
            continue
        if children:
            dd_id += 1
            parent_current = ' aria-current="page"' if (href == active_href or _active_in(active_href, children)) else ''
            dd_links = "\n        ".join(
                '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active_href else '', l)
                for h, l in children
            )
            desktop_items.append('''<div class="nav-item has-dropdown">
        <a class="nav-parent-link" href="%s"%s>%s</a>
        <button class="nav-caret-btn" type="button" aria-expanded="false" aria-controls="dd-%d" aria-label="Show %s submenu">
          <svg class="nav-caret" aria-hidden="true"><use href="#ic-chevron"/></svg>
        </button>
        <div class="nav-dropdown" id="dd-%d">
          %s
        </div>
      </div>''' % (href, parent_current, label, dd_id, label, dd_id, dd_links))
            mobile_items.append('<a href="%s"%s>%s</a>' % (href, parent_current, label))
            for h, l in children:
                mobile_items.append('<a class="mobile-sub" href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active_href else '', l))
        else:
            current = ' aria-current="page"' if href == active_href else ''
            desktop_items.append('<a href="%s"%s>%s</a>' % (href, current, label))
            mobile_items.append('<a href="%s"%s>%s</a>' % (href, current, label))
    nav_links = "\n      ".join(desktop_items)
    mobile_nav_links = "\n  ".join(mobile_items)
    return '''<a class="skip-link" href="#main">Skip to main content</a>

<header class="site-header" id="siteHeader">
  <div class="wrap">
    <a class="brand" href="index.html">
      %s
      <span class="brand-word"><span class="brand-full">Digital <b>Group</b> Media</span><span class="brand-short">D<b>G</b>M</span></span>
    </a>
    <nav class="nav-links" aria-label="Primary">
      %s
    </nav>
    <div class="nav-actions">
      <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
      <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="mobileNav" aria-label="Open menu">
        <span class="nav-toggle-bars"><span></span><span></span><span></span></span>
      </button>
    </div>
  </div>
</header>

<nav class="mobile-nav" id="mobileNav" aria-label="Mobile">
  %s
  <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
</nav>''' % (BRAND_MARK, nav_links, mobile_nav_links)


FOOTER = '''<footer class="site-footer">
  <div class="wrap footer-top">
    <div class="footer-brand">
      <a class="brand" href="index.html">
        %s
        <span class="brand-word">Digital <b>Group</b> Media</span>
      </a>
      <p>A Birmingham digital agency helping established UK SMEs build brands, websites and marketing systems that actually get results.</p>
    </div>
    <div class="footer-col">
      <h4>Web Design</h4>
      <ul>
        <li><a href="web-design.html">Website Development</a></li>
        <li><a href="support.html">WordPress Support</a></li>
      </ul>
      <h4 class="footer-col-spaced">Digital Marketing</h4>
      <ul>
        <li><a href="digital-marketing-services.html">All Marketing Services</a></li>
        <li><a href="ppc-management.html">PPC Management</a></li>
        <li><a href="sales-and-marketing-roadmap.html">Sales &amp; Marketing Roadmap</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Company</h4>
      <ul>
        <li><a href="videography-services.html">Video Production</a></li>
        <li><a href="success-stories.html">Success Stories</a></li>
        <li><a href="about-us.html">About Us</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="privacy-policy.html">Privacy Policy</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <address>
        Digital Group Media Ltd<br>
        305 The Greenhouse<br>
        The Custard Factory, Gibb Street<br>
        Birmingham, B9 4DP<br><br>
        <a href="mailto:hello@digitalgroupmedia.com">hello@digitalgroupmedia.com</a><br>
        <a href="tel:01212247412">0121 224 7412</a>
      </address>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>&copy; <span id="year">2026</span> Digital Group Media Ltd. All rights reserved.</span>
    <span class="footer-legal">
      <a href="privacy-policy.html">Privacy Policy</a>
      <a href="about-us.html">About Us</a>
    </span>
  </div>
</footer>''' % BRAND_MARK


def org_jsonld(description):
    return '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Digital Group Media",
  "description": "%s",
  "url": "https://digitalgroupmedia.com/",
  "telephone": "+441212247412",
  "email": "hello@digitalgroupmedia.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "305 The Greenhouse, The Custard Factory, Gibb Street",
    "addressLocality": "Birmingham",
    "postalCode": "B9 4DP",
    "addressCountry": "GB"
  },
  "foundingDate": "2008",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "ratingCount": "1",
    "bestRating": "5"
  }
}
</script>''' % description


PAGE_SHELL = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Open+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
%(icon_defs)s

%(header)s

<main id="main">
%(body)s
</main>

%(footer)s

%(jsonld)s
<script src="assets/js/main.js"></script>
</body>
</html>
'''


def build_page(filename, title, description, active_href, body_html):
    html = PAGE_SHELL % {
        "title": title,
        "description": description,
        "icon_defs": ICON_DEFS,
        "header": header_block(active_href),
        "body": body_html,
        "footer": FOOTER,
        "jsonld": org_jsonld(description),
    }
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path, len(html), "bytes")


# Content-only variant for the Artifact tool's main `file_path` — the
# publish skeleton wraps this in <!doctype html><head>...<body>, so it
# must NOT carry its own doctype/html/head/body (unlike every other
# page in this site, which is served raw as a standalone document).
ARTIFACT_MAIN_SHELL = '''<title>%(title)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Open+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/css/styles.css">
%(icon_defs)s

%(header)s

<main id="main">
%(body)s
</main>

%(footer)s

%(jsonld)s
<script src="assets/js/main.js"></script>
'''


def build_artifact_main(filename, title, description, active_href, body_html):
    html = ARTIFACT_MAIN_SHELL % {
        "title": title,
        "icon_defs": ICON_DEFS,
        "header": header_block(active_href),
        "body": body_html,
        "footer": FOOTER,
        "jsonld": org_jsonld(description),
    }
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path, len(html), "bytes (artifact main, content-only)")
