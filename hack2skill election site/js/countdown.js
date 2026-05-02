// ============================================================
// MATDAN — Countdown Timer (countdown.js)
// ============================================================
function updateCountdown() {
  const target = new Date('2029-05-01T00:00:00');
  const now = new Date();
  const diff = target - now;
  if (diff <= 0) {
    ['cd-days','cd-hours','cd-mins','cd-secs'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.textContent = '00';
    });
    return;
  }
  const days    = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours   = Math.floor((diff % (1000*60*60*24)) / (1000*60*60));
  const minutes = Math.floor((diff % (1000*60*60)) / (1000*60));
  const seconds = Math.floor((diff % (1000*60)) / 1000);

  const pad = n => String(n).padStart(2, '0');

  const setEl = (id, val) => { const el = document.getElementById(id); if (el) el.textContent = pad(val); };
  setEl('cd-days',  days);
  setEl('cd-hours', hours);
  setEl('cd-mins',  minutes);
  setEl('cd-secs',  seconds);
}
updateCountdown();
setInterval(updateCountdown, 1000);
