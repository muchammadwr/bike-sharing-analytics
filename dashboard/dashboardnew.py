import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


# Function
def total_rentals(df, column):
    total = df[column].sum()
    return total


# Data Frame
daily_df = pd.read_csv("daily_df.csv")
hourly_df = pd.read_csv("hourly_df.csv")
daily_demand_group_df = pd.read_csv("daily_demand_group_df.csv")
hourly_demand_group_df = pd.read_csv("hourly_demand_group_df.csv")


st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")
st.sidebar.title("Dashboard Filters")

# Sidebar
analysis_type = st.sidebar.radio(
    "Select Analysis Type", options=["Hourly", "Daily"], horizontal=True
)

# KPI Card
count = total_rentals(daily_df, "count")
registered = total_rentals(daily_df, "count")
casual = total_rentals(daily_df, "casual")
# Ttile
st.title("Bike Sharing Demand Analytics")
st.subheader("Understanding Rental Patterns to Improve Operational Efficiency")


# KPI Card
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Rentals", value=f"{count:,.0f}")

with col2:
    st.metric(label="Registered", value=f"{registered:,.0f}")

with col3:
    st.metric(label="Casual", value=f"{casual:,.0f}")


# Chart
# Chart
chart_col1, chart_col2, chart_col3 = st.columns(3)

demand_colors = {
    "Low Demand": "#E74C3C",
    "Medium Demand": "#F1C40F",
    "High Demand": "#2ECC71",
}

hourly_demand_group_df = hourly_demand_group_df.sort_values("hour")

hour_order = hourly_demand_group_df["hour"].tolist()

chart_col1, chart_col2, chart_col3 = st.columns(3)

with chart_col1:
    fig = px.bar(
        hourly_demand_group_df,
        x="hour",
        y="average",
        color="demand_group",
        color_discrete_map=demand_colors,
        category_orders={"hour": hour_order},
        title="Average Rentals by Hour",
        labels={
            "hour": "Hour",
            "average": "Average Rentals",
            "demand_group": "Demand Group",
        },
    )

    fig.update_layout(height=400, margin=dict(l=10, r=10, t=60, b=10), showlegend=False)

    st.plotly_chart(fig, width="stretch")
