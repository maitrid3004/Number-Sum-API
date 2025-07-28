# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Flask
RUN pip install flask

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
