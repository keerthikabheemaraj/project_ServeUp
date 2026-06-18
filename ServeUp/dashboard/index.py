import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="JUPENTA ServeUp Dashboard",
    page_icon="🍽️",
    layout="wide"
)


import os

@st.cache_data
def load_data():
    st.write("Current Folder:")
    st.write(os.getcwd())

    st.write("Files Available:")
    st.write(os.listdir())

    return pd.read_csv("ServeUp_cleaned_data.csv")

df = load_data()



st.title("🍽️ JUPENTA ServeUp Market Intelligence Dashboard")

st.markdown("""
### Competitor Analysis for Food Business Operating System

This dashboard provides insights from competitor research across
Restaurant POS, Restaurant OS, ERP, CRM, Ordering Platforms,
Bakery Software and Loyalty Solutions.
""")

st.divider()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Competitors",
        len(df)
    )

with col2:
    st.metric(
        "Categories",
        df['Category'].nunique()
    )

with col3:
    st.metric(
        "Countries",
        df['Country'].nunique()
    )

with col4:
    st.metric(
        "Pricing Models",
        df['Pricing'].nunique()
    )

st.divider()



st.sidebar.header("Filters")

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    df["Category"].isin(selected_category)
]



st.subheader("📊 Competitor Distribution by Category")

category_count = (
    filtered_df["Category"]
    .value_counts()
    .reset_index()
)

category_count.columns = ["Category", "Count"]

fig1 = px.bar(
    category_count,
    x="Category",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)


st.subheader("💰 Pricing Distribution")

pricing_count = (
    filtered_df["Pricing"]
    .value_counts()
    .reset_index()
)

pricing_count.columns = ["Pricing", "Count"]

fig2 = px.pie(
    pricing_count,
    names="Pricing",
    values="Count",
    hole=0.5
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


st.subheader("🌍 Country Analysis")

country_count = (
    filtered_df["Country"]
    .value_counts()
    .head(10)
    .reset_index()
)

country_count.columns = ["Country", "Count"]

fig3 = px.bar(
    country_count,
    x="Country",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)



st.subheader("🎯 Target Customer Analysis")

customer_count = (
    filtered_df["Target Customer"]
    .value_counts()
    .reset_index()
)

customer_count.columns = [
    "Target Customer",
    "Count"
]

fig4 = px.bar(
    customer_count,
    x="Target Customer",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)



st.subheader("⚙️ Feature Intelligence")

feature_cols = [
    'Billing POS',
    'Inventory',
    'Online Ordering',
    'Digital Menu',
    'Analytics',
    'Loyalty Program',
    'Multi Branch',
    'Payment Integration'
]

feature_data = []

for col in feature_cols:
    if col in filtered_df.columns:

        count = (
            filtered_df[col]
            .astype(str)
            .str.lower()
            .eq("yes")
            .sum()
        )

        feature_data.append(
            [col, count]
        )

feature_df = pd.DataFrame(
    feature_data,
    columns=["Feature", "Count"]
)

fig5 = px.bar(
    feature_df,
    x="Feature",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)



st.subheader("💪 Top Competitor Strengths")

strength_count = (
    filtered_df["Strengths"]
    .value_counts()
    .head(10)
    .reset_index()
)

strength_count.columns = [
    "Strength",
    "Count"
]

fig6 = px.bar(
    strength_count,
    x="Strength",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)


st.subheader("⚠️ Top Competitor Weaknesses")

weakness_count = (
    filtered_df["Weaknesses"]
    .value_counts()
    .head(10)
    .reset_index()
)

weakness_count.columns = [
    "Weakness",
    "Count"
]

fig7 = px.bar(
    weakness_count,
    x="Weakness",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig7,
    use_container_width=True
)



st.subheader("🚀 Strategic Opportunities for ServeUp")

opportunity_df = pd.DataFrame({
    "Market Gap":[
        "Expensive Software",
        "Weak Customer Support",
        "Generic POS Systems",
        "Limited Bakery Features",
        "Weak Analytics",
        "Weak Loyalty Systems"
    ],
    "ServeUp Recommendation":[
        "Affordable Pricing Plans",
        "Dedicated Support Team",
        "Industry Specific Workflows",
        "Bakery Production Module",
        "AI Analytics Dashboard",
        "Advanced Loyalty Engine"
    ]
})

st.dataframe(
    opportunity_df,
    use_container_width=True
)



st.subheader("📄 Competitor Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)


st.divider()

st.success(
    "Project: JUPENTA ServeUp | Competitor Analysis Dashboard"
)
