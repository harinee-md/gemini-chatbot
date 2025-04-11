import google.generativeai as genai
import google.auth
from google.oauth2 import service_account

import os
from dotenv import load_dotenv

load_dotenv()  

#service account file path from the .env file
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")



if not SERVICE_ACCOUNT_FILE:
    raise ValueError("SERVICE_ACCOUNT_FILE environment variable is not set. Check your .env file.")


# This authenticates your script to use Google's services, including Gemini
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

genai.configure(credentials=credentials)
prompt = input("Enter the prompt: ")

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
response = model.generate_content(prompt)
print("Gemini Response:\n", response.text)
