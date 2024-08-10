import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# # Set your Google API key
# os.environ["GOOGLE_API_KEY"] = "your_google_api_key"

# Function to return the response
def load_answer(question):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    answer = llm.invoke(question)
    return answer.content

# App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

# Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()
submit = st.button('Generate')

# If generate button is clicked
if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response)
