from langchain_groq import ChatGroq

# Initialize the model with the correct model name and API key
model = ChatGroq(model='llama-3.1-70b-versatile', 
                 api_key='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')

# Define the query
query = 'What is the capital of India?'

# Invoke the model with the query and get the result
result = model.invoke(query)

# Print the content of the result
print(result['content'])
