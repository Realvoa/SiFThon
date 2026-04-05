#!/bin/bash

PORT=${PORT:-8080}

SECRET=dd$(head -c 16 /dev/urandom | xxd -ps)

echo "MTProto Proxy Started"
echo "Secret: $SECRET"

./proxy-multi -p 8888 -H $PORT -S $SECRET
