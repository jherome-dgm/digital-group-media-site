# -*- coding: utf-8 -*-
from build_site import build_page

STATS_STRIP = '''  <section class="stats-strip" aria-label="Numbers from the work">
    <div class="wrap">
      <div class="stats-grid reveal-stagger">
        <div class="stat">
          <span class="stat-num"><span class="js-count" data-count="15" data-suffix="+">0</span></span>
          <p class="stat-cap">Years in business<em>Established 2008</em></p>
        </div>
        <div class="stat">
          <span class="stat-num"><span class="js-count" data-count="4.9" data-decimals="1">0</span>/5</span>
          <p class="stat-cap">Average Google rating<em>Across client reviews</em></p>
        </div>
        <div class="stat">
          <span class="stat-num"><span class="js-count" data-count="1800" data-suffix="%">0</span></span>
          <p class="stat-cap">Peak campaign ROI<em>Everquip, Google Ads</em></p>
        </div>
        <div class="stat">
          <span class="stat-num">&#163;<span class="js-count" data-count="500" data-suffix="k+">0</span></span>
          <p class="stat-cap">Added client sales<em>WoodWool UK, 2 years</em></p>
        </div>
      </div>
    </div>
  </section>
'''

def faq_block(items):
    out = ['<div class="faq-list reveal">']
    for q, a in items:
        out.append('<details><summary>%s</summary><p>%s</p></details>' % (q, a))
    out.append('</div>')
    return "\n        ".join(out)


def cta_final(eyebrow, headline, sub, primary_label, primary_href, secondary_label, secondary_href):
    return '''  <section class="cta-final section-pad on-dark" id="final-cta" aria-labelledby="cta-h2">
    <canvas class="signal-web" id="ctaCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="eyebrow">%s</span>
      <h2 id="cta-h2" class="reveal">%s</h2>
      <p class="lead reveal">%s</p>
      <div class="hero-cta reveal">
        <a class="btn btn-primary" href="%s">%s<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        <a class="btn btn-ghost" href="%s">%s</a>
      </div>
    </div>
  </section>
''' % (eyebrow, headline, sub, primary_href, primary_label, secondary_href, secondary_label)


