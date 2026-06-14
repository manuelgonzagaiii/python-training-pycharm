# Password hashing and signed audit entries

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.4 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Hash passwords with a salt using hashlib.pbkdf2_hmac and verify them
- Understand why constant-time comparison (hmac.compare_digest) defeats timing attacks
- Sign data with hmac.new and an app secret to detect tampering
- Handle the bytes/str boundary correctly when hashing

## Python features introduced
`hashlib (sha256, blake2b, pbkdf2_hmac)`, `salted hashing`, `hashlib.scrypt mention`, `hmac.new`, `hmac.compare_digest (constant-time comparison)`, `bytes vs str encoding for hashing`, `hexdigest`

## MiniERP increment
Secure the users and audit modules: hash_password(pw, salt) and verify_password using pbkdf2_hmac + compare_digest, and sign_entry(entry, key)/verify_entry for tamper-evident audit-log records signed with HMAC. MiniERP now stores hashed credentials and a signed audit trail instead of plaintext.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/security.py with hash_password/verify_password and sign_entry/verify_entry; learner implements with hashlib.pbkdf2_hmac, hmac.new, and compare_digest.
- **Test focus:** verify_password accepts the right password and rejects wrong ones; hashes are salted (same pw, different salt -> different hash); tampered audit entry fails verify_entry; comparisons are constant-time.

</div>
