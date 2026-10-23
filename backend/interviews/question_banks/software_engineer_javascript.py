"""
Software Engineer Question Bank - JavaScript Technology
25 distinct technical questions covering fundamentals, ES6+, closures, event loop, async, and DOM.
"""

SOFTWARE_ENGINEER_JAVASCRIPT_QUESTIONS = [
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "variable_declarations",
        "difficulty": "easy",
        "question_text": "Explain the differences between var, let, and const in JavaScript regarding scoping (function vs block), hoisting, and the Temporal Dead Zone (TDZ).",
        "expected_answer": "var is function-scoped (or global), hoisted with default initialization to undefined, and allows re-declaration. let and const are block-scoped ({ }), hoisted but uninitialized in the Temporal Dead Zone (TDZ) until their declaration line is evaluated, throwing ReferenceError if accessed early. const cannot be reassigned (though objects bound to it remain mutable).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does freezing an object with Object.freeze() differ from declaring it with const?",
        "code_snippet": "console.log(a); // undefined\nvar a = 10;\nconsole.log(b); // ReferenceError: TDZ\nlet b = 20;"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "types_and_equality",
        "difficulty": "easy",
        "question_text": "Explain the difference between loose equality (==) and strict equality (===) in JavaScript. What is type coercion, and why does '[] == ![]' evaluate to true?",
        "expected_answer": "=== (strict equality) checks both value and type without type conversion. == (loose equality) converts operands to a common type via abstract equality comparison algorithm before comparing. ![] coerces truthy array [] to false -> [] == false -> [] coerces to '' -> '' == 0 -> 0 == 0 -> true.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does Object.is() differ from === regarding NaN and -0/+0?",
        "code_snippet": "console.log(0 == '0');  // true\nconsole.log(0 === '0'); // false\nconsole.log(null == undefined);  // true\nconsole.log(null === undefined); // false"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "primitives_vs_references",
        "difficulty": "easy",
        "question_text": "Distinguish between primitive types and reference types in JavaScript. What are all the 7 primitive types in modern ECMAScript?",
        "expected_answer": "7 primitive types: string, number, bigint, boolean, undefined, symbol, and null. Primitives are immutable and stored by value directly on the call stack. Reference types (Object, Array, Function, Map, Set) are mutable and stored in the heap; variables hold a reference pointer to their memory address.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does 'typeof null' return 'object'?",
        "code_snippet": "let x = { val: 10 };\nlet y = x;\ny.val = 20;\nconsole.log(x.val); // 20"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "closures",
        "difficulty": "medium",
        "question_text": "What is a Closure in JavaScript, how does it relate to lexical scoping, and what are practical real-world applications (e.g. data privacy / factory functions)?",
        "expected_answer": "A closure is the combination of a function bundled together with references to its surrounding state (lexical environment). In JavaScript, every inner function retains access to variables in its outer enclosing scope even after the outer function has completed execution. Uses: private variables, memoization, event handlers, and currying.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can closures accidentally cause memory leaks if lingering references prevent garbage collection?",
        "code_snippet": "function createCounter() {\n  let count = 0;\n  return {\n    increment: () => ++count,\n    get: () => count\n  };\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "this_keyword",
        "difficulty": "medium",
        "question_text": "Explain how the 'this' keyword is bound in JavaScript across: 1) global context, 2) object method, 3) explicit binding (call/apply/bind), 4) constructor (new), and 5) arrow functions.",
        "expected_answer": "1) Global: window/global (or undefined in strict mode). 2) Method: the object before the dot (obj.method()). 3) Explicit: call/apply invoke immediately with specified this context (apply takes array); bind returns a new function with bound this. 4) new: freshly allocated instance. 5) Arrow functions do NOT have their own 'this'; they lexically retain 'this' from their enclosing scope.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does passing an object method as a callback (e.g. setTimeout(obj.sayHi, 1000)) lose its original 'this'?",
        "code_snippet": "const person = {\n  name: 'Alex',\n  greet: function() {\n    setTimeout(() => console.log(this.name), 100);\n  }\n};\nperson.greet(); // Alex"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "higher_order_array_methods",
        "difficulty": "medium",
        "question_text": "Compare map(), filter(), and reduce() array methods. Write a reduce() pipeline that takes an array of transaction objects and groups the sum of amounts by category.",
        "expected_answer": "map() returns a new array with results of calling a function on every element. filter() returns a new array with elements satisfying a condition. reduce() accumulates elements down to a single value (number, object, array). Grouping pipeline uses an initial accumulator object: acc[tx.category] = (acc[tx.category] || 0) + tx.amount; return acc.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does forEach() not return a value, and can you break out of a forEach() loop early?",
        "code_snippet": "const transactions = [\n  { category: 'Food', amount: 20 },\n  { category: 'Tech', amount: 50 },\n  { category: 'Food', amount: 15 }\n];\nconst totals = transactions.reduce((acc, { category, amount }) => {\n  acc[category] = (acc[category] || 0) + amount;\n  return acc;\n}, {});"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "event_loop",
        "difficulty": "hard",
        "question_text": "Explain the JavaScript Event Loop, Call Stack, Microtask Queue (Promises, queueMicrotask), and Macrotask Queue (setTimeout, setInterval, I/O). In what order are they processed?",
        "expected_answer": "JavaScript is single-threaded with a Call Stack. Synchronous code runs first. When the call stack empties: 1) The engine drains the entire Microtask Queue (resolved Promise callbacks, queueMicrotask, MutationObserver) until empty before rendering. 2) The engine takes ONE macrotask from the Task Queue (setTimeout callback, UI event) and executes it, then drains all new microtasks again before checking the next macrotask.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the output order: console.log(1); setTimeout(() => console.log(2), 0); Promise.resolve().then(() => console.log(3)); console.log(4);?",
        "code_snippet": "console.log('1');\nsetTimeout(() => console.log('2'), 0);\nPromise.resolve().then(() => console.log('3'));\nconsole.log('4');\n// Output: 1, 4, 3, 2"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "promises",
        "difficulty": "medium",
        "question_text": "What are the three states of a JavaScript Promise? Compare Promise.all(), Promise.allSettled(), Promise.race(), and Promise.any().",
        "expected_answer": "States: pending, fulfilled, rejected. Promise.all() waits for all to fulfill, rejects immediately if ANY reject. Promise.allSettled() waits for all to complete regardless of outcome, returning array of status objects ({status: 'fulfilled'|'rejected'}). Promise.race() settles as soon as the first promise settles (fulfills or rejects). Promise.any() resolves as soon as the first promise fulfills, rejecting only if all reject.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle unhandled promise rejections in Node.js vs the browser?",
        "code_snippet": "Promise.allSettled([\n  fetch('/api/users'),\n  fetch('/api/posts')\n]).then(results => console.log(results));"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "async_await",
        "difficulty": "medium",
        "question_text": "How does 'async/await' syntactic sugar work on top of Promises? How do you implement robust error handling with try/catch and avoid sequential execution waterfalls?",
        "expected_answer": "async functions always return a Promise; 'await' pauses coroutine execution until the awaited Promise settles. Error handling is done with try/catch blocks wrapping the await. To avoid sequential waterfalls when tasks are independent, initiate promises concurrently first, then await them together (e.g. const [u, p] = await Promise.all([fetchU(), fetchP()])).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What happens if you await a non-promise value (e.g. await 42)?",
        "code_snippet": "async function loadData() {\n  try {\n    const res = await fetch('/api/data');\n    if (!res.ok) throw new Error(`HTTP ${res.status}`);\n    return await res.json();\n  } catch (err) {\n    logger.error(err);\n  }\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "event_propagation",
        "difficulty": "medium",
        "question_text": "Explain Event Propagation in the DOM: Capturing Phase, Target Phase, and Bubbling Phase. What is Event Delegation and why is it memory-efficient for dynamic lists?",
        "expected_answer": "Capturing travels down from window -> document -> target. Target phase triggers on target. Bubbling bubbles back up target -> document -> window. Event Delegation attaches a single listener to a common parent instead of hundreds on children; using event.target, the parent inspects and handles events bubbling up from dynamic or newly inserted child elements, saving memory.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between event.stopPropagation() and event.preventDefault()?",
        "code_snippet": "document.getElementById('todo-list').addEventListener('click', (e) => {\n  if (e.target.matches('.delete-btn')) {\n    e.target.closest('li').remove();\n  }\n});"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "prototypal_inheritance",
        "difficulty": "hard",
        "question_text": "Explain how Prototypal Inheritance and the Prototype Chain work in JavaScript. How does the ES6 'class' keyword map to functions and prototypes under the hood?",
        "expected_answer": "Every JavaScript object has an internal [[Prototype]] link (__proto__) pointing to its prototype object. When an attribute or method is accessed, the engine traverses the prototype chain until found or reaching null (Object.prototype.__proto__ === null). ES6 classes are syntactic sugar over constructor functions and prototype method assignment (ClassName.prototype.method).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between an object's '__proto__' and a function's 'prototype' property?",
        "code_snippet": "function Animal(name) { this.name = name; }\nAnimal.prototype.speak = function() { return `${this.name} speaks`; };\nconst dog = new Animal('Buddy');"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "debounce_and_throttle",
        "difficulty": "hard",
        "question_text": "What is the difference between Debouncing and Throttling? Write a reusable debounce function from scratch in JavaScript.",
        "expected_answer": "Debounce delays execution until after a specified quiet period has elapsed since the last event (e.g. search autocomplete, window resize). Throttle guarantees execution at most once per specified time window (e.g. infinite scroll, game loop). Implementation uses setTimeout and clearTimeout.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you add an 'immediate/leading' execution option to a debounce function?",
        "code_snippet": "function debounce(fn, delay) {\n  let timerId;\n  return function(...args) {\n    clearTimeout(timerId);\n    timerId = setTimeout(() => fn.apply(this, args), delay);\n  };\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "destructuring_spread",
        "difficulty": "easy",
        "question_text": "Explain ES6 Object and Array Destructuring with default values and renaming. How does the rest parameter (...) differ from the spread operator (...) in usage?",
        "expected_answer": "Destructuring unpacks values from arrays or properties from objects into distinct variables, supporting defaults ({ name = 'Guest' }) and renaming ({ name: userName }). The spread operator expands an iterable into individual elements (in array literals, object clones, or function calls). The rest parameter gathers multiple remaining elements into a single array.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Does object spread ({ ...obj }) perform a shallow or deep copy?",
        "code_snippet": "const user = { id: 1, profile: { name: 'Alex' } };\nconst { id, profile: { name } } = user;\nconst cloned = { ...user, role: 'Admin' };"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "modules",
        "difficulty": "medium",
        "question_text": "Compare CommonJS (require/module.exports) and ES Modules (import/export). What advantages does ESM have regarding static analysis and tree-shaking?",
        "expected_answer": "CommonJS is synchronous, dynamically loaded at runtime, and loads copies of primitives (standard in legacy Node.js). ESM is asynchronous, statically parsed at compile time before execution, and imports live bindings. Static structure allows bundlers (Vite, Rollup, Webpack) to perform dead code elimination (tree-shaking) by dropping unused exports.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is dynamic import() and when would you use it for code splitting?",
        "code_snippet": "// ESM named and default export\nexport const helper = () => {};\nexport default class Service {}"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "json_serialization",
        "difficulty": "medium",
        "question_text": "How do JSON.stringify() and JSON.parse() work in JavaScript? What data types are lost or stripped during JSON.stringify, and what is the 'replacer' and 'reviver' argument?",
        "expected_answer": "JSON.stringify converts JS objects to JSON strings; it omits Functions, Symbols, and undefined properties in objects (or converts them to null in arrays), and converts Date to ISO string. A replacer function filters or transforms values during serialization; a reviver function transforms parsed values back (e.g. converting date strings back to Date objects).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does JSON.stringify fail with a TypeError if an object has circular references?",
        "code_snippet": "const jsonStr = JSON.stringify(data, (key, value) => {\n  return typeof value === 'bigint' ? value.toString() : value;\n});"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "dom_manipulation",
        "difficulty": "easy",
        "question_text": "Compare querySelector() vs getElementById() and querySelectorAll() vs getElementsByClassName(). What is the difference between a static NodeList and a live HTMLCollection?",
        "expected_answer": "getElementById and getElementsByClassName take literal names and are faster; getElementsByClassName returns a live HTMLCollection that automatically updates when DOM changes. querySelector and querySelectorAll accept arbitrary CSS selectors; querySelectorAll returns a static NodeList that does not update when DOM changes, but supports array-like forEach().",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you convert a NodeList or HTMLCollection into a real array?",
        "code_snippet": "const activeItems = Array.from(document.querySelectorAll('.item.active'));"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "memory_leaks",
        "difficulty": "hard",
        "question_text": "What are common causes of client-side JavaScript memory leaks in Single Page Applications (SPAs), and how can you diagnose them in Chrome DevTools?",
        "expected_answer": "Causes: 1) Lingering global variables (accidental window attachments); 2) Uncleared setInterval or setTimeout timers; 3) Forgotten DOM event listeners or observers (ResizeObserver, IntersectionObserver) on unmounted components; 4) Closures retaining large parent variables; 5) Detached DOM nodes referenced in JS. Diagnosed using Chrome DevTools Memory Heap Snapshots and Allocation Timelines.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do WeakMap and WeakSet prevent memory leaks by allowing garbage collection of keys?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "web_workers",
        "difficulty": "hard",
        "question_text": "What are Web Workers in JavaScript? How do they enable multithreaded processing in browser applications, and how do they communicate with the main UI thread?",
        "expected_answer": "Web Workers run scripts in background threads separate from the main UI execution thread, allowing heavy CPU tasks (image processing, data crunching) to execute without freezing or dropping frames on the UI. They communicate with the main thread asynchronously via postMessage() and onmessage event handlers using structured clone algorithms or Transferable Objects (ArrayBuffer).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why cannot Web Workers access the DOM or window object directly?",
        "code_snippet": "const worker = new Worker('worker.js');\nworker.postMessage({ data: largeBuffer });\nworker.onmessage = (e) => console.log(e.data);"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "set_and_map",
        "difficulty": "easy",
        "question_text": "Explain Map and Set data structures introduced in ES6. Why is a Map preferred over an Object when keys are dynamic or non-string types?",
        "expected_answer": "Set stores unique values of any type. Map stores key-value pairs where keys can be any type (including objects, functions, numbers, not just strings/symbols). Unlike plain Objects, Map guarantees insertion order iteration, has an O(1) .size property, performs better in frequent addition/deletion scenarios, and avoids default prototype key pollution.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you easily remove duplicate elements from an array using Set?",
        "code_snippet": "const unique = [...new Set([1, 2, 2, 3, 4, 4])]; // [1, 2, 3, 4]"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "error_handling",
        "difficulty": "medium",
        "question_text": "How do you create a custom Error class in JavaScript inheriting from Error? Why should Error.captureStackTrace() be used?",
        "expected_answer": "Create a subclass using 'class CustomError extends Error'. Call super(message) to initialize standard message, set this.name = 'CustomError', and attach custom status codes. Error.captureStackTrace(this, CustomError) creates a clean .stack trace property pointing to where the error occurred while omitting implementation constructor frames.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the 'cause' property in modern Error constructors (new Error(msg, { cause: err }))?",
        "code_snippet": "class NotFoundError extends Error {\n  constructor(message) {\n    super(message);\n    this.name = 'NotFoundError';\n    this.statusCode = 404;\n  }\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "generators_and_iterators",
        "difficulty": "hard",
        "question_text": "Explain Generator functions (function*) and the yield keyword in JavaScript. What is the Symbol.iterator well-known symbol?",
        "expected_answer": "A generator function (function*) returns a Generator object adhering to both iterable and iterator protocols. It executes lazily, pausing at 'yield' expressions and resuming when .next(val) is invoked. Symbol.iterator is the well-known symbol that defines the default iterator for an object, allowing custom objects to be iterated using for...of or spread syntax.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is an asynchronous generator (async function*) and for await...of loop?",
        "code_snippet": "function* idMaker() {\n  let id = 1;\n  while (true) yield id++;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "currying_and_composition",
        "difficulty": "hard",
        "question_text": "What is Function Currying in JavaScript, and how do higher-order functions enable functional composition?",
        "expected_answer": "Currying transforms a function with multiple arguments f(a, b, c) into a sequence of unary functions f(a)(b)(c). It relies on closures to retain earlier arguments. Function composition combines two or more functions (compose(f, g)(x) = f(g(x))) so the output of one function becomes the input of the next, building clean data transformation pipelines.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you write a pipe() function that evaluates functions left-to-right using reduce?",
        "code_snippet": "const curryMultiply = a => b => a * b;\nconst double = curryMultiply(2);\nconsole.log(double(5)); // 10"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "proxy_and_reflect",
        "difficulty": "hard",
        "question_text": "What are Proxy and Reflect objects in JavaScript? How do reactive frontend frameworks (like Vue 3) use Proxies to track state changes and trigger UI updates?",
        "expected_answer": "A Proxy wraps a target object and intercepts fundamental operations via traps (get, set, deleteProperty, has). Reflect provides default forwarding methods matching each trap signature. Reactive frameworks wrap state in Proxies: the 'get' trap tracks dependencies (which component accessed the property), and the 'set' trap intercepts mutations to trigger re-renders.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why cannot plain Object.defineProperty intercept newly added properties or array length changes cleanly?",
        "code_snippet": "const state = new Proxy({ count: 0 }, {\n  get(target, prop, receiver) {\n    return Reflect.get(target, prop, receiver);\n  },\n  set(target, prop, value, receiver) {\n    console.log(`Prop ${prop} updated to ${value}`);\n    return Reflect.set(target, prop, value, receiver);\n  }\n});"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "optional_chaining_nullish",
        "difficulty": "easy",
        "question_text": "Explain Optional Chaining (?.) and the Nullish Coalescing Operator (??) in modern JavaScript. How does (a ?? b) differ from (a || b)?",
        "expected_answer": "Optional Chaining (?.) short-circuits to undefined if the reference is null or undefined, avoiding 'Cannot read properties of undefined' crashes. Nullish Coalescing (??) returns the right-hand operand only if the left-hand operand is null or undefined. In contrast, the logical OR operator (||) checks for any falsy value, inappropriately falling back on 0, false, or ''.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Can optional chaining be used for function calls (fn?.()) and dynamic properties (obj?.[key])?",
        "code_snippet": "const count = 0;\nconsole.log(count ?? 10); // 0\nconsole.log(count || 10); // 10\nconst city = user?.address?.city;"
    },
    {
        "role": "Software Engineer",
        "technology": "javascript",
        "category": "practical_coding_problem",
        "difficulty": "medium",
        "question_text": "Write a function 'deepClone(obj)' in JavaScript that handles nested objects, arrays, and primitive values without relying on external libraries.",
        "expected_answer": "Candidate should handle: null/primitives check, Array vs Object creation, recursive traversal across keys. Can also mention structuredClone(obj) as the modern native Web API solution and explain handling for Dates or cyclic references.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What are the limitations of JSON.parse(JSON.stringify(obj)) for cloning objects?",
        "code_snippet": "function deepClone(obj) {\n  if (obj === null || typeof obj !== 'object') return obj;\n  if (Array.isArray(obj)) return obj.map(deepClone);\n  const clone = {};\n  for (const key of Object.keys(obj)) {\n    clone[key] = deepClone(obj[key]);\n  }\n  return clone;\n}"
    }
]
