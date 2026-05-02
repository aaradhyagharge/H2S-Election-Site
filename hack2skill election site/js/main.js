// ============================================================
// MATDAN — Main JS (main.js)
// ============================================================

// ---- Reveal on scroll ----
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(en => {
    if (en.isIntersecting) {
      en.target.classList.add('visible');
      revealObserver.unobserve(en.target);
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ---- Navbar hamburger ----
const hamburger = document.getElementById('hamburger-btn');
const navLinks  = document.getElementById('navbar-links');
if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
}

// ---- Active nav link ----
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.navbar-links a').forEach(a => {
  const href = a.getAttribute('href');
  if (href === currentPage || (currentPage === '' && href === 'index.html')) a.classList.add('active');
});

// ---- Accordion ----
document.querySelectorAll('.accordion-header').forEach(header => {
  header.addEventListener('click', () => {
    const body = header.nextElementSibling;
    const arrow = header.querySelector('.acc-arrow');
    body.classList.toggle('open');
    if (arrow) arrow.textContent = body.classList.contains('open') ? '▲' : '▼';
  });
});

// ---- Support ticket form ----
const supportForm = document.getElementById('support-form');
if (supportForm) {
  supportForm.addEventListener('submit', async e => {
    e.preventDefault();
    const fd = new FormData(supportForm);
    const data = Object.fromEntries(fd.entries());
    try {
      const res = await fetch('/api/support/ticket', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(data)
      });
      const json = await res.json();
      showToast(json.message || 'Ticket submitted!');
      supportForm.reset();
    } catch { showToast('Error submitting. Please try again.'); }
  });
}

// ---- CRT flicker on load ----
document.body.classList.add('crt-flicker');
setTimeout(() => document.body.classList.remove('crt-flicker'), 1000);

// ---- Toast utility ----
function showToast(msg, type = 'info') {
  const t = document.createElement('div');
  t.className = 'toast';
  if (type === 'error') t.style.borderColor = '#8B0000';
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3200);
}
window.showToast = showToast;

// ---- Stat counter animation ----
function animateCounter(el, target, duration = 1500) {
  const start = performance.now();
  const update = now => {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const val = Math.floor(progress * target);
    el.textContent = val.toLocaleString('en-IN');
    if (progress < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}
const statsObserver = new IntersectionObserver(entries => {
  entries.forEach(en => {
    if (en.isIntersecting) {
      const target = parseInt(en.target.dataset.target, 10);
      if (!isNaN(target)) animateCounter(en.target, target);
      statsObserver.unobserve(en.target);
    }
  });
}, { threshold: 0.5 });
document.querySelectorAll('.stat-number').forEach(el => statsObserver.observe(el));

// ---- Typewriter headlines ----
document.querySelectorAll('.typewriter').forEach(el => {
  const text = el.textContent;
  el.textContent = '';
  el.style.whiteSpace = 'nowrap';
  let i = 0;
  const interval = setInterval(() => {
    if (i < text.length) { el.textContent += text[i++]; } else clearInterval(interval);
  }, 60);
});

// ---- Page transition ----
document.querySelectorAll('a[data-transition]').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const href = link.href;
    document.body.classList.add('page-transition-out');
    setTimeout(() => { window.location.href = href; }, 400);
  });
});