# ================================================================ HOME
home_body = '''  <section class="hero" id="top" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>DIGITAL GROUP MEDIA &middot; EST. 2008 &middot; BIRMINGHAM</span>
      <h1 id="hero-h1" class="fs-h1-fix">Not Seeing The <span class="hl">Dosh</span> From Your Digital?</h1>
      <p class="hero-sub">We guide established UK businesses through the process of building a brand online that people trust, engage with &mdash; and buy from.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        <a class="btn btn-ghost" href="success-stories.html">See Our Work</a>
      </div>
      <div class="hero-proof">
        <span><strong>4.9/5</strong> on Google Reviews</span>
        <span><strong>15+ years</strong> in business</span>
        <span>Based in the <strong>Custard Factory</strong>, Birmingham</span>
      </div>
    </div>
  </section>

''' + STATS_STRIP + '''
  <section class="section-pad" id="services" aria-labelledby="services-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">What We Do</span>
          <h2 id="services-h2">Ten disciplines. One connected system.</h2>
        </div>
        <p class="lead">Real growth rarely comes from one channel working in isolation &mdash; it comes from the whole system working together.</p>
      </div>

      <div class="feat-grid feat-grid--5 reveal-stagger">
        <div class="feat-card">
          <span class="feat-num">01</span>
          <h3>Foundation</h3>
          <p>These are the fundamentals that, understood with clarity, make everything else in sales &amp; marketing far easier and more effective.</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">02</span>
          <h3>Brand &amp; Positioning</h3>
          <p>More than a nice logo &mdash; this is about how people perceive your brand, your value proposition, and where it sits in the marketplace.</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">03</span>
          <h3>Website</h3>
          <p>The hub of most of your sales &amp; marketing activity, and the primary source of information for your prospects. <a class="btn-line" style="font:inherit;color:inherit;background:none;padding:0" href="web-design.html">See our web design service &rarr;</a></p>
        </div>
        <div class="feat-card">
          <span class="feat-num">04</span>
          <h3>Search &amp; AI Discoverability</h3>
          <p>Understanding the opportunities on search engines and AI platforms. Can people find you when searching for a solution to their problem?</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">05</span>
          <h3>Content Marketing</h3>
          <p>How effectively are you using video, images, audio and text to become the trusted thought leader in your market?</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">06</span>
          <h3>Email</h3>
          <p>A relatively low-cost tool that automates and scales delivery of your value proposition to the right people at the right time.</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">07</span>
          <h3>Social Media</h3>
          <p>Most of your customers are using some combination of Facebook, Instagram, TikTok, LinkedIn &amp; X. Are you part of the conversation?</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">08</span>
          <h3>Offline</h3>
          <p>How effectively are you using time-tested traditional sales and marketing methods to generate leads and sales?</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">09</span>
          <h3>Insights &amp; Analytics</h3>
          <p>What gets measured gets improved. Success is difficult to replicate or scale unless you measure how it happened in the first place.</p>
        </div>
        <div class="feat-card">
          <span class="feat-num">10</span>
          <h3>Systems, Tools &amp; Support</h3>
          <p>How effectively are you leveraging software tools, and expertise from outside your business, to improve sales &amp; marketing?</p>
        </div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="why section-pad on-dark" id="why" aria-labelledby="why-h2">
    <div class="wrap">
      <div class="why-layout">
        <div class="why-intro reveal">
          <span class="eyebrow">Why Digital Group Media</span>
          <h2 id="why-h2">Eight reasons agencies get compared to us.</h2>
          <p class="lead">We work with owners, directors and marketing managers of established UK SMEs who need better results from their online presence.</p>
          <a class="btn-line why-cta" href="about-us.html">Meet the team<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        </div>

        <div class="orbit reveal" aria-hidden="true">
          <div class="orbit-lines">
            <div class="orbit-line" style="--i:0"></div><div class="orbit-line" style="--i:1"></div>
            <div class="orbit-line" style="--i:2"></div><div class="orbit-line" style="--i:3"></div>
            <div class="orbit-line" style="--i:4"></div><div class="orbit-line" style="--i:5"></div>
            <div class="orbit-line" style="--i:6"></div><div class="orbit-line" style="--i:7"></div>
          </div>
          <div class="orbit-nodes">
            <div class="orbit-node" style="--i:0"><div class="orbit-card" tabindex="0"><div class="n">01</div><div class="t">Knowledge &amp; Experience</div></div></div>
            <div class="orbit-node" style="--i:1"><div class="orbit-card" tabindex="0"><div class="n">02</div><div class="t">Easy To Work With</div></div></div>
            <div class="orbit-node" style="--i:2"><div class="orbit-card" tabindex="0"><div class="n">03</div><div class="t">Results Driven</div></div></div>
            <div class="orbit-node" style="--i:3"><div class="orbit-card" tabindex="0"><div class="n">04</div><div class="t">Discernment</div></div></div>
            <div class="orbit-node" style="--i:4"><div class="orbit-card" tabindex="0"><div class="n">05</div><div class="t">Great Value</div></div></div>
            <div class="orbit-node" style="--i:5"><div class="orbit-card" tabindex="0"><div class="n">06</div><div class="t">Never Stop Learning</div></div></div>
            <div class="orbit-node" style="--i:6"><div class="orbit-card" tabindex="0"><div class="n">07</div><div class="t">Processes &amp; Systems</div></div></div>
            <div class="orbit-node" style="--i:7"><div class="orbit-card" tabindex="0"><div class="n">08</div><div class="t">Creativity</div></div></div>
          </div>
          <div class="orbit-hub"><span>DIGITAL<br>GROUP<br>MEDIA</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad" id="process" aria-labelledby="process-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">How We Work</span>
          <h2 id="process-h2">How we get your results.</h2>
        </div>
        <p class="lead">Three stages, in order &mdash; each one earns the next. Scroll to watch the signal move through the process.</p>
      </div>

      <div class="process-track">
        <div class="process-line" aria-hidden="true"><div class="process-line-fill" id="processFill"></div></div>
        <div class="process-stages" id="processStages">
          <div class="stage" data-stage="1">
            <div class="stage-dot"></div>
            <span class="stage-num">01 / 03</span>
            <h3>Discovery &amp; Understanding</h3>
            <p>We determine your business goals and the obstacles standing between you and them, before a single recommendation is made.</p>
          </div>
          <div class="stage" data-stage="2">
            <div class="stage-dot"></div>
            <span class="stage-num">02 / 03</span>
            <h3>Strategy Creation</h3>
            <p>A clear, actionable plan &mdash; built around what we found, not a template pulled from the last client.</p>
          </div>
          <div class="stage" data-stage="3">
            <div class="stage-dot"></div>
            <span class="stage-num">03 / 03</span>
            <h3>Action &amp; Implementation</h3>
            <p>We execute the plan and monitor results, adjusting as real data comes in rather than waiting for a quarterly review.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad" id="work" aria-labelledby="work-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">Selected Work</span>
          <h2 id="work-h2">Results you can check for yourself.</h2>
        </div>
        <p class="lead">Four highlights &mdash; <a class="btn-line" style="display:inline-flex" href="success-stories.html">see every success story&nbsp;&rarr;</a></p>
      </div>

      <div class="work-grid reveal-stagger">
        <article class="work-card">
          <div class="work-art">
            <div class="art-bg" style="background:linear-gradient(135deg,#d6095b,#313864);"></div>
            <div class="art-grid"></div>
            <span class="art-cat">Garage Equipment Supply</span>
          </div>
          <div class="work-info">
            <h3>Everquip</h3>
            <p>Branding, website, Google Ads, content and analytics delivered an 1800% return on ad spend and the business's best-ever sales figures.</p>
            <a class="btn-line work-link" href="https://inspectionpits.co.uk/" target="_blank" rel="noopener">View project<svg class="ic" aria-hidden="true"><use href="#ic-arrow-up"/></svg></a>
          </div>
        </article>
        <article class="work-card">
          <div class="work-art">
            <div class="art-bg" style="background:linear-gradient(135deg,#e2591c,#242a4d);"></div>
            <div class="art-grid"></div>
            <span class="art-cat">Industrial Parts Cleaning</span>
          </div>
          <div class="work-info">
            <h3>Sonic Solutions</h3>
            <p>Website redevelopment with Google Ads, SEO and LinkedIn marketing turned a trickle of weekly enquiries into a steady flow of daily ones.</p>
            <a class="btn-line work-link" href="https://sonicsolutionsltd.com/" target="_blank" rel="noopener">View project<svg class="ic" aria-hidden="true"><use href="#ic-arrow-up"/></svg></a>
          </div>
        </article>
        <article class="work-card">
          <div class="work-art">
            <div class="art-bg" style="background:linear-gradient(135deg,#313864,#d6095b);"></div>
            <div class="art-grid"></div>
            <span class="art-cat">Electrical Contracting</span>
          </div>
          <div class="work-info">
            <h3>UK Electrical Installations</h3>
            <p>Brand identity, assets, website and content strategy that reads as warm and modern to the clients and candidates it needs to attract.</p>
            <a class="btn-line work-link" href="https://ukelectrical.co.uk/" target="_blank" rel="noopener">View project<svg class="ic" aria-hidden="true"><use href="#ic-arrow-up"/></svg></a>
          </div>
        </article>
        <article class="work-card">
          <div class="work-art">
            <div class="art-bg" style="background:linear-gradient(135deg,#313864,#e2591c);"></div>
            <div class="art-grid"></div>
            <span class="art-cat">Gas Detection &amp; Safety Equipment</span>
          </div>
          <div class="work-info">
            <h3>Duomo UK</h3>
            <p>A full eCommerce rebuild with SEO, Google Ads and photography lets specifiers buy safety equipment online, phone-free.</p>
            <a class="btn-line work-link" href="https://duomo.co.uk/" target="_blank" rel="noopener">View project<svg class="ic" aria-hidden="true"><use href="#ic-arrow-up"/></svg></a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="testi section-pad" id="testimonials" aria-labelledby="testi-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">In Their Words</span>
          <h2 id="testi-h2">What clients say when the work is done.</h2>
        </div>
      </div>

      <div class="testi-rail reveal" id="testiRail" tabindex="0" aria-label="Client testimonials, scrollable">
        <blockquote class="testi-card">
          <p class="testi-quote">If you want the problem of how to deal with enquiries, DGM will create them for you.</p>
          <footer class="testi-who">
            <span class="testi-avatar" style="background:#313864;">SS</span>
            <span><span class="testi-name">Sonic Solutions</span><br><span class="testi-role">Industrial Parts Cleaning</span></span>
          </footer>
        </blockquote>
        <blockquote class="testi-card">
          <p class="testi-quote">We're running at around an ROI of 1800%, which is fantastic &mdash; some of the leads we are getting are fantastic.</p>
          <footer class="testi-who">
            <span class="testi-avatar" style="background:#e2591c;">EQ</span>
            <span><span class="testi-name">Everquip</span><br><span class="testi-role">Director</span></span>
          </footer>
        </blockquote>
        <blockquote class="testi-card">
          <p class="testi-quote">Superb business and some great people. The team at DGM have delivered me the ultimate service on my website and its branding, and continue to amaze me with their ongoing support.</p>
          <footer class="testi-who">
            <span class="testi-avatar" style="background:#d6095b;">GM</span>
            <span><span class="testi-name">James, GainMore Solutions</span><br><span class="testi-role">Business Consultancy</span></span>
          </footer>
        </blockquote>
        <blockquote class="testi-card">
          <p class="testi-quote">Without that, we wouldn't be getting the sales. You get this plausibility, and you think &mdash; these are the right guys.</p>
          <footer class="testi-who">
            <span class="testi-avatar" style="background:#242a4d;">BM</span>
            <span><span class="testi-name">Nick DeBorde, Beaumont</span><br><span class="testi-role">Director</span></span>
          </footer>
        </blockquote>
        <blockquote class="testi-card">
          <p class="testi-quote">The ongoing sales and marketing support DGM gives us has literally added over &#163;500,000 in sales to the business &mdash; and that's in the last two years alone.</p>
          <footer class="testi-who">
            <span class="testi-avatar" style="background:#313864;">WW</span>
            <span><span class="testi-name">WoodWool UK</span><br><span class="testi-role">Wood Packaging Manufacturer</span></span>
          </footer>
        </blockquote>
        <blockquote class="testi-card">
          <p class="testi-quote">Since my site was redeveloped, visitors have increased by 400%, sales have increased significantly, and I'm now capturing sales leads as well as giving a much better experience to my customers.</p>
          <footer class="testi-who">
            <span class="testi-avatar" style="background:#e2591c;">ET</span>
            <span><span class="testi-name">Helen, EasyTots</span><br><span class="testi-role">Owner</span></span>
          </footer>
        </blockquote>
      </div>

      <div class="testi-controls">
        <button class="testi-arrow prev" id="testiPrev" aria-label="Previous testimonial"><svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></button>
        <button class="testi-arrow next" id="testiNext" aria-label="Next testimonial"><svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></button>
      </div>
    </div>
  </section>

''' + cta_final(
    "Let's Talk",
    "Ready to make your digital presence work harder?",
    "Get a clear, honest view of what's working, what isn't, and where the real opportunities are for growth &mdash; for free.",
    "Book a Call", "contact.html", "Call 0121 224 7412", "tel:01212247412"
)

build_page(
    "index.html",
    "Digital Group Media | Digital Agency, Birmingham",
    "A Birmingham digital agency helping established UK SMEs with branding, websites, SEO, PPC and digital marketing since 2008.",
    "index.html",
    home_body,
)

print("home built")

# ================================================================ WEB DESIGN
web_design_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>WEB DESIGN &middot; FROM &#163;3,750 + VAT</span>
      <h1 id="hero-h1">High Performance Websites That <span class="hl">Delight</span> &amp; Inform Your Visitors</h1>
      <p class="hero-sub">Converting them into customers. A website isn't just there to validate your business card &mdash; it's the window to your business and should be working hard for you 24/7.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        <a class="btn btn-ghost" href="success-stories.html">See Our Work</a>
      </div>
    </div>
  </section>

