# DevOps Private Kubernetes Project

A hands-on DevOps project demonstrating how to build, containerize, test, and deploy a Python Flask application across **QA, UAT, and Production** using Kubernetes, GitHub Actions, Docker, Kustomize, Ansible, Traefik, and Terraform.

The project focuses on real-world DevOps practices such as **CI/CD, immutable Docker images, environment promotion, manual production approvals, Kubernetes self-healing, rolling deployments, rollback, infrastructure as code, and security hardening**.

---

## 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │     Developer    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     GitHub       │
                         │   Source Code    │
                         └────────┬─────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │   GitHub Actions     │
                       │        CI/CD         │
                       └──────────┬───────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
             ┌──────────────┐           ┌──────────────┐
             │ Application  │           │ Docker Build │
             │    Tests     │           │   & Push     │
             └──────────────┘           └──────┬───────┘
                                               │
                                               ▼
                                      ┌─────────────────┐
                                      │   Docker Hub    │
                                      │ Image Registry  │
                                      └────────┬────────┘
                                               │
                                               ▼
                                      ┌─────────────────┐
                                      │ Kubernetes/K3s │
                                      └────────┬────────┘
                                               │
                         ┌─────────────────────┼─────────────────────┐
                         ▼                     ▼                     ▼
                    ┌─────────┐           ┌─────────┐          ┌────────────┐
                    │   QA    │ ───────► │   UAT   │ ───────► │ Production │
                    └─────────┘           └─────────┘          └────────────┘
                                               │                     │
                                               │ Approval            │ Approval
                                               ▼                     ▼
                                      Manual Validation      Controlled Release

                         ┌──────────────────────────────┐
                         │          Traefik             │
                         │      Ingress / Routing       │
                         └──────────────────────────────┘

                         ┌──────────────────────────────┐
                         │          Ansible             │
                         │ Server & Runner Configuration │
                         └──────────────────────────────┘

                         ┌──────────────────────────────┐
                         │          Terraform           │
                         │       AWS Infrastructure     │
                         │          & S3 State          │
                         └──────────────────────────────┘
```

---

## 🎯 Project Objectives

This project was created to demonstrate a complete DevOps workflow:

* Source code management with Git/GitHub
* Automated application testing
* Docker image creation
* Docker image versioning using Git commit SHA
* Container image storage in Docker Hub
* Kubernetes application deployment
* Environment separation
* Kustomize-based configuration management
* Automated QA deployment
* Manual approval before UAT and Production
* Traefik ingress routing
* Kubernetes health checks
* Rolling deployments
* Kubernetes rollback
* Self-healing and scaling
* Server configuration using Ansible
* Self-hosted GitHub Actions runner
* AWS infrastructure management using Terraform
* Terraform remote state using Amazon S3
* Basic container and Kubernetes security hardening

---

## 🛠️ Technologies Used

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| Linux          | Server operating system             |
| Git            | Version control                     |
| GitHub         | Source code repository              |
| GitHub Actions | CI/CD automation                    |
| Python         | Application development             |
| Flask          | Web application framework           |
| Docker         | Application containerization        |
| Docker Hub     | Container image registry            |
| Kubernetes     | Container orchestration             |
| K3s            | Lightweight Kubernetes distribution |
| Kustomize      | Kubernetes configuration management |
| Traefik        | Ingress and HTTP routing            |
| Ansible        | Server configuration and automation |
| Terraform      | Infrastructure as Code              |
| AWS S3         | Terraform remote state              |

---

## 📁 Project Structure

```text
devops-private-k8s-project/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
│
├── kubernetes/
│   ├── base/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── kustomization.yaml
│   │
│   └── environments/
│       ├── qa/
│       │   ├── kustomization.yaml
│       │   └── ingress.yaml
│       │
│       ├── uat/
│       │   ├── kustomization.yaml
│       │   └── ingress.yaml
│       │
│       └── production/
│           ├── kustomization.yaml
│           └── ingress.yaml
│
├── ansible/
│   ├── ansible.cfg
│   ├── inventory/
│   │   └── hosts
│   ├── group_vars/
│   │   └── kubernetes.yml
│   ├── playbook.yml
│   └── roles/
│       ├── kubernetes/
│       └── github_runner/
│
├── terraform/
│   ├── bootstrap/
│   └── main.tf
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
└── README.md
```

---

# 🔄 CI/CD Pipeline

The project follows this deployment flow:

```text
Developer Push
      │
      ▼
   GitHub
      │
      ▼
