# Phase 3 — Concurrency & Performance (Days 35–50)

> Track: `python_concurrency` · Outcome: generators, async, threads, multiprocessing, profiling

## Day Plan

| Day | Topic | Slug | Exercise direction |
|-----|-------|------|--------------------|
| 35 | Generators deep-dive | `day_35_generators` | Lazy ETL, infinite sequences |
| 36 | Generator pipelines | `day_36_gen_pipelines` | Log stream, data transform chain |
| 37 | `asyncio` basics | `day_37_asyncio_basics` | Concurrent fetchers |
| 38 | `asyncio` tasks & gather | `day_38_asyncio_tasks` | Parallel downloads |
| 39 | Async I/O patterns | `day_39_async_io` | aiofiles, aiohttp |
| 40 | Async generators & context | `day_40_async_advanced` | Streaming, async CM |
| 41 | Threading | `day_41_threading` | Concurrent I/O, shared state |
| 42 | Thread safety | `day_42_thread_safety` | Locks, queues, thread pool |
| 43 | `multiprocessing` | `day_43_multiprocessing` | CPU-bound parallel |
| 44 | `concurrent.futures` | `day_44_futures` | ThreadPool, ProcessPool |
| 45 | `subprocess` | `day_45_subprocess` | Shell automation |
| 46 | Memory management | `day_46_memory` | `__slots__`, weak refs, gc |
| 47 | Profiling | `day_47_profiling` | cProfile, line_profiler |
| 48 | Performance patterns | `day_48_performance` | Caching, lazy eval, batch |
| 49 | `struct` / `array` / `memoryview` | `day_49_binary` | Binary protocols |
| 50 | Concurrency project | `day_50_concurrency_project` | Async scraper + pipeline |

---

## Concept Checklists

### Day 35 — Generators Deep-dive (22)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `yield` keyword | `def gen(): yield x` |
| 2 | Generator function vs generator object | Calling returns iterator |
| 3 | `next()` | Manual stepping |
| 4 | `StopIteration` | End signal |
| 5 | `yield` in loop | Produce sequence |
| 6 | Generator expression | `(x for x in range(n))` |
| 7 | Lazy evaluation | Compute on demand |
| 8 | Memory efficiency | vs list |
| 9 | `yield from` | Delegate to sub-generator |
| 10 | `send()` | Push value into generator |
| 11 | `throw()` | Inject exception |
| 12 | `close()` | Terminate generator |
| 13 | `GeneratorExit` | Raised on close |
| 14 | Generator as coroutine (legacy) | Pre-asyncio pattern |
| 15 | Infinite generators | `count()` style |
| 16 | Stateful generators | Running totals, filters |
| 17 | `itertools` + generators | Composable pipelines |
| 18 | Two-pass problem | `itertools.tee()` |
| 19 | Anti-pattern: list(huge_gen) | Defeats purpose |
| 20 | Anti-pattern: generator reuse | Exhausted after one pass |
| 21 | Industrial: lazy ETL | Read→transform→write |
| 22 | Industrial: streaming log parser | Line-by-line processing |

### Day 36 — Generator Pipelines (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Pipeline composition | `gen1(gen2(source))` |
| 2 | Source generators | Read lines, rows |
| 3 | Transform generators | Map, filter, enrich |
| 4 | Sink functions | Aggregate, write |
| 5 | `yield from` chaining | Flatten nested |
| 6 | Branching pipelines | `tee()` for split |
| 7 | Error handling in pipeline | `try/except` in generator |
| 8 | Backpressure concept | Producer faster than consumer |
| 9 | `send()` for feedback | Control flow |
| 10 | Coroutine pipeline | `send()`-based |
| 11 | Generator + context manager | Resource cleanup |
| 12 | Testing generators | `list()` for snapshot |
| 13 | `itertools.chain` in pipeline | Merge sources |
| 14 | `itertools.islice` | Limit output |
| 15 | Batching in pipeline | `itertools.batched()` |
| 16 | Deduplication generator | `seen = set()` |
| 17 | Anti-pattern: eager collection | Stay lazy |
| 18 | Anti-pattern: no error handling | Generators just stop |
| 19 | Industrial: log stream processor | Parse→filter→alert |
| 20 | Industrial: data transform chain | CSV→clean→enrich→JSONL |

