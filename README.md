# Pagila Python Reporting

## Overview
This is a Streamlit reporting application utilizing the Pagila PostgreSQL database. It generates visualizations for rental categories and trends over time.

## AI Usage Documentation
**Tool Used:** Gemini 

**Prompts Used:**
1. "Create a Streamlit app that connects to PostgreSQL and shows a bar chart of film categories."
2. "Write a SQL query to group rentals by year and month from the view vw_rental_analysis."

**Learnings:**
- I learned how to use `pandas.read_sql` to pull data directly into a dataframe.
- I learned how to use `plotly.express` for interactive charts.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run app: `streamlit run app.py`
