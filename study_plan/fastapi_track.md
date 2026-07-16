# Phase 5 — FastAPI Track (Days 71–86)

> Track: `fastapi_track` · Outcome: REST APIs, middleware, auth, deployment

## Day Plan

| Day | Topic | Slug | Exercise direction |
|-----|-------|------|--------------------|
| 71 | FastAPI basics | `day_71_fastapi_basics` | Hello world, path params |
| 72 | Request & response models | `day_72_models` | Pydantic schemas |
| 73 | Path, query, body params | `day_73_params` | CRUD endpoints |
| 74 | Dependency injection | `day_74_di` | `Depends()`, shared logic |
| 75 | Database integration | `day_75_database` | SQLAlchemy + FastAPI |
| 76 | Authentication & JWT | `day_76_auth` | Login, protected routes |
| 77 | Middleware & CORS | `day_77_middleware` | Logging, timing, CORS |
| 78 | Error handling | `day_78_errors` | Custom handlers, HTTP exceptions |
| 79 | Background tasks | `day_79_background` | Email, cleanup tasks |
| 80 | File upload & streaming | `day_80_files` | Upload, download, streaming |
| 81 | WebSockets | `day_81_websockets` | Chat, real-time updates |
| 82 | Testing FastAPI | `day_82_testing` | TestClient, async tests |
| 83 | OpenAPI & docs | `day_83_openapi` | Schema customization |
| 84 | Performance & caching | `day_84_performance` | Redis, response cache |
| 85 | Docker & deployment | `day_85_deployment` | Dockerfile, uvicorn, gunicorn |
| 86 | FastAPI project | `day_86_project` | Full REST API |

---

## Concept Checklists

### Day 71 — FastAPI Basics (26)

