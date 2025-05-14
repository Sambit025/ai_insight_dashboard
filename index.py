import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# App Title
st.title("📊 AI-Based Insight Generator")
st.markdown("Upload a CSV file and let AI generate insights and visualizations from your data.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Preview of Data")
    st.dataframe(df.head())

    st.subheader("📈 Basic Summary Statistics")
    st.write(df.describe(include="all"))

    st.subheader("🧠 AI-Generated Insights")

    # Prepare prompt
    sample = df.sample(min(100, len(df))) if len(df) > 100 else df
    prompt = f"""
    You are a data analyst assistant.
    Analyze the following dataset and provide:
    1. Key insights
    2. Trends or patterns
    3. Anomalies (if any)
    4. Suggestions for useful visualizations

    Dataset (first few rows):
    {sample.to_csv(index=False)}
    """

    try:
        with st.spinner("Generating insights using AI..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert data analyst."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600
            )
            ai_response = response.choices[0].message.content
            st.markdown(ai_response)
    except Exception as e:
        st.error(f"Failed to generate insights: {e}")

    st.subheader("📊 Create Your Own Visualizations")

    chart_type = st.selectbox("Select Chart Type", ["Scatter Plot", "Histogram", "Line Chart", "Bar Chart", "Box Plot"])

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if len(numeric_cols) == 0:
        st.warning("No numeric columns available for charting.")
    else:
        x_axis = st.selectbox("Select X-axis", numeric_cols)
        y_axis = st.selectbox("Select Y-axis (if applicable)", ["None"] + numeric_cols)

        if chart_type == "Scatter Plot" and y_axis != "None":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        elif chart_type == "Histogram":
            fig = px.histogram(df, x=x_axis, title=f"Histogram of {x_axis}")
            st.plotly_chart(fig)
        elif chart_type == "Line Chart" and y_axis != "None":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Chart: {x_axis} over {y_axis}")
            st.plotly_chart(fig)
        elif chart_type == "Bar Chart" and y_axis != "None":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart: {x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        elif chart_type == "Box Plot" and y_axis != "None":
            fig = px.box(df, x=x_axis, y=y_axis, title=f"Box Plot: {x_axis} by {y_axis}")
            st.plotly_chart(fig)
        else:
            st.info("Please select both X and Y axes for this chart type.")
