import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="PowerStake Dashboard",
    page_icon="⚡",
    layout="wide"
)

# ---------- Styling ----------
st.markdown("""
<style>
    .main {
        background-color: #f7f9fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    .metric-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        border: 1px solid #edf0f2;
        min-height: 135px;
    }

    .metric-title {
        color: #333;
        font-size: 15px;
        font-weight: 600;
    }

    .metric-value {
        color: #0fa958;
        font-size: 34px;
        font-weight: 700;
        margin-top: 8px;
    }

    .metric-change {
        color: #0fa958;
        font-size: 14px;
        margin-top: 8px;
    }

    .card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        border: 1px solid #edf0f2;
        margin-bottom: 18px;
    }

    .alert-box {
        background: #fff7f3;
        padding: 14px;
        border-radius: 12px;
        margin-bottom: 12px;
        border-left: 5px solid #ff8a3d;
    }

    .recommend-box {
        background: #f0fff6;
        padding: 14px;
        border-radius: 12px;
        margin-bottom: 12px;
        border-left: 5px solid #0fa958;
    }

    .small-text {
        color: #667085;
        font-size: 13px;
    }

    h1, h2, h3 {
        color: #101828;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.markdown("## ⚡ PowerStake")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Devices", "Alerts", "Recommendations", "History", "Settings"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Today's Summary")
st.sidebar.metric("Total Energy", "12.45 kWh")
st.sidebar.metric("Estimated Cost", "$2.18")
st.sidebar.metric("CO₂ Saved", "1.2 kg")

# ---------- Fake Data ----------
hours = pd.date_range("2026-04-24 00:00", periods=24, freq="h")

power_data = pd.DataFrame({
    "Time": hours,
    "Power (W)": [
        340, 320, 315, 260, 220, 210, 250, 330,
        460, 700, 850, 620, 450, 360, 330, 340,
        360, 390, 410, 620, 660, 690, 480, 370
    ]
})

device_data = pd.DataFrame({
    "Device": ["Refrigerator", "TV", "Washing Machine", "Heater", "Desk Lamp", "Gaming Console"],
    "Status": ["On", "Standby", "On", "On", "Off", "Standby"],
    "Power (W)": [120, 15, 450, 2000, 0, 22],
    "Energy Today (kWh)": [2.45, 0.30, 1.80, 6.20, 0.00, 0.42],
    "AI Insight": [
        "Normal",
        "High standby duration",
        "Abnormal usage detected",
        "Recommend scheduled shutoff",
        "No issue",
        "Standby saving opportunity"
    ]
})

# ---------- Dashboard ----------
if page == "Dashboard":
    left, right = st.columns([3, 1])

    with left:
        st.title("Dashboard")
        st.caption(f"Last updated: {datetime.now().strftime('%I:%M:%S %p')}  •  Connected")

    with right:
        st.success("System Online")

    # Metric cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Total Power Now</div>
            <div class="metric-value">624 W</div>
            <div class="metric-change">↓ 8% vs yesterday</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Today's Energy</div>
            <div class="metric-value">12.45 kWh</div>
            <div class="metric-change">↑ 5% vs yesterday</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Today's Cost</div>
            <div class="metric-value">$2.18</div>
            <div class="metric-change">↑ 6% vs yesterday</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">Devices On</div>
            <div class="metric-value">7 / 10</div>
            <div class="metric-change">70% currently active</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    # Main layout
    chart_col, side_col = st.columns([2, 1])

    with chart_col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Power Usage Today")
        st.line_chart(power_data.set_index("Time"))
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Device Overview")
        st.dataframe(device_data, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with side_col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Active Alerts")

        st.markdown("""
        <div class="alert-box">
            <b>⚠ High Standby Power</b><br>
            <span class="small-text">TV has been in standby for 4+ hours</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="alert-box">
            <b>⚠ Abnormal Usage Detected</b><br>
            <span class="small-text">Washing machine power profile is higher than usual</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="alert-box">
            <b>⚠ Potential Fault</b><br>
            <span class="small-text">Heater power fluctuation detected</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Top Recommendations")

        st.markdown("""
        <div class="recommend-box">
            <b>✅ Turn off TV standby</b><br>
            <span class="small-text">Estimated saving: $0.32/day</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="recommend-box">
            <b>✅ Schedule heater shutdown</b><br>
            <span class="small-text">Estimated saving: $0.45/day</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="recommend-box">
            <b>✅ Unplug idle devices</b><br>
            <span class="small-text">3 devices currently in standby mode</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Devices ----------
elif page == "Devices":
    st.title("Devices")
    st.dataframe(device_data, use_container_width=True, hide_index=True)

# ---------- Alerts ----------
elif page == "Alerts":
    st.title("Alerts")

    st.warning("High Standby Power: TV has remained in standby for more than 4 hours.")
    st.warning("Abnormal Usage: Washing machine power profile is higher than normal.")
    st.error("Potential Fault: Heater power fluctuation detected.")

# ---------- Recommendations ----------
elif page == "Recommendations":
    st.title("Recommendations")

    st.success("Turn off TV standby — estimated saving $0.32/day.")
    st.success("Schedule heater shutdown after 10:30 PM — estimated saving $0.45/day.")
    st.success("Unplug idle devices — 3 standby devices detected.")

# ---------- History ----------
elif page == "History":
    st.title("Usage History")
    st.line_chart(power_data.set_index("Time"))

# ---------- Settings ----------
elif page == "Settings":
    st.title("Settings")

    st.toggle("Enable automatic shutoff recommendations", value=True)
    st.toggle("Enable fault alerts", value=True)
    st.slider("Standby detection threshold (W)", 1, 50, 10)
    st.slider("Inactivity time before recommendation (hours)", 1, 12, 4)