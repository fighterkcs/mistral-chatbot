# streamlit.py
import streamlit as st
import os
from config import get_mistral_answer
from dotenv import load_dotenv
load_dotenv()
HF_token = os.getenv("HF_token")

st.set_page_config(page_title="Mistral Chat Bot", page_icon="🤖")

st.title("🤖 Mistral Chat Bot")

st.markdown("You can ask any of your quirey here!")
question = st.text_area("Enter your quirey here") 

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a valid query.")
    elif not HF_token:
        st.error("No Hugging Face token found. Please check your .env file and variable name.")
    else:
        try:
            answer = get_mistral_answer(HF_token, question)
            if answer:
                st.success("Thank you for asking your query")
                st.write(answer)
            else:
                st.error("No answer received from the model. Please try again later.")
        except Exception as e:
            st.error(f"Error: {e}")