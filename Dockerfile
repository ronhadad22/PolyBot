FROM python:3.10
WORKDIR /PolyBot
COPY bot.py bot.py
COPY utils.py utils.py
COPY requirements.txt .requirements.txt
COPY .telegramToken  .telegramToken
COPY .gitifnore .gitignore 
RUN pip install -r .requirements.txt
CMD ["python3", "bot.py"]
