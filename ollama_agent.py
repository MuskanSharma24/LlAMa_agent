# import requests
# import json
# import ast
# from langchain_core.messages.human import HumanMessage

# class OllamaJSONModel:
#     def __init__(self, temperature=0, model="llama3:instruct"):
#         self.headers = {"Content-Type": "application/json"}
#         self.model_endpoint = "http://localhost:11434/api/generate"
#         self.temperature = temperature
#         self.model = model

#     def invoke(self, messages):

#         system = messages[0]["content"]
#         user = messages[1]["content"]

#         payload = {
#                 "model": self.model,
#                 "prompt": user,
#                 "format": "json",
#                 "system": system,
#                 "stream": False,
#                 "temperature": 0,
#             }
        
#         try:
#             request_response = requests.post(
#                 self.model_endpoint, 
#                 headers=self.headers, 
#                 data=json.dumps(payload)
#                 )
            
#             print("REQUEST RESPONSE", request_response)
#             request_response_json = request_response.json()
#             # print("REQUEST RESPONSE JSON", request_response_json)
#             response = json.loads(request_response_json['response'])
#             response = json.dumps(response)

#             response_formatted = HumanMessage(content=response)

#             return response_formatted
#         except requests.RequestException as e:
#             response = {"error": f"Error in invoking model! {str(e)}"}
#             response_formatted = HumanMessage(content=response)
#             return response_formatted

# class OllamaModel:
#     def __init__(self, temperature=0, model="llama3:instruct"):
#         self.headers = {"Content-Type": "application/json"}
#         self.model_endpoint = "http://localhost:11434/api/generate"
#         self.temperature = temperature
#         self.model = model

#     def invoke(self, messages):

#         system = messages[0]["content"]
#         user = messages[1]["content"]

#         payload = {
#                 "model": self.model,
#                 "prompt": user,
#                 "system": system,
#                 "stream": False,
#                 "temperature": 0,
#             }
        
#         try:
#             request_response = requests.post(
#                 self.model_endpoint, 
#                 headers=self.headers, 
#                 data=json.dumps(payload)
#                 )
            
#             print("REQUEST RESPONSE JSON", request_response)

#             request_response_json = request_response.json()['response']
#             response = str(request_response_json)
            
#             response_formatted = HumanMessage(content=response)

#             return response_formatted
#         except requests.RequestException as e:
#             response = {"error": f"Error in invoking model! {str(e)}"}
#             response_formatted = HumanMessage(content=response)
#             return response_formatted



# import requests
# import json
# from time import sleep
# from requests.exceptions import RequestException

# class OllamaJSONModel:
#     def __init__(self, temperature=0, model="llama3:instruct"):
#         self.headers = {"Content-Type": "application/json"}
#         self.model_endpoint = "http://localhost:11434/api/generate"
#         self.temperature = temperature
#         self.model = model

#     def invoke(self, messages):
#         system = messages[0]["content"]
#         user = messages[1]["content"]

#         payload = {
#             "model": self.model,
#             "prompt": user,
#             "format": "json",
#             "system": system,
#             "stream": False,
#             "temperature": 0,
#         }

#         try:
#             request_response = requests.post(
#                 self.model_endpoint,
#                 headers=self.headers,
#                 data=json.dumps(payload)
#             )

#             request_response_json = request_response.json()

#             if 'response' in request_response_json:
#                 response = request_response_json['response']
#                 return response
#             else:
#                 return {"error": "Response format error: 'response' key not found"}

#         except requests.RequestException as e:
#             return {"error": f"Error in invoking model! {str(e)}"}

# class OllamaModel:
#     def __init__(self, temperature=0, model="llama3:instruct"):
#         self.headers = {"Content-Type": "application/json"}
#         self.model_endpoint =  
#             "llama3": "/llama3/api/generate",
#             "openapi": "/openapi",
#             "talviy": "/talviy",
#         self.temperature = temperature
#         self.model = model

#     def invoke(self, messages):
#         system = messages[0]["content"]
#         user = messages[1]["content"]

#         payload = {
#             "model": self.model,
#             "prompt": user,
#             "system": system,
#             "stream": False,
#             "temperature": 0,
#         }

#         try:
#             request_response = requests.post(
#                 self.model_endpoint,
#                 headers=self.headers,
#                 data=json.dumps(payload)
#             )

#             request_response_json = request_response.json()

#             if 'response' in request_response_json:
#                 response = request_response_json['response']
#                 return response
#             else:
#                 return {"error": "Response format error: 'response' key not found"}

#         except requests.RequestException as e:
#             return {"error": f"Error in invoking model! {str(e)}"}

# def main():
#     json_model = OllamaJSONModel()
#     normal_model = OllamaModel()

#     print("Welcome to Ollama Agent!")
#     print("Type 'exit' to quit.")

#     while True:
#         user_message = input("You: ")

#         if user_message.lower() == 'exit':
#             print("Goodbye!")
#             break

#         # Use the same system message for both models for simplicity
#         system_message = "This is the system prompt."

#         messages = [
#             {"content": system_message},
#             {"content": user_message}
#         ]

#         try:
#             json_response = json_model.invoke(messages)
#             print("Ollama JSON Model:", json_response)
#         except RequestException as json_error:
#             print("Error invoking Ollama JSON model:", json_error)

#         try:
#             normal_response = normal_model.invoke(messages)
#             print("Ollama Model:", normal_response)
#         except RequestException as normal_error:
#             print("Error invoking Ollama model:", normal_error)

#         sleep(1)

# if __name__ == "__main__":
#     main()




import os 
from dotenv import load_dotenv
load_dotenv()

import requests
import json

class LanggraphChatbot:
    def __init__(self, api_key, model="default"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://app.tavily.com"
        self.endpoint = "/chat"

    def send_message(self, message):
        url = self.base_url + self.endpoint
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "message": message
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=data,
                verify=True  
            )
            if response.status_code == 200:
                return response.json()["response"]
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.RequestException as e:
            return f"Request error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Langgraph API key
    api_key = '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'
    chatbot = LanggraphChatbot(api_key)

    # Example conversation loop
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = chatbot.send_message(user_input)
        print(f"Langgraph Bot: {response}")

import requests

url = 'https://app.tavily.com/chat'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'
}
data = {
    'model': 'default',
    'message': 'Hello, Langgraph!'
}

try:
    response = requests.post(url, headers=headers, json=data, verify=True)
    if response.status_code == 200:
        print(response.json()['response'])
    else:
        print(f"Error {response.status_code}: {response.text}")
        # Log the full response content for debugging purposes
        print(f"Response content: {response.content}")
except requests.RequestException as e:
    print(f"Request error: {str(e)}")
