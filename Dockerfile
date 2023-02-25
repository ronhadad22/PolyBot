FROM python:3.8-slim-buster
WORKDIR /PolyBot
COPY . . 
COPY requirements.txt .requirements.txt
RUN pip install -r .requirements.txt
CMD ["python3", "bot.py"]
