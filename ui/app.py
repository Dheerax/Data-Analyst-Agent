import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import DataAnalysisAgent
from core.llm import get_llm

st.set_page_config(page_title="Agent Aether", layout='wide')
st.title("Agent Aether Prototype")

uploaded_file = st.file_uploader( "Upload Your CSV file here",type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    st.session_state.llm = get_llm()
    st.session_state.agent = DataAnalysisAgent(st.session_state.llm)
    success = st.session_state.agent.init_agent(df)

    if success:
        query = st.text_input("Enter Your Query")
        if query:
            with st.spinner("Thinking.."):
                try:
                    result = st.session_state.agent.run_query(query)
                    st.success(result)
                except Exception as e:
                    st.error(f"{e}")
    else:
        st.error("Agent NOT Initialized!")

