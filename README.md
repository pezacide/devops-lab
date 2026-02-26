# 🚀 Zero-to-DevOps: The Complete Beginner's Guide

Welcome to the Cloud! This guide will take you from a blank screen to a live, scalable web application running on **Google Kubernetes Engine (GKE)**.

## 📁 Project Structure

Arrange your files in a folder named `devops-lab` exactly like this:

```text
/devops-lab
├── app.py             # The Python logic
├── Dockerfile         # The container blueprint
├── compose.yaml       # Local multi-container setup
├── deployment.yaml    # Kubernetes Web App config
├── service.yaml       # Kubernetes Network config
└── redis.yaml         # Kubernetes Database config

```

---

## 🛠 Phase 1: Local Development

**Goal:** Build and test your app on your own machine.

### 1. The Code (`app.py`)

```python
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='db', port=6379)

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
    except:
        count = "Error connecting to Redis"
    return f"<h1>DevOps Lab</h1><p>Visitor count: {count}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

### 2. The Container (`Dockerfile`)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install redis flask
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

```

### 3. The Orchestrator (`compose.yaml`)

```yaml
services:
  web-app:
    build: .
    ports: ["5000:5000"]
    depends_on: [db]
  db:
    image: "redis:alpine"

```

**Terminal Commands:**

```bash
docker compose up -d           # Start local environment
# Open Web Preview on port 5000 to see it working!

```

---

## ☁️ Phase 2: Google Cloud Setup

**Goal:** Prepare the cloud to receive your work.

1. **Set Project:** `gcloud config set project kubernetes-micro-services`
2. **Enable APIs:**
```bash
gcloud services enable artifactregistry.googleapis.com container.googleapis.com

```


3. **Create Registry:**
```bash
gcloud artifacts repositories create my-docker-repo \
    --repository-format=docker --location=us-central1

```


4. **Push Image:**
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
docker tag my-app:v1 us-central1-docker.pkg.dev/kubernetes-micro-services/my-docker-repo/python-web-app:v1
docker push us-central1-docker.pkg.dev/kubernetes-micro-services/my-docker-repo/python-web-app:v1

```



---

## ☸️ Phase 3: Kubernetes Deployment

**Goal:** Run 3 copies of your app with a public IP.

### 1. Create Cluster

```bash
gcloud container clusters create-auto my-first-cluster --location=us-central1

```

### 2. Apply Manifests

Create `deployment.yaml`, `service.yaml`, and `redis.yaml` (copy the code from our previous chat). Then run:

```bash
kubectl apply -f .

```

### 3. Get Your URL

```bash
kubectl get service web-service --watch

```

Wait for the **EXTERNAL-IP** to appear. Copy and paste it into your browser!

---

## 🔍 Troubleshooting (The "Help!" Section)

| Error | Meaning | Solution |
| --- | --- | --- |
| **ImagePullBackOff** | K8s can't find the image. | Check Project ID in `deployment.yaml`. |
| **CrashLoopBackOff** | App crashed on start. | Run `kubectl logs [POD_NAME]` to see errors. |
| **Pending IP** | Google is building the IP. | Wait 60-90 seconds. |

---

## 🛑 Cleanup

**CRITICAL:** Run this when finished to avoid charges:

```bash
gcloud container clusters delete my-first-cluster --location=us-central1

```
Step,Command
Local Start,docker compose up -d
Local Stop,docker compose down
Auth Google,gcloud auth configure-docker us-central1-docker.pkg.dev
Build & Tag,docker build -t my-app . && docker tag my-app [REMOTE_URL]
Push,docker push [REMOTE_URL]
Deploy K8s,kubectl apply -f .
Check App,kubectl get pods
Check URL,kubectl get svc web-service
Cleanup,gcloud container clusters delete my-first-cluster --location=us-central1
---

**Would you like me to help you create a specific "Quick Start" cheat sheet that lists only the commands and no explanations?**
