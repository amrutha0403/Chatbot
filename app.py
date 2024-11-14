from langchain_groq import ChatGroq
import streamlit as st

# Initialize the model with the correct model name and API key
model = ChatGroq(model='llama-3.1-70b-versatile', 
                 api_key='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')


#query = 'What is the capital of India?'

st.title("Chatbot!!!!")
#query=str(input('what is your query?'))

query=st.text_input('what is your query?')

result = model.invoke(query)


#print(result.content)
st.write(result.content)