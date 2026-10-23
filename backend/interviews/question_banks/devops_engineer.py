"""
DevOps Engineer Question Bank - 25 distinct technical questions.
Covers Linux systems, Docker containerization, Kubernetes orchestration, CI/CD pipelines, Terraform IaC, networking, and observability.
"""

DEVOPS_ENGINEER_QUESTIONS = [
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "docker",
        "difficulty": "medium",
        "question_text": "How do multi-stage Docker builds reduce container image size and improve security for production deployments?",
        "expected_answer": "Multi-stage builds define multiple FROM instructions in a single Dockerfile. The first stages contain heavy build tools, compilers, and dev dependencies to build artifacts (e.g. binaries, minified bundles). The final minimal stage (e.g. alpine or distroless) copies only the compiled artifact and runtime dependencies, shrinking image size from gigabytes to megabytes and drastically reducing the attack surface.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should containers avoid running processes as the root user?",
        "code_snippet": "FROM node:20 AS builder\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci\nCOPY . .\nRUN npm run build\n\nFROM nginx:alpine\nCOPY --from=builder /app/dist /usr/share/nginx/html\nEXPOSE 80\nCMD [\"nginx\", \"-g\", \"daemon off;\"]"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "kubernetes",
        "difficulty": "medium",
        "question_text": "Explain the difference between Liveness, Readiness, and Startup Probes in Kubernetes. What happens when each probe fails?",
        "expected_answer": "Liveness Probe checks if the application container is still alive; if it fails, kubelet kills and restarts the container. Readiness Probe checks if the application is ready to accept incoming network traffic; if it fails, the pod's IP is removed from matching Service endpoints so no traffic is routed to it. Startup Probe checks if slow-starting apps have initialized; while running, it disables liveness and readiness probes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the danger of setting an aggressive initialDelaySeconds on liveness probes?",
        "code_snippet": "livenessProbe:\n  httpGet:\n    path: /healthz\n    port: 8080\n  initialDelaySeconds: 15\n  periodSeconds: 10\nreadinessProbe:\n  httpGet:\n    path: /ready\n    port: 8080\n  periodSeconds: 5"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "kubernetes",
        "difficulty": "hard",
        "question_text": "What is the difference between a ClusterIP, NodePort, and LoadBalancer Service in Kubernetes? How does an Ingress Controller route traffic to them?",
        "expected_answer": "ClusterIP exposes the Service on an internal cluster IP, accessible only within the cluster (default). NodePort exposes the Service on a static high port (30000-32767) on each node's external IP. LoadBalancer provisions an external cloud load balancer (AWS NLB/ALB) pointing to the nodes. An Ingress Controller (like NGINX) acts as a reverse proxy/layer 7 router, routing external HTTP/HTTPS domain paths to multiple internal ClusterIP services using a single public IP.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do annotations in Ingress resources configure TLS termination with cert-manager?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "terraform_iac",
        "difficulty": "medium",
        "question_text": "What is the role of Terraform State (terraform.tfstate)? Why must state files be stored remotely in S3/GCS with state locking enabled (e.g. DynamoDB)?",
        "expected_answer": "Terraform state maps real-world cloud resources to your configuration files, tracks metadata, and caches resource attributes. Storing state remotely provides team collaboration on a single source of truth and prevents secret leakage in git. State locking (via DynamoDB or backend lock) prevents concurrent terraform apply executions from corrupting or overwriting the state file.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does terraform refresh detect configuration drift between code and cloud infrastructure?",
        "code_snippet": "terraform {\n  backend \"s3\" {\n    bucket         = \"my-terraform-state-bucket\"\n    key            = \"prod/infrastructure.tfstate\"\n    region         = \"us-east-1\"\n    dynamodb_table = \"terraform-locks\"\n    encrypt        = true\n  }\n}"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "ci_cd",
        "difficulty": "medium",
        "question_text": "Compare Blue-Green Deployments, Canary Releases, and Rolling Updates. What are the trade-offs of each regarding zero-downtime and resource cost?",
        "expected_answer": "Rolling Update gradually replaces old pods/instances with new ones; resource efficient (no extra fleet needed) but runs two versions simultaneously during rollout. Blue-Green maintains two identical production environments (Blue=live, Green=idle); deployment switches router/load balancer instantly, enabling instant rollback, but doubles infrastructure cost during deploy. Canary releases route a small percentage of traffic (5%) to the new version to test error rates before full rollout.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does Argo Rollouts or Flagger automate canary rollbacks based on Prometheus metrics?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "linux_networking",
        "difficulty": "medium",
        "question_text": "How do you troubleshoot a Linux server where an application cannot connect to an external database port? What commands do you run step-by-step?",
        "expected_answer": "Steps: 1. Verify DNS resolution: 'dig db.internal' or 'nslookup'. 2. Check network route and reachability: 'ping' or 'traceroute'. 3. Test port connectivity: 'nc -zv db.internal 5432' or 'telnet' or 'curl -v'. 4. Check local outbound firewall: 'iptables -L -n -v' or 'ufw status'. 5. Check local socket state: 'ss -tulpn' or 'netstat -tuln'. 6. Check security group / network ACLs on cloud provider.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What does TCP SYN_SENT status in netstat output indicate?",
        "code_snippet": "# Test TCP port handshake with timeout:\nnc -zv -w 5 db.production.internal 5432"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "git_strategies",
        "difficulty": "easy",
        "question_text": "Compare Trunk-Based Development with GitFlow. Why do high-performing DevOps teams favor trunk-based development with feature flags?",
        "expected_answer": "GitFlow relies on long-lived branches (develop, release, feature, hotfix) with infrequent large merges, often causing 'merge hell' and delayed feedback. Trunk-Based Development has developers commit small, frequent changes directly into the main trunk (short-lived branches < 1 day) and gates unready features behind Feature Flags. This enables rapid CI/CD, fast feedback loops, and continuous deployment.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do short-lived branches prevent large merge conflicts in agile teams?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "kubernetes",
        "difficulty": "hard",
        "question_text": "How does Horizontal Pod Autoscaler (HPA) work in Kubernetes? What metrics (CPU, Memory, Custom Metrics via Prometheus Adapter) trigger scaling events?",
        "expected_answer": "HPA queries the Metrics Server or Prometheus Adapter every 15 seconds (default). It calculates desired replicas using the formula: desiredReplicas = ceil[currentReplicas * (currentMetricValue / targetMetricValue)]. While CPU/Memory are standard, queue length (RabbitMQ/Kafka) or HTTP request rate (RPS) are superior metrics for scaling web and worker services before queues back up.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is memory alone often tricky for HPA scale-down decisions in garbage-collected languages?",
        "code_snippet": "apiVersion: autoscaling/v2\nkind: HorizontalPodAutoscaler\nmetadata:\n  name: api-hpa\nspec:\n  scaleTargetRef:\n    apiVersion: apps/v1\n    kind: Deployment\n    name: api-deployment\n  minReplicas: 2\n  maxReplicas: 10\n  metrics:\n  - type: Resource\n    resource:\n      name: cpu\n      target:\n        type: Utilization\n        averageUtilization: 70"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "security_devsecops",
        "difficulty": "medium",
        "question_text": "How do you securely manage production secrets in Kubernetes and CI/CD pipelines instead of committing them to Git?",
        "expected_answer": "Never commit plaintext secrets to Git. Best practices: 1. Use centralized secret managers like HashiCorp Vault, AWS Secrets Manager, or Google Secret Manager. 2. In Kubernetes, integrate External Secrets Operator (ESO) or Vault CSI Driver to inject secrets dynamically into pod memory/files. 3. In GitOps, use encrypted repos with Mozilla SOPS or Bitnami Sealed Secrets. 4. In CI/CD, use OIDC short-lived tokens instead of permanent access keys.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does GitHub Actions OIDC integration with AWS IAM eliminate stored AWS_SECRET_ACCESS_KEY credentials?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "observability",
        "difficulty": "medium",
        "question_text": "Explain the Three Pillars of Observability: Metrics, Logs, and Traces. How does OpenTelemetry unify these three pillars?",
        "expected_answer": "Metrics are aggregable numeric values over time (counters, gauges, histograms) tracking system health and rates. Logs are discrete timestamped text events detailing specific actions or errors. Traces track the end-to-end journey of a single request across distributed microservices via a trace ID. OpenTelemetry provides a single vendor-neutral standard API, SDK, and Collector agent to generate, collect, and export all three data types.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between an SLI, an SLO, and an SLA?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "linux_internals",
        "difficulty": "hard",
        "question_text": "Explain how Linux cgroups (control groups) and namespaces form the underlying foundation of container isolation in Docker and Linux containers.",
        "expected_answer": "Namespaces provide isolation of system resources: PID (process IDs), NET (network interfaces/routing), MNT (filesystem mount points), UTS (hostname), IPC (inter-process communication), and USER (user/group IDs). Cgroups (Control Groups) provide resource metering, allocation, and limitation: capping how much CPU, memory, disk I/O, and pids a container process tree can consume.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What happens when a process exceeds its cgroup memory limit (OOM Killer)?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "networking_cloud",
        "difficulty": "medium",
        "question_text": "What is a VPC (Virtual Private Cloud)? Explain the architecture of Public Subnets versus Private Subnets and the role of an Internet Gateway (IGW) vs NAT Gateway.",
        "expected_answer": "A VPC is an isolated virtual network in the cloud. Public subnets have route tables pointing to an Internet Gateway (IGW), allowing resources with public IPs bidirectional direct internet communication. Private subnets have route tables pointing to a NAT Gateway (located in a public subnet), allowing backend instances (databases, app servers) outbound internet access (for package updates) while blocking all unsolicited inbound connections from the internet.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why are databases always placed in private isolated subnets without public IPs?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "gitops",
        "difficulty": "medium",
        "question_text": "What is GitOps (e.g. ArgoCD or Flux)? How does the pull-based GitOps model differ from traditional push-based CI/CD deployment pipelines?",
        "expected_answer": "In GitOps, a Git repository is the single source of truth for desired infrastructure and application state. Push-based CI/CD executes scripts in runners with production cluster credentials to push changes. Pull-based GitOps runs an agent (ArgoCD/Flux) inside the Kubernetes cluster that monitors the Git repo, detects divergence (drift), and pulls changes into the cluster, eliminating cluster write credentials from CI runners.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does ArgoCD handle automated drift reconciliation when someone manually edits a resource using kubectl?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "ansible_config",
        "difficulty": "easy",
        "question_text": "What does Idempotency mean in configuration management tools like Ansible or Chef? Why is idempotency critical for server provisioning?",
        "expected_answer": "Idempotency means that executing a playbook or task multiple times produces the exact same system state as executing it once, without making unnecessary modifications or causing errors if the desired state is already satisfied (e.g. ensuring an NGINX package is installed only if not present, rather than reinstalling). This guarantees predictable, reliable system state.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you test Ansible playbooks in CI using Molecule?",
        "code_snippet": "- name: Ensure nginx is installed and started\n  apt:\n    name: nginx\n    state: present\n- name: Ensure nginx service is running\n  service:\n    name: nginx\n    state: started\n    enabled: yes"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "monitoring_alerting",
        "difficulty": "medium",
        "question_text": "What are Prometheus Counter, Gauge, and Histogram metric types? How do you write a PromQL query to calculate the 5-minute HTTP 5xx error rate percentage?",
        "expected_answer": "Counter is a cumulative metric that only increases or resets to zero (e.g. total_requests). Gauge is a value that goes up and down (e.g. memory_usage, temperature). Histogram samples observations (usually request durations) and counts them into configurable buckets. 5xx error rate PromQL: sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m])) * 100.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should rate() always be calculated on counters before taking sums or averages?",
        "code_snippet": "sum(rate(http_requests_total{status=~\"5..\"}[5m]))\n/\nsum(rate(http_requests_total[5m])) * 100"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "docker_compose",
        "difficulty": "easy",
        "question_text": "How do Docker Compose networks and volumes enable multi-container local development environments? What is the difference between bind mounts and named volumes?",
        "expected_answer": "Docker Compose creates a default bridge network where containers resolve each other by service name via built-in DNS. Bind mounts map a specific host directory directly into the container (ideal for live code reloading in development). Named volumes are managed entirely by Docker inside the Docker storage area, offering superior I/O performance on macOS/Windows and persistent database storage across container recreations.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why do bind mounts on Docker Desktop for Mac often suffer file I/O performance bottlenecks?",
        "code_snippet": "services:\n  db:\n    image: postgres:16\n    volumes:\n      - pgdata:/var/lib/postgresql/data\n  web:\n    build: .\n    volumes:\n      - ./:/app\nvolumes:\n  pgdata:"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "kubernetes",
        "difficulty": "hard",
        "question_text": "What are Kubernetes Network Policies? By default, can all pods in a cluster communicate with each other, and how do you enforce zero-trust isolation?",
        "expected_answer": "By default, Kubernetes network is an open flat network where any pod can communicate with any other pod across all namespaces. Network Policies act as firewall rules at layer 3/4. Creating an empty default-deny NetworkPolicy isolates the namespace. Then, explicit ingress/egress rules allow communication only between authorized pods using label selectors (e.g. backend pods can only talk to database pods on port 5432).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does NetworkPolicy require a CNI plugin that supports it (like Calico or Cilium)?",
        "code_snippet": "kind: NetworkPolicy\napiVersion: networking.k8s.io/v1\nmetadata:\n  name: default-deny-all\nspec:\n  podSelector: {}\n  policyTypes:\n  - Ingress\n  - Egress"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "ssl_tls",
        "difficulty": "medium",
        "question_text": "Explain the TLS 1.3 handshake process. How does automated SSL certificate rotation work with Let's Encrypt and cert-manager using ACME HTTP-01 or DNS-01 challenges?",
        "expected_answer": "TLS 1.3 completes in 1-RTT: client sends ClientHello with supported ciphers and key share; server responds with ServerHello, certificate, and key share; both derive encryption keys. ACME HTTP-01 challenge creates a token file at http://domain/.well-known/acme-challenge/ and Let's Encrypt verifies ownership over port 80. DNS-01 challenge creates a TXT record (_acme-challenge.domain) via Cloud DNS API, enabling wildcard certificates (*.domain).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is DNS-01 challenge required for wildcard certificates?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "linux_performance",
        "difficulty": "hard",
        "question_text": "What does a high Linux Load Average (e.g. load average 24.0 on an 8-core CPU) mean? How do you distinguish between CPU saturation, disk I/O wait, and memory thrashing?",
        "expected_answer": "Load average is the average number of processes in the run queue (running or waiting for CPU) plus processes in uninterruptible sleep state (D state, usually waiting for disk I/O). On an 8-core machine, load > 8 means saturation. Diagnostic commands: 1. 'top' or 'htop' to check %CPU vs %wa (I/O wait). 2. 'vmstat 1' to check runnable processes (r) vs blocked (b). 3. 'iostat -xz 1' to check disk queue and %util. 4. 'sar -B' or 'free -m' for swap paging.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What causes uninterruptible D-state processes on NFS mounts?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "security_devsecops",
        "difficulty": "medium",
        "question_text": "What is container image vulnerability scanning (e.g. Trivy or Grype), and how do you implement a gate in CI/CD to block deployment on CRITICAL CVEs?",
        "expected_answer": "Vulnerability scanners inspect container filesystem layers and package manifests against CVE vulnerability databases (NVD, GitHub Advisories). In CI/CD pipelines, Trivy scans the built image before pushing to the container registry: running 'trivy image --exit-code 1 --severity CRITICAL' exits with code 1 if critical CVEs without fixes are found, immediately halting the pipeline before deployment.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a Software Bill of Materials (SBOM) and why are tools like Syft used to generate them?",
        "code_snippet": "- name: Scan image with Trivy\n  run: |\n    trivy image --exit-code 1 --severity CRITICAL,HIGH myapp:${{ github.sha }}"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "disaster_recovery",
        "difficulty": "medium",
        "question_text": "Define Recovery Point Objective (RPO) and Recovery Time Objective (RTO). How do automated database backups and multi-region replication satisfy low RPO/RTO SLAs?",
        "expected_answer": "RPO is the maximum acceptable data loss measured in time (e.g. 5 minutes of data). RTO is the maximum acceptable downtime duration to restore operations (e.g. 30 minutes to recover). Low RPO is achieved via continuous WAL (write-ahead log) archiving / point-in-time recovery (PITR) and synchronous multi-AZ replication. Low RTO is achieved via automated failover (multi-region DNS routing or pilot light environments).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between Hot Standby and Pilot Light disaster recovery strategies?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "kubernetes",
        "difficulty": "hard",
        "question_text": "What are DaemonSets, StatefulSets, and Jobs in Kubernetes? When would you use a StatefulSet instead of a standard Deployment?",
        "expected_answer": "DaemonSet ensures that all (or some) nodes run a copy of a pod (e.g. Fluentd log collectors, node-exporter). Jobs run pods to completion and terminate (batch tasks). Deployments manage stateless pods with randomized pod names and interchangeable pods. StatefulSets manage stateful applications (databases, Kafka, Elasticsearch) requiring unique stable network IDs (pod-0, pod-1), ordered deployment/scaling, and dedicated PersistentVolumeClaims per pod.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a Headless Service and why do StatefulSets require one?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "linux_automation",
        "difficulty": "easy",
        "question_text": "Write a bash script that checks if a critical service (e.g. nginx) is active using systemctl, and if down, restarts it and logs an alert timestamp to a log file.",
        "expected_answer": "Use systemctl is-active --quiet nginx. If the exit code is non-zero (failed), execute systemctl restart nginx, verify, and append the current date and message to /var/log/service_monitor.log.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you schedule this script to run every 5 minutes using cron?",
        "code_snippet": "#!/bin/bash\nSERVICE=\"nginx\"\nLOG_FILE=\"/var/log/service_monitor.log\"\nif ! systemctl is-active --quiet \"$SERVICE\"; then\n    echo \"[$(date '+%Y-%m-%d %H:%M:%S')] $SERVICE is down! Restarting...\" >> \"$LOG_FILE\"\n    systemctl restart \"$SERVICE\"\nfi"
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "ci_cd",
        "difficulty": "medium",
        "question_text": "What is Cache Poisoning and Dependency Locking in CI/CD pipelines? How do lockfiles (package-lock.json, poetry.lock, Pipfile.lock) guarantee build reproducibility?",
        "expected_answer": "Dependency drift occurs when builds install floating versions (e.g. ^1.2.0) that pull broken upstream releases. Lockfiles specify exact cryptographic hashes and version pins for all direct and transitive dependencies. In CI/CD, running clean install commands (e.g. npm ci instead of npm install) guarantees identical dependencies across all builds and prevents compromised or altered packages.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does npm ci fail if package-lock.json is out of sync with package.json?",
        "code_snippet": None
    },
    {
        "role": "DevOps Engineer",
        "technology": "devops",
        "category": "service_mesh",
        "difficulty": "hard",
        "question_text": "What is a Service Mesh (e.g. Istio or Linkerd)? How do sidecar proxies provide mutual TLS (mTLS) and fine-grained traffic shifting without code changes?",
        "expected_answer": "A service mesh manages service-to-service communication via a data plane of Envoy sidecar proxies deployed alongside each application container and a centralized control plane. Proxies intercept all inbound and outbound traffic, encrypting communication with transparent mutual TLS (mTLS) with short-lived X.509 certs, providing distributed tracing headers, circuit breaking, rate limiting, and canary traffic routing without touching app code.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the CPU and memory overhead of running Envoy sidecars on thousands of microservice pods?",
        "code_snippet": None
    }
]
