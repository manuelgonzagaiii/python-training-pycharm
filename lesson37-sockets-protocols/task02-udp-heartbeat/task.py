"""Connectionless messaging with UDP

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import socket, struct

HEADER = "!BHB"  # version (u8), node_id (u16), status (u8)

def send_heartbeat(host, port, node_id, status, version=1):
    """Pack a heartbeat and send it as one UDP datagram."""
    # TODO: build a SOCK_DGRAM socket, struct.pack the header, sendto
    raise NotImplementedError

def collect_one(host="127.0.0.1", port=0, timeout=1.0):
    """Bind a UDP socket, return (bound_port, recv_fn) where recv_fn()->(node_id,status,addr)."""
    # TODO: bind, settimeout, return a closure that recvfrom-s and struct.unpacks
    raise NotImplementedError
"""

# Your code here.
