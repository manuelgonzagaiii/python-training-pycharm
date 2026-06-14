"""Modeling addresses with ipaddress

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import ipaddress
from ipaddress import IPv4Address, IPv6Address

def parse_addr(text: str) -> IPv4Address | IPv6Address:
    """Parse text into an address object, raising ValueError on bad input."""
    # TODO: return ipaddress.ip_address(text)
    raise NotImplementedError

def is_allowed(addr: str, allowed_cidrs: list[str]) -> bool:
    """True if addr falls inside any of the allowed CIDR networks."""
    # TODO: build ip_network objects (strict=False) and test membership
    raise NotImplementedError

def classify(addr: str) -> str:
    """Return 'loopback' | 'private' | 'global' | 'other' using match/case."""
    raise NotImplementedError
"""

# Your code here.
