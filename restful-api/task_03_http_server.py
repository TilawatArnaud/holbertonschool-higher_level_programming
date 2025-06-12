#!/usr/bin/python3
import http.server
import json
PORT = 8000
"""
Class for handling HTTP GET requests.
"""


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Handle HTTP GET requests.
    """
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(bytes(message, "utf8"))
            return

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"status": "ok"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Not Found")


def run():
    """
    Run the HTTP server.
    """
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving on port {PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
