from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.0-pro-latest')

# Function to get response from the model
def get_response(query):
    response = model.generate_content(query)
    return response.text

# Initialize our streamplit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

## When submit is clicked
if submit:
    response = get_response(input)
    st.subheader("The Response is ")
    st.write(response)

