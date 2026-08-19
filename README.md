# Financial Performance Analysis

## Project Overview

**Financial Performance Analysis** is a data analytics and visualization project developed using Python and Jupyter Notebook. The project analyzes customer-level financial, income, savings, investment, credit, loan, debt, payment, and fraud-related information to identify financial patterns and support data-driven insights.

The analysis is performed on a customer banking/credit dataset containing **5,000 customer records and 28 attributes**. The notebook uses Pandas, NumPy, Matplotlib, and Seaborn for data handling, statistical analysis, and visualization.

The project has also been converted into an interactive **Streamlit dashboard**, allowing users to upload the Excel dataset, apply filters, explore financial KPIs, visualize relationships, inspect customer records, and download filtered data.

---

## Project Objectives

The main objectives of this project are:

- Analyze customer income and savings behaviour.
- Examine the relationship between monthly income and savings.
- Analyze investment behaviour in relation to income.
- Study EMI and debt-to-income patterns.
- Understand credit utilization and credit limits.
- Analyze credit scores and loan portfolios.
- Examine missed payments, late payments, and defaults.
- Investigate fraud-related customer behaviour.
- Compare financial characteristics across employment types and occupations.
- Identify relationships among numerical financial variables using correlation analysis.
- Provide an interactive dashboard for exploring the analysis.

---

## Dataset

The project uses the Excel dataset:

```text
Credir_Card_Bank.xlsx
```

The dataset contains:

- **5,000 customer records**
- **28 columns**

The notebook loads the dataset using:

```python
df = pd.read_excel('../Dataset/Credir_Card_Bank.xlsx')
```

### Important Dataset Attributes

The dataset contains customer and financial attributes including:

| Category | Variables |
|---|---|
| Customer Information | `Customer_ID`, `Age`, `Gender` |
| Employment | `Employment_Type`, `Occupation` |
| Income | `Monthly_Income`, `Annual_Income` |
| Credit Profile | `Credit_Score`, `Credit_Utilization`, `Credit_Limit` |
| Banking Relationship | `Years_With_Bank`, `Existing_Credit_Cards` |
| Savings & Finance | `Savings_Balance`, `Investment_Value` |
| Debt | `EMI_Per_Month`, `Debt_To_Income_Ratio` |
| Credit History | `Credit_History_Years` |
| Payment Behaviour | `Missed_Payments`, `Late_Payment_Count` |
| Defaults | `Number_of_Defaults` |
| Verification | `PAN_Verified`, `KYC_Status` |
| Risk | `Fraud_Flag` |
| Residential Information | `Residential_Status` |

> **Note:** The README describes the fields visible and used in the supplied notebook. It does not assume additional columns or analyses that are not supported by the source notebook.

---

## Technologies Used

### Programming Language

- Python 3.x

### Development Environment

- Jupyter Notebook
- Streamlit

### Python Libraries

| Library | Purpose |
|---|---|
| Pandas | Data loading, manipulation, grouping and analysis |
| NumPy | Numerical calculations and derived metrics |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Plotly | Interactive Streamlit visualizations |
| Streamlit | Interactive web dashboard |
| OpenPyXL | Reading Excel `.xlsx` files |
| Statsmodels | Statistical trendline support used by Plotly |

---

## Project Structure

Recommended project structure:

```text
Financial-Performance-Analysis/
│
├── Dataset/
│   └── Credir_Card_Bank.xlsx
│
├── Financial_Performance_Analysis_Updated (1).ipynb
│
├── financial_performance_app.py
│
├── requirements.txt
│
└── README.md
```

### File Description

| File | Description |
|---|---|
| `Financial_Performance_Analysis_Updated (1).ipynb` | Original Jupyter Notebook containing the financial analysis |
| `financial_performance_app.py` | Interactive Streamlit dashboard converted from the notebook |
| `Credir_Card_Bank.xlsx` | Input customer financial dataset |
| `requirements.txt` | Python dependencies required for the Streamlit application |
| `README.md` | Project documentation |

---

# Jupyter Notebook Analysis

## 1. Data Loading

