import os
import random
import requests
import subprocess

# قائمة البروكسيات
proxies = [
("socks4","98.188.47.132","4145"),
("socks4","199.187.210.54","4145"),
("socks4","72.195.114.169","4145"),
("http","57.128.188.167","9158"),
("http","159.223.225.118","8888"),
("http","173.212.246.157","3128"),
]

def gen_secret():
    return ''.join(random.choice("0123456789abcdef") for _ in range(32))

def test_proxy(proxy_type, ip, port):
    try:

        proxy_url = f"{proxy_type}://{ip}:{port}"

        p = {
            "http": proxy_url,
            "https": proxy_url
        }

        r = requests.get(
            "https://api.ipify.org",
            proxies=p,
            timeout=8
        )

        if r.status_code == 200:
            print("✅ Proxy working:", proxy_url)
            return True

    except:
        pass

    print("❌ Proxy dead:", ip)
    return False


print("📦 تثبيت الأدوات...")

os.system("pkg install -y git clang make proxychains-ng || apt install -y git clang make proxychains")

print("⬇️ تحميل MTProxy...")

if not os.path.exists("MTProxy"):
    os.system("git clone https://github.com/TelegramMessenger/MTProxy.git")

print("⚙️ تجميع MTProxy...")

os.system("cd MTProxy && make")

conf_path = "/data/data/com.termux/files/usr/etc/proxychains.conf"
if not os.path.exists(conf_path):
    conf_path = "/etc/proxychains.conf"

working_proxy = None

print("🔎 اختبار البروكسيات...")

for ptype, ip, port in proxies:

    if test_proxy(ptype, ip, port):
        working_proxy = (ptype, ip, port)
        break


if not working_proxy:
    print("❌ لم يتم العثور على بروكسي يعمل")
    exit()


ptype, ip, port = working_proxy

print("🛠 استخدام البروكسي:", ip)

with open(conf_path, "a") as f:
    f.write(f"\n{ptype} {ip} {port}\n")


secret = gen_secret()

server_ip = requests.get("https://api.ipify.org").text.strip()

print("🚀 تشغيل MTProxy...")

cmd = f"""
proxychains ./MTProxy/objs/bin/mtproto-proxy \
-u nobody \
-p 8888 \
-H 443 \
-S {secret} \
--aes-pwd MTProxy/mtproto-proxy-secret mtproxy
"""

subprocess.Popen(cmd, shell=True)

print("\n🗿 MTProxy started")

print("Telegram link:")

print(f"https://t.me/proxy?server={server_ip}&port=443&secret={secret}")

input("\nاضغط Enter للإيقاف...")
