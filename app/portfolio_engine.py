import yfinance as yf
import pandas as pd

def run_portfolio_analysis(weights, start_date="2016-01-01", end_date="2026-08-01"):
    tickers = list(weights.keys())
    prices = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)["Close"]
    returns = prices.pct_change().dropna()
    
    # Portfolio Return & Value
    weights_series = pd.Series(weights)
    portfolio_returns = (returns * weights_series).sum(axis=1)
    cumulative = (1 + portfolio_returns).cumprod()
    portfolio_value = 100000 * cumulative
    
    # Standard Risk Metrics
    volatility = portfolio_returns.std() * (252 ** 0.5)
    max_dd = ((cumulative - cumulative.cummax()) / cumulative.cummax()).min()
    
    # Risk Contribution Breakdown
    cov_matrix = returns.cov() * 252
    port_var = weights_series @ cov_matrix @ weights_series
    port_vol = port_var ** 0.5
    marginal_contrib = cov_matrix @ weights_series
    risk_contrib = (weights_series * marginal_contrib) / port_vol
    risk_contrib_pct = risk_contrib / risk_contrib.sum()
    
    # Stress Testing Calculations
    scenarios = {
        "Equity Crash": {"SPY": -0.20, "IEF": 0.05, "VXUS": -0.25, "GLD": 0.10},
        "Rate Shock": {"SPY": -0.10, "IEF": -0.08, "VXUS": -0.12, "GLD": 0.03},
        "Global Risk-Off": {"SPY": -0.30, "IEF": 0.10, "VXUS": -0.35, "GLD": 0.15}
    }
    
    stress_results = []
    for scenario, shocks in scenarios.items():
        impact = sum(weights[asset] * shocks[asset] for asset in weights)
        stress_results.append({"Scenario": scenario, "Impact": f"{impact:.1%}"})
        
    stress_df = pd.DataFrame(stress_results)
    
    # Regime Analysis
    monthly_returns = returns.resample("ME").apply(lambda x: (1 + x).prod() - 1)
    regime = pd.Series("Neutral", index=monthly_returns.index)
    regime[monthly_returns["SPY"] > 0] = "Bull"
    regime[monthly_returns["SPY"] < 0] = "Bear"
    regime[monthly_returns["IEF"] < 0] = "Rising_Rate"
    
    portfolio_monthly = portfolio_returns.resample("ME").apply(lambda x: (1 + x).prod() - 1)
    regime_df = pd.DataFrame({"Portfolio": portfolio_monthly, "Regime": regime})
    regime_summary = regime_df.groupby("Regime")["Portfolio"].agg(["mean", "std", "count"])

    return {
        "portfolio_value": portfolio_value,
        "final_value": portfolio_value.iloc[-1],
        "volatility": volatility,
        "max_drawdown": max_dd,
        "returns": returns,
        "risk_contributions": risk_contrib_pct,
        "stress_test_results": stress_df,
        "regime_performance": regime_summary
    }