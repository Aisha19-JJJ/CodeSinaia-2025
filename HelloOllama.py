import ollama

# Specify the model name
model_name = "gemma3:1b"

# Define the prompt
prompt = input()

# Send the prompt to the model and get the response
answer=ollama.chat(model=model_name, messages=[{'role': 'user', 'content':prompt}])
answer_text=answer['message']['content']
#response = ollama.generate(model=model_name, prompt=prompt)

# Print the response
#print(type(response))
#print(response.response)

#rint(type(answer))
print(answer_text)