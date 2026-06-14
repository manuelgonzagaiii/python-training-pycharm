"""A JSON REST API with BaseHTTPRequestHandler

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class ERPHandler(BaseHTTPRequestHandler):
    def _send_json(self, status, payload):
        body = json.dumps(payload).encode()
        # TODO: send_response(status), Content-Type/Content-Length headers, end_headers, wfile.write
        raise NotImplementedError

    def do_GET(self):
        # TODO: route self.path -> products list / product by id / customers
        raise NotImplementedError

    def do_POST(self):
        # TODO: read Content-Length bytes from rfile, json.loads, create product, 201
        raise NotImplementedError

def make_server(host="127.0.0.1", port=0):
    return ThreadingHTTPServer((host, port), ERPHandler)
"""

# Your code here.
