# Encrypting a socket with ssl

> **Phase:** Networking & the Web  •  **Stage:** 37.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand TLS as a wrapper over an existing TCP socket
- Build client and server SSLContext objects with the right Purpose
- Wrap sockets and complete a handshake on localhost
- Reason about hostname checking and why it is disabled only for a self-signed local test

## Python features introduced
`ssl.SSLContext`, `ssl.create_default_context`, `Purpose.CLIENT_AUTH / SERVER_AUTH`, `context.wrap_socket`, `self-signed cert generation via ssl/cryptography-free stdlib (tempfile + openssl-less test cert)`, `check_hostname and CERT_NONE for localhost`, `server_hostname`

## MiniERP increment
Adds erp/net/secure_probe.py: an opt-in TLS variant of the inventory probe so credentials/quantities travel encrypted. Ships a test-only self-signed certificate helper under erp/net/_testcert.py used by the tests; production code path reads a real cert from config.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import ssl, socket

def client_context():
    """Return an SSLContext for a client that trusts our local self-signed cert."""
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    # TODO: for localhost self-signed: load_verify_locations(cafile) OR relax check_hostname
    raise NotImplementedError

def server_context(certfile, keyfile):
    """Return an SSLContext for a TLS server."""
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # TODO: ctx.load_cert_chain(certfile, keyfile)
    raise NotImplementedError

def wrap_client(sock, ctx, server_hostname):
    """Wrap a connected client socket for TLS."""
    # TODO: return ctx.wrap_socket(sock, server_hostname=server_hostname)
    raise NotImplementedError
- **Test focus:** Using the bundled self-signed cert, complete a TLS handshake between a wrapped server and client socket on port 0 and exchange one encrypted line; assert the plaintext arrives intact through the encrypted channel.

</div>
