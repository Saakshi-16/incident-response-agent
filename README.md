# Incident Response Agent

An agentic AI system that investigates production incidents across logs,
metrics, databases and deployments, identifies the likely root cause with
supporting evidence, and applies fixes only after human approval.

## Problem

When a production incident happens (high latency, API failures, database
connection exhaustion), engineers manually jump between logs, metrics,
deployment history and runbooks to find the root cause. This is slow and
increases Mean Time To Resolve (MTTR).

## Solution

A LangGraph-based multi-agent system:

1. **Receives an alert** from Prometheus Alertmanager
2. **Investigates in parallel** with specialist agents: Logs, Metrics,
   Database, Deployments
3. **Retrieves knowledge** from runbooks and past incidents (RAG)
4. **Performs root-cause analysis** backed by evidence
5. **Recommends a fix** and waits for **human approval**
6. **Executes approved actions** from a safe allowlist and verifies the result

## Status

🚧 Phase 1: Demo microservices

## Roadmap

- [x] Phase 0: Dev environment and project setup
- [ ] Phase 1: Demo microservices (FastAPI + PostgreSQL + Docker Compose)
- [ ] Phase 2: Observability (OpenTelemetry, Prometheus, Loki, Grafana)
- [ ] Phase 3: Failure injection and alerting
- [ ] Phase 4: Investigation tools
- [ ] Phase 5: AI agents (single agent → multi-agent → RAG)
- [ ] Phase 6: Root-cause report and human approval
- [ ] Phase 7: Safe remediation (Action Agent)
- [ ] Phase 8: Evaluation
- [ ] Phase 9: AWS deployment

## Tech stack

Python · FastAPI · PostgreSQL · Docker · OpenTelemetry · Prometheus ·
Loki · Grafana · LangGraph · Claude API

## Project structure

| Folder | Purpose |
|---|---|
| `services/` | Demo microservices that get monitored |
| `infra/` | Docker Compose and observability configs |
| `chaos/` | Scripts that inject failures |
| `agent/` | AI agents and investigation tools |
| `runbooks/` | Knowledge base for RAG |
| `evals/` | Accuracy evaluation |
| `tests/` | Automated tests |
| `docs/` | Architecture and design decisions |