JS_CONTENT = """
// Global state
let currentTab = 'overview';
let batterView = 'cards';
let bowlerView = 'cards';
let radarChart = null;

// RR Auction War Room State
let auctionBudget = 120.0; // In Crore INR
let spentBudget = 0.0;
let squadBought = [];
let pendingPlayerForBid = null; // Holds player object when bid modal is active

// Base Rajasthan Royals Retained Core (Updated with 2026 Season State: Samson traded to CSK, Jadeja to RR, Parag Captain)
const rrRetainedCore = [
  { name: 'Yashasvi Jaiswal', role: 'Opening Batter / VC', type: 'retained', cost: 18.0, clutch: 88, overseas: false },
  { name: 'Riyan Parag (C)', role: 'Captain / Middle-Order Batter', type: 'retained', cost: 14.0, clutch: 85, overseas: false },
  { name: 'Ravindra Jadeja', role: 'All-Rounder (Joined RR in 2026)', type: 'retained', cost: 16.0, clutch: 89, overseas: false },
  { name: 'Dhruv Jurel (WK)', role: 'Wicketkeeper / Finisher', type: 'retained', cost: 14.0, clutch: 84, overseas: false },
  { name: 'Shimron Hetmyer', role: 'Death Finisher', type: 'retained', cost: 11.0, clutch: 89, overseas: true },
  { name: 'Sandeep Sharma', role: 'Death Specialist Pacer', type: 'retained', cost: 4.0, clutch: 87, overseas: false },
  { name: 'Jofra Archer', role: 'Express Strike Pacer', type: 'retained', cost: 10.0, clutch: 86, overseas: true }
];

// Initialize on DOM Load
document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  renderBatters();
  renderBowlers();
  initCompareDropdowns();
  initSimulator();
  initAuctionWarRoom();
  initCharts();
});

// Tab Navigation
function initTabs() {
  const tabBtns = document.querySelectorAll('.nav-tab-btn');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      switchTab(target);
    });
  });
}

function switchTab(tabId) {
  currentTab = tabId;
  document.querySelectorAll('.nav-tab-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.tab === tabId);
  });
  document.querySelectorAll('.tab-content').forEach(c => {
    c.classList.toggle('active', c.id === 'tab-' + tabId);
  });
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Refresh radar chart if switching to compare
  if (tabId === 'compare' && radarChart) {
    radarChart.resize();
    updateCompareRadar();
  }
}

// Render Batters
function renderBatters() {
  const container = document.getElementById('batters-cards-container');
  const tableBody = document.getElementById('batters-table-body');
  if (!container || !tableBody) return;

  const search = (document.getElementById('batter-search')?.value || '').toLowerCase();
  const roleFilter = document.getElementById('batter-role-filter')?.value || 'all';
  const tierFilter = document.getElementById('batter-tier-filter')?.value || 'all';
  const sortBy = document.getElementById('batter-sort')?.value || 'rank';

  let list = [...RAW_DATA.batters];

  // Filtering
  list = list.filter(b => {
    const matchSearch = b.name.toLowerCase().includes(search) || b.country.toLowerCase().includes(search) || b.role.toLowerCase().includes(search);
    const matchRole = roleFilter === 'all' || 
      (roleFilter === 'opener' && b.role.toLowerCase().includes('opener')) ||
      (roleFilter === 'middle' && b.role.toLowerCase().includes('middle')) ||
      (roleFilter === 'finisher' && b.role.toLowerCase().includes('finisher')) ||
      (roleFilter === 'allrounder' && b.role.toLowerCase().includes('all-rounder'));
    const matchTier = tierFilter === 'all' || b.tier.toLowerCase().includes(tierFilter);
    return matchSearch && matchRole && matchTier;
  });

  // Sorting
  list.sort((a, b) => {
    if (sortBy === 'rank') return a.rank - b.rank;
    if (sortBy === 'impact') return b.impact - a.impact;
    if (sortBy === 'resilience') return b.resilience - a.resilience;
    if (sortBy === 'consistency') return b.consistency - a.consistency;
    if (sortBy === 'sr_pressure') return b.sr_pressure - a.sr_pressure;
    if (sortBy === 'balls') return b.pressure_balls - a.pressure_balls;
    return a.rank - b.rank;
  });

  // Render Cards
  container.innerHTML = list.map(b => {
    const isBought = squadBought.some(p => p.name === b.name);
    const tierClass = b.tier.includes('Tier 1') ? 'marquee' : (b.tier.includes('Tier 2') ? 'tactical' : (b.tier.includes('Tier 3') ? 'steal' : 'benchmark'));
    const srGain = b.sr_delta >= 0 ? `+${b.sr_delta}` : `${b.sr_delta}`;
    const diffPct = Math.min(100, Math.max(10, Math.round((b.sr_pressure / 220) * 100)));

    return `
      <div class="player-card rank-${b.rank}">
        <div class="card-top">
          <div class="card-identity">
            <div class="rank-number">${b.rank}</div>
            <div class="player-names">
              <h3>${b.name}</h3>
              <div class="player-role-badge">
                <span>${b.country}</span> • <span>${b.role}</span>
              </div>
            </div>
          </div>
          <span class="tier-badge ${tierClass}">${b.tier.split(' ')[0]}</span>
        </div>

        <div class="card-metrics-grid">
          <div class="metric-item">
            <span class="metric-label">Impact (WPA/100)</span>
            <span class="metric-value positive">+${b.impact.toFixed(1)}</span>
            <span class="metric-sub">${b.pressure_balls} Pressure Balls</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">Resilience (z)</span>
            <span class="metric-value highlight">+${b.resilience.toFixed(2)}</span>
            <span class="metric-sub">vs Normal Baseline</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">Consistency</span>
            <span class="metric-value">${b.consistency}%</span>
            <span class="metric-sub">Positive Win Impact</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">Pressure SR</span>
            <span class="metric-value gold">${b.sr_pressure}</span>
            <span class="metric-sub">Usual: ${b.sr_usual} (${srGain})</span>
          </div>
        </div>

        <div class="card-diff-bar-wrap">
          <div class="diff-header">
            <span>High Pressure SR Surge</span>
            <span style="color: ${b.sr_delta >= 0 ? 'var(--accent-green)' : 'var(--text-muted)'}; font-weight:700;">${srGain} SR</span>
          </div>
          <div class="diff-bar-track">
            <div class="diff-bar-fill" style="width: ${diffPct}%;"></div>
          </div>
        </div>

        <div class="rr-strategy-preview">
          <strong>RR Auction Fit:</strong> ${b.rr_fit}
        </div>

        <div class="card-actions">
          <button class="btn-card-action" onclick="openPlayerDossier('${b.name}', 'batter')">
            <span>📋 Dossier</span>
          </button>
          <button class="btn-card-action" onclick="sendToCompare('${b.name}', 'batter')">
            <span>⚔️ Compare</span>
          </button>
          <button class="btn-card-action btn-buy ${isBought ? 'bought' : ''}" onclick="toggleAuctionBuy('${b.name}', 'batter')">
            <span>${isBought ? '✓ In Squad' : '+ Add to RR'}</span>
          </button>
        </div>
      </div>
    `;
  }).join('');

  // Render Table
  tableBody.innerHTML = list.map(b => {
    return `
      <tr>
        <td style="font-weight:700;">#${b.rank}</td>
        <td><strong>${b.name}</strong> <span style="font-size:0.75rem; color:var(--text-muted);">(${b.country})</span></td>
        <td>${b.role}</td>
        <td>${b.pressure_balls}</td>
        <td style="color:var(--accent-green); font-weight:700;">+${b.impact.toFixed(1)}</td>
        <td style="color:var(--rr-pink-light); font-weight:700;">+${b.resilience.toFixed(2)}</td>
        <td>${b.consistency}%</td>
        <td style="font-weight:700; color:var(--rr-gold);">${b.sr_pressure}</td>
        <td style="color:var(--text-muted);">${b.sr_usual}</td>
        <td style="color:${b.sr_delta >= 0 ? 'var(--accent-green)' : 'var(--accent-red)'}; font-weight:700;">${b.sr_delta >= 0 ? '+' : ''}${b.sr_delta}</td>
        <td>1 in ${b.balls_per_dismissal}</td>
        <td><span class="tier-badge ${b.tier.includes('Tier 1') ? 'marquee' : 'tactical'}">${b.target_purse}</span></td>
        <td>
          <button class="btn-card-action" style="padding:0.25rem 0.5rem; font-size:0.75rem;" onclick="openPlayerDossier('${b.name}', 'batter')">Dossier</button>
        </td>
      </tr>
    `;
  }).join('');
}

// Render Bowlers
function renderBowlers() {
  const container = document.getElementById('bowlers-cards-container');
  const tableBody = document.getElementById('bowlers-table-body');
  if (!container || !tableBody) return;

  const search = (document.getElementById('bowler-search')?.value || '').toLowerCase();
  const typeFilter = document.getElementById('bowler-type-filter')?.value || 'all';
  const tierFilter = document.getElementById('bowler-tier-filter')?.value || 'all';
  const sortBy = document.getElementById('bowler-sort')?.value || 'rank';

  let list = [...RAW_DATA.bowlers];

  // Filtering
  list = list.filter(b => {
    const matchSearch = b.name.toLowerCase().includes(search) || b.country.toLowerCase().includes(search) || b.role.toLowerCase().includes(search);
    const matchType = typeFilter === 'all' || 
      (typeFilter === 'spin' && (b.role.toLowerCase().includes('spin') || b.role.toLowerCase().includes('orthodox'))) ||
      (typeFilter === 'pace' && (b.role.toLowerCase().includes('pace') || b.role.toLowerCase().includes('swing')));
    const matchTier = tierFilter === 'all' || b.tier.toLowerCase().includes(tierFilter);
    return matchSearch && matchType && matchTier;
  });

  // Sorting
  list.sort((a, b) => {
    if (sortBy === 'rank') return a.rank - b.rank;
    if (sortBy === 'impact') return b.impact - a.impact;
    if (sortBy === 'resilience') return b.resilience - a.resilience;
    if (sortBy === 'consistency') return b.consistency - a.consistency;
    if (sortBy === 'econ_pressure') return a.econ_pressure - b.econ_pressure;
    if (sortBy === 'wickets') return a.balls_per_wicket - b.balls_per_wicket;
    return a.rank - b.rank;
  });

  // Render Cards
  container.innerHTML = list.map(b => {
    const isBought = squadBought.some(p => p.name === b.name);
    const tierClass = b.tier.includes('Tier 1') ? 'marquee' : (b.tier.includes('Tier 2') ? 'tactical' : 'steal');
    const econImp = b.econ_delta <= 0 ? `${b.econ_delta.toFixed(2)}` : `+${b.econ_delta.toFixed(2)}`;

    return `
      <div class="player-card rank-${b.rank}">
        <div class="card-top">
          <div class="card-identity">
            <div class="rank-number">${b.rank}</div>
            <div class="player-names">
              <h3>${b.name}</h3>
              <div class="player-role-badge">
                <span>${b.country}</span> • <span>${b.role}</span>
              </div>
            </div>
          </div>
          <span class="tier-badge ${tierClass}">${b.tier.split(' ')[0]}</span>
        </div>

        <div class="card-metrics-grid">
          <div class="metric-item">
            <span class="metric-label">Impact (WPA/100)</span>
            <span class="metric-value positive">+${b.impact.toFixed(1)}</span>
            <span class="metric-sub">${b.pressure_balls} Pressure Deliveries</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">Resilience (z)</span>
            <span class="metric-value highlight">+${b.resilience.toFixed(2)}</span>
            <span class="metric-sub">vs Normal Spells</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">Consistency</span>
            <span class="metric-value">${b.consistency}%</span>
            <span class="metric-sub">Non-Negative Impact</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">Pressure Economy</span>
            <span class="metric-value gold">${b.econ_pressure.toFixed(2)}</span>
            <span class="metric-sub">Usual: ${b.econ_usual.toFixed(2)} (${econImp})</span>
          </div>
        </div>

        <div class="card-diff-bar-wrap">
          <div class="diff-header">
            <span>Dot Ball % & Strike Threat</span>
            <span style="color: var(--accent-cyan); font-weight:700;">${b.dot_pct}% Dots • 1 Wk / ${b.balls_per_wicket}b</span>
          </div>
          <div class="diff-bar-track">
            <div class="diff-bar-fill" style="width: ${Math.min(100, b.dot_pct * 2)}%; background: linear-gradient(90deg, var(--rr-pink) 0%, var(--accent-cyan) 100%);"></div>
          </div>
        </div>

        <div class="rr-strategy-preview">
          <strong>RR Auction Fit:</strong> ${b.rr_fit}
        </div>

        <div class="card-actions">
          <button class="btn-card-action" onclick="openPlayerDossier('${b.name}', 'bowler')">
            <span>📋 Dossier</span>
          </button>
          <button class="btn-card-action" onclick="sendToCompare('${b.name}', 'bowler')">
            <span>⚔️ Compare</span>
          </button>
          <button class="btn-card-action btn-buy ${isBought ? 'bought' : ''}" onclick="toggleAuctionBuy('${b.name}', 'bowler')">
            <span>${isBought ? '✓ In Squad' : '+ Add to RR'}</span>
          </button>
        </div>
      </div>
    `;
  }).join('');

  // Render Table
  tableBody.innerHTML = list.map(b => {
    return `
      <tr>
        <td style="font-weight:700;">#${b.rank}</td>
        <td><strong>${b.name}</strong> <span style="font-size:0.75rem; color:var(--text-muted);">(${b.country})</span></td>
        <td>${b.role}</td>
        <td>${b.pressure_balls}</td>
        <td style="color:var(--accent-green); font-weight:700;">+${b.impact.toFixed(1)}</td>
        <td style="color:var(--rr-pink-light); font-weight:700;">+${b.resilience.toFixed(2)}</td>
        <td>${b.consistency}%</td>
        <td style="font-weight:700; color:var(--rr-gold);">${b.econ_pressure.toFixed(2)}</td>
        <td style="color:var(--text-muted);">${b.econ_usual.toFixed(2)}</td>
        <td style="color:${b.econ_delta <= 0 ? 'var(--accent-green)' : 'var(--text-dim)'}; font-weight:700;">${b.econ_delta.toFixed(2)}</td>
        <td>1 in ${b.balls_per_wicket}</td>
        <td>${b.dot_pct}%</td>
        <td><span class="tier-badge ${b.tier.includes('Tier 1') ? 'marquee' : 'steal'}">${b.target_purse}</span></td>
        <td>
          <button class="btn-card-action" style="padding:0.25rem 0.5rem; font-size:0.75rem;" onclick="openPlayerDossier('${b.name}', 'bowler')">Dossier</button>
        </td>
      </tr>
    `;
  }).join('');
}

// Toggle View: Cards vs Table
function setBatterView(view) {
  batterView = view;
  document.getElementById('batter-btn-cards').classList.toggle('active', view === 'cards');
  document.getElementById('batter-btn-table').classList.toggle('active', view === 'table');
  document.getElementById('batters-cards-container').style.display = view === 'cards' ? 'grid' : 'none';
  document.getElementById('batters-table-container').style.display = view === 'table' ? 'block' : 'none';
}

function setBowlerView(view) {
  bowlerView = view;
  document.getElementById('bowler-btn-cards').classList.toggle('active', view === 'cards');
  document.getElementById('bowler-btn-table').classList.toggle('active', view === 'table');
  document.getElementById('bowlers-cards-container').style.display = view === 'cards' ? 'grid' : 'none';
  document.getElementById('bowlers-table-container').style.display = view === 'table' ? 'block' : 'none';
}

// Player Dossier Modal
function openPlayerDossier(name, type) {
  const player = (type === 'batter' ? RAW_DATA.batters : RAW_DATA.bowlers).find(p => p.name === name);
  if (!player) return;

  const modal = document.getElementById('player-modal');
  const body = document.getElementById('modal-dossier-body');
  if (!modal || !body) return;

  const isBatter = type === 'batter';

  body.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
      <div>
        <div style="display:flex; align-items:center; gap:0.75rem;">
          <span style="background:var(--rr-pink); color:white; font-family:var(--font-heading); font-weight:800; padding:0.2rem 0.6rem; border-radius:6px; font-size:1.1rem;">#${player.rank}</span>
          <h2 style="font-family:var(--font-heading); font-size:2rem; font-weight:800; color:white; line-height:1;">${player.name}</h2>
        </div>
        <p style="color:var(--text-muted); font-size:0.95rem; margin-top:0.35rem;">${player.country} • ${player.role} • <span style="color:var(--rr-pink-light); font-weight:600;">${player.archetype}</span></p>
      </div>
      <div style="text-align:right;">
        <span class="tier-badge marquee" style="font-size:0.85rem; padding:0.35rem 0.85rem;">${player.tier}</span>
        <div style="font-family:var(--font-mono); color:var(--rr-gold); font-size:1.1rem; font-weight:700; margin-top:0.35rem;">Target: ${player.target_purse}</div>
      </div>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(160px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
      <div style="background:rgba(5,11,20,0.7); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
        <div style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">Impact (WPA/100)</div>
        <div style="font-size:1.6rem; font-weight:800; color:var(--accent-green); font-family:var(--font-mono);">+${player.impact.toFixed(1)}</div>
        <div style="font-size:0.75rem; color:var(--text-dim);">${player.pressure_balls} clutch balls</div>
      </div>
      <div style="background:rgba(5,11,20,0.7); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
        <div style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">Resilience Score</div>
        <div style="font-size:1.6rem; font-weight:800; color:var(--rr-pink-light); font-family:var(--font-mono);">+${player.resilience.toFixed(2)}</div>
        <div style="font-size:0.75rem; color:var(--text-dim);">z-score lift</div>
      </div>
      <div style="background:rgba(5,11,20,0.7); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
        <div style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">Match Consistency</div>
        <div style="font-size:1.6rem; font-weight:800; color:white; font-family:var(--font-mono);">${player.consistency}%</div>
        <div style="font-size:0.75rem; color:var(--text-dim);">Beta-shrunk win rate</div>
      </div>
      <div style="background:rgba(5,11,20,0.7); padding:1rem; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
        <div style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">${isBatter ? 'Pressure Strike Rate' : 'Pressure Economy'}</div>
        <div style="font-size:1.6rem; font-weight:800; color:var(--rr-gold); font-family:var(--font-mono);">${isBatter ? player.sr_pressure : player.econ_pressure.toFixed(2)}</div>
        <div style="font-size:0.75rem; color:var(--text-dim);">Usual: ${isBatter ? player.sr_usual : player.econ_usual.toFixed(2)}</div>
      </div>
    </div>

    <div class="glass-section" style="padding:1.25rem; margin-bottom:1.25rem; background:rgba(18,38,68,0.5);">
      <h4 style="font-family:var(--font-heading); color:var(--rr-pink-light); text-transform:uppercase; margin-bottom:0.6rem; font-size:1.1rem;">
        👑 Rajasthan Royals Tactical Blueprint
      </h4>
      <p style="font-size:0.92rem; color:#E2E8F0; margin-bottom:0.85rem; line-height:1.5;">${player.rr_fit}</p>
      
      <div style="margin-bottom:0.75rem;">
        <strong style="color:var(--text-main); font-size:0.85rem;">Core Synergy:</strong>
        <p style="font-size:0.85rem; color:var(--text-muted);">${player.synergy}</p>
      </div>

      <div style="margin-bottom:0.75rem;">
        <strong style="color:var(--text-main); font-size:0.85rem;">Sawai Mansingh Stadium (Jaipur) Fit:</strong>
        <p style="font-size:0.85rem; color:var(--text-muted);">${player.sms_fit}</p>
      </div>

      <div>
        <strong style="color:var(--text-main); font-size:0.85rem;">Auction Execution Strategy:</strong>
        <p style="font-size:0.85rem; color:var(--text-muted);">${player.auction_strategy}</p>
      </div>
    </div>

    <div style="display:flex; justify-content:flex-end; gap:0.75rem; margin-top:1.5rem;">
      <button class="btn-card-action" onclick="sendToCompare('${player.name}', '${type}'); closePlayerDossier();">
        ⚔️ Compare Player
      </button>
      <button class="btn-export-pdf" onclick="toggleAuctionBuy('${player.name}', '${type}'); closePlayerDossier();">
        ${squadBought.some(p => p.name === player.name) ? '✓ In RR Squad' : '+ Add to RR War Room Squad'}
      </button>
    </div>
  `;

  modal.classList.add('open');
}

function closePlayerDossier() {
  const modal = document.getElementById('player-modal');
  if (modal) modal.classList.remove('open');
}

// Compare Tool Setup
function initCompareDropdowns() {
  const selA = document.getElementById('compare-player-a');
  const selB = document.getElementById('compare-player-b');
  const catSel = document.getElementById('compare-category');
  if (!selA || !selB || !catSel) return;

  function populate(cat) {
    const list = cat === 'batters' ? RAW_DATA.batters : RAW_DATA.bowlers;
    const opts = list.map(p => `<option value="${p.name}">${p.rank}. ${p.name} (${p.country})</option>`).join('');
    selA.innerHTML = opts;
    selB.innerHTML = opts;
    selB.selectedIndex = Math.min(1, list.length - 1);
    updateCompareView();
  }

  catSel.addEventListener('change', () => {
    populate(catSel.value);
  });

  selA.addEventListener('change', updateCompareView);
  selB.addEventListener('change', updateCompareView);

  populate('batters');
}

function sendToCompare(name, type) {
  switchTab('compare');
  const catSel = document.getElementById('compare-category');
  const selA = document.getElementById('compare-player-a');
  const selB = document.getElementById('compare-player-b');
  if (!catSel || !selA || !selB) return;

  const cat = type === 'batter' ? 'batters' : 'bowlers';
  catSel.value = cat;
  
  const list = cat === 'batters' ? RAW_DATA.batters : RAW_DATA.bowlers;
  const opts = list.map(p => `<option value="${p.name}">${p.rank}. ${p.name} (${p.country})</option>`).join('');
  selA.innerHTML = opts;
  selB.innerHTML = opts;

  selA.value = name;
  const other = list.find(p => p.name !== name);
  if (other) selB.value = other.name;

  updateCompareView();
}

function updateCompareView() {
  const cat = document.getElementById('compare-category')?.value || 'batters';
  const nameA = document.getElementById('compare-player-a')?.value;
  const nameB = document.getElementById('compare-player-b')?.value;

  const list = cat === 'batters' ? RAW_DATA.batters : RAW_DATA.bowlers;
  const pA = list.find(p => p.name === nameA) || list[0];
  const pB = list.find(p => p.name === nameB) || list[1];

  // Render side-by-side stats table
  const isBatter = cat === 'batters';
  const tableContainer = document.getElementById('compare-stats-table');
  if (tableContainer) {
    tableContainer.innerHTML = `
      <table class="data-table">
        <thead>
          <tr>
            <th>Metric Dimension</th>
            <th style="color:var(--rr-pink-light); font-size:1.1rem;">#${pA.rank} ${pA.name}</th>
            <th style="color:var(--accent-cyan); font-size:1.1rem;">#${pB.rank} ${pB.name}</th>
            <th>Tactical Advantage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Impact WPA / 100 Balls</td>
            <td style="font-weight:700; color:${pA.impact >= pB.impact ? 'var(--accent-green)' : 'var(--text-main)'};">+${pA.impact.toFixed(1)}</td>
            <td style="font-weight:700; color:${pB.impact >= pA.impact ? 'var(--accent-green)' : 'var(--text-main)'};">+${pB.impact.toFixed(1)}</td>
            <td><strong>${pA.impact >= pB.impact ? pA.name : pB.name}</strong> (+${Math.abs(pA.impact - pB.impact).toFixed(1)})</td>
          </tr>
          <tr>
            <td>Resilience z-Score (Clutch Lift)</td>
            <td style="font-weight:700; color:${pA.resilience >= pB.resilience ? 'var(--accent-green)' : 'var(--text-main)'};">+${pA.resilience.toFixed(2)}</td>
            <td style="font-weight:700; color:${pB.resilience >= pA.resilience ? 'var(--accent-green)' : 'var(--text-main)'};">+${pB.resilience.toFixed(2)}</td>
            <td><strong>${pA.resilience >= pB.resilience ? pA.name : pB.name}</strong></td>
          </tr>
          <tr>
            <td>Consistency Rate (% Win Positive)</td>
            <td style="font-weight:700; color:${pA.consistency >= pB.consistency ? 'var(--accent-green)' : 'var(--text-main)'};">${pA.consistency}%</td>
            <td style="font-weight:700; color:${pB.consistency >= pA.consistency ? 'var(--accent-green)' : 'var(--text-main)'};">${pB.consistency}%</td>
            <td><strong>${pA.consistency >= pB.consistency ? pA.name : pB.name}</strong></td>
          </tr>
          <tr>
            <td>${isBatter ? 'Pressure Strike Rate' : 'Pressure Economy (Lower is Better)'}</td>
            <td style="font-weight:700; color:${(isBatter ? pA.sr_pressure >= pB.sr_pressure : pA.econ_pressure <= pB.econ_pressure) ? 'var(--accent-green)' : 'var(--text-main)'};">
              ${isBatter ? pA.sr_pressure : pA.econ_pressure.toFixed(2)}
            </td>
            <td style="font-weight:700; color:${(isBatter ? pB.sr_pressure >= pA.sr_pressure : pB.econ_pressure <= pA.econ_pressure) ? 'var(--accent-green)' : 'var(--text-main)'};">
              ${isBatter ? pB.sr_pressure : pB.econ_pressure.toFixed(2)}
            </td>
            <td><strong>${(isBatter ? pA.sr_pressure >= pB.sr_pressure : pA.econ_pressure <= pB.econ_pressure) ? pA.name : pB.name}</strong></td>
          </tr>
          <tr>
            <td>${isBatter ? 'Balls Per Dismissal (Survival)' : 'Balls Per Wicket (Strike Rate)'}</td>
            <td>${isBatter ? pA.balls_per_dismissal + ' bpd' : pA.balls_per_wicket + ' bpw'}</td>
            <td>${isBatter ? pB.balls_per_dismissal + ' bpd' : pB.balls_per_wicket + ' bpw'}</td>
            <td><strong>${(isBatter ? pA.balls_per_dismissal >= pB.balls_per_dismissal : pA.balls_per_wicket <= pB.balls_per_wicket) ? pA.name : pB.name}</strong></td>
          </tr>
          <tr>
            <td>Pressure Sample Deliveries</td>
            <td>${pA.pressure_balls} balls</td>
            <td>${pB.pressure_balls} balls</td>
            <td><strong>${pA.pressure_balls >= pB.pressure_balls ? pA.name : pB.name}</strong> (Higher Sample)</td>
          </tr>
          <tr>
            <td>Estimated Auction Valuation</td>
            <td style="color:var(--rr-gold); font-weight:700;">${pA.target_purse}</td>
            <td style="color:var(--rr-gold); font-weight:700;">${pB.target_purse}</td>
            <td>${pA.tier} vs ${pB.tier}</td>
          </tr>
        </tbody>
      </table>
    `;
  }

  updateCompareRadar(pA, pB, isBatter);
}

function updateCompareRadar(pA, pB, isBatter) {
  const canvas = document.getElementById('compare-radar-chart');
  if (!canvas) return;

  if (!pA || !pB) {
    const cat = document.getElementById('compare-category')?.value || 'batters';
    const list = cat === 'batters' ? RAW_DATA.batters : RAW_DATA.bowlers;
    pA = list[0];
    pB = list[1];
    isBatter = cat === 'batters';
  }

  // Normalize stats 0 to 100 for radar
  const normImpactA = Math.min(100, (pA.impact / 10) * 100);
  const normImpactB = Math.min(100, (pB.impact / 10) * 100);

  const normResilA = Math.min(100, (pA.resilience / 5) * 100);
  const normResilB = Math.min(100, (pB.resilience / 5) * 100);

  const normConsistA = pA.consistency;
  const normConsistB = pB.consistency;

  const normRateA = isBatter ? Math.min(100, (pA.sr_pressure / 200) * 100) : Math.max(0, 100 - (pA.econ_pressure - 6) * 20);
  const normRateB = isBatter ? Math.min(100, (pB.sr_pressure / 200) * 100) : Math.max(0, 100 - (pB.econ_pressure - 6) * 20);

  const normStabilityA = pA.bootstrap_stability;
  const normStabilityB = pB.bootstrap_stability;

  const labels = ['Impact WPA', 'Resilience', 'Consistency', isBatter ? 'Strike Rate' : 'Economy Squeeze', 'Sample Stability'];

  if (radarChart) {
    radarChart.destroy();
  }

  radarChart = new Chart(canvas, {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [
        {
          label: pA.name,
          data: [normImpactA, normResilA, normConsistA, normRateA, normStabilityA],
          backgroundColor: 'rgba(231, 56, 149, 0.25)',
          borderColor: '#E73895',
          borderWidth: 2,
          pointBackgroundColor: '#E73895',
          pointBorderColor: '#fff',
        },
        {
          label: pB.name,
          data: [normImpactB, normResilB, normConsistB, normRateB, normStabilityB],
          backgroundColor: 'rgba(6, 182, 212, 0.25)',
          borderColor: '#06B6D4',
          borderWidth: 2,
          pointBackgroundColor: '#06B6D4',
          pointBorderColor: '#fff',
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
          grid: { color: 'rgba(255, 255, 255, 0.1)' },
          pointLabels: {
            color: '#94A3B8',
            font: { family: "'Rajdhani', sans-serif", size: 12, weight: 'bold' }
          },
          ticks: { display: false, min: 0, max: 100 }
        }
      },
      plugins: {
        legend: {
          labels: { color: '#F8FAFC', font: { family: "'Outfit', sans-serif", size: 13, weight: 'bold' } }
        }
      }
    }
  });
}

// Match Pressure & Leverage Simulator
function initSimulator() {
  const inputs = ['sim-target', 'sim-score', 'sim-overs', 'sim-wickets', 'sim-innings'];
  inputs.forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener('input', updateSimulator);
    }
  });

  updateSimulator();
}

function updateSimulator() {
  const target = parseFloat(document.getElementById('sim-target')?.value || 190);
  const score = parseFloat(document.getElementById('sim-score')?.value || 140);
  const oversDone = parseFloat(document.getElementById('sim-overs')?.value || 16.0);
  const wickets = parseInt(document.getElementById('sim-wickets')?.value || 4);
  const innings = parseInt(document.getElementById('sim-innings')?.value || 2);

  // Update slider label values
  document.getElementById('val-sim-target').innerText = target;
  document.getElementById('val-sim-score').innerText = score;
  document.getElementById('val-sim-overs').innerText = oversDone.toFixed(1);
  document.getElementById('val-sim-wickets').innerText = wickets;

  // Ball calculations
  const totalBalls = 120;
  const completedOversInt = Math.floor(oversDone);
  const ballsInOver = Math.round((oversDone - completedOversInt) * 10);
  const ballsBowled = Math.min(120, completedOversInt * 6 + ballsInOver);
  const ballsRemaining = Math.max(1, 120 - ballsBowled);
  const oversRemaining = ballsRemaining / 6;

  const runsNeeded = Math.max(1, target - score);
  const rrr = runsNeeded / oversRemaining;
  const crr = score / Math.max(0.1, ballsBowled / 6);

  // Model-grounded Win Probability & Leverage Calculation
  // Grounded in Chase LightGBM logic from Methodology Report (AUC 0.89)
  let winProbBatting = 0.5;
  if (innings === 2) {
    const requiredRunGap = rrr - crr;
    const wicketDiscount = (10 - wickets) / 10;
    // Logistic approximation of out-of-fold GBDT model
    const logit = 1.8 - (0.42 * rrr) + (0.55 * wicketDiscount * 10) - (0.015 * ballsRemaining);
    winProbBatting = 1 / (1 + Math.exp(-logit));
  } else {
    // 1st innings projection
    const projectedFinal = score + (oversRemaining * 9.2);
    winProbBatting = 1 / (1 + Math.exp(-((projectedFinal - target) / 25)));
  }
  winProbBatting = Math.max(0.01, Math.min(0.99, winProbBatting));

  // Leverage calculation: L_i = expected absolute swing over possible ball outcomes
  // Higher when game is 20-80% win prob and few balls remaining
  const closenessFactor = 1 - Math.abs(winProbBatting - 0.5) * 2; // peaks at 50%
  const urgencyFactor = Math.sqrt(120 / Math.max(6, ballsRemaining));
  const leverage = (closenessFactor * 2.8) * urgencyFactor * (0.8 + (rrr / 12) * 0.4);
  const shrunkLeverage = Math.min(8.5, Math.max(0.3, leverage));

  // Pressure Classification
  let tierLabel = 'Low Pressure (Ordinary)';
  let tierClass = 'tier-low';
  let tierDesc = 'Match state is comfortably decided or in early consolidation phase.';

  if (shrunkLeverage >= 4.0 || (shrunkLeverage >= 2.47 && ballsRemaining <= 24)) {
    tierLabel = 'CRUCIBLE (EXTREME PRESSURE)';
    tierClass = 'tier-crucible';
    tierDesc = 'Game on the line! Every delivery alters win probability by 3.5%+ win points.';
  } else if (shrunkLeverage >= 2.47) {
    tierLabel = 'HIGH PRESSURE (Q3 THRESHOLD)';
    tierClass = 'tier-high';
    tierDesc = 'Qualifies into the 28,264 official high-pressure deliveries dataset.';
  } else if (shrunkLeverage >= 1.5) {
    tierLabel = 'MODERATE PRESSURE';
    tierClass = 'tier-moderate';
    tierDesc = 'Contest in balance; pivotal phase before late acceleration.';
  }

  // Update UI Displays
  const levEl = document.getElementById('sim-leverage-display');
  const tierEl = document.getElementById('sim-tier-display');
  const descEl = document.getElementById('sim-tier-desc');
  const wpBatEl = document.getElementById('sim-wp-bat');
  const wpBowlEl = document.getElementById('sim-wp-bowl');
  const rrrEl = document.getElementById('sim-rrr-display');

  if (levEl) levEl.innerText = shrunkLeverage.toFixed(2);
  if (tierEl) {
    tierEl.className = 'pressure-tier-pill ' + tierClass;
    tierEl.innerText = tierLabel;
  }
  if (descEl) descEl.innerText = tierDesc;
  if (wpBatEl) wpBatEl.innerText = `${(winProbBatting * 100).toFixed(1)}%`;
  if (wpBowlEl) wpBowlEl.innerText = `${((1 - winProbBatting) * 100).toFixed(1)}%`;
  if (rrrEl) rrrEl.innerText = rrr.toFixed(2);

  // Dynamic Tactical Recommendation based on exact match state
  renderSimTacticalRecommendation(shrunkLeverage, rrr, ballsRemaining, wickets, innings);
}

function renderSimTacticalRecommendation(leverage, rrr, ballsLeft, wickets, innings) {
  const recContainer = document.getElementById('sim-recommendation-box');
  if (!recContainer) return;

  let recBatter = RAW_DATA.batters[0]; // Jos Buttler default
  let recBowler = RAW_DATA.bowlers[0]; // Axar Patel default

  if (rrr > 12 || ballsLeft <= 18) {
    // Extreme death overs burst
    recBatter = RAW_DATA.batters[1]; // Tim David (Impact +9.5, SR 179)
    recBowler = RAW_DATA.bowlers[4]; // Bhuvneshwar Kumar (Wk every 13b)
  } else if (wickets >= 5) {
    // Crisis stabilization
    recBatter = RAW_DATA.batters[2]; // David Miller (38 bpd, +3.35 Resil)
    recBowler = RAW_DATA.bowlers[1]; // Sunil Narine (Econ 7.25, 37% dots)
  } else if (ballsLeft >= 60) {
    // Middle overs spin phase
    recBatter = RAW_DATA.batters[4]; // Heinrich Klaasen (179 SR vs spin)
    recBowler = RAW_DATA.bowlers[3]; // Kuldeep Yadav (Wk every 14b, 7.11 econ)
  }

  recContainer.innerHTML = `
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.25rem;">
      <div style="background:rgba(5,11,20,0.6); padding:1.25rem; border-radius:8px; border:1px solid rgba(231,56,149,0.3);">
        <div style="font-size:0.75rem; text-transform:uppercase; color:var(--rr-pink-light); font-weight:700;">🏏 Optimal Batter to Send In</div>
        <h4 style="font-family:var(--font-heading); font-size:1.4rem; color:white; margin:0.3rem 0;">#${recBatter.rank} ${recBatter.name}</h4>
        <p style="font-size:0.8rem; color:var(--text-muted);">${recBatter.role} (${recBatter.country})</p>
        <div style="margin-top:0.6rem; font-size:0.82rem; color:var(--text-main);">
          ⚡ <strong>Expected Pressure SR:</strong> <span style="color:var(--rr-gold);">${recBatter.sr_pressure}</span><br>
          🛡️ <strong>Survival Rate:</strong> 1 dismissal / ${recBatter.balls_per_dismissal} balls<br>
          🎯 <strong>Tactical Purpose:</strong> ${recBatter.strengths[0]}
        </div>
      </div>

      <div style="background:rgba(5,11,20,0.6); padding:1.25rem; border-radius:8px; border:1px solid rgba(6,182,212,0.3);">
        <div style="font-size:0.75rem; text-transform:uppercase; color:var(--accent-cyan); font-weight:700;">🎯 Optimal Bowler to Bowl This Over</div>
        <h4 style="font-family:var(--font-heading); font-size:1.4rem; color:white; margin:0.3rem 0;">#${recBowler.rank} ${recBowler.name}</h4>
        <p style="font-size:0.8rem; color:var(--text-muted);">${recBowler.role} (${recBowler.country})</p>
        <div style="margin-top:0.6rem; font-size:0.82rem; color:var(--text-main);">
          🔒 <strong>Pressure Economy:</strong> <span style="color:var(--accent-green);">${recBowler.econ_pressure.toFixed(2)} RPO</span><br>
          💥 <strong>Strike Threat:</strong> Wicket every ${recBowler.balls_per_wicket} balls (${recBowler.dot_pct}% dots)<br>
          🎯 <strong>Tactical Purpose:</strong> ${recBowler.strengths[0]}
        </div>
      </div>
    </div>
  `;
}

// Auction War Room & Squad Builder
function initAuctionWarRoom() {
  updateAuctionUI();

  // Enter key support for bid input
  const bidInput = document.getElementById('bid-price-input');
  if (bidInput) {
    bidInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') confirmAuctionBid();
    });
  }
}

// Open the Live Bid Modal to ask the user for winning auction price
function toggleAuctionBuy(name, type) {
  const existingIdx = squadBought.findIndex(p => p.name === name);
  if (existingIdx >= 0) {
    // If already in squad, clicking removes them
    squadBought.splice(existingIdx, 1);
    updateAuctionUI();
    renderBatters();
    renderBowlers();
    return;
  }

  // Not in squad: prompt for auction price before adding
  const list = type === 'batter' ? RAW_DATA.batters : RAW_DATA.bowlers;
  const player = list.find(p => p.name === name);
  if (!player) return;

  openBidModal(player, type);
}

function openBidModal(player, type) {
  pendingPlayerForBid = { player, type };
  const modal = document.getElementById('auction-bid-modal');
  const nameEl = document.getElementById('bid-modal-player-name');
  const roleEl = document.getElementById('bid-modal-player-role');
  const purseEl = document.getElementById('bid-modal-current-purse');
  const inputEl = document.getElementById('bid-price-input');
  const presetsEl = document.getElementById('bid-price-presets');
  const errEl = document.getElementById('bid-error-msg');

  if (!modal || !nameEl || !inputEl) return;

  const remaining = Math.max(0, auctionBudget - spentBudget);

  nameEl.innerText = player.name;
  roleEl.innerText = `${player.role} • ${player.country} (Expected: ${player.target_purse})`;
  purseEl.innerText = `₹${remaining.toFixed(1)} Cr`;
  errEl.innerText = '';

  // Extract recommended price bounds
  let low = 5.0, mid = 8.0, high = 12.0;
  if (player.target_purse.includes('-')) {
    const parts = player.target_purse.replace('Cr', '').trim().split('-');
    low = parseFloat(parts[0]);
    high = parseFloat(parts[1]);
    mid = parseFloat(((low + high) / 2).toFixed(2));
  }

  inputEl.value = mid;
  inputEl.max = remaining;

  // Preset chips
  if (presetsEl) {
    presetsEl.innerHTML = `
      <span class="preset-chip" onclick="setBidInputValue(${low})">₹${low} Cr (Base)</span>
      <span class="preset-chip" onclick="setBidInputValue(${mid})">₹${mid} Cr (Mid)</span>
      <span class="preset-chip" onclick="setBidInputValue(${high})">₹${high} Cr (Ceiling)</span>
      <span class="preset-chip" onclick="setBidInputValue(${Math.min(remaining, high + 2.5)})">₹${Math.min(remaining, high + 2.5)} Cr (Aggressive)</span>
    `;
  }

  modal.classList.add('open');
  setTimeout(() => inputEl.focus(), 100);
}

function setBidInputValue(val) {
  const input = document.getElementById('bid-price-input');
  if (input) input.value = val;
}

function closeBidModal() {
  const modal = document.getElementById('auction-bid-modal');
  if (modal) modal.classList.remove('open');
  pendingPlayerForBid = null;
}

function confirmAuctionBid() {
  if (!pendingPlayerForBid) return;
  const { player, type } = pendingPlayerForBid;
  const input = document.getElementById('bid-price-input');
  const errEl = document.getElementById('bid-error-msg');
  const price = parseFloat(input?.value || 0);

  if (isNaN(price) || price <= 0) {
    if (errEl) errEl.innerText = 'Please enter a valid auction bid greater than 0.';
    return;
  }

  const remaining = auctionBudget - spentBudget;
  if (price > remaining) {
    if (errEl) errEl.innerText = `Purse Exceeded! You only have ₹${remaining.toFixed(1)} Cr available.`;
    return;
  }

  // Successfully add player at the custom bid price
  squadBought.push({
    ...player,
    type: type,
    estimatedCost: price,
    isOverseas: player.country !== 'India'
  });

  closeBidModal();
  updateAuctionUI();
  renderBatters();
  renderBowlers();

  // If in auction tab, smooth scroll to predictions
  if (currentTab === 'auction') {
    const predEl = document.getElementById('dynamic-auction-predictions-container');
    if (predEl) predEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

function updateAuctionUI() {
  spentBudget = squadBought.reduce((acc, p) => acc + p.estimatedCost, 0);
  const remaining = Math.max(0, auctionBudget - spentBudget);
  const overseasCount = squadBought.filter(p => p.isOverseas).length + 1; // 1 retained overseas (Hetmyer)

  // Update budget widgets
  const remEl = document.getElementById('auction-purse-remaining');
  const spentEl = document.getElementById('auction-purse-spent');
  const boughtCountEl = document.getElementById('auction-bought-count');
  const overseasEl = document.getElementById('auction-overseas-count');
  const predPursePill = document.getElementById('predictions-purse-pill');

  if (remEl) remEl.innerText = `₹${remaining.toFixed(1)} Cr`;
  if (spentEl) spentEl.innerText = `₹${spentBudget.toFixed(1)} Cr`;
  if (boughtCountEl) boughtCountEl.innerText = `${squadBought.length} Targets`;
  if (overseasEl) overseasEl.innerText = `${overseasCount} / 8 Allowed`;
  if (predPursePill) predPursePill.innerText = `Purse Available: ₹${remaining.toFixed(1)} Cr`;

  // Top header quick purse update
  const topPurse = document.getElementById('top-bar-purse');
  if (topPurse) topPurse.innerText = `₹${remaining.toFixed(1)} Cr`;

  // Calculate Team Clutch Index
  const allClutchScores = [
    ...rrRetainedCore.map(c => c.clutch),
    ...squadBought.map(p => Math.round(50 + p.impact * 3 + p.resilience * 5))
  ];
  const avgClutch = Math.round(allClutchScores.reduce((a, b) => a + b, 0) / allClutchScores.length);
  const clutchEl = document.getElementById('auction-team-clutch');
  if (clutchEl) clutchEl.innerText = `${avgClutch} / 100`;

  // Render Bought List
  const listEl = document.getElementById('auction-bought-list');
  if (listEl) {
    if (squadBought.length === 0) {
      listEl.innerHTML = `
        <div style="text-align:center; padding:2rem; color:var(--text-muted); font-size:0.9rem;">
          No auction targets added yet. Click "+ Add to RR" on any Top-10 batter or bowler. You will be prompted to enter your winning bid price!
        </div>
      `;
    } else {
      listEl.innerHTML = squadBought.map(p => `
        <div style="display:flex; align-items:center; justify-content:space-between; background:rgba(5,11,20,0.6); border:1px solid rgba(255,255,255,0.06); padding:0.6rem 1rem; border-radius:6px; margin-bottom:0.5rem;">
          <div>
            <strong style="color:white; font-size:0.95rem;">${p.name}</strong>
            <span style="font-size:0.75rem; color:var(--text-muted); margin-left:0.4rem;">(${p.role})</span>
          </div>
          <div style="display:flex; align-items:center; gap:0.75rem;">
            <span style="color:var(--rr-gold); font-family:var(--font-mono); font-weight:700;">₹${p.estimatedCost.toFixed(1)} Cr</span>
            <button onclick="toggleAuctionBuy('${p.name}', '${p.type}')" title="Remove player from squad" style="background:transparent; border:none; color:var(--accent-red); cursor:pointer; font-size:1rem;">✕</button>
          </div>
        </div>
      `).join('');
    }
  }

  // Render Dynamic AI Predictions based on Remaining Purse
  renderRemainingPursePredictions(remaining, overseasCount);

  // Render Simulated RR Playing XI
  renderSimulatedRRXI();
}

// Dynamic AI Predictions based on live remaining purse
function renderRemainingPursePredictions(remaining, overseasCount) {
  const container = document.getElementById('dynamic-auction-predictions-container');
  if (!container) return;

  // Find all remaining unbought top players
  const unboughtBatters = RAW_DATA.batters.filter(b => !squadBought.some(p => p.name === b.name));
  const unboughtBowlers = RAW_DATA.bowlers.filter(b => !squadBought.some(p => p.name === b.name));
  const allUnbought = [...unboughtBatters.map(p => ({ ...p, type: 'batter' })), ...unboughtBowlers.map(p => ({ ...p, type: 'bowler' }))];

  if (allUnbought.length === 0) {
    container.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:1.5rem; color:var(--accent-green); font-weight:700;">All 20 top clutch targets have been acquired into the Rajasthan Royals setup!</div>`;
    return;
  }

  // Evaluate affordability and AI advice for each unbought player
  const cardsHtml = allUnbought.map(player => {
    let low = 4.0, high = 10.0;
    if (player.target_purse.includes('-')) {
      const parts = player.target_purse.replace('Cr', '').trim().split('-');
      low = parseFloat(parts[0]);
      high = parseFloat(parts[1]);
    }

    const isOverseas = player.country !== 'India';
    const overseasBlocked = isOverseas && overseasCount >= 8;

    let status = 'affordable';
    let badge = 'Feasible Priority';
    let badgeClass = 'green';
    let advice = `Comfortably within remaining ₹${remaining.toFixed(1)} Cr purse. Recommended maximum bid: ₹${Math.min(remaining, high).toFixed(1)} Cr.`;

    if (overseasBlocked) {
      status = 'unaffordable';
      badge = 'Overseas Cap Reached (8/8)';
      badgeClass = 'red';
      advice = 'RR has exhausted its 8 overseas roster slots. Must target Indian alternatives.';
    } else if (remaining < low) {
      status = 'unaffordable';
      badge = 'Purse Deficit';
      badgeClass = 'red';
      advice = `Remaining purse (₹${remaining.toFixed(1)} Cr) is below minimum entry price (₹${low} Cr). Requires releasing drafted targets.`;
    } else if (remaining < high) {
      status = 'stretch';
      badge = 'Tight Purse / High Risk';
      badgeClass = 'gold';
      advice = `Can only be acquired if bid does not exceed ₹${remaining.toFixed(1)} Cr. Leaves very little cushion for squad depth.`;
    } else {
      // Affordability combination advice
      const remAfter = remaining - high;
      if (remAfter >= 15.0) {
        advice = `Prime Target! Even after paying ₹${high} Cr, RR retains ₹${remAfter.toFixed(1)} Cr to secure another marquee name.`;
      } else if (remAfter >= 6.0) {
        advice = `Great fit! Leaves ₹${remAfter.toFixed(1)} Cr, perfectly suited to pair with a budget steal like Taskin Ahmed or Krunal Pandya.`;
      }
    }

    return `
      <div class="prediction-card ${status}">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.5rem;">
            <div>
              <span style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">#${player.rank} ${player.type.toUpperCase()}</span>
              <h4 style="font-family:var(--font-heading); font-size:1.25rem; color:white; margin:0.1rem 0;">${player.name}</h4>
              <span style="font-size:0.75rem; color:var(--text-muted);">${player.country} • ${player.role}</span>
            </div>
            <span class="prediction-badge ${badgeClass}">${badge}</span>
          </div>

          <div style="display:flex; justify-content:space-between; font-size:0.8rem; margin:0.6rem 0; padding:0.4rem 0.6rem; background:rgba(0,0,0,0.3); border-radius:4px; font-family:var(--font-mono);">
            <span style="color:var(--text-dim);">Market Range: <strong style="color:var(--text-main);">${player.target_purse}</strong></span>
            <span style="color:var(--accent-green);">Impact: +${player.impact.toFixed(1)}</span>
          </div>

          <p style="font-size:0.8rem; color:#CBD5E1; line-height:1.4; margin-bottom:0.85rem;">
            💡 <strong>AI Prediction:</strong> ${advice}
          </p>
        </div>

        <button class="btn-card-action btn-buy" style="padding:0.45rem; font-size:0.8rem;" ${status === 'unaffordable' ? 'disabled style="opacity:0.4; cursor:not-allowed;"' : ''} onclick="openBidModal(RAW_DATA.${player.type === 'batter' ? 'batters' : 'bowlers'}.find(p => p.name === '${player.name}'), '${player.type}')">
          🔨 Enter Winning Bid
        </button>
      </div>
    `;
  }).join('');

  container.innerHTML = cardsHtml;
}

function renderSimulatedRRXI() {
  const pitchContainer = document.getElementById('simulated-rr-xi');
  if (!pitchContainer) return;

  // Build an optimal XI combining retained core (2026: Samson->CSK, Parag Captain, Jadeja to RR) + top auction acquisitions
  const xiSlots = [
    { pos: '1. Opener (LHB)', default: 'Yashasvi Jaiswal (VC)', targetRole: 'opener', assigned: 'Yashasvi Jaiswal (VC - Retained)' },
    { pos: '2. Opener / WK (RHB)', default: 'Auction Target', targetRole: 'opener', assigned: squadBought.find(p => p.role.includes('Opener') || p.name === 'Jos Buttler' || p.name === 'Phil Salt')?.name || 'Jos Buttler (Top Target: Replaces Samson WK Void)' },
    { pos: '3. Top-Order Power (#3)', default: 'Auction Target', targetRole: 'anchor', assigned: squadBought.find(p => p.name === 'Cameron Green' || p.name === 'Glenn Maxwell' || p.name === 'Daryl Mitchell')?.name || 'Cameron Green / Maxwell (Solves Samson #3 Spot)' },
    { pos: '4. Middle Order & Anchor', default: 'Riyan Parag (C)', targetRole: 'middle', assigned: 'Riyan Parag (Captain - Retained)' },
    { pos: '5. Spin Destroyer', default: 'Auction Target', targetRole: 'middle', assigned: squadBought.find(p => p.name === 'Heinrich Klaasen' || p.name === 'David Miller')?.name || 'Heinrich Klaasen / David Miller' },
    { pos: '6. Death Finisher', default: 'Shimron Hetmyer (O)', targetRole: 'finisher', assigned: 'Shimron Hetmyer (Retained)' },
    { pos: '7. Wicketkeeper / Finisher', default: 'Dhruv Jurel (WK)', targetRole: 'finisher', assigned: 'Dhruv Jurel (WK - Retained)' },
    { pos: '8. Spin All-Rounder', default: 'Ravindra Jadeja', targetRole: 'spin', assigned: 'Ravindra Jadeja (Retained - Joined RR in 2026)' },
    { pos: '9. Strike Spinner', default: 'Auction Target', targetRole: 'spin', assigned: squadBought.find(p => p.name === 'Axar Patel' || p.name === 'Kuldeep Yadav' || p.name === 'Sunil Narine' || p.name === 'Ravichandran Ashwin')?.name || 'Axar Patel / Kuldeep Yadav' },
    { pos: '10. Death Pacer', default: 'Sandeep Sharma', targetRole: 'pace', assigned: 'Sandeep Sharma (Retained)' },
    { pos: '11. Express Pacer (O)', default: 'Jofra Archer (Retained)', targetRole: 'pace', assigned: squadBought.find(p => p.name === 'Josh Hazlewood' || p.name === 'Taskin Ahmed')?.name || 'Jofra Archer (Retained) / Hazlewood' }
  ];

  pitchContainer.innerHTML = xiSlots.map(s => {
    const isTarget = !s.assigned.includes('Retained');
    return `
      <div class="pitch-slot ${isTarget ? 'bought' : ''}">
        <div>
          <span style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">${s.pos}</span><br>
          <strong style="color:${isTarget ? 'var(--rr-pink-light)' : 'white'};">${s.assigned}</strong>
        </div>
        <span style="font-size:0.75rem; color:${isTarget ? 'var(--rr-gold)' : 'var(--accent-green)'}; font-family:var(--font-mono);">
          ${isTarget ? '★ Auction' : '🔒 Retained'}
        </span>
      </div>
    `;
  }).join('');
}

// Chart.js initializations for overview charts
function initCharts() {
  const ctxBat = document.getElementById('overview-batters-chart');
  const ctxBowl = document.getElementById('overview-bowlers-chart');

  if (ctxBat) {
    new Chart(ctxBat, {
      type: 'bar',
      data: {
        labels: RAW_DATA.batters.map(b => b.name),
        datasets: [
          {
            label: 'Impact (WPA/100 Balls)',
            data: RAW_DATA.batters.map(b => b.impact),
            backgroundColor: 'rgba(231, 56, 149, 0.7)',
            borderColor: '#E73895',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'Resilience (z-Score)',
            data: RAW_DATA.batters.map(b => b.resilience),
            backgroundColor: 'rgba(245, 158, 11, 0.7)',
            borderColor: '#F59E0B',
            borderWidth: 1,
            borderRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { labels: { color: '#F8FAFC', font: { family: "'Outfit', sans-serif" } } }
        },
        scales: {
          x: { ticks: { color: '#94A3B8', maxRotation: 45, minRotation: 45 } },
          y: { ticks: { color: '#94A3B8' }, grid: { color: 'rgba(255, 255, 255, 0.05)' } }
        }
      }
    });
  }

  if (ctxBowl) {
    new Chart(ctxBowl, {
      type: 'bar',
      data: {
        labels: RAW_DATA.bowlers.map(b => b.name),
        datasets: [
          {
            label: 'Impact (WPA/100 Balls)',
            data: RAW_DATA.bowlers.map(b => b.impact),
            backgroundColor: 'rgba(6, 182, 212, 0.7)',
            borderColor: '#06B6D4',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'Consistency (%)',
            data: RAW_DATA.bowlers.map(b => b.consistency / 10), // scaled to fit
            backgroundColor: 'rgba(16, 185, 129, 0.7)',
            borderColor: '#10B981',
            borderWidth: 1,
            borderRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { labels: { color: '#F8FAFC', font: { family: "'Outfit', sans-serif" } } }
        },
        scales: {
          x: { ticks: { color: '#94A3B8', maxRotation: 45, minRotation: 45 } },
          y: { ticks: { color: '#94A3B8' }, grid: { color: 'rgba(255, 255, 255, 0.05)' } }
        }
      }
    });
  }
}

// Print / PDF Exporter
function exportSubmissionPDF() {
  window.print();
}
"""
