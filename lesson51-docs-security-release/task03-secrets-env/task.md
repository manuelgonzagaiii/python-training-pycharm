# Security Pass I: Secrets via Environment & Config

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 51.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Move every secret (DB path creds, SMTP creds, signing/session keys) out of source code into environment variables
- Build a typed config loader with precedence: environment over config file over safe defaults
- Generate cryptographically strong secrets with the stdlib secrets module
- Fail loudly when a required secret is missing rather than using an insecure default

## Python features introduced
`os.environ / os.getenv with defaults`, `12-factor config`, `python-dotenv (OSS) or stdlib .env parsing`, `secrets module (token_urlsafe/token_hex)`, `keeping secrets out of source & images`, `config precedence (env > file > default)`, `tomllib for non-secret config`

## MiniERP increment
Harden MiniERP's configuration: a single Config loader reads all secrets from the environment (with tomllib for non-secret settings), generates secure tokens with the secrets module when bootstrapping, and refuses to start if a required secret is absent — closing the gap that Docker/Compose/PyInstaller all depend on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide load_config(env, files)->Config and require_secret(name)->str using os.environ + secrets; learner implements precedence and the missing-secret failure.
- **Test focus:** env overrides file overrides default; require_secret raises on absence; generated tokens have expected length/entropy; no secret literals remain in the loader; non-secret config parsed via tomllib.

</div>