The notebook begins by importing the core Python libraries:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
```

The Excel dataset is then loaded into a Pandas DataFrame.

```python
df = pd.read_excel('../Dataset/Credir_Card_Bank.xlsx')
```

The loaded dataset contains 5,000 rows and 28 columns.

---

## 2. Income vs Savings Analysis

A derived metric named `Savings_Percentage` is created to measure savings relative to monthly income.

```python
df["Savings_Percentage"] = (
    df["Savings_Balance"] /
    df["Monthly_Income"]
) * 100
```

### Purpose

This metric helps evaluate how much of a customer's monthly income is represented by their savings balance.

### Analysis Areas

- Monthly income
- Savings balance
- Savings percentage
- Income-to-savings relationship
- Customer savings behaviour

---

## 3. Income vs Investment Analysis

Investment behaviour is analyzed in relation to customer income.

The analysis considers:

- Monthly income
- Annual income
- Investment value
- Investment percentage

The purpose is to understand whether customers with different income levels demonstrate different investment patterns.

---

## 4. EMI and Debt Analysis

The project examines customer debt obligations using:

- Monthly EMI
- Debt-to-income ratio
- Income
- Loan-related information

The **Debt-to-Income Ratio (DTI)** is particularly useful for understanding the relative burden of debt compared with income.

The analysis can be used to identify customer groups with comparatively higher debt exposure.

---

## 5. Credit Utilization Analysis

Credit utilization is analyzed to understand how customers use their available credit.

Important variables include:

```text
Credit_Utilization
Credit_Limit
Existing_Credit_Limit
Credit_Score
```

The project visualizes the distribution of credit utilization and compares credit behaviour across customer groups.

---

## 6. Credit Score Analysis

Credit score distribution is analyzed to understand the overall credit profile of customers.

The analysis can be used to examine:

- Credit score distribution
- Average credit score
- Credit score differences across customer groups
- Relationship between credit score and other financial variables

---

## 7. Loan Portfolio Analysis

The project analyzes the customer's loan portfolio using `Loan_Count`.

Analysis includes:

- Number of loans held by customers
- Income across different loan-count groups
- Credit score across different loan-count groups

This provides a view of how loan exposure relates to customer financial characteristics.

---

## 8. Payment Behaviour and Default Analysis

The project examines customer payment behaviour using:

```text
Missed_Payments
Late_Payment_Count
Number_of_Defaults
```

These variables help identify patterns in payment performance and default behaviour.

The analysis also compares default and payment characteristics across employment groups.

---

## 9. Fraud Analysis

The dataset contains a `Fraud_Flag` attribute.

The project uses this variable to explore potential differences between customers marked with different fraud statuses.

Fraud analysis includes:

- Fraud flag distribution
- Credit score comparison
- Spending behaviour
- Employment-related comparisons

The project is an exploratory analytics system; the presence of a fraud flag should not be interpreted as an independently verified fraud determination.

---

# Streamlit Dashboard

The notebook analysis was converted into an interactive Streamlit application.

## Dashboard Features

### 1. Key Financial Indicators

The dashboard provides KPI cards for metrics such as:

- Total Customers
- Average Monthly Income
- Total Savings
- Average Savings
- Total Investments
- Average EMI
- Average Debt-to-Income Ratio
- Average Credit Utilization
- Average Credit Score
- Average Existing Credit Limit

---

### 2. Interactive Filters

The sidebar provides filters for:

- Employment Type
- Occupation

All dashboard analyses update according to the selected filters.

---

### 3. Income & Savings

Interactive visualizations include:

- Income vs Savings scatter plot
- Savings percentage distribution
- Employment-wise financial statistics
- Average savings by employment type

---

### 4. Investments

The investment section includes:

- Income vs investment scatter plot
- Investment percentage distribution
- Top occupations by average annual income

---

### 5. Debt & EMI

The dashboard provides:

- EMI distribution
- Debt-to-income ratio visualization
- EMI statistics
- Employment-wise DTI comparison

---

### 6. Credit Analysis

Credit analysis includes:

- Credit utilization distribution
- Existing credit limit distribution
- Occupation-wise credit utilization
- Credit score statistics
- Credit score distribution

---

### 7. Loan Portfolio

The loan section provides:

- Loan count distribution
- Annual income vs loan count
- Credit score vs loan count

---

### 8. Risk & Fraud

The risk section includes:

- Defaults by employment type
- Credit score vs average monthly spending
- Missed payment analysis
- Late payment analysis
- Fraud flag distribution

---

### 9. Customer Data

The dashboard provides an interactive filtered data table.

Users can also download the filtered dataset as CSV.

---

### 10. Correlation Analysis

The dashboard provides:

- Numerical correlation matrix
- Interactive heatmap
- Strongest correlation pairs

This helps identify relationships between financial variables.

---

# Installation

## 1. Clone or Download the Project

Place the project files in a single project directory.

Example:

```bash
git clone <your-repository-url>
cd Financial-Performance-Analysis
```

If the project is not hosted on GitHub, simply extract/download the project and open its folder.

---

## 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

The requirements file contains the packages needed for the Streamlit application.

---

# Running the Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Financial_Performance_Analysis_Updated (1).ipynb
```

Make sure the dataset is available at the path expected by the notebook:

```text
Dataset/Credir_Card_Bank.xlsx
```

Then execute the notebook cells sequentially.

---

# Running the Streamlit Application

From the project directory, run:

```bash
streamlit run financial_performance_app.py
```

Streamlit will start a local web server.

