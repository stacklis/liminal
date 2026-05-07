"""serve-newest.py — serves the highest-numbered liminal_N.html as the index."""

import http.server
import os
import re
import socketserver
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
PATTERN = re.compile(r"^liminal_(\d+)\.html$")


def newest_filename():
    candidates = []
    for name in os.listdir(DIR):
        m = PATTERN.match(name)
        if m:
            candidates.append((int(m.group(1)), name))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            target = newest_filename()
            if target:
                self.path = "/" + target
        return super().do_GET()


def main():
    os.chdir(DIR)
    n = newest_filename() or "(none found)"
    print(f"[liminal] serving on 0.0.0.0:{PORT} | / -> {n}", flush=True)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[liminal] stopped", flush=True)


if __name__ == "__main__":
    main()
