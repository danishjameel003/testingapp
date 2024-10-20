# app.py
import streamlit as st
import pandas as pd

# Title
st.title("Simple Data Analysis App")

# Upload CSV data
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataset
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Show columns
    st.subheader("Data Columns")
    st.write(df.columns)

    # Plot data
    st.subheader("Visualize Data")
    selected_column = st.selectbox("Select a column to visualize", df.columns)
    st.line_chart(df[selected_column])

else:
    st.write("Please upload a CSV file to analyze.")
