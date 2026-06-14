# asyncio.Queue, Lock & a streaming server

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Coordinate async producers and consumers with asyncio.Queue (the async analog of queue.Queue)
- Guard async-shared state with asyncio.Lock / asyncio.Event (and see why threading locks are wrong here)
- Build a real asyncio TCP server with start_server and the streams API
- Read requests and write responses over StreamReader/StreamWriter with proper drain/close

## Python features introduced
`asyncio.Queue`, `asyncio.Lock`, `asyncio.Event`, `async producer-consumer`, `asyncio.start_server`, `asyncio.StreamReader / StreamWriter`, `reader.readline / writer.write / await writer.drain`, `writer.close / wait_closed`, `serve_forever`

## MiniERP increment
Delivers the async server core: an asyncio TCP endpoint that accepts simple line-based MiniERP commands (e.g. GET /low-stock), dispatches to the async service facade, and streams results back. An internal asyncio.Queue decouples request intake from a worker coroutine; this is the concrete 'async core for the web layer.'

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** An async handle_client(reader, writer) reading commands, an asyncio.Queue worker, and start_server wiring; a client coroutine drives it in tests.
- **Test focus:** The server handles multiple concurrent client connections, queued commands are processed in order, responses stream back correctly, and connections close cleanly without leaking tasks.

</div>
