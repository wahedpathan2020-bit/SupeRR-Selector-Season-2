HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SupeRR Selector Season 2 | Rajasthan Royals IPL 2027 Auction War Room</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Outfit:wght@300;400;500;600;700;800;900&family=Rajdhani:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <style>
    {css_content}
  </style>
</head>
<body>

  <!-- Header & Navigation -->
  <header class="app-header">
    <div class="header-top">
      <div class="brand-container">
        <div class="rr-crest-badge">RR</div>
        <div class="brand-text">
          <h1>SupeRR Selector <span style="font-size: 0.9rem; background: var(--rr-pink); color: white; padding: 0.15rem 0.5rem; border-radius: 4px; font-weight: 800; letter-spacing: 1px;">SEASON 2</span></h1>
          <p>Rajasthan Royals War Room • IPL 2027 Pressure Analytics & Auction Strategy</p>
        </div>
      </div>

      <div class="header-status-pills">
        <div class="status-pill highlight">
          <span class="pulse-dot"></span>
          <span>LIVE WAR ROOM AUDIT</span>
        </div>
        <div class="status-pill gold">
          <span>IPL 2027 PURSE: ₹120.0 CR</span>
        </div>
        <div class="status-pill">
          <span>ROUND 1: CLUTCH RELIABILITY</span>
        </div>
        <button class="btn-export-pdf" onclick="exportSubmissionPDF()">
          <span>🖨️ Export Report / PDF</span>
        </button>
      </div>
    </div>

    <!-- Nav Tabs -->
    <nav class="app-nav">
      <button class="nav-tab-btn active" data-tab="overview">🏟️ War Room Overview</button>
      <button class="nav-tab-btn" data-tab="batters">🏏 Top 10 Batters</button>
      <button class="nav-tab-btn" data-tab="bowlers">🎯 Top 10 Bowlers</button>
      <button class="nav-tab-btn" data-tab="compare">⚔️ Head-to-Head Compare</button>
      <button class="nav-tab-btn" data-tab="simulator">⚡ Match Pressure Simulator</button>
      <button class="nav-tab-btn" data-tab="auction">💰 RR Auction Squad Builder</button>
      <button class="nav-tab-btn" data-tab="methodology">📐 Pressure Methodology</button>
      <button class="nav-tab-btn" data-tab="validation">🔬 Reliability & Validation</button>
    </nav>
  </header>

  <!-- Main Dashboard Container -->
  <main class="dashboard-container">

    <!-- Key Metrics Stats Banner (Visible across tabs) -->
    <div class="stats-banner-grid">
      <div class="stat-card">
        <div class="stat-card-title">Ball-By-Ball Dataset</div>
        <div class="stat-card-value">200,999</div>
        <div class="stat-card-sub">766 T20I & IPL matches (2022-2026)</div>
      </div>
      <div class="stat-card gold">
        <div class="stat-card-title">High-Pressure Deliveries</div>
        <div class="stat-card-value">28,264</div>
        <div class="stat-card-sub">Top Quartile Leverage (L ≥ 2.47 win-pts)</div>
      </div>
      <div class="stat-card green">
        <div class="stat-card-title">Chase Model Accuracy</div>
        <div class="stat-card-value">0.89 AUC</div>
        <div class="stat-card-sub">5-Fold Out-of-fold Calibrated GBDT</div>
      </div>
      <div class="stat-card cyan">
        <div class="stat-card-title">Eligible Player Pool</div>
        <div class="stat-card-value">105 Bat / 111 Bowl</div>
        <div class="stat-card-sub">≥80 clutch balls across ≥12 matches</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-title">RR Available Purse</div>
        <div class="stat-card-value" id="top-bar-purse">₹120.0 Cr</div>
        <div class="stat-card-sub">Targeting 4-5 High Clutch Assets</div>
      </div>
    </div>

    <!-- ================= TAB 1: WAR ROOM OVERVIEW ================= -->
    <div class="tab-content active" id="tab-overview">
      <div class="glass-section" style="background: linear-gradient(135deg, rgba(231, 56, 149, 0.12) 0%, rgba(10, 25, 47, 0.9) 100%);">
        <div class="section-header">
          <div>
            <h2 class="section-title">
              <span class="icon">👑</span> Rajasthan Royals IPL 2027 Auction Blueprint
            </h2>
            <p class="section-subtitle">
              Proprietary war-room intelligence identifying who delivers when the game is on the line.
            </p>
          </div>
          <span class="status-pill highlight">Halla Bol Under Pressure</span>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
          <div style="background: rgba(5, 11, 20, 0.6); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--rr-pink);">
            <h3 style="font-family: var(--font-heading); font-size: 1.2rem; color: white; margin-bottom: 0.5rem;">Why Traditional Stats Lie</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
              Standard strike rates reward low-leverage run accumulations (e.g. 40 off 20 in an easy chase of 120). Conversely, standard bowling economies hide garbage-time overs. Our <strong>Win Probability Added (WPA)</strong> framework credits performance strictly relative to the win-equity swing at stake on every individual delivery.
            </p>
          </div>

          <div style="background: rgba(5, 11, 20, 0.6); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--rr-gold);">
            <h3 style="font-family: var(--font-heading); font-size: 1.2rem; color: white; margin-bottom: 0.5rem;">The Jaipur Home Fortress Factor</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
              Sawai Mansingh Stadium features large square boundaries (75m+) and surfaces that decelerate in middle overs. RR requires spinners with flat trajectories who force mishits (Axar Patel, Krunal Pandya) and batters who hit true 85m+ maximums or possess elite placement (Buttler, Klaasen, Mitchell).
            </p>
          </div>

          <div style="background: rgba(5, 11, 20, 0.6); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--accent-cyan);">
            <h3 style="font-family: var(--font-heading); font-size: 1.2rem; color: white; margin-bottom: 0.5rem;">The Tri-Factor Composite Index</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
              Rankings do not rely on reputation. Every player is evaluated on a rigorous composite: <strong>50% Opponent-Adjusted Impact</strong> (via joint ridge regression), <strong>25% Resilience</strong> (z-score vs own baseline), and <strong>25% Consistency</strong> (Beta-shrunk share of positive matches).
            </p>
          </div>
        </div>
      </div>

      <!-- Verified Roster Intelligence: Sanju Samson in CSK & RR Rebuild -->
      <div class="glass-section" style="border: 1px solid var(--rr-gold); background: linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(10, 25, 47, 0.95) 100%); margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-size: 1.75rem;">🔄</span>
            <div>
              <h3 style="font-family: var(--font-heading); font-size: 1.35rem; color: var(--rr-gold); text-transform: uppercase; line-height: 1.1;">
                Verified Roster Intelligence: Sanju Samson in CSK & The Post-Samson Rebuild
              </h3>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">
                Proprietary Dataset Audit: Sanju Samson represented Chennai Super Kings in IPL 2026; Riyan Parag took over RR Captaincy and Ravindra Jadeja returned to Rajasthan.
              </p>
            </div>
          </div>
          <span class="status-pill gold">2026 Roster Reality</span>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; font-size: 0.85rem; line-height: 1.5; color: #E2E8F0;">
          <div style="background: rgba(5, 11, 20, 0.6); padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--rr-pink);">
            <strong style="color: white;">1. The Massive #3 & Wicketkeeping Void:</strong><br>
            With Sanju Samson at CSK in 2026, Rajasthan lost their premier top-order anchor and wicketkeeper. This elevates <strong>Jos Buttler (Rank 1)</strong>, <strong>Heinrich Klaasen (Rank 5)</strong>, and <strong>Phil Salt (Rank 6)</strong> from luxury acquisitions to <em>essential priority targets</em> to take back the gloves and explosive top-order scoring.
          </div>
          <div style="background: rgba(5, 11, 20, 0.6); padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--accent-cyan);">
            <strong style="color: white;">2. Riyan Parag's Captaincy Spine:</strong><br>
            Riyan Parag captained RR in 14 matches during IPL 2026 (with Yashasvi Jaiswal as VC). In high-pressure playoff chases, Parag needs senior tactical support. Re-acquiring <strong>Jos Buttler</strong>, <strong>Axar Patel</strong>, or <strong>Ravichandran Ashwin</strong> gives Parag a battle-hardened leadership spine.
          </div>
          <div style="background: rgba(5, 11, 20, 0.6); padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--accent-green);">
            <strong style="color: white;">3. Ravindra Jadeja's Home Reunion:</strong><br>
            With Ravindra Jadeja returning to Rajasthan Royals in 2026, RR already possesses elite left-arm control at SMS Stadium. Adding <strong>Axar Patel (Rank 1 Bowler)</strong> or <strong>Kuldeep Yadav (Rank 4)</strong> forms an impenetrable middle-overs spin choke.
          </div>
        </div>
      </div>

      <!-- Quick Rankings Summary Grid -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
        <!-- Batters Summary -->
        <div class="glass-section">
          <div class="section-header">
            <h3 class="section-title"><span class="icon">🏏</span> Top 10 Batters Under Pressure</h3>
            <button class="nav-tab-btn" onclick="switchTab('batters')" style="font-size:0.8rem; padding:0.3rem 0.75rem;">View Full Table →</button>
          </div>
          <div style="height: 280px;">
            <canvas id="overview-batters-chart"></canvas>
          </div>
          <div style="margin-top: 1rem; font-size: 0.82rem; color: var(--text-muted);">
            👑 <strong>Top Pick:</strong> Jos Buttler (+9.4 Impact, +3.28 Resilience, 184 Pressure SR vs 153 usual).
          </div>
        </div>

        <!-- Bowlers Summary -->
        <div class="glass-section">
          <div class="section-header">
            <h3 class="section-title"><span class="icon">🎯</span> Top 10 Bowlers Under Pressure</h3>
            <button class="nav-tab-btn" onclick="switchTab('bowlers')" style="font-size:0.8rem; padding:0.3rem 0.75rem;">View Full Table →</button>
          </div>
          <div style="height: 280px;">
            <canvas id="overview-bowlers-chart"></canvas>
          </div>
          <div style="margin-top: 1rem; font-size: 0.82rem; color: var(--text-muted);">
            👑 <strong>Top Pick:</strong> Axar Patel (+8.4 Impact, +2.24 Resilience, 7.98 Pressure Economy across 436 balls).
          </div>
        </div>
      </div>

      <!-- Executive Recommendations for RR 2027 Auction -->
      <div class="glass-section">
        <h3 class="section-title" style="margin-bottom: 1.25rem;">
          <span class="icon">🎯</span> Rajasthan Royals War Room Action Plan: 4 Strategic Targets
        </h3>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem;">
          <div style="background: rgba(18, 38, 68, 0.6); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid rgba(231, 56, 149, 0.25);">
            <span class="tier-badge marquee">Target 1 • Marquee Re-Acquisition</span>
            <h4 style="font-family: var(--font-heading); font-size: 1.3rem; color: white; margin: 0.5rem 0;">Jos Buttler (WK / Opener)</h4>
            <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
              Rank 1 batter in world cricket under pressure. SR elevates from 153 to 184 (+31) in clutch situations. Crucial talisman alongside Yashasvi Jaiswal.
            </p>
            <div style="margin-top: 0.75rem; font-family: var(--font-mono); color: var(--rr-gold); font-size: 0.85rem; font-weight: 700;">
              Valuation: ₹14.0 - 18.0 Cr
            </div>
          </div>

          <div style="background: rgba(18, 38, 68, 0.6); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid rgba(6, 182, 212, 0.25);">
            <span class="tier-badge marquee">Target 2 • Middle Overs Squeeze</span>
            <h4 style="font-family: var(--font-heading); font-size: 1.3rem; color: white; margin: 0.5rem 0;">Axar Patel (All-Rounder)</h4>
            <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
              Rank 1 pressure bowler with 436 legal clutch deliveries. Concedes only 7.98 RPO in high pressure. Lengthens batting at #7.
            </p>
            <div style="margin-top: 0.75rem; font-family: var(--font-mono); color: var(--accent-cyan); font-size: 0.85rem; font-weight: 700;">
              Valuation: ₹12.0 - 15.0 Cr
            </div>
          </div>

          <div style="background: rgba(18, 38, 68, 0.6); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid rgba(245, 158, 11, 0.25);">
            <span class="tier-badge tactical">Target 3 • Death Overs Finisher</span>
            <h4 style="font-family: var(--font-heading); font-size: 1.3rem; color: white; margin: 0.5rem 0;">Tim David (Finisher)</h4>
            <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
              Highest raw Impact rating in tournament (+9.5). Sustains a staggering 179 SR under fire. Partners Hetmyer to solve RR's 12+ RPO chases.
            </p>
            <div style="margin-top: 0.75rem; font-family: var(--font-mono); color: var(--rr-gold); font-size: 0.85rem; font-weight: 700;">
              Valuation: ₹9.0 - 12.5 Cr
            </div>
          </div>

          <div style="background: rgba(18, 38, 68, 0.6); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid rgba(16, 185, 129, 0.25);">
            <span class="tier-badge steal">Target 4 • Moneyball Steal</span>
            <h4 style="font-family: var(--font-heading); font-size: 1.3rem; color: white; margin: 0.5rem 0;">Taskin Ahmed / Krunal Pandya</h4>
            <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
              Taskin holds the best fast-bowling pressure economy (6.78 RPO) and 38% dots; Krunal's economy improves by -1.12 in clutch. Huge value buys.
            </p>
            <div style="margin-top: 0.75rem; font-family: var(--font-mono); color: var(--accent-green); font-size: 0.85rem; font-weight: 700;">
              Valuation: ₹3.0 - 6.0 Cr
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= TAB 2: TOP 10 BATTERS ================= -->
    <div class="tab-content" id="tab-batters">
      <div class="glass-section">
        <div class="section-header">
          <div>
            <h2 class="section-title"><span class="icon">🏏</span> Top 10 Batters Under Pressure</h2>
            <p class="section-subtitle">Ranked by Composite Index (50% Opponent-Adjusted Impact + 25% Resilience + 25% Consistency)</p>
          </div>

          <div class="view-toggle">
            <button class="view-toggle-btn active" id="batter-btn-cards" onclick="setBatterView('cards')">Cards View</button>
            <button class="view-toggle-btn" id="batter-btn-table" onclick="setBatterView('table')">Data Table</button>
          </div>
        </div>

        <!-- Controls: Search & Filters -->
        <div class="controls-bar">
          <div class="search-input-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" id="batter-search" placeholder="Search batter, country, or role..." oninput="renderBatters()">
          </div>

          <div class="filter-group">
            <span class="filter-label">Role:</span>
            <select class="filter-select" id="batter-role-filter" onchange="renderBatters()">
              <option value="all">All Roles</option>
              <option value="opener">Openers</option>
              <option value="middle">Middle Order</option>
              <option value="finisher">Finishers</option>
              <option value="allrounder">All-Rounders</option>
            </select>
          </div>

          <div class="filter-group">
            <span class="filter-label">Auction Tier:</span>
            <select class="filter-select" id="batter-tier-filter" onchange="renderBatters()">
              <option value="all">All Tiers</option>
              <option value="tier 1">Tier 1 Marquee</option>
              <option value="tier 2">Tier 2 Tactical</option>
              <option value="tier 3">Tier 3 Smart Steal</option>
            </select>
          </div>

          <div class="filter-group">
            <span class="filter-label">Sort By:</span>
            <select class="filter-select" id="batter-sort" onchange="renderBatters()">
              <option value="rank">Rank (1 to 10)</option>
              <option value="impact">Impact WPA (High to Low)</option>
              <option value="resilience">Resilience Lift (High to Low)</option>
              <option value="consistency">Consistency %</option>
              <option value="sr_pressure">Pressure Strike Rate</option>
              <option value="balls">Pressure Sample Deliveries</option>
            </select>
          </div>
        </div>

        <!-- Batters Cards Grid -->
        <div class="player-cards-grid" id="batters-cards-container">
          <!-- Populated by JS -->
        </div>

        <!-- Batters Table View -->
        <div class="table-responsive" id="batters-table-container" style="display: none; margin-top: 1rem;">
          <table class="data-table">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Player</th>
                <th>Role</th>
                <th>Pressure Balls</th>
                <th>Impact (WPA/100)</th>
                <th>Resilience (z)</th>
                <th>Consistency</th>
                <th>Pressure SR</th>
                <th>Usual SR</th>
                <th>SR Delta</th>
                <th>Dismissal Freq</th>
                <th>Auction Target</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="batters-table-body">
              <!-- Populated by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ================= TAB 3: TOP 10 BOWLERS ================= -->
    <div class="tab-content" id="tab-bowlers">
      <div class="glass-section">
        <div class="section-header">
          <div>
            <h2 class="section-title"><span class="icon">🎯</span> Top 10 Bowlers Under Pressure</h2>
            <p class="section-subtitle">Ranked by Composite Index (50% Opponent-Adjusted Impact + 25% Resilience + 25% Consistency)</p>
          </div>

          <div class="view-toggle">
            <button class="view-toggle-btn active" id="bowler-btn-cards" onclick="setBowlerView('cards')">Cards View</button>
            <button class="view-toggle-btn" id="bowler-btn-table" onclick="setBowlerView('table')">Data Table</button>
          </div>
        </div>

        <!-- Controls: Search & Filters -->
        <div class="controls-bar">
          <div class="search-input-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" id="bowler-search" placeholder="Search bowler, country, or type..." oninput="renderBowlers()">
          </div>

          <div class="filter-group">
            <span class="filter-label">Type:</span>
            <select class="filter-select" id="bowler-type-filter" onchange="renderBowlers()">
              <option value="all">All Types</option>
              <option value="spin">Spin Bowlers</option>
              <option value="pace">Pace Bowlers</option>
            </select>
          </div>

          <div class="filter-group">
            <span class="filter-label">Auction Tier:</span>
            <select class="filter-select" id="bowler-tier-filter" onchange="renderBowlers()">
              <option value="all">All Tiers</option>
              <option value="tier 1">Tier 1 Marquee</option>
              <option value="tier 2">Tier 2 Tactical</option>
              <option value="tier 3">Tier 3 Smart Steal</option>
            </select>
          </div>

          <div class="filter-group">
            <span class="filter-label">Sort By:</span>
            <select class="filter-select" id="bowler-sort" onchange="renderBowlers()">
              <option value="rank">Rank (1 to 10)</option>
              <option value="impact">Impact WPA (High to Low)</option>
              <option value="resilience">Resilience Lift (High to Low)</option>
              <option value="consistency">Consistency %</option>
              <option value="econ_pressure">Pressure Economy (Lowest First)</option>
              <option value="wickets">Strike Rate (Balls per Wicket)</option>
            </select>
          </div>
        </div>

        <!-- Bowlers Cards Grid -->
        <div class="player-cards-grid" id="bowlers-cards-container">
          <!-- Populated by JS -->
        </div>

        <!-- Bowlers Table View -->
        <div class="table-responsive" id="bowlers-table-container" style="display: none; margin-top: 1rem;">
          <table class="data-table">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Player</th>
                <th>Role</th>
                <th>Pressure Deliveries</th>
                <th>Impact (WPA/100)</th>
                <th>Resilience (z)</th>
                <th>Consistency</th>
                <th>Pressure Econ</th>
                <th>Usual Econ</th>
                <th>Econ Delta</th>
                <th>Strike Rate</th>
                <th>Dot Ball %</th>
                <th>Auction Target</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="bowlers-table-body">
              <!-- Populated by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ================= TAB 4: HEAD TO HEAD COMPARE ================= -->
    <div class="tab-content" id="tab-compare">
      <div class="glass-section">
        <div class="section-header">
          <div>
            <h2 class="section-title"><span class="icon">⚔️</span> Head-to-Head Player Comparison Matrix</h2>
            <p class="section-subtitle">Multi-dimensional radar analysis across Impact, Resilience, Consistency, Rate, and Stability.</p>
          </div>
          <div class="filter-group">
            <span class="filter-label">Category:</span>
            <select class="filter-select" id="compare-category">
              <option value="batters">Compare Batters</option>
              <option value="bowlers">Compare Bowlers</option>
            </select>
          </div>
        </div>

        <div class="compare-grid" style="margin-bottom: 2rem;">
          <div class="compare-selector-box" style="border-left: 4px solid var(--rr-pink);">
            <div style="font-size:0.75rem; text-transform:uppercase; color:var(--rr-pink-light); font-weight:700;">Select Player A</div>
            <select class="filter-select" id="compare-player-a" style="width:100%; margin-top:0.5rem; font-size:1rem; padding:0.75rem;"></select>
          </div>

          <div class="compare-selector-box" style="border-left: 4px solid var(--accent-cyan);">
            <div style="font-size:0.75rem; text-transform:uppercase; color:var(--accent-cyan); font-weight:700;">Select Player B</div>
            <select class="filter-select" id="compare-player-b" style="width:100%; margin-top:0.5rem; font-size:1rem; padding:0.75rem;"></select>
          </div>
        </div>

        <!-- Radar Chart Container -->
        <div class="glass-section" style="padding:1.5rem; height:420px; position:relative; margin-bottom:2rem;">
          <canvas id="compare-radar-chart"></canvas>
        </div>

        <!-- Detailed Side-by-Side Comparison Table -->
        <div class="table-responsive" id="compare-stats-table">
          <!-- Populated by JS -->
        </div>
      </div>
    </div>

    <!-- ================= TAB 5: MATCH PRESSURE SIMULATOR ================= -->
    <div class="tab-content" id="tab-simulator">
      <div class="glass-section">
        <div class="section-header">
          <div>
            <h2 class="section-title"><span class="icon">⚡</span> Live Match Pressure & Leverage Simulator</h2>
            <p class="section-subtitle">Dynamic calculation of Win Probability, Ball-by-Ball Leverage, and optimal RR player selection.</p>
          </div>
          <span class="status-pill highlight">GBDT Calibrated (0.89 AUC)</span>
        </div>

        <div class="simulator-layout">
          <!-- Controls Panel -->
          <div class="simulator-controls">
            <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:white; margin-bottom:1.25rem;">
              🎛️ Match State Inputs
            </h3>

            <div class="slider-group">
              <div class="slider-header">
                <span>Innings Phase</span>
              </div>
              <select class="filter-select" id="sim-innings" style="width:100%; padding:0.6rem;">
                <option value="2">2nd Innings (Chasing Target)</option>
                <option value="1">1st Innings (Setting Target)</option>
              </select>
            </div>

            <div class="slider-group">
              <div class="slider-header">
                <span>Target Runs</span>
                <span class="slider-val" id="val-sim-target">190</span>
              </div>
              <input type="range" class="slider-input" id="sim-target" min="120" max="240" step="1" value="190">
            </div>

            <div class="slider-group">
              <div class="slider-header">
                <span>Current Score</span>
                <span class="slider-val" id="val-sim-score">140</span>
              </div>
              <input type="range" class="slider-input" id="sim-score" min="40" max="230" step="1" value="140">
            </div>

            <div class="slider-group">
              <div class="slider-header">
                <span>Overs Completed</span>
                <span class="slider-val" id="val-sim-overs">16.0</span>
              </div>
              <input type="range" class="slider-input" id="sim-overs" min="3.0" max="19.5" step="0.1" value="16.0">
            </div>

            <div class="slider-group">
              <div class="slider-header">
                <span>Wickets Lost</span>
                <span class="slider-val" id="val-sim-wickets">4</span>
              </div>
              <input type="range" class="slider-input" id="sim-wickets" min="0" max="9" step="1" value="4">
            </div>

            <div style="background:rgba(5,11,20,0.5); padding:0.85rem; border-radius:6px; border:1px solid rgba(255,255,255,0.06); font-size:0.78rem; color:var(--text-muted); line-height:1.4;">
              💡 <em>Threshold Rule: High pressure is flagged when Leverage ≥ 2.47 win-pts, Win Prob is 20%-80%, and Overs ≥ 3.</em>
            </div>
          </div>

          <!-- Real-Time Results & Dial Panel -->
          <div class="simulator-results">
            <div class="gauge-display-box">
              <div style="font-size:0.85rem; text-transform:uppercase; color:var(--text-muted); font-family:var(--font-heading); letter-spacing:1px;">
                Instant Ball Leverage Index
              </div>
              <div class="leverage-value-large" id="sim-leverage-display">3.64</div>
              <div style="font-size:0.8rem; color:var(--text-dim); margin-bottom:1rem;">Expected Absolute Win-Probability Swing Per Ball (Win-Pts)</div>

              <div id="sim-tier-display" class="pressure-tier-pill tier-high">HIGH PRESSURE (Q3 THRESHOLD)</div>
              <p id="sim-tier-desc" style="font-size:0.85rem; color:var(--text-muted); margin-top:0.75rem;">
                Qualifies into the 28,264 official high-pressure deliveries dataset.
              </p>

              <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin-top:1.5rem; padding-top:1.25rem; border-top:1px solid rgba(255,255,255,0.08);">
                <div>
                  <div style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">Required Run Rate</div>
                  <div style="font-size:1.5rem; font-weight:800; color:var(--rr-gold); font-family:var(--font-mono);" id="sim-rrr-display">12.50</div>
                </div>
                <div>
                  <div style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">Batting Win Prob</div>
                  <div style="font-size:1.5rem; font-weight:800; color:var(--accent-green); font-family:var(--font-mono);" id="sim-wp-bat">46.2%</div>
                </div>
                <div>
                  <div style="font-size:0.7rem; color:var(--text-muted); text-transform:uppercase;">Bowling Win Prob</div>
                  <div style="font-size:1.5rem; font-weight:800; color:var(--accent-cyan); font-family:var(--font-mono);" id="sim-wp-bowl">53.8%</div>
                </div>
              </div>
            </div>

            <!-- Contextual Tactical Recommendation -->
            <div id="sim-recommendation-box">
              <!-- Populated by JS -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= TAB 6: AUCTION WAR ROOM & SQUAD BUILDER ================= -->
    <div class="tab-content" id="tab-auction">
      <div class="glass-section">
        <div class="section-header">
          <div>
            <h2 class="section-title"><span class="icon">💰</span> Rajasthan Royals IPL 2027 Auction War Room</h2>
            <p class="section-subtitle">Simulate real-time purse allocations (₹120 Cr budget) and build Rajasthan Royals' invincible clutch squad.</p>
          </div>
          <span class="status-pill gold">Auction Ceiling: ₹120.0 Cr</span>
        </div>

        <!-- Budget & Roster Dashboard -->
        <div class="auction-budget-bar">
          <div class="budget-widget" style="border-left: 3px solid var(--accent-green);">
            <div class="budget-widget-title">Purse Remaining</div>
            <div class="budget-widget-num" style="color:var(--accent-green);" id="auction-purse-remaining">₹120.0 Cr</div>
          </div>

          <div class="budget-widget" style="border-left: 3px solid var(--rr-pink);">
            <div class="budget-widget-title">Auction Spend</div>
            <div class="budget-widget-num" style="color:var(--rr-pink-light);" id="auction-purse-spent">₹0.0 Cr</div>
          </div>

          <div class="budget-widget" style="border-left: 3px solid var(--rr-gold);">
            <div class="budget-widget-title">Auction Targets Selected</div>
            <div class="budget-widget-num" style="color:var(--rr-gold);" id="auction-bought-count">0 Targets</div>
          </div>

          <div class="budget-widget" style="border-left: 3px solid var(--accent-cyan);">
            <div class="budget-widget-title">Overseas Slots Utilized</div>
            <div class="budget-widget-num" style="color:var(--accent-cyan);" id="auction-overseas-count">1 / 8 Allowed</div>
          </div>

          <div class="budget-widget" style="border-left: 3px solid #8B5CF6;">
            <div class="budget-widget-title">Overall Team Clutch Index</div>
            <div class="budget-widget-num" style="color:#C4B5FD;" id="auction-team-clutch">86 / 100</div>
          </div>
        </div>

        <!-- Squad Builder Grid: Bought Targets vs Simulated Playing XI -->
        <div class="squad-builder-grid">
          <!-- Targets in Draft -->
          <div class="glass-section" style="padding:1.25rem;">
            <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:white; margin-bottom:1rem; display:flex; justify-content:space-between; align-items:center;">
              <span>🛒 Drafted Auction Targets</span>
              <span style="font-size:0.75rem; color:var(--text-muted);">Use "+ Add to RR" on player cards</span>
            </h3>

            <div id="auction-bought-list" style="min-height:240px;">
              <!-- Populated by JS -->
            </div>
          </div>

          <!-- Simulated RR 2027 Playing XI Pitch -->
          <div class="glass-section" style="padding:1.25rem;">
            <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:white; margin-bottom:1rem; display:flex; justify-content:space-between; align-items:center;">
              <span>🏟️ Simulated RR 2027 Playing XI</span>
              <span class="status-pill highlight" style="font-size:0.7rem;">Jaipur SMS Fortress</span>
            </h3>

            <div class="rr-xi-pitch" id="simulated-rr-xi">
              <!-- Populated by JS -->
            </div>
          </div>
        </div>

        <!-- Dynamic Remaining Purse Predictions & Next Targets Advisory -->
        <div class="glass-section" style="margin-top: 1.5rem; background: rgba(18, 38, 68, 0.65); border: 1px solid var(--rr-blue-border);">
          <div class="section-header" style="margin-bottom: 0.75rem;">
            <div>
              <h3 class="section-title"><span class="icon">🔮</span> Real-Time Purse Feasibility & AI Next-Pick Predictions</h3>
              <p class="section-subtitle">Dynamically recalibrated as you enter winning bids. Shows what combinations of remaining top clutch players RR can still acquire with the remaining purse.</p>
            </div>
            <span class="status-pill gold" id="predictions-purse-pill">Purse Available: ₹120.0 Cr</span>
          </div>

          <div id="dynamic-auction-predictions-container" class="auction-predictions-grid">
            <!-- Populated dynamically by JS based on remaining purse -->
          </div>
        </div>
      </div>
    </div>

    <!-- ================= TAB 7: METHODOLOGY & MODEL ARCHITECTURE ================= -->
    <div class="tab-content" id="tab-methodology">
      <div class="glass-section">
        <div class="section-header">
          <div>
            <h2 class="section-title"><span class="icon">📐</span> Rigorous Quantitative Methodology</h2>
            <p class="section-subtitle">How pressure is defined, calibrated, and measured across 200,999 deliveries.</p>
          </div>
          <span class="status-pill highlight">Reproducible Pipeline</span>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.5rem; margin-bottom:2rem;">
          <div style="background:rgba(5,11,20,0.6); padding:1.5rem; border-radius:var(--radius-md); border-top:4px solid var(--rr-pink);">
            <h3 style="font-family:var(--font-heading); font-size:1.3rem; color:white; margin-bottom:0.75rem;">
              Stage 1: Out-of-Fold Win Probability
            </h3>
            <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5;">
              Trained separate gradient-boosted decision tree (GBDT) models for Innings 1 and Innings 2 across 766 completed IPL & T20I matches. Evaluated strictly via 5-fold match-grouped cross-validation so no match is scored by a model that saw it.
            </p>
            <div style="margin-top:0.75rem; font-size:0.8rem; color:var(--accent-green); font-family:var(--font-mono);">
              ✓ Chase Model AUC: 0.89 • Calibrated across all deciles
            </div>
          </div>

          <div style="background:rgba(5,11,20,0.6); padding:1.5rem; border-radius:var(--radius-md); border-top:4px solid var(--rr-gold);">
            <h3 style="font-family:var(--font-heading); font-size:1.3rem; color:white; margin-bottom:0.75rem;">
              Stage 2: Ball-by-Ball Leverage Index
            </h3>
            <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5;">
              Leverage quantifies the game-equity swing at stake. Computed as the expected absolute win-probability change across counterfactual outcomes weighted by empirical frequencies.
            </p>
            <div class="equation-box" style="margin:0.75rem 0; padding:0.75rem 1rem; font-size:0.85rem;">
              L_i = Σ P(k) · |WP(state | outcome k) - WP(state)|
            </div>
            <div style="font-size:0.8rem; color:var(--rr-gold); font-family:var(--font-mono);">
              ✓ High Pressure: L ≥ 2.47 win-pts, WP 20-80%, Over ≥ 3
            </div>
          </div>

          <div style="background:rgba(5,11,20,0.6); padding:1.5rem; border-radius:var(--radius-md); border-top:4px solid var(--accent-cyan);">
            <h3 style="font-family:var(--font-heading); font-size:1.3rem; color:white; margin-bottom:0.75rem;">
              Stage 3: Opponent-Adjusted Joint Ridge
            </h3>
            <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5;">
              Solves the quality-of-opposition challenge. A simultaneous ridge regression models every batter (+) and bowler (-). Batters facing Bumrah or Rashid Khan are credited accordingly, while ridge penalty applies empirical-Bayes shrinkage.
            </p>
            <div style="margin-top:0.75rem; font-size:0.8rem; color:var(--accent-cyan); font-family:var(--font-mono);">
              ✓ Prevents small-sample distortion • Shrinks noisy spikes
            </div>
          </div>
        </div>

        <!-- Composite Score Formula -->
        <div class="glass-section" style="background:rgba(18,38,68,0.7);">
          <h3 style="font-family:var(--font-heading); font-size:1.3rem; color:var(--rr-pink-light); text-transform:uppercase; margin-bottom:0.75rem;">
            The Tri-Factor Composite Scoring Formula
          </h3>
          <p style="font-size:0.88rem; color:#E2E8F0; margin-bottom:1rem;">
            Eligible players (≥80 high-pressure deliveries, ≥12 pressure matches, ≥8 qualifying innings/spells) are ranked by standardizing three orthogonal dimensions:
          </p>

          <div class="equation-box">
            Composite Score = 0.50 · z(Impact) + 0.25 · z(Resilience) + 0.25 · z(Consistency)
          </div>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1rem; margin-top:1.25rem;">
            <div>
              <strong style="color:var(--text-main); font-size:0.9rem;">1. Impact (50% Weight):</strong>
              <p style="font-size:0.82rem; color:var(--text-muted);">Opponent-adjusted Win Probability Added per 100 pressure deliveries. Measures pure winning contribution against tough opposition.</p>
            </div>
            <div>
              <strong style="color:var(--text-main); font-size:0.9rem;">2. Resilience (25% Weight):</strong>
              <p style="font-size:0.82rem; color:var(--text-muted);">Player's own baseline test. Difference between leverage captured in high pressure vs low-pressure baseline play. Rewards those who rise when things get tight.</p>
            </div>
            <div>
              <strong style="color:var(--text-main); font-size:0.9rem;">3. Consistency (25% Weight):</strong>
              <p style="font-size:0.82rem; color:var(--text-muted);">Beta-shrunk percentage of pressure innings or spells with non-negative WPA impact. Heavily penalizes single-game wonders.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= TAB 8: VALIDATION & RELIABILITY ================= -->
    <div class="tab-content" id="tab-validation">
      <div class="glass-section">
        <div class="section-header">
          <div>
            <h2 class="section-title"><span class="icon">🔬</span> Robustness, Bootstrap Stability & Limitations</h2>
            <p class="section-subtitle">Rigorous statistical verification and transparent franchise risk boundaries.</p>
          </div>
          <span class="status-pill highlight">60-Fold Bootstrap Verified</span>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem; margin-bottom:2rem;">
          <!-- Bootstrap Stability -->
          <div class="glass-section" style="padding:1.5rem;">
            <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:white; margin-bottom:0.75rem;">
              📊 60-Fold Match Bootstrap Retention
            </h3>
            <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.4; margin-bottom:1rem;">
              Matches resampled 60 times with replacement to test if ranking order survives random variance:
            </p>
            <div style="font-size:0.85rem; color:var(--text-main); line-height:1.8;">
              • <strong>Jos Buttler:</strong> 92% retention in Top 10<br>
              • <strong>Axar Patel:</strong> 89% retention in Top 10<br>
              • <strong>Tim David:</strong> 87% retention in Top 10<br>
              • <strong>Sunil Narine:</strong> 86% retention in Top 10<br>
              • <strong>Heinrich Klaasen:</strong> 84% retention in Top 10<br>
              • <strong>Kuldeep Yadav:</strong> 83% retention in Top 10<br>
              <span style="color:var(--text-dim); font-size:0.75rem;">Ranks 8-10 (Rinku, Ashwin, Taskin) retain at 65-72%, functioning as an interchangeable high-value tier.</span>
            </div>
          </div>

          <!-- Weight Sensitivity -->
          <div class="glass-section" style="padding:1.5rem;">
            <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:white; margin-bottom:0.75rem;">
              ⚖️ 9-Scheme Weight Sensitivity
            </h3>
            <p style="font-size:0.82rem; color:var(--text-muted); line-height:1.4; margin-bottom:1rem;">
              Evaluated across 9 alternative weighting regimes (including Impact-only, Equal Weights 33/33/33, and No-Consistency):
            </p>
            <div style="font-size:0.85rem; color:var(--text-main); line-height:1.8;">
              • <strong>Batter Top 10:</strong> Retains 8 to 10 of the identical names across all 9 schemes (Rank correlation &gt; 0.95).<br>
              • <strong>Bowler Top 10:</strong> Retains 7 to 10 identical names across all 9 schemes.<br>
              • <strong>Leverage Threshold Shift:</strong> Moving cutoff to Top 20% or Top 30% retains 9/10 batters and 8/10 bowlers.
            </div>
          </div>
        </div>

        <!-- Honest Persistence & Limitations -->
        <div class="glass-section" style="background:rgba(5,11,20,0.6);">
          <h3 style="font-family:var(--font-heading); font-size:1.2rem; color:var(--rr-pink-light); text-transform:uppercase; margin-bottom:0.75rem;">
            Honest Check on Persistence & Model Limitations
          </h3>
          <p style="font-size:0.85rem; color:var(--text-muted); line-height:1.5; margin-bottom:1rem;">
            Splitting matches into odd and even halves yields a rank correlation of ~0.17 for batters (n=94) and ~0.18 for bowlers (n=105), translating to ~0.30 under Spearman-Brown correction. This confirms a known truth in cricket analytics: <strong>pressure clutch is partially an innate skill and partially subject to high natural variance.</strong>
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1rem; font-size:0.82rem; color:var(--text-dim);">
            <div>
              <strong style="color:var(--text-main);">Innings 1 Coarseness:</strong> Without real-time pitch bounce data, the 1st innings model operates at 0.67 AUC vs 0.89 in chases.
            </div>
            <div>
              <strong style="color:var(--text-main);">Eligibility Cutoff:</strong> Players with &lt;80 clutch deliveries were omitted. Rising stars like Vaibhav Sooryavanshi placed at rank 11 due to small sample size.
            </div>
            <div>
              <strong style="color:var(--text-main);">Cross-League Transfer:</strong> IPL scoring environments are denser than bilateral T20Is; ridge adjustment controls for opposition but pitch nuances remain.
            </div>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- Application Footer -->
  <footer class="app-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <h2>
            <span style="color:var(--rr-pink);">👑</span> Rajasthan Royals SupeRR Selector
          </h2>
          <p>
            Official Round 1 submission: <strong>Identify the Most Reliable Players Under Pressure</strong>. A data-driven analytical framework shaping Rajasthan Royals' IPL 2027 Auction Strategy, calibrated on 200,999 delivery records across 766 matches.
          </p>
          <div class="footer-analyst-badge">
            <div class="analyst-avatar">WP</div>
            <div>
              <div class="analyst-info-name">Wahed Pathan</div>
              <div class="analyst-info-sub">Lead Data & Auction Strategy Analyst • SupeRR Selector S2</div>
            </div>
          </div>
        </div>

        <div class="footer-col">
          <h4>War Room Navigation</h4>
          <ul>
            <li><a onclick="switchTab('overview')">🏟️ Overview & Blueprint</a></li>
            <li><a onclick="switchTab('batters')">🏏 Top 10 Batters</a></li>
            <li><a onclick="switchTab('bowlers')">🎯 Top 10 Bowlers</a></li>
            <li><a onclick="switchTab('compare')">⚔️ Head-to-Head Compare</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Analytical Tools</h4>
          <ul>
            <li><a onclick="switchTab('simulator')">⚡ Match Pressure Simulator</a></li>
            <li><a onclick="switchTab('auction')">💰 RR Auction Squad Builder</a></li>
            <li><a onclick="switchTab('methodology')">📐 WPA & Leverage Model</a></li>
            <li><a onclick="switchTab('validation')">🔬 Bootstrap & Reliability</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Submission Details</h4>
          <ul>
            <li><span>Competition: SupeRR Selector S2</span></li>
            <li><span>Organizer: Rajasthan Royals</span></li>
            <li><span>Platform: Unstop Hackathon</span></li>
            <li><span>Round: 1 (Pressure Reliability)</span></li>
            <li><a onclick="exportSubmissionPDF()" style="color:var(--rr-gold); font-weight:700;">🖨️ Export Submission PDF</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          © 2026 Rajasthan Royals SupeRR Selector Season 2 • Prepared by <strong>Wahed Pathan</strong>. All rights reserved.
        </div>
        <div class="rr-motto">
          HALLA BOL! 👑 • JAIPUR HOME FORTRESS
        </div>
      </div>
    </div>
  </footer>

  <!-- Player Tactical Dossier Modal -->
  <div class="modal-backdrop" id="player-modal" onclick="if(event.target === this) closePlayerDossier()">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closePlayerDossier()">✕</button>
      <div id="modal-dossier-body">
        <!-- Populated dynamically by JS -->
      </div>
    </div>
  </div>

  <!-- Interactive Auction Live Bid Modal -->
  <div class="modal-backdrop" id="auction-bid-modal" onclick="if(event.target === this) closeBidModal()">
    <div class="price-modal-box">
      <button class="modal-close-btn" onclick="closeBidModal()">✕</button>
      <div style="font-size:0.75rem; text-transform:uppercase; color:var(--rr-pink-light); font-weight:700; letter-spacing:1px; margin-bottom:0.25rem;">
        🔨 LIVE AUCTION BID ENTRY
      </div>
      <h3 id="bid-modal-player-name" style="font-family:var(--font-heading); font-size:1.75rem; color:white; line-height:1.2; margin-bottom:0.25rem;">
        Player Name
      </h3>
      <div id="bid-modal-player-role" style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
        Role • Country
      </div>

      <div style="background:rgba(5,11,20,0.6); padding:0.75rem; border-radius:var(--radius-sm); border:1px solid rgba(255,255,255,0.06); margin-bottom:1rem; font-size:0.85rem;">
        <span style="color:var(--text-dim);">Current Remaining Purse:</span>
        <strong id="bid-modal-current-purse" style="color:var(--accent-green); font-family:var(--font-mono); margin-left:0.35rem;">₹120.0 Cr</strong>
      </div>

      <label for="bid-price-input" style="font-size:0.85rem; color:var(--text-muted); text-transform:uppercase; font-family:var(--font-heading); letter-spacing:0.5px;">
        Enter Winning Bid Amount (in ₹ Crore):
      </label>
      <input type="number" id="bid-price-input" class="price-input-field" step="0.25" min="0.5" max="120" placeholder="e.g. 14.5">

      <div class="price-preset-chips" id="bid-price-presets">
        <!-- Preset quick buttons populated dynamically -->
      </div>

      <div id="bid-error-msg" style="color:var(--accent-red); font-size:0.8rem; margin-bottom:1rem; min-height:1.2rem; font-weight:600;"></div>

      <div style="display:flex; gap:0.75rem;">
        <button class="btn-card-action" style="flex:1; padding:0.75rem;" onclick="closeBidModal()">
          Cancel
        </button>
        <button class="btn-export-pdf" style="flex:1; padding:0.75rem; justify-content:center;" onclick="confirmAuctionBid()">
          🔨 Confirm & Deduct Purse
        </button>
      </div>
    </div>
  </div>

  <!-- Raw Data & Scripts Injection -->
  <script>
    const RAW_DATA = {raw_data_json};
  </script>
  <script>
    {js_content}
  </script>
</body>
</html>
"""
