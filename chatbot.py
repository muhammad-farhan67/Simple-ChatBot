import streamlit as st
import google.generativeai as genai
import os

# Configure API Key
Google_API_KEY = "AIzaSyA76y4VjfH7Ara7qo3uH6binRS6ixAMgfc"
genai.configure(api_key=Google_API_KEY)
# Model initiation
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit UI Config
st.set_page_config(page_title="Chatbot with Google Generative AI", page_icon="🤖", layout="centered")

# Main Page
st.markdown("<h1 style='text-align: center;'>🤖 Simple ChatBot 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>Powered By Google Generative AI</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #f2f2f2;'>", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state["history"] = []

# Chat Form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your prompt:", "", max_chars=2000, placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = getResponseFromModel(user_input)
            st.session_state.history.append((user_input, response))
            st.write(response)
        else:
            st.warning("Please enter a prompt to continue.")

# Display Chat History
st.markdown("<hr style='border: 2px solid #f2f2f2;'>", unsafe_allow_html=True)
if st.session_state["history"]:
    for i, (user_query, bot_response) in enumerate(reversed(st.session_state["history"])):
        st.write(f"**You:** {user_query}")
        st.write(f"**Bot:** {bot_response}")
        if i < len(st.session_state["history"]) - 1:
            st.markdown("<hr style='border: 1px dashed #ccc;'>", unsafe_allow_html=True)

# Footer
st.markdown("<hr style='border: 2px solid #f2f2f2;'>", unsafe_allow_html=True)
st.markdown("<footer style='text-align: center;'>© 2024 ChatBot. All Rights Reserved.</footer>", unsafe_allow_html=True)