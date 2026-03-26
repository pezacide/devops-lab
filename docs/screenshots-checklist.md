# Screenshot Checklist

This repo is already strong on written steps. The next polish step is to add a small set of real screenshots from your own environment.

These should be **real screenshots from Cloud Shell, Google Cloud, Docker, and Kubernetes**, not mockups.

## Suggested screenshot set

### 01-cloud-shell-open.png
Show:
- Google Cloud Console open
- Cloud Shell active
- editor visible if possible

### 02-local-docker-compose.png
Show:
- `docker compose up -d` running successfully
- containers visible if you want extra context

### 03-local-app-preview.png
Show:
- the local app in browser preview
- the visitor counter working

### 04-artifact-registry-image.png
Show:
- the pushed container image in Artifact Registry
- repository name visible

### 05-gke-workloads.png
Show:
- GKE workloads or pods after deployment
- at least one successful running pod

### 06-loadbalancer-service.png
Show:
- `kubectl get service web-service`
- external IP or pending status

## Where to store them

Create a folder called `screenshots/` and save them with the filenames above.

## Good screenshot habits

- crop out unrelated browser tabs
- hide sensitive project or billing info if needed
- keep the terminal text readable
- use the same naming pattern so links are easy to maintain

## Optional README section to add later

Once screenshots exist, add a short section to the README like this:

```md
## Visual walkthrough

![Cloud Shell setup](screenshots/01-cloud-shell-open.png)
![Docker Compose running locally](screenshots/02-local-docker-compose.png)
![Application preview](screenshots/03-local-app-preview.png)
```

That alone will make the repo feel much more handover-ready.