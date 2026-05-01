import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("PowerStake Dashboard")

# Metrics row
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Power", "624 W", "-8%")
col2.metric("Energy Today", "12.45 kWh", "+5%")
col3.metric("Cost Today", "$2.18", "+6%")
col4.metric("Devices On", "7 / 10")

# Chart
st.subheader("Power Usage")
data = np.random.randint(200, 800, 24)
st.line_chart(data)

# Alerts + Recommendations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Alerts")
    st.warning("High standby power (TV)")
    st.warning("Abnormal usage (Washing Machine)")

with col2:
    st.subheader("Recommendations")
    st.success("Turn off TV standby")
    st.success("Schedule heater shutdown")

# Table
st.subheader("Device Overview")
df = pd.DataFrame({
    "Device": ["TV", "Fridge", "Heater"],
    "Power (W)": [15, 120, 2000],
    "Status": ["Standby", "On", "On"]
})
st.dataframe(df)