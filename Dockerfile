FROM python:3.10

WORKDIR /app

RUN apt update && apt install -y wget

RUN wget https://github.com/9seconds/mtg/releases/latest/download/mtg-linux-amd64 -O mtg
RUN chmod +x mtg

COPY app.py .

CMD ["python","app.py"]
