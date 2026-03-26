# Kubernetes Sample Manifests

This folder contains simple sample manifests for the DevOps Lab app.

They are designed to match the learning flow in the main README:

- `deployment.yaml` for the Flask web app
- `service.yaml` for public access
- `redis.yaml` for the Redis backing service and deployment

## Before you apply these files

Update the image value in `deployment.yaml` to your real Artifact Registry image, for example:

```yaml
image: us-central1-docker.pkg.dev/your-project-id/my-docker-repo/python-web-app:v1
```

## Deploy the sample app

```bash
kubectl apply -f k8s/
```

## Check the rollout

```bash
kubectl get pods
kubectl get svc
```

## Clean up

```bash
kubectl delete -f k8s/
```

## Why this folder helps

Having the Kubernetes files in their own folder makes the repo easier to hand over because learners can see the application code and the infrastructure manifests as separate parts of the same lab.