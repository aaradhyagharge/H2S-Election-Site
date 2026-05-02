// ============================================================
// MATDAN — Translator (translate.js)
// ============================================================
let currentLang = localStorage.getItem('matdan_lang') || 'en';
let translations = {};

async function loadTranslations(lang) {
  try {
    const r = await fetch(`/translations/${lang}.json`);
    translations = await r.json();
  } catch (e) {
    console.error('Translation load failed', e);
  }
}

function applyTranslations() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (translations[key]) el.textContent = translations[key];
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (translations[key]) el.placeholder = translations[key];
  });
  document.documentElement.lang = currentLang;
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === currentLang);
  });
  // Apply Devanagari font for hi/mr
  document.body.style.fontFamily = (currentLang === 'en')
    ? "'Rajdhani', sans-serif"
    : "'Noto Sans Devanagari', 'Rajdhani', sans-serif";
}

async function switchLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('matdan_lang', lang);
  await loadTranslations(lang);
  applyTranslations();
}

// Init
(async () => {
  await loadTranslations(currentLang);
  applyTranslations();
})();

// Expose globally
window.switchLanguage = switchLanguage;
window.getCurrentLang = () => currentLang;
window.getTranslations = () => translations;
