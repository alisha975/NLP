import streamlit as st
from helper import get_qa_chain
from helper import create_vector_db
st.title("EasyChat")
btn = st.button("Create KnowledgeBase")
if btn:
    pass

question = st.text_input("Question: ")
if question:
    chain=get_qa_chain()
    response = chain(question)

    st.header("Answer: ")
    st.write(response["result"])
