# A JSON REST API with BaseHTTPRequestHandler

> **Phase:** Networking & the Web  •  **Stage:** 38.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Subclass BaseHTTPRequestHandler and implement do_GET/do_POST
- Route on self.path and read a JSON request body via Content-Length
- Write correct status lines, headers, and a JSON body
- Run the handler under ThreadingHTTPServer for concurrent requests

## Python features introduced
`http.server.BaseHTTPRequestHandler`, `do_GET / do_POST`, `self.path, self.headers, rfile/wfile`, `send_response/send_header/end_headers`, `Content-Length and reading the request body`, `json.dumps/loads`, `http.server.ThreadingHTTPServer`, `HTTPStatus enum`, `re for simple path routing`

## MiniERP increment
Adds erp/web/api.py: the first real MiniERP REST API over the existing services — GET /products, GET /products/{id}, POST /products, GET /customers — returning JSON. This is the stdlib baseline the FastAPI version will later replace while keeping identical routes.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import json
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
- **Test focus:** Start make_server on port 0 in a thread, then use the Lesson-1 urllib client to GET /products (200 + JSON list), GET an unknown id (404), and POST a new product (201 + body echo); assert it actually appears via a follow-up GET.

</div>
