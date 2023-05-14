import streamlit as st
import pandas as pd
import numpy as np

# データのアップロード
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    # 列名の選択
    st.subheader('Choose Columns')

    selected_columns = st.multiselect('Select Columns', data.columns)
    selected_data = data[selected_columns]

    if selected_columns:
        st.subheader('Choose Values')
        for column in selected_columns:
            unique_values = data[column].unique()
            selected_values = st.multiselect(f'Select {column}', unique_values)
            if selected_values:
                selected_data = selected_data[selected_data[column].isin(selected_values)]

    numerical_columns = selected_data.select_dtypes(include=[np.number]).columns
    selected_data[numerical_columns] = selected_data[numerical_columns].apply(lambda x: x.round(0).astype(int))

    st.dataframe(selected_data, width=1000, height=500) # <- ここに追加します

    if selected_data.select_dtypes(include=[np.number]).columns.any():  # check if there is any number column
        st.subheader('Total')
        total = selected_data.select_dtypes(include=[np.number]).sum().sum()  # sum only number columns
        total = round(total)  # round to integer
        st.markdown(f'<h1 style="color: red;">{total}</h1>', unsafe_allow_html=True)  # display in large red font