FROM python:3.9
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install venv and create a virtual environment
RUN python -m venv /opt/venv

# Ensure the virtual environment is used
ENV PATH="/opt/venv/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 5050 available
EXPOSE 5050

# Define environment variable
ENV FLASK_APP=flask_app.py

# Run app.py when the container launches
CMD ["python", "flask_app.py"]