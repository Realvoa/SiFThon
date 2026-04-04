import os
import random
import time

def secret():
    return ''.join(random.choice("abcdef0123456789") for _ in range(32))

sec = secret()
port = 8080

# تحميل البروكسي
os.system("git clone https://github.com/TelegramMessenger/MTProxy")
os.chdir("MTProxy")
os.system("make")

ip = os.popen("curl -s ifconfig.me").read().strip()

print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("⚡ MTProto Proxy")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━")

print("Server:", ip)
print("Port:", port)
print("Secret:", sec)

print("\nTelegram Link:")
print(f"https://t.me/proxy?server={ip}&port={port}&secret={sec}")

print("\nProxy Starting...")

os.system(f"./objs/bin/mtproto-proxy -u nobody -p 8888 -H {port} -S {sec} --aes-pwd proxy-secret proxy-multi.conf -M 1 &")

while True:
    print("Proxy Alive ✔")
    time.sleep(60)
