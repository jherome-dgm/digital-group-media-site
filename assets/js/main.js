(function(){
  "use strict";
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- year ---------- */
  var yEl = document.getElementById('year');
  if (yEl) yEl.textContent = new Date().getFullYear();

  /* ---------- header solidify (sentinel-based, zero scroll listeners) ---------- */
  var header = document.getElementById('siteHeader');
  var heroEl = document.querySelector('.hero');
  var sentinelHeight = heroEl ? Math.max(heroEl.offsetHeight - 80, 72) : 72;
  var sentinel = document.createElement('div');
  sentinel.setAttribute('aria-hidden', 'true');
  sentinel.style.cssText = 'position:absolute;top:0;left:0;height:' + sentinelHeight + 'px;width:1px;pointer-events:none;';
  document.body.insertBefore(sentinel, document.body.firstChild);
  if ('IntersectionObserver' in window && header){
    var hObs = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ header.classList.toggle('is-solid', !e.isIntersecting); });
    }, { threshold: 0 });
    hObs.observe(sentinel);
  } else if (header){
    header.classList.add('is-solid');
  }

  /* ---------- mobile nav ---------- */
  var navToggle = document.getElementById('navToggle');
  var mobileNav = document.getElementById('mobileNav');
  function closeNav(){
    document.body.classList.remove('nav-open');
    if (navToggle) navToggle.setAttribute('aria-expanded','false');
  }
  if (navToggle){
    navToggle.addEventListener('click', function(){
      var open = document.body.classList.toggle('nav-open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  if (mobileNav){
    mobileNav.addEventListener('click', function(e){
      if (e.target.tagName === 'A') closeNav();
    });
  }
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') closeNav();
  });

  /* ---------- desktop dropdown submenus (click/tap + keyboard) ---------- */
  var navItems = document.querySelectorAll('.nav-item.has-dropdown');
  function closeAllDropdowns(except){
    navItems.forEach(function(item){
      if (item === except) return;
      item.classList.remove('is-open');
      var btn = item.querySelector('.nav-caret-btn');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    });
  }
  navItems.forEach(function(item){
    var btn = item.querySelector('.nav-caret-btn');
    if (!btn) return;
    btn.addEventListener('click', function(e){
      e.stopPropagation();
      var open = item.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      closeAllDropdowns(open ? item : null);
    });
  });
  document.addEventListener('click', function(){ closeAllDropdowns(null); });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') closeAllDropdowns(null);
  });

  /* ---------- reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
  if ('IntersectionObserver' in window && revealEls.length){
    var rObs = new IntersectionObserver(function(entries, obs){
      entries.forEach(function(e){
        if (e.isIntersecting){
          e.target.classList.add('is-visible');
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.18, rootMargin: '0px 0px -60px 0px' });
    revealEls.forEach(function(el){ rObs.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('is-visible'); });
  }

  /* ---------- count-up numbers ---------- */
  var counters = document.querySelectorAll('.js-count');
  function animateCount(el){
    var target = parseFloat(el.getAttribute('data-count')) || 0;
    var decimals = parseInt(el.getAttribute('data-decimals'), 10) || 0;
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduced){ el.textContent = target.toFixed(decimals) + suffix; return; }
    var start = null, dur = 1300;
    function tick(ts){
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(decimals) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  if ('IntersectionObserver' in window && counters.length){
    var cObs = new IntersectionObserver(function(entries, obs){
      entries.forEach(function(e){
        if (e.isIntersecting){ animateCount(e.target); obs.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function(el){ cObs.observe(el); });
  } else {
    counters.forEach(animateCount);
  }

  /* ---------- process scroll activation ---------- */
  var stages = document.querySelectorAll('.stage');
  var processTrack = document.querySelector('.process-track');
  if ('IntersectionObserver' in window && stages.length && processTrack){
    var maxActive = 0;
    var pObs = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        var n = parseInt(e.target.getAttribute('data-stage'), 10);
        if (e.isIntersecting){
          e.target.classList.add('is-active');
          if (n > maxActive) maxActive = n;
          processTrack.style.setProperty('--active-stage', maxActive);
        }
      });
    }, { threshold: 0.55, rootMargin: '0px 0px -15% 0px' });
    stages.forEach(function(s){ pObs.observe(s); });
  } else {
    stages.forEach(function(s){ s.classList.add('is-active'); });
    if (processTrack) processTrack.style.setProperty('--active-stage', 3);
  }

  /* ---------- testimonial rail controls ---------- */
  var rail = document.getElementById('testiRail');
  var prevBtn = document.getElementById('testiPrev');
  var nextBtn = document.getElementById('testiNext');
  function railStep(dir){
    if (!rail) return;
    var card = rail.querySelector('.testi-card');
    var step = card ? card.getBoundingClientRect().width + 24 : 400;
    rail.scrollBy({ left: dir * step, behavior: reduced ? 'auto' : 'smooth' });
  }
  if (prevBtn) prevBtn.addEventListener('click', function(){ railStep(-1); });
  if (nextBtn) nextBtn.addEventListener('click', function(){ railStep(1); });

  /* ---------- contact form (mailto handoff — static site, no backend) ---------- */
  var contactForm = document.getElementById('contactForm');
  if (contactForm){
    contactForm.addEventListener('submit', function(e){
      e.preventDefault();
      var data = new FormData(contactForm);
      var name = (data.get('name') || '').toString();
      var company = (data.get('company') || '').toString();
      var phone = (data.get('phone') || '').toString();
      var email = (data.get('email') || '').toString();
      var website = (data.get('website') || '').toString();
      var message = (data.get('message') || '').toString();
      var lines = [
        'Name: ' + name,
        'Company: ' + company,
        'Phone: ' + phone,
        'Email: ' + email,
        'Current website: ' + website,
        '',
        message
      ];
      var subject = encodeURIComponent('Website enquiry from ' + (name || 'your website'));
      var body = encodeURIComponent(lines.join('\n'));
      window.location.href = 'mailto:hello@digitalgroupmedia.com?subject=' + subject + '&body=' + body;
    });
  }

  /* Signal-canvas hero animation removed — the hero now uses a plain CSS
     gradient (matching the live site's magenta-to-orange brand gradient)
     instead of a JS particle network, for a cleaner look and less JS. */

})();
