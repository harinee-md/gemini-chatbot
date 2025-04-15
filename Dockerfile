# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy everything to /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "gemini_call.py"]
