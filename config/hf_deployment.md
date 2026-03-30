# Hugging Face Spaces Deployment Guide

This environment is compatible with Hugging Face Spaces using the Docker SDK.

## Prerequisites
- A Hugging Face account.
- `git` installed locally.
- (Optional) `docker` installed for local testing.

## Step-by-Step Deployment

### 1. Create a New Space
Go to [huggingface.co/new-space](https://huggingface.co/new-space) and follow these settings:
- **Space Name:** `customer-support-triage` (or your choice)
- **SDK:** `Docker`
- **Template:** `Blank`
- **Public/Private:** Choose as needed.

### 2. Clone the Space Repository
```bash
git clone https://huggingface.co/spaces/<your-username>/customer-support-triage
cd customer-support-triage
```

### 3. Copy Project Files
Copy all files from this project into the cloned repository:
- `env/`
- `models/`
- `tasks/`
- `graders/`
- `scripts/`
- `config/`
- `openenv.yaml`
- `Dockerfile`

### 4. Push to Hugging Face
```bash
git add .
git commit -m "Initial commit: OpenEnv Customer Triage"
git push
```

### 5. Set Environment Variables
In the Space settings on Hugging Face, add your `OPENAI_API_KEY` under the "Variables and Secrets" section.

### 6. Verify Tags
Ensure the `openenv.yaml` is in the root directory. This allows the Hugging Face OpenEnv discovery system to find and index your environment.
