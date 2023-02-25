FROM python:3.8.12-slim-buster
WORKDIR /PolyApp
COPY . .
COPY requirements.txt requirements.txt
COPY .telegramToken .telegramToken
RUN pip3 install -r requirements.txt
CMD ["python3", "bot.py"]