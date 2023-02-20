FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set environment variables
ENV TELEGRAM_BOT_TOKEN=5830256501:AAEw2SQ98GeG9mI5Ze2Soi_aupyFL5CaMI0

#Run the command to start the bot

CMD ["python3", "bot.py"]