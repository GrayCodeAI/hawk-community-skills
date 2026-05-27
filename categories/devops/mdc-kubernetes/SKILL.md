---
name: mdc-kubernetes
description: This guide defines definitive best practices for writing, organizing,
  and securing Kubernetes manifests and Operators, ensuring maintainable, performant,
  and reliable cloud-native deployments.
license: MIT
tags:
- devops
---

# deployment.yaml
spec:
  template:
    spec:
      containers:
      - name: my-app
        image: myregistry/my-app:v1.2.3
        volumeMounts:
        - name: secret-volume
          mountPath: "/etc/secrets"
          readOnly: true
        env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-app-secret
              key: DB_PASSWORD # ✅ Inject specific secret key as env var
      volumes:
      - name: secret-volume
        secret:
          secretName: my-app-secret # ✅ Mount secret as files
```

## Logging and Monitoring

Ensure applications are observable.

### 10. Log to `stdout`/`stderr`

Containers must log to `stdout` and `stderr`. Kubernetes handles log collection, forwarding them to your cluster's logging solution.

❌ **BAD:** Logging to files inside the container.

```dockerfile
# Dockerfile
CMD ["/app/start.sh"] # start.sh writes logs to /var/log/app.log
```

✅ **GOOD:** Standard output logging.

```dockerfile
# Dockerfile
CMD ["/app/start.sh"] # start.sh writes logs to stdout/stderr
```

```yaml
# deployment.yaml
spec:
  template:
    spec:
      containers:
      - name: my-app
        image: myregistry/my-app:v1.2.3
        # ✅ Logs automatically collected from stdout/stderr
```

## Testing and Validation

Automate validation of your manifests.

### 11. Lint and Validate Manifests in CI/CD

Integrate tools like `kube-linter`, `kube-score`, `kube-val`, or OPA Gatekeeper/Kyverno into your CI/CD pipeline to validate manifests against best practices and policies before deployment.

❌ **BAD:** Deploying manifests without automated checks.

```bash
# CI/CD pipeline step
kubectl apply -f manifests/ # ❌ No validation, deploys potentially problematic YAML
```

✅ **GOOD:** Automated validation prevents common errors.

```bash
# CI/CD pipeline step
kube-linter lint manifests/
kube-score score manifests/
# For policy enforcement:
# conftest test -p policies/ manifests/
# ✅ Fails fast if manifests violate rules
kubectl apply -f manifests/
```