GitHub Actions
      │
      ├── Run Tests
      │
      ├── Build Docker Image
      │
      └── Push Image
              │
              ▼
          Docker Hub
              │
              ▼
           Deploy QA
              │
              ▼
       QA Validation
              │
              ▼
        UAT Approval
              │
              ▼
          Deploy UAT
              │
              ▼
       UAT Validation
              │
              ▼
    Production Approval
              │
              ▼
      Deploy Production
```

---

# 🚀 Build Once, Promote Many

One of the main design principles of this project is:

> **Build the Docker image once and promote the same image through all environments.**

The Docker image is tagged using the Git commit SHA.

Example:

```text
devops-app:<git-commit-sha>
```

The same image is promoted through:

```text
QA → UAT → Production
```

This avoids rebuilding the application separately for each environment and provides better release traceability.

---

# ☸️ Kubernetes

The application runs on Kubernetes using separate namespaces for:

```text
QA
UAT
Production
```

Each environment can have different:

* Replica counts
* Environment variables
* Ingress configuration
* Deployment configuration

The common Kubernetes configuration is maintained in the **base** directory, while environment-specific settings are maintained using **Kustomize overlays**.

### Kubernetes Features Demonstrated

* Deployments
* Services
* Namespaces
* Configurations
* Replica management
* Rolling updates
* Readiness probes
* Liveness probes
* Resource requests and limits
* Self-healing
* Scaling
* Rollbacks
* Ingress

---

# 🔧 Kustomize

Kustomize is used to maintain reusable Kubernetes configuration.

```text
                    Kubernetes Base
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
            QA          UAT     Production
```

This avoids maintaining completely separate Kubernetes manifests for every environment.

---

# 🌐 Traefik

Traefik is used as the Kubernetes ingress controller.

It provides HTTP routing from external requests to the appropriate Kubernetes Service.

Conceptually:

```text
Client
  │
  ▼
Traefik
  │
  ├── QA → QA Service
  │
  ├── UAT → UAT Service
  │
  └── Production → Production Service
```

The application Services remain internal to Kubernetes while Traefik acts as the entry point.

---

# 🤖 Ansible

Ansible is used for server configuration and automation.

The Ansible automation handles tasks such as:

* Installing required packages
* Checking Kubernetes/K3s availability
* Configuring the environment
* Creating the GitHub Actions runner user
* Preparing the self-hosted runner directory
* Validating the Kubernetes server

The project uses an Ansible role-based structure to keep automation organized and reusable.

---

# 🏃 Self-Hosted GitHub Actions Runner

The project uses a self-hosted GitHub Actions runner located in the private Kubernetes environment.

This allows GitHub Actions jobs to execute commands against the private Kubernetes cluster without exposing the Kubernetes API directly to the public internet.

Conceptually:

```text
GitHub
   │
   │ Outbound runner connection
   ▼
Self-Hosted Runner
   │
   ▼
Private Kubernetes Cluster
```

---

# 🌎 Terraform & AWS

Terraform is used separately from the Kubernetes application deployment.

Its responsibility is:

```text
Terraform
    │
    ▼
AWS Infrastructure
    │
    └── S3 Terraform State
```

Terraform remote state is stored in Amazon S3 with:

* Versioning
* Server-side encryption
* Public access blocked
* Native S3 state locking

Terraform is intentionally separated from the application CI/CD process.

---

# 🔐 Security Practices

The project includes several security improvements.

### Container Security

The Flask application runs as a non-root user inside the container.

```text
Root
  ↓
Avoided

appuser
  ↓
Application
```

### Kubernetes Security

The deployment uses security controls such as:

* `runAsNonRoot`
* `allowPrivilegeEscalation: false`
* CPU requests/limits
* Memory requests/limits
* Readiness probes
* Liveness probes

### Secrets

Sensitive information is not stored in the repository.

Examples:

```text
Docker Hub token
AWS credentials
GitHub runner registration token
Terraform sensitive variables
```

These should be supplied through appropriate secret-management mechanisms.

---

# ❤️ Application Health

The application provides a health endpoint:

```text
/health
```

Kubernetes uses this endpoint for:

* Readiness checks
* Liveness checks

This allows Kubernetes to determine whether the application is ready to receive traffic and whether a container needs to be restarted.

---

# 🔄 Deployment Strategy

Production deployments use a rolling update strategy.

The goal is to avoid unnecessary downtime while a new application version is deployed.

```text
Old Version
     │
     ├── Running
     │
     ▼
