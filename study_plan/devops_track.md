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

### Day 87 — Docker Fundamentals (22)

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

### Day 88 — Docker Compose (20)

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

### Day 89 — CI/CD: GitHub Actions (22)

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

### Day 90 — CI/CD: Advanced Pipelines (20)

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

### Day 91 — Environment Management (20)

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

### Day 92 — Monitoring: Logging & Metrics (20)

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

### Day 93 — Monitoring: Alerting & Dashboards (20)

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

### Day 94 — Infrastructure as Code (20)

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

### Day 95 — Cloud Basics (20)

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

### Day 96 — Capstone: Design (20)

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

### Day 97 — Capstone: Core Logic (20)

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

### Day 98 — Capstone: API Layer (20)

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

### Day 99 — Capstone: Deployment (20)

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

### Day 100 — Capstone: Polish & Review (20)

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

---

## Sunday Labs (Phase 6)

| Lab | After | Build |
|-----|-------|-------|
| 18 | Days 87–91 | Docker + CI: containerized app with GitHub Actions |
| 19 | Days 92–95 | Observable service: metrics + logging + cloud deploy |
| 20 | Days 96–100 | Capstone: Tic-Tac-Toe API — design → build → deploy |
