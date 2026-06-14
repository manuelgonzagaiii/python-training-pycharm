# Modeling addresses with ipaddress

> **Phase:** Networking & the Web  •  **Stage:** 37.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Parse and validate IPv4/IPv6 addresses and CIDR networks
- Test membership of an address in a network
- Distinguish private, loopback, and global addresses
- Use match/case and PEP 604 unions over the address hierarchy

## Python features introduced
`ipaddress.ip_address`, `ip_network`, `ip_interface`, `IPv4Address/IPv6Address`, `in operator for network membership`, `is_private/is_loopback/is_global`, `ValueError on bad input`, `PEP 604 unions (IPv4Address | IPv6Address)`, `match/case on address type`

## MiniERP increment
Adds erp/net/access.py: an IP allow-list the REST API will consult so admin-only endpoints can be restricted to a trusted CIDR (e.g. the office LAN). Returns a typed decision the service layer logs to the existing audit log.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import ipaddress
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
- **Test focus:** Assert is_allowed for addresses inside/outside given CIDRs (both IPv4 and IPv6), classify() returns the right bucket for 127.0.0.1 / 10.0.0.5 / 8.8.8.8, and parse_addr raises ValueError on garbage.

</div>
