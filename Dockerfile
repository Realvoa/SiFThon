FROM telegrammessenger/proxy:latest

RUN apt-get update && apt-get install -y xxd

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
