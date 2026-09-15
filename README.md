# Digital Group Media — website

This is the source for digitalgroupmedia.com: a static site (plain HTML,
CSS and JS, no build step required to run it) that deploys as-is to
GitHub Pages / Cloudflare Pages.

## Folder structure

```
index.html                      Home page
about-us.html
contact.html
digital-marketing-services.html
ppc-management.html
privacy-policy.html
sales-and-marketing-roadmap.html
success-stories.html
support.html
videography-services.html
web-design.html

assets/
  css/styles.css                All styling for every page
  js/main.js                    All interactive behaviour (nav, dropdown,
                                 counters, testimonial rail, etc.)
  images/logo-dgm.png           The logo used in the header and footer

dev/
  build_site.py                 Shared page shell, header/nav, footer
  build_pages.py                Each page's actual content
```

The `.html` files and `assets/` folder are what gets deployed — this is
the exact structure GitHub Pages / Cloudflare Pages expect, with
`index.html` at the repo root.

## Editing content directly (simplest)

For a small wording or styling tweak, just open the relevant `.html`
file (or `assets/css/styles.css` / `assets/js/main.js`) directly in
VS Code and edit it. This is the easiest path for most changes — no
tooling required, and it's exactly what the Claude Code / Claude
extension in VS Code is good at.

**One thing to know:** every page repeats the same header, nav and
footer markup at the top and bottom of the file, because this is a
plain static site with no shared-template system built in at the HTML
level. If you change the navigation or footer, you need to make the
same change in all 11 pages — or use the build scripts below, which
generate that shared markup from one place.

## Editing via the build scripts (for header/nav/footer changes)

The `dev/` folder holds the Python scripts this site was originally
generated with. They're optional, but useful specifically for anything
that touches **every page at once** — the header, the navigation
(including the dropdown menus), or the footer — since editing those in
one place and regenerating is much safer than hand-editing 11 files.

- `dev/build_site.py` — the page shell, the `NAV_STRUCTURE` list that
  drives the header/dropdown nav and the mobile menu, and the shared
  footer.
- `dev/build_pages.py` — the actual body content for every page (hero
  text, sections, pricing, FAQs, etc.), one Python-string block per
  page.

To regenerate every page after an edit to either file, run this from
the repo root (requires Python 3, no extra packages):

```
python3 dev/build_pages.py
```

That overwrites all 11 `.html` files in the repo root with freshly
generated versions. Nothing outside `dev/` needs to be touched by hand
for changes of this kind.

## Previewing locally

Since it's plain static HTML, you don't need a server to look at it —
opening `index.html` directly in a browser works. If you'd rather serve
it over `http://` (closer to production), from the repo root:

```
python3 -m http.server 8000
```

then visit `http://localhost:8000`.

## Deployment

This repo is connected to Cloudflare Pages, building from the `main`
branch with no build command and an output directory of `/` (the repo
root). Any push to `main` redeploys automatically — whether that push
came from editing the `.html`/`css`/`js` files directly, or from
running the build scripts and committing the regenerated pages.
