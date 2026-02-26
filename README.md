![Status](https://img.shields.io/badge/Status-Maintained-green)
![K8s Version](https://img.shields.io/badge/Kubernetes-GKE%20Autopilot-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://github.com/pezacide/devops-lab/actions/workflows/status.yaml/badge.svg)

## 🏁 Phase 0: Getting Started with Cloud Shell

Before writing code, you need a workspace. Google Cloud Shell provides a free, pre-configured Linux machine in your browser.

1. **Open the Console:** Go to [console.cloud.google.com](https://console.cloud.google.com).
2. **Select Project:** Click the dropdown at the top left and select `kubernetes-micro-services`.
3. **Activate Cloud Shell:** Click the **>_** icon in the top right header.
4. **Open Editor:** Once the terminal opens, click the **Open Editor** button (pencil icon) to see your files.
5. **Create Folder:** In the terminal, type:
```bash
mkdir devops-lab && cd devops-lab

```



---

## 📦 Phase 1: Creating the App (Docker)

**Goal:** Build a "container" that holds your code and its tools.

### Step 1: Create the Python Code

1. In the Editor, right-click the `devops-lab` folder and create a new file named **`app.py`**.
2. Paste this code:

```python
from flask import Flask
import redis

app = Flask(__name__)
# Connects to a database named 'db'
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

### Step 2: Create the Dockerfile

1. Create a new file named **`Dockerfile`** (no file extension).
2. Paste this:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install redis flask
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

```

### Step 3: Build & Test Locally

In the terminal, run:

```bash
docker build -t my-app:v1 .

```

---

## 🎼 Phase 2: Connecting the Database (Docker Compose)

**Goal:** Make the app and database work together on your machine.

### Step 1: Create the Compose File

1. Create a new file named **`compose.yaml`**.
2. Paste this:

```yaml
services:
  web-app:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: "redis:alpine"

```

### Step 2: Run and Preview

1. In the terminal, run: `docker compose up -d`
2. Click the **Web Preview** button (top right of Cloud Shell) and select **Preview on port 8080**.
* *Note: Since we mapped 5000:5000, you might need to change the preview port to 5000.*



---

## 🚀 Phase 3: Moving to the Cloud (Artifact Registry)

**Goal:** Upload your image so Google’s servers can find it.

### Step 1: Prepare the Registry

Run these three commands one by one:

```bash
# 1. Enable the API
gcloud services enable artifactregistry.googleapis.com

# 2. Create the Storage Repository
gcloud artifacts repositories create my-docker-repo \
    --repository-format=docker \
    --location=us-central1

# 3. Give Docker permission to upload
gcloud auth configure-docker us-central1-docker.pkg.dev

```

### Step 2: Tag and Upload

```bash
# Replace [PROJECT_ID] with 'kubernetes-micro-services'
docker tag my-app:v1 us-central1-docker.pkg.dev/kubernetes-micro-services/my-docker-repo/python-web-app:v1

# Push the image up to Google
docker push us-central1-docker.pkg.dev/kubernetes-micro-services/my-docker-repo/python-web-app:v1

```

---

## ☸️ Phase 4: Scaling with Kubernetes (GKE)

**Goal:** Run the app on multiple servers with a public URL.

### Step 1: Launch the Cluster

```bash
# Enable Kubernetes API
gcloud services enable container.googleapis.com

# Create the cluster (Wait 5-8 mins)
gcloud container clusters create-auto my-first-cluster --location=us-central1

```

### Step 2: Create Manifests

Create three files in the editor:

**`deployment.yaml`** (The Logic)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-web-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: python-web
        image: us-central1-docker.pkg.dev/kubernetes-micro-services/my-docker-repo/python-web-app:v1
        ports:
        - containerPort: 5000

```

**`service.yaml`** (The Entryway)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer

```

**`redis.yaml`** (The Database)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  selector:
    app: redis
  ports:
    - protocol: TCP
      port: 6379
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-deployment
spec:
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:alpine

```

### Step 3: Deploy and Go Live

Run:

```bash
kubectl apply -f .

```

Wait 1 minute, then run:

```bash
kubectl get service web-service

```

Copy the **EXTERNAL-IP** and paste it into a new browser tab. **Success!**

---

## 🛑 Phase 5: Cleanup (Don't skip!)

To avoid being charged, delete the cluster when finished:

```bash
gcloud container clusters delete my-first-cluster --location=us-central1

```
To set this up in GitHub properly, you aren't just uploading files; you are creating a "Repository." This is the home for your code where GitHub will automatically turn your `README.md` into the beautiful manual we just wrote.

Here is the step-by-step for a complete beginner:

### 1. Create the Repository on GitHub

1. Log in to [GitHub](https://github.com).
2. Click the **+** icon in the top right and select **New repository**.
3. **Repository name:** `devops-lab`.
4. **Public/Private:** Choose Public (if you want to share the link easily) or Private.
5. **Check the box** that says **Add a README file**.
6. Click **Create repository**.

### 2. Add Your Files (The "No-Code" Way)

If your colleague isn't ready for the `git` command line yet, they can use the browser:

1. Inside your new repository, click **Add file** > **Create new file**.
2. Name the file (e.g., `app.py`) and paste the code.
3. Scroll down and click **Commit changes**.
4. Repeat this for all 6 files (`Dockerfile`, `compose.yaml`, `deployment.yaml`, `service.yaml`, `redis.yaml`).

### 3. Polish the Manual (The README)

1. Click on the **README.md** file in your list.
2. Click the **pencil icon** (Edit) in the top right.
3. **Delete everything** currently in there and paste the **"Zero-to-DevOps Master Guide"** I gave you in the previous response.
4. Click **Commit changes**.

---


## ⚡ Quick Start Command Cheat Sheet

| Step | Command |
| --- | --- |
| **Local Start** | `docker compose up -d` |
| **Local Stop** | `docker compose down` |
| **Auth Google** | `gcloud auth configure-docker us-central1-docker.pkg.dev` |
| **Build & Tag** | `docker build -t my-app . && docker tag my-app [REMOTE_URL]` |
| **Push** | `docker push [REMOTE_URL]` |
| **Deploy K8s** | `kubectl apply -f .` |
| **Check App** | `kubectl get pods` |
| **Check URL** | `kubectl get svc web-service` |
| **Cleanup** | `gcloud container clusters delete my-first-cluster --location=us-central1` |

---

