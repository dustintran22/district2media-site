// District 2 Media site
//
// CONTACT FORM SETUP: create a free Web3Forms access key at https://web3forms.com with the
// inbox that should receive leads (e.g. info@district2media.com) and paste it below.
var WEB3FORMS_KEY = 'd9e5a454-eea7-45cf-a2b0-807fce207384';
var CONTACT_EMAIL = 'info@district2media.com';

(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Menu: hamburger on phones, dropdown submenus everywhere
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  var items = Array.prototype.slice.call(document.querySelectorAll('.has-menu'));
  function closeAll(except) {
    items.forEach(function (it) {
      if (it === except) return;
      it.classList.remove('open');
      var b = it.querySelector('.sub-toggle'); if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  items.forEach(function (it) {
    var b = it.querySelector('.sub-toggle');
    b.addEventListener('click', function (ev) {
      ev.stopPropagation();
      var open = !it.classList.contains('open');
      closeAll(it);
      it.classList.toggle('open', open);
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (ev) { if (!ev.target.closest('.has-menu')) closeAll(); });
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Escape') return;
    var openItem = document.querySelector('.has-menu.open');
    closeAll();
    if (openItem) openItem.querySelector('.sub-toggle').focus();
  });
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (!open) closeAll();
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); toggle.setAttribute('aria-label', 'Open menu'); closeAll(); }
    });
  }

  // Quick-jump bar: highlight the section being read
  var sub = document.querySelector('.subnav');
  if (sub && 'IntersectionObserver' in window) {
    var links = Array.prototype.slice.call(sub.querySelectorAll('a'));
    var byId = {};
    links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove('active'); });
        var a = byId[en.target.id];
        if (a) { a.classList.add('active'); a.scrollIntoView({ block: 'nearest', inline: 'nearest' }); }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    Object.keys(byId).forEach(function (id) { var el = document.getElementById(id); if (el) spy.observe(el); });
  }

  // Viewfinder: running timecode and the "Now shooting" word
  var tc = document.getElementById('timecode');
  if (tc) {
    var vidEl = document.getElementById('promo');
    var start = Date.now();
    var pad = function (n) { return String(n).padStart(2, '0'); };
    var tick = function () {
      var ms = vidEl && !isNaN(vidEl.currentTime) ? vidEl.currentTime * 1000 : Date.now() - start, s = Math.floor(ms / 1000);
      tc.textContent = pad(Math.floor(s / 3600)) + ':' + pad(Math.floor(s / 60) % 60) + ':' + pad(s % 60) + ':' + pad(Math.floor((ms % 1000) / 1000 * 24));
    };
    tick();
    if (!reduce) setInterval(tick, 1000 / 24);
  }
  // Promo video: timecode follows the video; Sound button unmutes
  var vid = document.getElementById('promo');
  var snd = document.getElementById('vf-sound');
  if (vid && snd) {
    snd.addEventListener('click', function () {
      vid.muted = !vid.muted;
      if (!vid.muted) { vid.play().catch(function () {}); }
      snd.setAttribute('aria-pressed', vid.muted ? 'false' : 'true');
      document.getElementById('vf-sound-label').textContent = vid.muted ? 'Sound' : 'Mute';
      document.getElementById('vf-sound-waves').setAttribute('d', vid.muted ? 'M23 9l-6 6M17 9l6 6' : 'M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14');
    });
    if (reduce) { vid.removeAttribute('autoplay'); vid.pause(); vid.controls = true; }
  }

  // Reveal on scroll (content is visible without JS; see .js .reveal in CSS)
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -6% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Contact form
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = document.getElementById('c-status');
  var send = document.getElementById('c-send');
  var f = form.elements;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status.className = 'form-status';
    status.textContent = '';
    var name = f.name.value.trim(), biz = f.business.value.trim(), email = f.email.value.trim(), msg = f.message.value.trim();
    var bad = !name ? f.name : !biz ? f.business : !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ? f.email : !msg ? f.message : null;
    if (bad) {
      status.className = 'form-status err';
      status.textContent = bad === f.email ? 'Enter a valid email so we can reply.' : 'Fill in your name, business, email and a short message.';
      bad.focus();
      return;
    }
    if (f.botcheck.checked) return;
    var picked = function (n) { return Array.prototype.map.call(form.querySelectorAll('input[name="' + n + '"]:checked'), function (c) { return c.value; }).join(', ') || 'Not specified'; };
    var needs = picked('needs'), goals = picked('goals');
    if (WEB3FORMS_KEY.indexOf('PASTE-') === 0) {
      status.className = 'form-status err';
      status.innerHTML = 'This form isn’t connected yet. Email <a class="text-link" href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a> instead.';
      return;
    }
    send.disabled = true;
    send.textContent = 'Sending…';
    fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        access_key: WEB3FORMS_KEY,
        subject: 'New project inquiry: ' + biz,
        from_name: 'District 2 Media website',
        replyto: email,
        'Name': name, 'Business': biz, 'Type of business': f.btype ? f.btype.value : '', 'Email': email, 'Phone': f.phone.value.trim(),
        'Looking for': needs, 'Main goals': goals, 'Monthly budget': f.budget.value, 'Website / Instagram': f.link.value.trim(), 'Message': msg
      })
    })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === false) throw new Error('send'); }); })
      .then(function () {
        form.reset();
        status.className = 'form-status ok';
        status.textContent = 'Thank you. We’ll reply within one business day to set up a strategy conversation.';
      })
      .catch(function () {
        status.className = 'form-status err';
        status.innerHTML = 'Couldn’t send. Try again, or email <a class="text-link" href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a>.';
      })
      .then(function () { send.disabled = false; send.innerHTML = 'Send <span class="arrow">→</span>'; });
  });
})();
