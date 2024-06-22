# FastAPI Demo App

## deploy

### local
```
$ docker compose up
```
Open http://localhost:8000/docs URL in browser.

### gcp
```
$ docker build -t gcr.io/{PROJECT_ID}/demo-app:latest --platform linux/amd64 -f Dockerfile.cloud .

$ docker push gcr.io/{PROJECT_ID}/demo-app:latest

$ gcloud run deploy {SERVICE_NAME} --image {IMAGE_URL}
```

Open https://{CLOUD_RUN_URL}/docs URL in browser.