''' + STATS_STRIP + '''
  <section class="section-pad" aria-labelledby="tiers-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">Three Ways In</span>
          <h2 id="tiers-h2">Pick the scope that matches where you are.</h2>
        </div>
        <p class="lead">Every tier starts with the same bespoke, contemporary design &mdash; the difference is how much of the wider system comes built in.</p>
      </div>

      <div class="tier-grid reveal-stagger">
        <div class="tier-card">
          <div class="tier-name">Foundation</div>
          <div class="tier-price">From &#163;3,750<span> +VAT</span></div>
          <p class="tier-desc">Get your marketing-ready website and the foundation of your online presence.</p>
          <ul class="tier-feat">
            <li>Half day in-person strategy &amp; planning session</li>
            <li>Bespoke contemporary design</li>
            <li>Unlimited pages</li>
            <li>Content management system</li>
            <li>Speed optimised</li>
            <li>Managed launch</li>
            <li>GA4, Search Console &amp; Bing Webmaster Tools configured</li>
            <li>Website training</li>
            <li>1 month unlimited hosting, support &amp; maintenance</li>
          </ul>
          <a class="btn btn-ghost btn-block" href="contact.html">Ask About Foundation</a>
        </div>
        <div class="tier-card tier-card--featured">
          <span class="tier-badge">Most Chosen</span>
          <div class="tier-name">Market Leader</div>
          <div class="tier-price">Custom<span> scope</span></div>
          <p class="tier-desc">Establish yourself as a leader in your industry with a thoroughly researched, planned website.</p>
          <ul class="tier-feat">
            <li>Full day strategy &amp; planning, incl. digital marketing</li>
            <li>Your own custom AI</li>
            <li>Bespoke contemporary design</li>
            <li>Content creation &amp; support</li>
            <li>Lead magnet production</li>
            <li>Professional photography</li>
            <li>Unlimited pages, CMS &amp; speed optimised</li>
            <li>3rd party testing &amp; managed launch</li>
            <li>3 months unlimited hosting, support &amp; maintenance</li>
          </ul>
          <a class="btn btn-primary btn-block" href="contact.html">Ask About Market Leader</a>
        </div>
        <div class="tier-card">
          <div class="tier-name">Apex</div>
          <div class="tier-price">Custom<span> scope</span></div>
          <p class="tier-desc">Only for serious businesses that intend to play in the big leagues online.</p>
          <ul class="tier-feat">
            <li>Everything in Market Leader</li>
            <li>Your own custom AI &amp; lead magnet production</li>
            <li>Professional photography</li>
            <li>3 months unlimited hosting, support &amp; maintenance</li>
            <li>3 months of Sales &amp; Marketing support (PPC, email, social media)</li>
          </ul>
          <a class="btn btn-ghost btn-block" href="contact.html">Ask About Apex</a>
        </div>
      </div>
      <p class="tier-note" style="text-align:center;margin-top:2rem;color:var(--text-mute);font-size:.88rem;">If you're unsure what any of these features and deliverables mean and how they would benefit your project, we'd be happy to run through it with you and answer any questions &mdash; <a class="btn-line" style="display:inline-flex" href="contact.html">get in touch&nbsp;&rarr;</a></p>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad" aria-labelledby="build-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">How We Build It</span>
          <h2 id="build-h2">Bespoke, tested, and handed over properly.</h2>
        </div>
      </div>
      <div class="feat-grid reveal-stagger">
        <div class="feat-card">
          <div class="feat-num">01</div>
          <h3>In-Person Strategy</h3>
          <p>A half to full-day strategy session before a single pixel is designed.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">02</div>
          <h3>Bespoke Design</h3>
          <p>Contemporary, on-brand design built for your business &mdash; not a recoloured template.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">03</div>
          <h3>Speed-Tested</h3>
          <p>Performance optimisation and third-party testing before launch, not after complaints.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">04</div>
          <h3>Managed Launch</h3>
          <p>A managed go-live, plus training so your team can actually use what we've built.</p>
        </div>
      </div>
    </div>
  </section>

''' + cta_final(
    "Free Review",
    "Ready for a website that earns its keep?",
    "Get a free, honest review of your current site &mdash; what's working, what's costing you enquiries, and what to fix first.",
    "Book a Call", "contact.html", "Get Your Free Review", "contact.html"
)

build_page(
    "web-design.html",
    "Web Design Services | Digital Group Media",
    "High-performance websites that delight and inform visitors, and convert them into customers. Bespoke web design for established UK SMEs, from Digital Group Media.",
    "web-design.html",
    web_design_body,
)

# ================================================================ DIGITAL MARKETING
dm_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>DIGITAL MARKETING &middot; BIRMINGHAM</span>
      <h1 id="hero-h1">Stop Leaving <span class="hl">Money</span> On The Table</h1>
      <p class="hero-sub">Digital marketing companies in Birmingham are ten a penny these days &mdash; the key is to find one that values meaningful outcomes like increased sales, not vanity metrics.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        <a class="btn btn-ghost" href="contact.html">Get Your Free Expert Review</a>
      </div>
    </div>
  </section>

''' + STATS_STRIP + '''
  <section class="section-pad" aria-labelledby="dm-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">What We Offer</span>
          <h2 id="dm-h2">Services that include, but aren't limited to&hellip;</h2>
        </div>
        <p class="lead">You may need our help with all or just some of these things, but it starts by establishing clear &amp; realistic objectives &mdash; e.g. 5 new business enquiries per working day.</p>
      </div>
      <div class="feat-grid reveal-stagger">
        <div class="feat-card">
          <div class="feat-num">01</div>
          <h3>Google Ads Management</h3>
          <p>Pay-Per-Click advertising built, tested and optimised around a clear return on investment.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">02</div>
          <h3>SEO</h3>
          <p>Search Engine Optimisation that gets you found by the people already searching for what you do.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">03</div>
          <h3>Landing Pages &amp; CRO</h3>
          <p>Landing page creation and Conversion Rate Optimisation, so more of your traffic turns into enquiries.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">04</div>
          <h3>E-Mail Marketing</h3>
          <p>Direct, automated communication that keeps your value proposition in front of the right people.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">05</div>
          <h3>"Done For You" LinkedIn Campaigns</h3>
          <p>Professional networking and lead generation handled for you on the platform your B2B buyers use.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">06</div>
          <h3>Facebook Ads Management</h3>
          <p>Social platform advertising and targeting built around real commercial outcomes.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">07</div>
          <h3>Social Media</h3>
          <p>Content strategy and community management that keeps your brand part of the conversation.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">08</div>
          <h3>Content Marketing</h3>
          <p>Strategic content that attracts and nurtures prospects long before they're ready to buy.</p>
        </div>
      </div>
      <p class="tier-note" style="text-align:center;margin-top:2.5rem;color:var(--text-mute);font-size:.92rem;max-width:62ch;margin-inline:auto;">We won't mindlessly waste your money or indulge in pointless or risky campaigns that don't have a clear return on investment. We'll only take on digital marketing work once we're all confident that we can deliver results that matter.</p>
      <div class="team-strip reveal" style="margin-top:2rem;justify-content:center;">
        <span class="team-chip">Google Ads</span>
        <span class="team-chip">Facebook Ads</span>
        <span class="team-chip">LinkedIn</span>
        <span class="team-chip">ActiveCampaign</span>
        <span class="team-chip">WordPress</span>
        <span class="team-chip">Mailchimp</span>
        <span class="team-chip">Hotjar</span>
        <span class="team-chip">Zapier</span>
        <span class="team-chip">Swydo</span>
        <span class="team-chip">CallRail</span>
      </div>
    </div>
  </section>

''' + cta_final(
    "Free Review",
    "Ready to stop leaving money on the table?",
    "Get a clear, honest view of what's working, what isn't, and where the real opportunities are for growth &mdash; for free.",
    "Book a Call", "contact.html", "Get Your Free Expert Review", "contact.html"
)

build_page(
    "digital-marketing-services.html",
    "Digital Marketing Services | Digital Group Media",
    "Results-focused digital marketing for UK SMEs: Google Ads, SEO, landing pages, email, LinkedIn, Facebook Ads, social and content marketing.",
    "digital-marketing-services.html",
    dm_body,
)

# ================================================================ VIDEOGRAPHY
video_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>VIDEOGRAPHY SERVICES &middot; FROM &#163;2,495</span>
      <h1 id="hero-h1">Give Your Business The <span class="hl">Edge</span></h1>
      <p class="hero-sub">Starting from as little as &#163;2,495, give your business the edge with a compelling video that can be expertly shot and edited within 24 hours.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        <a class="btn btn-ghost" href="success-stories.html">See Our Work</a>
      </div>
    </div>
  </section>

''' + STATS_STRIP + '''
  <section class="section-pad" aria-labelledby="video-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">Why Businesses Choose Us</span>
          <h2 id="video-h2">Fast, professional, and built on real brands.</h2>
        </div>
      </div>
      <div class="feat-grid reveal-stagger">
        <div class="feat-card">
          <div class="feat-num">01</div>
          <h3>Same-Day Turnaround</h3>
          <p>Professionally shot and edited video, often delivered within 24 hours.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">02</div>
          <h3>Full Crew, No Hassle</h3>
          <p>Professional shooting and post-production, handled start to finish, on-site or in-studio.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">03</div>
          <h3>Built On Real Brands</h3>
          <p>Portfolio work for UK Electrical Installations, Sonic Solutions, BLOCC Interiors, Duomo UK and more.</p>
        </div>
        <div class="feat-card">
          <div class="feat-num">04</div>
          <h3>Priced To Start</h3>
          <p>From &#163;2,495 &mdash; a serious video asset without agency-scale overhead.</p>
        </div>
      </div>
      <div class="team-strip reveal" style="margin-top:2.5rem;">
        <span class="team-chip">Applied Pumps</span>
        <span class="team-chip">Beaumont</span>
        <span class="team-chip">BLOCC Interiors</span>
        <span class="team-chip">C&amp;D South West</span>
        <span class="team-chip">Duomo UK</span>
        <span class="team-chip">EasyTots</span>
      </div>
    </div>
  </section>

