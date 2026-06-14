# A TCP server and client with sockets

> **Phase:** Networking & the Web  •  **Stage:** 37.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create a TCP listening socket and a connecting client socket
- Understand the bind/listen/accept vs connect lifecycle
- Send and receive bytes and convert to/from str with explicit encoding
- Use a socket as a context manager and set SO_REUSEADDR
- Run a blocking server on a background thread so a test can talk to it

## Python features introduced
`socket.socket`, `AF_INET`, `SOCK_STREAM`, `bind/listen/accept`, `connect`, `sendall/recv`, `socket as context manager (with)`, `SO_REUSEADDR via setsockopt`, `bytes <-> str encode/decode`, `threading.Thread for the server`, `f-string '=' debugging`

## MiniERP increment
Adds erp/net/tcp_probe.py: a tiny line-based 'inventory probe' protocol where a client sends a product SKU and a localhost TCP server replies with the on-hand quantity from the existing inventory service. Establishes the project's first raw socket server, started on an ephemeral port (bind to port 0) for tests.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import socket, threading

ENCODING = "utf-8"

def serve_once(handler, host="127.0.0.1", port=0):
    """Bind a TCP server, return (host, port, started_thread). handler(text)->text per line."""
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # TODO: bind to (host, port), listen, capture the real bound port
    # TODO: start a thread that accepts one client, reads a line, sends handler(line) back
    raise NotImplementedError

def probe(host, port, sku):
    """Connect, send sku + newline, return the server's reply text (stripped)."""
    # TODO: open a client socket as a context manager, sendall, recv, decode
    raise NotImplementedError
- **Test focus:** Spin up serve_once with a fake handler on port 0, then assert probe() returns the handler's reply; verify bytes/str boundary by sending non-ASCII SKU and checking round-trip integrity.

</div>
