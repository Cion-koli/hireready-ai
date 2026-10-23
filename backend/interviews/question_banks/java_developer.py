"""
Java Developer Question Bank - 25 distinct technical questions.
Focuses on Java Core, OOP, JVM Architecture & GC, Collections, Multithreading, Streams, and Spring Boot.
"""

JAVA_DEVELOPER_QUESTIONS = [
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "jvm_memory_model",
        "difficulty": "hard",
        "question_text": "Explain the JVM Memory Architecture: Heap (Young Generation: Eden, S0, S1, and Old/Tenured Generation), Metaspace, Stack Memory, and Program Counter Register.",
        "expected_answer": "Stack memory stores primitive local variables and method call frames per thread (LIFO, thread-safe). Heap memory stores all objects and is shared across threads; divided into Young Gen (Eden where new objects are allocated, and Survivor spaces S0/S1 where surviving objects are copied during Minor GC) and Old/Tenured Gen (objects that survive tenure threshold). Metaspace (replaced PermGen in Java 8) stores class metadata in native off-heap memory.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What causes an OutOfMemoryError: Metaspace versus OutOfMemoryError: Java heap space?",
        "code_snippet": ""
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "garbage_collection",
        "difficulty": "hard",
        "question_text": "Compare Java Garbage Collectors: Serial, Parallel, G1 (Garbage-First), and modern low-latency ZGC / Shenandoah. How does G1 divide heap memory into regions?",
        "expected_answer": "Serial: single-threaded, for small CLI apps. Parallel: throughput-focused multi-threaded GC, causes longer Stop-The-World (STW) pauses. G1 GC: divides heap into thousands of equal-sized virtual regions (Eden, Survivor, Old, Humongous), prioritizing regions with the most garbage first for predictable pause times. ZGC / Shenandoah: concurrent collectors performing marking, relocation, and compaction concurrently with application threads, keeping STW pauses sub-millisecond.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a 'Stop-The-World' pause in Java?",
        "code_snippet": ""
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "collections_framework",
        "difficulty": "medium",
        "question_text": "Explain the internal working of HashMap in Java 8+. How does it handle hash collisions using LinkedList and Red-Black Trees (TREEIFY_THRESHOLD)?",
        "expected_answer": "HashMap uses an array of Node buckets. It hashes the key (key.hashCode() spread), computes index (hash & (n-1)). If a collision occurs, entries are chained in a LinkedList. In Java 8+, when a single bucket exceeds TREEIFY_THRESHOLD (8 entries) and table capacity is >= 64, the linked list converts to a balanced Red-Black Tree (TreeNode), improving worst-case search time from O(N) to O(log N).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why must equals() and hashCode() contracts always be maintained when using custom objects as HashMap keys?",
        "code_snippet": "Map<String, Integer> map = new HashMap<>(16, 0.75f);"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "multithreading_concurrency",
        "difficulty": "hard",
        "question_text": "Explain the 'volatile' keyword in Java. How does it ensure memory visibility across CPU thread caches, and why is it not sufficient for atomic compound operations (like count++)?",
        "expected_answer": "The volatile keyword ensures that reads and writes to a variable are written directly to and read directly from main memory (RAM), establishing a 'happens-before' relationship and preventing CPU caching inconsistencies. However, compound operations like count++ involve three distinct steps (read, modify, write); volatile does not provide mutual exclusion, so race conditions still occur unless AtomicInteger or synchronized locks are used.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do AtomicInteger and Compare-And-Swap (CAS) achieve lock-free thread safety?",
        "code_snippet": "private volatile boolean running = true;\nprivate AtomicInteger counter = new AtomicInteger(0);"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "concurrent_hashmap",
        "difficulty": "hard",
        "question_text": "How does ConcurrentHashMap achieve thread safety in Java without locking the entire map like Hashtable or Collections.synchronizedMap()?",
        "expected_answer": "Hashtable locks the entire table for every read/write via synchronized methods. In Java 7, ConcurrentHashMap used Segment Locking (16 independent locks). In Java 8+, it eliminated segments in favor of bucket-level synchronization using lock-free Compare-And-Swap (CAS) for node insertion and synchronized locks strictly on the first node (head) of individual colliding buckets, allowing high concurrency across unrelated buckets.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Does ConcurrentHashMap permit null keys or null values?",
        "code_snippet": "ConcurrentMap<String, String> cache = new ConcurrentHashMap<>();"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "java_streams",
        "difficulty": "medium",
        "question_text": "Explain Java 8 Streams: Intermediate operations (filter, map, flatMap, distinct) versus Terminal operations (collect, reduce, forEach). Why are streams lazy?",
        "expected_answer": "Intermediate operations return a new Stream and are executed lazily; they do not process data until a Terminal operation is invoked. Terminal operations produce a non-stream result (List, count, optional) and consume the stream. Laziness allows stream fusion: the engine processes items through the pipeline in a single pass without allocating intermediate collection buffers.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between map() and flatMap() in Java Streams?",
        "code_snippet": "List<String> names = users.stream()\n    .filter(u -> u.getAge() >= 18)\n    .map(User::getName)\n    .collect(Collectors.toList());"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "functional_interfaces",
        "difficulty": "easy",
        "question_text": "What is a Functional Interface in Java (@FunctionalInterface)? Name the 4 core functional interfaces in java.util.function: Predicate, Function, Consumer, and Supplier.",
        "expected_answer": "A Functional Interface has exactly one abstract method (SAM), though it can have multiple default or static methods. Predicate<T>: takes T, returns boolean (test). Function<T, R>: takes T, returns R (apply). Consumer<T>: takes T, returns void (accept). Supplier<T>: takes no args, returns T (get).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do method references (ClassName::methodName) provide shorthand for lambda expressions?",
        "code_snippet": "Predicate<String> isNotEmpty = s -> !s.isEmpty();\nSupplier<Double> randomValue = Math::random;"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "spring_boot_ioc",
        "difficulty": "medium",
        "question_text": "Explain Inversion of Control (IoC) and Dependency Injection (DI) in Spring Boot. Why is Constructor Injection preferred over Field Injection (@Autowired on private fields)?",
        "expected_answer": "IoC delegates object creation and lifecycle management to the Spring ApplicationContext container. DI injects dependencies into components. Constructor Injection is preferred because: 1) It ensures immutability (dependencies can be final); 2) It prevents NullPointerExceptions by guaranteeing dependencies exist at construction; 3) It makes unit testing easy without needing reflection or Spring runners.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What are Bean scopes in Spring (Singleton, Prototype, Request, Session)?",
        "code_snippet": "@Service\npublic class UserService {\n    private final UserRepository userRepo;\n    public UserService(UserRepository userRepo) {\n        this.userRepo = userRepo;\n    }\n}"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "spring_data_jpa",
        "difficulty": "medium",
        "question_text": "How does Spring Data JPA simplify database persistence? What is the difference between CrudRepository, JpaRepository, and custom @Query methods?",
        "expected_answer": "Spring Data JPA auto-generates implementation classes for repository interfaces using method name conventions (findByEmail). CrudRepository provides basic CRUD operations. JpaRepository extends PagingAndSortingRepository and CrudRepository, adding JPA-specific methods (flush, batch deletes). @Query allows defining custom JPQL or native SQL queries.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the N+1 select problem in Hibernate and how does @EntityGraph resolve it?",
        "code_snippet": "public interface UserRepository extends JpaRepository<User, Long> {\n    Optional<User> findByEmail(String email);\n    @Query(\"SELECT u FROM User u WHERE u.active = true\")\n    List<User> findAllActive();\n}"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "exception_handling",
        "difficulty": "easy",
        "question_text": "Explain the difference between Checked Exceptions (Exception) and Unchecked Exceptions (RuntimeException) in Java. Why have modern frameworks (Spring) adopted unchecked exceptions?",
        "expected_answer": "Checked exceptions (IOException, SQLException) inherit from Exception and must be either caught (try-catch) or declared in the method signature (throws), checked at compile-time. Unchecked exceptions (NullPointerException, IllegalArgumentException) inherit from RuntimeException and represent programming bugs, not checked at compile-time. Modern frameworks use unchecked exceptions to eliminate verbose boilerplate try-catch clutter.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does try-with-resources (AutoCloseable) automate resource cleanup?",
        "code_snippet": "try (BufferedReader br = new BufferedReader(new FileReader(file))) {\n    return br.readLine();\n}"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "spring_transactions",
        "difficulty": "hard",
        "question_text": "How does @Transactional work in Spring using Spring AOP proxies? Why does calling a @Transactional method from another method inside the same class bypass the transaction?",
        "expected_answer": "Spring creates a dynamic proxy wrapping the target bean. When an external caller invokes the method, the proxy intercepts the call, opens a transaction, delegates to the real method, and commits/rollbacks upon completion. Self-invocation (calling this.method() inside the same class) bypasses the proxy wrapper entirely, running directly on the raw instance without transactional interception.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What are Transaction Propagation options in Spring (REQUIRED, REQUIRES_NEW, SUPPORTS)?",
        "code_snippet": "@Transactional(rollbackFor = Exception.class)\npublic void transferFunds(Long from, Long to, BigDecimal amount) { ... }"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "thread_pools",
        "difficulty": "medium",
        "question_text": "Explain the parameters of ThreadPoolExecutor in Java: corePoolSize, maximumPoolSize, keepAliveTime, and workQueue (BlockingQueue). What happens when the queue is full?",
        "expected_answer": "Tasks are initially executed by up to corePoolSize threads. If all core threads are busy, incoming tasks are queued in workQueue. If the queue fills up to capacity, new threads are created up to maximumPoolSize. If maximumPoolSize is reached and queue is full, the RejectedExecutionHandler is triggered (AbortPolicy throws RejectedExecutionException, CallerRunsPolicy executes on calling thread).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is Executors.newFixedThreadPool() dangerous in production due to an unbounded LinkedBlockingQueue?",
        "code_snippet": "ExecutorService pool = new ThreadPoolExecutor(\n    4, 8, 60L, TimeUnit.SECONDS, new ArrayBlockingQueue<>(100)\n);"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "java_generics",
        "difficulty": "medium",
        "question_text": "Explain Type Erasure in Java Generics. What is the difference between upper-bounded wildcards (<? extends T>) and lower-bounded wildcards (<? super T>) (PECS rule)?",
        "expected_answer": "Type Erasure removes generic type parameters at compile-time, replacing them with Object (or bounds) and inserting necessary casts, maintaining backward compatibility with pre-Java 5 bytecode. PECS stands for Producer Extends, Consumer Super: use <? extends T> when reading from a collection (it produces Ts); use <? super T> when writing to a collection (it consumes Ts).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why can't you create generic arrays in Java (new T[10])?",
        "code_snippet": "public static <T> void copy(List<? super T> dest, List<? extends T> src) { ... }"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "virtual_threads_project_loom",
        "difficulty": "hard",
        "question_text": "What are Virtual Threads introduced in Java 21 (Project Loom)? How do they achieve high-throughput concurrency compared to traditional OS-backed platform threads?",
        "expected_answer": "Platform threads are 1:1 mapped to OS threads, requiring ~1MB of memory each and expensive OS context switches, limiting JVMs to a few thousand threads. Virtual Threads are lightweight user-mode threads managed entirely by the JVM (M:N mapped onto carrier platform threads). When a virtual thread blocks on I/O, the JVM unmounts it from the carrier thread and mounts another virtual thread, allowing millions of concurrent threads with standard synchronous code.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is 'pinning' in Virtual Threads and how does synchronized blocks trigger it?",
        "code_snippet": "Thread.startVirtualThread(() -> {\n    System.out.println(\"Running on lightweight virtual thread\");\n});"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "string_pool",
        "difficulty": "easy",
        "question_text": "Explain the String Constant Pool in Java. Why are Strings immutable, and how does String interning (s.intern()) work?",
        "expected_answer": "The String Pool is a specialized memory space in the Java Heap storing unique literal string instances. Immutability guarantees security (network sockets, database URLs), thread safety without synchronization, and allows string pool caching. Literal assignments reuse existing pool references; 'new String(\"abc\")' allocates a new heap object; s.intern() queries the pool, returning the pooled reference.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should you use StringBuilder instead of String concatenation (+) in large loops?",
        "code_snippet": "String s1 = \"hello\";\nString s2 = new String(\"hello\");\nSystem.out.println(s1 == s2); // false\nSystem.out.println(s1 == s2.intern()); // true"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "completable_future",
        "difficulty": "hard",
        "question_text": "Explain CompletableFuture in Java for asynchronous programming. How do thenApply(), thenCompose(), and thenCombine() differ?",
        "expected_answer": "CompletableFuture represents a future result that can be explicitly completed and chained asynchronously. thenApply() transforms the result synchronously (T -> U, like map). thenCompose() chains dependent futures where the function returns another CompletableFuture (T -> CompletableFuture<U>, like flatMap). thenCombine() executes two independent futures concurrently and combines their outputs via BiFunction.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is exceptionally() and handle() for async error recovery?",
        "code_snippet": "CompletableFuture.supplyAsync(() -> fetchOrder())\n    .thenCompose(order -> fetchPayment(order))\n    .thenAccept(receipt -> printReceipt(receipt));"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "spring_security",
        "difficulty": "hard",
        "question_text": "Explain the Spring Security Filter Chain architecture. How does it authenticate requests using SecurityContextHolder, AuthenticationManager, and OncePerRequestFilter?",
        "expected_answer": "Spring Security registers a DelegatingFilterProxy that routes requests through a chain of security filters (SecurityFilterChain). A custom JWT filter extends OncePerRequestFilter, extracts the Bearer token, validates signature, builds an Authentication object (UsernamePasswordAuthenticationToken), and populates SecurityContextHolder.getContext().setAuthentication(auth), enabling @PreAuthorize role checks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you configure stateless session management (SessionCreationPolicy.STATELESS)?",
        "code_snippet": ""
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "equals_and_hashcode",
        "difficulty": "easy",
        "question_text": "State the contract between equals() and hashCode() in Java. What happens in a HashSet if two objects evaluate to true on equals() but produce different hashCodes?",
        "expected_answer": "Contract: 1) If obj1.equals(obj2) is true, then obj1.hashCode() MUST equal obj2.hashCode(). 2) If hashCodes are equal, equals() is not required to be true (hash collision). If two equal objects have different hashCodes, a HashSet/HashMap computes different bucket indices, storing duplicate equal objects and failing to find existing items on contains().",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does Objects.hash(...) simplify implementing hashCode()?",
        "code_snippet": "@Override\npublic boolean equals(Object o) { ... }\n@Override\npublic int hashCode() { return Objects.hash(id, email); }"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "java_records",
        "difficulty": "easy",
        "question_text": "What are Java Records (introduced in Java 14+)? How do they eliminate Lombok boilerplate for immutable Data Transfer Objects (DTOs)?",
        "expected_answer": "A record (record UserDTO(Long id, String name) {}) is an immutable transparent carrier for shallowly immutable data. The compiler automatically generates: private final fields, a canonical constructor, accessor methods (id(), name()), equals(), hashCode(), and a clean toString(). They replace verbose POJO boilerplate and Lombok annotations (@Getter, @AllArgsConstructor).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Can a record extend another class in Java?",
        "code_snippet": "public record UserDTO(Long id, String name, String email) {\n    public UserDTO {\n        Objects.requireNonNull(email, \"Email required\");\n    }\n}"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "design_patterns_java",
        "difficulty": "medium",
        "question_text": "How do you implement the Builder pattern in Java? Why is it preferred over telescoping constructors when an entity has 8+ optional attributes?",
        "expected_answer": "Telescoping constructors (overloading constructors with 1, 2, 3... parameters) make code unreadable and error-prone when adjacent parameters share types. The Builder pattern uses a static inner Builder class with chained setter methods returning 'this' and a terminal .build() method that enforces cross-field validations before returning the immutable target object.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does Lombok's @Builder annotation automate this pattern?",
        "code_snippet": "User user = User.builder()\n    .firstName(\"Jane\")\n    .email(\"jane@example.com\")\n    .build();"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "spring_actuator_observability",
        "difficulty": "medium",
        "question_text": "What is Spring Boot Actuator? Explain endpoints like /actuator/health, /actuator/metrics, and how Micrometer integrates with Prometheus for production monitoring.",
        "expected_answer": "Spring Boot Actuator exposes production-ready operational endpoints (health, info, metrics, env, loggers) for monitoring application status. Health indicators check database, disk, and messaging connections. Micrometer acts as a dimensional metrics facade (like SLF4J for metrics), collecting JVM stats (heap, GC, thread count) and custom timers to export to Prometheus for Grafana dashboards.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should sensitive actuator endpoints be secured behind authentication in production?",
        "code_snippet": "management.endpoints.web.exposure.include=health,metrics,prometheus"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "class_loaders",
        "difficulty": "hard",
        "question_text": "Explain the Java ClassLoader hierarchy: Bootstrap ClassLoader, Platform/Extension ClassLoader, and Application/System ClassLoader. What is the Delegation-Parent Principle?",
        "expected_answer": "The ClassLoader hierarchy loads .class bytecode into JVM memory. The Delegation-Parent Principle states: when a ClassLoader receives a request to load a class, it first delegates the request to its parent ClassLoader before attempting to find the class itself. Only if the parent cannot find the class does the child ClassLoader search its own classpath, preventing security attacks where malicious code shadows core java.lang classes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do web containers (Tomcat) break parent delegation for webapp class loading?",
        "code_snippet": ""
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "java_io_vs_nio",
        "difficulty": "hard",
        "question_text": "Compare Java IO (InputStream/OutputStream) with Java NIO (Channels, Buffers, Selectors). How does NIO facilitate scalable non-blocking I/O (like Netty)?",
        "expected_answer": "Standard Java IO is stream-oriented and blocking: one thread reads bytes sequentially and blocks until bytes arrive (one thread per client). Java NIO is buffer-oriented and non-blocking: Channels transfer data to/from Buffers. A single Selector thread multiplexes and monitors multiple channels for ready events (OP_ACCEPT, OP_READ, OP_WRITE), enabling a single thread to service tens of thousands of active network connections.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between direct memory buffers (ByteBuffer.allocateDirect) and heap buffers?",
        "code_snippet": ""
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "sealed_classes",
        "difficulty": "medium",
        "question_text": "What are Sealed Classes in modern Java (Java 17+)? How do 'permits', pattern matching for switch, and exhaustive type checking work together?",
        "expected_answer": "Sealed classes (public sealed class Shape permits Circle, Square) restrict which other classes or interfaces can extend or implement them. Subclasses must be final, sealed, or non-sealed. When used with pattern matching for switch (Java 21), the compiler knows all possible subtypes and enforces exhaustiveness, eliminating the need for an otherwise unreachable 'default' branch.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do sealed classes implement Domain-Driven Design Algebraic Data Types (ADTs)?",
        "code_snippet": "public sealed interface PaymentMethod permits CreditCard, BankTransfer, PayPal {}\nreturn switch (payment) {\n    case CreditCard c -> processCard(c);\n    case BankTransfer b -> processBank(b);\n    case PayPal p -> processPayPal(p);\n};"
    },
    {
        "role": "Java Developer",
        "technology": "java",
        "category": "practical_coding_concurrency",
        "difficulty": "hard",
        "question_text": "Implement a thread-safe Bounded Blocking Queue in Java using wait() and notifyAll() (or ReentrantLock and Condition).",
        "expected_answer": "Candidate should demonstrate: a queue container, capacity limit, synchronized blocks or ReentrantLock with two Condition objects (notFull, notEmpty). put() waits while queue is full; take() waits while queue is empty; signal/notify after state modification. Always use while loops around wait/await to handle spurious wakeups.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why must wait() always be called inside a loop checking the condition rather than an if statement?",
        "code_snippet": "public synchronized void put(T item) throws InterruptedException {\n    while (queue.size() == capacity) {\n        wait();\n    }\n    queue.add(item);\n    notifyAll();\n}"
    }
]