''' + cta_final(
    "Let's Talk",
    "Ready for video that gives you the edge?",
    "Tell us what you're trying to show off &mdash; product, premises, people &mdash; and we'll tell you what it takes to shoot it properly.",
    "Book a Call", "contact.html", "Call 0121 224 7412", "tel:01212247412"
)

build_page(
    "videography-services.html",
    "Videography Services | Digital Group Media",
    "Professionally shot and edited business video, often delivered within 24 hours, from Digital Group Media. From £2,495.",
    "videography-services.html",
    video_body,
)

# ================================================================ WORDPRESS SUPPORT
support_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>WORDPRESS SUPPORT &middot; &#163;99pm</span>
      <h1 id="hero-h1">Unlimited WordPress <span class="hl">Support</span>, Hosting &amp; Maintenance</h1>
      <p class="hero-sub">&#163;99pm for peace of mind &mdash; we proactively monitor, secure and update your site, so your investment in having a website keeps paying off.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        <a class="btn btn-ghost" href="contact.html">Request a Free Expert Review</a>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="wrap">
      <div class="about-story">
        <div class="reveal">
          <span class="eyebrow">Why Support Matters</span>
          <h2>Peace of mind, and more from your investment.</h2>
        </div>
        <div class="lead-block reveal">
          <p>The purpose of our website support service is to ensure peace of mind and to help you make the most of your investment in having a website in the first place.</p>
          <p>At a fundamental level, you'll enjoy the fact that behind the scenes we're pro-actively monitoring, securing and updating your website for you. Further, with your input, we can continually add fresh content and optimise performance &mdash; ensuring your website continues to perform well and stay aligned with your business goals.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad on-dark why" aria-labelledby="incl-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">What's Included</span>
        <h2 id="incl-h2">Everything in your &#163;99pm&hellip;</h2>
      </div>
      <div class="values-grid reveal-stagger" style="margin-top:3rem;">
        <div class="value-card"><h3>Unlimited Site Tasks</h3><p>Any technical task on the list below, whenever you need it.</p></div>
        <div class="value-card"><h3>Unlimited Content Updates</h3><p>Text, images and pages kept current without you touching the CMS.</p></div>
        <div class="value-card"><h3>Twice Daily Backups</h3><p>Two full backups a day, so nothing meaningful is ever at risk.</p></div>
        <div class="value-card"><h3>SSL Certificate</h3><p>Kept active and correctly configured at all times.</p></div>
        <div class="value-card"><h3>Task &amp; Monitoring Dashboard</h3><p>Full visibility of what's being managed and when.</p></div>
        <div class="value-card"><h3>Vulnerability Scanning</h3><p>Ongoing scans to catch security issues before they're a problem.</p></div>
        <div class="value-card"><h3>Uptime Monitoring</h3><p>We know the moment your site goes down &mdash; usually before you do.</p></div>
        <div class="value-card"><h3>Managed Plugin, Theme &amp; WP Updates</h3><p>Kept current safely, without breaking your live site.</p></div>
        <div class="value-card"><h3>Bug Fixes &amp; Enhancements</h3><p>Issues resolved as part of the service, not billed as extras.</p></div>
        <div class="value-card"><h3>Minor HTML &amp; CSS Tweaks</h3><p>Small design changes handled without a separate project.</p></div>
        <div class="value-card"><h3>World Class Web Hosting</h3><p>Fast, secure hosting included in your monthly fee.</p></div>
      </div>
    </div>
  </section>

  <section class="section-pad" aria-labelledby="tasks-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div>
          <span class="eyebrow">Unlimited Site Tasks</span>
          <h2 id="tasks-h2">A small sample of what "unlimited" covers.</h2>
        </div>
        <p class="lead">Every task below is included in your &#163;99pm &mdash; call as often as you need to.</p>
      </div>
      <div class="prose tasks-columns reveal">
        <p>(Re)Install WordPress</p>
        <p>Fix Configuration File</p>
        <p>Optimise / Clean Up Hosting</p>
        <p>Activate SSL &amp; Force SSL</p>
        <p>Fix Connectivity Issue</p>
        <p>Reset Admin Passwords</p>
        <p>Add 3rd Party Code</p>
        <p>Fix Contact Form Errors</p>
        <p>Restore a Site &amp; On-Demand Backups</p>
        <p>Add Cloudflare</p>
        <p>Fix Dead Links</p>
        <p>Set Up Backups &amp; Audit DNS</p>
        <p>Fix Plugin Errors &amp; Update Plugins</p>
        <p>Set Up Cron Jobs</p>
        <p>Audit Hosting</p>
        <p>Fix White Screen of Death</p>
        <p>Set Up Custom Nameservers</p>
        <p>Change Site Domain &amp; Manage Domains</p>
        <p>Set Up Emails &amp; Configure MX Records</p>
        <p>Configure DNS &amp; Redirects</p>
        <p>Install a Plugin or Theme</p>
        <p>Set Up WordPress SSL</p>
        <p>Configure Hosting</p>
        <p>Install Demo Content</p>
        <p>Transfer Domain Between Providers</p>
        <p>Update CSS &amp; PHP Settings</p>
        <p>Create an SPF Record &amp; FTP Accounts</p>
        <p>Migrate Database &amp; Update WordPress</p>
        <p>Database Administration</p>
        <p>Website Migration</p>
        <p>Diagnose Internal Server Errors</p>
        <p>Optimise for SEO</p>
      </div>
    </div>
  </section>

''' + cta_final(
    "Our Guarantee",
    "Not 100% happy? We'll refund every penny.",
    "If you're not 100% happy, confident or satisfied with our service, we'll refund 100% of your money or give you the next month for free.",
    "Book a Call", "contact.html", "Call 0121 224 7412", "tel:01212247412"
)

build_page(
    "support.html",
    "WordPress Support & Hosting | Digital Group Media",
    "Unlimited WordPress website support, hosting and maintenance from Digital Group Media for £99pm — backups, security, updates and unlimited site tasks.",
    "support.html",
    support_body,
)

print("wordpress support built")

