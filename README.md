<<<<<<< HEAD
# 👑 SupeRR Selector Season 2: Rajasthan Royals IPL 2027 Auction War Room

> **Author & Lead Analyst:** **Wahed Pathan**  
> **Round 1 Challenge:** Identify the Most Reliable Players Under Pressure  
> **Target Franchise:** Rajasthan Royals (IPL 2027 Auction Strategy)  
> **Dataset Analyzed:** 200,999 Ball-by-Ball Records across 766 Completed T20I & IPL Matches (2022–2026)  
> **High-Pressure Sample:** 28,264 Deliveries (Top-Quartile Leverage $L \ge 2.47$ win-pts, Win Prob 20–80%, Over $\ge 3$)  

---

## 🚀 Quick Start: Launch the Interactive Dashboard

You can explore the interactive War Room Web Application immediately:
1. **Double-click `run_dashboard.bat`** (or open `index.html` directly in any web browser).
2. Explore:
   - **🏟️ War Room Overview:** Executive summary, 4 core auction targets, and franchise tactical blueprint.
   - **🏏 Top 10 Batters Under Pressure:** Full stats, filter by role/tier, and detailed tactical dossiers.
   - **🎯 Top 10 Bowlers Under Pressure:** Economy reduction under pressure, strike rate, dot %, and dossiers.
   - **⚔️ Head-to-Head Compare:** Live multi-axis radar chart and differential matrix.
   - **⚡ Match Pressure Simulator:** Interactive match state sliders (Runs, Overs, Wickets, Target) computing dynamic Win Probability, Leverage Index, and optimal clutch player recommendations.
   - **💰 RR Auction War Room & Live Bid Simulator:** 
     - **Dynamic Bid Entry:** When drafting any player, an auction bid modal prompts you to enter the *exact winning bid price* (with quick base/mid/ceiling preset chips).
     - **Live Purse Deduction:** The entered amount is subtracted in real time from Rajasthan Royals' ₹120.0 Cr purse.
     - **Real-Time Remaining Purse AI Predictions:** Evaluates every remaining player against the newly updated balance, categorizing them as *Feasible Priority*, *Tight Purse / High Risk*, or *Purse Deficit*, with dynamic tactical advice for next picks.
   - **📐 Methodology & Mathematical Architecture:** 3-stage quantitative pipeline equations, leverage distribution, and calibration curves.
   - **🔬 Reliability & Validation:** 60-fold bootstrap stability, 9-scheme weight sensitivity, and split-half persistence.
   - **🖨️ Export Report / PDF:** 1-click browser export formatted for clean multi-page hackathon submission.

---

## 🏆 Official Round 1 Rankings (For Unstop Dropdowns)

Ensure these exact selections are chosen in rank order (1 to 10) on the Unstop submission portal:

### 🏏 Top 10 Batters Under Pressure
| Rank | Player | Pressure Balls | Impact (WPA/100) | Resilience ($z$) | Consistency (%) | Pressure SR vs Usual | Dismissal Freq | RR Auction Tier & Valuation |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **Jos Buttler** | 309 | **+9.4** | +3.28 | 60% | **184** / 153 (+31) | 1 in 28 balls | Tier 1 Marquee (₹14.0 - 18.0 Cr) |
| **2** | **Tim David** | 258 | **+9.5** | +2.06 | 64% | **179** / 179 (0) | 1 in 18 balls | Tier 1 Marquee (₹9.0 - 12.5 Cr) |
| **3** | **David Miller** | 227 | **+5.1** | +3.35 | 59% | **153** / 146 (+7) | **1 in 38 balls** | Tier 2 Tactical (₹6.0 - 8.5 Cr) |
| **4** | **Glenn Maxwell** | 159 | **+5.4** | **+4.56** | 45% | **161** / 161 (0) | 1 in 20 balls | Tier 2 Tactical (₹7.5 - 10.0 Cr) |
| **5** | **Heinrich Klaasen** | 231 | **+8.1** | +0.44 | 65% | **179** / 165 (+14) | 1 in 21 balls | Tier 1 Marquee (₹15.0 - 20.0 Cr) |
| **6** | **Phil Salt** | 178 | **+6.7** | +0.87 | 66% | **196** / 168 (+28) | 1 in 30 balls | Tier 1 Marquee (₹8.0 - 11.5 Cr) |
| **7** | **Daryl Mitchell** | 138 | **+5.4** | +0.82 | **72%** | **188** / 142 (+46) | **1 in 69 balls** | Tier 3 Smart Steal (₹4.5 - 7.0 Cr) |
| **8** | **Cameron Green** | 220 | **+6.1** | +1.33 | 59% | **170** / 150 (+20) | 1 in 22 balls | Tier 1 Marquee (₹10.0 - 13.5 Cr) |
| **9** | **Mohammad Rizwan** | 201 | **+4.9** | +0.73 | 62% | **139** / 125 (+14) | **1 in 50 balls** | Model Baseline Benchmark |
| **10** | **Rinku Singh** | 203 | **+3.7** | +2.26 | 54% | **141** / 153 (-12) | 1 in 34 balls | Tier 1 Marquee (₹9.0 - 13.0 Cr) |

