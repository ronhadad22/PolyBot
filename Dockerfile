FROM python:3.8.12-slim-buster

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV TOKEN_PATH /app/.telegramToken

CMD ["python3", "bot.py"]