# ================================================================ PPC MANAGEMENT
ppc_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>PPC MANAGEMENT &middot; GOOGLE ADS</span>
      <h1 id="hero-h1">Not Seeing The <span class="hl">Cash</span> From Your Clicks?</h1>
      <p class="hero-sub">If you're looking to unlock the power of Google Ads, book your no-obligation Discovery Call or Google Ads Audit with either James or Danny.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
        <a class="btn btn-ghost" href="contact.html">Get a Free Google Ads Audit</a>
      </div>
    </div>
  </section>

  <section class="section-pad" aria-labelledby="why-ads-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div><span class="eyebrow">Why Google Ads</span><h2 id="why-ads-h2">Direct, measurable, and fast to act on.</h2></div>
      </div>
      <div class="feat-grid reveal-stagger">
        <div class="feat-card"><div class="feat-num">01</div><h3>Get To The Top Of Google</h3><p>Direct access to appear at the top of search results for the searches that matter to you.</p></div>
        <div class="feat-card"><div class="feat-num">02</div><h3>Beat Your Competition</h3><p>The tools to stay ahead and capture the attention of your potential customers first.</p></div>
        <div class="feat-card"><div class="feat-num">03</div><h3>Laser-Targeted Advertising</h3><p>Precisely target ads by location, demographics, interests and search intent.</p></div>
        <div class="feat-card"><div class="feat-num">04</div><h3>Instant Results</h3><p>Campaigns can start generating traffic and leads as soon as they go live.</p></div>
        <div class="feat-card"><div class="feat-num">05</div><h3>Measurable ROI</h3><p>Robust tracking and analytics let you measure return on investment accurately.</p></div>
        <div class="feat-card"><div class="feat-num">06</div><h3>Control &amp; Flexibility</h3><p>Adjust spend, scale campaigns up or down, and pause or resume as your business needs.</p></div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad" aria-labelledby="ideal-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">Is This For You?</span>
        <h2 id="ideal-h2">Who this is &mdash; and isn't &mdash; built for.</h2>
      </div>
      <div class="check-grid reveal-stagger" style="margin-top:2.5rem;">
        <div class="check-col is-yes">
          <h3>Who This Is Ideal For</h3>
          <ul>
            <li>Growing SMEs ready to scale</li>
            <li>Businesses seeking a steady, rhythmic flow of leads</li>
            <li>Entrepreneurs committed to strategic investment</li>
            <li>Marketing novices who want it done properly</li>
            <li>Those enhancing an existing Google Ads campaign</li>
            <li>Companies aiming for measurable results</li>
          </ul>
        </div>
        <div class="check-col is-no">
          <h3>Who This Is NOT For</h3>
          <ul>
            <li>Risk-averse business owners</li>
            <li>Budget-constrained businesses</li>
            <li>Those with short-term marketing goals</li>
            <li>Anyone lacking a clear value proposition</li>
            <li>Businesses unwilling to adapt on feedback</li>
            <li>Those with a poor existing web presence</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-pad on-dark why" aria-labelledby="why-us-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">Why Work With Us</span>
        <h2 id="why-us-h2">Award-winning, certified, and beyond the dashboard.</h2>
      </div>
      <div class="values-grid reveal-stagger" style="margin-top:3rem;">
        <div class="value-card"><h3>Award Winners</h3><p>Previous winners of the Best Business Enabler Award at the National Entrepreneur Awards.</p></div>
        <div class="value-card"><h3>Google Ads Experts</h3><p>Certified and highly experienced, having generated tens of millions of pounds through Google Ads.</p></div>
        <div class="value-card"><h3>&#163;400 Free Ad Spend</h3><p>Elevate your initial Google Ads experience with a substantial ad credit for new accounts.</p></div>
        <div class="value-card"><h3>Cost-Effective</h3><p>Competitively but fairly priced, enabling us to use the best people and tools.</p></div>
        <div class="value-card"><h3>Transparent Reporting</h3><p>Full call tracking, so you understand exactly what's working and why.</p></div>
        <div class="value-card"><h3>Beyond The Dashboard</h3><p>Expertise that extends past campaign management into your wider marketing picture.</p></div>
      </div>
    </div>
  </section>

  <section class="section-pad" aria-labelledby="how-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div><span class="eyebrow">How It Works</span><h2 id="how-h2">Four steps from discovery call to results.</h2></div>
      </div>
      <div class="feat-grid reveal-stagger">
        <div class="feat-card"><div class="feat-num">Step 1</div><h3>Discovery Call</h3><p>A 30-minute Zoom call with James or Danny to understand your USPs, audience and realistic customer-acquisition costs, with custom keyword and competitor insight.</p></div>
        <div class="feat-card"><div class="feat-num">Step 2</div><h3>Onboarding &amp; Set-Up</h3><p>Landing pages reviewed, competitors analysed, ad creative built, tracking and analytics installed &mdash; typically 1&ndash;2 weeks.</p></div>
        <div class="feat-card"><div class="feat-num">Step 3</div><h3>Campaign Launch &amp; Monitoring</h3><p>Real-time monitoring and adjustment as your campaigns go live, with a patient, data-driven approach to normal fluctuations.</p></div>
        <div class="feat-card"><div class="feat-num">Step 4</div><h3>Monitor, Optimise &amp; Report</h3><p>Ongoing quality-score checks, search-term analysis, call and form review, and human-written reporting &mdash; not just automated numbers.</p></div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad" aria-labelledby="price-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">Your Investment</span>
        <h2 id="price-h2">Straightforward setup and monthly management.</h2>
      </div>
      <div class="price-grid reveal-stagger" style="margin-top:2.5rem;">
        <div class="price-card">
          <h3>Onboarding &amp; Setup</h3>
          <div class="price-amount">&#163;195</div>
          <p class="price-desc">Kickstart your Google Ads journey swiftly and easily with a comprehensive setup package, including analytics, call and form tracking.</p>
        </div>
        <div class="price-card">
          <h3>Ongoing Monthly Management</h3>
          <div class="price-amount">&#163;395<span>/mo, up to &#163;1,000 spend</span></div>
          <p class="price-desc">+&#163;100 per additional &#163;1,000 of monthly ad spend managed. Covers bid management, A/B testing, conversion tracking, budget management and regular reporting.</p>
        </div>
      </div>
      <p style="text-align:center;margin-top:1.75rem;color:var(--text-mute);font-size:.88rem;max-width:60ch;margin-inline:auto;">Minimum commitment of 3 months, transitioning to a rolling monthly agreement with 30 days' notice to cancel. We recommend an ad spend of at least &#163;500 per month to properly kickstart your campaign.</p>
    </div>
  </section>

  <section class="section-pad" aria-labelledby="faq-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">Questions</span>
        <h2 id="faq-h2">Frequently Asked Questions</h2>
      </div>
      <div style="margin-top:2.5rem;">
''' + faq_block([
    ("How much does it cost to advertise with Google Ads?",
     "Two components: our management fee and your ad spend with Google. Our fee structure typically includes a one-time setup fee and a monthly management fee from £395/mo, with a recommended ad spend minimum of £500+ monthly. At the time of writing, the average cost per click across our managed accounts is around £1.21."),
    ("How long does it take to see results?",
     "Immediate visibility often occurs as soon as campaigns go live, but meaningful optimisation and results typically start emerging within the first 3 months, depending on industry competitiveness, ad spend and landing page quality."),
    ("What happens if it doesn't work?",
     "There's an element of risk in any advertising endeavour. We use Google's historical data to model expectations, and if a campaign isn't meeting its objectives, we'll be straightforward in our advice &mdash; including recommending a halt if that's in your best interest."),
    ("Do you offer any guarantees?",
     "An absolute guarantee of campaign success isn't realistic given the variables involved, but we guarantee our unwavering commitment to high-quality work, transparent reporting and regular updates, with no long-term binding contracts."),
    ("How often will I get updates &amp; reports?",
     "Regular monthly reports from your campaign manager, including a detailed Loom video recording covering the month's activity and results, plus weekly or ad-hoc updates by email or phone, Monday to Friday."),
    ("How long are your contracts and what happens if I want to cancel?",
     "A three-month commitment with a one-month notice period thereafter. We're not here to keep you financially shackled to us if you're not happy with the results."),
    ("Who will be running my campaign day to day?",
     "A team of Google Ads certified professionals reviews your account weekly, with a dedicated technician handling daily monitoring and a named account manager as your main point of contact."),
]) + '''
      </div>
    </div>
  </section>

