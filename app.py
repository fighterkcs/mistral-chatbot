# streamlit.py
import streamlit as st
from config import get_mistral_answer

# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="Mistral Chatbot", page_icon="🤖")

st.title("🤖 Mistral Chatbot")
st.write("Ask me anything — powered by Hugging Face Mistral model!")

# 1️⃣ Token input (password style)
HF_token = st.text_input("Enter your Hugging Face Token:", type="password")

# 2️⃣ Question input
question = st.text_area("Enter your question:")

# 3️⃣ Submit button
if st.button("Get Answer"):
    if not HF_token:
        st.warning("Please enter your Hugging Face token.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking... ⏳"):
            try:
                answer = get_mistral_answer(HF_token, question)
                st.success("✅ Answer received!")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")
                