import streamlit as st
import pandas as pd
# Load Data
df = pd.read_csv("nyc311_final_cleaned.csv")

# Sidebar Filter
st.sidebar.title("Urban Pulse Filters")

selected_borough = st.sidebar.selectbox(
    "Select Borough",
    ["All"] + sorted(df["borough"].dropna().unique())
)

if selected_borough != "All":
    df = df[df["borough"] == selected_borough]

# KPI Calculations
closed = (df['status'] == 'Closed').sum()
closure_rate = round((closed / len(df)) * 100, 2)

open_requests = len(df) - closed

median_resolution = round(
    df['resolution_hours'].median(), 2
)

over_72 = round(
    (df['resolution_hours'].dropna() > 72).mean() * 100,
    2
)

# Dashboard Title
st.title("Urban Pulse NYC Dashboard")

# KPI Row
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Requests", len(df))
col2.metric("Closure Rate (%)", closure_rate)
col3.metric("Open Requests", open_requests)
col4.metric("Median Resolution Hours", median_resolution)
col5.metric("Over 72 Hours (%)", over_72)

# Summary
st.subheader("Project Summary")

st.info(
    f"""
    Total Requests: {len(df):,}
    | Closure Rate: {closure_rate}%
    | Open Requests: {open_requests:,}
    """
)
# Top 10 Complaint Types
st.subheader("Top 10 Complaint Types")

st.bar_chart(
    df['complaint_type']
    .value_counts()
    .head(10)
)

# Requests by Borough
st.subheader("Requests by Borough")

st.bar_chart(
    df['borough'].value_counts()
)

# Status Distribution
st.subheader("Status Distribution")

st.bar_chart(
    df['status'].value_counts()
)

# Agency Workload
st.subheader("Agency Workload")

st.bar_chart(
    df['agency']
    .value_counts()
    .head(10)
)

# Monthly Request Trend
st.subheader("Monthly Request Trend")

st.bar_chart(
    df['month'].value_counts()
)
# Key Insights
st.subheader("Key Insights")

st.write("""
✅ More than 71% of requests have been closed.

✅ NYPD handles the highest workload among agencies.

✅ Illegal Parking is one of the most reported complaint types.

✅ Only a small percentage of complaints exceed 72 hours.

✅ Most complaints are resolved within a short time period.
""")
# Download Button
st.download_button(
    label="Download Filtered Data",
    data=df.to_csv(index=False),
    file_name="urban_pulse_filtered.csv",
    mime="text/csv"
)
# Top Agencies
st.subheader("Top 5 Agencies by Workload")

top_agencies = df["agency"].value_counts().head(5)

for agency, count in top_agencies.items():
    st.write(f"🏢 {agency}: {count:,} requests")
st.markdown("---")

st.caption(
    "Urban Pulse NYC | Citizen Complaint Intelligence & Resolution Analytics"
)
st.subheader("Key Insights")

st.write(f"✅ {closure_rate}% of requests have been closed.")

st.write("✅ NYPD handles the highest workload among agencies.")

st.write("✅ Illegal Parking is one of the most reported complaint types.")

st.write(f"✅ {over_72}% of complaints exceed 72 hours.")

st.write("✅ Most complaints are resolved within a short time period.")
st.subheader("Data Preview")
st.dataframe(df.head(20))
st.success("Dashboard generated successfully from NYC 311 Service Request Data.")
selected_complaint = st.sidebar.selectbox(
    "Filter by Complaint Type",
    ["All"] + sorted(df["complaint_type"].dropna().unique())
)

if selected_complaint != "All":
    df = df[df["complaint_type"] == selected_complaint]
    selected_agency = st.sidebar.selectbox(
    "Filter by Agency",
    ["All"] + sorted(df["agency"].dropna().unique())
)

selected_agency = st.sidebar.selectbox(
    "Filter by Agency",
    ["All"] + sorted(df["agency"].dropna().unique())
)

if selected_agency != "All":
    df = df[df["agency"] == selected_agency]
       