''' + cta_final(
    "Let's Talk",
    "Ready to see what your clicks could be worth?",
    "Book a no-obligation Discovery Call or Google Ads Audit with James or Danny.",
    "Book a Call", "contact.html", "Call 0121 224 7412", "tel:01212247412"
)

build_page(
    "ppc-management.html",
    "PPC Management | Google Ads | Digital Group Media",
    "Google Ads (PPC) management from Digital Group Media, Birmingham — certified experts, transparent reporting, from £195 setup and £395/mo management.",
    "ppc-management.html",
    ppc_body,
)

print("ppc-management built")

# ================================================================ SALES & MARKETING ROADMAP
roadmap_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>SALES &amp; MARKETING ROADMAP</span>
      <h1 id="hero-h1">Chart Your Course With A Bespoke <span class="hl">Roadmap</span></h1>
      <p class="hero-sub">A bespoke, actionable sales &amp; marketing plan tailored to your business goals &mdash; giving you the clarity you need to accelerate growth, sales and revenue.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
      </div>
    </div>
  </section>

  <section class="section-pad">
    <div class="wrap">
      <div class="about-story">
        <div class="reveal">
          <span class="eyebrow">The Idea</span>
          <h2>This is YOUR map to YOUR treasure.</h2>
        </div>
        <div class="lead-block reveal">
          <p>Imagine having one of our experts spend two full days with you, diving deep into your business, your goals, your competitors and your customers through a series of targeted exercises and collaborative sessions.</p>
          <p>Within a week or so, you receive an entirely custom-to-you action plan covering all the key activity areas and priorities in practical terms, along with the resources and guidance to get them done.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad on-dark why" aria-labelledby="why-rm-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">Why A Roadmap</span>
        <h2 id="why-rm-h2">Six reasons to get one built.</h2>
      </div>
      <div class="values-grid values-grid--3 reveal-stagger" style="margin-top:3rem;">
        <div class="value-card"><h3>Understand Your Goals</h3><p>We tailor the roadmap to align perfectly with your vision, so every step moves you closer to your desired outcomes.</p></div>
        <div class="value-card"><h3>Get A Clear Plan Of Action</h3><p>A comprehensive, detailed plan outlining each step required &mdash; clarity and direction to navigate marketing with confidence.</p></div>
        <div class="value-card"><h3>Remove The Guesswork</h3><p>Clear, evidence-based strategies and tactics give you and your team the confidence to focus on what works.</p></div>
        <div class="value-card"><h3>Allocate Budget &amp; Resources</h3><p>Detailed guidance on where to allocate your budget for maximum impact and improved return on investment.</p></div>
        <div class="value-card"><h3>Outmanoeuvre Competitors</h3><p>In-depth analysis and strategic insight highlight opportunities to get and stay ahead in your market.</p></div>
        <div class="value-card"><h3>Increase Company Value</h3><p>A well-executed strategy builds a stronger brand, increases customer loyalty and drives revenue growth.</p></div>
      </div>
    </div>
  </section>

  <section class="section-pad" aria-labelledby="familiar-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">Sound Familiar?</span>
        <h2 id="familiar-h2">Does this sound like you?</h2>
      </div>
      <div class="familiar-list reveal-stagger" style="margin-top:2.5rem;">
        <div class="familiar-item"><h3>I want to grow sales but I don't know where to start</h3><p>Ambitious goals for growth, but unsure how to align sales and marketing strategies to achieve them.</p></div>
        <div class="familiar-item"><h3>I'm overwhelmed by marketing choices</h3><p>Facing a sea of tactics and strategies, unsure which ones will truly benefit your business.</p></div>
        <div class="familiar-item"><h3>I don't have the right skills in-house</h3><p>You recognise the need for advanced marketing strategies but lack the specialised team to implement them.</p></div>
        <div class="familiar-item"><h3>My marketing team needs direction</h3><p>Your team is working hard, but without a clear plan efforts feel scattered and uncoordinated.</p></div>
        <div class="familiar-item"><h3>I'm uncertain where to allocate budget</h3><p>You're investing in marketing but not confident you're spending it in the most effective areas.</p></div>
        <div class="familiar-item"><h3>My competitors are stealing my lunch</h3><p>Your competitors seem to be one step ahead, and you're struggling to outmanoeuvre them.</p></div>
        <div class="familiar-item"><h3>I need clarity and focus</h3><p>You want a clear, actionable plan that outlines exactly what steps to take to boost leads, sales and revenue.</p></div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad" aria-labelledby="cover-h2">
    <div class="wrap">
      <div class="head-row reveal">
        <div><span class="eyebrow">What It Covers</span><h2 id="cover-h2">Ten key activity areas, in one plan.</h2></div>
      </div>
      <div class="feat-grid feat-grid--5 reveal-stagger">
        <div class="feat-card"><div class="feat-num">01</div><h3>Foundation</h3><p>The fundamentals that make everything else in sales &amp; marketing far easier and more effective.</p></div>
        <div class="feat-card"><div class="feat-num">02</div><h3>Brand &amp; Positioning</h3><p>How people perceive your brand, your value proposition and where it fits in the marketplace.</p></div>
        <div class="feat-card"><div class="feat-num">03</div><h3>Website</h3><p>The hub of most of your sales &amp; marketing activity &mdash; your website should be your best salesperson.</p></div>
        <div class="feat-card"><div class="feat-num">04</div><h3>Search &amp; AI Discoverability</h3><p>Can people find you when searching for a solution to their problem or need?</p></div>
        <div class="feat-card"><div class="feat-num">05</div><h3>Content Marketing</h3><p>How effectively are you using video, images, audio and text to become a trusted thought leader?</p></div>
        <div class="feat-card"><div class="feat-num">06</div><h3>Email</h3><p>A relatively low-cost tool that automates and scales delivery of your value proposition.</p></div>
        <div class="feat-card"><div class="feat-num">07</div><h3>Social Media</h3><p>Are you part of the conversation on the platforms your customers already use?</p></div>
        <div class="feat-card"><div class="feat-num">08</div><h3>Offline</h3><p>How effectively are you using time-tested traditional sales &amp; marketing methods?</p></div>
        <div class="feat-card"><div class="feat-num">09</div><h3>Insights &amp; Analytics</h3><p>What gets measured gets improved &mdash; success is hard to replicate without it.</p></div>
        <div class="feat-card"><div class="feat-num">10</div><h3>Systems, Tools &amp; Support</h3><p>How effectively are you leveraging software and outside expertise?</p></div>
      </div>
    </div>
  </section>

  <section class="section-pad on-dark why" aria-labelledby="process-rm-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">The Process</span>
        <h2 id="process-rm-h2">From application to action plan.</h2>
      </div>
      <div class="values-grid reveal-stagger" style="margin-top:3rem;">
        <div class="value-card"><h3>1. Fill Out An Application</h3><p>Our simple form helps us understand your business and objectives, ensuring we're a good fit for each other.</p></div>
        <div class="value-card"><h3>2. Spend Two Days With Our Team</h3><p>Collaborative exercises and sessions dive deep into your business, goals, competitors and customers.</p></div>
        <div class="value-card"><h3>3. We'll Create Your Roadmap</h3><p>Within 4 weeks, a bespoke, organised, actionable 300+ page roadmap tailored to your needs.</p></div>
        <div class="value-card"><h3>4. Start Winning</h3><p>We present your roadmap and action plan, giving you the clarity and tools to fuel growth.</p></div>
      </div>
    </div>
  </section>

  <section class="section-pad" aria-labelledby="faq-rm-h2">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">Questions</span>
        <h2 id="faq-rm-h2">Frequently Asked Questions</h2>
      </div>
      <div style="margin-top:2.5rem;">
''' + faq_block([
    ("What is the cost of the Sales &amp; Marketing Roadmap service?",
     "£5,495 + VAT. You should easily see this investment returned to you &mdash; and if you can't, then this probably isn't for you."),
    ("How long does the entire process take?",
     "A two-day intensive session with our team, then within 4 weeks you'll receive your detailed 300+ page roadmap. In total, around 14 working days from start to finish."),
    ("Who will be delivering the roadmap?",
     "Led by one of our Directors and delivered by our experienced team of sales &amp; marketing professionals, who work closely with you to tailor it to your business."),
    ("Can you help us implement the roadmap?",
     "Absolutely. Beyond delivering the roadmap, we offer comprehensive digital marketing services to help implement it &mdash; website, SEO, PPC, social media and video production."),
    ("What if we need ongoing support?",
     "We offer ongoing support packages to keep you on track, with guidance, strategy adjustments and help navigating any challenges that arise."),
    ("How do we track the progress of our marketing efforts?",
     "Alongside your roadmap, we provide a tool to help you prioritise tasks and track progress, so you can measure effectiveness and make data-driven decisions."),
    ("Is this service suitable for small businesses?",
     "Yes. Designed to benefit businesses of all sizes &mdash; whether a small startup or a larger corporation, our tailored approach ensures your specific needs are met."),
    ("What makes your roadmap different from other marketing plans?",
     "It's not just a plan; it's a comprehensive, actionable guide tailored to your business, combining deep insight into your goals, competitors and market with evidence-based strategies and clear steps."),
]) + '''
      </div>
    </div>
  </section>

''' + cta_final(
    "Let's Talk",
    "Ready for your map to your treasure?",
    "Book a call to find out if a Sales & Marketing Roadmap is the right next step for your business.",
    "Book a Call", "contact.html", "Call 0121 224 7412", "tel:01212247412"
)

build_page(
    "sales-and-marketing-roadmap.html",
    "Sales & Marketing Roadmap | Digital Group Media",
    "A bespoke, actionable Sales & Marketing Roadmap from Digital Group Media — two days with our experts, a custom 300+ page action plan, from £5,495 + VAT.",
    "sales-and-marketing-roadmap.html",
    roadmap_body,
)

print("sales-and-marketing-roadmap built")

print("web-design, digital-marketing, videography built")

# ================================================================ SUCCESS STORIES
def work_card(gradient, category, name, desc, url):
    return '''        <article class="work-card">
          <div class="work-art">
            <div class="art-bg" style="background:linear-gradient(135deg,%s);"></div>
            <div class="art-grid"></div>
            <span class="art-cat">%s</span>
          </div>
          <div class="work-info">
            <h3>%s</h3>
            <p>%s</p>
            <a class="btn-line work-link" href="%s" target="_blank" rel="noopener">View project<svg class="ic" aria-hidden="true"><use href="#ic-arrow-up"/></svg></a>
          </div>
        </article>
''' % (gradient, category, name, desc, url)

