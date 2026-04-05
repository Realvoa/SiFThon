#!/bin/bash

SECRET=dd$(head -c 16 /dev/urandom | xxd -ps)

echo "================================="
echo "MTProto Proxy Started "
echo "SECRET: $SECRET"
echo "================================="

./proxy-multi -p 8888 -H 443 -S $SECRET
