import os
import random
import subprocess
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8000))

def gen_secret():
    chars = "0123456789abcdef"
    return "dd" + "".join(random.choice(chars) for _ in range(30))

SECRET = gen_secret()

print("MTProto Proxy Started 🗿")
print("PORT:", PORT)
print("SECRET:", SECRET)

# تحميل ملفات تيليغرام
os.system("curl -s https://core.telegram.org/getProxySecret -o /app/MTProxy/proxy-secret")
os.system("curl -s https://core.telegram.org/getProxyConfig -o /app/MTProxy/proxy-multi.conf")

def start_proxy():
    subprocess.run([
        "/app/MTProxy/objs/bin/mtproto-proxy",
        "-u","nobody",
        "-p","8888",
        "-H",str(PORT),
        "-S",SECRET,
        "-M","5",
        "--aes-pwd","/app/MTProxy/proxy-secret",
        "/app/MTProxy/proxy-multi.conf"
    ])

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Proxy Running")

def start_http():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

threading.Thread(target=start_proxy).start()
start_http()
