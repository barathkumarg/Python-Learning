# Phase 6 — DevOps &Tic-Tac-Toe Capstone (Days 87–100)

> Track: `devops_track` · Outcome: Docker, CI/CD, monitoring, capstone project

## Day Plan

| Day | Topic | Slug | Exercise direction |
|-----|-------|------|--------------------|
| 87 | Docker fundamentals | `day_87_docker` | Images, containers, volumes |
| 88 | Docker Compose | `day_88_compose` | Multi-service stack |
| 89 | CI/CD: GitHub Actions | `day_89_ci` | Lint + test + build pipeline |
| 90 | CI/CD: advanced pipelines | `day_90_cd` | Deploy, matrix, secrets |
| 91 | Environment management | `day_91_envs` | Dev/staging/prod configs |
| 92 | Monitoring: logging & metrics | `day_92_monitoring` | Prometheus, structured logs |
| 93 | Monitoring: alerting & dashboards | `day_93_alerting` | Grafana, health checks |
| 94 | Infrastructure as Code | `day_94_iac` | Terraform/Ansible basics |
| 95 | Cloud basics | `day_95_cloud` | AWS/GCP fundamentals |
| 96 | Capstone: design | `day_96_capstone_design` | Architecture, API design |
| 97 | Capstone: core logic | `day_97_capstone_core` | Game engine, validation |
| 98 | Capstone: API layer | `day_98_capstone_api` | FastAPI endpoints |
| 99 | Capstone: deployment | `day_99_capstone_deploy` | Docker + CI + monitoring |
| 100 | Capstone: polish & review | `day_100_capstone_review` | Tests, docs, retrospective |

---

## Concept Checklists

### Day 87 — Docker Fundamentals (28)