---

### 🎯 Top 10 Bowlers Under Pressure
| Rank | Player | Pressure Deliveries | Impact (WPA/100) | Resilience ($z$) | Consistency (%) | Pressure Econ vs Usual | Strike Rate | Dot Ball % | RR Auction Tier & Valuation |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **Axar Patel** | 436 | **+8.4** | +2.24 | 68% | **7.98** / 7.97 | 1 in 26 balls | 33% | Tier 1 Marquee (₹12.0 - 15.0 Cr) |
| **2** | **Sunil Narine** | 297 | **+7.2** | +1.06 | 68% | **7.25** / 6.90 | 1 in 25 balls | 37% | Tier 1 Marquee (₹10.0 - 13.5 Cr) |
| **3** | **Krunal Pandya** | 225 | **+7.2** | +1.01 | 67% | **7.04** / 8.16 (**-1.12**) | 1 in 16 balls | 29% | Tier 2 Tactical (₹5.5 - 8.0 Cr) |
| **4** | **Kuldeep Yadav** | 292 | **+7.9** | +0.54 | 62% | **7.11** / 8.19 (**-1.08**) | **1 in 14 balls** | 31% | Tier 1 Marquee (₹11.0 - 14.5 Cr) |
| **5** | **Bhuvneshwar Kumar** | 272 | **+5.3** | **+2.75** | 56% | **9.64** / 8.34 | **1 in 13 balls** | 31% | Tier 3 Smart Steal (₹4.0 - 6.5 Cr) |
| **6** | **Ravindra Jadeja** | 240 | **+5.3** | +0.77 | 71% | **7.60** / 8.06 (-0.46) | 1 in 35 balls | 33% | Tier 1 Marquee (₹12.0 - 16.0 Cr) |
| **7** | **Josh Hazlewood** | 203 | **+5.6** | +1.75 | 56% | **8.72** / 8.55 | **1 in 13 balls** | **39%** | Tier 1 Marquee (₹8.5 - 12.0 Cr) |
| **8** | **Moeen Ali** | 125 | **+4.3** | +0.61 | **72%** | **7.06** / 8.67 (**-1.61**) | **1 in 12 balls** | 35% | Tier 3 Smart Steal (₹4.0 - 6.0 Cr) |
| **9** | **Taskin Ahmed** | 139 | **+4.4** | +1.04 | 68% | **6.78** / 8.56 (**-1.78**) | 1 in 16 balls | **38%** | Tier 3 Smart Steal (₹2.5 - 4.5 Cr) |
| **10** | **Ravichandran Ashwin** | 259 | **+4.7** | +0.83 | 67% | **7.97** / 7.88 | 1 in 27 balls | 28% | Tier 3 Smart Steal (₹3.5 - 5.5 Cr) |

---

## 🏰 Rajasthan Royals IPL 2027 Auction Strategy Blueprint

