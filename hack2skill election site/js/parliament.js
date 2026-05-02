// ============================================================
// MATDAN — Parliament (parliament.js)
// ============================================================
let allMembers = [], allParties = [];

async function loadParliamentData() {
  const [memRes, parRes] = await Promise.all([
    fetch('/api/parliament/members'),
    fetch('/api/parliament/parties')
  ]);
  allMembers = await memRes.json();
  allParties = await parRes.json();
  renderMembers(allMembers);
  renderParties(allParties);
}

function renderMembers(members) {
  const grid = document.getElementById('members-grid');
  if (!grid) return;
  grid.innerHTML = members.length === 0
    ? '<p class="text-muted text-center">No members found.</p>'
    : members.map(m => `
      <div class="hud-card reveal card-reveal-anim" style="animation-delay:${Math.random()*0.3}s">
        <div style="display:flex;gap:1rem;align-items:center;margin-bottom:1rem;">
          <div style="width:56px;height:56px;border-radius:50%;background:rgba(255,153,51,0.1);border:2px solid #FF9933;display:flex;align-items:center;justify-content:center;font-size:1.5rem;">👤</div>
          <div>
            <div style="font-weight:700;font-size:1.1rem;">${m.name}</div>
            <div class="text-muted" style="font-size:0.85rem;">${m.party || '—'}</div>
          </div>
        </div>
        <div class="badge-tag">${m.constituency || '—'}</div>
      </div>`).join('');
  document.querySelectorAll('.reveal').forEach(el => {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); } });
    }, { threshold: 0.1 });
    io.observe(el);
  });
}

function renderParties(parties) {
  const grid = document.getElementById('parties-grid');
  if (!grid) return;
  grid.innerHTML = parties.map(p => `
    <div class="hud-card green-variant reveal">
      <div style="font-size:1.5rem;margin-bottom:0.5rem;">🏛️</div>
      <div style="font-weight:700;font-size:1.1rem;">${p.name}</div>
      <div class="badge-tag cyan" style="margin:0.5rem 0;">${p.abbreviation || ''}</div>
      <div class="text-muted" style="font-size:0.85rem;">Founded: ${p.founded_year || '—'}</div>
    </div>`).join('');
}

function filterMembers() {
  const q = document.getElementById('member-search')?.value.toLowerCase() || '';
  const filtered = allMembers.filter(m =>
    (m.name||'').toLowerCase().includes(q) ||
    (m.party||'').toLowerCase().includes(q) ||
    (m.constituency||'').toLowerCase().includes(q)
  );
  renderMembers(filtered);
}

document.addEventListener('DOMContentLoaded', () => {
  loadParliamentData();
  const searchInput = document.getElementById('member-search');
  if (searchInput) searchInput.addEventListener('input', filterMembers);
});
