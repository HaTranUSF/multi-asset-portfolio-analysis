# Multi-Asset Portfolio Monitor: Performance, Risk & Market Regime Analysis

An interactive multi-asset portfolio dashboard and quantitative framework built with Python and Streamlit. This project evaluates historical performance, asset-level risk contributions, behavior across macroeconomic market regimes, and scenario stress testing for a diversified portfolio.

🚀 **[Live Interactive Dashboard](https://multi-asset-portfolio-analysis-9hsmazappwugibh5bqs4crm.streamlit.app/)**

 [Link to my notebook](https://github.com/HaTranUSF/multi-asset-portfolio-analysis/blob/main/Analysis/Multi_Asset_Portfolio_Monitor_Performance%2C_Risk_%26_Market_Regime_Analysis.ipynb)

---

## 📌 Executive Summary & Scenario

* **Role:** Junior Multi-Asset Analyst supporting a Portfolio Manager.
* **Objective:** Move beyond single-stock analysis to evaluate portfolio-level risk decomposition, asset correlation, and macroeconomic resilience.
* **Target Portfolio Allocation (Moderately Risk-Tolerant):**
  * **U.S. Equities (SPY):** 50%
  * **U.S. Treasury Bonds (IEF):** 30%
  * **International Equities (VXUS):** 10%
  * **Gold (GLD):** 10%

---

## 📊 Key Findings & Analytical Insights

1. **Growth & Capital Compounding:** Between 2016 and 2026, the hypothetical portfolio nearly tripled in value, growing from **$100,000 to ~$285,000**.
2. **Equity Concentration in Risk Contribution:** While **SPY** makes up 50% of the portfolio weight, it accounts for **78.9% of total portfolio risk**. Combined with **VXUS (14.2%)**, equities drive **93.1%** of overall portfolio variance.
3. **Diversification Benefits:** Combining non-correlated assets reduced total portfolio annualized volatility to **~10.7%** (compared to ~17.8% for SPY) and mitigated maximum drawdown to **~21%** (compared to ~34% for SPY and ~36% for VXUS).
4. **Risk-Adjusted Return:** The portfolio's annualized **Sharpe Ratio of ~0.80** confirms that diversification didn't just reduce volatility, it preserved a reasonable return per unit of risk taken, consistent with a moderately risk-tolerant allocation.
5. **Market Regime Resilience:**
   * **Bull Markets:** Averaged **+2.63%** monthly return.
   * **Bear Markets:** Averaged **-1.11%** monthly return, demonstrating strong downside mitigation from Treasuries and Gold.
   * **Rising Rate Environments:** Averaged **-0.08%** monthly return, highlighting fixed-income duration sensitivity during rate-hike cycles.
6. **Stress Test Scenarios:**
   * **Equity Crash (-20% SPY, -25% VXUS, +5% IEF, +10% GLD):** **-10.0%** Portfolio Impact.
   * **Rate Shock (-10% SPY, -12% VXUS, -8% IEF, +3% GLD):** **-8.3%** Portfolio Impact.
   * **Global Risk-Off (-30% SPY, -35% VXUS, +10% IEF, +15% GLD):** **-14.0%** Portfolio Impact.

---

## 🛠️ Tech Stack & Methodology

* **Language:** Python 3.14
* **Web Framework:** Streamlit
* **Data Sources:** `yfinance`
* **Data Analysis & Visualization:** `pandas`, `numpy`, `matplotlib`, `seaborn`
* **Risk Modeling:** Covariance matrix risk contribution decomposition, cumulative drawdowns, resampled regime performance analysis.
---

## 📂 Project Structure

```text
multi-asset-portfolio-analysis/
│
├── Multi_Asset_Portfolio_Monitor.ipynb   # Exploratory analysis & narrative findings
│
├── app/
│   ├── app.py                            # Streamlit user interface & layout logic
│   └── portfolio_engine.py               # Core analytical engine (returns, risk, regimes, stress testing)
│
├── requirements.txt                      # Package dependencies for local execution & cloud deployment
└── README.md                             # Project documentation
```

---

## ▶️ Running Locally

```bash
# Clone the repo
git clone https://github.com/HaTranUSF/multi-asset-portfolio-analysis.git
cd multi-asset-portfolio-analysis

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run app/app.py
```

The app will open at `http://localhost:8501`. Adjust the sidebar sliders to test different allocations - the weights must sum to 100%.
