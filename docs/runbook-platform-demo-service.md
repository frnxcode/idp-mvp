# Runbook: platform-demo-service

## Health check
curl http://localhost:8081/health

## Check pods
kubectl get pods -n demo-dev

## Check logs
kubectl logs -n demo-dev deployment/platform-demo-service --tail=50

## Check metrics
kubectl port-forward svc/platform-demo-service -n demo-dev 8080:80
curl http://localhost:8080/metrics

## Check recent events
kubectl get events -n demo-dev --sort-by=.metadata.creationTimestamp

## Restart the deployment
kubectl rollout restart deployment/platform-demo-service -n demo-dev

## Common issue: ImagePullBackOff
# If running locally with kind:
kind load docker-image <image>:<tag> --name idp-mvp

## Common issue: CrashLoopBackOff
kubectl logs -n demo-dev deployment/platform-demo-service --previous
