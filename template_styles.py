CSS_CONTENT = """
:root {
  --rr-pink: #E73895;
  --rr-pink-light: #FF5EAA;
  --rr-pink-glow: rgba(231, 56, 149, 0.35);
  --rr-blue: #0A192F;
  --rr-blue-deep: #050B14;
  --rr-blue-card: rgba(13, 27, 49, 0.82);
  --rr-blue-surface: rgba(18, 38, 68, 0.7);
  --rr-blue-border: rgba(231, 56, 149, 0.22);
  --rr-gold: #F59E0B;
  --rr-gold-glow: rgba(245, 158, 11, 0.3);
  --text-main: #F8FAFC;
  --text-muted: #94A3B8;
  --text-dim: #64748B;
  --accent-green: #10B981;
  --accent-red: #EF4444;
  --accent-cyan: #06B6D4;
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --font-heading: 'Rajdhani', sans-serif;
  --font-body: 'Outfit', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 25px var(--rr-pink-glow);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: var(--rr-blue-deep);
  background-image: 
    radial-gradient(circle at 10% 20%, rgba(231, 56, 149, 0.12) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(10, 25, 47, 0.8) 0%, transparent 50%),
    linear-gradient(180deg, #050B14 0%, #0A192F 100%);
  background-attachment: fixed;
  color: var(--text-main);
  font-family: var(--font-body);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}

/* Scrollbar */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
::-webkit-scrollbar-track {
  background: var(--rr-blue-deep);
}
::-webkit-scrollbar-thumb {
  background: rgba(231, 56, 149, 0.3);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--rr-pink);
}

/* Header & Navbar */
header.app-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(5, 11, 20, 0.92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--rr-blue-border);
  padding: 0.75rem 2rem;
}

.header-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.brand-container {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.rr-crest-badge {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--rr-pink) 0%, #9F1239 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 15px var(--rr-pink-glow);
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 1.5rem;
  color: white;
  letter-spacing: -1px;
}

.brand-text h1 {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  background: linear-gradient(90deg, #FFFFFF, var(--rr-pink-light));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.brand-text h1 span {
  -webkit-text-fill-color: #FFFFFF !important;
  color: #FFFFFF !important;
  display: inline-block;
}

.brand-text p {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1.5px;
}

.header-status-pills {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.status-pill {
  padding: 0.35rem 0.85rem;
  background: var(--rr-blue-surface);
  border: 1px solid var(--rr-blue-border);
  border-radius: 9999px;
  font-size: 0.75rem;
  font-family: var(--font-mono);
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.status-pill.highlight {
  border-color: var(--rr-pink);
  color: var(--rr-pink-light);
  background: rgba(231, 56, 149, 0.1);
}

.status-pill.gold {
  border-color: var(--rr-gold);
  color: var(--rr-gold);
  background: rgba(245, 158, 11, 0.1);
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background-color: var(--accent-green);
  border-radius: 50%;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.9); opacity: 0.7; }
  50% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.7; }
}

/* Nav Tabs */
nav.app-nav {
  margin-top: 0.6rem;
  display: flex;
  gap: 0.4rem;
  overflow-x: auto;
  padding-bottom: 0.25rem;
}

.nav-tab-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-family: var(--font-heading);
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 0.5rem 1rem;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-tab-btn:hover {
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.05);
}

.nav-tab-btn.active {
  color: white;
  background: linear-gradient(135deg, rgba(231, 56, 149, 0.25) 0%, rgba(231, 56, 149, 0.05) 100%);
  border-bottom: 2px solid var(--rr-pink);
  box-shadow: 0 4px 12px var(--rr-pink-glow);
}

.btn-export-pdf {
  background: linear-gradient(135deg, var(--rr-pink) 0%, #C2185B 100%);
  color: white;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: var(--radius-sm);
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
  box-shadow: 0 4px 15px var(--rr-pink-glow);
}

.btn-export-pdf:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--rr-pink-glow);
}

/* Main Container */
main.dashboard-container {
  max-width: 1500px;
  margin: 0 auto;
  padding: 2rem;
}

/* Tab Content Visibility */
.tab-content {
  display: none;
  animation: fadeIn 0.3s ease;
}

.tab-content.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Metric Stats Grid */
.stats-banner-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--rr-blue-card);
  border: 1px solid var(--rr-blue-border);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-card);
  backdrop-filter: blur(12px);
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-3px);
  border-color: var(--rr-pink);
}

.stat-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--rr-pink);
}

.stat-card.gold::after { background: var(--rr-gold); }
.stat-card.green::after { background: var(--accent-green); }
.stat-card.cyan::after { background: var(--accent-cyan); }

.stat-card-title {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  color: var(--text-muted);
  font-family: var(--font-heading);
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.stat-card-value {
  font-size: 1.85rem;
  font-weight: 800;
  font-family: var(--font-heading);
  color: var(--text-main);
  line-height: 1.2;
}

.stat-card-sub {
  font-size: 0.75rem;
  color: var(--text-dim);
  margin-top: 0.35rem;
}

/* Glass Section Container */
.glass-section {
  background: var(--rr-blue-card);
  border: 1px solid var(--rr-blue-border);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  margin-bottom: 2rem;
  box-shadow: var(--shadow-card);
  backdrop-filter: blur(14px);
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.section-title {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.section-title .icon {
  color: var(--rr-pink);
}

.section-subtitle {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-top: 0.2rem;
}

/* Controls bar: search, filters */
.controls-bar {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
  background: rgba(10, 25, 47, 0.6);
  padding: 0.85rem 1.25rem;
  border-radius: var(--radius-md);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.search-input-wrap {
  position: relative;
  flex: 1;
  min-width: 220px;
}

.search-input-wrap input {
  width: 100%;
  background: rgba(5, 11, 20, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.6rem 1rem 0.6rem 2.2rem;
  border-radius: var(--radius-sm);
  color: white;
  font-family: var(--font-body);
  font-size: 0.9rem;
  transition: border-color 0.2s;
}

.search-input-wrap input:focus {
  outline: none;
  border-color: var(--rr-pink);
}

.search-input-wrap .search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-dim);
  font-size: 0.85rem;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.filter-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-family: var(--font-heading);
  text-transform: uppercase;
}

select.filter-select {
  background: rgba(5, 11, 20, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  padding: 0.55rem 1rem;
  border-radius: var(--radius-sm);
  font-family: var(--font-body);
  font-size: 0.85rem;
  cursor: pointer;
}

select.filter-select:focus {
  outline: none;
  border-color: var(--rr-pink);
}

.view-toggle {
  display: flex;
  background: rgba(5, 11, 20, 0.8);
  border-radius: var(--radius-sm);
  padding: 0.2rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.view-toggle-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.4rem 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8rem;
  transition: all 0.2s;
}

.view-toggle-btn.active {
  background: var(--rr-pink);
  color: white;
}

/* Player Cards Grid */
.player-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 1.5rem;
}

.player-card {
  background: var(--rr-blue-surface);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-md);
  padding: 1.35rem;
  position: relative;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.player-card:hover {
  transform: translateY(-4px);
  border-color: var(--rr-pink);
  box-shadow: 0 12px 30px -5px rgba(0, 0, 0, 0.6), 0 0 15px var(--rr-pink-glow);
}

.player-card.rank-1 {
  border-color: var(--rr-gold);
  background: linear-gradient(145deg, rgba(245, 158, 11, 0.08) 0%, rgba(18, 38, 68, 0.8) 100%);
}

.player-card.rank-1::before {
  content: 'TOP PICK';
  position: absolute;
  top: -10px;
  right: 15px;
  background: var(--rr-gold);
  color: #000;
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 0.65rem;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  letter-spacing: 1px;
}

.card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 0.85rem;
}

.card-identity {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.rank-number {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--text-main);
}

.player-card.rank-1 .rank-number {
  background: var(--rr-gold);
  color: #000;
  border-color: var(--rr-gold);
}

.player-card.rank-2 .rank-number,
.player-card.rank-3 .rank-number {
  background: rgba(231, 56, 149, 0.25);
  color: var(--rr-pink-light);
  border-color: var(--rr-pink);
}

.player-names h3 {
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 700;
  color: white;
  line-height: 1.1;
}

.player-role-badge {
  font-size: 0.75rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: 0.2rem;
}

.tier-badge {
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.65rem;
  font-family: var(--font-mono);
  font-weight: 600;
  text-transform: uppercase;
}

.tier-badge.marquee {
  background: rgba(231, 56, 149, 0.2);
  color: var(--rr-pink-light);
  border: 1px solid var(--rr-pink);
}

.tier-badge.tactical {
  background: rgba(6, 182, 212, 0.15);
  color: var(--accent-cyan);
  border: 1px solid rgba(6, 182, 212, 0.4);
}

.tier-badge.steal {
  background: rgba(16, 185, 129, 0.15);
  color: var(--accent-green);
  border: 1px solid rgba(16, 185, 129, 0.4);
}

.tier-badge.benchmark {
  background: rgba(148, 163, 184, 0.15);
  color: var(--text-muted);
  border: 1px solid var(--text-dim);
}

/* Key Metrics Grid inside card */
.card-metrics-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.65rem;
  margin: 1rem 0;
  background: rgba(5, 11, 20, 0.5);
  padding: 0.85rem;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(255, 255, 255, 0.04);
}

.metric-item {
  display: flex;
  flex-direction: column;
}

.metric-label {
  font-size: 0.65rem;
  text-transform: uppercase;
  color: var(--text-dim);
  font-family: var(--font-heading);
  letter-spacing: 0.5px;
}

.metric-value {
  font-family: var(--font-mono);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-main);
  display: flex;
  align-items: baseline;
  gap: 0.25rem;
}

.metric-value.positive { color: var(--accent-green); }
.metric-value.highlight { color: var(--rr-pink-light); }
.metric-value.gold { color: var(--rr-gold); }

.metric-sub {
  font-size: 0.7rem;
  color: var(--text-muted);
  font-weight: 400;
}

/* Performance comparison bar */
.card-diff-bar-wrap {
  margin-bottom: 1rem;
}

.diff-header {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-bottom: 0.35rem;
}

.diff-bar-track {
  height: 8px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
  display: flex;
}

.diff-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--rr-pink) 0%, var(--accent-green) 100%);
  border-radius: 4px;
  transition: width 0.5s ease;
}

/* RR Strategic Box inside card */
.rr-strategy-preview {
  background: rgba(231, 56, 149, 0.06);
  border-left: 3px solid var(--rr-pink);
  padding: 0.65rem 0.85rem;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  font-size: 0.78rem;
  color: #E2E8F0;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.card-actions {
  display: flex;
  gap: 0.5rem;
  margin-top: auto;
}

.btn-card-action {
  flex: 1;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--text-main);
  padding: 0.5rem;
  border-radius: var(--radius-sm);
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
}

.btn-card-action:hover {
  background: rgba(231, 56, 149, 0.2);
  border-color: var(--rr-pink);
  color: white;
}

.btn-card-action.btn-buy {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.2) 0%, rgba(245, 158, 11, 0.05) 100%);
  border-color: rgba(245, 158, 11, 0.4);
  color: var(--rr-gold);
}

.btn-card-action.btn-buy:hover {
  background: var(--rr-gold);
  color: #000;
}

/* Data Table Styling */
.table-responsive {
  overflow-x: auto;
  border-radius: var(--radius-md);
  border: 1px solid var(--rr-blue-border);
}

table.data-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.88rem;
}

table.data-table th {
  background: rgba(5, 11, 20, 0.9);
  padding: 0.85rem 1rem;
  font-family: var(--font-heading);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-muted);
  border-bottom: 2px solid var(--rr-blue-border);
  cursor: pointer;
  white-space: nowrap;
}

table.data-table th:hover {
  color: var(--rr-pink-light);
}

table.data-table td {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  color: var(--text-main);
  white-space: nowrap;
}

table.data-table tr:hover td {
  background: rgba(231, 56, 149, 0.05);
}

/* Modal Dossier */
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.modal-backdrop.open {
  display: flex;
}

.modal-content {
  background: var(--rr-blue);
  border: 1px solid var(--rr-pink);
  box-shadow: 0 0 40px var(--rr-pink-glow);
  border-radius: var(--radius-lg);
  max-width: 800px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  padding: 2rem;
  position: relative;
  animation: modalScale 0.25s ease;
}

@keyframes modalScale {
  from { transform: scale(0.95); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.modal-close-btn {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.modal-close-btn:hover {
  background: var(--rr-pink);
}

/* Head to Head Compare Tool */
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

@media (max-width: 900px) {
  .compare-grid { grid-template-columns: 1fr; }
}

.compare-selector-box {
  background: var(--rr-blue-surface);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  padding: 1.5rem;
}

/* Match Pressure Simulator */
.simulator-layout {
  display: grid;
  grid-template-columns: 360px 1fr;
  gap: 2rem;
}

@media (max-width: 960px) {
  .simulator-layout { grid-template-columns: 1fr; }
}

.simulator-controls {
  background: var(--rr-blue-surface);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-md);
  padding: 1.5rem;
}

.slider-group {
  margin-bottom: 1.25rem;
}

.slider-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.4rem;
  font-size: 0.85rem;
  font-family: var(--font-heading);
  text-transform: uppercase;
  color: var(--text-muted);
}

.slider-val {
  font-family: var(--font-mono);
  color: var(--rr-pink-light);
  font-weight: 700;
}

.slider-input {
  width: 100%;
  accent-color: var(--rr-pink);
  height: 6px;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.1);
}

.simulator-results {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.gauge-display-box {
  background: var(--rr-blue-surface);
  border: 1px solid var(--rr-blue-border);
  border-radius: var(--radius-md);
  padding: 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.leverage-value-large {
  font-family: var(--font-heading);
  font-size: 3.5rem;
  font-weight: 900;
  line-height: 1;
  margin: 0.5rem 0;
  background: linear-gradient(90deg, #FFFFFF, var(--rr-pink));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.pressure-tier-pill {
  display: inline-block;
  padding: 0.4rem 1.25rem;
  border-radius: 9999px;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.tier-crucible { background: rgba(239, 68, 68, 0.2); border: 1px solid var(--accent-red); color: #FCA5A5; }
.tier-high { background: rgba(245, 158, 11, 0.2); border: 1px solid var(--rr-gold); color: #FDE68A; }
.tier-moderate { background: rgba(6, 182, 212, 0.2); border: 1px solid var(--accent-cyan); color: #A5F3FC; }
.tier-low { background: rgba(16, 185, 129, 0.2); border: 1px solid var(--accent-green); color: #A7F3D0; }

/* Auction War Room & Squad Builder */
.auction-budget-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.budget-widget {
  background: rgba(5, 11, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-sm);
  padding: 1rem;
}

.budget-widget-title {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  font-family: var(--font-heading);
}

.budget-widget-num {
  font-size: 1.75rem;
  font-weight: 800;
  font-family: var(--font-heading);
  color: var(--text-main);
}

.squad-builder-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

@media (max-width: 960px) {
  .squad-builder-grid { grid-template-columns: 1fr; }
}

.rr-xi-pitch {
  background: linear-gradient(180deg, #0c2d1b 0%, #06190e 100%);
  border: 2px solid rgba(16, 185, 129, 0.3);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  position: relative;
  min-height: 480px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.pitch-slot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.4rem 0.85rem;
  border-radius: 6px;
  margin-bottom: 0.4rem;
  font-size: 0.82rem;
}

.pitch-slot.bought {
  border-color: var(--rr-pink);
  background: rgba(231, 56, 149, 0.2);
}

/* Methodology Equations */
.equation-box {
  background: rgba(5, 11, 20, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  padding: 1.25rem 1.75rem;
  margin: 1.25rem 0;
  font-family: var(--font-mono);
  color: #F1F5F9;
  font-size: 0.95rem;
  border-left: 4px solid var(--rr-pink);
}

/* Auction Live Recommendations & Dynamic Prediction Panel */
.auction-predictions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin-top: 1.5rem;
}

.prediction-card {
  background: rgba(5, 11, 20, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.prediction-card.affordable {
  border-left: 4px solid var(--accent-green);
}

.prediction-card.stretch {
  border-left: 4px solid var(--rr-gold);
}

.prediction-card.unaffordable {
  border-left: 4px solid var(--accent-red);
  opacity: 0.65;
}

.prediction-badge {
  display: inline-block;
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.7rem;
  font-family: var(--font-mono);
  font-weight: 700;
  text-transform: uppercase;
}

.prediction-badge.green { background: rgba(16, 185, 129, 0.2); color: var(--accent-green); }
.prediction-badge.gold { background: rgba(245, 158, 11, 0.2); color: var(--rr-gold); }
.prediction-badge.red { background: rgba(239, 68, 68, 0.2); color: #FCA5A5; }

/* Custom Price Input Modal */
.price-modal-box {
  background: var(--rr-blue);
  border: 2px solid var(--rr-pink);
  box-shadow: 0 0 50px var(--rr-pink-glow);
  border-radius: var(--radius-lg);
  max-width: 480px;
  width: 100%;
  padding: 2rem;
  position: relative;
  text-align: center;
  animation: modalScale 0.2s ease;
}

.price-input-field {
  width: 100%;
  background: rgba(5, 11, 20, 0.9);
  border: 2px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-sm);
  padding: 0.85rem 1rem;
  font-size: 1.75rem;
  font-family: var(--font-mono);
  font-weight: 800;
  color: var(--rr-gold);
  text-align: center;
  margin: 1.25rem 0;
  outline: none;
  transition: border-color 0.2s;
}

.price-input-field:focus {
  border-color: var(--rr-pink);
  box-shadow: 0 0 15px var(--rr-pink-glow);
}

.price-preset-chips {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.preset-chip {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--text-main);
  padding: 0.35rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-family: var(--font-mono);
  cursor: pointer;
  transition: all 0.2s;
}

.preset-chip:hover {
  background: var(--rr-pink);
  color: white;
  border-color: var(--rr-pink);
}

/* Footer Styles */
footer.app-footer {
  margin-top: 3rem;
  background: rgba(5, 11, 20, 0.95);
  border-top: 1px solid var(--rr-blue-border);
  padding: 3rem 2rem 2rem;
  backdrop-filter: blur(16px);
}

.footer-inner {
  max-width: 1500px;
  margin: 0 auto;
}

.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 2.5rem;
  padding-bottom: 2.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

@media (max-width: 900px) {
  .footer-top {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.footer-brand h2 {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 800;
  color: white;
  letter-spacing: 0.5px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.footer-brand p {
  font-size: 0.85rem;
  color: var(--text-muted);
  line-height: 1.6;
  max-width: 480px;
}

.footer-col h4 {
  font-family: var(--font-heading);
  font-size: 1rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--rr-pink-light);
  letter-spacing: 1px;
  margin-bottom: 1rem;
}

.footer-col ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer-col ul li a, .footer-col ul li span {
  color: var(--text-muted);
  font-size: 0.85rem;
  text-decoration: none;
  transition: color 0.2s;
  cursor: pointer;
}

.footer-col ul li a:hover {
  color: var(--rr-pink-light);
}

.footer-analyst-badge {
  background: rgba(231, 56, 149, 0.1);
  border: 1px solid var(--rr-pink);
  border-radius: var(--radius-sm);
  padding: 0.85rem 1.25rem;
  margin-top: 0.75rem;
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
}

.analyst-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--rr-pink) 0%, var(--rr-gold) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 1.2rem;
  color: #000;
}

.analyst-info-name {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1.15rem;
  color: #FFFFFF;
  line-height: 1.1;
}

.analyst-info-sub {
  font-size: 0.75rem;
  color: var(--rr-pink-light);
}

.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 1.75rem;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.8rem;
  color: var(--text-dim);
}

.footer-bottom .rr-motto {
  color: var(--rr-gold);
  font-family: var(--font-heading);
  font-weight: 700;
  letter-spacing: 1px;
}

/* Print Stylesheet for 1-Click Submission Report PDF */
@media print {
  body {
    background: #FFFFFF !important;
    color: #111827 !important;
    font-size: 11pt;
  }
  header.app-header,
  nav.app-nav,
  .controls-bar,
  .btn-export-pdf,
  .btn-card-action,
  .modal-backdrop,
  .view-toggle {
    display: none !important;
  }
  .tab-content {
    display: block !important;
    page-break-after: always;
  }
  .glass-section,
  .stat-card,
  .player-card {
    background: #FFFFFF !important;
    border: 1px solid #D1D5DB !important;
    box-shadow: none !important;
    color: #111827 !important;
    break-inside: avoid;
  }
  .stat-card-value,
  .section-title,
  .player-names h3 {
    color: #001E46 !important;
    -webkit-text-fill-color: initial !important;
  }
  table.data-table th {
    background: #F3F4F6 !important;
    color: #111827 !important;
    border-bottom: 2px solid #000 !important;
  }
  table.data-table td {
    border-bottom: 1px solid #E5E7EB !important;
    color: #111827 !important;
  }
  footer.app-footer {
    background: transparent !important;
    border-top: 2px solid #000 !important;
    color: #111827 !important;
    padding: 1.5rem 0 0 !important;
  }
  .footer-analyst-badge {
    border: 1px solid #111827 !important;
    background: #F3F4F6 !important;
  }
  .analyst-info-name {
    color: #001E46 !important;
  }
}
"""
