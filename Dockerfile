FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y git build-essential curl

# تحميل MTProxy
RUN git clone https://github.com/TelegramMessenger/MTProxy.git

WORKDIR /app/MTProxy
RUN make

WORKDIR /app

COPY app.py .

CMD ["python","app.py"]
