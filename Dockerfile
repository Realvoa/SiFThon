FROM debian:stable-slim

WORKDIR /app

RUN apt update && apt install -y wget tar ca-certificates

# تحميل mtg
RUN wget https://github.com/9seconds/mtg/releases/download/v2.2.7/mtg-2.2.7-linux-amd64.tar.gz

# فك الضغط
RUN tar -xzf mtg-2.2.7-linux-amd64.tar.gz

# نقل الملف من داخل المجلد
RUN mv mtg-2.2.7-linux-amd64/mtg /usr/local/bin/mtg

RUN chmod +x /usr/local/bin/mtg

# تشغيل البروكسي
CMD sh -c 'SECRET=$(head -c 16 /dev/urandom | xxd -ps); mtg run --bind 0.0.0.0:8080 --secret $SECRET --domain www.cloudflare.com'
