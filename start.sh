#!/bin/bash

PORT=${PORT:-8080}

SECRET=dd$(head -c 16 /dev/urandom | xxd -p)

echo "=========================="
echo "MTProto Proxy Started 🗿"
echo "PORT: $PORT"
echo "SECRET: $SECRET"
echo "=========================="

/mtproto-proxy -u nobody -p 8888 -H $PORT -S $SECRET