**Prerequisites:** Day 14 (tooling and environments), Day 82 (containerizing a FastAPI app)
**Real-world use:** every service ships as a container image — reproducible builds, identical dev/prod runtime, and fast rollbacks.
**Production example (code.py):** a build helper that renders a multi-stage, non-root Python `Dockerfile` from a project spec (pinned base image, uv install layer, `HEALTHCHECK`) and shells out to `docker build`/`docker run` with parsed status — no shell-string injection.
**Sources:** [Docker — Official docs](https://docs.docker.com/) · [FastAPI — Docker deployment](https://fastapi.tiangolo.com/deployment/docker/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Docker image | Read-only template |
| 2 | Docker container | Running instance |
| 3 | `Dockerfile` | Build instructions |
| 4 | `FROM` | Base image |
| 5 | `COPY` / `ADD` | Add files |
| 6 | `RUN` | Execute command |
| 7 | `CMD` / `ENTRYPOINT` | Default command |
| 8 | `WORKDIR` | Working directory |
| 9 | `EXPOSE` | Document port |
| 10 | `ENV` | Environment variable |
| 11 | `docker build` | Build image |
| 12 | `docker run` | Start container |
| 13 | `docker ps` / `docker logs` | Monitor |
| 14 | `docker exec` | Execute in running container |
| 15 | Volumes | `-v host:container` |
| 16 | `.dockerignore` | Exclude from build |
| 17 | Multi-stage builds | Smaller final image |
| 18 | Layer caching | Order matters |
| 19 | Non-root user | `USER appuser` |
| 20 | Image tagging | `image:tag` |
| 21 | Anti-pattern: latest tag | Use specific versions |
| 22 | Industrial: Python Dockerfile | Optimized for pip/uv |
| 23 | `ARG` build args | `ARG PY_VERSION=3.12` |
| 24 | `HEALTHCHECK` instruction | Container-level liveness probe |
| 25 | Registry push/pull | `docker pull`, `docker push` |
| 26 | Container lifecycle | `docker stop` / `rm` / `rmi` |
| 27 | `docker inspect` | Config + state as JSON |
| 28 | Restart policies | `--restart unless-stopped` |

### Day 88 — Docker Compose (25)

**Prerequisites:** Day 87 (images, containers, volumes), Day 83 (settings management)
**Real-world use:** local and CI stacks run app + database + cache together with one command and reproducible wiring.
**Production example (code.py):** a compose-stack orchestrator that generates a `compose.yaml` for app+db+redis with healthcheck-gated `depends_on`, brings the stack up, and polls each service's health before returning ready.
**Sources:** [Docker Compose docs](https://docs.docker.com/compose/) · [Docker — Official docs](https://docs.docker.com/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `compose.yaml` | Service definitions |
| 2 | `services` | Named containers |
| 3 | `build` | Build from Dockerfile |
| 4 | `image` | Use existing image |
| 5 | `ports` | Port mapping |
| 6 | `volumes` | Data persistence |
| 7 | `environment` | Env vars |
| 8 | `depends_on` | Service ordering |
| 9 | `networks` | Custom networks |
| 10 | `docker compose up` | Start all |
| 11 | `docker compose down` | Stop and remove |
| 12 | `docker compose logs` | View logs |
| 13 | Health checks | `healthcheck` section |
| 14 | Named volumes | Persistent data |
| 15 | `.env` file | Variable substitution |
| 16 | Profiles | `profiles: ["debug"]` |
| 17 | Override files | `compose.override.yaml` |
| 18 | Anti-pattern: no health check | Services may not be ready |
| 19 | Industrial: app + db + redis | Three-service stack |
| 20 | Industrial: dev environment | Hot-reload with volumes |
| 21 | `command` / `entrypoint` override | Per-service startup |
| 22 | `restart` policy | `restart: unless-stopped` |
| 23 | `depends_on` condition | `condition: service_healthy` |
| 24 | `docker compose exec` / `build` | Run in / rebuild service |
| 25 | Resource limits | `deploy.resources`, `mem_limit` |

### Day 89 — CI/CD: GitHub Actions (27)

**Prerequisites:** Day 61 (ruff and pre-commit), Day 60 (coverage), Day 87 (Docker images)
**Real-world use:** every push is linted, type-checked, and tested automatically so broken code never reaches main.
**Production example (code.py):** a workflow generator + validator that emits a lint→typecheck→test→build matrix `ci.yml` and parses `pytest`/`ruff` JSON output into a single pass/fail gate summary.
**Sources:** [GitHub Actions docs](https://docs.github.com/actions) · [GitHub Actions — Quickstart](https://docs.github.com/actions/quickstart)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Workflow file | `.github/workflows/ci.yml` |
| 2 | `on` triggers | `push`, `pull_request` |
| 3 | `jobs` | Named job definitions |
| 4 | `runs-on` | `ubuntu-latest` |
| 5 | `steps` | Sequential actions |
| 6 | `uses` | Reusable actions |
| 7 | `run` | Shell commands |
| 8 | `actions/checkout` | Clone repo |
| 9 | `actions/setup-python` | Install Python |
| 10 | Cache dependencies | `actions/cache` |
| 11 | Environment variables | `env:` section |
| 12 | Secrets | `${{ secrets.TOKEN }}` |
| 13 | Matrix strategy | Multiple Python versions |
| 14 | Artifacts | Upload test results |
| 15 | Job dependencies | `needs: [build]` |
| 16 | Conditional steps | `if: success()` |
| 17 | Status badges | `![CI](url)` |
| 18 | Lint step | `ruff check .` |
| 19 | Test step | `pytest --cov` |
| 20 | Type check step | `mypy .` |
| 21 | Anti-pattern: no CI | Always automate |
| 22 | Industrial: full pipeline | Lint → test → build → deploy |
| 23 | `workflow_dispatch` | Manual trigger |
| 24 | `schedule` (cron) | Timed runs |
| 25 | `concurrency` groups | Cancel in-progress runs |
| 26 | `permissions` | Scope `GITHUB_TOKEN` |
| 27 | Step/job outputs | `GITHUB_OUTPUT`, `needs.x.outputs` |

### Day 90 — CI/CD: Advanced Pipelines (24)

**Prerequisites:** Day 89 (CI workflows), Day 87 (image build and tagging)
**Real-world use:** promoting a build from staging to production safely — tagged releases, image push, approvals, and a rollback path.
**Production example (code.py):** a release-orchestration helper that computes the next semver tag from git history, builds and pushes a multi-arch image to GHCR, and writes a deployment record with a rollback reference.
**Sources:** [GitHub Actions docs](https://docs.github.com/actions) · [Docker — Official docs](https://docs.docker.com/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Deployment workflows | Push to prod |
| 2 | Environment protection | Manual approval |
| 3 | Reusable workflows | `workflow_call` |
| 4 | Composite actions | Custom actions |
| 5 | Docker build in CI | `docker/build-push-action` |
| 6 | Registry push | Docker Hub, GHCR |
| 7 | Semantic versioning | Tag-based releases |
| 8 | Release automation | `softprops/action-gh-release` |
| 9 | Branch strategies | main, develop, feature |
| 10 | PR checks | Required status checks |
| 11 | Code coverage gate | Fail if below threshold |
| 12 | Security scanning | `trivy`, `bandit` |
| 13 | Dependency updates | `dependabot` |
| 14 | Rollback strategy | Revert or redeploy |
| 15 | Blue-green deployment | Zero downtime |
| 16 | Canary deployment | Gradual rollout |
| 17 | Anti-pattern: manual deploy | Automate everything |
| 18 | Anti-pattern: no rollback | Always have escape |
| 19 | Industrial: staging → prod | Promotion pipeline |
| 20 | Industrial: GitOps | Infrastructure as code |
| 21 | OIDC cloud auth | Keyless credentials |
| 22 | Multi-arch builds | `buildx`, `platforms` |
| 23 | SBOM + attestation | Supply-chain provenance |
| 24 | Deployment environments | Approvals + protection rules |

### Day 91 — Environment Management (24)

**Prerequisites:** Day 83 (settings management), Day 01 (types and validation)
**Real-world use:** twelve-factor config — the same image runs in dev/staging/prod driven only by environment, with secrets never in code.
**Production example (code.py):** a `pydantic-settings` config loader with per-environment layering (defaults → `.env` → env vars), `SecretStr` for credentials, and fail-fast validation that reports every missing/invalid key at startup.
**Sources:** [Pydantic Settings docs](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) · [FastAPI — Settings and environment variables](https://fastapi.tiangolo.com/advanced/settings/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | `.env` files | `KEY=value` |
| 2 | `python-dotenv` | `load_dotenv()` |
| 3 | `os.environ` | Access env vars |
| 4 | `pydantic-settings` | `BaseSettings` class |
| 5 | Settings hierarchy | .env → env vars → defaults |
| 6 | Dev vs staging vs prod | Config per environment |
| 7 | Secrets management | Never in code |
| 8 | `.env.example` | Template for team |
| 9 | Docker env injection | `--env-file`, `environment:` |
| 10 | CI secrets | Repository secrets |
| 11 | Vault overview | HashiCorp Vault concept |
| 12 | AWS Secrets Manager | Cloud secrets concept |
| 13 | Feature flags | Enable/disable features |
| 14 | Config validation | Fail fast on missing |
| 15 | Immutable config | Frozen dataclass |
| 16 | Anti-pattern: hardcoded config | Use env vars |
| 17 | Anti-pattern: secrets in git | Use .gitignore |
| 18 | Industrial: 12-factor app | Config in environment |
| 19 | Industrial: multi-env deploy | Per-env settings |
| 20 | Testing config | Override in tests |
| 21 | `SecretStr` | Masked secret fields |
| 22 | Env prefix / nested settings | `SettingsConfigDict(env_prefix=...)` |
| 23 | Secret rotation | Rotate without redeploy |
| 24 | Encrypted secrets | SOPS, sealed secrets |

### Day 92 — Monitoring: Logging & Metrics (25)

**Prerequisites:** Day 49 (logging in concurrent systems), Day 85 (health and readiness)
**Real-world use:** you cannot fix what you cannot see — structured logs and Prometheus metrics are the baseline for any on-call service.
**Production example (code.py):** a metrics + logging middleware that exposes a `/metrics` endpoint with request Counter/Histogram/Gauge by route and status code, and emits JSON structured logs with a bound request-id.
**Sources:** [Prometheus — Python client](https://prometheus.io/docs/guides/python/) · [structlog](https://www.structlog.org/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Structured logging (recap) | JSON format |
| 2 | Log aggregation | Centralized logs |
| 3 | ELK stack overview | Elasticsearch, Logstash, Kibana |
| 4 | Prometheus overview | Metrics collection |
| 5 | `prometheus_client` | `Counter`, `Histogram`, `Gauge` |
| 6 | Metrics endpoint | `/metrics` |
| 7 | Counter | Total count of events |
| 8 | Histogram | Duration distributions |
| 9 | Gauge | Current value |
| 10 | Labels | Dimension metadata |
| 11 | Request duration metric | Middleware histogram |
| 12 | Error rate metric | Counter by status code |
| 13 | Custom business metrics | Domain-specific counts |
| 14 | Health check endpoint | `/health`, `/ready` |
| 15 | Liveness vs readiness | Different health probes |
| 16 | Anti-pattern: no metrics | Can't improve unseen |
| 17 | Anti-pattern: high-cardinality labels | Memory explosion |
| 18 | Industrial: RED method | Rate, Errors, Duration |
| 19 | Industrial: USE method | Utilization, Saturation, Errors |
| 20 | Industrial: SLI/SLO | Service level indicators |
| 21 | `Summary` metric | Client-side quantiles |
| 22 | `CollectorRegistry` | Isolated metric registry |
| 23 | `generate_latest` | Exposition format |
| 24 | Pushgateway | Metrics for batch jobs |
| 25 | Multiprocess mode | Gunicorn worker aggregation |

### Day 93 — Monitoring: Alerting & Dashboards (25)

**Prerequisites:** Day 92 (metrics, structured logs), Day 41 (async error handling)
**Real-world use:** alerts on user-impacting symptoms plus distributed traces turn raw telemetry into fast incident resolution.
**Production example (code.py):** an OpenTelemetry tracing setup that starts spans around request handling, propagates W3C `traceparent` context, injects the trace-id into logs, and exports via OTLP — with a burn-rate alert-rule generator.
**Sources:** [OpenTelemetry — Python SDK](https://opentelemetry.io/docs/languages/python/) · [OpenTelemetry — Traces](https://opentelemetry.io/docs/concepts/signals/traces/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Grafana overview | Dashboard tool |
| 2 | Grafana + Prometheus | Data source config |
| 3 | Dashboard design | Key metrics panels |
| 4 | Alert rules | Threshold conditions |
| 5 | Notification channels | Slack, email, PagerDuty |
| 6 | Alert fatigue | Meaningful thresholds |
| 7 | On-call practices | Rotation, escalation |
| 8 | Incident response | Detect → respond → resolve |
| 9 | Post-mortem | Blameless review |
| 10 | Runbooks | Step-by-step recovery |
| 11 | Uptime monitoring | External ping |
| 12 | Error tracking | Sentry integration |
| 13 | Distributed tracing | OpenTelemetry concept |
| 14 | Trace context | Request ID propagation |
| 15 | Log correlation | Trace ID in logs |
| 16 | Anti-pattern: alert on everything | Focus on user impact |
| 17 | Anti-pattern: no runbooks | Panic during incidents |
| 18 | Industrial: golden signals | Latency, traffic, errors, saturation |
| 19 | Industrial: SLO dashboard | Error budget tracking |
| 20 | Industrial: observability stack | Logs + metrics + traces |
| 21 | OTLP exporter | Export spans/metrics |
| 22 | Span attributes + events | Structured span data |
| 23 | Context propagation | W3C `traceparent` header |
| 24 | Alertmanager | Routing + deduplication |
| 25 | Burn-rate alerts | Multi-window SLO alerting |

### Day 94 — Infrastructure as Code (24)

**Prerequisites:** Day 91 (environment and config), Day 87 (containers and images)
**Real-world use:** infrastructure is versioned, reviewed, and reproducible — no snowflake servers, no manual console clicks.
**Production example (code.py):** a Python IaC helper (Pulumi-style over boto3) that declares an S3 bucket + tags idempotently, detects drift against declared state, and prints a plan (create/update/no-op) before applying.
**Sources:** [Boto3 — AWS SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) · [Docker Engine API](https://docs.docker.com/engine/api/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | IaC concept | Define infra in code |
| 2 | Terraform overview | `resource`, `provider` |
| 3 | Terraform workflow | `init` → `plan` → `apply` |
| 4 | State management | `terraform.tfstate` |
| 5 | Variables | `variable "name" {}` |
| 6 | Outputs | `output "ip" { value = ... }` |
| 7 | Modules | Reusable components |
| 8 | Ansible overview | YAML playbooks |
| 9 | Ansible tasks | `apt`, `copy`, `service` |
| 10 | Ansible inventory | Host groups |
| 11 | Pulumi overview | IaC in Python |
| 12 | Immutable infrastructure | Replace, don't patch |
| 13 | Configuration drift | Detect + remediate |
| 14 | State locking | Prevent concurrent changes |
| 15 | Remote state | S3, Terraform Cloud |
| 16 | Anti-pattern: manual changes | Always through IaC |
| 17 | Anti-pattern: no state management | Drift + conflicts |
| 18 | Industrial: Terraform + CI | Auto-apply on merge |
| 19 | Industrial: environment parity | Same IaC, different vars |
| 20 | Industrial: disaster recovery | Recreate from IaC |
| 21 | `validate` / `fmt` | Pre-apply checks |
| 22 | Data sources | Read existing infra |
| 23 | `count` / `for_each` | Resource iteration |
| 24 | Ansible roles + idempotency | Reusable, repeatable tasks |

### Day 95 — Cloud Basics (25)

**Prerequisites:** Day 91 (secrets and config), Day 94 (infrastructure as code)
**Real-world use:** shipping to a cloud means choosing compute, storage, networking, and IAM with least-privilege and cost awareness.
**Production example (code.py):** a boto3 automation that uploads build artifacts to S3 with server-side encryption, uses a paginator to list objects, and applies a least-privilege bucket policy — with waiters for consistency.
**Sources:** [Boto3 — AWS SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) · [Docker — Official docs](https://docs.docker.com/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Cloud service models | IaaS, PaaS, SaaS |
| 2 | AWS overview | EC2, S3, RDS, Lambda |
| 3 | GCP overview | Compute Engine, Cloud Run |
| 4 | Azure overview | App Service, Functions |
| 5 | Compute options | VM, container, serverless |
| 6 | Object storage | S3, GCS, Azure Blob |
| 7 | Managed databases | RDS, Cloud SQL |
| 8 | Container services | ECS, Cloud Run, AKS |
| 9 | Serverless functions | Lambda, Cloud Functions |
| 10 | CDN | CloudFront, Cloud CDN |
| 11 | DNS | Route 53, Cloud DNS |
| 12 | Load balancing | ALB, Cloud LB |
| 13 | IAM | Users, roles, policies |
| 14 | VPC / networking | Subnets, security groups |
| 15 | Cost management | Budgets, right-sizing |
| 16 | Anti-pattern: over-provision | Start small, scale up |
| 17 | Anti-pattern: no IAM | Least privilege |
| 18 | Industrial: three-tier | Web + app + DB |
| 19 | Industrial: microservices | Container orchestration |
| 20 | Industrial: cost optimization | Reserved, spot instances |
| 21 | Regions and AZs | Fault isolation |
| 22 | Auto-scaling | Scale on demand |
| 23 | Managed queues | SQS, Pub/Sub |
| 24 | Cloud monitoring | CloudWatch metrics/logs |
| 25 | boto3 client patterns | Paginators, waiters |

### Day 96 — Capstone: Design (23)

**Prerequisites:** Day 64 (repository and DI), Day 71 (FastAPI app basics)
**Real-world use:** a written design (requirements, API contract, data model, ADRs) prevents rework and aligns the team before code.
**Production example (code.py):** a design-artifact generator that emits the capstone's OpenAPI-first API contract stub, a data-model dataclass module, and an ADR template file from a project spec.
**Sources:** [Own repo modules (`src/`)](../src) · [FastAPI — Tutorial](https://fastapi.tiangolo.com/tutorial/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Requirements gathering | Functional + non-functional |
| 2 | API design | RESTful endpoints |
| 3 | Data model | Database schema |
| 4 | Architecture diagram | Components + connections |
| 5 | Technology choices | Justify stack |
| 6 | User stories | "As a user, I want..." |
| 7 | Project structure | Directory layout |
| 8 | Interface design | Protocol/ABC definitions |
| 9 | Error strategy | Domain exceptions |
| 10 | Auth strategy | JWT or API key |
| 11 | Testing strategy | Unit + integration |
| 12 | Deployment strategy | Docker + CI |
| 13 | Monitoring strategy | Metrics + logging |
| 14 | Documentation plan | README, API docs |
| 15 | Sprint planning | Break into tasks |
| 16 | Anti-pattern: no design | Start coding blindly |
| 17 | Anti-pattern: over-design | Analysis paralysis |
| 18 | Industrial: design doc | Written proposal |
| 19 | Industrial: tech review | Peer feedback |
| 20 | Industrial: ADR | Architecture Decision Records |
| 21 | Threat model | STRIDE, trust boundaries |
| 22 | OpenAPI-first contract | Design the API schema first |
| 23 | Idempotency + concurrency | Design for retries/races |

### Day 97 — Capstone: Core Logic (23)

**Prerequisites:** Day 15 (classes and object state), Day 20 (dataclasses), Day 59 (pytest fixtures)
**Real-world use:** the domain core is pure, fully typed, and exhaustively tested — no I/O, so it is trivially testable and reusable.
**Production example (code.py):** the Tic-Tac-Toe engine — immutable board state, validated moves, win/draw detection, and a minimax (alpha-beta) AI strategy, with property-based tests for invariants.
**Sources:** [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) · [Own repo modules (`src/`)](../src)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Game board model | 2D array or flat |
| 2 | Player model | Enum or dataclass |
| 3 | Move validation | Check bounds + empty |
| 4 | Win detection | Rows, cols, diagonals |
| 5 | Draw detection | Board full, no winner |
| 6 | Game state | `Enum`: playing, won, draw |
| 7 | Turn management | Alternate players |
| 8 | Move history | List of moves |
| 9 | Undo move | Pop from history |
| 10 | AI opponent (basic) | Random or minimax |
| 11 | Board display | String representation |
| 12 | Input parsing | Coordinate validation |
| 13 | Type annotations | Full coverage |
| 14 | Unit tests | Test all game logic |
| 15 | Edge cases | Full board, immediate win |
| 16 | Anti-pattern: god class | Split game + board |
| 17 | Anti-pattern: no validation | Silently accept bad moves |
| 18 | Industrial: domain model | Pure logic, no I/O |
| 19 | Industrial: strategy pattern | Pluggable AI |
| 20 | Industrial: immutable state | New state per move |
| 21 | Minimax + alpha-beta | Optimal AI, pruned search |
| 22 | Property-based tests | Hypothesis invariants |
| 23 | State serialization | Save/rehydrate game state |

### Day 98 — Capstone: API Layer (24)

**Prerequisites:** Day 71–74 (FastAPI, models, dependencies, error handling), Day 97 (game engine)
**Real-world use:** the API wraps the domain core with validation, RFC 7807 errors, and OpenAPI docs behind a clean service layer.
**Production example (code.py):** the FastAPI game API — create/move/get/list endpoints over the engine via a service dependency, idempotency keys, ETag optimistic concurrency (409), and `problem+json` error mapping.
**Sources:** [FastAPI — Official docs](https://fastapi.tiangolo.com/) · [FastAPI — Testing](https://fastapi.tiangolo.com/tutorial/testing/)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | FastAPI app setup | Router + models |
| 2 | Create game endpoint | `POST /games` |
| 3 | Make move endpoint | `POST /games/{id}/moves` |
| 4 | Get game state | `GET /games/{id}` |
| 5 | List games | `GET /games` |
| 6 | Pydantic models | Request + response |
| 7 | Error responses | 400, 404, 409 |
| 8 | Game storage | In-memory or DB |
| 9 | Dependency injection | Game service |
| 10 | WebSocket for live | Real-time game updates |
| 11 | Auth (optional) | Player identification |
| 12 | OpenAPI docs | Full documentation |
| 13 | Integration tests | TestClient suite |
| 14 | Middleware | Logging, CORS |
| 15 | Health check | `/health` endpoint |
| 16 | Anti-pattern: logic in routes | Use service layer |
| 17 | Anti-pattern: no error handling | Map domain errors |
| 18 | Industrial: API design | RESTful conventions |
| 19 | Industrial: versioning | `/api/v1/` prefix |
| 20 | Industrial: rate limiting | Per-player limits |
| 21 | RFC 7807 errors | `application/problem+json` |
| 22 | Idempotency keys | Safe retries on POST |
| 23 | ETag / optimistic concurrency | `409 Conflict` on stale write |
| 24 | Lifespan events | Startup/shutdown resources |

### Day 99 — Capstone: Deployment (24)

**Prerequisites:** Day 87–92 (Docker, Compose, CI, config, metrics), Day 98 (API layer)
**Real-world use:** the capstone ships the way real services do — containerized, CI-gated, observable, and rollback-ready.
**Production example (code.py):** a deploy-slice script that builds and scans the image, runs a smoke test against a temporary container, tags/pushes on success, and verifies `/health` post-deploy with an automatic rollback on failure.
**Sources:** [FastAPI — Docker deployment](https://fastapi.tiangolo.com/deployment/docker/) · [GitHub Actions docs](https://docs.github.com/actions)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Dockerfile | Multi-stage, non-root |
| 2 | Docker Compose | App + DB (optional) |
| 3 | GitHub Actions CI | Lint + test + build |
| 4 | Docker image push | GHCR or Docker Hub |
| 5 | Environment config | `.env` + pydantic-settings |
| 6 | Health check | Docker + app level |
| 7 | Logging config | JSON structured logs |
| 8 | Metrics (optional) | Prometheus counters |
| 9 | Graceful shutdown | Signal handling |
| 10 | Documentation | README with setup steps |
| 11 | API docs | OpenAPI auto-generated |
| 12 | Security review | Input validation, auth |
| 13 | Performance check | Load test basics |
| 14 | Monitoring dashboard | Grafana (optional) |
| 15 | Runbook | Troubleshooting guide |
| 16 | Anti-pattern: manual deploy | CI/CD only |
| 17 | Anti-pattern: no health check | Silent failures |
| 18 | Industrial: production checklist | Pre-launch review |
| 19 | Industrial: rollback plan | How to revert |
| 20 | Industrial: post-deploy verify | Smoke tests |
| 21 | Image vulnerability scan | `trivy image` in CI |
| 22 | Migrations on deploy | Run before cutover |
| 23 | Zero-downtime rollout | Rolling / blue-green |
| 24 | Resource limits | CPU/memory requests + limits |

### Day 100 — Capstone: Polish & Review (23)

**Prerequisites:** Day 60 (coverage), Day 62 (security scanning), Day 99 (deployment)
**Real-world use:** the last mile — coverage, type-strictness, security audit, docs, and a portfolio-ready README — is what makes work presentable and maintainable.
**Production example (code.py):** a release-readiness checker that runs `ruff`/`mypy --strict`/`pytest --cov`/`pip-audit`, verifies README badges and required docs exist, and prints a go/no-go checklist with per-gate status.
**Sources:** [Own repo (`src/`, `docs/`)](../src) · [NeetCode — Roadmap](https://neetcode.io/roadmap)

| # | Concept | Key syntax |
|---|---------|-----------|
| 1 | Code review checklist | Style, logic, tests |
| 2 | Test coverage report | `pytest --cov` |
| 3 | Type checking | `mypy --strict` |
| 4 | Linting | `ruff check .` |
| 5 | Documentation review | README, API docs |
| 6 | Security audit | Input validation, secrets |
| 7 | Performance review | Profiling results |
| 8 | Error handling review | All paths covered |
| 9 | Logging review | Structured, leveled |
| 10 | CI/CD verification | Pipeline passes |
| 11 | Docker verification | Build + run clean |
| 12 | Retrospective | What worked, what didn't |
| 13 | Lessons learned | Key takeaways |
| 14 | Portfolio entry | README + screenshots |
| 15 | Future improvements | Backlog items |
| 16 | Knowledge gaps | Topics to revisit |
| 17 | Anti-pattern: ship without review | Always review |
| 18 | Industrial: demo preparation | Present your work |
| 19 | Industrial: handoff docs | For future maintainers |
| 20 | Celebration 🎉 | 100 days done! |
| 21 | Dependency audit | `pip-audit` for CVEs |
| 22 | README badges + diagram | CI, coverage, architecture |
| 23 | CHANGELOG / release notes | Versioned change history |

---

## Sunday Labs (Phase 6)

| Lab | After | Build |
|-----|-------|-------|
| 18 | Days 87–91 | Docker + CI: containerized app with GitHub Actions |
| 19 | Days 92–95 | Observable service: metrics + logging + cloud deploy |
| 20 | Days 96–100 | Capstone: Tic-Tac-Toe API — design → build → deploy |
