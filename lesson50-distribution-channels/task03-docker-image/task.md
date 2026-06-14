# Containerize MiniERP: a Multi-Stage Dockerfile

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 50.3 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a multi-stage Dockerfile: a builder stage that produces the wheel, a slim runtime stage that installs only that wheel
- Order layers and use .dockerignore for fast, cache-friendly, small images
- Run as a non-root user and set ENTRYPOINT to the `minierp` console script
- Parameterize secrets/config via ENV (never baked in) and EXPOSE the web port

## Python features introduced
`Dockerfile (FROM/COPY/RUN/ENTRYPOINT/CMD)`, `multi-stage builds (builder vs runtime)`, `python:3.14-slim base image`, `installing the wheel inside the image`, `.dockerignore`, `non-root USER`, `ENV / build args`, `layer caching strategy`, `EXPOSE for the web front-end`

## MiniERP increment
Containerize MiniERP so `docker build` + `docker run` launches the web front-end (and CLI) with no host Python required. The image installs the wheel from the build-and-package lesson, runs as a non-root user, reads config/secrets from ENV, and serves the HTTP API on the exposed port.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a partially written Dockerfile and a lint_dockerfile(text)->list[str] checker (parsing instructions, flagging root user / missing healthcheck); learner completes the Dockerfile to pass the checks.
- **Test focus:** lint_dockerfile passes: multi-stage present, slim base, wheel installed (not raw source), non-root USER, ENTRYPOINT invokes minierp, no hardcoded secrets, port EXPOSEd.

</div>
