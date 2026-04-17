import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🛒 E-Commerce Data Analysis Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)

    st.write("### 📊 Raw Data")
    st.write(df.head())

    # Data Cleaning
    df = df.dropna()

    # Convert Date
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Create TotalPrice
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    # Extract Month
    df['Month'] = df['InvoiceDate'].dt.month

    # ==========================
    # 📊 Monthly Sales
    st.write("## 📈 Monthly Sales Trend")
    monthly_sales = df.groupby('Month')['TotalPrice'].sum()

    fig1, ax1 = plt.subplots()
    monthly_sales.plot(kind='bar', ax=ax1)
    st.pyplot(fig1)

    # ==========================
    # 📊 Top Products
    st.write("## 🏆 Top 5 Selling Products")
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(5)

    fig2, ax2 = plt.subplots()
    top_products.plot(kind='bar', ax=ax2)
    st.pyplot(fig2)

    # ==========================
    # 📊 Country Revenue
    st.write("## 🌍 Top 5 Countries by Revenue")
    country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(5)

    fig3, ax3 = plt.subplots()
    country_sales.plot(kind='bar', ax=ax3)
    st.pyplot(fig3)

else:
    st.write("👆 Upload a CSV file to begin")