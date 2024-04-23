## Integrate our code OpenAI API
import json
import os
from constants import openai_key
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework

st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic you want")

# Prompt Templates

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}  under 60 words"

)

## OPENAI LLMS
llm = OpenAI(api_key=openai_key, temperature=0.8)

chain = LLMChain(llm = llm, prompt=first_input_prompt, verbose=True)


if input_text:
    st.write(chain.invoke(input_text)["text"])