WORK_CARDS = [
    ("#313864,#d6095b", "Electrical Contracting", "UK Electrical Installations",
     "Brand identity, assets, website and content strategy that reads as warm and modern to the clients and candidates it needs to attract.",
     "https://ukelectrical.co.uk/"),
    ("#e2591c,#242a4d", "Industrial Parts Cleaning", "Sonic Solutions",
     "Website redevelopment with Google Ads, SEO and LinkedIn marketing turned a trickle of weekly enquiries into a steady flow of daily ones.",
     "https://sonicsolutionsltd.com/"),
    ("#242a4d,#e2591c", "Interior Design Studio", "BLOCC Interiors",
     "Branding, website, SEO, Google Ads, email marketing and CRM working together to convert presence into service sales.",
     "https://blocc.co.uk/"),
    ("#d6095b,#313864", "Garage Equipment Supply", "Everquip",
     "Branding, website, Google Ads, content and analytics delivered an 1800% return on ad spend and the business's best-ever sales figures.",
     "https://inspectionpits.co.uk/"),
    ("#313864,#e2591c", "Gas Detection &amp; Safety Equipment", "Duomo UK",
     "A full eCommerce rebuild with SEO, Google Ads and photography lets specifiers buy safety equipment online, phone-free.",
     "https://duomo.co.uk/"),
    ("#e2591c,#d6095b", "Metal Pressings &amp; Fabrication", "QuTec",
     "New branding, logo and website with Google Ads gave a metal fabricator the credibility to be placed on six-figure deals.",
     "https://qutecpershoreltd.co.uk/"),
    ("#242a4d,#d6095b", "Transport &amp; Logistics", "C&amp;D South West",
     "A dynamic website, hosting and ongoing support keep a logistics operator visible in search while they focus on the road.",
     "https://cdsw.co.uk/"),
    ("#d6095b,#e2591c", "Business Consultancy", "GainMore Solutions",
     "Website, landing pages, content strategy, photography and Google Ads gave a coach and consultant credibility to match their expertise.",
     "https://gainmoresolutions.com/"),
    ("#313864,#242a4d", "Wood Packaging Manufacturer", "WoodWool UK",
     "Website, eCommerce, lead generation, email, CRM and SEO added over &#163;500,000 in sales to the business in two years.",
     "https://woodwooluk.com/"),
    ("#e2591c,#313864", "Baby-Led Weaning Products", "EasyTots",
     "A full eCommerce rebuild grew visitors by 400% and turned the site into a genuine sales and lead-generation channel.",
     "https://easytots.com/"),
    ("#242a4d,#313864", "Barware Supply (B2B)", "Beaumont",
     "Website development, Google Ads and video production the director credits as essential to the business's sales success.",
     "https://beaumonttm.co.uk/products/"),
    ("#d6095b,#242a4d", "Home Improvement Retail", "Kitchen Doors &amp; Worktops",
     "Website, SEO, Google Ads, content, CRM and email marketing built into one inbound system for lead generation.",
     "https://doorsandworktops.com/"),
]

success_cards_html = "".join(work_card(*c) for c in WORK_CARDS)

success_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>SELECTED WORK</span>
      <h1 id="hero-h1">Results You Can Check For Yourself</h1>
      <p class="hero-sub">Every project below links to the real, live business we built it for &mdash; no invented case studies, no stock photography.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a Call<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></a>
      </div>
    </div>
  </section>

''' + STATS_STRIP + '''
  <section class="section-pad">
    <div class="wrap">
      <div class="work-grid work-grid--3 reveal-stagger">
''' + success_cards_html + '''      </div>
    </div>
  </section>

''' + cta_final(
    "Let's Talk",
    "Want results like these for your business?",
    "Get a clear, honest view of what's working, what isn't, and where the real opportunities are for growth &mdash; for free.",
    "Book a Call", "contact.html", "Get Your Free Review", "contact.html"
)

build_page(
    "success-stories.html",
    "Success Stories | Digital Group Media",
    "Real client results from Digital Group Media: branding, websites, SEO and Google Ads work for established UK SMEs, linked to the live businesses.",
    "success-stories.html",
    success_body,
)

print("success-stories built")

# ================================================================ ABOUT US
about_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>ABOUT US &middot; EST. 2008</span>
      <h1 id="hero-h1">The People Behind Your <span class="hl">Digital</span> Growth</h1>
      <p class="hero-sub">A small, flexible Birmingham agency &mdash; built so every client gets top-level involvement, not a junior account team.</p>
    </div>
  </section>

  <section class="section-pad">
    <div class="wrap">
      <div class="about-story">
        <div class="reveal">
          <span class="eyebrow">Our Story</span>
          <h2>Fifteen-plus years, one straightforward idea.</h2>
        </div>
        <div class="lead-block reveal">
          <p>Digital Group Media was founded in 2008 by Managing Director James Middleditch. In 2012, Danny joined as a partner, and the team has since grown to include Nick, Mark, Jherome, Jemma and a number of additional specialists.</p>
          <p>We're based in the Custard Factory, in Birmingham's Digbeth creative quarter &mdash; and we've worked remotely, at least in part, since before it was a pandemic necessity. That lets us work with premier talent wherever they are, while keeping our overheads lower than a traditional agency.</p>
          <p>We stay small and flexible on purpose. It means every project gets top-level involvement &mdash; not delegated down to whoever's free that week.</p>
          <div class="team-strip">
            <span class="team-chip">James Middleditch</span>
            <span class="team-chip">Danny</span>
            <span class="team-chip">Nick</span>
            <span class="team-chip">Mark</span>
            <span class="team-chip">Jherome</span>
            <span class="team-chip">Jemma</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="why section-pad on-dark">
    <div class="wrap">
      <div class="center-head reveal">
        <span class="eyebrow">What We Stand For</span>
        <h2>Four things we don't compromise on.</h2>
      </div>
      <div class="values-grid reveal-stagger" style="margin-top:3rem;">
        <div class="value-card">
          <h3>Respect</h3>
          <p>Mutual regard between our agency and your business &mdash; we treat your company the way we'd want ours treated.</p>
        </div>
        <div class="value-card">
          <h3>Knowledge</h3>
          <p>Continuous investment in capability across every discipline we offer, not just the ones that are easy.</p>
        </div>
        <div class="value-card">
          <h3>Meaningful Results</h3>
          <p>We focus on projects with outcomes that are measurable and accountable, not just busy.</p>
        </div>
        <div class="value-card">
          <h3>Transparency</h3>
          <p>Clear communication about our strategy &mdash; and just as clear about our strengths and weaknesses.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="signal-divider" aria-hidden="true"></div>

  <section class="section-pad" aria-labelledby="why-h2">
    <div class="wrap">
      <div class="why-layout">
        <div class="why-intro reveal">
          <span class="eyebrow" style="color:var(--orange-text)">Why Digital Group Media</span>
          <h2 id="why-h2" style="color:var(--navy)">Eight reasons agencies get compared to us.</h2>
          <p class="lead">We work with owners, directors and marketing managers of established UK SMEs who need better results from their online presence.</p>
          <div class="why-desc-list" style="--text-col:var(--text)">
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">Knowledge &amp; Experience</summary><p style="color:var(--text-soft)">Over 15 years operating across diverse industries &mdash; insight that goes well beyond a hobbyist effort.</p></details>
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">Easy To Work With</summary><p style="color:var(--text-soft)">A strong emphasis on people skills, open communication and transparent relationships built on genuine partnership.</p></details>
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">Results Driven</summary><p style="color:var(--text-soft)">Success measured against metrics we agree together &mdash; visitor growth, conversion rate, or brand perception.</p></details>
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">Discernment</summary><p style="color:var(--text-soft)">We're selective about the projects we take on, partnering only where we can make a tangible difference.</p></details>
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">Great Value</summary><p style="color:var(--text-soft)">Premium pricing, justified through superior ROI and honest, transparent project scoping.</p></details>
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">We Never Stop Learning</summary><p style="color:var(--text-soft)">Continuous investment in emerging skills and strategies that benefit every client we work with.</p></details>
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">Processes &amp; Systems</summary><p style="color:var(--text-soft)">Refined project management that delivers high-quality work efficiently, with consistent updates along the way.</p></details>
            <details style="border-color:var(--line)"><summary style="color:var(--navy)">Creativity</summary><p style="color:var(--text-soft)">Contemporary, user-friendly design paired with creative problem-solving across every discipline.</p></details>
          </div>
        </div>
        <div class="orbit reveal" aria-hidden="true">
          <div class="orbit-lines">
            <div class="orbit-line" style="--i:0"></div><div class="orbit-line" style="--i:1"></div>
            <div class="orbit-line" style="--i:2"></div><div class="orbit-line" style="--i:3"></div>
            <div class="orbit-line" style="--i:4"></div><div class="orbit-line" style="--i:5"></div>
            <div class="orbit-line" style="--i:6"></div><div class="orbit-line" style="--i:7"></div>
          </div>
          <div class="orbit-nodes">
            <div class="orbit-node" style="--i:0"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">01</div><div class="t" style="color:var(--navy)">Knowledge &amp; Experience</div></div></div>
            <div class="orbit-node" style="--i:1"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">02</div><div class="t" style="color:var(--navy)">Easy To Work With</div></div></div>
            <div class="orbit-node" style="--i:2"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">03</div><div class="t" style="color:var(--navy)">Results Driven</div></div></div>
            <div class="orbit-node" style="--i:3"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">04</div><div class="t" style="color:var(--navy)">Discernment</div></div></div>
            <div class="orbit-node" style="--i:4"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">05</div><div class="t" style="color:var(--navy)">Great Value</div></div></div>
            <div class="orbit-node" style="--i:5"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">06</div><div class="t" style="color:var(--navy)">Never Stop Learning</div></div></div>
            <div class="orbit-node" style="--i:6"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">07</div><div class="t" style="color:var(--navy)">Processes &amp; Systems</div></div></div>
            <div class="orbit-node" style="--i:7"><div class="orbit-card" style="background:var(--paper-raised);border-color:var(--line)" tabindex="0"><div class="n" style="color:var(--orange-text)">08</div><div class="t" style="color:var(--navy)">Creativity</div></div></div>
          </div>
          <div class="orbit-hub"><span>DIGITAL<br>GROUP<br>MEDIA</span></div>
        </div>
      </div>
    </div>
  </section>

''' + STATS_STRIP + cta_final(
    "Let's Talk",
    "Ready to meet the team properly?",
    "Book a call &mdash; no pitch deck, just a conversation about what you're trying to achieve.",
    "Book a Call", "contact.html", "Call 0121 224 7412", "tel:01212247412"
)

