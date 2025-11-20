import streamlit as st
import pandas as pd
import plotly.express as px

import sys
import os

# Add project root to Python path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ROOT_DIR)
second_root=os.path.dirname(os.path.abspath(__file__))
print(second_root)
sys.path.append(ROOT_DIR)


from etl.load_data import *
from etl.metrics import *
from etl.insights import *

st.title("📊 Life Score – Weekly Wellness Dashboard")

# Upload files
# browser_file = st.file_uploader("Upload Browser History JSON")
# app_file = st.file_uploader("Upload App Usage CSV")
# sleep_file = st.file_uploader("Upload Sleep/Steps CSV")

DATA_DIR=os.path.join(ROOT_DIR,"sample_data")

browser_file=os.path.join(DATA_DIR,"browser_history.json")
app_file=os.path.join(DATA_DIR,"app_usage.csv")
sleep_file=os.path.join(DATA_DIR,"sleep_steps.csv")


if browser_file and app_file and sleep_file:
    browser_df = pd.read_json(browser_file)
    app_df = pd.read_csv(app_file)
    sleep_df = pd.read_csv(sleep_file)

    # METRICS
    prod = compute_productivity_score(browser_df, app_df)
    sleep_index = compute_sleep_adequacy(sleep_df)
    ratio = entertainment_work_ratio(app_df)
    summary = generate_weekly_summary(prod, sleep_index, ratio)

    st.subheader("📈 Life Scores")
    st.metric("Productivity Score", f"{prod}/100")
    st.metric("Sleep Adequacy", f"{sleep_index}/100")
    st.metric("Entertainment-Work Ratio", ratio)

    st.subheader("📊 Time Series (Sleep & Steps)")
    fig = px.line(sleep_df, x="date", y=["sleep_hours", "steps"])
    st.plotly_chart(fig)

    st.subheader("🧩 App Usage Pie Chart")
    pie = px.pie(app_df, names='app_name', values='minutes')
    st.plotly_chart(pie)

    st.subheader("🧠 AI Insights Summary")
    st.write(summary)
