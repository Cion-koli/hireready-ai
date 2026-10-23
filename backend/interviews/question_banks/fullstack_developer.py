"""
Full-Stack Developer Question Bank - 25 distinct technical questions.
Focuses on end-to-end web architecture, frontend-to-backend integration, rendering modes, database modeling, and deployment.
"""

FULLSTACK_DEVELOPER_QUESTIONS = [
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "rendering_architectures",
        "difficulty": "medium",
        "question_text": "Compare Client-Side Rendering (CSR), Server-Side Rendering (SSR), Static Site Generation (SSG), and Incremental Static Regeneration (ISR). When would an e-commerce platform use each?",
        "expected_answer": "CSR renders HTML on client via JS; fast page transitions, but slow initial load and poor SEO for crawlers. SSR renders HTML on server per request; excellent SEO and fast FCP, higher server load. SSG builds HTML at compile time; blazing fast from CDN, ideal for marketing/blog pages. ISR re-generates static pages in background on-demand when traffic arrives, ideal for e-commerce product pages with millions of SKUs.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Hydration in SSR and why can hydration mismatches cause UI bugs?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "auth_flow",
        "difficulty": "medium",
        "question_text": "Walk through an end-to-end secure authentication flow in a full-stack SPA with React frontend and Python/Node backend using HTTP-only cookies and JWTs.",
        "expected_answer": "1) User submits credentials via HTTPS POST /api/auth/login. 2) Backend validates hash, generates short-lived access token and long-lived refresh token. 3) Backend sets refresh token in an HttpOnly, Secure, SameSite=Lax cookie and returns access token in JSON body (or both in cookies). 4) Frontend stores access token in memory. 5) Axios/fetch interceptor attaches access token as Bearer header. 6) On 401 expiration, interceptor calls /api/auth/refresh to rotate tokens transparently.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does storing refresh tokens in an HttpOnly cookie protect against XSS token theft?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "api_contract_management",
        "difficulty": "medium",
        "question_text": "How do you maintain end-to-end Type Safety between backend API models and frontend components (e.g. OpenAPI / Swagger codegen, tRPC, GraphQL code generator)?",
        "expected_answer": "In polyglot setups: the backend generates an OpenAPI (Swagger) spec from models (FastAPI / DRF Spectacular), and openapi-typescript-codegen generates matching TypeScript interfaces on the frontend. In TypeScript-only full-stack: tRPC shares backend router types directly with frontend clients without code generation, ensuring compile-time safety across client-server boundaries.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do schema registries prevent breaking contract changes in production?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "database_design",
        "difficulty": "medium",
        "question_text": "Design a relational database schema for an interview preparation SaaS with Users, InterviewSessions, Questions, Answers, and Evaluations. Explain foreign key relationships and cascade deletion rules.",
        "expected_answer": "Users (1) -> (M) Interviews (user_id FK, CASCADE); Interviews (1) -> (M) Questions (interview_id FK, CASCADE); Questions (1) -> (1) Answers (question_id FK UNIQUE, CASCADE); Answers (1) -> (1) Evaluations (answer_id FK UNIQUE, CASCADE); Interviews (1) -> (1) Reports (interview_id FK UNIQUE, CASCADE). Cascade rules ensure deleting a user or interview session cleans up all dependent child entities.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "When should soft deletion (deleted_at IS NULL) be used instead of hard ON DELETE CASCADE?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "realtime_websocket",
        "difficulty": "hard",
        "question_text": "How do you architect real-time bidirectional communication between a React frontend and Python backend using WebSockets, Redis Pub/Sub, and connection state management?",
        "expected_answer": "Frontend establishes a WebSocket connection with reconnect logic and heartbeats (ping/pong). Backend ASGI server (Django Channels / FastAPI) handles the WebSocket connection and binds client to a channel group. When an event occurs on any backend server, it publishes to a Redis Pub/Sub broker, which broadcasts the event to the appropriate WebSocket server workers and pushes to the client socket.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you authenticate WebSocket connections during the initial HTTP upgrade handshake?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "cors_debugging",
        "difficulty": "easy",
        "question_text": "You deploy your React app to https://app.example.com and your backend API to https://api.example.com. API requests fail with a CORS error in the browser console. What causes this, and how do you resolve it on the backend?",
        "expected_answer": "The browser enforces the Same-Origin Policy because the subdomains differ. When sending cross-origin requests with credentials, the browser sends an OPTIONS preflight. The backend must configure CORS middleware to allow the origin 'https://app.example.com', set Access-Control-Allow-Credentials: true, allow necessary headers (Content-Type, Authorization), and allow methods (GET, POST, PUT, DELETE, OPTIONS).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why doesn't Postman or curl experience CORS errors?",
        "code_snippet": "CORS_ALLOWED_ORIGINS = ['https://app.example.com']\nCORS_ALLOW_CREDENTIALS = True"
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "state_hydration",
        "difficulty": "hard",
        "question_text": "What is Hydration in React/Next.js? What causes hydration mismatch errors (e.g. 'Text content does not match server-rendered HTML'), and how do you fix them?",
        "expected_answer": "Hydration is the process where client-side JavaScript attaches event listeners and state to server-rendered HTML DOM. Mismatches happen when client and server generate different markup, caused by: checking window/localStorage during initial render, rendering dynamic dates/times (new Date()), or invalid HTML nesting (e.g. <p> inside <p>). Fix by using useEffect for client-only rendering or suppressing hydration warnings where intentional.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does React 18 Selective Hydration and Streaming SSR work?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "ci_cd_deployment",
        "difficulty": "medium",
        "question_text": "Describe a production CI/CD deployment pipeline for a full-stack application using GitHub Actions, Docker, and cloud hosting (e.g. AWS / Vercel).",
        "expected_answer": "1) PR opened: GitHub Actions runs linting, unit tests for frontend and backend, and build checks. 2) Merge to main: Action builds production Docker image for backend, runs DB migration checks, and pushes image to ECR. 3) Deploys backend to ECS / Kubernetes with rolling updates. 4) Builds frontend static bundle, pushes to S3 / CloudFront CDN (or Vercel) with asset cache headers and invalidates edge cache.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you run database migrations safely during deployment without downtime?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "web_security_csrf",
        "difficulty": "medium",
        "question_text": "Explain how the Double Submit Cookie pattern and Anti-CSRF tokens protect full-stack web applications from Cross-Site Request Forgery.",
        "expected_answer": "In Double Submit Cookie: the server sets a random CSRF token in an un-HttpOnly cookie. On state-changing requests (POST/PUT), the frontend reads this cookie and injects its value into a custom request header (X-CSRFToken). An attacker site cannot read cookies from another origin under SOP; when the backend verifies that the header matches the cookie, the request is confirmed legitimate.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does SameSite=Strict / Lax cookie attribute eliminate most CSRF attacks natively?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "performance_optimistic_ui",
        "difficulty": "easy",
        "question_text": "What is Optimistic UI updating on the frontend? How do you implement it while ensuring state rollback if the backend API mutation fails?",
        "expected_answer": "Optimistic UI immediately updates the client interface assuming the server request will succeed, providing zero-latency perceived performance. Implementation: 1) Save previous state snapshot; 2) Mutate UI state optimistically; 3) Send API request; 4) If request fails, revert state to the snapshot and display an error toast notification to the user.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does React Query / TanStack Query manage onMutate and onError rollbacks?",
        "code_snippet": "const previous = state;\nsetState(optimisticState);\ntry { await api.save(); } catch { setState(previous); }"
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "serverless_architectures",
        "difficulty": "medium",
        "question_text": "What are the trade-offs of deploying full-stack backends on Serverless Functions (AWS Lambda, Vercel Serverless)? Explain Cold Starts and database connection exhaustion.",
        "expected_answer": "Pros: automatic scaling to zero, low cost for intermittent traffic, zero server maintenance. Cons: Cold starts cause 500ms-2s latency when spinning up new micro-VMs. Connection exhaustion: every concurrent serverless instance establishes its own DB connection; 1,000 requests can open 1,000 connections, crashing PostgreSQL unless an external connection proxy (AWS RDS Proxy, PgBouncer) is used.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do provisioned concurrency and edge runtime functions mitigate cold starts?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "error_monitoring",
        "difficulty": "easy",
        "question_text": "How do you set up centralized error monitoring across both frontend and backend using tools like Sentry? What is source map uploading?",
        "expected_answer": "Sentry SDKs are integrated into both frontend (React ErrorBoundary) and backend (Django/Express middleware). Unhandled exceptions and console errors are captured with stack traces, breadcrumbs, user ID, and browser context. For production minified frontend bundles, CI/CD uploads source maps securely to Sentry to de-minify stack traces back to readable original source code.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should source maps never be served publicly on production web servers?",
        "code_snippet": "Sentry.init({ dsn: '...', tracesSampleRate: 1.0 });"
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "pagination_strategy",
        "difficulty": "medium",
        "question_text": "Compare Offset-based pagination with Keyset (Cursor-based) pagination across both backend SQL queries and frontend Infinite Scroll components.",
        "expected_answer": "Offset: SELECT * FROM t LIMIT 20 OFFSET 1000; simple, allows page jumps (/page/5), but gets progressively slower on large offsets (full index scan) and produces duplicate/skipped items if records are inserted while user scrolls. Keyset: SELECT * FROM t WHERE id < last_id ORDER BY id DESC LIMIT 20; O(1) indexed lookups, consistent during real-time writes, ideal for infinite scroll feeds.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does GraphQL Relay specification standardize cursor-based pagination (edges, node, pageInfo)?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "database_migrations",
        "difficulty": "medium",
        "question_text": "What steps are required to rename a column in a production database without taking down the running application during deployment?",
        "expected_answer": "Expand and Contract phase: 1) Add new column with NULLable setting. 2) Update backend code to dual-write to both old and new columns, reading from old. Deploy. 3) Run background script to backfill historical rows from old to new column. 4) Update backend code to read and write to new column. Deploy. 5) Drop old column in a subsequent release.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the Danger of running DDL locks on high-write production tables?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "rest_restful_principles",
        "difficulty": "easy",
        "question_text": "Explain HATEOAS (Hypermedia As The Engine Of Application State) and Richardson Maturity Model levels in REST API design.",
        "expected_answer": "Level 0: The Swamp of POX (single URI, POST for everything, e.g. XML-RPC). Level 1: Resources (individual URIs for resources). Level 2: HTTP Verbs (GET for read, POST for create, DELETE for delete, proper HTTP status codes). Level 3: Hypermedia Controls (HATEOAS, responses contain hypermedia links detailing next permissible actions).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why do most commercial REST APIs stop at Level 2 of the Richardson Maturity Model?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "file_upload_pipeline",
        "difficulty": "medium",
        "question_text": "Design a complete file upload pipeline: user uploads a profile picture from React -> backend validates and generates S3 presigned URL -> image is uploaded -> async worker generates thumbnails -> UI updates.",
        "expected_answer": "1) React requests presigned upload URL from backend with file metadata (size, content-type). 2) Backend validates allowed MIME types and max size, generates S3 PUT presigned URL. 3) React uploads file directly to S3 via HTTP PUT. 4) S3 triggers an EventBridge / Lambda or webhook notifying backend. 5) Background worker resizes image into multiple thumbnails and stores CDN URLs in DB. 6) Frontend updates via polling or WebSocket.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you validate image MIME types on the server beyond checking file extensions?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "search_indexing",
        "difficulty": "medium",
        "question_text": "When should you introduce a dedicated search engine (Elasticsearch, Meilisearch, Algolia) instead of relying on SQL 'LIKE %query%' or PostgreSQL Full-Text Search?",
        "expected_answer": "SQL 'LIKE %query%' requires full table scans and cannot use standard B-Tree indexes. PostgreSQL Full-Text Search (tsvector, tsquery, GIN index) works well for moderate workloads up to hundreds of thousands of documents. Dedicated engines (Elasticsearch/Meilisearch) become necessary when requiring typo tolerance (fuzzy matching), facet filtering, relevance scoring (TF-IDF/BM25), synonyms, and sub-10ms queries across millions of documents.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is an Inverted Index in search engines?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "docker_compose",
        "difficulty": "easy",
        "question_text": "How do you use Docker and Docker Compose to containerize a full-stack project (React frontend, Django backend, PostgreSQL database, and Redis cache)?",
        "expected_answer": "Create Dockerfile for backend (Python + dependencies) and frontend (Node build + Nginx). In docker-compose.yml, define services: 'db' (postgres:16 with volume mount for data persistence), 'redis' (redis:alpine), 'backend' (depends_on db/redis, port 8000), 'frontend' (port 80/5173). Docker Compose sets up internal DNS so backend connects to db using host 'db' and Redis using 'redis'.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the purpose of Docker multi-stage builds for frontend apps?",
        "code_snippet": "services:\n  backend:\n    build: ./backend\n    ports: ['8000:8000']\n    environment: [DATABASE_URL=postgres://db:5432/app]"
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "security_headers",
        "difficulty": "medium",
        "question_text": "Explain essential HTTP security headers for modern web applications: Strict-Transport-Security (HSTS), Content-Security-Policy (CSP), X-Content-Type-Options, and Referrer-Policy.",
        "expected_answer": "HSTS forces browsers to connect strictly over HTTPS, preventing SSL stripping. CSP restricts origins from which scripts, styles, and images can load, preventing XSS and data exfiltration. X-Content-Type-Options: nosniff prevents browsers from MIME-sniffing files as executable scripts. Referrer-Policy controls how much referrer information is leaked when clicking external links.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the CSP directive 'upgrade-insecure-requests'?",
        "code_snippet": "Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-random123';"
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "caching_layer_cdn",
        "difficulty": "medium",
        "question_text": "Explain the multi-tier caching hierarchy in full-stack web applications: Browser Cache -> CDN Edge Cache -> Application Reverse Proxy (Nginx) -> In-Memory Cache (Redis) -> Database Buffer Cache.",
        "expected_answer": "1) Browser Cache: client memory/disk, fastest. 2) CDN Edge Cache (CloudFront/Cloudflare): geographically distributed, serves static assets and cached edge responses without hitting origin. 3) Reverse Proxy (Nginx): load balances, terminates SSL, caches API responses. 4) In-Memory Cache (Redis): stores frequently queried data models and session tokens in RAM. 5) DB Buffer Cache: database shared memory caching index and data pages.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you invalidate a CDN edge cache on new production deployments?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "async_job_queues",
        "difficulty": "medium",
        "question_text": "A user clicks 'Generate Comprehensive PDF Report'. Generating the report takes 45 seconds. How do you design this end-to-end full-stack experience to prevent HTTP timeouts?",
        "expected_answer": "1) Client clicks button, sends POST /api/reports/generate. 2) Backend validates, enqueues task in message queue (Celery/BullMQ), generates job_id, and returns 202 Accepted immediately with { job_id: 'xyz' }. 3) Client polls GET /api/jobs/xyz (or listens on WebSocket / SSE). 4) Worker generates PDF, uploads to S3, updates job status to 'completed' with download URL. 5) Client receives notification and displays download button.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does a 202 Accepted response adhere to REST principles for long-running jobs?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "oauth2_social_login",
        "difficulty": "hard",
        "question_text": "Explain the OAuth 2.0 Authorization Code Grant with PKCE (Proof Key for Code Exchange) flow for user sign-in with Google or GitHub in modern web apps.",
        "expected_answer": "1) Client generates random code_verifier and computes code_challenge (SHA-256 hash). 2) Redirects user to Google OAuth URL with code_challenge. 3) User authenticates and consents; Google redirects back to client with authorization code. 4) Backend sends authorization code + original code_verifier to Google token endpoint. 5) Google hashes verifier, confirms it matches challenge, and returns access_token / id_token, preventing authorization code interception.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why was PKCE originally created for mobile apps and now mandated for Single Page Applications?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "e2e_testing",
        "difficulty": "medium",
        "question_text": "Compare Unit Testing, Integration Testing, and End-to-End (E2E) Testing (Playwright / Cypress) in the testing pyramid of a full-stack project.",
        "expected_answer": "Unit tests (Jest/Vitest/pytest) test isolated functions/components in memory (fast, cheap, highest volume). Integration tests test component interactions (API route calling database). E2E tests (Playwright/Cypress) launch a real headless browser and execute real user journeys from frontend UI to database and back (verifies critical flows like signup and payment), most realistic but slowest and most expensive.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you manage test database seeding and teardown during CI test runs?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "rate_limiting_fullstack",
        "difficulty": "medium",
        "question_text": "How do frontend and backend cooperate to handle API rate limiting cleanly using HTTP 429 Too Many Requests and the Retry-After header?",
        "expected_answer": "Backend detects client request threshold exceeded, returns HTTP 429 with 'Retry-After: 30' header indicating seconds to wait. Frontend HTTP interceptor intercepts 429, reads Retry-After header, disables submit buttons, displays a countdown timer to the user, and automatically retries the request when the timer expires.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is jitter in exponential backoff algorithms and why does it prevent thundering herds?",
        "code_snippet": ""
    },
    {
        "role": "Full-Stack Developer",
        "technology": "fullstack",
        "category": "practical_system_design",
        "difficulty": "hard",
        "question_text": "Design a collaborative real-time document editor (like Google Docs). How do you handle simultaneous concurrent edits from two users (Operational Transformation vs CRDTs)?",
        "expected_answer": "Architecture: React editor canvas connected via WebSockets to backend servers clustered over Redis. Conflict resolution: Operational Transformation (OT) transforms operations based on concurrent operation logs via a central server (used by Google Docs). CRDTs (Conflict-free Replicated Data Types, like Yjs / Automerge) mathematically guarantee convergence without requiring a central authority, allowing seamless offline-first edits.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between state-based and operation-based CRDTs?",
        "code_snippet": ""
    }
]
