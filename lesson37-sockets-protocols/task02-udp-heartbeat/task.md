# Connectionless messaging with UDP

> **Phase:** Networking & the Web  •  **Stage:** 37.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Contrast UDP datagrams with TCP streams (no connection, message boundaries, possible loss)
- Use sendto/recvfrom and read the sender address
- Set a socket timeout and handle the timeout exception
- Pack a small fixed binary header with struct

## Python features introduced
`socket.SOCK_DGRAM`, `sendto`, `recvfrom`, `settimeout and socket.timeout`, `datagram boundaries vs streams`, `struct.pack/unpack for a fixed binary header`, `bytes literals`

## MiniERP increment
Adds erp/net/heartbeat.py: a UDP 'service heartbeat' beacon. A node sends a packed (version, node_id, status) datagram; a collector recvfrom-s and decodes it, feeding a liveness map the Reporting module can later display. Reinforces that monitoring traffic is fire-and-forget.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import socket, struct

HEADER = "!BHB"  # version (u8), node_id (u16), status (u8)

def send_heartbeat(host, port, node_id, status, version=1):
    """Pack a heartbeat and send it as one UDP datagram."""
    # TODO: build a SOCK_DGRAM socket, struct.pack the header, sendto
    raise NotImplementedError

def collect_one(host="127.0.0.1", port=0, timeout=1.0):
    """Bind a UDP socket, return (bound_port, recv_fn) where recv_fn()->(node_id,status,addr)."""
    # TODO: bind, settimeout, return a closure that recvfrom-s and struct.unpacks
    raise NotImplementedError
- **Test focus:** Bind a collector on port 0, send a heartbeat to it, and assert the unpacked node_id/status match; assert settimeout raises socket.timeout when no packet arrives.

</div>
