"""
Software Engineer Question Bank - Python Technology
25 distinct technical questions covering fundamentals, OOP, memory, concurrency, and real-world scenarios.
"""

SOFTWARE_ENGINEER_PYTHON_QUESTIONS = [
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "variables_and_types",
        "difficulty": "easy",
        "question_text": "What are the primary built-in data types in Python, and how does Python's dynamic typing system determine variable types at runtime?",
        "expected_answer": "Python has int, float, complex, str, bool, list, tuple, range, dict, set, frozenset, and bytes. Python is dynamically typed, meaning variables hold references to objects and types are bound to the object rather than the variable name.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does dynamic typing impact performance compared to statically typed languages?",
        "code_snippet": "x = 42\nx = 'now a string'\nprint(type(x))"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "mutability",
        "difficulty": "easy",
        "question_text": "Explain the difference between mutable and immutable objects in Python. Give three examples of each and explain why passing a mutable default argument to a function can cause bugs.",
        "expected_answer": "Mutable objects (list, dict, set) can have their state modified in place without changing memory identity (id). Immutable objects (int, float, str, tuple, frozenset) cannot be changed once created. Mutable default arguments (e.g. def fn(x=[])) are evaluated once at function definition time, sharing the same object across calls.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the idiomatic pattern to avoid mutable default argument traps?",
        "code_snippet": "def append_item(val, target=None):\n    if target is None:\n        target = []\n    target.append(val)\n    return target"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "data_structures",
        "difficulty": "easy",
        "question_text": "Compare Python lists, tuples, sets, and dictionaries in terms of indexing, duplicate handling, ordering, and underlying hash table vs array implementations.",
        "expected_answer": "Lists are ordered, mutable, indexed, and allow duplicates (dynamic arrays). Tuples are ordered, immutable, indexed, and allow duplicates. Sets are unordered (or insertion-ordered in recent Python), mutable, unindexed, unique-only (hash table). Dicts store key-value pairs where keys must be hashable and unique.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the average time complexity for checking membership in a set versus a list?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "control_flow",
        "difficulty": "easy",
        "question_text": "How does the 'else' block behave when attached to a for loop or while loop in Python? When would you use it?",
        "expected_answer": "The else clause on a loop executes only if the loop completes normally without encountering a 'break' statement. It is commonly used in search loops where you break on finding an item and use else for the 'not found' fallback.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does this compare to try-except-else?",
        "code_snippet": "for item in items:\n    if condition(item):\n        break\nelse:\n    print('Not found')"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "functions",
        "difficulty": "easy",
        "question_text": "Explain the difference between positional arguments, keyword arguments, *args, and **kwargs in Python function definitions.",
        "expected_answer": "Positional arguments are matched by order. Keyword arguments are matched by parameter name. *args captures arbitrary positional arguments as a tuple. **kwargs captures arbitrary keyword arguments as a dictionary.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do keyword-only arguments work using a bare asterisk (*) in parameter definitions?",
        "code_snippet": "def log_event(event_name, *tags, **metadata):\n    pass"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "comprehensions",
        "difficulty": "easy",
        "question_text": "Write and explain a list comprehension that filters a list of integers to find all even numbers squared. How does a list comprehension differ from a generator expression in memory usage?",
        "expected_answer": "List comprehension [x**2 for x in nums if x % 2 == 0] builds the complete list in memory immediately. A generator expression (x**2 for x in nums if x % 2 == 0) produces values lazily one at a time via iterator protocol, using constant O(1) auxiliary memory.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "When would you prefer a list comprehension over a generator?",
        "code_snippet": "nums = [1, 2, 3, 4, 5, 6]\nsquared_evens = [x**2 for x in nums if x % 2 == 0]"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "exception_handling",
        "difficulty": "medium",
        "question_text": "Explain how try, except, else, and finally blocks interact during exception handling in Python. When does the finally block execute if a return statement is inside try?",
        "expected_answer": "try contains code that might raise; except catches specific errors; else runs only if no exception occurred; finally runs unconditionally regardless of whether an exception was raised, caught, or even if return/break/continue was executed. A return in finally overrides any return in try.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is using a bare 'except:' considered an antipattern in Python?",
        "code_snippet": "try:\n    f = open('data.txt')\nexcept FileNotFoundError as e:\n    logger.error(e)\nelse:\n    process(f)\nfinally:\n    cleanup()"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "file_handling",
        "difficulty": "easy",
        "question_text": "Why is the 'with' statement recommended for file I/O in Python, and how does it relate to Context Managers and the __enter__ and __exit__ methods?",
        "expected_answer": "'with' ensures that resources are automatically and safely closed even if exceptions occur. It invokes the context manager protocol: __enter__() is called before block execution, and __exit__(exc_type, exc_val, exc_tb) is guaranteed to execute upon exit, closing file descriptors.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can you create a custom context manager using contextlib.contextmanager?",
        "code_snippet": "with open('config.json', 'r') as f:\n    data = json.load(f)"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "modules_and_packages",
        "difficulty": "medium",
        "question_text": "What is the purpose of the __init__.py file in Python packages? How does Python resolve import paths using sys.path and PYTHONPATH?",
        "expected_answer": "__init__.py marks a directory as an importable Python package and can initialize package-level namespace and __all__. Python searches modules in order: current script directory, directories in PYTHONPATH environment variable, standard library, and installed site-packages (all listed in sys.path).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between relative imports (.module) and absolute imports?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "oop_basics",
        "difficulty": "medium",
        "question_text": "Explain the difference between class attributes and instance attributes in Python. What happens when an instance modifies an attribute that has the same name as a class attribute?",
        "expected_answer": "Class attributes belong to the class definition and are shared across all instances. Instance attributes are tied to self within individual objects. When an instance assigns to self.attr where attr exists on the class, Python creates a new instance-level attribute shadowing the class attribute without altering the class attribute for other instances.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do __slots__ affect instance attribute allocation in memory?",
        "code_snippet": "class Service:\n    timeout = 30 # class attribute\n    def __init__(self, name):\n        self.name = name # instance attribute"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "oop_inheritance",
        "difficulty": "medium",
        "question_text": "How does multiple inheritance work in Python, and what is Method Resolution Order (MRO)? How does the C3 Linearization algorithm prevent ambiguous diamond inheritance?",
        "expected_answer": "Python supports multiple inheritance where a subclass inherits from multiple base classes. MRO dictates the order in which Python traverses classes to resolve methods. Python uses C3 Linearization to guarantee that children precede parents and the order of declared bases is preserved, accessible via ClassName.mro() or ClassName.__mro__.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the role of super() in cooperative multiple inheritance?",
        "code_snippet": "class A: pass\nclass B(A): pass\nclass C(A): pass\nclass D(B, C): pass\nprint(D.mro())"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "oop_encapsulation",
        "difficulty": "medium",
        "question_text": "How does Python handle encapsulation and private attributes? Explain the difference between single underscore (_var) and double underscore (__var) name mangling.",
        "expected_answer": "Python doesn't enforce strict access specifiers. Single underscore (_var) is a PEP 8 convention indicating protected/internal use. Double underscore (__var) triggers name mangling, where the interpreter renames it to _ClassName__var to avoid naming collisions in subclasses.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do @property decorators provide getters, setters, and deleter encapsulation?",
        "code_snippet": "class Account:\n    def __init__(self, balance):\n        self.__balance = balance"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "oop_polymorphism",
        "difficulty": "medium",
        "question_text": "Explain duck typing in Python ('If it walks like a duck and quacks like a duck, it's a duck'). How does it differ from abstract base classes (abc.ABC)?",
        "expected_answer": "Duck typing is dynamic polymorphism: Python does not check an object's formal inheritance hierarchy; rather, it attempts to access methods/attributes and succeeds if the object supports them. ABCs from the 'abc' module allow defining formal interfaces with @abstractmethod for explicit contract validation at instantiation time.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "When would you prefer ABCs over pure duck typing in large engineering codebases?",
        "code_snippet": "from abc import ABC, abstractmethod\nclass Notifier(ABC):\n    @abstractmethod\n    def send(self, msg: str): pass"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "generators",
        "difficulty": "medium",
        "question_text": "Explain how the 'yield' statement works in Python. What is the iterator protocol, and how do __iter__ and __next__ facilitate streaming data pipelines?",
        "expected_answer": "'yield' pauses a function's execution and saves its state, returning an iterator. The iterator protocol requires __iter__() returning self and __next__() returning the next item or raising StopIteration. Generators enable memory-efficient streaming of huge files or infinite sequences.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is 'yield from' and how is it used to delegate to sub-generators?",
        "code_snippet": "def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "decorators",
        "difficulty": "hard",
        "question_text": "Explain how Python decorators work under the hood. Write a decorator that measures and logs the execution time of any function, preserving the original function's docstring and metadata using functools.wraps.",
        "expected_answer": "Decorators are callables that accept a function and return an altered wrapper function. Using @functools.wraps(fn) copies metadata (name, docstring, annotations). Execution time can be measured using time.perf_counter() before and after calling the wrapped function.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you implement a decorator that takes arguments (e.g. @retry(times=3))?",
        "code_snippet": "import time, functools\ndef timing_decorator(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.perf_counter()\n        result = func(*args, **kwargs)\n        print(f'{func.__name__} took {time.perf_counter() - start:.4f}s')\n        return result\n    return wrapper"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "lambda_functions",
        "difficulty": "easy",
        "question_text": "What are lambda functions in Python, what limitations do they have compared to standard functions defined with def, and where are they most appropriately used?",
        "expected_answer": "Lambda functions are small anonymous single-expression functions: lambda arguments: expression. They cannot contain statements, assignments, loops, or complex annotations. They are typically used for short throwaway callables in sorting keys (sorted(items, key=lambda x: x[1])) or functional helpers (map/filter).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does PEP 8 advise against binding lambda to a variable name (e.g. f = lambda x: x+1)?",
        "code_snippet": "users = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]\nusers_sorted = sorted(users, key=lambda u: u['age'])"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "scope_and_namespaces",
        "difficulty": "medium",
        "question_text": "Explain the LEGB rule for Python variable scope resolution. How do the 'global' and 'nonlocal' keywords alter variable bindings inside nested functions?",
        "expected_answer": "LEGB: Local -> Enclosing (nested functions) -> Global (module level) -> Built-in. 'global var' forces binding to the module scope. 'nonlocal var' binds to the nearest enclosing non-global scope, essential for stateful closures.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is an UnboundLocalError and why does it happen when you assign to a variable without global/nonlocal?",
        "code_snippet": "def outer():\n    count = 0\n    def inner():\n        nonlocal count\n        count += 1\n        return count\n    return inner"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "copying",
        "difficulty": "medium",
        "question_text": "Explain the difference between assignment (=), shallow copy (copy.copy), and deep copy (copy.deepcopy) for nested lists or dictionaries.",
        "expected_answer": "Assignment merely creates a new reference pointing to the existing object. Shallow copy creates a new outer container, but inserts references to the original child objects. Deep copy recursively creates copies of all nested objects so modifications to child elements do not affect the original.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do circular references get handled by deepcopy?",
        "code_snippet": "import copy\noriginal = [[1, 2], [3, 4]]\nshallow = copy.copy(original)\ndeep = copy.deepcopy(original)"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "builtins",
        "difficulty": "easy",
        "question_text": "Explain the practical use cases for zip(), enumerate(), any(), and all() in Python with short code examples.",
        "expected_answer": "enumerate() yields (index, item) pairs avoiding manual counter tracking. zip() aggregates elements from multiple iterables element-wise. any() returns True if at least one item is truthy; all() returns True if all items are truthy.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What happens if iterables passed to zip() have differing lengths in Python 3.10+ (strict=True)?",
        "code_snippet": "names = ['Alice', 'Bob']\nscores = [95, 88]\nfor i, (name, score) in enumerate(zip(names, scores)):\n    print(i, name, score)"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "memory_management",
        "difficulty": "hard",
        "question_text": "How does CPython manage memory? Explain reference counting and the cyclic garbage collector (gc module with generational collection).",
        "expected_answer": "CPython uses reference counting as its primary memory mechanism: every object stores ob_refcnt; when it reaches 0, memory is deallocated immediately. To handle reference cycles (e.g. A references B and B references A), Python uses a cyclic garbage collector organized into three generations (Gen 0, 1, 2) that detects unreachable reference cycles via periodic pointer traversal.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does weakref allow referencing objects without incrementing their reference count?",
        "code_snippet": "import gc, sys\nx = []\nx.append(x) # cycle\ndel x\ngc.collect()"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "concurrency_and_gil",
        "difficulty": "hard",
        "question_text": "What is the Global Interpreter Lock (GIL) in CPython, why does it exist, and how does it affect CPU-bound multithreading versus I/O-bound concurrency? What are the alternatives?",
        "expected_answer": "The GIL is a mutex preventing multiple native threads from executing Python bytecode simultaneously, preserving thread safety in CPython's memory management. For CPU-bound tasks, multithreading does not provide multi-core speedup; multiprocessing or C-extensions are needed. For I/O-bound tasks, threads release the GIL during network/disk wait, making threading and asyncio highly effective.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the status of free-threaded (no-GIL) Python in Python 3.13?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "asyncio",
        "difficulty": "hard",
        "question_text": "Explain the event loop and coroutines in Python asyncio. What is the difference between asyncio.gather() and asyncio.wait()?",
        "expected_answer": "An event loop runs cooperative multitasking by managing tasks and I/O polling. Coroutines are declared with async def and paused at await points, yielding control back to the event loop. asyncio.gather() runs multiple awaitables concurrently and aggregates their results, raising or returning exceptions together. asyncio.wait() offers finer-grained completion controls (FIRST_COMPLETED, ALL_COMPLETED).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should you never call time.sleep() inside an async coroutine?",
        "code_snippet": "import asyncio\nasync def fetch_data(id):\n    await asyncio.sleep(1)\n    return f'data {id}'\n\nasync def main():\n    results = await asyncio.gather(*(fetch_data(i) for i in range(5)))"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "packaging_and_tooling",
        "difficulty": "medium",
        "question_text": "How do virtual environments work in Python? Compare requirements.txt with modern dependency lock files (poetry.lock, pipenv, or pyproject.toml with uv).",
        "expected_answer": "Virtual environments isolate package dependencies per project by modifying the PATH and sys.prefix to point to a local directory with its own python binary and site-packages. A flat requirements.txt often lacks exact sub-dependency version hashes; modern tools use pyproject.toml and lockfiles to guarantee deterministic, reproducible builds with resolved dependency graphs.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between pip freeze and pip list?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "magic_methods",
        "difficulty": "medium",
        "question_text": "Explain dunder (magic) methods in Python. What is the difference between __str__ and __repr__, and how do __eq__ and __hash__ work together when placing objects in sets or dict keys?",
        "expected_answer": "__repr__ is intended for developers/debugging (unambiguous, ideally reproducible with eval). __str__ is for end-user readability. If a class defines __eq__, __hash__ is set to None by default unless explicitly implemented; for an object to be usable as a dict key or set item, its hash must not change across its lifetime, meaning it must be immutable.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do __getitem__, __setitem__, and __len__ allow a class to act like a collection?",
        "code_snippet": "class Point:\n    def __init__(self, x, y): self.x, self.y = x, y\n    def __repr__(self): return f'Point({self.x}, {self.y})'\n    def __eq__(self, other): return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)\n    def __hash__(self): return hash((self.x, self.y))"
    },
    {
        "role": "Software Engineer",
        "technology": "python",
        "category": "debugging_and_profiling",
        "difficulty": "hard",
        "question_text": "How do you diagnose and debug a production memory leak or CPU spike in a Python backend service? Name the tools and profiling methods you would use.",
        "expected_answer": "To diagnose CPU spikes: cProfile, py-spy (sampling profiler), or yappi. For memory leaks: tracemalloc (identifying memory allocation line numbers), objgraph (visualizing object reference graphs and lingering types), and inspecting the gc module (gc.get_objects()). Verify if uncollected closures, global caches (lru_cache without maxsize), or circular references are growing.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can @lru_cache cause a silent memory leak if used carelessly?",
        "code_snippet": "import tracemalloc\ntracemalloc.start()\n# code to test\nsnapshot = tracemalloc.take_snapshot()\nfor stat in snapshot.statistics('lineno')[:5]:\n    print(stat)"
    }
]
