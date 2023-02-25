FROM python:3.10 
WORKDIR /PolyApp
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]