**Prerequisites:** Day 14 (tooling/venv), Day 39 (async/await), Day 03 (functions).
**Real-world use:** every backend service starts here — declaring typed routes, auto-validated params, and self-documenting JSON endpoints served by an ASGI server.
**Production example (code.py):** a versioned health + resource service — `APIRouter(prefix="/api/v1")` mounting `GET /health` (liveness) and `GET /items/{item_id}` with a typed path param, wired through a lifespan that opens/closes a shared resource, with request logic delegated to a service layer.
**Sources:** [FastAPI — First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) · [FastAPI — Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `FastAPI()` app | `app = FastAPI()` |
| 2 | `@app.get()` | Route decorator |
| 3 | `@app.post()` / `put()` / `delete()` | HTTP methods |
| 4 | Path parameters | `@app.get("/items/{id}")` |
| 5 | Type-annotated params | `def read(id: int):` |
| 6 | Auto-validation | 422 on wrong type |
| 7 | `uvicorn` | `uvicorn main:app --reload` |
| 8 | Interactive docs | `/docs` (Swagger), `/redoc` |
| 9 | Response return | Return dict → JSON |
| 10 | Status codes | `status_code=201` |
| 11 | `JSONResponse` | Explicit response |
| 12 | Router | `APIRouter(prefix="/api")` |
| 13 | `app.include_router()` | Mount router |
| 14 | Async endpoints | `async def endpoint():` |
| 15 | Sync vs async | When to use which |
| 16 | `Request` object | `request: Request` |
| 17 | `Response` object | Set headers, cookies |
| 18 | Startup/shutdown events | `@app.on_event("startup")` |
| 19 | Lifespan context | `@asynccontextmanager` lifespan |
| 20 | Anti-pattern: logic in routes | Use service layer |
| 21 | Anti-pattern: no validation | Always type params |
| 22 | Industrial: project structure | Router + service + model |
| 23 | Enum path parameters | `class Name(str, Enum)` predefined values |
| 24 | `fastapi` CLI | `fastapi dev main.py`, `fastapi run` |
| 25 | Path operation order | Fixed paths before `{param}` routes |
| 26 | Response classes | `HTMLResponse`, `PlainTextResponse`, `RedirectResponse` |

### Day 72 — Request & Response Models (30)

**Prerequisites:** Day 71 (routes/response), Day 20 (dataclasses), Day 31 (typing basics).
**Real-world use:** every request/response crosses a validation boundary — Pydantic v2 models parse, coerce, and validate untrusted JSON and shape exactly what the API returns.
**Production example (code.py):** an order API with separated schemas — `OrderCreate` (input) validated with `@field_validator` + constrained types, `OrderResponse` (output, `from_attributes=True`) with a `@computed_field` total, and a reusable `Money` value type used across nested line items.
**Sources:** [Pydantic — Models](https://docs.pydantic.dev/latest/concepts/models/) · [FastAPI — Request Body](https://fastapi.tiangolo.com/tutorial/body/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Pydantic `BaseModel` | `class Item(BaseModel):` |
| 2 | Field types | `str`, `int`, `float`, `bool` |
| 3 | Optional fields | `name: str | None = None` |
| 4 | Default values | `count: int = 0` |
| 5 | `Field()` | `Field(ge=0, description="...")` |
| 6 | Nested models | Model inside model |
| 7 | `model_validate()` | Create from dict |
| 8 | `model_dump()` | Convert to dict |
| 9 | `model_dump_json()` | Convert to JSON |
| 10 | Response model | `response_model=Item` |
| 11 | `response_model_exclude` | Hide fields |
| 12 | Input vs output models | `CreateItem` vs `ItemResponse` |
| 13 | `@field_validator` | Custom validation |
| 14 | `@model_validator` | Cross-field validation |
| 15 | Config | `model_config = ConfigDict(...)` |
| 16 | `from_attributes=True` | ORM mode |
| 17 | Enum in models | `status: Status` |
| 18 | Anti-pattern: dict everywhere | Use models |
| 19 | Anti-pattern: one model for all | Separate in/out |
| 20 | Industrial: schema versioning | V1/V2 models |
| 21 | `Annotated` field style | `Annotated[int, Field(ge=0)]` |
| 22 | `Field(default_factory=...)` | Safe mutable defaults |
| 23 | Field aliases | `alias=`, `populate_by_name`, `by_alias` |
| 24 | Special types | `EmailStr`, `HttpUrl`, `UUID`, `datetime` |
| 25 | Constrained types | `PositiveInt`, `conint`, `constr` |
| 26 | `@computed_field` | Derived/read-only properties |
| 27 | `@field_serializer` / `@model_serializer` | Custom serialization |
| 28 | Discriminated unions | `Field(discriminator="type")` |
| 29 | `ValidationError.errors()` | Inspect field-level failures |
| 30 | Strict vs lax mode | Coercion control, `Strict` types |

### Day 73 — Path, Query, Body Params (27)

**Prerequisites:** Day 72 (Pydantic models), Day 71 (routing), Day 31 (typing).
**Real-world use:** correct parameter typing and constraints are the first line of defense — they reject bad input at the edge with a 422 before any handler code runs.
**Production example (code.py):** a paginated, filterable `GET /products` — `Annotated` query params with `min_length`/numeric bounds, a `sort` enum, a list-valued `tags` filter, and a validated `{product_id}` path param, returning a typed page envelope.
**Sources:** [FastAPI — Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/) · [FastAPI — Request Body](https://fastapi.tiangolo.com/tutorial/body/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Path parameters | `{item_id}` in route |
| 2 | `Path()` | `Path(ge=1, description="...")` |
| 3 | Query parameters | `def read(skip: int = 0):` |
| 4 | `Query()` | `Query(max_length=50)` |
| 5 | Required query | No default value |
| 6 | Optional query | `q: str | None = None` |
| 7 | Body parameter | Pydantic model in args |
| 8 | `Body()` | `Body(embed=True)` |
| 9 | Multiple body params | Multiple models |
| 10 | `Header()` | `x_token: str = Header()` |
| 11 | `Cookie()` | `session: str = Cookie()` |
| 12 | `Form()` | Form data |
| 13 | `File()` / `UploadFile` | File uploads |
| 14 | Mixed parameters | Path + query + body |
| 15 | Validation | Auto from type hints |
| 16 | Custom validation | `@field_validator` |
| 17 | Anti-pattern: too many params | Group in model |
| 18 | Anti-pattern: no validation | Always constrain |
| 19 | Industrial: pagination | `skip`, `limit` params |
| 20 | Industrial: filtering | Query params for search |
| 21 | `Annotated` param style | `Annotated[int, Path(ge=1)]` |
| 22 | Query list / multiple values | `list[str] = Query()` |
| 23 | Query param alias | `Query(alias="item-query")` |
| 24 | Numeric constraints | `gt`, `ge`, `lt`, `le` |
| 25 | String constraints | `min_length`, `max_length`, `pattern` |
| 26 | Enum params | Predefined choices |
| 27 | Pydantic model as query params | `Annotated[Filters, Query()]` |

### Day 74 — Dependency Injection (24)

**Prerequisites:** Day 71 (routes), Day 27 (context managers/yield), Day 64 (DI/repository).
**Real-world use:** dependency injection wires DB sessions, current-user, settings, and shared services into routes — testable, reusable, and cleaned up per request.
**Production example (code.py):** a request-scoped dependency stack — a `yield` DB-session dependency, a `get_current_user` auth dependency layered on it, and a settings dependency, all exposed as reusable `Annotated` aliases and overridable in tests.
**Sources:** [FastAPI — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) · [FastAPI — Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependency-injection-in-fastapi/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `Depends()` | `def endpoint(dep=Depends(fn)):` |
| 2 | Function dependency | Returns value |
| 3 | Class dependency | `__init__` + callable |
| 4 | Nested dependencies | Depends in Depends |
| 5 | Shared dependencies | Same instance per request |
| 6 | Yield dependencies | `yield` for cleanup |
| 7 | Async dependencies | `async def dep():` |
| 8 | DB session dependency | `get_db()` → yield Session |
| 9 | Auth dependency | `get_current_user()` |
| 10 | Global dependencies | `app = FastAPI(dependencies=[])` |
| 11 | Router dependencies | `APIRouter(dependencies=[])` |
| 12 | Override in testing | `app.dependency_overrides[dep] = mock` |
| 13 | Parameterized deps | Factory returning dependency |
| 14 | Dependency caching | `use_cache=True` default |
| 15 | Security dependencies | `HTTPBearer`, `OAuth2PasswordBearer` |
| 16 | Anti-pattern: global state | Use DI instead |
| 17 | Anti-pattern: no cleanup | Use yield deps |
| 18 | Industrial: service injection | Business logic layer |
| 19 | Industrial: config injection | Settings dependency |
| 20 | Industrial: multi-tenant | Tenant from header |
| 21 | `Annotated` dependency style | `Annotated[Session, Depends(get_db)]` |
| 22 | Path-operation `dependencies=` | `@app.get(dependencies=[Depends(verify)])` |
| 23 | Dependency type aliases | Reusable `Annotated` alias |
| 24 | `yield` dep exception handling | Cleanup runs on error too |

### Day 75 — Database Integration (27)

**Prerequisites:** Day 74 (DB dependency), Day 39 (async), Day 64 (repository pattern).
**Real-world use:** real APIs persist state — async SQLAlchemy 2.0 models, sessions, and Alembic migrations back every CRUD endpoint without blocking the event loop.
**Production example (code.py):** an async CRUD service for a resource — `DeclarativeBase`/`Mapped` models, an `AsyncSession` dependency, 2.0-style `select()` with `selectinload` for relationships, transactional writes, and an Alembic migration for the schema.
**Sources:** [SQLAlchemy — Async ORM](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) · [Alembic — Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | SQLAlchemy setup | `create_engine()` + `sessionmaker()` |
| 2 | DB dependency | `def get_db(): yield session` |
| 3 | Model definition | SQLAlchemy models |
| 4 | Pydantic schemas | Request/response models |
| 5 | CRUD functions | `create()`, `read()`, `update()`, `delete()` |
| 6 | `session.add()` | Insert |
| 7 | `session.query()` | Read |
| 8 | `session.commit()` | Persist |
| 9 | `session.refresh()` | Reload from DB |
| 10 | Pagination | `offset()`, `limit()` |
| 11 | Filtering | `.filter()`, `.filter_by()` |
| 12 | Relationships in API | Nested responses |
| 13 | `from_attributes=True` | ORM → Pydantic |
| 14 | Transaction management | Commit/rollback in dependency |
| 15 | Async SQLAlchemy | `create_async_engine()` |
| 16 | Connection pooling | Pool size, overflow |
| 17 | Anti-pattern: no transaction | Data inconsistency |
| 18 | Anti-pattern: N+1 queries | Eager loading |
| 19 | Industrial: repository pattern | Abstract DB access |
| 20 | Industrial: service layer | Business logic separation |
| 21 | Alembic migrations | `revision --autogenerate`, `upgrade head` |
| 22 | `AsyncSession` dependency | `async_sessionmaker` + `yield` |
| 23 | 2.0-style `select()` | `select(Model).where(...)` |
| 24 | `scalars()` / `scalar_one_or_none()` | Result extraction |
| 25 | Eager loading | `selectinload`, `joinedload` |
| 26 | `DeclarativeBase` + `Mapped` | Typed ORM models, `mapped_column` |
| 27 | Transaction block | `async with session.begin():` |

### Day 76 — Authentication & JWT (24)

**Prerequisites:** Day 75 (user table/DB), Day 74 (auth dependency), Day 10 (exceptions).
**Real-world use:** authentication and authorization gate every non-public endpoint — hashed passwords, signed JWTs, and role checks protect user data.
**Production example (code.py):** an OAuth2 password-flow auth module — `POST /token` verifying a `CryptContext`-hashed password and issuing a JWT with `exp`, plus a `get_current_active_user` dependency that decodes the bearer token and enforces role/scope on protected routes.
**Sources:** [FastAPI — OAuth2 with JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) · [FastAPI — Security](https://fastapi.tiangolo.com/tutorial/security/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `OAuth2PasswordBearer` | Token endpoint |
| 2 | `OAuth2PasswordRequestForm` | Login form |
| 3 | Password hashing | `passlib` / `bcrypt` |
| 4 | JWT creation | `jose.jwt.encode()` |
| 5 | JWT decode | `jose.jwt.decode()` |
| 6 | Token expiry | `exp` claim + `timedelta` |
| 7 | `get_current_user` dep | Decode → query user |
| 8 | Protected routes | `Depends(get_current_user)` |
| 9 | Role-based access | Check user role |
| 10 | Refresh tokens | Separate endpoint |
| 11 | Token revocation | Blacklist or short-lived |
| 12 | API key auth | `APIKeyHeader` |
| 13 | HTTP Basic auth | `HTTPBasic` |
| 14 | Scopes | `Security(dep, scopes=["read"])` |
| 15 | Password validation | Min length, complexity |
| 16 | Anti-pattern: token in URL | Use Authorization header |
| 17 | Anti-pattern: no expiry | Set short TTL |
| 18 | Industrial: auth service | Separate auth module |
| 19 | Industrial: middleware auth | Verify before route |
| 20 | Testing auth | Override auth dependency |
| 21 | `CryptContext` | `passlib` hash + verify |
| 22 | `WWW-Authenticate` header | `Bearer` on 401 responses |
| 23 | Active user check | Reject disabled accounts |
| 24 | `Token` response model | `access_token` + `token_type` |

### Day 77 — Middleware & CORS (24)

**Prerequisites:** Day 71 (Request/Response), Day 49 (logging), Day 76 (security context).
**Real-world use:** cross-cutting concerns — CORS, request IDs, timing, compression, and security headers — belong in middleware, applied uniformly to every request.
**Production example (code.py):** an observability + security middleware stack — a custom timing/request-ID/logging middleware, `CORSMiddleware` restricted to configured origins with credentials, `GZipMiddleware`, and injected security headers (HSTS/CSP).
**Sources:** [FastAPI — CORS](https://fastapi.tiangolo.com/tutorial/cors/) · [FastAPI — Advanced Middleware](https://fastapi.tiangolo.com/advanced/middleware/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `@app.middleware("http")` | Custom middleware |
| 2 | `call_next(request)` | Pass to next handler |
| 3 | Request timing | Start → call_next → end |
| 4 | Request logging | Log method, path, status |
| 5 | `CORSMiddleware` | `add_middleware(CORSMiddleware)` |
| 6 | CORS origins | `allow_origins=["*"]` |
| 7 | CORS methods | `allow_methods=["GET", "POST"]` |
| 8 | CORS headers | `allow_headers=["Authorization"]` |
| 9 | `TrustedHostMiddleware` | Host validation |
| 10 | `GZipMiddleware` | Response compression |
| 11 | Custom headers | Add via middleware |
| 12 | Request ID | UUID per request |
| 13 | Rate limiting middleware | Token bucket |
| 14 | Error handling middleware | Catch + format |
| 15 | Middleware order | First added = outermost |
| 16 | `Starlette` middleware | Base class |
| 17 | Anti-pattern: heavy middleware | Slow every request |
| 18 | Anti-pattern: CORS `*` in prod | Restrict origins |
| 19 | Industrial: observability middleware | Timing + logging + tracing |
| 20 | Industrial: security headers | CSP, HSTS |
| 21 | `BaseHTTPMiddleware` class | Reusable class-based middleware |
| 22 | CORS credentials | `allow_credentials=True` |
| 23 | CORS preflight | `OPTIONS`, `max_age`, `expose_headers` |
| 24 | Pure ASGI middleware | Wrap the ASGI app directly |

### Day 78 — Error Handling (24)

**Prerequisites:** Day 10 (exceptions/domain errors), Day 72 (models), Day 71 (responses).
**Real-world use:** consistent, safe error responses — mapping domain exceptions to HTTP status codes with machine-readable bodies and no leaked stack traces.
**Production example (code.py):** a uniform error layer — domain exceptions (`NotFoundError`, `ConflictError`) mapped via `@app.exception_handler` to an RFC 7807-style JSON body, a `RequestValidationError` handler surfacing field errors, and structured logging of 5xx.
**Sources:** [FastAPI — Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [Pydantic — Model Validation](https://docs.pydantic.dev/latest/concepts/models/#model-validation)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `HTTPException` | `raise HTTPException(404)` |
| 2 | `detail` parameter | Error message |
| 3 | `headers` parameter | Custom headers |
| 4 | Custom exception classes | `class NotFound(HTTPException):` |
| 5 | `@app.exception_handler()` | Custom handler |
| 6 | `RequestValidationError` | 422 handler |
| 7 | `StarletteHTTPException` | Base HTTP exception |
| 8 | Error response model | Consistent format |
| 9 | Domain exceptions | `class OrderError(Exception):` |
| 10 | Exception → HTTP mapping | Domain → status code |
| 11 | Validation error format | Field-level errors |
| 12 | Global error handler | Catch-all |
| 13 | Logging errors | `logger.exception()` |
| 14 | Error codes | Machine-readable codes |
| 15 | Problem details (RFC 7807) | Standard error format |
| 16 | Anti-pattern: generic 500 | Specific error codes |
| 17 | Anti-pattern: stack trace in response | Log only |
| 18 | Industrial: error catalog | Documented error codes |
| 19 | Industrial: error monitoring | Sentry integration |
| 20 | Testing error responses | Assert status + body |
| 21 | `status` constants | `status.HTTP_404_NOT_FOUND` |
| 22 | Override default handlers | `@app.exception_handler(HTTPException)` |
| 23 | `RequestValidationError.errors()` | Access invalid fields |
| 24 | Handler returns `JSONResponse` | Custom body + status code |

### Day 79 — Background Tasks (22)

**Prerequisites:** Day 71 (endpoints), Day 39 (async), Day 74 (dependencies).
**Real-world use:** offload slow, non-critical work (emails, audit logs, cleanup) so the response returns fast, escalating to Celery/arq when durability is needed.
**Production example (code.py):** a signup endpoint that returns 201 immediately and schedules background work — a `BackgroundTasks` welcome-email send plus an audit-log write, with a documented threshold for graduating to a distributed queue.
**Sources:** [FastAPI — Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) · [asyncio — Tasks](https://docs.python.org/3/library/asyncio-task.html)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `BackgroundTasks` | `def endpoint(bg: BackgroundTasks):` |
| 2 | `bg.add_task()` | Schedule after response |
| 3 | Task with arguments | `add_task(fn, arg1, arg2)` |
| 4 | Multiple tasks | Add several |
| 5 | Async background tasks | `async def task():` |
| 6 | Dependency + background | `Depends` returning tasks |
| 7 | Email sending | Background email |
| 8 | File cleanup | Remove temp files |
| 9 | Logging / audit | Background audit log |
| 10 | Notification | Push notifications |
| 11 | Celery overview | Distributed task queue |
| 12 | Celery vs BackgroundTasks | Simple vs distributed |
| 13 | `arq` overview | Async task queue |
| 14 | Task retry | Handle failures |
| 15 | Task timeout | Prevent hanging |
| 16 | Anti-pattern: heavy background | Use Celery instead |
| 17 | Anti-pattern: no error handling | Tasks fail silently |
| 18 | Industrial: webhook delivery | Retry + timeout |
| 19 | Industrial: report generation | Async + notify |
| 20 | Testing background tasks | Sync execution in tests |
| 21 | `BackgroundTask` (Starlette) | Single task attached to a `Response` |
| 22 | Runs after response sent | Ordering guarantee, not for critical work |

### Day 80 — File Upload & Streaming (23)

**Prerequisites:** Day 09 (file I/O), Day 40 (async I/O), Day 71 (responses).
**Real-world use:** APIs ingest and serve files — validated uploads and memory-safe streaming for large downloads and generated exports.
**Production example (code.py):** an upload/download service — `UploadFile` validated for size and MIME, streamed to disk (or proxied to object storage) in chunks, and a `StreamingResponse` that generates a CSV export lazily with a `Content-Disposition` header.
**Sources:** [FastAPI — Request Files](https://fastapi.tiangolo.com/tutorial/request-files/) · [Starlette](https://www.starlette.io/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `UploadFile` | `file: UploadFile` |
| 2 | `File()` | `file: bytes = File()` |
| 3 | `file.read()` | Read contents |
| 4 | `file.filename` | Original name |
| 5 | `file.content_type` | MIME type |
| 6 | Multiple files | `files: list[UploadFile]` |
| 7 | Save to disk | Write chunks |
| 8 | File size limit | Validate before save |
| 9 | Allowed types | Check extension/MIME |
| 10 | `StreamingResponse` | `StreamingResponse(gen)` |
| 11 | `FileResponse` | Serve static file |
| 12 | CSV streaming | Generate rows lazily |
| 13 | Large file download | Chunked transfer |
| 14 | `aiofiles` integration | Async file ops |
| 15 | Temp file handling | Save → process → delete |
| 16 | Anti-pattern: read all to memory | Stream large files |
| 17 | Anti-pattern: no type check | Malicious uploads |
| 18 | Industrial: S3 upload | Proxy to cloud storage |
| 19 | Industrial: image processing | Upload → resize → store |
| 20 | Testing uploads | `TestClient` with files |
| 21 | `UploadFile` async I/O | `await file.read()`, `.seek()`, `.close()` |
| 22 | `Content-Disposition` | `attachment; filename=` for downloads |
| 23 | `media_type` on responses | Correct MIME on stream/file responses |

### Day 81 — WebSockets (22)

**Prerequisites:** Day 39 (async), Day 74 (dependencies), Day 76 (auth).
**Real-world use:** WebSockets power real-time features — chat, live dashboards, notifications — over a persistent bidirectional connection.
**Production example (code.py):** a chat server — a `ConnectionManager` tracking active sockets per room, token-authenticated `accept()`, JSON message broadcast, and clean `WebSocketDisconnect` handling that removes dead connections.
**Sources:** [FastAPI — WebSockets](https://fastapi.tiangolo.com/advanced/websockets/) · [Starlette — WebSockets](https://www.starlette.io/websockets/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `@app.websocket()` | WebSocket route |
| 2 | `websocket.accept()` | Accept connection |
| 3 | `websocket.receive_text()` | Receive message |
| 4 | `websocket.send_text()` | Send message |
| 5 | `websocket.close()` | Close connection |
| 6 | JSON messages | `receive_json()` / `send_json()` |
| 7 | Connection manager | Track active connections |
| 8 | Broadcast | Send to all clients |
| 9 | Rooms/channels | Group connections |
| 10 | Error handling | `WebSocketDisconnect` |
| 11 | Authentication | Token in query or first message |
| 12 | Heartbeat/ping | Keep connection alive |
| 13 | Binary messages | `receive_bytes()` / `send_bytes()` |
| 14 | Concurrent WS + HTTP | Same app |
| 15 | Rate limiting | Per-connection limits |
| 16 | Anti-pattern: no disconnect handling | Clean up connections |
| 17 | Anti-pattern: blocking in WS | Use async |
| 18 | Industrial: chat server | Rooms + broadcast |
| 19 | Industrial: live dashboard | Push updates |
| 20 | Testing WebSockets | `TestClient.websocket_connect()` |
| 21 | Dependencies in WebSocket | `Depends()` in a `websocket` route |
| 22 | Close codes | `websocket.close(code=1008)` |

### Day 82 — Testing FastAPI (23)

**Prerequisites:** Day 59 (pytest fixtures), Day 74 (dependency overrides), Day 47 (testing async).
**Real-world use:** every endpoint needs automated tests — `TestClient`/async clients with dependency overrides and a test DB make the suite fast and deterministic.
**Production example (code.py):** an API test suite — pytest fixtures building a `TestClient` with `app.dependency_overrides` swapping in a transactional test DB and a fake current-user, covering happy-path, 422, and auth-failure cases.
**Sources:** [FastAPI — Testing](https://fastapi.tiangolo.com/tutorial/testing/) · [pytest — Docs](https://docs.pytest.org/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `TestClient` | `client = TestClient(app)` |
| 2 | `client.get()` / `post()` | HTTP methods |
| 3 | Assert status | `assert resp.status_code == 200` |
| 4 | Assert JSON | `resp.json()` |
| 5 | Request headers | `headers={"Authorization": ...}` |
| 6 | Request body | `json={"key": "val"}` |
| 7 | Query params | `params={"q": "search"}` |
| 8 | Dependency override | `app.dependency_overrides[dep] = mock` |
| 9 | DB testing | Override `get_db` |
| 10 | Async TestClient | `httpx.AsyncClient` |
| 11 | Fixture setup | pytest fixtures for app/client |
| 12 | Factory fixtures | Create test data |
| 13 | Auth in tests | Inject token/user |
| 14 | File upload tests | `files={"file": ...}` |
| 15 | WebSocket tests | `client.websocket_connect()` |
| 16 | Integration vs unit | Full app vs isolated |
| 17 | Anti-pattern: test implementation | Test behavior |
| 18 | Anti-pattern: shared state | Isolate tests |
| 19 | Industrial: CI test suite | Automated testing |
| 20 | Industrial: contract tests | Schema validation |
| 21 | Lifespan in tests | `with TestClient(app) as client:` |
| 22 | `httpx.ASGITransport` | Wire async client to the app |
| 23 | `@pytest.mark.parametrize` | Table-driven request cases |

### Day 83 — OpenAPI & Docs (23)

**Prerequisites:** Day 72 (models/schema), Day 71 (routes), Day 76 (security schemes).
**Real-world use:** the OpenAPI schema is the API contract — accurate tags, descriptions, examples, and response models drive client SDKs and interactive docs.
**Production example (code.py):** a fully documented router — `summary`/`description`/`tags`, `responses=` documenting error codes, model `examples`, and app metadata (`title`, `version`, `openapi_tags`) producing a clean `/docs` and an exportable `/openapi.json`.
**Sources:** [FastAPI — Official docs](https://fastapi.tiangolo.com/) · [Pydantic — Models](https://docs.pydantic.dev/latest/concepts/models/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Auto-generated docs | `/docs`, `/redoc` |
| 2 | `summary` / `description` | Route documentation |
| 3 | `tags` | Group endpoints |
| 4 | `response_model` | Document response |
| 5 | `responses=` | Multiple response codes |
| 6 | `deprecated=True` | Mark deprecated |
| 7 | Model `json_schema_extra` | Example values |
| 8 | `Field(example=...)` | Field examples |
| 9 | `openapi_extra` | Custom OpenAPI fields |
| 10 | Custom OpenAPI schema | `app.openapi()` override |
| 11 | API versioning | Prefix or header |
| 12 | Security schemes | OAuth2 in docs |
| 13 | Export OpenAPI JSON | `/openapi.json` |
| 14 | Code generation | From OpenAPI spec |
| 15 | Changelog | Document breaking changes |
| 16 | Anti-pattern: no docs | Always document |
| 17 | Anti-pattern: outdated docs | Auto-generate from code |
| 18 | Industrial: API portal | Host interactive docs |
| 19 | Industrial: client SDK | Generate from spec |
| 20 | Industrial: API governance | Schema review process |
| 21 | App metadata | `title`, `version`, `description`, `openapi_tags` |
| 22 | `examples=` (OpenAPI 3.1) | Multiple named examples |
| 23 | Disable / relocate docs | `docs_url=None`, `openapi_url` |

### Day 84 — Performance & Caching (23)

**Prerequisites:** Day 39 (async), Day 75 (DB/pooling), Day 30 (itertools/streaming).
**Real-world use:** latency and throughput matter — response caching, connection pooling, and non-blocking I/O keep an API fast under load.
**Production example (code.py):** a read-through cache layer — a Redis-backed cache dependency with TTL and invalidation-on-write around a hot `GET` endpoint, an `ORJSONResponse` default, and cursor pagination to bound query cost.
**Sources:** [FastAPI — Official docs](https://fastapi.tiangolo.com/) · [Uvicorn](https://www.uvicorn.org/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Response caching | `Cache-Control` headers |
| 2 | Redis integration | `aioredis` / `redis-py` |
| 3 | Cache decorator | Key → Redis → return |
| 4 | TTL-based cache | Expiry on keys |
| 5 | Cache invalidation | On write, purge key |
| 6 | ETag / conditional | `If-None-Match` |
| 7 | Async endpoints | Non-blocking I/O |
| 8 | Connection pooling | DB + Redis pools |
| 9 | N+1 query prevention | Eager loading |
| 10 | Pagination | Offset or cursor-based |
| 11 | Response compression | GZip middleware |
| 12 | Profiling endpoints | Timing middleware |
| 13 | Load testing | `locust`, `hey` |
| 14 | Worker configuration | `uvicorn --workers` |
| 15 | Gunicorn + uvicorn | Production setup |
| 16 | Anti-pattern: unbounded queries | Always paginate |
| 17 | Anti-pattern: sync in async | Blocks event loop |
| 18 | Industrial: Redis cache layer | Read-through cache |
| 19 | Industrial: CDN integration | Static + API caching |
| 20 | Industrial: APM | Application monitoring |
| 21 | `ORJSONResponse` | Faster JSON serialization |
| 22 | Async DB drivers | `asyncpg` / `aiomysql` non-blocking I/O |
| 23 | Cache stampede protection | Lock / single-flight on miss |

### Day 85 — Docker & Deployment (24)

**Prerequisites:** Day 14 (tooling/deps), Day 71 (uvicorn), Day 83 (settings preview).
**Real-world use:** shipping to production means a small, secure, reproducible container image and a correct ASGI process model behind a proxy.
**Production example (code.py):** a production container — a multi-stage `Dockerfile` on `python:3.12-slim` running as a non-root user, dependency-layer caching, a `/health` endpoint, `--proxy-headers` for a reverse proxy, and a Compose file wiring app + DB.
**Sources:** [FastAPI — Docker Deployment](https://fastapi.tiangolo.com/deployment/docker/) · [Docker — Official docs](https://docs.docker.com/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Dockerfile for FastAPI | Multi-stage build |
| 2 | Base image | `python:3.12-slim` |
| 3 | `COPY` / `RUN` | Install deps, copy code |
| 4 | `CMD` | `uvicorn main:app` |
| 5 | `.dockerignore` | Exclude files |
| 6 | Environment variables | `ENV` / `--env` |
| 7 | Docker Compose | Multi-service setup |
| 8 | Health check | `/health` endpoint |
| 9 | Gunicorn config | Workers, timeout |
| 10 | `uvicorn` production | `--host 0.0.0.0 --port 8000` |
| 11 | Logging in container | Stdout/stderr |
| 12 | Secrets management | Don't bake in image |
| 13 | Multi-stage build | Reduce image size |
| 14 | Non-root user | Security best practice |
| 15 | Graceful shutdown | Signal handling |
| 16 | Anti-pattern: root user | Run as non-root |
| 17 | Anti-pattern: fat image | Multi-stage + slim base |
| 18 | Industrial: CI/CD pipeline | Build → test → deploy |
| 19 | Industrial: Kubernetes basics | Deployment + service |
| 20 | Industrial: cloud deployment | AWS/GCP/Azure overview |
| 21 | Layer caching | Copy deps before source code |
| 22 | `WORKDIR` / `EXPOSE` | Image conventions |
| 23 | Behind a proxy | `--proxy-headers`, `root_path` |
| 24 | Reverse proxy | nginx / Traefik TLS termination |

### Day 86 — FastAPI Project (23)

**Prerequisites:** Days 71–85 (entire FastAPI track), Day 65 (packaging), Day 67 (CI).
**Real-world use:** a portfolio-grade REST API that ties every prior day together — the artifact you show in interviews and deploy for real.
**Production example (code.py):** a complete multi-resource REST API — layered `app/routers/services/models`, JWT auth, async SQLAlchemy + Alembic, Pydantic schemas, custom error handlers, middleware, one background task, tests, Docker, and CI.
**Sources:** Builds on Days 71–85 `fastapi_track` modules · [FastAPI — Tutorial](https://fastapi.tiangolo.com/tutorial/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Project structure | `app/`, `routers/`, `models/`, `services/` |
| 2 | Config management | `pydantic-settings` |
| 3 | Database setup | SQLAlchemy + Alembic |
| 4 | Auth module | JWT + password hashing |
| 5 | CRUD endpoints | Full REST for 2+ resources |
| 6 | Validation | Pydantic models |
| 7 | Error handling | Custom handlers |
| 8 | Middleware | Logging, CORS, timing |
| 9 | Background tasks | At least one |
| 10 | Testing | TestClient + fixtures |
| 11 | OpenAPI docs | Tags, descriptions |
| 12 | Docker | Dockerfile + compose |
| 13 | CI pipeline | Test + lint |
| 14 | README | Setup, usage, API docs |
| 15 | Type annotations | Full coverage |
| 16 | Logging | Structured JSON |
| 17 | Anti-pattern: monolith route file | Split by resource |
| 18 | Anti-pattern: no tests | Minimum 80% coverage |
| 19 | Industrial: production checklist | Security + monitoring |
| 20 | Code review | Final quality pass |
| 21 | Alembic migrations | Schema versioning committed to repo |
| 22 | Pagination & filtering | Consistent list endpoints |
| 23 | Rate limiting & security headers | Production hardening |

---

## Sunday Labs (Phase 5)

| Lab | After | Build |
|-----|-------|-------|
| 15 | Days 71–75 | CRUD API: FastAPI + SQLAlchemy + Pydantic |
| 16 | Days 76–80 | Auth API: JWT + file upload + background tasks |
| 17 | Days 81–86 | Full API project: WebSocket + Docker + CI |
