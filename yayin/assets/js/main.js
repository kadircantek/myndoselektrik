/* Bodrum Elektrik – interactions */
(function () {
  "use strict";
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = matchMedia("(pointer: fine)").matches;

  /* Preloader */
  window.addEventListener("load", () => {
    setTimeout(() => { $("#loader")?.classList.add("done"); document.body.classList.add("bulb-on"); }, 350);
  });
  setTimeout(() => $("#loader")?.classList.add("done"), 2500);

  /* Header scroll + mobile menu */
  const header = $(".header");
  const onScroll = () => header.classList.toggle("scrolled", scrollY > 30);
  addEventListener("scroll", onScroll, { passive: true }); onScroll();
  $(".burger")?.addEventListener("click", () => {
    const open = document.body.classList.toggle("nav-open");
    $(".burger").setAttribute("aria-expanded", open);
  });
  $$(".menu a").forEach(a => a.addEventListener("click", () => document.body.classList.remove("nav-open")));

  /* Year */
  $$("[data-year]").forEach(e => (e.textContent = new Date().getFullYear()));

  /* Spark particles canvas */
  const cv = $("#sparks");
  if (cv && !reduce) {
    const ctx = cv.getContext("2d");
    let w, h, dpr, parts = [];
    const N = innerWidth < 700 ? 34 : 80;
    const mouse = { x: -999, y: -999 };
    const resize = () => {
      dpr = Math.min(devicePixelRatio || 1, 2);
      w = cv.width = innerWidth * dpr; h = cv.height = innerHeight * dpr;
      cv.style.width = innerWidth + "px"; cv.style.height = innerHeight + "px";
    };
    const mk = (init) => ({
      x: Math.random() * w, y: init ? Math.random() * h : h + 20,
      r: (Math.random() * 1.8 + .6) * dpr, vy: -(Math.random() * .35 + .12) * dpr,
      vx: (Math.random() - .5) * .2 * dpr, a: Math.random() * .6 + .25,
      hue: Math.random() < .82 ? 38 + Math.random() * 14 : 188, t: Math.random() * 6.28
    });
    resize(); for (let i = 0; i < N; i++) parts.push(mk(true));
    addEventListener("resize", resize);
    addEventListener("pointermove", e => { mouse.x = e.clientX * dpr; mouse.y = e.clientY * dpr; }, { passive: true });
    let visible = true;
    document.addEventListener("visibilitychange", () => (visible = !document.hidden));
    (function loop() {
      if (visible) {
        ctx.clearRect(0, 0, w, h);
        for (const p of parts) {
          p.t += .02; p.x += p.vx + Math.sin(p.t) * .15 * dpr; p.y += p.vy;
          const dx = p.x - mouse.x, dy = p.y - mouse.y, d = Math.hypot(dx, dy);
          if (d < 120 * dpr) { p.x += dx / d * 1.2; p.y += dy / d * 1.2; }
          if (p.y < -20) Object.assign(p, mk(false));
          const fl = p.a * (.75 + Math.sin(p.t * 3) * .25);
          const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 5);
          g.addColorStop(0, `hsla(${p.hue},100%,75%,${fl})`); g.addColorStop(1, `hsla(${p.hue},100%,60%,0)`);
          ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p.x, p.y, p.r * 5, 0, 6.28); ctx.fill();
        }
      }
      requestAnimationFrame(loop);
    })();
  }

  /* Bulb pull-switch */
  const swing = $(".bulb-swing");
  if (swing) {
    const toggle = () => {
      document.body.classList.toggle("lights-off");
      document.body.classList.remove("bulb-on"); void swing.offsetWidth;
      if (!document.body.classList.contains("lights-off")) document.body.classList.add("bulb-on");
      if (navigator.vibrate) navigator.vibrate(15);
    };
    swing.addEventListener("click", toggle);
    swing.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); } });
    /* subtle mouse parallax on bulb */
    if (finePointer && !reduce) {
      const stage = $(".bulb-stage");
      addEventListener("pointermove", e => {
        const x = (e.clientX / innerWidth - .5) * 14, y = (e.clientY / innerHeight - .5) * 10;
        stage.style.transform = `rotateY(${x}deg) rotateX(${-y}deg)`;
      }, { passive: true });
    }
  }

  /* Hero bg parallax */
  const heroImg = $(".hero-bg img");
  if (heroImg && !reduce) addEventListener("scroll", () => {
    if (scrollY < innerHeight) heroImg.style.transform = `scale(1.08) translateY(${scrollY * .25}px)`;
  }, { passive: true });

  /* 3D tilt cards */
  if (finePointer && !reduce) $$(".tilt").forEach(el => {
    el.addEventListener("pointermove", e => {
      const r = el.getBoundingClientRect(), px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      el.style.transform = `perspective(900px) rotateY(${(px - .5) * 14}deg) rotateX(${(.5 - py) * 14}deg) translateZ(0)`;
      el.style.setProperty("--mx", px * 100 + "%"); el.style.setProperty("--my", py * 100 + "%");
    });
    el.addEventListener("pointerleave", () => (el.style.transform = ""));
  });

  /* Reveal on scroll + counters */
  const io = new IntersectionObserver(es => es.forEach(en => {
    if (!en.isIntersecting) return;
    en.target.classList.add("in");
    $$("[data-count]", en.target).forEach(countUp);
    io.unobserve(en.target);
  }), { threshold: .12, rootMargin: "0px 0px -40px 0px" });
  $$(".reveal").forEach(el => io.observe(el));
  function countUp(el) {
    if (el.dataset.done) return; el.dataset.done = 1;
    const end = +el.dataset.count, suf = el.dataset.suffix || "", t0 = performance.now(), dur = 1800;
    const step = t => { const k = Math.min((t - t0) / dur, 1), v = Math.round(end * (1 - Math.pow(1 - k, 3))); el.textContent = v + suf; if (k < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  }

  /* Smart home demo */
  const room = $(".room");
  if (room) {
    const img = $("img", room), shade = $(".shade", room);
    const update = () => {
      const on = $$(".tgl").filter(b => b.getAttribute("aria-pressed") === "true");
      $$(".tgl").forEach(b => room.classList.toggle("on-" + b.dataset.zone, b.getAttribute("aria-pressed") === "true"));
      const curtains = $('.tgl[data-zone="curtain"]')?.getAttribute("aria-pressed") === "true";
      const lit = on.filter(b => b.dataset.zone !== "curtain").length;
      shade.style.opacity = Math.max(0, .78 - lit * .2) + (curtains ? .1 : 0);
      img.style.filter = `saturate(${.6 + lit * .15}) brightness(${.75 + lit * .1})`;
    };
    $$(".tgl").forEach(b => b.addEventListener("click", () => { b.setAttribute("aria-pressed", b.getAttribute("aria-pressed") !== "true"); update(); }));
    const scenes = { movie: ["led", "curtain"], dinner: ["living", "garden"], all: ["living", "led", "garden", "pool"], off: [] };
    $$(".scenes button").forEach(s => s.addEventListener("click", () => {
      const z = scenes[s.dataset.scene];
      $$(".tgl").forEach(b => b.setAttribute("aria-pressed", z.includes(b.dataset.zone)));
      update();
    }));
    update();
  }

  /* Lightbox */
  const lb = $(".lightbox");
  if (lb) {
    const lbImg = $("img", lb), lbCap = $("p", lb);
    $$(".g-item").forEach(f => f.addEventListener("click", () => {
      const i = $("img", f); lbImg.src = i.src; lbImg.alt = i.alt; lbCap.textContent = $("figcaption", f)?.innerText.replace(/\n/g, " – ") || "";
      lb.classList.add("open");
    }));
    const close = () => lb.classList.remove("open");
    lb.addEventListener("click", e => { if (e.target !== lbImg) close(); });
    addEventListener("keydown", e => e.key === "Escape" && close());
  }

  /* Contact form → WhatsApp */
  const form = $("#contactForm");
  form?.addEventListener("submit", e => {
    e.preventDefault();
    const d = new FormData(form), L = form.dataset;
    const msg = `${L.hello}\n\n${L.lname}: ${d.get("name")}\n${L.lphone}: ${d.get("phone")}\n${L.lservice}: ${d.get("service")}\n${L.lmsg}: ${d.get("message")}`;
    window.open(`https://wa.me/${form.dataset.wa}?text=${encodeURIComponent(msg)}`, "_blank", "noopener");
  });

  /* Lazy map */
  const map = $(".map[data-src]");
  if (map) new IntersectionObserver((es, o) => es.forEach(en => {
    if (en.isIntersecting) { map.innerHTML = `<iframe src="${map.dataset.src}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="${map.dataset.title}"></iframe>`; o.disconnect(); }
  }), { rootMargin: "300px" }).observe(map);

  /* Automatic language: redirect first-time visitors by browser language (bots excluded),
     remember manual choice from switcher. */
  const cur = document.documentElement.lang.slice(0, 2);
  $$(".lang a").forEach(a => a.addEventListener("click", () => { try { localStorage.setItem("lang", a.hreflang); } catch (_) {} }));
  const isBot = /bot|crawl|spider|slurp|lighthouse|google|bing|yandex|baidu|duckduck|facebookexternalhit|preview/i.test(navigator.userAgent);
  let saved = null; try { saved = localStorage.getItem("lang"); } catch (_) {}
  const pref = (navigator.languages && navigator.languages[0] || navigator.language || "tr").slice(0, 2).toLowerCase();
  const target = ["tr", "en", "ru"].includes(pref) ? pref : (["uk", "be", "kk"].includes(pref) ? "ru" : "en");
  const link = l => $(`.lang a[hreflang="${l}"]`);
  if (!isBot && !saved && target !== cur && link(target)) {
    try { localStorage.setItem("lang", target); } catch (_) {}
    location.replace(link(target).href + location.hash);
  }
})();
