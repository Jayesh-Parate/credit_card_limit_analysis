
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Financial Performance Analysis",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #6b7280;
        margin-bottom: 1.5rem;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.45rem;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# DATA LOADING
# ---------------------------------------------------------
@st.cache_data
def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df


st.sidebar.title("💰 Financial Analytics")
st.sidebar.markdown("### Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload Credir_Card_Bank.xlsx",
    type=["xlsx", "xls"]
)

if uploaded_file is None:
    st.title("💰 Financial Performance Analysis")
    st.info(
        "Upload the **Credir_Card_Bank.xlsx** Excel file from the sidebar "
        "to start the interactive dashboard."
    )

    st.markdown("""
    ### Dashboard includes
    - Income vs Savings Analysis
    - Income vs Investment Analysis
    - EMI and Debt Analysis
    - Credit Utilization Analysis
    - Credit Limit Analysis
    - Loan Portfolio Analysis
    - Credit Score Analysis
    - Default & Payment Behaviour
    - Fraud Analysis
    - KPI Summary
    - Correlation Matrix
    """)
    st.stop()


df = load_data(uploaded_file)

# ---------------------------------------------------------
# BASIC VALIDATION / CALCULATED COLUMNS
# ---------------------------------------------------------
required_columns = [
    "Customer_ID", "Monthly_Income", "Annual_Income",
    "Savings_Balance", "Investment_Value", "EMI_Per_Month",
    "Debt_To_Income_Ratio", "Credit_Utilization",
    "Existing_Credit_Limit", "Loan_Count", "Credit_Score",
    "Employment_Type", "Occupation", "Number_of_Defaults",
    "Missed_Payments", "Late_Payment_Count",
    "Avg_Monthly_Spending", "Fraud_Flag"
]

missing_columns = [c for c in required_columns if c not in df.columns]

if missing_columns:
    st.error("The uploaded file is missing these required columns:")
    st.write(missing_columns)
    st.stop()

df["Savings_Percentage"] = np.where(
    df["Monthly_Income"] != 0,
    (df["Savings_Balance"] / df["Monthly_Income"]) * 100,
    np.nan
)

df["Investment_Percentage"] = np.where(
    df["Monthly_Income"] != 0,
    (df["Investment_Value"] / df["Monthly_Income"]) * 100,
    np.nan
)

# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.header("🔎 Filters")

employment_options = sorted(df["Employment_Type"].dropna().unique().tolist())
occupation_options = sorted(df["Occupation"].dropna().unique().tolist())

selected_employment = st.sidebar.multiselect(
    "Employment Type",
    employment_options,
    default=employment_options
)

selected_occupation = st.sidebar.multiselect(
    "Occupation",
    occupation_options,
    default=occupation_options
)

filtered_df = df[
    df["Employment_Type"].isin(selected_employment) &
    df["Occupation"].isin(selected_occupation)
].copy()

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">💰 Financial Performance Analysis</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Interactive analysis of income, savings, '
    'investments, debt, credit behaviour and financial risk.</div>',
    unsafe_allow_html=True
)

if filtered_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# ---------------------------------------------------------
# KPI CARDS
# ---------------------------------------------------------
st.subheader("📊 Key Financial Indicators")

kpi_values = [
    ("Total Customers", filtered_df["Customer_ID"].nunique()),
    ("Avg Monthly Income", filtered_df["Monthly_Income"].mean()),
    ("Total Savings", filtered_df["Savings_Balance"].sum()),
    ("Avg Savings", filtered_df["Savings_Balance"].mean()),
    ("Total Investments", filtered_df["Investment_Value"].sum()),
    ("Avg EMI", filtered_df["EMI_Per_Month"].mean()),
    ("Avg Debt-to-Income", filtered_df["Debt_To_Income_Ratio"].mean()),
    ("Avg Credit Utilization", filtered_df["Credit_Utilization"].mean()),
    ("Avg Credit Score", filtered_df["Credit_Score"].mean()),
    ("Avg Existing Credit Limit", filtered_df["Existing_Credit_Limit"].mean())
]

cols = st.columns(5)

for i, (label, value) in enumerate(kpi_values):
    if "Customers" in label:
        display_value = f"{int(value):,}"
    elif "Score" in label:
        display_value = f"{value:,.1f}"
    elif "Utilization" in label or "Debt-to-Income" in label:
        display_value = f"{value:,.2f}"
    else:
        display_value = f"₹{value:,.0f}"

    cols[i % 5].metric(label, display_value)

st.markdown("---")

# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------
tabs = st.tabs([
    "💵 Income & Savings",
    "📈 Investments",
    "💳 Debt & EMI",
    "🏦 Credit",
    "💰 Loans",
    "⚠️ Risk & Fraud",
    "📋 Data",
    "🔗 Correlation"
])


# =========================================================
# TAB 1: INCOME & SAVINGS
# =========================================================
with tabs[0]:
    st.header("Income vs Savings Analysis")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.scatter(
            filtered_df,
            x="Monthly_Income",
            y="Savings_Balance",
            trendline="ols",
            opacity=0.55,
            title="Income vs Savings"
        )
        fig.update_layout(
            xaxis_title="Monthly Income",
            yaxis_title="Savings Balance"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            filtered_df,
            x="Savings_Percentage",
            nbins=30,
            marginal="box",
            title="Savings Percentage Distribution"
        )
        fig.update_layout(
            xaxis_title="Savings Percentage (%)",
            yaxis_title="Customers"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Employment-wise Income and Savings Statistics")

    summary = (
        filtered_df
        .groupby("Employment_Type")[["Annual_Income", "Savings_Balance"]]
        .describe()
        .round(2)
    )

    st.dataframe(summary, use_container_width=True)

    employment_savings = (
        filtered_df.groupby("Employment_Type", as_index=False)["Savings_Balance"]
        .mean()
        .sort_values("Savings_Balance", ascending=False)
    )

    fig = px.bar(
        employment_savings,
        x="Employment_Type",
        y="Savings_Balance",
        title="Average Savings by Employment Type"
    )
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# TAB 2: INVESTMENTS
# =========================================================
with tabs[1]:
    st.header("Income vs Investment Analysis")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.scatter(
            filtered_df,
            x="Monthly_Income",
            y="Investment_Value",
            trendline="ols",
            opacity=0.55,
            title="Income vs Investments"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            filtered_df,
            x="Investment_Percentage",
            nbins=30,
            marginal="box",
            title="Investment Percentage Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top 10 Occupations by Average Annual Income")

    occupation_summary = (
        filtered_df
        .groupby("Occupation")[["Annual_Income", "Investment_Value"]]
        .mean()
        .round(2)
        .sort_values("Annual_Income", ascending=False)
        .head(10)
        .reset_index()
    )

    st.dataframe(occupation_summary, use_container_width=True)

    fig = px.bar(
        occupation_summary.sort_values("Annual_Income"),
        x="Annual_Income",
        y="Occupation",
        orientation="h",
        title="Top 10 Occupations by Average Annual Income"
    )
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# TAB 3: DEBT & EMI
# =========================================================
with tabs[2]:
    st.header("Debt & EMI Analysis")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            filtered_df,
            x="EMI_Per_Month",
            nbins=30,
            marginal="box",
            title="Monthly EMI Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.box(
            filtered_df,
            y="Debt_To_Income_Ratio",
            title="Debt-to-Income Ratio"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("EMI Statistics")
    st.dataframe(
        filtered_df[["EMI_Per_Month"]].describe().T.round(2),
        use_container_width=True
    )

    st.subheader("Average Debt-to-Income Ratio by Employment Type")

    dti_summary = (
        filtered_df
        .groupby("Employment_Type", as_index=False)["Debt_To_Income_Ratio"]
        .mean()
        .sort_values("Debt_To_Income_Ratio", ascending=False)
    )

    fig = px.bar(
        dti_summary,
        x="Employment_Type",
        y="Debt_To_Income_Ratio",
        title="Average Debt-to-Income Ratio by Employment Type"
    )
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# TAB 4: CREDIT
# =========================================================
with tabs[3]:
    st.header("Credit Analysis")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            filtered_df,
            x="Credit_Utilization",
            nbins=30,
            marginal="box",
            title="Credit Utilization Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(
            filtered_df,
            x="Existing_Credit_Limit",
            nbins=30,
            marginal="box",
            title="Existing Credit Limit"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Credit Utilization by Occupation")

    occupation_credit = (
        filtered_df
        .groupby("Occupation", as_index=False)["Credit_Utilization"]
        .mean()
        .sort_values("Credit_Utilization", ascending=False)
    )

    fig = px.bar(
        occupation_credit,
        x="Occupation",
        y="Credit_Utilization",
        title="Average Credit Utilization by Occupation"
    )
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Credit Limit Statistics")
        st.dataframe(
            filtered_df[["Existing_Credit_Limit"]].describe().round(2),
            use_container_width=True
        )

    with col2:
        st.subheader("Credit Score Statistics")
        st.dataframe(
            filtered_df[["Credit_Score"]].describe().T.round(2),
            use_container_width=True
        )

    fig = px.histogram(
        filtered_df,
        x="Credit_Score",
        nbins=30,
        marginal="box",
        title="Credit Score Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# TAB 5: LOANS
# =========================================================
with tabs[4]:
    st.header("Loan Portfolio Analysis")

    loan_counts = (
        filtered_df["Loan_Count"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    loan_counts.columns = ["Loan_Count", "Customers"]

    fig = px.bar(
        loan_counts,
        x="Loan_Count",
        y="Customers",
        title="Loan Portfolio"
    )
    st.plotly_chart(fig, use_container_width=True)

    loan_summary = (
        filtered_df
        .groupby("Loan_Count")[["Annual_Income", "Credit_Score"]]
        .mean()
        .round(2)
        .reset_index()
    )

    st.subheader("Average Income and Credit Score by Loan Count")
    st.dataframe(loan_summary, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(
            loan_summary,
            x="Loan_Count",
            y="Annual_Income",
            markers=True,
            title="Annual Income vs Loan Count"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.line(
            loan_summary,
            x="Loan_Count",
            y="Credit_Score",
            markers=True,
            title="Credit Score vs Loan Count"
        )
        st.plotly_chart(fig, use_container_width=True)


# =========================================================
# TAB 6: RISK & FRAUD
# =========================================================
with tabs[5]:
    st.header("Risk, Defaults & Fraud Analysis")

    col1, col2 = st.columns(2)

    with col1:
        default_summary = (
            filtered_df
            .groupby("Employment_Type", as_index=False)["Number_of_Defaults"]
            .mean()
            .sort_values("Number_of_Defaults", ascending=False)
        )

        fig = px.bar(
            default_summary,
            x="Employment_Type",
            y="Number_of_Defaults",
            title="Average Number of Defaults by Employment Type"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(
            filtered_df,
            x="Credit_Score",
            y="Avg_Monthly_Spending",
            color="Fraud_Flag",
            opacity=0.65,
            title="Credit Score vs Average Monthly Spending"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Payment Behaviour by Employment Type")

    payment_summary = (
        filtered_df
        .groupby("Employment_Type")[
            ["Missed_Payments", "Late_Payment_Count", "Number_of_Defaults"]
        ]
        .mean()
        .round(2)
    )

    st.dataframe(payment_summary, use_container_width=True)

    st.subheader("Fraud Flag Analysis")

    fraud_summary = (
        filtered_df
        .groupby("Fraud_Flag")[["Avg_Monthly_Spending", "Credit_Score"]]
        .mean()
        .round(2)
    )

    st.dataframe(fraud_summary, use_container_width=True)

    fraud_counts = (
        filtered_df["Fraud_Flag"]
        .value_counts()
        .reset_index()
    )
    fraud_counts.columns = ["Fraud_Flag", "Customers"]

    fig = px.pie(
        fraud_counts,
        names="Fraud_Flag",
        values="Customers",
        hole=0.45,
        title="Fraud Flag Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)


# =========================================================
# TAB 7: DATA
# =========================================================
with tabs[6]:
    st.header("Customer Dataset")

    st.write(
        f"Showing **{len(filtered_df):,}** filtered records "
        f"out of **{len(df):,}** total records."
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=550
    )

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Filtered Data as CSV",
        data=csv,
        file_name="financial_analysis_filtered.csv",
        mime="text/csv"
    )


# =========================================================
# TAB 8: CORRELATION
# =========================================================
with tabs[7]:
    st.header("Correlation Matrix")

    numeric_df = filtered_df.select_dtypes(include="number")

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Numerical Feature Correlation Matrix"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Strongest Correlations")

    corr_pairs = corr.where(
        np.triu(np.ones(corr.shape), k=1).astype(bool)
    ).stack().reset_index()

    corr_pairs.columns = ["Feature 1", "Feature 2", "Correlation"]

    corr_pairs["Absolute_Correlation"] = corr_pairs["Correlation"].abs()

    corr_pairs = (
        corr_pairs
        .sort_values("Absolute_Correlation", ascending=False)
        .head(15)
        .drop(columns="Absolute_Correlation")
        .reset_index(drop=True)
    )

    st.dataframe(
        corr_pairs.style.format({"Correlation": "{:.3f}"}),
        use_container_width=True
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption(
    "Financial Performance Analysis Dashboard | "
    "Converted from the provided Jupyter Notebook"
)
