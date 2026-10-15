import streamlit as st
import altair as alt
from notebooks.explore import (
    load_data,
    revenue_by_branch,
    quantity_by_product,
    revenue_by_month,
)

st.title("SME Sales Dashboard")

df = load_data()

# --- Sidebar filters ---
st.sidebar.header("Filters")

all_branches = sorted(df["branch"].unique())
selected_branches = st.sidebar.multiselect(
    "Branch", options=all_branches, default=all_branches
)

all_products = sorted(df["product"].unique())
selected_products = st.sidebar.multiselect(
    "Product", options=all_products, default=all_products
)

filtered = df[
    df["branch"].isin(selected_branches) & df["product"].isin(
        selected_products)
]

if filtered.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

# --- KPI cards ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"P{filtered['total_revenue'].sum():,}")
col2.metric("Units Sold", f"{filtered['quantity_sold'].sum():,}")
col3.metric("Transactions", f"{len(filtered):,}")

# --- Charts (all built from the filtered data) ---
st.subheader("Revenue by Branch")
st.bar_chart(revenue_by_branch(filtered))

st.subheader("Quantity Sold by Product")
product_data = quantity_by_product(filtered).reset_index()
product_chart = (
    alt.Chart(product_data)
    .mark_bar()
    .encode(
        x=alt.X("quantity_sold:Q", title="Quantity Sold"),
        y=alt.Y("product:N", sort="x", title=None),
    )
)
st.altair_chart(product_chart, width="stretch")

st.subheader("Revenue by Month")
month_names = {4: "Apr", 5: "May", 6: "Jun", 7: "Jul"}
month_data = revenue_by_month(filtered).reset_index()
month_data["month_name"] = month_data["month"].map(month_names)

month_chart = (
    alt.Chart(month_data)
    .mark_line(point=True)
    .encode(
        x=alt.X(
            "month_name:N",
            sort=list(month_names.values()),
            title="Month",
            axis=alt.Axis(labelAngle=0),
        ),
        y=alt.Y("total_revenue:Q", title="Total Revenue"),
    )
)
st.altair_chart(month_chart, width="stretch")
