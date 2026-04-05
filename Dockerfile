FROM debian:stable-slim

WORKDIR /app

RUN apt update && apt install -y wget tar openssl ca-certificates

# تحميل mtg
RUN wget https://github.com/9seconds/mtg/releases/download/v2.2.7/mtg-2.2.7-linux-amd64.tar.gz

RUN tar -xzf mtg-2.2.7-linux-amd64.tar.gz
RUN mv mtg-2.2.7-linux-amd64/mtg /usr/local/bin/mtg
RUN chmod +x /usr/local/bin/mtg

# تشغيل البروكسي
CMD sh -c 'SECRET=$(openssl rand -hex 16); mtg run $SECRET 0.0.0.0:8080 www.cloudflare.com'
