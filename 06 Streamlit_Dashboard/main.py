import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title("Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe()) 

    st.subheader("Filter Data")
    colmuns = df.columns.tolist()
    selected_columns = st.selectbox("Select Colmun to filter by",colmuns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Selet value", unique_values)

    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis", colmuns)
    y_column = st.selectbox("Select y-axis", colmuns)

    if st.button("Plot Data"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload...")
