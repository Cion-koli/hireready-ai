"""
Python Developer Question Bank - 25 distinct technical questions.
Focuses on advanced Python architecture, web frameworks (Django/FastAPI), ORMs, testing, async, and APIs.
"""

PYTHON_DEVELOPER_QUESTIONS = [
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "language_features",
        "difficulty": "easy",
        "question_text": "How do generator functions and generator expressions differ from normal functions returning lists in Python, and when is generator streaming critical for large datasets?",
        "expected_answer": "Generators use 'yield' and produce values lazily on demand without holding the entire collection in RAM, maintaining constant memory O(1). Normal functions evaluate and allocate the full list in memory at once. Streaming is vital when reading multi-gigabyte log files or large SQL cursor sets.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you chain generators using itertools.chain?",
        "code_snippet": "def read_large_file(file_path):\n    with open(file_path, 'r') as f:\n        for line in f:\n            yield line.strip()"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "oop_design",
        "difficulty": "medium",
        "question_text": "What are dataclasses in Python (introduced in 3.7)? How do @dataclass(frozen=True) and field(default_factory=...) work compared to standard __init__ methods?",
        "expected_answer": "@dataclass automatically generates boilerplate special methods (__init__, __repr__, __eq__, __hash__). frozen=True makes the instances immutable and hashable (generating __hash__). default_factory=list ensures that mutable default collections are instantiated fresh per instance rather than shared.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do dataclasses compare to NamedTuple and Pydantic models?",
        "code_snippet": "from dataclasses import dataclass, field\n@dataclass(frozen=True)\nclass UserDTO:\n    id: int\n    roles: list = field(default_factory=list)"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "decorators",
        "difficulty": "medium",
        "question_text": "How do you write a parameterized decorator in Python that retries an API call up to N times with exponential backoff before re-raising the exception?",
        "expected_answer": "A parameterized decorator is a function returning a decorator function, which returns the wrapper. It catches specified exceptions in a loop up to max_retries, sleep with time.sleep(delay * (2 ** attempt)), and re-raises if attempts are exhausted.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why must functools.wraps be applied on the wrapper?",
        "code_snippet": "def retry(max_attempts=3, backoff=1):\n    def decorator(func):\n        @functools.wraps(func)\n        def wrapper(*args, **kwargs):\n            # retry logic with sleep\n            pass\n        return wrapper\n    return decorator"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "context_managers",
        "difficulty": "medium",
        "question_text": "How do you implement a custom Context Manager using contextlib.contextmanager? Explain what happens if an exception occurs inside the yield block.",
        "expected_answer": "Decorate a generator function with @contextmanager. Code before yield represents setup (__enter__); code after yield represents teardown (__exit__). If an exception occurs in the caller's with-block, it is re-raised inside the generator at the yield statement; therefore, wrapping yield in a try-finally ensures teardown executes safely.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you suppress specific exceptions inside a context manager using contextlib.suppress?",
        "code_snippet": "from contextlib import contextmanager\n@contextmanager\ndef db_session():\n    session = Session()\n    try:\n        yield session\n        session.commit()\n    except Exception:\n        session.rollback()\n        raise\n    finally:\n        session.close()"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "metaprogramming",
        "difficulty": "hard",
        "question_text": "What is a metaclass in Python, and how does __init_subclass__ in modern Python (3.6+) provide a simpler alternative for class registration and validation?",
        "expected_answer": "A metaclass is the 'class of a class' (subclass of type) that controls how classes are created, overriding __new__ or __init__ to intercept class creation. __init_subclass__ allows parent classes to automatically execute setup/validation logic whenever a child class inherits from them, without needing explicit metaclass machinery.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does type(name, bases, dict) dynamically generate classes at runtime?",
        "code_snippet": "class PluginBase:\n    registry = {}\n    def __init_subclass__(cls, plugin_name, **kwargs):\n        super().__init_subclass__(**kwargs)\n        cls.registry[plugin_name] = cls"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "concurrency",
        "difficulty": "hard",
        "question_text": "Compare threading, multiprocessing, and asyncio in Python. For a web scraper fetching 5,000 URLs versus an image processing batch job converting 5,000 photos, which concurrency model would you choose and why?",
        "expected_answer": "For web scraping (I/O-bound): asyncio (or a ThreadPoolExecutor) is best because threads/tasks yield while waiting on network sockets with minimal overhead and no GIL limitation. For image processing (CPU-bound): multiprocessing is necessary because separate OS processes bypass the GIL and utilize multiple physical CPU cores.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does concurrent.futures.ProcessPoolExecutor simplify multiprocessing?",
        "code_snippet": "from concurrent.futures import ProcessPoolExecutor\nwith ProcessPoolExecutor(max_workers=4) as executor:\n    results = list(executor.map(process_image, image_paths))"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "fastapi_pydantic",
        "difficulty": "medium",
        "question_text": "How does FastAPI leverage Python type hints and Pydantic models for automatic request validation, serialization, and OpenAPI documentation generation?",
        "expected_answer": "FastAPI inspects route parameter type annotations. Pydantic models define schemas; incoming JSON is automatically parsed, type-coerced, and validated against Pydantic field constraints, returning 422 Unprocessable Entity automatically on errors. Type annotations also auto-generate Swagger / ReDoc OpenAPI documentation.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do FastAPI Dependency Injection (Depends) and background tasks work?",
        "code_snippet": "from fastapi import FastAPI\nfrom pydantic import BaseModel, EmailStr\nclass UserCreate(BaseModel):\n    email: EmailStr\n    age: int"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "django_orm",
        "difficulty": "medium",
        "question_text": "Explain the 'N+1 query problem' in Django ORM. How do select_related() and prefetch_related() solve it, and what is the difference between them?",
        "expected_answer": "The N+1 problem occurs when fetching N records causes N additional SQL queries to fetch related foreign key data in a loop. select_related performs an SQL INNER/LEFT JOIN to fetch single-valued relationships (ForeignKey, OneToOne) in a single query. prefetch_related does a separate query with an IN clause for multi-valued relationships (ManyToMany, reverse ForeignKey) and joins them in Python memory.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can django-debug-toolbar or connection.queries be used to audit query counts?",
        "code_snippet": "# 1 query with SQL JOIN instead of N+1\nbooks = Book.objects.select_related('author').all()"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "testing_pytest",
        "difficulty": "easy",
        "question_text": "Why is pytest preferred over unittest in modern Python development? Explain pytest fixtures, parameterization (@pytest.mark.parametrize), and monkeypatching.",
        "expected_answer": "pytest uses standard Python asserts instead of self.assertEqual boilerplate. Fixtures (@pytest.fixture) provide modular, reusable, dependency-injected setup/teardown with yield syntax. @pytest.mark.parametrize runs the same test function against multiple input/output datasets cleanly. monkeypatch safely mocks environment variables, attributes, or functions.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is fixture scope (function, class, module, session)?",
        "code_snippet": "@pytest.mark.parametrize('val,expected', [(2, 4), (3, 9)])\ndef test_square(val, expected):\n    assert val ** 2 == expected"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "memory_optimization",
        "difficulty": "medium",
        "question_text": "What is the purpose of '__slots__' in Python classes? How does it reduce memory consumption and prevent dynamic attribute creation?",
        "expected_answer": "By default, Python instances store attributes in a dynamic dictionary (__dict__), which has high memory overhead. Specifying __slots__ = ('x', 'y') tells Python to allocate a fixed-size array of attribute references directly on the C struct, saving significant RAM when instantiating millions of small objects and preventing arbitrary attribute assignment.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What limitations exist when subclassing a class that uses __slots__?",
        "code_snippet": "class Point:\n    __slots__ = ('x', 'y')\n    def __init__(self, x, y):\n        self.x, self.y = x, y"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "typing_system",
        "difficulty": "medium",
        "question_text": "Explain Python's 'typing' module (Union, Optional, Any, Callable, TypeVar, Generic). How do static type checkers like mypy enhance code quality in production?",
        "expected_answer": "Type hints provide static documentation and contract checking without affecting runtime execution. mypy analyzes type hints before deployment, catching bugs (NoneType dereferences, wrong argument types, missing dict keys). TypeVar and Generic enable reusable generic classes and functions while preserving strict type safety.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is typing.Protocol (structural subtyping) in Python 3.8+?",
        "code_snippet": "from typing import TypeVar, Generic\nT = TypeVar('T')\nclass Stack(Generic[T]):\n    def push(self, item: T) -> None: pass"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "celery_async_tasks",
        "difficulty": "medium",
        "question_text": "How do you integrate Celery with Redis/RabbitMQ for background asynchronous job processing in a Python web application? How do you handle task failures and retries?",
        "expected_answer": "Celery offloads long-running tasks (emails, report generation, video processing) to worker processes. Redis or RabbitMQ acts as the message broker queue. Tasks are decorated with @app.task(bind=True, max_retries=3) and invoked using .delay() or .apply_async(). Errors are handled with self.retry(exc=e, countdown=60).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between a message broker and a result backend in Celery?",
        "code_snippet": "@celery_app.task(bind=True, max_retries=3)\ndef send_email_task(self, email):\n    try: api.send(email)\n    except Exception as e: raise self.retry(exc=e, countdown=30)"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "string_formatting",
        "difficulty": "easy",
        "question_text": "Compare % formatting, str.format(), and f-strings (formatted string literals) in Python. What advanced formatting capabilities do f-strings support in Python 3.8+ (e.g. f'{x=}')?",
        "expected_answer": "f-strings (f'...') evaluate expressions directly at runtime inside braces, offering superior readability and speed compared to legacy % and str.format(). In Python 3.8+, f'{x=}' prints both the variable name and its value for effortless debugging. f-strings also support decimal formatting (f'{val:.2f}') and datetime specs.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should f-strings never be used to construct raw SQL queries?",
        "code_snippet": "price = 49.956\nprint(f'{price=:.2f}') # price=49.96"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "security_practices",
        "difficulty": "hard",
        "question_text": "What is pickle serialization in Python, and why is unpickling untrusted user data a severe Remote Code Execution (RCE) vulnerability? What secure alternatives exist?",
        "expected_answer": "pickle serializes Python object graphs into bytecode. When deserializing (pickle.loads), it can execute arbitrary Python callables defined by the __reduce__ method on classes in the payload, allowing attackers to run arbitrary shell commands (os.system). Safe alternatives: JSON, Protocol Buffers, or MessagePack for untrusted data exchange.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do JWT tokens or signed cookies prevent payload tampering?",
        "code_snippet": ""
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "collections_module",
        "difficulty": "easy",
        "question_text": "Explain the practical utility of defaultdict, Counter, deque, and namedtuple from the Python standard 'collections' module.",
        "expected_answer": "defaultdict automatically initializes missing keys using a factory function (e.g. list, int), avoiding KeyError and manual checks. Counter tallies hashable elements and provides .most_common(N). deque is a double-ended queue offering O(1) appends and pops from both ends (unlike list with O(N) pop(0)). namedtuple creates lightweight tuple subclasses with named fields.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the time complexity of deque.popleft() versus list.pop(0)?",
        "code_snippet": "from collections import Counter, defaultdict\ncounts = Counter('abracadabra')\ngroups = defaultdict(list)"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "api_design",
        "difficulty": "medium",
        "question_text": "How do you implement pagination, filtering, and rate limiting in a Python REST API service?",
        "expected_answer": "Pagination: Limit/offset or cursor-based pagination (ideal for high-frequency writes to avoid page drift). Filtering: query parameters mapped to ORM filters (e.g. /items?status=active&min_price=10). Rate limiting: token bucket or sliding window algorithms implemented in Redis cache middleware by tracking client IP or API key request counts.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is keyset (cursor) pagination faster on large database tables than OFFSET 100000?",
        "code_snippet": ""
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "functional_itertools",
        "difficulty": "medium",
        "question_text": "Explain itertools functions in Python: chain(), islice(), groupby(), and product(). Why must data be pre-sorted before calling itertools.groupby()?",
        "expected_answer": "chain combines iterables sequentially; islice lazily slices an iterator without copying; product computes Cartesian products. groupby() groups consecutive keys from an iterable; if the iterable is not pre-sorted by the grouping key, it creates multiple duplicate groups whenever the key value changes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does itertools.cycle() create an infinite rotating loop over an iterable?",
        "code_snippet": "import itertools\ndata = sorted(['apple', 'avocado', 'banana', 'blueberry'])\nfor key, group in itertools.groupby(data, key=lambda x: x[0]):\n    print(key, list(group))"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "error_logging",
        "difficulty": "easy",
        "question_text": "How does Python's built-in 'logging' module work? Explain logger hierarchies, log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), and structured JSON logging.",
        "expected_answer": "Loggers are organized hierarchically using dot notation (logging.getLogger(__name__)). Messages propagate up to handlers (Console, File, Syslog) through Formatters and Filters. Log levels filter output severity. In production cloud environments, formatters output single-line JSON logs for automated ingestion by Datadog, Elastic, or CloudWatch.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should you use logger.exception('...') inside except blocks instead of logger.error()?",
        "code_snippet": "import logging\nlogger = logging.getLogger(__name__)\nlogging.basicConfig(level=logging.INFO)"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "descriptors",
        "difficulty": "hard",
        "question_text": "What is a Python Descriptor? Explain __get__, __set__, and __delete__. How do @property and ORM field definitions use descriptors under the hood?",
        "expected_answer": "A descriptor is any object defining at least one of __get__, __set__, or __delete__ in its class. When accessed as an attribute on another class instance, Python invokes the descriptor method. @property is a built-in descriptor. ORMs (Django, SQLAlchemy) define model fields as descriptors to intercept attribute access and handle database type mapping and dirty tracking.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between a Data Descriptor and a Non-Data Descriptor?",
        "code_snippet": "class PositiveInteger:\n    def __set_name__(self, owner, name): self.name = name\n    def __set__(self, instance, value):\n        if value < 0: raise ValueError('Must be positive')\n        instance.__dict__[self.name] = value"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "design_patterns",
        "difficulty": "medium",
        "question_text": "Demonstrate how to implement the Singleton pattern in Python using a module, a decorator, or __new__. Why is a Python module often considered the simplest Singleton?",
        "expected_answer": "In Python, modules are imported once and cached in sys.modules; subsequent imports reuse the same module namespace instance, making module-level objects natural singletons. In classes, overriding __new__ checks a private _instance class attribute and returns the cached instance if already initialized.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What thread-safety issues arise if multiple threads instantiate a singleton simultaneously?",
        "code_snippet": "class Singleton:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "environment_variables",
        "difficulty": "easy",
        "question_text": "How do you securely manage environment configuration in Python applications (e.g. python-dotenv, os.environ, pydantic-settings)?",
        "expected_answer": "Never hardcode API keys or secrets in source code. Use .env files for local development (loaded via python-dotenv) and real OS environment variables in production. Pydantic-settings provides strongly typed configuration classes that auto-load and type-check environment variables on application startup.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should .env always be in .gitignore?",
        "code_snippet": "from pydantic_settings import BaseSettings\nclass Settings(BaseSettings):\n    database_url: str\n    gemini_api_key: str"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "mocking_and_testing",
        "difficulty": "medium",
        "question_text": "How does unittest.mock (Mock, MagicMock, patch) work in Python tests? Explain how to mock an external HTTP request or database query in a unit test.",
        "expected_answer": "unittest.mock replaces real objects with Mock instances that record calls and return predetermined return_value or side_effect. The @patch('module.Class') decorator temporarily swaps the target object during test execution. It is crucial to patch where the object is *imported and used*, not where it is defined.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between Mock and MagicMock (support for magic methods)?",
        "code_snippet": "from unittest.mock import patch\n@patch('requests.get')\ndef test_fetch(mock_get):\n    mock_get.return_value.status_code = 200\n    mock_get.return_value.json.return_value = {'data': 123}"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "caching_strategies",
        "difficulty": "medium",
        "question_text": "How does functools.lru_cache work? When should you use Redis caching over in-memory Python caching for a multi-process or multi-server deployment?",
        "expected_answer": "@lru_cache caches function return values in an in-memory dictionary bounded by maxsize, evicting the least recently used keys. In multi-worker (Gunicorn) or multi-server architectures, in-memory caches are isolated per process, leading to cache duplication and stale data; an external centralized cache like Redis shares state across all workers and nodes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why can caching mutable objects with @lru_cache cause subtle state mutation bugs?",
        "code_snippet": "from functools import lru_cache\n@lru_cache(maxsize=1024)\ndef compute_expensive_hash(input_str: str) -> str:\n    return hashlib.sha256(input_str.encode()).hexdigest()"
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "web_servers_wsgi_asgi",
        "difficulty": "hard",
        "question_text": "Compare WSGI (Web Server Gateway Interface, e.g. Gunicorn/uWSGI) and ASGI (Asynchronous Server Gateway Interface, e.g. Uvicorn/Daphne). Why did the Python ecosystem evolve to ASGI?",
        "expected_answer": "WSGI is a synchronous protocol where each request blocks a worker thread until response completion, making it unsuitable for long-lived connections (WebSockets, HTTP/2, server-sent events). ASGI provides an asynchronous interface capable of handling async/await coroutines, enabling thousands of concurrent WebSockets and long-polling connections on a single worker process.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Can Django run under ASGI?",
        "code_snippet": ""
    },
    {
        "role": "Python Developer",
        "technology": "python",
        "category": "practical_debugging",
        "difficulty": "medium",
        "question_text": "How do you use the built-in 'pdb' / 'breakpoint()' debugger in Python? What are the key commands (n, s, c, q, p)?",
        "expected_answer": "Calling breakpoint() drops execution into an interactive Pdb session at that line. 'n' (next) steps to next line in current function; 's' (step) steps into called function; 'c' (continue) resumes until next breakpoint; 'p expr' prints expression; 'q' quits debugging session.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can PYTHONBREAKPOINT=0 be used to disable all breakpoints in production?",
        "code_snippet": "def calculate_discount(price, rate):\n    breakpoint() # drops into interactive debugger\n    return price * (1 - rate)"
    }
]
