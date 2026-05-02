// ============================================================
// MATDAN — Charts (charts.js) — using Chart.js
// ============================================================
const CHART_DEFAULTS = {
  color: '#FFFFFF',
  plugins: { legend: { labels: { color: '#FFFFFF', font: { family: 'Share Tech Mono' } } } }
};

async function initGenderChart() {
  const canvas = document.getElementById('gender-chart');
  if (!canvas) return;
  try {
    const res  = await fetch('/api/analytics/states');
    const data = await res.json();
    let totalMale = 0, totalFemale = 0;
    data.forEach(d => { totalMale += d.male_voters || 0; totalFemale += d.female_voters || 0; });
    new Chart(canvas, {
      type: 'doughnut',
      data: {
        labels: ['Male Voters', 'Female Voters'],
        datasets: [{
          data: [totalMale, totalFemale],
          backgroundColor: ['#FF9933', '#138808'],
          borderColor: ['#0A0A0A'],
          borderWidth: 3
        }]
      },
      options: {
        ...CHART_DEFAULTS,
        animation: { animateRotate: true, duration: 1500 },
        plugins: {
          ...CHART_DEFAULTS.plugins,
          tooltip: { callbacks: { label: ctx => ` ${ctx.label}: ${(ctx.parsed/1e6).toFixed(1)}M` } }
        }
      }
    });
  } catch (e) { console.error('Gender chart error', e); }
}

async function initStateChart() {
  const canvas = document.getElementById('state-chart');
  if (!canvas) return;
  try {
    const res  = await fetch('/api/analytics/states');
    const data = await res.json();
    const labels   = data.map(d => d.state);
    const turnouts = data.map(d => d.turnout || 0);
    new Chart(canvas, {
      type: 'bar',
      data: {
        labels,
        datasets: [{
          label: 'Voter Turnout %',
          data: turnouts,
          backgroundColor: labels.map((_, i) => i % 2 === 0 ? 'rgba(255,153,51,0.7)' : 'rgba(19,136,8,0.7)'),
          borderColor: '#FFD700',
          borderWidth: 1
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        animation: { duration: 1500 },
        plugins: {
          ...CHART_DEFAULTS.plugins,
          tooltip: { callbacks: { label: ctx => ` Turnout: ${ctx.parsed.x.toFixed(1)}%` } }
        },
        scales: {
          x: { ticks: { color: '#FFFFFF', font: { family: 'Share Tech Mono' } }, grid: { color: 'rgba(255,255,255,0.05)' }, max: 100 },
          y: { ticks: { color: '#FFFFFF', font: { family: 'Rajdhani', size: 11 } }, grid: { display: false } }
        }
      }
    });
  } catch (e) { console.error('State chart error', e); }
}

// Scroll-triggered chart draw
function observeCharts() {
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        if (en.target.id === 'gender-chart') initGenderChart();
        if (en.target.id === 'state-chart')  initStateChart();
        io.unobserve(en.target);
      }
    });
  }, { threshold: 0.3 });
  ['gender-chart','state-chart'].forEach(id => {
    const el = document.getElementById(id);
    if (el) io.observe(el);
  });
}

document.addEventListener('DOMContentLoaded', observeCharts);
