# Cloud-Based Law Firm Management System

A cloud-native, enterprise-grade law firm management system built with **Spring Boot 3 (Java 17+)**, **React 19 + TypeScript + Tailwind CSS + Vite**, and supported by a full **DevOps suite (AWS, Docker, Kubernetes, Ansible, Terraform, and GitHub Actions CI/CD)**.

---

## Key Features & Architecture
- **Authentication & Security**: JWT-based stateless authentication with BCrypt password hashing.
- **Role-Based Access Control**: Pre-seeded `ADMIN`, `LAWYER`, and `STAFF` roles with fine-grained access.
- **Client Directory**: Track individual, corporate, non-profit, and government clients with consultation notes and history.
- **Lawyer & Counsel Management**: Track bar registration numbers, practice specializations, and real-time availability.
- **Legal Case Tracking**: Comprehensive case registration, court filings, hearing schedules, and lawyer assignments.
- **Appointments & Hearings**: Scheduling, room allocation, meeting agendas, and status workflow.
- **Document Repository**: Secure multi-part document uploads (PDF, DOCX, XLSX, Images), metadata indexing, and single-click downloading.
- **Live Analytics Dashboard**: Real-time metrics for cases, status distribution charts (Pie Chart), monthly case registrations (Bar Chart), and audit activity logs.

---

## Demo Credentials
- **Email:** `admin@lawfirm.com`
- **Password:** `Admin@123`

---

## Local Development

### Prerequisites
- **Java**: JDK 17 or higher
- **Node.js**: v18 or higher (v20+ recommended)

### 1. Run Backend
```bash
cd backend
# On Windows:
.\mvnw.cmd spring-boot:run

# On Linux / macOS:
./mvnw spring-boot:run
```
Backend will be available on: **http://localhost:8081**  
H2 Web Console: **http://localhost:8081/h2-console** (JDBC URL: `jdbc:h2:mem:lawfirmdb`, User: `sa`, Password: empty)

### 2. Run Frontend
In a separate terminal:
```bash
cd frontend
npm install
npm run dev
```
Frontend will be available on: **http://localhost:5173**

---

## DevOps & Cloud Tools

### 1. Docker & Docker Compose
The project includes production-ready multi-stage Dockerfiles for both services and an automated reverse proxy with Nginx:
```bash
# Build and run entire stack in background:
docker-compose up --build -d

# View running services:
docker-compose ps

# Tear down:
docker-compose down
```
- Frontend: **http://localhost:5173**
- Backend: **http://localhost:8081**

---

### 2. Kubernetes (K8s)
Complete Kubernetes manifests with Namespace, ConfigMap, Secrets, PVC, Deployments, ClusterIP Services, HPA, and Ingress are located in `k8s/`:
```bash
# Apply entire Kubernetes configuration via Kustomize:
kubectl apply -k k8s/

# Or apply manifests individually:
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/postgres-pvc.yaml
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/ingress.yaml

# Check pod statuses:
kubectl get pods -n lawfirm
```

---

### 3. Ansible Automation
Automated server provisioning and deployment playbook is in `ansible/`:
```bash
cd ansible
# Run playbook on target servers:
ansible-playbook -i inventory.ini playbook.yml
```
This installs Docker, Git, UFW firewall rules, clones the repository, deploys the stack, and verifies backend health.

---

### 4. AWS Cloud Infrastructure (Terraform)
Production AWS Cloud infrastructure (VPC, Subnets, RDS PostgreSQL, S3 Documents Bucket, ECR, ECS Fargate, and ALB) is declared in `terraform/`:
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Outputs will provide:
- `alb_dns_name`: Public URL for the Application Load Balancer
- `rds_endpoint`: PostgreSQL connection endpoint
- `s3_documents_bucket`: Document storage bucket
- `ecr_backend_url` & `ecr_frontend_url`: ECR image registries

---

### 5. AWS CloudFormation
For 1-click AWS stack launch without Terraform:
```bash
aws cloudformation create-stack \
  --stack-name lawfirm-stack \
  --template-body file://aws/cloudformation.yaml \
  --parameters ParameterKey=EnvironmentName,ParameterValue=production
```

---

### 6. CI/CD Pipeline (GitHub Actions)
Automated pipeline in `.github/workflows/ci-cd-aws.yml`:
- Builds and runs tests for Spring Boot backend
- Builds and bundles React frontend
- Builds multi-stage Docker images
- Pushes images to Amazon ECR
- Updates AWS ECS service deployments
