/* CCM Secretarial — progressive enhancement. All content works without JS. */
(function () {
  'use strict';
  var WA = '60164779365';
  var L = JSON.parse(document.getElementById('i18n').textContent);
  var SH = L.sh, FULL = L.full;
  var fmt = function (t, o) { return t.replace(/\{(\w+)\}/g, function (m, k) { return o[k]; }); };
  var wa = function (t) { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(t); };
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  document.documentElement.classList.add('js');

  /* ---- mobile menu ---- */
  var mb = $('.menu-btn'), nav = $('#site-nav');
  if (mb && nav) {
    mb.addEventListener('click', function () {
      var o = nav.classList.toggle('open');
      mb.setAttribute('aria-expanded', o);
      mb.textContent = o ? '✕' : '☰';
    });
  }

  /* ---- deadline planner ---- */
  var pl = $('#planner');
  if (pl) {
    var inc = $('#p-inc'), fye = $('#p-fye'), list = $('#p-list'), days = $('#p-days'), remind = $('#p-remind');
    var render = function () {
      var today = new Date(); today.setHours(0, 0, 0, 0);
      var DAY = 864e5, Y = today.getFullYear();
      var incD = new Date(inc.value + 'T00:00:00'), valid = !isNaN(incD.getTime());
      var f = (+fye.value) - 1;
      var add = function (d, n) { return new Date(d.getTime() + n * DAY); };
      var out = [];
      var pick = function (title, sub, c) {
        var d = c.filter(function (x) { return x >= today; }).sort(function (a, b) { return a - b; })[0];
        if (d) out.push({ title: title, sub: sub, date: d });
      };
      if (valid) pick(L.t_ar, L.s_ar,
        [Y - 1, Y, Y + 1, Y + 2].filter(function (y) { return y > incD.getFullYear(); })
          .map(function (y) { return add(new Date(y, incD.getMonth(), incD.getDate()), 30); }));
      var fyes = [Y - 2, Y - 1, Y, Y + 1, Y + 2].map(function (y) { return new Date(y, f + 1, 0); })
        .filter(function (d) { return !valid || d > incD; });
      var eom = function (d, m) { return new Date(d.getFullYear(), d.getMonth() + m, 0); };
      pick(L.t_circ, L.s_circ, fyes.map(function (d) { return eom(d, 7); }));
      pick(L.t_lodge, L.s_lodge, fyes.map(function (d) { return add(eom(d, 7), 30); }));
      pick(L.t_c, L.s_c, fyes.map(function (d) { return eom(d, 8); }));
      pick(L.t_cp, L.s_cp, fyes.map(function (d) { return add(d, -29); }));
      out.sort(function (a, b) { return a.date - b.date; });
      out = out.slice(0, 4).map(function (o) {
        o.days = Math.round((o.date - today) / DAY);
        o.full = o.date.getDate() + ' ' + SH[o.date.getMonth()] + ' ' + o.date.getFullYear();
        return o;
      });
      list.innerHTML = '';
      out.forEach(function (o) {
        var li = document.createElement('li');
        li.innerHTML = '<span class="d"><b></b><span></span></span><span><strong></strong><small></small></span><span class="chip"></span>';
        $('b', li).textContent = SH[o.date.getMonth()];
        $('.d span', li).textContent = o.date.getDate();
        $('strong', li).textContent = o.title;
        $('small', li).textContent = o.sub;
        var c = $('.chip', li);
        c.textContent = o.days === 0 ? L.chip_today : o.days + ' ' + (o.days === 1 ? L.days : L.days_pl);
        if (o.days <= 60) c.className = 'chip urgent';
        list.appendChild(li);
      });
      var n = out[0];
      days.textContent = n ? (n.days === 0 ? L.today : n.days + ' ' + (n.days === 1 ? L.days : L.days_pl)) : L.none;
      remind.href = wa(fmt(L.remind, { inc: inc.value, fye: FULL[f] }) + '\n' +
        out.map(function (d) { return '• ' + d.title + ' – ' + d.full; }).join('\n'));
    };
    inc.addEventListener('change', render);
    fye.addEventListener('change', render);
    // default incorporation date: two years ago, so the demo always has upcoming dates
    var d0 = new Date(); d0.setFullYear(d0.getFullYear() - 2);
    inc.value = d0.toISOString().slice(0, 10);
    render();
  }

  /* ---- persona tabs ---- */
  var tabs = $$('[data-persona-tab]');
  if (tabs.length) {
    var panels = $$('[data-persona-panel]');
    var show = function (id) {
      tabs.forEach(function (t) { var on = t.getAttribute('data-persona-tab') === id; t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1; });
      panels.forEach(function (p) { p.hidden = p.getAttribute('data-persona-panel') !== id; });
    };
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { show(t.getAttribute('data-persona-tab')); });
      t.addEventListener('keydown', function (e) {
        var k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!k) return;
        var nx = tabs[(i + k + tabs.length) % tabs.length]; nx.focus(); nx.click(); e.preventDefault();
      });
    });
    $$('[data-quote-persona]').forEach(function (a) {
      a.addEventListener('click', function () {
        var form = $('#enquiry');
        if (!form) return;
        var needs = a.getAttribute('data-needs').split('|'), stage = a.getAttribute('data-stage');
        $$('input[name=need]', form).forEach(function (i) { i.checked = needs.indexOf(i.value) > -1; });
        $$('input[name=stage]', form).forEach(function (i) { i.checked = i.value === stage; });
        form.elements.msg.value = fmt(L.w_pkg, { plan: a.getAttribute('data-quote-persona') });
        form.dispatchEvent(new CustomEvent('reset-step'));
      });
    });
    show('run');
  }

  /* ---- health check quiz ---- */
  var qz = $('#quiz');
  if (qz) {
    var QUIZ = JSON.parse($('#quiz-data').textContent);
    var ans = [], qi = 0;
    var qs = $('#quiz-q'), qn = $('#quiz-n'), bar = $('#quiz-bar'), back = $('#quiz-back'),
        runEl = $('#quiz-run'), doneEl = $('#quiz-done'), static_ = $('#quiz-static');
    if (static_) static_.hidden = true;
    var paint = function () {
      var done = qi >= QUIZ.length;
      runEl.hidden = done; doneEl.hidden = !done;
      bar.style.width = (qi / QUIZ.length * 100) + '%';
      back.hidden = qi === 0 || done;
      if (!done) { qs.textContent = QUIZ[qi].q; qn.textContent = fmt(L.quiz_q, { n: qi + 1, t: QUIZ.length }); return; }
      var score = ans.filter(function (a) { return a === 'yes'; }).length;
      var gaps = QUIZ.filter(function (q, i) { return ans[i] && ans[i] !== 'yes'; }).map(function (q) { return q.fix; });
      var r = score === 5 ? [L.r_healthy, L.r_healthy_m] : score >= 3 ? [L.r_gaps, L.r_gaps_m] : [L.r_look, L.r_look_m];
      $('#quiz-score').textContent = score + '/5';
      var ring = $('#quiz-ring');
      ring.style.setProperty('--deg', (score / 5 * 360) + 'deg');
      ring.style.setProperty('--c', score === 5 ? '#9cc7a9' : score >= 3 ? '#e2b3b2' : '#e0876f');
      $('#quiz-title').textContent = r[0]; $('#quiz-msg').textContent = r[1];
      var g = $('#quiz-gaps'); g.hidden = !gaps.length;
      var ul = $('ul', g); ul.innerHTML = '';
      gaps.forEach(function (t) { var li = document.createElement('li'); li.textContent = t; ul.appendChild(li); });
      $('#quiz-wa').href = wa(fmt(L.quiz_wa, { s: score }) +
        (gaps.length ? L.quiz_help + gaps.map(function (x) { return '• ' + x; }).join('\n') : L.quiz_talk));
    };
    $$('[data-ans]', qz).forEach(function (b) {
      b.addEventListener('click', function () { ans = ans.slice(0, qi); ans.push(b.getAttribute('data-ans')); qi++; paint(); });
    });
    back.addEventListener('click', function () { qi = Math.max(0, qi - 1); paint(); });
    $('#quiz-reset').addEventListener('click', function () { qi = 0; ans = []; paint(); });
    paint();
  }

  /* ---- multi-step enquiry form ---- */
  var form = $('#enquiry');
  if (form) {
    var sets = $$('fieldset[data-step]', form), step = 0;
    var bars = $$('.pbars i', form), sn = $('.step-n', form), next = $('#f-next'), prev = $('#f-back'), err = $('.err', form);
    var checked = function (n) { return $$('input[name=' + n + ']:checked', form).map(function (i) { return i.value; }); };
    var valid = function () { return step === 0 ? checked('need').length > 0 : step === 1 ? checked('stage').length > 0 : true; };
    var paintF = function () {
      sets.forEach(function (s, i) { s.hidden = i !== step; });
      bars.forEach(function (b, i) { b.className = i <= step ? 'on' : ''; });
      sn.textContent = fmt(L.step, { n: step + 1 });
      prev.hidden = step === 0;
      next.textContent = step === 2 ? L.f_final : L.f_next;
      next.style.opacity = valid() ? 1 : .55;
      err.textContent = '';
    };
    form.addEventListener('change', function () { next.style.opacity = valid() ? 1 : .55; });
    form.addEventListener('reset-step', function () { step = 0; paintF(); });
    prev.addEventListener('click', function () { step = Math.max(0, step - 1); paintF(); });
    next.addEventListener('click', function () {
      if (!valid()) { err.textContent = step === 0 ? L.e_need : L.e_stage; return; }
      if (step < 2) { step++; paintF(); return; }
      form.requestSubmit ? form.requestSubmit() : form.submit();
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.elements.name.value.trim(), phone = form.elements.phone.value;
      if (!name || phone.replace(/\D/g, '').length < 9) { err.textContent = L.e_contact; return; }
      var needs = checked('need'), stage = checked('stage')[0] || '', co = form.elements.company.value.trim(), msg = form.elements.msg.value.trim();
      var sum = needs.length ? needs.join(', ').toLowerCase() : L.your_needs;
      var text = fmt(L.w_hi, { name: name }) + (co ? fmt(L.w_from, { co: co }) : '') + fmt(L.w_stage, { stage: stage, sum: sum }) + (msg ? ' ' + msg : '') + fmt(L.w_phone, { phone: phone });
      $('#thanks-name').textContent = name.split(' ')[0];
      $('#thanks-phone').textContent = phone;
      $('#thanks-need').textContent = sum;
      $('#thanks-wa').href = wa(text);
      $('#thanks-mail').href = 'mailto:corpsec@ccmsecretarial.com?subject=' + encodeURIComponent(fmt(L.mail_subj, { name: name })) + '&body=' + encodeURIComponent(text);
      form.hidden = true; $('#thanks').hidden = false;
      $('#thanks').scrollIntoView({ block: 'center' });
    });
    $('#f-new').addEventListener('click', function () {
      form.reset(); form.hidden = false; $('#thanks').hidden = true; step = 0; paintF();
    });
    paintF();
  }
})();
