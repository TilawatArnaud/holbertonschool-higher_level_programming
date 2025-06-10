#!/usr/bin/python3
"""
Simple HTTP Server

This module implements a basic HTTP server using Python's http.server module.
It serves text, JSON responses
and handles different endpoints with error handling.
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that responds to GET requests.
    """

    def do_GET(self):
        """
        Handle GET requests by sending appropriate responses.
        """
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found")


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """
    Run the HTTP server on the specified port.

    Args:
        server_class: The HTTP server class to use
        handler_class: The request handler class to use
        port: The port number to run the server on
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
