import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# DATAFRAME
daily_df = pd.read_csv("daily_df.csv")
hourly_df = pd.read_csv("hourly_df.csv")
daily_demand_group_df = pd.read_csv("daily_demand_group_df.csv")
hourly_demand_group_df = pd.read_csv("hourly_demand_group_df.csv")


# HELPER FUNCTIONS
def total_rentals(df, column):
    total = df[column].sum()
    return total


# Average daily rentals by weather
weather_average_df = (
    daily_df.groupby("weathersit", as_index=False, observed=False)
    .agg(average_rentals=("count", "mean"))
    .round({"average_rentals": 2})
    .sort_values("average_rentals", ascending=False)
)

# Menyiapkan data komposisi pengguna
daily_user_type_df = pd.DataFrame(
    {
        "user_type": ["Registered", "Casual"],
        "total_rentals": [daily_df["registered"].sum(), daily_df["casual"].sum()],
    }
)


# DASHBOARD
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")
st.sidebar.title("Dashboard Filters")

# Sidebar
analysis_type = st.sidebar.radio(
    "Select Analysis Type", options=["Hourly", "Daily"], horizontal=True
)


# Title
st.title("Bike Sharing Demand Analytics")
st.subheader("Understanding Rental Patterns to Improve Operational Efficiency")

# KPI
count = total_rentals(daily_df, "count")
registered = total_rentals(daily_df, "count")
casual = total_rentals(daily_df, "casual")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Rentals", value=f"{count:,.0f}")

with col2:
    st.metric(label="Registered", value=f"{registered:,.0f}")

with col3:
    st.metric(label="Casual", value=f"{casual:,.0f}")


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

with chart_col2:
    fig_date = px.line(
        daily_df,
        x="date",
        y="count",
        title="Total Rentals by Date",
        labels={"date": "Date", "count": "Total Rentals"},
    )

    fig_date.update_traces(
        line_color="#72BCD4",
        line_width=2,
        hovertemplate=(
            "<b>Date: %{x|%d %B %Y}</b><br>Total Rentals: %{y:,.0f}<extra></extra>"
        ),
    )

    fig_date.update_layout(
        height=400, margin=dict(l=10, r=10, t=60, b=10), showlegend=False
    )

    st.plotly_chart(fig_date, width="stretch")

with chart_col3:
    fig_weather = px.bar(
        weather_average_df,
        x="weathersit",
        y="average_rentals",
        title="Average Daily Rentals by Weather",
        labels={
            "weathersit": "Weather Condition",
            "average_rentals": "Average Daily Rentals",
        },
        color="average_rentals",
        color_continuous_scale="Blues",
        text_auto=".0f",
    )

    fig_weather.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>Weather: %{x}</b><br>Average Rentals: %{y:,.2f}<extra></extra>"
        ),
    )

    fig_weather.update_layout(
        height=400,
        margin=dict(l=10, r=10, t=60, b=10),
        coloraxis_showscale=False,
        showlegend=False,
        xaxis_title="Weather Condition",
        yaxis_title="Average Daily Rentals",
    )

    st.plotly_chart(fig_weather, width="stretch")


fig_pie = px.pie(
    daily_user_type_df,
    names="user_type",
    values="total_rentals",
    title="Daily Rentals by User Type",
    color="user_type",
    color_discrete_map={"Registered": "#72BCD4", "Casual": "#FFB703"},
    hole=0.45,
)

fig_pie.update_traces(
    textposition="inside",
    textinfo="label+percent",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "Total Rentals: %{value:,.0f}<br>"
        "Percentage: %{percent}"
        "<extra></extra>"
    ),
)

fig_pie.update_layout(
    height=400, margin=dict(l=10, r=10, t=60, b=10), legend_title="User Type"
)

st.plotly_chart(fig_pie, width="stretch")