### Day 37 — asyncio Basics (22)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `async def` | Coroutine function |
| 2 | `await` | Suspend until done |
| 3 | `asyncio.run()` | Entry point |
| 4 | Coroutine object | Calling async def returns it |
| 5 | Event loop concept | Single-thread concurrency |
| 6 | `asyncio.sleep()` | Non-blocking delay |
| 7 | `asyncio.gather()` | Run multiple coroutines |
| 8 | `asyncio.create_task()` | Schedule coroutine |
| 9 | Task vs coroutine | Task starts immediately |
| 10 | `asyncio.wait()` | Fine-grained control |
| 11 | `asyncio.wait_for()` | Timeout wrapper |
| 12 | Cancellation | `task.cancel()` |
| 13 | `CancelledError` | Handle cancellation |
| 14 | `asyncio.Queue` | Async producer-consumer |
| 15 | `asyncio.Semaphore` | Concurrency limiter |
| 16 | `asyncio.Lock` | Async mutex |
| 17 | `asyncio.Event` | Signal between tasks |
| 18 | Return values from gather | `results = await gather(a, b)` |
| 19 | Exception in gather | `return_exceptions=True` |
| 20 | Anti-pattern: blocking in async | Use `run_in_executor` |
| 21 | Anti-pattern: forget `await` | Coroutine never runs |
| 22 | Industrial: concurrent fetchers | Parallel HTTP calls |

### Day 38 — asyncio Tasks & Gather (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `TaskGroup` (3.11+) | `async with TaskGroup() as tg:` |
| 2 | `tg.create_task()` | Structured concurrency |
| 3 | Exception propagation | TaskGroup cancels on error |
| 4 | `asyncio.as_completed()` | First-finished order |
| 5 | `asyncio.shield()` | Protect from cancellation |
| 6 | Timeout patterns | `asyncio.timeout()` (3.11+) |
| 7 | Fan-out / fan-in | Scatter tasks, collect results |
| 8 | Rate limiting | Semaphore-based |
| 9 | Progress tracking | Callback on task done |
| 10 | `add_done_callback` | Task completion hook |
| 11 | `asyncio.to_thread()` | Run sync in thread |
| 12 | `run_in_executor()` | Thread/process pool |
| 13 | Structured concurrency | Lifetime management |
| 14 | Graceful shutdown | Cancel all tasks |
| 15 | `asyncio.current_task()` | Introspection |
| 16 | Task naming | `name=` parameter |
| 17 | Anti-pattern: fire and forget | Unhandled exceptions |
| 18 | Anti-pattern: unbounded tasks | Memory leak |
| 19 | Industrial: parallel downloads | Fan-out + semaphore |
| 20 | Industrial: worker pool | Queue + N consumers |

### Day 39 — Async I/O Patterns (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `aiofiles` | `async with aiofiles.open():` |
| 2 | `aiohttp` client | `async with ClientSession():` |
| 3 | `aiohttp` server basics | `web.Application()` |
| 4 | Async context managers | `async with` |
| 5 | Async iteration | `async for` |
| 6 | `__aenter__` / `__aexit__` | Async CM protocol |
| 7 | `__aiter__` / `__anext__` | Async iterator protocol |
| 8 | Connection pooling | Reuse sessions |
| 9 | Retry with backoff | Async retry pattern |
| 10 | Timeout per request | `asyncio.wait_for()` |
| 11 | Streaming response | Chunked reads |
| 12 | `asyncio.StreamReader/Writer` | TCP streams |
| 13 | Error handling in async I/O | `aiohttp.ClientError` |
| 14 | SSL/TLS | `ssl=` parameter |
| 15 | Anti-pattern: sync I/O in async | Blocks event loop |
| 16 | Anti-pattern: no session reuse | Connection overhead |
| 17 | Industrial: async HTTP client | Session + retry + timeout |
| 18 | Industrial: async file pipeline | aiofiles for ETL |
| 19 | `asyncio.open_connection()` | Low-level TCP |
| 20 | `asyncio.start_server()` | TCP server |

### Day 40 — Async Generators & Advanced (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `async def gen()` with `yield` | Async generator |
| 2 | `async for` consumption | `async for item in agen():` |
| 3 | `@asynccontextmanager` | Async CM from generator |
| 4 | Async comprehensions | `[x async for x in agen()]` |
| 5 | `aiter()` / `anext()` (3.10+) | Async manual stepping |
| 6 | `asyncio.Queue` patterns | Producer-consumer |
| 7 | Multiple queues | Fan-out/fan-in with queues |
| 8 | Sentinel for shutdown | `None` or special object |
| 9 | Async callback pattern | Schedule callbacks |
| 10 | `asyncio.Barrier` (3.11+) | Synchronization point |
| 11 | Error handling in async gen | `try/finally` cleanup |
| 12 | `aclose()` | Cleanup async generator |
| 13 | Mixing sync and async | `to_thread()`, `run_in_executor()` |
| 14 | Debug mode | `asyncio.run(debug=True)` |
| 15 | `asyncio.Runner` (3.11+) | Reusable runner |
| 16 | Anti-pattern: async without I/O | No benefit for CPU work |
| 17 | Anti-pattern: blocking generator | Use async generator |
| 18 | Industrial: streaming pipeline | Async gen chain |
| 19 | Industrial: real-time processor | Queue + async consumers |
| 20 | Testing async code | `pytest-asyncio` |

