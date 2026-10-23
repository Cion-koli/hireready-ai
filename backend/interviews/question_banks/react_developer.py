"""
React Developer Question Bank - 25 distinct technical questions.
Covers core React concepts, hooks, component patterns, state management, reconciliation, performance optimization, and testing.
"""

REACT_DEVELOPER_QUESTIONS = [
    {
        "role": "React Developer",
        "technology": "react",
        "category": "core_concepts",
        "difficulty": "easy",
        "question_text": "What is the Virtual DOM in React, and how does the reconciliation algorithm determine when and how to update the actual DOM efficiently?",
        "expected_answer": "The Virtual DOM is a lightweight in-memory representation of the real DOM tree. When state or props change, React creates a new Virtual DOM tree and diffs it against the previous one (reconciliation). It uses heuristics like component types and unique 'key' attributes to calculate the minimal set of real DOM mutations needed in the commit phase.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How did React Fiber improve the reconciliation process over the legacy stack reconciler?",
        "code_snippet": None
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "hooks",
        "difficulty": "easy",
        "question_text": "What are the fundamental Rules of Hooks in React, and why must hooks only be called at the top level rather than inside conditions or loops?",
        "expected_answer": "Rules of Hooks: 1. Only call hooks at the top level of React function components or custom hooks. 2. Do not call hooks inside loops, conditionals, or nested functions. This rule is necessary because React relies on the exact order of hook calls across renders to associate state variables with their internal linked list node.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does ESLint's eslint-plugin-react-hooks enforce this statically?",
        "code_snippet": "// Invalid:\nif (isLoggedIn) {\n    useEffect(() => { ... }, []);\n}"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "hooks",
        "difficulty": "medium",
        "question_text": "Explain the difference between useEffect, useLayoutEffect, and the new useInsertionEffect hook. When should each be utilized?",
        "expected_answer": "useEffect fires asynchronously after layout and paint, non-blocking to the browser. useLayoutEffect runs synchronously immediately after all DOM mutations but before the browser paints screen pixels, useful for reading DOM measurements or preventing visual flicker. useInsertionEffect runs before DOM mutations, specifically designed for CSS-in-JS libraries to inject style tags.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does React warn against useLayoutEffect during Server-Side Rendering (SSR)?",
        "code_snippet": None
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "state_management",
        "difficulty": "easy",
        "question_text": "Why is React state considered immutable, and what happens if you mutate state directly instead of calling the setter function?",
        "expected_answer": "State is treated as immutable so that React can use shallow reference equality checks (Object.is) to quickly detect whether a component needs re-rendering. Mutating state directly (e.g. state.items.push(x)) retains the same object reference, preventing React from detecting the mutation and causing missing or inconsistent UI updates.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do libraries like Immer help manage deep immutable state updates safely?",
        "code_snippet": "// Incorrect:\nstate.count = state.count + 1;\n// Correct:\nsetCount(prev => prev + 1);"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "performance",
        "difficulty": "medium",
        "question_text": "How do React.memo, useMemo, and useCallback differ, and what is the cost of overusing memoization everywhere in an application?",
        "expected_answer": "React.memo is a higher-order component that memoizes component rendering based on shallow prop comparison. useMemo memoizes the computed result of an expensive calculation. useCallback memoizes the function reference between renders. Overusing them everywhere introduces overhead from maintaining dependencies arrays and performing shallow comparisons, which can exceed the cost of simple re-renders.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "When does passing an inline callback actually break React.memo optimization of a child component?",
        "code_snippet": "const memoizedCallback = useCallback(() => {\n    doSomething(a, b);\n}, [a, b]);"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "hooks",
        "difficulty": "medium",
        "question_text": "What is the purpose of useRef? How does mutating ref.current differ from updating state with useState in terms of component re-renders?",
        "expected_answer": "useRef returns a mutable ref object whose .current property persists across the entire component lifecycle. Unlike useState, updating ref.current does NOT trigger a re-render. It is used to directly access DOM elements (focus, scroll position) or to store mutable values that do not affect the rendered output (e.g. interval IDs, previous prop values).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can you use useRef to store the previous value of a prop or state variable?",
        "code_snippet": "const inputRef = useRef(null);\nconst handleFocus = () => inputRef.current.focus();\nreturn <input ref={inputRef} />;"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "architecture",
        "difficulty": "medium",
        "question_text": "Compare Controlled Components vs Uncontrolled Components in React forms. When would you prefer uncontrolled components with FormData or React Hook Form?",
        "expected_answer": "Controlled components bind form input values to React state via onChange handlers, providing immediate validation and dynamic UI synchronization. Uncontrolled components let the DOM maintain form state, accessing values via refs or native FormData on submit. Uncontrolled forms reduce re-renders on every keystroke, offering superior performance for huge enterprise forms.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does React 19 introduce form actions and useActionState?",
        "code_snippet": None
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "context_api",
        "difficulty": "medium",
        "question_text": "What is the Context API in React, and what is the primary pitfall regarding unnecessary re-renders when context values update?",
        "expected_answer": "Context API provides a way to pass data through the component tree without prop drilling. The pitfall is that whenever the context Provider's value reference changes, ALL consuming components that call useContext re-render, even if they only read a small untouched property of the context object. Mitigation involves splitting contexts by domain or memoizing value objects.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do selector-based libraries like Zustand or Redux Toolkit avoid this re-rendering pitfall?",
        "code_snippet": "const UserContext = React.createContext(null);\nexport const UserProvider = ({ children }) => {\n    const [user, setUser] = useState(null);\n    const value = useMemo(() => ({ user, setUser }), [user]);\n    return <UserContext.Provider value={value}>{children}</UserContext.Provider>;\n};"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "hooks",
        "difficulty": "medium",
        "question_text": "When is useReducer preferred over useState, and how do you structure a reducer function and action types?",
        "expected_answer": "useReducer is preferred when state logic is complex, involves multiple sub-values, when the next state depends on the previous state, or when different components dispatch related events. It follows the Redux pattern: (state, action) => newState, with action having a 'type' string and optional 'payload', making state transitions predictable and easy to unit test.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can you pass dispatch down through context instead of callbacks?",
        "code_snippet": "function reducer(state, action) {\n    switch (action.type) {\n        case 'FETCH_SUCCESS': return { ...state, data: action.payload, loading: false };\n        case 'FETCH_FAIL': return { ...state, error: action.payload, loading: false };\n        default: return state;\n    }\n}"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "custom_hooks",
        "difficulty": "medium",
        "question_text": "Design a reusable custom hook called useDebounce that debounces any fast-changing value (such as a search input) by a specified delay in milliseconds.",
        "expected_answer": "useDebounce accepts a value and a delay. Inside, it manages debouncedValue with useState and uses useEffect to set a setTimeout that updates debouncedValue after delay. In the effect cleanup function, it calls clearTimeout to cancel pending timeouts if the value changes before delay elapses.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How would you handle immediate execution on the leading edge?",
        "code_snippet": "function useDebounce(value, delay = 300) {\n    const [debouncedValue, setDebouncedValue] = useState(value);\n    useEffect(() => {\n        const handler = setTimeout(() => setDebouncedValue(value), delay);\n        return () => clearTimeout(handler);\n    }, [value, delay]);\n    return debouncedValue;\n}"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "error_handling",
        "difficulty": "medium",
        "question_text": "What is an Error Boundary in React? Why can Error Boundaries only be written as class components (or via libraries), and what errors do they NOT catch?",
        "expected_answer": "An Error Boundary is a component that catches JavaScript errors anywhere in its child component tree, logs the error, and displays a fallback UI instead of crashing the whole component tree. It requires static getDerivedStateFromError or componentDidCatch, which have no hook equivalent. They do NOT catch: event handler errors, asynchronous code (setTimeout, fetch), SSR errors, or errors in the boundary itself.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle unhandled errors in async effects or click handlers?",
        "code_snippet": "class ErrorBoundary extends React.Component {\n    state = { hasError: false };\n    static getDerivedStateFromError(error) { return { hasError: true }; }\n    componentDidCatch(error, errorInfo) { logErrorToService(error, errorInfo); }\n    render() { return this.state.hasError ? <h1>Something went wrong.</h1> : this.props.children; }\n}"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "code_splitting",
        "difficulty": "medium",
        "question_text": "How do React.lazy and Suspense enable route-based code splitting, and how does dynamic import() reduce the initial bundle size?",
        "expected_answer": "React.lazy takes a function that calls dynamic import('path/to/Component'), returning a Promise that resolves to a module. Suspense wraps the lazy component and displays a fallback UI (like a spinner) while the bundle chunk downloads. Route-based code splitting ensures clients only download JavaScript chunks for pages they visit, drastically reducing initial TTI and FCP.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle network chunk load failures when lazy-loading a route?",
        "code_snippet": "const Dashboard = React.lazy(() => import('./Dashboard'));\n<Suspense fallback={<Spinner />}>\n    <Dashboard />\n</Suspense>"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "component_patterns",
        "difficulty": "hard",
        "question_text": "Explain the Compound Components pattern in React. How do subcomponents (e.g. <Tabs>, <Tabs.List>, <Tabs.Tab>, <Tabs.Panel>) share implicit state without prop drilling?",
        "expected_answer": "Compound Components coordinate a set of subcomponents that share state implicitly behind the scenes, offering an expressive, declarative API like HTML <select> and <option>. The parent component creates a React Context holding active state and handlers. The subcomponents consume this context internally, allowing callers full control over layout and DOM markup.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does React.Children.map with React.cloneElement contrast with Context in compound components?",
        "code_snippet": "<Tabs defaultValue=\"account\">\n    <Tabs.List>\n        <Tabs.Tab value=\"account\">Account</Tabs.Tab>\n        <Tabs.Tab value=\"password\">Password</Tabs.Tab>\n    </Tabs.List>\n    <Tabs.Panel value=\"account\"><AccountSettings /></Tabs.Panel>\n</Tabs>"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "performance",
        "difficulty": "hard",
        "question_text": "What is windowing / virtualization in React list rendering (e.g. react-window or tanstack-virtual), and how does it maintain 60 FPS when rendering 100,000 items?",
        "expected_answer": "Virtualization renders only the DOM nodes currently visible within the viewport (plus a small buffer), recycling or repositioning them dynamically as the user scrolls. Instead of adding 100,000 DOM elements (which consumes hundreds of megabytes of memory and throttles layout reflows), it maintains only 20-30 active DOM elements with absolute positioning and container offset calculations.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do dynamic row heights complicate virtualization calculations?",
        "code_snippet": None
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "hooks",
        "difficulty": "hard",
        "question_text": "What causes the 'stale closure' problem in React hooks (such as useEffect or setInterval callbacks), and what are two effective ways to resolve it?",
        "expected_answer": "Stale closures occur when an asynchronous callback captures state or prop variables from an earlier render pass because the effect dependency array was empty or incomplete. Ways to resolve: 1. Use the functional state updater setCount(prev => prev + 1), which always receives fresh current state. 2. Store the fresh mutable callback in a useRef updated on every render.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does useEffectEvent (experimental) solve this problem without adding dependencies?",
        "code_snippet": "// Buggy:\nuseEffect(() => {\n    const id = setInterval(() => {\n        setCount(count + 1); // stale count!\n    }, 1000);\n    return () => clearInterval(id);\n}, []);"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "react_18",
        "difficulty": "hard",
        "question_text": "Explain Concurrent Mode features in React 18, specifically startTransition and useDeferredValue. How do they prevent UI freezing during CPU-intensive tasks?",
        "expected_answer": "Concurrent React allows rendering to be interrupted and prioritized. Urgent updates (typing in an input, clicking buttons) run immediately with top priority. Non-urgent updates (filtering a 10,000-item grid) wrapped in startTransition or passed to useDeferredValue yield CPU time back to browser events between render slices, keeping the input responsive without lag.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the boolean pending state returned by useTransition?",
        "code_snippet": "const [isPending, startTransition] = useTransition();\nfunction handleSearch(e) {\n    setQuery(e.target.value); // Urgent\n    startTransition(() => {\n        setSearchFilter(e.target.value); // Transition\n    });\n}"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "testing",
        "difficulty": "medium",
        "question_text": "What is the guiding philosophy of React Testing Library ('Test components the way users use them'), and why are user-event and findByRole preferred over querySelector or wrapper.instance()?",
        "expected_answer": "RTL encourages testing application code by simulating real user interactions and querying accessible DOM elements rather than testing internal component state or implementation details. This makes tests resilient to refactoring. findByRole encourages accessible markup (ARIA roles/labels) and userEvent accurately simulates real browser click/keyboard events with focus.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between getByRole, queryByRole, and findByRole?",
        "code_snippet": "test('submits user credentials', async () => {\n    render(<LoginForm />);\n    await userEvent.type(screen.getByRole('textbox', { name: /username/i }), 'john');\n    await userEvent.click(screen.getByRole('button', { name: /login/i }));\n    expect(await screen.findByText(/welcome john/i)).toBeInTheDocument();\n});"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "routing",
        "difficulty": "easy",
        "question_text": "How does React Router v6 handle nested routing and layouts using the <Outlet /> component?",
        "expected_answer": "React Router v6 supports nested route definitions where a parent route renders shared layout elements (navigation bar, sidebar, footer) and places an <Outlet /> element where matched child route elements are inserted. This avoids re-mounting shared layouts when navigating between sibling routes and keeps layout code DRY.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do useParams and useNavigate interact with nested routes?",
        "code_snippet": "<Routes>\n    <Route path=\"/dashboard\" element={<DashboardLayout />}>\n        <Route index element={<Overview />} />\n        <Route path=\"analytics\" element={<Analytics />} />\n    </Route>\n</Routes>"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "data_fetching",
        "difficulty": "medium",
        "question_text": "Why is data fetching with TanStack Query (React Query) or SWR generally preferred over raw useEffect + useState fetching?",
        "expected_answer": "TanStack Query and SWR handle client-side cache management, background revalidation (stale-while-revalidate), deduping identical network requests, automatic refetch on window focus or network reconnect, pagination/infinite scroll caching, mutation side-effects, and loading/error states out of the box. useEffect fetching often causes race conditions and memory leaks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does query key serialization work in React Query cache invalidation?",
        "code_snippet": "const { data, isLoading, error } = useQuery({\n    queryKey: ['todos', userId],\n    queryFn: () => fetchTodos(userId),\n    staleTime: 1000 * 60 * 5\n});"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "ssr_architecture",
        "difficulty": "hard",
        "question_text": "What is Hydration in React SSR (Next.js/Remix), and what causes a Hydration Mismatch error?",
        "expected_answer": "Hydration is the client-side process where React attaches event listeners and hooks up internal state to pre-rendered HTML sent by the server. A Hydration Mismatch error occurs when the server-rendered HTML tree differs from the initial client render tree, caused by client-only checks (window !== undefined, Date.now(), Math.random(), or mismatched browser cookies).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does suppressHydrationWarning work and when is it appropriate to use?",
        "code_snippet": None
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "rsc",
        "difficulty": "hard",
        "question_text": "What are React Server Components (RSC), and how do they differ fundamentally from traditional Client Components marked with 'use client'?",
        "expected_answer": "Server Components run strictly on the server and are serialized to a special stream format; their code and dependency packages (e.g. database drivers, heavy markdown parsers) are never bundled or downloaded to the client browser. Client Components ('use client') run on both server (for SSR) and client, containing interactivity, hooks, and browser APIs.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Can you pass Server Components as children to Client Components?",
        "code_snippet": "// Server Component (default in Next App Router)\nasync function UserProfile({ id }) {\n    const user = await db.user.findUnique({ where: { id } });\n    return <div>{user.name}</div>;\n}"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "component_patterns",
        "difficulty": "medium",
        "question_text": "What is forwardRef in React, and when must a child component be wrapped in React.forwardRef?",
        "expected_answer": "By default, React components do not accept the ref attribute as a standard prop; passing ref to a custom component results in undefined. React.forwardRef creates a component that receives a ref parameter as its second argument, allowing parent components to obtain a direct reference to a specific DOM node or imperative handle inside the child.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does useImperativeHandle restrict what the parent ref can access?",
        "code_snippet": "const FancyInput = React.forwardRef((props, ref) => (\n    <input ref={ref} className=\"fancy-input\" {...props} />\n));"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "security",
        "difficulty": "medium",
        "question_text": "How does React protect against Cross-Site Scripting (XSS) by default, and when can dangerouslySetInnerHTML expose a vulnerability?",
        "expected_answer": "React automatically escapes all strings rendered inside JSX expressions before injecting them into the DOM, converting characters like <, >, &, \" to safe HTML entities. dangerouslySetInnerHTML bypasses this protection to inject raw HTML; if malicious user-provided strings are injected without sanitization (via DOMPurify), an attacker can execute arbitrary JavaScript.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Can malicious href='javascript:...' attributes execute XSS despite JSX escaping?",
        "code_snippet": "import DOMPurify from 'dompurify';\n<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userContent) }} />"
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "performance",
        "difficulty": "medium",
        "question_text": "How do you detect and profile unnecessary component re-renders using the React Developer Tools Profiler and the React 19 / React scan tools?",
        "expected_answer": "Use React Profiler tab to record render interactions, checking flamecharts and ranked bars. Enabling 'Highlight updates when components render' shows visual bounding boxes. Profiler displays why each component rendered (e.g., 'props changed', 'hook X changed'). Profiling pinpoints whether parent re-renders or unstable object/array prop references are causing cascading renders.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does React 19's React Compiler (Forget) automate memoization at build time?",
        "code_snippet": None
    },
    {
        "role": "React Developer",
        "technology": "react",
        "category": "portals",
        "difficulty": "easy",
        "question_text": "What are React Portals (ReactDOM.createPortal), and why are they essential for modals, tooltips, and dialogs?",
        "expected_answer": "Portals provide a way to render children into a DOM node that exists outside the DOM hierarchy of the parent component (e.g. directly under document.body). This avoids CSS styling issues like parent overflow: hidden clipping, z-index stacking context restrictions, and relative positioning constraints, while preserving React event bubbling up the React component tree.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Does an event fired from a portal child bubble to its React parent or its DOM parent?",
        "code_snippet": "import ReactDOM from 'react-dom';\nfunction Modal({ children }) {\n    return ReactDOM.createPortal(\n        <div className=\"modal-backdrop\">{children}</div>,\n        document.getElementById('modal-root')\n    );\n}"
    }
]
