# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create a virtual environment
RUN python -m venv $VIRTUAL_ENV

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Flask and requests within the virtual environment
RUN pip install --no-cache-dir flask requests

# Make port 5000 available to the world outside this container
EXPOSE 5020

# Define environment variable for M3U URL
ENV M3U_URL=""

# Run app.py when the container launches
CMD ["python", "app.py"]