### Day 41 — Threading (22)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `threading.Thread` | `Thread(target=fn)` |
| 2 | `.start()` / `.join()` | Launch and wait |
| 3 | `daemon=True` | Background thread |
| 4 | Thread arguments | `args=()`, `kwargs={}` |
| 5 | GIL concept | One Python thread at a time |
| 6 | GIL and I/O | Released during I/O |
| 7 | Thread safety | Shared mutable state |
| 8 | `threading.Lock` | `with lock:` |
| 9 | `threading.RLock` | Reentrant lock |
| 10 | `threading.Event` | Signal between threads |
| 11 | `threading.Condition` | Wait/notify |
| 12 | `threading.Semaphore` | Limit concurrency |
| 13 | `threading.Barrier` | Synchronization point |
| 14 | `queue.Queue` | Thread-safe FIFO |
| 15 | `queue.PriorityQueue` | Ordered by priority |
| 16 | `threading.local()` | Thread-local storage |
| 17 | `threading.Timer` | Delayed execution |
| 18 | Thread naming | `name=` for debugging |
| 19 | Anti-pattern: shared mutable | Race conditions |
| 20 | Anti-pattern: no join | Orphaned threads |
| 21 | Industrial: concurrent I/O | Parallel file/network ops |
| 22 | Industrial: producer-consumer | Queue + worker threads |

### Day 42 — Thread Safety (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Race condition | Concurrent read-modify-write |
| 2 | Critical section | Code under lock |
| 3 | Deadlock | Two locks, wrong order |
| 4 | Lock ordering | Consistent acquisition order |
| 5 | `Lock` vs `RLock` | Non-reentrant vs reentrant |
| 6 | Context manager lock | `with lock:` |
| 7 | `queue.Queue` as message bus | Decouple threads |
| 8 | Atomic operations | What's safe without lock |
| 9 | `threading.Event` patterns | Start/stop signals |
| 10 | `Condition` wait/notify | Producer signals consumer |
| 11 | `Semaphore` for pool | Limit concurrent access |
| 12 | `BoundedSemaphore` | Cannot release more than acquired |
| 13 | Thread-safe collections | `queue.Queue`, not plain list |
| 14 | `concurrent.futures.ThreadPoolExecutor` | Managed pool |
| 15 | `executor.map()` | Parallel map |
| 16 | `executor.submit()` | Returns Future |
| 17 | `Future.result()` | Get/wait for result |
| 18 | Anti-pattern: lock everything | Over-synchronization |
| 19 | Anti-pattern: global state | Harder to reason about |
| 20 | Industrial: thread pool + queue | Bounded workers |

### Day 43 — Multiprocessing (22)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `multiprocessing.Process` | `Process(target=fn)` |
| 2 | `.start()` / `.join()` | Launch and wait |
| 3 | No GIL limitation | True parallelism |
| 4 | `multiprocessing.Pool` | `Pool(processes=4)` |
| 5 | `pool.map()` / `pool.starmap()` | Parallel apply |
| 6 | `pool.apply_async()` | Non-blocking submit |
| 7 | `multiprocessing.Queue` | IPC queue |
| 8 | `multiprocessing.Pipe` | Two-way communication |
| 9 | `multiprocessing.Value` / `Array` | Shared memory |
| 10 | `multiprocessing.Lock` | Process lock |
| 11 | `multiprocessing.Manager` | Shared objects |
| 12 | Process start methods | `fork`, `spawn`, `forkserver` |
| 13 | `if __name__ == "__main__":` | Required for spawn |
| 14 | Pickling requirement | Args must be picklable |
| 15 | `ProcessPoolExecutor` | `concurrent.futures` interface |
| 16 | Process vs thread | CPU vs I/O bound |
| 17 | `os.cpu_count()` | Available cores |
| 18 | Shared memory (3.8+) | `multiprocessing.shared_memory` |
| 19 | Anti-pattern: too many processes | Overhead > benefit |
| 20 | Anti-pattern: large data in queue | Use shared memory |
| 21 | Industrial: CPU-bound parallel | Image processing, hashing |
| 22 | Industrial: worker pool | Process pool + queue |