### 1. The 4 Key Tactical Roles RR Must Target:
1. **Marquee Re-Acquisition / Explosive Opener:** **Jos Buttler** (Rank 1 Batter). Pair with Yashasvi Jaiswal to maximize powerplay output and take scoring pressure off Sanju Samson. If price exceeds ₹17.5 Cr, pivot to **Phil Salt** (Rank 6, 196.0 Pressure SR).
2. **Indian Middle-Overs Spin Anchor:** **Axar Patel** (Rank 1 Bowler). Gives RR 4 tight overs (7.98 RPO in pressure) and bats at #7, creating batting depth. Budget alternative: **Krunal Pandya** (Rank 3 Bowler, 7.04 Pressure RPO).
3. **Pure Death-Overs Muscle:** **Tim David** (Rank 2 Batter). The highest raw Impact batter (+9.5 WPA) in cricket. Combines with Shimron Hetmyer and Dhruv Jurel to make 12+ RPO chases achievable.
4. **Moneyball Bowling Steal:** **Taskin Ahmed** (Rank 9 Bowler). Holds the lowest pressure economy among all fast bowlers (6.78 RPO) with 38% dot balls. Low auction price tag (₹3-4 Cr) leaves maximum purse for marquee Indian stars.

### 2. Verified Dataset Roster Insight: Sanju Samson in CSK & The Post-Samson Rebuild
In this proprietary dataset, an unexpected trade occurred ahead of **IPL 2026**:
- **Sanju Samson played for Chennai Super Kings (CSK)** (Row 5462 in `competition_team_player_mapping.csv`).
- **Ravindra Jadeja moved to Rajasthan Royals (RR)**.
- **Riyan Parag was appointed Rajasthan Royals Captain** (leading RR in 14 matches in IPL 2026, with Yashasvi Jaiswal as VC).
- **The Strategic Consequence for RR's IPL 2027 Auction:**
  1. **The Critical #3 & Wicketkeeping Void:** Samson's departure leaves Rajasthan without their primary Indian keeper-anchor. This elevates **Jos Buttler (Rank 1)**, **Heinrich Klaasen (Rank 5)**, and **Phil Salt (Rank 6)** into *essential priority targets* to take over wicketkeeping duties and top-order firepower.
  2. **Leadership Spine:** Captain Riyan Parag needs veteran tactical allies in high-pressure playoff matches. Re-acquiring **Jos Buttler** or **Axar Patel** provides this critical guidance.
  3. **Jadeja-Axar Spin Fortress:** With Ravindra Jadeja already at RR, acquiring **Axar Patel** or **Kuldeep Yadav** locks down Jaipur's large boundary outfield completely.

### 3. Sawai Mansingh Stadium (Jaipur Fortress) Adaptation:
- **Spacious Boundary Dimensions:** 75m+ square boundaries punish mistimed aggressive shots.
- **Spin Trajectory:** Axar Patel and Krunal Pandya use flat, darting trajectories into the wicket that prevent batters from getting under the ball.
- **Death Pacing:** Sandeep Sharma and Bhuvneshwar Kumar utilize wide knuckleballs and change-ups to deny boundaries on large outfields.

---

## 🔬 Mathematical Methodology Summary

1. **Win-Probability Model:**
   - Calibrated Gradient Boosted Decision Trees trained across 766 matches (5-fold out-of-fold match CV, Chase AUC 0.89).
2. **Leverage Metric ($L_i$):**
   $$L_i = \sum_{k \in \text{outcomes}} P(k) \cdot |\text{WP}(\text{state} \mid k) - \text{WP}(\text{state})|$$
   - Deliveries in the top quartile ($L \ge 2.47$ win-pts) with live win probability (20%–80%) after over 3 qualify as High Pressure.
3. **Opponent-Adjusted Joint Ridge Regression:**
   - Simultaneous model evaluating batters ($+$) and bowlers ($-$) to control for opponent strength with Empirical-Bayes shrinkage.
4. **Tri-Factor Composite Formula:**
   $$\text{Composite Score} = 0.50 \cdot z(\text{Impact}) + 0.25 \cdot z(\text{Resilience}) + 0.25 \cdot z(\text{Consistency})$$
5. **Statistical Stability:**
   - 60-fold bootstrap resampling confirms top performers maintain top-tier ranks in 85%+ of samples.
=======
# SupeRR-Selector-Season-2
A quantitative cricket analytics &amp; live IPL 2027 auction war room analyzing 200,999 deliveries across 766 matches using Win Probability Added (WPA), counterfactual leverage, and empirical-Bayes shrinkage to rank the most reliable clutch players. By Wahed Pathan.
>>>>>>> 37478f027c1da5f02bd414072d2be4b1be24f6e9
