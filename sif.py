import os
import random
import time

def secret():
    return ''.join(random.choice("abcdef0123456789") for _ in range(32))

sec = secret()
port = 8080

ip = os.popen("curl -s ifconfig.me").read().strip()

print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("⚡ SiFThon MTProto Proxy")
print("📢 Channel : https://t.me/sifthon")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━")

print("Server:", ip)
print("Port:", port)
print("Secret:", sec)

print("\nTelegram Link:")
print(f"https://t.me/proxy?server={ip}&port={port}&secret={sec}")

print("\nProxy Starting...")

os.system(f"./objs/bin/mtproto-proxy -u nobody -p 8888 -H {port} -S {sec} --aes-pwd proxy-secret proxy-multi.conf -M 1 &")

print("Proxy Running...")

while True:
    print("Proxy Alive ✔")
    time.sleep(60)
