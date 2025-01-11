FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Upgrade pip to the latest version for better dependency resolution
RUN pip install --upgrade pip

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r backend/requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "backend/app.py"]