### Day 44 — concurrent.futures (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `ThreadPoolExecutor` | `with ThreadPoolExecutor() as ex:` |
| 2 | `ProcessPoolExecutor` | `with ProcessPoolExecutor() as ex:` |
| 3 | `executor.submit()` | Returns `Future` |
| 4 | `executor.map()` | Ordered results |
| 5 | `Future.result()` | Block until done |
| 6 | `Future.done()` | Check completion |
| 7 | `Future.cancel()` | Cancel pending |
| 8 | `Future.exception()` | Get exception |
| 9 | `as_completed()` | First-done order |
| 10 | `wait()` | Wait for futures |
| 11 | `FIRST_COMPLETED` / `ALL_COMPLETED` | Wait modes |
| 12 | `max_workers` | Pool size |
| 13 | Context manager | Auto shutdown |
| 14 | Exception propagation | `result()` re-raises |
| 15 | Callback | `future.add_done_callback()` |
| 16 | Chaining futures | Result of one → input to next |
| 17 | Anti-pattern: submit without collect | Lost exceptions |
| 18 | Anti-pattern: wrong executor | Thread for I/O, Process for CPU |
| 19 | Industrial: batch API calls | ThreadPool + rate limit |
| 20 | Industrial: parallel computation | ProcessPool for heavy math |

### Day 45 — subprocess (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `subprocess.run()` | `run(["cmd", "arg"])` |
| 2 | `capture_output=True` | Get stdout/stderr |
| 3 | `text=True` | Decode to string |
| 4 | `check=True` | Raise on non-zero exit |
| 5 | `returncode` | Exit code |
| 6 | `stdout` / `stderr` | Output access |
| 7 | `input=` | Send stdin |
| 8 | `timeout=` | Kill after timeout |
| 9 | `shell=True` | Shell interpretation (dangerous) |
| 10 | `Popen` | Advanced control |
| 11 | `Popen.communicate()` | Send input, get output |
| 12 | `Popen.poll()` | Check if running |
| 13 | `Popen.wait()` | Wait for completion |
| 14 | Piping processes | `stdout=PIPE` chaining |
| 15 | Environment variables | `env=` parameter |
| 16 | Working directory | `cwd=` parameter |
| 17 | `shlex.split()` | Safe command splitting |
| 18 | Anti-pattern: `shell=True` | Injection risk |
| 19 | Anti-pattern: no timeout | Hanging process |
| 20 | Industrial: shell automation | Build scripts, git ops |

### Day 46 — Memory Management (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Reference counting | Automatic cleanup |
| 2 | `sys.getrefcount()` | Check references |
| 3 | Garbage collector | Cycle detection |
| 4 | `gc` module | `gc.collect()`, `gc.get_objects()` |
| 5 | `__del__` finalizer | Avoid if possible |
| 6 | `weakref` | `weakref.ref(obj)` |
| 7 | `WeakValueDictionary` | Auto-evicting cache |
| 8 | `__slots__` | Remove `__dict__` overhead |
| 9 | `sys.getsizeof()` | Object size in bytes |
| 10 | `tracemalloc` | Memory tracing |
| 11 | `tracemalloc.get_traced_memory()` | Peak tracking |
| 12 | Generators vs lists | Memory comparison |
| 13 | Interning | String/int caching |
| 14 | Copy semantics | Shallow vs deep |
| 15 | Circular references | `gc` handles them |
| 16 | Memory leaks | Long-lived references |
| 17 | `__sizeof__()` | Object's own memory |
| 18 | Anti-pattern: cache without bound | Memory grows forever |
| 19 | Anti-pattern: circular refs with `__del__` | GC can't collect |
| 20 | Industrial: memory profiling | `tracemalloc` snapshots |

### Day 47 — Profiling (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `time.perf_counter()` | Wall-clock timing |
| 2 | `time.process_time()` | CPU time |
| 3 | `timeit` module | `timeit.timeit(stmt, number=)` |
| 4 | `cProfile` | `python -m cProfile script.py` |
| 5 | `cProfile` programmatic | `cProfile.run()` |
| 6 | `pstats` | Profile stats analysis |
| 7 | `snakeviz` | Visual profiler |
| 8 | `line_profiler` | `@profile` per-line |
| 9 | `memory_profiler` | `@profile` memory per-line |
| 10 | `tracemalloc` (recap) | Memory snapshots |
| 11 | Big-O validation | Measure scaling |
| 12 | Benchmarking best practices | Warm-up, multiple runs |
| 13 | `dis` module | Bytecode disassembly |
| 14 | `sys.getsizeof` chain | Deep size measurement |
| 15 | Hotspot identification | Top cumulative time |
| 16 | I/O vs CPU bottleneck | Profile tells you |
| 17 | Anti-pattern: premature optimization | Profile first |
| 18 | Anti-pattern: micro-benchmarks | Measure real workload |
| 19 | Industrial: CI perf regression | Benchmark in pipeline |
| 20 | Industrial: production profiling | Sampling profiler |

