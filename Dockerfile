FROM python:3.10-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the project code.
COPY . .

# Default command to show CLI help (modify as needed).
CMD ["python", "main.py", "-h"]
