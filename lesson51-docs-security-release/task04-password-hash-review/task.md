# Security Pass II: Review Password Hashing & Validation

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 51.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Audit the Users-&-Roles password storage: confirm a salted, slow KDF (scrypt/pbkdf2_hmac) — never plain MD5/SHA or unsalted hashes
- Verify passwords with constant-time hmac.compare_digest to resist timing attacks
- Tighten input validation at every trust boundary (CLI args, HTTP bodies, import files)
- Confirm all SQL uses parameterized queries so imported/user data can't inject

## Python features introduced
`hashlib.scrypt / pbkdf2_hmac`, `per-user random salt (secrets.token_bytes)`, `hmac.compare_digest (constant-time)`, `never store plaintext / fast hashes`, `input validation & sanitization`, `parameterized SQL (sqlite3 placeholders) to prevent injection`, `raising on invalid input`

## MiniERP increment
Strengthen MiniERP's auth and boundaries: review and, where needed, upgrade password hashing to a salted slow KDF with constant-time verification, and add/confirm input validation on the import/export and HTTP/CLI entry points so MiniERP 1.0 ships without the classic auth and injection footguns.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide hash_password(pw)->str, verify_password(pw,stored)->bool, and validate_* helpers; learner implements the salted KDF, constant-time check, and validators.
- **Test focus:** hash output embeds salt+params and differs per call; verify_password accepts correct/rejects wrong and uses compare_digest; weak/plaintext schemes rejected; validators reject malformed input and SQL stays parameterized.

</div>
