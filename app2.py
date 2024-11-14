from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.messages import SystemMessage, AIMessage,HumanMessage

# Initialize the model with the correct model name and API key
model = ChatGroq(model='llama-3.1-70b-versatile', 
                 api_key='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')

messages=[ ]

while True:
    query=str(input('what is your query?'))
    messages.append(HumanMessage(content=query))
    result=model.invoke(messages)
    print(result.content)
    messages.append(AIMessage(result.content))