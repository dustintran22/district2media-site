// District 2 Media site
//
// CONTACT FORM SETUP: create a free Web3Forms access key at https://web3forms.com with the
// inbox that should receive leads (e.g. hello@district2media.com) and paste it below.
var WEB3FORMS_KEY = 'PASTE-YOUR-WEB3FORMS-ACCESS-KEY-HERE';
var CONTACT_EMAIL = 'hello@district2media.com';

(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Viewfinder: running timecode and the "Now shooting" word
  var tc = document.getElementById('timecode');
  if (tc) {
    var start = Date.now();
    var pad = function (n) { return String(n).padStart(2, '0'); };
    var tick = function () {
      var ms = Date.now() - start, s = Math.floor(ms / 1000);
      tc.textContent = pad(Math.floor(s / 3600)) + ':' + pad(Math.floor(s / 60) % 60) + ':' + pad(s % 60) + ':' + pad(Math.floor((ms % 1000) / 1000 * 24));
    };
    tick();
    if (!reduce) setInterval(tick, 1000 / 24);
  }
  var word = document.getElementById('vf-word');
  if (word && !reduce) {
    var words = ['Restaurants', 'Cafés', 'Salons', 'Gyms', 'Coaches', 'Local shops', 'Your business'];
    var i = 0;
    setInterval(function () {
      i = (i + 1) % words.length;
      word.classList.remove('swap');
      void word.offsetWidth;
      word.textContent = words[i];
      word.classList.add('swap');
    }, 2200);
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
    var needs = Array.prototype.map.call(form.querySelectorAll('input[name="needs"]:checked'), function (c) { return c.value; }).join(', ') || 'Not specified';
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
        'Name': name, 'Business': biz, 'Email': email, 'Phone': f.phone.value.trim(),
        'Needs': needs, 'Monthly budget': f.budget.value, 'Website / Instagram': f.link.value.trim(), 'Message': msg
      })
    })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === false) throw new Error('send'); }); })
      .then(function () {
        form.reset();
        status.className = 'form-status ok';
        status.textContent = 'Got it. We’ll reply within one business day.';
      })
      .catch(function () {
        status.className = 'form-status err';
        status.innerHTML = 'Couldn’t send. Try again, or email <a class="text-link" href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a>.';
      })
      .then(function () { send.disabled = false; send.innerHTML = 'Send <span class="arrow">→</span>'; });
  });
})();
