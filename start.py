import os
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8080))

class Health(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")
    def log_message(self, *args):
        pass

def run_health():
    HTTPServer(("0.0.0.0", PORT), Health).serve_forever()

threading.Thread(target=run_health, daemon=True).start()

subprocess.run(["markitdown-mcp", "--http", "--host", "0.0.0.0", "--port", str(PORT + 1)])
