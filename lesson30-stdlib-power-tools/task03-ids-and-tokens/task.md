# Random sampling, secure tokens, and UUIDs

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.3 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use random for reproducible, non-security sampling (e.g. demo data) with a seeded Random instance
- Use secrets for security-sensitive values (API tokens, password reset codes) and explain why random is unsafe there
- Generate unique IDs with uuid4 and deterministic IDs with uuid5 over a namespace
- Choose the right tool for IDs vs tokens vs sampling

## Python features introduced
`random (seed, choice, sample, shuffle, randint, Random instance)`, `reproducible random with seeded Random`, `secrets (token_hex, token_urlsafe, choice, randbelow)`, `random vs secrets security distinction`, `uuid.uuid4`, `uuid.uuid5 with a namespace`, `UUID.hex / str(UUID)`

## MiniERP increment
Stamp every record with a stable identity: new_id() returning a uuid4 hex for products/customers/invoices, deterministic sku_uuid(name) via uuid5, and api_token()/reset_code() via secrets. A seeded random helper generates reproducible demo/seed data. MiniERP entities now have real IDs and the auth layer has secure tokens.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/ids.py with new_id(), sku_uuid(name), api_token(), and seed_demo(rng_seed); learner implements with uuid, secrets, and a seeded random.Random.
- **Test focus:** new_id() is unique per call and valid hex; sku_uuid is deterministic for the same name; api_token length/charset; seed_demo reproducible for a fixed seed.

</div>
