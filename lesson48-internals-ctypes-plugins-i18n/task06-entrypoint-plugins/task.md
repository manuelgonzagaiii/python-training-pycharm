# A plugin system via entry points

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.6 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Discover installed plugins through importlib.metadata entry points by group
- Load and instantiate plugins lazily, isolating import failures
- Define a plugin contract (Protocol) so third-party packages can extend the ERP
- Register plugin-contributed commands into the existing registry

## Python features introduced
`importlib.metadata.entry_points`, `EntryPoint.load() / .name / .group`, `entry-point groups (selecting by group=)`, `plugin protocol via typing.Protocol`, `importlib.metadata.version / metadata`, `graceful load-failure handling`

## MiniERP increment
Delivers the plugin system: erp/plugins.py discovers ERP extensions advertised under the 'minierp.plugins' entry-point group, loads each, validates it against an ErpPlugin Protocol, and merges its commands into the registry from lesson 1 — so outside packages add modules (e.g. a shipping calculator) without modifying core. Fulfills the plugin-system milestone.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
from importlib.metadata import entry_points
from typing import Protocol, runtime_checkable

GROUP = "minierp.plugins"


@runtime_checkable
class ErpPlugin(Protocol):
    name: str
    def register(self, registry: dict) -> None: ...


def discover() -> dict[str, ErpPlugin]:
    """Find entry points in GROUP, load each, skip ones that fail to load or
    do not satisfy ErpPlugin. Return name -> plugin instance."""
    raise NotImplementedError

- **Test focus:** Tests discover with a monkeypatched/fake entry_points result: loads valid plugins, skips ones that raise on load, and rejects objects not matching the ErpPlugin Protocol; verifies plugin commands are registered into a passed registry.

</div>
