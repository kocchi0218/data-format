import streamlit as st
import pandas as pd

# データのアップロード
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    # データの抽出
    st.subheader('Extracted Data')
    select_line = st.selectbox('Select Line', data['顧客名'].unique())
    selected_data = data[data['顧客名'] == select_line]

    select_breed = st.selectbox('Select Breed', selected_data['顧客名'].unique())
    selected_data = selected_data[selected_data['顧客名'] == select_breed][['地域', 'メールアドレス']]

    st.write(selected_data)
