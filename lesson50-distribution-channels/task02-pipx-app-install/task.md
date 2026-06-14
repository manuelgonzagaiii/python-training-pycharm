# pipx: Install MiniERP as a Global, Isolated App

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 50.2 of 5  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand pipx's model: each CLI app gets its own hidden venv but its command is exposed globally
- Install MiniERP with `pipx install minierp` (and from the local wheel) and run it from anywhere
- Use `pipx run` for ephemeral execution and `pipx inject` to add an extra into an installed app
- Choose pipx for end-user CLI apps vs pip for libraries inside a project

## Python features introduced
`pipx (OSS) install/run/inject`, `per-app isolated venvs`, `PATH shim management`, `pipx run (ephemeral)`, `console_scripts exposure via pipx`, `comparison: pip vs pipx vs uv tool`

## MiniERP increment
Document and verify MiniERP's recommended end-user install: `pipx install minierp` yields a globally available `minierp` command backed by an isolated environment — positioning MiniERP as a first-class installable CLI app, not just a library.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Theory page; task.py contains an annotated transcript and a parse_pipx_list(text)->dict helper the learner can run against sample `pipx list` output.
- **Test focus:** Theory — no automated check; the helper merely demonstrates parsing pipx's output so learners can verify an install.

</div>