build_page(
    "about-us.html",
    "About Us | Digital Group Media",
    "Founded in Birmingham in 2008, Digital Group Media is a small, flexible agency built so every client gets top-level involvement.",
    "about-us.html",
    about_body,
)

print("about-us built")

# ================================================================ CONTACT
contact_body = '''  <section class="hero hero--page" aria-labelledby="hero-h1">
    <div class="hero-grid" aria-hidden="true"></div>
    <canvas class="hero-canvas" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>CONTACT &middot; WE REPLY FAST</span>
      <h1 id="hero-h1">Let's Talk About Your <span class="hl">Growth</span></h1>
      <p class="hero-sub">Tell us where you're stuck, or just say hello &mdash; we read every message ourselves.</p>
    </div>
  </section>

  <section class="section-pad">
    <div class="wrap">
      <div class="contact-grid">
        <form id="contactForm" class="reveal" novalidate>
          <div class="form-grid">
            <div class="field">
              <label for="cf-name">Your name</label>
              <input id="cf-name" name="name" type="text" required autocomplete="name">
            </div>
            <div class="field">
              <label for="cf-company">Company <span class="opt">(optional)</span></label>
              <input id="cf-company" name="company" type="text" autocomplete="organization">
            </div>
          </div>
          <div class="form-row">
            <div class="form-grid">
              <div class="field">
                <label for="cf-phone">Best contact number</label>
                <input id="cf-phone" name="phone" type="tel" required autocomplete="tel">
              </div>
              <div class="field">
                <label for="cf-email">Your email</label>
                <input id="cf-email" name="email" type="email" required autocomplete="email">
              </div>
            </div>
            <div class="field">
              <label for="cf-website">Your current website <span class="opt">(if applicable)</span></label>
              <input id="cf-website" name="website" type="url" placeholder="https://">
            </div>
            <div class="field">
              <label for="cf-message">How can we help?</label>
              <textarea id="cf-message" name="message" required></textarea>
            </div>
            <label class="check-row"><input type="checkbox" required> I agree to the Privacy Policy.</label>
            <label class="check-row"><input type="checkbox"> Keep me posted with occasional news and updates.</label>
            <button type="submit" class="btn btn-primary btn-block">Send Message<svg class="ic" aria-hidden="true"><use href="#ic-arrow"/></svg></button>
            <p class="form-note">This opens a pre-filled email to hello@digitalgroupmedia.com from your own email client &mdash; nothing is stored on this page.</p>
          </div>
        </form>

        <div class="contact-card reveal">
          <h3>Digital Group Media Ltd</h3>
          <address>
            305 The Greenhouse<br>
            The Custard Factory, Gibb Street<br>
            Birmingham, B9 4DP, UK<br><br>
            <a href="tel:01212247412">0121 224 7412</a><br>
            <a href="mailto:hello@digitalgroupmedia.com">hello@digitalgroupmedia.com</a><br>
            <a href="mailto:support@digitalgroupmedia.com">support@digitalgroupmedia.com</a> (support)
          </address>
          <a class="btn-line" href="https://www.google.com/maps/search/?api=1&amp;query=305+The+Greenhouse+The+Custard+Factory+Gibb+Street+Birmingham+B9+4DP" target="_blank" rel="noopener">Get Directions<svg class="ic" aria-hidden="true"><use href="#ic-arrow-up"/></svg></a>
          <div class="map-note">Rated 4.9/5 on Google Reviews &middot; 15+ years working with established UK SMEs.</div>
        </div>
      </div>
    </div>
  </section>
'''

build_page(
    "contact.html",
    "Contact Us | Digital Group Media",
    "Get in touch with Digital Group Media, Birmingham: call 0121 224 7412, email hello@digitalgroupmedia.com, or send a message.",
    "contact.html",
    contact_body,
)

# ================================================================ PRIVACY POLICY
privacy_body = '''  <section class="hero hero--page section-pad-sm" aria-labelledby="hero-h1">
    <div class="wrap">
      <span class="hero-badge"><span class="dot"></span>LEGAL</span>
      <h1 id="hero-h1" style="max-width:20ch;font-size:clamp(2rem,3.6vw + 1rem,3rem);">Privacy Policy</h1>
      <p class="hero-sub">How Digital Group Media Ltd collects, uses and protects your information.</p>
    </div>
  </section>

  <section class="section-pad">
    <div class="wrap">
      <div class="prose reveal">
        <p>This policy explains what personal data Digital Group Media Ltd collects through this website, why we collect it, and the choices you have. If anything here is unclear, <a class="btn-line" style="display:inline-flex" href="contact.html">get in touch&nbsp;&rarr;</a></p>

        <h2>What information do we collect about you?</h2>
        <p>We collect personal data through contact forms, emails, blog comments and cookies &mdash; including your name, email address, postal address, phone number, IP address and company details.</p>

        <h2>Why we need your data</h2>
        <p>We use the information you give us to respond to your enquiries, fulfil requests, manage accounts, send marketing communications you've opted into, and personalise your experience of this website.</p>

        <h2>How long will we store your data?</h2>
        <p>We retain basic personal data for a minimum of six years, in line with UK tax law. Marketing data is kept until you ask us to remove it.</p>

        <h2>Marketing</h2>
        <p>Where you've opted in, we may send you updates about our products and services. You can opt out at any time.</p>

        <h2>What are your rights?</h2>
        <p>You can ask to see the personal information we hold about you and request corrections. If you're unhappy with how we've handled your data, you can complain to the Information Commissioner's Office (ICO).</p>

        <h2>Cookies &amp; tracking</h2>
        <p>This site can use cookies via services such as Google Analytics, Hotjar, A1 WebStats, ActiveCampaign and Tawk.to. You can manage or disable cookies at any time through your browser settings.</p>

        <h2>Other websites</h2>
        <p>This privacy policy only applies to this website. Where we link to other sites, they'll have their own separate policies.</p>

        <h2>Changes to this policy</h2>
        <p>We review this policy regularly. Any updates will be posted on this page.</p>

        <h2>How to contact us</h2>
        <p>For any privacy-related questions, email <a class="btn-line" style="display:inline-flex" href="mailto:privacy@digitalgroupmedia.com">privacy@digitalgroupmedia.com&nbsp;&rarr;</a> or write to us at 305 The Greenhouse, The Custard Factory, Gibb Street, Birmingham, B9 4DP.</p>
      </div>
    </div>
  </section>
'''

build_page(
    "privacy-policy.html",
    "Privacy Policy | Digital Group Media",
    "How Digital Group Media Ltd collects, uses and protects your personal data.",
    "privacy-policy.html",
    privacy_body,
)

print("contact, privacy-policy built")

# ================================================================ ARTIFACT MAIN (content-only index for Artifact publish)
from build_site import build_artifact_main
build_artifact_main(
    "index-artifact.html",
    "Digital Group Media | Digital Agency, Birmingham",
    "A Birmingham digital agency helping established UK SMEs with branding, websites, SEO, PPC and digital marketing since 2008.",
    "index.html",
    home_body,
)
print("artifact main variant built")
