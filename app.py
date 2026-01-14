import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# 1. Database Connection Configuration
# Replace these values with your specific local database credentials [cite: 86-91]
DB_CONFIG = {
    "host": "localhost",
    "database": "pagila.dwh",
    "user": "postgres",      # Change to your username
    "password": "SachuSachu543@"   # Change to your password
}

# Function to load data from PostgreSQL
def load_data(query):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        # Load directly into a pandas DataFrame [cite: 127]
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# App Title
st.title("Pagila DVD Rental Reporting")
st.write("DMAR Exercise - Winter Term 2025/26")

# --- REPORT 1: Rentals by Film Category ---
st.header("1. Rentals by Film Category")
st.write("Bar chart showing total rentals per category.")

# SQL Query for Report 1 [cite: 37-41]
query_category = """
    SELECT film_category,
           COUNT(*) AS total_rentals,
           SUM(rental_amount) AS total_revenue
    FROM vw_rental_analysis
    GROUP BY film_category
    ORDER BY total_rentals DESC;
"""

df_category = load_data(query_category)

if df_category is not None:
    # Create Bar Chart using Plotly [cite: 61]
    fig_bar = px.bar(
        df_category, 
        x='film_category', 
        y='total_rentals',
        title="Total Rentals by Category",
        color='total_revenue', # Added bonus: color by revenue
        labels={'film_category': 'Category', 'total_rentals': 'Rentals'}
    )
    st.plotly_chart(fig_bar)

# --- REPORT 2: Rental Trends Over Time ---
st.header("2. Rental Trends Over Time")
st.write("Line chart showing rental trends by month.")

# SQL Query for Report 2 [cite: 50-54]
query_trends = """
    SELECT year, month, 
           TO_DATE(year::text || '-' || month::text, 'YYYY-MM') as date_col,
           COUNT(*) AS total_rentals,
           SUM(rental_amount) AS total_revenue
    FROM vw_rental_analysis
    GROUP BY year, month
    ORDER BY year, month;
"""

df_trends = load_data(query_trends)

if df_trends is not None:
    # Create Line Chart using Plotly [cite: 46]
    fig_line = px.line(
        df_trends,
        x='date_col',
        y='total_rentals',
        title="Monthly Rental Trends",
        markers=True
    )
    st.plotly_chart(fig_line)