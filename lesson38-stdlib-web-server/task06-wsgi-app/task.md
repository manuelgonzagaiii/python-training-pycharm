# A WSGI application with wsgiref

> **Phase:** Networking & the Web  •  **Stage:** 38.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement the raw WSGI callable contract by hand
- Read request data out of the environ dict and the input stream
- Call start_response with a status line and header list and return a bytes iterable
- Serve the app with wsgiref.simple_server and see the standard interface in action

## Python features introduced
`wsgiref.simple_server.make_server`, `the WSGI callable (environ, start_response)`, `reading PATH_INFO / REQUEST_METHOD / QUERY_STRING / wsgi.input`, `start_response(status, headers)`, `returning an iterable of bytes`, `wsgiref.util helpers`, `closing the response`

## MiniERP increment
Adds erp/web/wsgi_app.py: the MiniERP HTML UI re-expressed as a portable WSGI app (reusing render_products and the services), so the same UI can run under any WSGI server. Demonstrates the standardized interface that uvicorn's ASGI counterpart will mirror.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from wsgiref.simple_server import make_server

def app(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    # TODO: route GET / -> product list HTML; build (status, headers, body_bytes)
    # TODO: start_response(status, headers); return [body_bytes]
    raise NotImplementedError

def serve(host="127.0.0.1", port=0):
    return make_server(host, port, app)
- **Test focus:** Drive app() directly with a hand-built environ and a fake start_response, capturing the status/headers and asserting the body bytes contain the product table; also start it via make_server on port 0 and fetch it with the urllib client.

</div>
