# Python Flask Service Template

## How to create a new service

1. Copy this folder to a new directory named after your service.
2. Replace every occurrence of SERVICE_NAME with your service name.
3. Run: find . -type f | xargs grep -l SERVICE_NAME
   to confirm all replacements.
4. Build the Docker image and test locally.
5. Create a Helm values file for your environment.
6. Commit to a new Git repository.
7. Create an Argo CD Application pointing to your Helm chart.

## Platform defaults enforced by this template

- Runs as non-root user (UID 1000)
- Exposes /health for readiness and liveness probes
- Declares CPU and memory requests and limits
- Uses a dedicated ServiceAccount
- Exposes /metrics for Prometheus scraping
- Includes a ServiceMonitor for automatic discovery
- Includes a NetworkPolicy template