### Day 48 — Performance Patterns (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `lru_cache` memoization | Avoid recomputation |
| 2 | Lazy evaluation | Compute when needed |
| 3 | Generator pipelines | Stream processing |
| 4 | Batch operations | Amortize overhead |
| 5 | `__slots__` for many objects | Memory reduction |
| 6 | String join vs concat | `"".join()` is O(n) |
| 7 | Set for lookups | O(1) vs O(n) list |
| 8 | Dict lookup vs if/elif | O(1) dispatch |
| 9 | List comprehension vs loop | CPython optimization |
| 10 | `collections.deque` for queue | O(1) popleft |
| 11 | `bisect` for sorted insert | O(log n) |
| 12 | `array.array` for numeric | Less memory than list |
| 13 | Pre-allocation | `[None] * n` |
| 14 | Local variable faster | Less lookup overhead |
| 15 | Avoid global state | Namespace lookup cost |
| 16 | `map()` vs comprehension | Sometimes faster |
| 17 | Anti-pattern: nested loops on large data | Consider hashmap |
| 18 | Anti-pattern: repeated computation | Cache results |
| 19 | Industrial: query caching | LRU + TTL |
| 20 | Industrial: bulk processing | Batch I/O operations |

### Day 49 — struct / array / memoryview (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `struct.pack()` | `struct.pack("!I", 42)` |
| 2 | `struct.unpack()` | `struct.unpack("!I", data)` |
| 3 | Format strings | `b`, `h`, `i`, `f`, `d`, `s` |
| 4 | Byte order | `!` network, `<` little, `>` big |
| 5 | `struct.calcsize()` | Size of format |
| 6 | `array.array` | `array("i", [1,2,3])` |
| 7 | `array` type codes | `b`, `i`, `f`, `d` |
| 8 | `array` vs list | Typed, compact |
| 9 | `array` file I/O | `.tofile()`, `.fromfile()` |
| 10 | `memoryview` | `mv = memoryview(buf)` |
| 11 | Zero-copy slicing | `mv[10:20]` |
| 12 | `memoryview.cast()` | Reinterpret type |
| 13 | Buffer protocol | `bytes`, `bytearray`, `array` |
| 14 | `bytes` vs `bytearray` | Immutable vs mutable |
| 15 | `bytearray` operations | `ba[0] = 0xFF` |
| 16 | Binary file reading | `struct.unpack` from file |
| 17 | Network packet parsing | Header format strings |
| 18 | Anti-pattern: string for binary | Use bytes/struct |
| 19 | Industrial: binary protocol | Pack/unpack messages |
| 20 | Industrial: high-perf buffer | memoryview pipeline |

### Day 50 — Concurrency Project (20)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Project architecture | Modules, interfaces |
| 2 | Async HTTP client | `aiohttp.ClientSession` |
| 3 | Rate limiter | Semaphore-based |
| 4 | Retry logic | Exponential backoff |
| 5 | Result aggregation | `asyncio.gather()` |
| 6 | Error collection | `return_exceptions=True` |
| 7 | Progress reporting | Callback or queue |
| 8 | Generator pipeline | Transform results |
| 9 | File output | Async or sync write |
| 10 | Configuration | Dataclass config |
| 11 | Logging integration | `logging.getLogger` |
| 12 | Testing async | `pytest-asyncio` |
| 13 | CLI interface | `argparse` entry point |
| 14 | Graceful shutdown | Signal handling |
| 15 | Performance measurement | `time.perf_counter` |
| 16 | Type annotations | Full typing |
| 17 | Anti-pattern: no error handling | Silent failures |
| 18 | Anti-pattern: no timeout | Hanging requests |
| 19 | Industrial: production scraper | All patterns combined |
| 20 | Industrial: monitoring | Metrics + logging |

---

## Sunday Labs (Phase 3)

| Lab | After | Build |
|-----|-------|-------|
| 08 | Days 35–40 | Async data pipeline: generator → async transform → JSONL |
| 09 | Days 41–45 | Thread + process hybrid: I/O pool + CPU pool + subprocess |
| 10 | Days 46–50 | Profiled scraper: async + caching + memory tracking |
