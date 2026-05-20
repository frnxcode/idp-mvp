# Platform Golden Path

## What is the golden path

The approved, platform-supported route from code to production.

Services on the golden path receive:

- Automated image building and scanning
- GitOps-driven deployment via Argo CD
- Prometheus metrics and Grafana dashboards
- Namespace isolation and NetworkPolicy
- Runbook template

## How to onboard

1. Copy templates/python-flask-service
2. Follow the README inside the template
3. Open a pull request to this repository
4. Platform team review is automatic via CODEOWNERS

## Deviation process

Services that cannot follow the golden path
must open a platform exception request.
