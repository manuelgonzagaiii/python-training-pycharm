# A thread-safe report-job queue

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 34.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use queue.Queue to hand work from producers to worker threads without manual locking
- Coordinate completion with task_done() and Queue.join()
- Drain and shut down workers cleanly with a sentinel (poison pill)
- Choose between FIFO, LIFO, and priority queues, and submit urgent report jobs ahead of routine ones with PriorityQueue

## Python features introduced
`queue.Queue`, `Queue.put / Queue.get`, `Queue.task_done / Queue.join`, `queue.Empty / queue.Full`, `queue.LifoQueue`, `queue.PriorityQueue`, `sentinel / poison-pill shutdown pattern`, `producer-consumer pattern`

## MiniERP increment
Introduces erp/jobs/queue.py: a ReportJobQueue where the CLI enqueues report requests (each a small dataclass) and one or more worker threads pull and execute them. Priority queue lets an 'urgent' invoice/report jump the line; the queue replaces ad-hoc threading from the previous task.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A producer that enqueues JobRequest items, a worker loop that get()/processes/task_done()s, and a shutdown that injects sentinels; a priority variant orders by (priority, seq).
- **Test focus:** All enqueued jobs are processed exactly once, Queue.join() returns only when the backlog is empty, and priority ordering is respected with a stable tie-break.

</div>
