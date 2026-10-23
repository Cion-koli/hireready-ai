"""
Backend Developer Question Bank - 25 distinct technical questions.
Focuses on REST/gRPC API design, authentication, databases, caching, concurrency, security, and scalability.
"""

BACKEND_DEVELOPER_QUESTIONS = [
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "api_design_idempotency",
        "difficulty": "medium",
        "question_text": "What is Idempotency in HTTP REST APIs? Which HTTP methods are idempotent by specification, and how do you implement Idempotency Keys in POST payment endpoints?",
        "expected_answer": "An HTTP method is idempotent if making the request multiple times produces the exact same server-side state as making it once. GET, PUT, DELETE, HEAD, and OPTIONS are idempotent; POST is not. For POST payments, clients generate an Idempotency-Key header (UUID). The server stores the key with request hash and result in a distributed cache (Redis) with lock; duplicate requests return the cached response without charging twice.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle in-flight duplicate requests arriving before the first request finishes?",
        "code_snippet": "POST /api/v1/payments\nIdempotency-Key: e4b2c1f0-7b56-4b9d-9f12-32a821e289bf"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "authentication_jwt",
        "difficulty": "medium",
        "question_text": "Explain the architecture of JSON Web Tokens (JWT). What are the three parts of a JWT, and how do you securely handle token revocation / logout without storing all tokens in a database?",
        "expected_answer": "JWT consists of Header (algorithm, type), Payload (claims, exp, sub), and Signature (HMAC or RSA hash of header + payload using secret/private key). Since JWTs are stateless, instant revocation can be handled via: short-lived access tokens (5-15 min) paired with refresh tokens, maintaining a Redis token blacklist of revoked jti (token ID) identifiers until their expiration, or incrementing a user-level token_version.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should sensitive data like passwords or credit cards never be placed in JWT payload claims?",
        "code_snippet": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIn0.signature"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "database_transactions",
        "difficulty": "hard",
        "question_text": "What is the difference between Optimistic Concurrency Control and Pessimistic Locking in database updates? In what traffic scenarios would you choose each?",
        "expected_answer": "Pessimistic locking uses database locks (SELECT ... FOR UPDATE) to block concurrent transactions until the current transaction completes, best for high-contention, low-latency critical updates (bank transfers, ticket bookings). Optimistic locking doesn't lock rows during read; instead, it checks a version column on update (UPDATE table SET balance=..., version=version+1 WHERE id=1 AND version=curr_version); if 0 rows affected, it detects conflict and retries, best for read-heavy low-contention systems.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the risk of deadlocks with pessimistic row-level locking?",
        "code_snippet": "UPDATE inventory SET stock = stock - 1, version = version + 1 \nWHERE id = 42 AND version = 3;"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "caching_redis",
        "difficulty": "medium",
        "question_text": "Explain common caching patterns: Cache-Aside, Write-Through, and Write-Behind. What are Cache Stampede (Dog-Piling) and Cache Penetration, and how do you prevent them?",
        "expected_answer": "Cache-Aside: app queries cache; on miss, queries DB and writes to cache. Write-Through: writes to cache and DB simultaneously. Write-Behind: writes to cache immediately, queues async DB flush. Cache Stampede occurs when a high-traffic key expires, causing thousands of concurrent requests to hit the DB; prevent with mutex locks or probabilistic early expiration (XFetch). Cache Penetration queries non-existent keys; prevent with Bloom Filters or caching null values.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What eviction policies does Redis offer (volatile-lru, allkeys-lru, allkeys-lfu)?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "rate_limiting",
        "difficulty": "hard",
        "question_text": "Explain rate limiting algorithms: Token Bucket, Leaky Bucket, and Sliding Window Log. How would you implement distributed rate limiting with Redis?",
        "expected_answer": "Token bucket adds tokens at fixed rate up to capacity; requests consume tokens, allowing bursts. Leaky bucket processes requests at constant smooth rate. Sliding window log records timestamps of requests in Redis sorted set (ZADD), removes timestamps older than window (ZREMRANGEBYSCORE), and checks cardinality (ZCARD); if under limit, request proceeds.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does a fixed window counter suffer from 2x burst traffic around window boundaries?",
        "code_snippet": "MULTI\nZADD ratelimit:user_123 1719999999 1719999999\nZREMRANGEBYSCORE ratelimit:user_123 0 1719999939\nZCARD ratelimit:user_123\nEXEC"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "microservices_communication",
        "difficulty": "medium",
        "question_text": "Compare Synchronous REST / gRPC communication with Asynchronous Event-Driven Messaging (Kafka, RabbitMQ) between microservices. When should each be used?",
        "expected_answer": "Synchronous (gRPC/REST) blocks until target service responds, tightly coupling services; ideal for immediate query reads and operations requiring instantaneous responses. Asynchronous messaging (Kafka/RabbitMQ) decouples services, buffers spikes, guarantees eventual consistency, and enables event-driven architectures where services publish domain events without knowing consumers.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Protocol Buffers (Protobuf) and why is gRPC faster than REST JSON?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "distributed_transactions",
        "difficulty": "hard",
        "question_text": "What is the SAGA pattern for managing distributed transactions across multiple microservices? Compare Choreography-based SAGAs with Orchestration-based SAGAs.",
        "expected_answer": "SAGA breaks a distributed business transaction into a series of local transactions across services; if any step fails, compensating transactions are executed in reverse order to rollback state. Choreography: services emit domain events and react to each other without central coordinator, simple but hard to trace. Orchestration: a central coordinator service tells participants what local transactions to execute and manages compensations, easier to monitor and maintain.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is Two-Phase Commit (2PC) considered an antipattern in cloud microservices?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "sql_vs_nosql",
        "difficulty": "easy",
        "question_text": "When would you choose a Relational Database (PostgreSQL, MySQL) over a NoSQL database (MongoDB, Cassandra, DynamoDB)? Explain ACID vs BASE.",
        "expected_answer": "Relational: structured relational data, strong ACID consistency, complex multi-table JOINs, financial/transactional systems. NoSQL: document or key-value structures with dynamic schemas, horizontal scaling across clusters, high-write throughput. Relational follows ACID; NoSQL follows BASE (Basically Available, Soft-state, Eventual consistency).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the CAP Theorem (Consistency, Availability, Partition Tolerance)?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "security_owasp",
        "difficulty": "medium",
        "question_text": "Explain SQL Injection and how Parameterized Queries (Prepared Statements) prevent it at the database driver level. Why is string sanitization or regex filtering insufficient?",
        "expected_answer": "SQL injection occurs when untrusted input is concatenated into query strings, allowing attackers to alter query semantics. Parameterized queries send query structure and parameter values separately over the database protocol; the database pre-compiles the query plan with parameter placeholders ($1, ?), treating values purely as literal data, making code injection structurally impossible. String sanitizers frequently fail due to encoding edge cases or bypasses.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Second-Order SQL Injection?",
        "code_snippet": "-- Safe Parameterized Query\ncursor.execute('SELECT * FROM users WHERE email = %s', [user_email])"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "load_balancing",
        "difficulty": "medium",
        "question_text": "Explain Layer 4 (Transport) vs Layer 7 (Application) Load Balancing. Name common balancing algorithms (Round Robin, Least Connections, IP Hash) and their applications.",
        "expected_answer": "Layer 4 load balancing operates at TCP/UDP level, routing packets based on IP and port without inspecting payload, very fast. Layer 7 operates at HTTP/HTTPS level, inspecting headers, URLs, cookies, and payloads to route requests intelligently (e.g. /api to backend pool, /images to CDN). Round Robin distributes equally; Least Connections directs traffic to servers with fewest active requests; IP Hash ensures session affinity.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is SSL/TLS Termination at the load balancer?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "message_queues",
        "difficulty": "medium",
        "question_text": "Explain message delivery guarantees: At-most-once, At-least-once, and Exactly-once. Why is designing consumers to be idempotent the industry standard for message processing?",
        "expected_answer": "At-most-once: messages may be lost, never duplicated. At-least-once: messages never lost, but network retries can deliver duplicates. Exactly-once: highly complex, requires end-to-end transactional coordination. Industry standard is At-least-once with idempotent consumers, ensuring duplicate message processing has no adverse side effects.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a Dead Letter Queue (DLQ) and when is a poison message moved to it?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "circuit_breaker",
        "difficulty": "hard",
        "question_text": "Explain the Circuit Breaker pattern (Closed, Open, Half-Open states) in distributed backend services. How does it prevent cascading failures?",
        "expected_answer": "Closed: requests pass normally; failure count tracked. Open: if failure rate crosses threshold, circuit trips open immediately, failing fast without calling downstream service, preventing thread exhaustion. Half-Open: after timeout, a small test batch of requests is allowed through; if they succeed, circuit resets to Closed; if they fail, circuit returns to Open.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do libraries like Resilience4j or Netflix Hystrix implement circuit breakers?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "webhooks",
        "difficulty": "medium",
        "question_text": "How do you design a reliable Webhook delivery system that notifies third-party client endpoints of events? Explain signature verification using HMAC-SHA256.",
        "expected_answer": "Delivery: queue webhook payloads in message queue, dispatch via workers, implement exponential backoff retries on failure (up to 24-72 hours), and record delivery logs. Security: sign the payload using HMAC-SHA256 with a shared webhook secret, sending signature in a header (X-Signature); the receiver computes HMAC of raw request body and verifies match using constant-time comparison.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is constant-time comparison (hmac.compare_digest) critical against timing attacks?",
        "code_snippet": "signature = hmac.new(webhook_secret, payload_bytes, hashlib.sha256).hexdigest()"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "graphql_vs_rest",
        "difficulty": "medium",
        "question_text": "Compare GraphQL with REST APIs. What problem does GraphQL solve regarding Over-Fetching and Under-Fetching, and what are its performance trade-offs (e.g. N+1 in resolvers)?",
        "expected_answer": "REST has fixed endpoints returning predetermined payloads (leading to over-fetching unnecessary data or under-fetching requiring multiple API requests). GraphQL lets clients request exactly the fields needed in a single query. Trade-offs: complex query analysis required to prevent malicious deep queries, caching is harder (no HTTP status/URL caching), and nested field resolvers easily cause N+1 database queries unless using DataLoader batching.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does DataLoader batch and deduplicate database requests across resolvers?",
        "code_snippet": "query { user(id: \"1\") { name email posts { title } } }"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "database_connection_pooling",
        "difficulty": "medium",
        "question_text": "What is Database Connection Pooling (e.g. PgBouncer, HikariCP)? Why is establishing a new database connection on every HTTP request expensive?",
        "expected_answer": "Establishing a database connection requires TCP handshakes, TLS negotiation, authentication, and backend server process/thread memory allocation. A connection pool maintains an active set of pre-warmed connections; application worker threads borrow an active connection, execute their query, and return it to the pool, dramatically reducing latency and protecting the database from process exhaustion.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between session pooling and transaction pooling in PgBouncer?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "distributed_tracing",
        "difficulty": "medium",
        "question_text": "What is Distributed Tracing (OpenTelemetry)? How do Trace IDs and Span IDs track a single user request across dozens of microservices?",
        "expected_answer": "Distributed tracing tracks request lifecycles through microservice networks. When a request enters the API Gateway, a unique Trace ID is generated and propagated in HTTP headers (traceparent) across all downstream HTTP/gRPC calls. Each service creates Spans (with Span IDs, start/end timestamps, logs, and attributes) tied to the parent Trace ID, visualized in Jaeger or Datadog.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the W3C Trace Context standard?",
        "code_snippet": "traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "database_sharding_keys",
        "difficulty": "hard",
        "question_text": "How do you choose an effective Shard Key for horizontal database partitioning? What happens when a query does not include the shard key (scatter-gather)?",
        "expected_answer": "A good shard key provides uniform write/read distribution across all shards and isolates common queries to a single shard (e.g. user_id or tenant_id). If a query lacks the shard key, the database coordinator must perform a scatter-gather query: sending queries to all shards in parallel and aggregating/sorting results in memory, causing high latency and CPU bottlenecks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is consistent hashing and how does it minimize data movement when adding new shards?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "http_status_codes",
        "difficulty": "easy",
        "question_text": "Explain when to return HTTP status codes: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, and 422 Unprocessable Entity in a REST API.",
        "expected_answer": "400: malformed syntax (invalid JSON). 401: client lacks valid authentication credentials. 403: client is authenticated but lacks required permission/role. 404: requested resource does not exist. 409: request conflicts with current server state (duplicate unique key, version mismatch). 422: syntax is valid, but semantic validation failed (e.g. age must be > 18).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should you sometimes return 404 instead of 403 to prevent resource enumeration?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "password_hashing",
        "difficulty": "easy",
        "question_text": "How should user passwords be stored securely in a backend database? Explain salts, work factors (cost factor), and why MD5 or SHA-256 are dangerous for password storage.",
        "expected_answer": "Passwords must be hashed using adaptive, salted algorithms (bcrypt, Argon2, PBKDF2). A unique cryptographic salt per user prevents Rainbow Table attacks. A configurable work factor slows down hashing to resist brute-force hardware attacks. MD5 and SHA-256 are designed for speed, allowing attackers with GPUs to calculate billions of hashes per second.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is Argon2id the recommended winner of the Password Hashing Competition?",
        "code_snippet": "hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "api_versioning",
        "difficulty": "medium",
        "question_text": "Compare API versioning strategies: URI path (/v1/users), Query parameter (/users?v=1), Header versioning (Accept: application/vnd.company.v1+json). What are the pros and cons of each?",
        "expected_answer": "URI Path: clear, easy to test in browser and cache, most popular in industry, but mixes versioning with resource identity. Query Param: simple, but cluttered URLs. Header Versioning: adheres strictly to REST principles, clean URLs, but harder to test in browser and requires custom cache configurations.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you deprecate old API versions gracefully using Sunset and Deprecation HTTP headers?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "graceful_shutdown",
        "difficulty": "medium",
        "question_text": "How do you implement Graceful Shutdown in a backend web service container upon receiving a SIGTERM signal from Kubernetes or Docker?",
        "expected_answer": "1) Listen for SIGTERM/SIGINT. 2) Stop accepting new incoming requests at load balancer / readiness probe. 3) Allow currently active in-flight HTTP requests and database transactions to finish within a timeout window (e.g. 30s). 4) Close background worker consumers and flush logs. 5) Close database connection pools. 6) Exit process with code 0.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What happens if the service does not terminate before the terminationGracePeriodSeconds expires (SIGKILL)?",
        "code_snippet": ""
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "file_upload_architecture",
        "difficulty": "medium",
        "question_text": "Why should high-volume file uploads (e.g. videos, PDFs) bypass application backend servers using Pre-Signed S3 / Cloud Storage URLs?",
        "expected_answer": "Streaming large files through backend web servers consumes worker memory, holds open connection sockets, and wastes backend CPU bandwidth. With Pre-Signed URLs, the client requests a temporary cryptographically signed upload URL from the backend; the client then uploads the file directly to object storage (S3/GCS); upon completion, object storage triggers an event webhook to notify the backend.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does multipart upload allow resilient resuming of failed large file uploads?",
        "code_snippet": "url = s3_client.generate_presigned_url('put_object', Params={'Bucket': 'b', 'Key': 'k'}, ExpiresIn=300)"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "distributed_locking",
        "difficulty": "hard",
        "question_text": "How does the Redlock algorithm or Redis SETNX provide distributed locking across backend servers? What caveats exist regarding clock drift and garbage collection pauses?",
        "expected_answer": "SET key uuid NX PX timeout acquires a lock only if it doesn't exist, expiring automatically. The UUID ensures only the acquiring process can release the lock via Lua script. Redlock acquires locks across N independent Redis nodes. Caveat: If a client experiences a long GC pause, the lock might expire in Redis and be granted to another client while the first client still thinks it owns the lock (mitigated with fencing tokens).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a fencing token and how does it prevent stale lock writes?",
        "code_snippet": "SET lock:resource_42 unique_client_id NX PX 30000"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "eventual_consistency",
        "difficulty": "hard",
        "question_text": "What is the Transactional Outbox pattern, and how does it guarantee that database state changes and message queue events occur atomically without distributed 2PC transactions?",
        "expected_answer": "When modifying database state, the application writes both the business entity update and an 'outbox event' record inside the SAME local ACID database transaction. A separate background process (or Debezium change data capture reading WAL) reads unpublished outbox rows, publishes them to the message broker (Kafka/RabbitMQ), and marks them published, ensuring zero event loss.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Change Data Capture (CDC)?",
        "code_snippet": "BEGIN;\nINSERT INTO orders (id, total) VALUES (1, 100);\nINSERT INTO outbox_events (event_type, payload) VALUES ('OrderCreated', '{\"id\": 1}');\nCOMMIT;"
    },
    {
        "role": "Backend Developer",
        "technology": "backend",
        "category": "practical_system_design",
        "difficulty": "hard",
        "question_text": "Design a URL shortener backend (like bit.ly) handling 100M URLs per month. Explain the hashing/base62 encoding, database schema, caching, and redirect status code (301 vs 302).",
        "expected_answer": "Architecture: Base62 encoding (a-z, A-Z, 0-9) converts auto-incrementing 64-bit ID to 7-character short code (62^7 = 3.5 trillion URLs). Database: SQL or NoSQL with index on short_code. Caching: Redis stores top 20% URLs with LRU eviction. HTTP Redirects: 301 Moved Permanently caches in browser (faster, but loses analytics); 302 Found forces all clicks to hit the backend server for accurate click analytics.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you generate unique IDs across multiple distributed backend servers (Snowflake ID)?",
        "code_snippet": ""
    }
]
