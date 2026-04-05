import os
import random
import subprocess
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8000))
PROXY_PORT = 9000

def gen_secret():
    chars="0123456789abcdef"
    return "".join(random.choice(chars) for _ in range(32))

SECRET = gen_secret()

print("Proxy started 🗿")
print("PORT:", PROXY_PORT)
print("SECRET:", SECRET)

def start_proxy():
    subprocess.run([
        "./mtg",
        "run",
        "--bind",
        f"0.0.0.0:{PROXY_PORT}",
        SECRET
    ])

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def start_http():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

threading.Thread(target=start_proxy).start()
start_http()
