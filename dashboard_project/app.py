import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Load Data
@st.cache_data
def load_data():
    return pd.read_excel("data/business_data.xlsx")

df = load_data()

# Sidebar Filters
st.sidebar.title("🔍 Filters")
regions = st.sidebar.multiselect("Select Region(s):", df["Region"].unique(), default=df["Region"].unique())
departments = st.sidebar.multiselect("Select Department(s):", df["Department"].unique(), default=df["Department"].unique())
date_range = st.sidebar.date_input("Select Date Range:", [df["Date"].min(), df["Date"].max()])

# Filter Data
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Department"].isin(departments)) &
    (df["Date"] >= pd.to_datetime(date_range[0])) &
    (df["Date"] <= pd.to_datetime(date_range[1]))
]

# Dashboard Title
st.title("📊 Business Performance Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Avg. Satisfaction", f"{filtered_df['Customer Satisfaction'].mean():.1f}%")
col3.metric("Tickets Resolved", int(filtered_df['Support Tickets Resolved'].sum()))

# Charts
st.subheader("📈 Sales Over Time")
sales_chart = px.line(filtered_df.groupby("Date")["Sales"].sum().reset_index(), x="Date", y="Sales", title="Daily Sales")
st.plotly_chart(sales_chart, use_container_width=True)

# Charts in 3 columns
st.subheader("📊 Visualizations")

col1, col2, col3 = st.columns([1, 1, 1], gap="large")  # Equal width, with spacing

# Chart 1: Sales Over Time
with col1:
    sales_chart = px.line(
        filtered_df.groupby("Date")["Sales"].sum().reset_index(),
        x="Date", y="Sales", title="📈 Sales Over Time"
    )
    st.plotly_chart(sales_chart, use_container_width=True)

# Chart 2: Leads by Department
with col2:
    leads_chart = px.bar(
        filtered_df.groupby("Department")["Leads Generated"].sum().reset_index(),
        x="Department", y="Leads Generated", color="Department", title="📌 Leads by Department"
    )
    st.plotly_chart(leads_chart, use_container_width=True)

# Chart 3: Tickets Resolved by Region
with col3:
    tickets_chart = px.pie(
        filtered_df.groupby("Region")["Support Tickets Resolved"].sum().reset_index(),
        names="Region", values="Support Tickets Resolved", title="🎟️ Tickets Resolved by Region"
    )
    st.plotly_chart(tickets_chart, use_container_width=True)