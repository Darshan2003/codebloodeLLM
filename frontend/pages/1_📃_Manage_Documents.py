import streamlit as st
import base64
from src.utils import page_init
from src.database import get_doc_names, get_db
import pandas as pd
import requests
st.session_state['verif_email'] = 'kenneth@mail.com'

page_init()
st.markdown("# Manage Documents")
conn = get_db()
filesUrls = get_doc_names(conn, st.session_state['verif_email'])
name_len = len(st.session_state['verif_email'])
for i in filesUrls:
    with st.expander(i.split('/')[-1].replace(st.session_state['verif_email'], '')):
        pdf = requests.get(i).content
        pdf_base64 = base64.b64encode(pdf).decode('utf-8')
        st.markdown(
    F'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" type="application/pdf"></iframe>', unsafe_allow_html=True)
    
    # with st.expander(f"## {i}"):
        
        
    #     with open(i, "rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    #     # Embedding PDF in HTML
    #     pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'

    #     # Displaying File
    #     st.markdown(pdf_display, unsafe_allow_html=True)

st.button("Clear All", key=i)