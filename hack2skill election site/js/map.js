// ============================================================
// MATDAN — Map (map.js) — Leaflet.js
// ============================================================
let map;

function initMap(lat = 20.5937, lng = 78.9629, zoom = 5) {
  if (!document.getElementById('map')) return;
  map = L.map('map', { zoomControl: true }).setView([lat, lng], zoom);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 18
  }).addTo(map);
  map.getContainer().style.background = '#0A0A0A';
}

const saffronIcon = L.divIcon({
  className: '',
  html: `<div style="width:14px;height:14px;background:#FF9933;border:2px solid #FFD700;border-radius:50%;box-shadow:0 0 8px #FF9933;"></div>`,
  iconSize: [14, 14],
  iconAnchor: [7, 7]
});

function addBoothMarkers(booths) {
  if (!map) return;
  booths.forEach(b => {
    if (!b.latitude || !b.longitude) return;
    L.marker([b.latitude, b.longitude], { icon: saffronIcon })
      .addTo(map)
      .bindPopup(`
        <div style="font-family:Rajdhani,sans-serif;color:#0A0A0A;min-width:200px;">
          <b style="color:#FF9933;">${b.booth_number} — ${b.name}</b><br>
          <small>${b.address || ''}</small><hr style="margin:4px 0;">
          <b>BLO:</b> ${b.blo_name || 'N/A'}<br>
          ♿ ${b.facilities?.wheelchair ? '✅' : '❌'} &nbsp;
          💧 ${b.facilities?.water ? '✅' : '❌'} &nbsp;
          🌳 ${b.facilities?.shade ? '✅' : '❌'}
        </div>`);
  });
}

async function findBooths() {
  const pincodeEl = document.getElementById('pincode-input');
  const pincode   = pincodeEl?.value.trim();
  const tbody     = document.getElementById('booth-list-body');

  const res  = await fetch('/api/booth/find', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({ pincode })
  });
  const booths = await res.json();

  if (!booths.length) { window.showToast && showToast('No booths found.', 'error'); return; }
  addBoothMarkers(booths);
  if (booths[0].latitude) map.setView([booths[0].latitude, booths[0].longitude], 13);
  if (tbody) {
    tbody.innerHTML = booths.map(b => `
      <tr>
        <td>${b.booth_number}</td>
        <td>${b.name}</td>
        <td>${b.address || '—'}</td>
        <td>${b.blo_name || '—'}</td>
        <td>
          ${b.facilities?.wheelchair ? '♿' : ''} 
          ${b.facilities?.water ? '💧' : ''} 
          ${b.facilities?.shade ? '🌳' : ''}
        </td>
      </tr>`).join('');
  }
}

function useMyLocation() {
  if (!navigator.geolocation) { alert('Geolocation not supported'); return; }
  navigator.geolocation.getCurrentPosition(pos => {
    const { latitude: lat, longitude: lng } = pos.coords;
    map.setView([lat, lng], 14);
    L.marker([lat, lng]).addTo(map).bindPopup('📍 Your Location').openPopup();
  }, () => alert('Could not get location'));
}

document.addEventListener('DOMContentLoaded', () => {
  initMap();
  const searchBtn = document.getElementById('booth-search-btn');
  const locBtn    = document.getElementById('booth-location-btn');
  if (searchBtn) searchBtn.addEventListener('click', findBooths);
  if (locBtn)    locBtn.addEventListener('click', useMyLocation);
});
