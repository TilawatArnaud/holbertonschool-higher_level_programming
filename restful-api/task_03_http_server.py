#!/usr/bin/python3
"""Module for handling HTTP GET requests."""

import http.server
import json
PORT = 8000


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """Handle HTTP GET requests."""

    def do_GET(self):
        """Handle GET requests."""
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
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "OK"
            self.wfile.write(bytes(message, "utf8"))
            return

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))
            return

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            message = {"status": "404 Not Found", "message": "Endpoint not found"}
            self.wfile.write(json.dumps(message).encode('utf-8'))


def run():
    """Run the HTTP server."""
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving on port {PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
