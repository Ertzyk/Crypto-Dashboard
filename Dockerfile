# 1. Use the official Python image
FROM python:3.9

# 2. Set the working directory
WORKDIR /app

# 3. Copy your project files into the container
COPY . .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the Streamlit port
EXPOSE 8501

# 6. Command to run Streamlit
CMD ["streamlit", "run", "streamlit_app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