Open the displayed local URL in your browser.

The application provides an Excel uploader in the sidebar. Upload:

```text
Credir_Card_Bank.xlsx
```

The dashboard will automatically load the data and generate the interactive analysis.

---

# Dashboard Workflow

```text
Credir_Card_Bank.xlsx
        │
        ▼
   Data Upload
        │
        ▼
   Pandas DataFrame
        │
        ▼
Calculated Metrics
        │
        ├── Savings Percentage
        └── Investment Percentage
        │
        ▼
     Filters
        │
        ├── Employment Type
        └── Occupation
        │
        ▼
   Financial Analysis
        │
        ├── Income & Savings
        ├── Investments
        ├── Debt & EMI
        ├── Credit
        ├── Loans
        ├── Risk & Fraud
        └── Correlation
        │
        ▼
 Interactive Streamlit Dashboard
```

---

# Key Calculated Metrics

## Savings Percentage

```text
Savings Percentage =
(Savings Balance / Monthly Income) × 100
```

Implemented as:

```python
df["Savings_Percentage"] = (
    df["Savings_Balance"] /
    df["Monthly_Income"]
) * 100
```

## Investment Percentage

The Streamlit application additionally calculates:

```text
Investment Percentage =
(Investment Value / Monthly Income) × 100
```

with zero-income protection.

---

# Visualizations

The project uses several visualization techniques.

| Visualization | Purpose |
|---|---|
| Scatter Plot | Analyze relationships between financial variables |
| Histogram | Examine distributions |
| Box Plot | Identify spread and potential outliers |
| Bar Chart | Compare groups |
| Line Chart | Compare trends across ordered loan-count groups |
| Pie Chart | Show categorical distribution |
| Heatmap | Analyze numerical correlations |
| Data Table | Inspect individual customer records |
| KPI Cards | Provide high-level financial indicators |

---

# Example Insights That Can Be Derived

The dashboard can be used to investigate questions such as:

1. How does savings vary with monthly income?
2. Which employment groups have higher average savings?
3. Which occupations have higher average annual income?
4. How are investments distributed across income levels?
5. Which groups show higher debt-to-income ratios?
6. What is the distribution of credit utilization?
7. How does credit score vary across customers?
8. How does loan count relate to annual income?
9. How does loan count relate to credit score?
10. Which employment groups have higher average defaults?
11. How are missed and late payments distributed?
12. What is the distribution of fraud flags?
13. Which numerical variables have the strongest correlations?

The dashboard is designed to allow these questions to be explored interactively rather than relying only on static results.

---

# Data Quality and Interpretation Notes

- Financial amounts are treated as numerical variables.
- Categorical variables such as employment type, occupation, and fraud status are analyzed as groups.
- Derived percentages depend on the corresponding income values.
- Zero monthly income is protected against division-by-zero in the Streamlit implementation.
- Correlation measures statistical association and does not establish causation.
- A `Fraud_Flag` should be interpreted as a dataset-provided classification rather than independent proof of fraudulent activity.
- The notebook and dashboard should be interpreted within the scope and quality of the supplied dataset.

---

# Project Benefits

This project demonstrates practical skills in:

- Data loading and preprocessing
- Exploratory Data Analysis (EDA)
- Feature calculation
- Statistical summarization
- Financial data analysis
- Customer segmentation
- Credit analysis
- Risk analysis
- Data visualization
- Interactive dashboard development
- Python-based analytics
- Streamlit application development

---

# Future Enhancements

Potential extensions include:

- Machine-learning-based credit risk prediction.
- Customer segmentation using clustering.
- Interactive date-based analysis if temporal data is added.
- Automated financial risk scoring.
- Advanced anomaly detection.
- Predictive default analysis.
- Explainable AI for risk predictions.
- Database integration.
- User authentication.
- Cloud deployment.
- Automated report generation.
- Additional dashboard pages for customer-level profiling.

These are proposed enhancements and are not part of the current notebook analysis.

---

# Conclusion

The **Financial Performance Analysis** project provides a structured approach to understanding customer financial behaviour through exploratory data analysis and interactive visualization.

The original Jupyter Notebook establishes the analytical foundation using Python, Pandas, NumPy, Matplotlib, and Seaborn. The Streamlit implementation extends this work into an interactive dashboard where users can upload the source Excel dataset, filter customer groups, examine financial KPIs, explore relationships between variables, analyze credit and risk characteristics, and download filtered data.

The project therefore combines **Python-based EDA with an interactive business analytics interface**, making the analysis easier to explore, demonstrate, and present.

---

## Author

Jayesh Parate

**Financial Performance Analysis Project**

Developed using Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Streamlit.

---

## License

This project is intended for educational, academic, and analytical purposes. Dataset ownership and usage rights should be verified separately before public redistribution.
