# opsboy

A unified operations CLI for AI operators. Manage tasks, log events, track metrics, and run health checks - all from one tool.

Built for people who run AI agents in production.

## Features

- **Health Checks**: Plugin-based health checks for services (HTTP, process, disk, memory, custom scripts)
- **Task Management**: Lightweight task queue with status, priority, tags, notes
- **Event Logging**: Structured event log with JSON payloads and tags
- **Metrics Tracking**: Track named counters and gauges over time
- **Runbook**: Markdown-based runbook for declaring how to fix things
- **Zero Dependencies**: Python standard library + SQLite only

## Installation

```bash
git clone https://github.com/nilsyai/opsboy.git
cd opsboy
chmod +x opsboy
./opsboy --help
```

## Quick Start

```bash
# Run all health checks
opsboy check run

# Add a task
opsboy task add "Deploy v2.1" -p high -t deployment

# Log an event
opsboy log --tag deploy "Deployed version 2.1 to production"

# Track a metric
opsboy metric inc deploys

# View runbook
opsboy runbook show my-service
```

## Health Check Plugins

Checks live in `checks/` directory. Each is a Python file with a `check()` function returning (status, message):
- `"ok"` - healthy
- `"warn"` - degraded
- `"fail"` - down

```python
# checks/my_service.py
def check():
    import requests
    try:
        r = requests.get("https://my-service.internal/health", timeout=3)
        return ("ok", f"status={r.status_code}") if r.status_code == 200 else ("fail", f"status={r.status_code}")
    except Exception as e:
        return ("fail", str(e))
```

## Runbook Format

```markdown
# my-service

## Symptoms
- High latency
- Error rate > 1%

## Diagnosis
1. Check logs: `opsboy log --tag my-service`
2. Check metrics: `opsboy metric get error_rate`

## Fix
./scripts/restart-my-service.sh
```
