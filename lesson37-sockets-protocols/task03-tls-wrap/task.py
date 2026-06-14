"""Encrypting a socket with ssl

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import ssl, socket

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
"""

# Your code here.
