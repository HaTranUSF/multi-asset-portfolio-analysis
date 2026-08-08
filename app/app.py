import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Import analytical engine logic
from portfolio_engine import run_portfolio_analysis
 
st.set_page_config(page_title="Multi-Asset Portfolio Analysis", layout="wide")
 
st.title("Multi-Asset Portfolio Analysis")
 
# 1. Sidebar Inputs
st.sidebar.header("Portfolio Weights")
w_spy = st.sidebar.slider("SPY (US Equities)", 0.0, 1.0, 0.50, step=0.05)
w_ief = st.sidebar.slider("IEF (Treasuries)", 0.0, 1.0, 0.30, step=0.05)
w_vxus = st.sidebar.slider("VXUS (Intl Equities)", 0.0, 1.0, 0.10, step=0.05)
w_gld = st.sidebar.slider("GLD (Gold)", 0.0, 1.0, 0.10, step=0.05)
 
weights = {"SPY": w_spy, "IEF": w_ief, "VXUS": w_vxus, "GLD": w_gld}
total_weight = sum(weights.values())
 
# Validate weights before running the engine
st.sidebar.metric("Total Allocation", f"{total_weight:.0%}")
if abs(total_weight - 1.0) > 0.01:
    st.sidebar.warning("Weights must sum to 100%. Adjust the sliders above.")
    st.warning(
        f"Portfolio weights currently total {total_weight:.0%}, not 100%. "
        "Results below are not shown until allocation is fixed."
    )
    st.stop()
 
# 2. Run Engine
results = run_portfolio_analysis(weights)
 
# Top Metrics Overview
col1, col2, col3, col4 = st.columns(4)
col1.metric("Final Value ($100k start)", f"${results['final_value']:,.2f}")
col2.metric("Annualized Volatility", f"{results['volatility']:.1%}")
col3.metric("Max Drawdown", f"{results['max_drawdown']:.1%}")
col4.metric("Sharpe Ratio", f"{results['sharpe_ratio']:.2f}")
 
# 3. Organize Output Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Performance Growth",
    "Risk & Contribution",
    "Market Regimes",
    "Stress Testing"
])
 
# TAB 1: Performance
with tab1:
    st.subheader("Cumulative Portfolio Value")
    st.line_chart(results["portfolio_value"])
 
# TAB 2: Risk Analysis
with tab2:
    st.subheader("Asset Correlation & Risk Contribution")
 
    col_a, col_b = st.columns(2)
 
    with col_a:
        st.write("Correlation Matrix")
        fig_corr, ax_corr = plt.subplots(figsize=(5, 4))
        sns.heatmap(results["returns"].corr(), annot=True, cmap="coolwarm", ax=ax_corr)
        st.pyplot(fig_corr)
 
    with col_b:
        st.write("Risk Contribution Breakdown")
        fig_pie, ax_pie = plt.subplots(figsize=(5, 4))
        ax_pie.pie(results["risk_contributions"], labels=results["risk_contributions"].index, autopct="%1.1f%%")
        st.pyplot(fig_pie)
 
# TAB 3: Market Regime Analysis
with tab3:
    st.subheader("Performance Across Market Regimes")
    st.write("Evaluating portfolio behavior across Bull, Bear, and Rising Rate environments.")
    st.dataframe(results["regime_performance"])
 
# TAB 4: Stress Testing
with tab4:
    st.subheader("Hypothetical Stress Scenarios")
    st.table(results["stress_test_results"])
