# Generate a Documentation Site (Sphinx / MkDocs)

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 51.2 of 6  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Configure a doc generator (Sphinx autodoc+napoleon or MkDocs+mkdocstrings) to build an HTML site from the docstrings you just wrote
- Understand how autodoc imports your package and renders its API reference
- Author landing/usage pages (rST or Markdown) alongside the auto-generated API docs
- Build the site locally and know how it would be published

## Python features introduced
`Sphinx (OSS) autodoc / napoleon`, `or MkDocs (OSS) + mkdocstrings`, `conf.py / mkdocs.yml`, `reStructuredText vs Markdown`, `autodoc pulling from docstrings`, `API reference generation`, `html builder output`, `intersphinx / cross-refs`

## MiniERP increment
Stand up MiniERP's documentation site: an autodoc-driven API reference generated from the package's docstrings plus hand-written install/usage/quickstart pages — the user-facing docs that ship with the 1.0 release.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Theory page; task.py includes a parse_mkdocs_nav(text)/parse_sphinx_conf(text) helper plus annotated config so learners can run a local build off-task.
- **Test focus:** Theory — no automated check; provided helpers let learners validate their own conf.py/mkdocs.yml nav structure.

</div>
