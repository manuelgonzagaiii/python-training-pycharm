# Shelling out: subprocess for external validation

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 35.4 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Run an external command with subprocess.run, capture stdout/stderr, and check the return code
- Handle non-zero exits (CalledProcessError) and timeouts (TimeoutExpired)
- Stream large data through a child via Popen.communicate and pipes
- Understand why shell=False with an argument list avoids shell-injection, and why you never interpolate untrusted CSV paths into a shell string

## Python features introduced
`subprocess.run`, `subprocess.CompletedProcess`, `capture_output / text / check / timeout`, `subprocess.CalledProcessError / TimeoutExpired`, `subprocess.Popen`, `Popen.communicate / stdin / stdout / stderr pipes`, `subprocess.PIPE / DEVNULL`, `shell=False and argument lists (injection safety)`, `return codes`

## MiniERP increment
Adds erp/import_/external.py: before bulk import, MiniERP pipes the CSV through an external validator/normalizer command (e.g. the interpreter running a bundled validate_csv.py, or a tool like `iconv`/`python -m`) via subprocess, capturing its report and feeding normalized output to the importer. Integrates with the concurrent importer from lesson 1.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A validate_csv(path) wrapping subprocess.run with check/timeout, plus a streaming normalize() using Popen.communicate; both built with argument lists, shell=False.
- **Test focus:** A clean CSV passes (return code 0, parsed report), a malformed CSV raises/returns a structured failure, a hanging command hits the timeout, and arguments are passed as a list (no shell).

</div>