New Version Started
     │
     ▼
Health Check
     │
     ▼
Traffic Continues
     │
     ▼
Old Version Removed
```

---

# ↩️ Rollback

If a deployment introduces a problem, Kubernetes Deployment history can be used to return to a previous revision.

```text
Version 1
   ↓
Version 2
   ↓
Version 3
   ↓
Problem
   ↓
Rollback
   ↓
Version 2
```

This provides a fast recovery mechanism for failed releases.

---

# 📊 Environment Strategy

| Environment | Purpose                      | Deployment      |
| ----------- | ---------------------------- | --------------- |
| QA          | Automated initial validation | Automatic       |
| UAT         | User/functional validation   | Manual approval |
| Production  | Final release                | Manual approval |

This provides a controlled promotion process instead of deploying every change directly to production.

---

# 🧠 Key DevOps Concepts Demonstrated

This project demonstrates practical understanding of:

* CI/CD
* Git workflows
* Docker
* Containerization
* Docker image versioning
* Kubernetes
* K3s
* Kubernetes namespaces
* Deployments
* Services
* Ingress
* Traefik
* Kustomize
* Health probes
* Resource management
* Self-healing
* Scaling
* Rolling updates
* Rollbacks
* Environment promotion
* Immutable artifacts
* Infrastructure as Code
* Terraform
* AWS S3
* Ansible automation
* GitHub Actions
* Self-hosted runners
* Secrets management
* Container security

---

# 🔍 Observability & Troubleshooting

The project also provides a foundation for operational troubleshooting through Kubernetes and container tooling.

Examples include:

```bash
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get ingress
kubectl describe pod
kubectl logs
kubectl rollout status
kubectl rollout history
kubectl rollout undo
```

These commands can be used to investigate application health, deployments, networking, and release issues.

---

# 📌 Design Principles

### 1. Build Once

The application image is built once during CI.

### 2. Immutable Artifact

The Docker image is identified using the Git commit SHA.

### 3. Promote the Same Image

The same image moves through:

```text
QA → UAT → Production
```

### 4. Environment Isolation

Each environment has its own Kubernetes namespace and configuration.

### 5. Automated QA

QA deployment occurs automatically after a successful CI build.

### 6. Controlled Production

UAT and Production require explicit approval.

### 7. Infrastructure as Code

AWS infrastructure is managed using Terraform.

### 8. Configuration Automation

Server configuration is managed using Ansible.

### 9. Secure by Default

Containers run without unnecessary root privileges and secrets are kept outside source control.

---

# 🎓 Learning Outcomes

By completing this project, I gained practical experience with:

* Designing a complete CI/CD pipeline
* Containerizing a Python application
* Deploying applications on Kubernetes
* Managing multiple Kubernetes environments
* Using Kustomize for configuration management
* Implementing ingress with Traefik
* Building GitHub Actions workflows
* Configuring self-hosted runners
* Automating server configuration with Ansible
* Managing AWS infrastructure with Terraform
* Using S3 for Terraform remote state
* Implementing deployment approvals
* Performing Kubernetes rollbacks
* Applying basic container and Kubernetes security practices

---

# 👨‍💻 Project Summary

This project represents a complete **private Kubernetes-based DevOps delivery platform** for a containerized application.

It combines:

```text
GitHub
   +
GitHub Actions
   +
Docker
   +
Docker Hub
   +
Kubernetes / K3s
   +
Kustomize
   +
Traefik
   +
Ansible
   +
Terraform
   +
AWS
```

The resulting workflow demonstrates how a development change can move from **source code → automated testing → container image → QA → UAT → Production** using modern DevOps practices.

---

## 📄 Disclaimer

This repository is intended as a **learning and portfolio project**.

Environment-specific information such as private IP addresses, credentials, tokens, internal hostnames, and production secrets should never be committed to the repository.

---

## 👤 Author

**Shivam Yadav**

DevOps Engineer 

Areas of interest:

* Linux
* AWS
* Docker
* Kubernetes
* Ansible
* Terraform
* CI/CD
* DevOps
