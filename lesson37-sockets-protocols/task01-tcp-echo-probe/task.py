"""A TCP server and client with sockets

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import socket, threading

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
"""

# Your code here.
