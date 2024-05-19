import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Function to dynamically set environment variables within the Streamlit app
def set_api_keys(openai_api_key, langchain_api_key):
    os.environ["OPENAI_API_KEY"] = openai_api_key
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

# Streamlit framework
st.title('Langchain Demo With OpenAI API Made by DKB')

# API keys input section
st.sidebar.title("API Keys Configuration")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
langchain_api_key = st.sidebar.text_input("Langchain API Key", type="password")

if openai_api_key and langchain_api_key:
    set_api_keys(openai_api_key, langchain_api_key)
    st.sidebar.success("API keys are set!")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Input text for the query
input_text = st.text_input("Search the topic you want")

# OpenAI LLM 
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)
