# import ollama 

# response = ollama.chat(model="llama3",messages=[
#     {
#       "role" : "user",
#       "content": "what color is the water",                     
#     }
# ])
# print(response["message"]["content"])



import ollama

def chat_with_ollama():
    user_input = input("You: ")

    # Call ollama.chat with user input
    response = ollama.chat(model="llama3", messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ])

    # Print the response from ollama
    print("Langgraph Bot:", response["message"]["content"])

# Example usage:
if __name__ == "__main__":
    print("Welcome to the Langgraph Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        chat_with_ollama()
