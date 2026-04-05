import os
import random
import subprocess

def gen_secret():
    chars = "0123456789abcdef"
    return "dd" + "".join(random.choice(chars) for _ in range(30))

PORT = os.environ.get("PORT", "8080")
SECRET = gen_secret()

print("================================")
print("MTProto Proxy Started 🗿")
print("PORT:", PORT)
print("SECRET:", SECRET)
print("================================")

# تحميل ملفات Telegram
os.system("curl -s https://core.telegram.org/getProxySecret -o /app/MTProxy/proxy-secret")
os.system("curl -s https://core.telegram.org/getProxyConfig -o /app/MTProxy/proxy-multi.conf")

subprocess.run([
"/app/MTProxy/objs/bin/mtproto-proxy",
"-u","nobody",
"-p","8888",
"-H",PORT,
"-S",SECRET,
"--aes-pwd","/app/MTProxy/proxy-secret",
"/app/MTProxy/proxy-multi.conf"
])
