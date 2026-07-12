import streamlit as st
import requests
import json

st.set_page_config(page_title="Country API", layout="centered")

st.title("Country API")

country = st.text_input("Введите название страны", "russia", key="country_input")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Полная информация", use_container_width=True):
        st.session_state.endpoint = ""
with col2:
    if st.button("Столица", use_container_width=True):
        st.session_state.endpoint = "/capital"
with col3:
    if st.button("Население", use_container_width=True):
        st.session_state.endpoint = "/population"
with col4:
    if st.button("Флаг", use_container_width=True):
        st.session_state.endpoint = "/flag"

if 'endpoint' in st.session_state:
    endpoint = st.session_state.endpoint
    if country:
        with st.spinner("Запрос к API..."):
            try:
                response = requests.get(f"http://127.0.0.1:8000/country/{country}{endpoint}", timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    st.success("Успешно!")
                    st.json(data)
                else:
                    st.error(f"Ошибка {response.status_code}")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Не удалось подключиться к серверу.\n\nУбедитесь, что запущен:\n`uvicorn main:app --reload`")
                st.info(str(e))
    else:
        st.warning("Введите название страны")

st.caption("Streamlit GUI для CountryAPI")