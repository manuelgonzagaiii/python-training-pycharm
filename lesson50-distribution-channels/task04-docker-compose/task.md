# A Full Stack with Docker Compose: app + mail + data

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 50.4 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compose a multi-service stack: the MiniERP app, an OSS aiosmtpd mail container, and a persistent SQLite data volume
- Wire services together with environment/env_file, depends_on, healthchecks and an internal network
- Persist MiniERP's SQLite database in a named volume so data survives container restarts
- Inject secrets via an .env file kept out of the image and out of version control

## Python features introduced
`docker-compose.yaml (YAML)`, `services / networks / volumes`, `depends_on & healthcheck`, `environment & env_file (secrets via .env)`, `named volumes for SQLite persistence`, `aiosmtpd (OSS) mail sidecar service`, `port mapping`, `service-to-service DNS`

## MiniERP increment
Deliver `docker compose up` as MiniERP's one-command deployment: the app talks to the aiosmtpd sidecar for invoice/payment emails (the OSS SMTP stand-in from earlier phases), stores its SQLite DB in a named volume, and reads all secrets from .env — a runnable, reproducible deployment of the whole suite.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide load_compose(path)->dict (yaml/tomllib-style parse via a tiny provided parser or json fixture) and validate_stack(cfg)->list[str]; learner completes the compose file's services/volumes/healthchecks.
- **Test focus:** compose defines the three expected services; app depends_on the mail/db with healthchecks; a named volume backs the SQLite path; secrets come from env_file not literals; the web port is mapped.

</div>
