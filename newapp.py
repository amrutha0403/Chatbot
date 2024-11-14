from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import streamlit as st

# Initialize the model with the correct model name and API key
model = ChatGroq(model='llama-3.1-70b-versatile', 
                 api_key='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')

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are flight attendent, if a plane is going to crash, then try to calm the paasengers"),
        ("user","{query}")
    ]
)
st.title("CHATBOT!!!!!")
query=st.text_input("Enter a query")

if query:
    formatted_prompt=prompt.format(query=query)
    response=model.invoke(formatted_prompt)
    st.write(response.content)
#You are flight attendent, if a plane is going to crash, then try to c
#("system","You are helpful assistant, please help the user with respecct to the query"),