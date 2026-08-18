import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


sns.set_theme(style="dark")


# KPI

# Data Frame
daily_df = pd.read_csv("daily_df.csv")
hourly_df = pd.read_csv("hourly_df.csv")
daily_demand_group_df = pd.read_csv("daily_demand_group_df.csv")
hourly_demand_group_df = pd.read_csv("hourly_demand_group_df.csv")


# Visualizatin
# Ttile
st.title("Bike Sharing Demand Analytics", text_alignment="right")
st.subheader("Understanding Rental Patterns to Improve Operational Efficiency")


total_rentals = daily_df["count"].sum()
registered_rentals = daily_df["registered"].sum()
casual_rentals = daily_df["casual"].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Rentals", value=f"{total_rentals:,.0f}")

with col2:
    st.metric(label="Registered", value=f"{registered_rentals:,.0f}")

with col3:
    st.metric(label="Casual", value=f"{casual_rentals:,.0f}")


# st.markdown(

#     """
#     <div class="dashboard-title">
#         Bike Sharing Analytics Dashboard
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Membaca dataset
# hourly_grouping_df = pd.read_csv("hourly_demand_group_df.csv")

# # Menampilkan data
# st.subheader("Hourly Rental Data")
# st.dataframe(hourly_grouping_df.head())

# # Membuat bar chart
# st.bar_chart(
#     data=hourly_grouping_df,
#     x="hour",
#     y=["total", "average"],
#     color="demand_group",
#     stack=False,
# )

# import altair as alt
# import streamlit as st


# # Mengurutkan data berdasarkan jam
# hourly_grouping_df = hourly_grouping_df.sort_values("hour")

# hour_order = hourly_grouping_df["hour"].tolist()

# demand_colors = {
#     "Low Demand": "#E74C3C",
#     "Medium Demand": "#F1C40F",
#     "High Demand": "#2ECC71",
# }

# fig = px.bar(
#     hourly_grouping_df,
#     x="hour",
#     y="average",
#     color="demand_group",
#     color_discrete_map=demand_colors,
#     category_orders={
#         "hour": hour_order,
#         "demand_group": ["Low Demand", "Medium Demand", "High Demand"],
#     },
#     custom_data=["total", "demand_group"],
#     title="Average Bike Rentals by Hour",
#     labels={
#         "hour": "Hour",
#         "average": "Average Rentals",
#         "demand_group": "Demand Group",
#     },
# )

# fig.update_traces(
#     hovertemplate=(
#         "<b>Hour: %{x}</b><br>"
#         "Average Rentals: %{y:.2f}<br>"
#         "Total Rentals: %{customdata[0]:,}<br>"
#         "Demand Group: %{customdata[1]}"
#         "<extra></extra>"
#     )
# )

# fig.update_layout(
#     height=500,
#     bargap=0.15,
#     xaxis_title="Hour",
#     yaxis_title="Average Rentals",
#     legend_title="Demand Group",
# )

# st.plotly_chart(fig, width="stretch")
