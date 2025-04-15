import google.generativeai as genai
import google.auth
from google.oauth2 import service_account
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Service account file path from the .env file
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

if not SERVICE_ACCOUNT_FILE:
    raise ValueError("SERVICE_ACCOUNT_FILE environment variable is not set. Check your .env file.")

# This authenticates your script to use Google's services, including Gemini
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

# Configure Gemini with the credentials
genai.configure(credentials=credentials)

# Get the prompt from the user
prompt = input("Enter the prompt: ")

# Generate response using Gemini
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
response = model.generate_content(prompt)

# Print the Gemini response
print("Gemini Response:\n", response.text)