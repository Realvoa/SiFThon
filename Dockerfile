FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y git build-essential curl

RUN git clone https://github.com/TelegramMessenger/MTProxy.git

WORKDIR /app/MTProxy
RUN make

WORKDIR /app

COPY proxy.py .

CMD ["python","proxy.py"]
