"""
Frontend Developer Question Bank - 25 distinct technical questions.
Focuses on modern Web APIs, bundlers (Vite/Webpack), performance (Core Web Vitals), state, accessibility, and CSS architecture.
"""

FRONTEND_DEVELOPER_QUESTIONS = [
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "core_web_vitals",
        "difficulty": "hard",
        "question_text": "Explain Google's Core Web Vitals: LCP (Largest Contentful Paint), INP (Interaction to Next Paint), and CLS (Cumulative Layout Shift). How do you diagnose and optimize each?",
        "expected_answer": "LCP measures loading speed (hero image, heading); optimize via priority hints (fetchpriority='high'), preloading critical assets, CDN caching. INP measures responsiveness to user interactions; optimize by minimizing long JavaScript main-thread tasks, breaking work with requestIdleCallback, debouncing. CLS measures visual stability; optimize by setting explicit width/height or aspect-ratio on images/embeds and reserving ad banner space.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How did INP replace FID (First Input Delay) in March 2024?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "build_tools_vite_webpack",
        "difficulty": "medium",
        "question_text": "Why does Vite achieve dramatically faster local development server startup times compared to traditional Webpack bundles? Explain native ES modules (ESM) in development vs Rollup production bundling.",
        "expected_answer": "Webpack pre-bundles the entire application into memory before serving. Vite leverages native browser ES Modules (ESM): during development, it serves source files directly on-demand when requested by the browser, pre-bundling only dependencies via lightning-fast esbuild in Go. For production, it uses Rollup for tree-shaking, code-splitting, and minification.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Hot Module Replacement (HMR) and how does Vite implement it?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "browser_rendering",
        "difficulty": "hard",
        "question_text": "What is the difference between Reflow (Layout) and Repaint in browser rendering? Which CSS properties trigger both, and which properties trigger composite-only animations?",
        "expected_answer": "Reflow recalculates geometry and positions of nodes in the document, affecting parent and sibling layouts (triggered by width, height, margin, padding, fontSize). Repaint updates visual styling without altering geometry (color, background-color, box-shadow). Composite-only properties (transform, opacity) are executed on the GPU, avoiding CPU reflow and repaint entirely.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is layout thrashing and how does batching DOM reads and writes prevent it?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "cross_origin_cors",
        "difficulty": "medium",
        "question_text": "What is the Same-Origin Policy (SOP), and how does Cross-Origin Resource Sharing (CORS) work? What is a CORS Preflight (OPTIONS) request?",
        "expected_answer": "SOP restricts scripts on one origin (scheme + domain + port) from reading resources on another origin. CORS is an HTTP header mechanism where the server specifies who can access its resources (Access-Control-Allow-Origin). For 'non-simple' requests (custom headers like Authorization, or PUT/DELETE methods), browsers send an automatic HTTP OPTIONS preflight request before sending the actual request.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does Access-Control-Allow-Credentials: true require an explicit origin instead of wildcard '*'?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "security_xss_csrf",
        "difficulty": "hard",
        "question_text": "Explain Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) from a frontend perspective. How do HttpOnly cookies, SameSite cookie attributes, and Content Security Policy (CSP) defend against them?",
        "expected_answer": "XSS injects malicious client-side code to steal sessions; prevented by escaping, React's auto-escaping, CSP headers, and HttpOnly cookies (inaccessible to JS document.cookie). CSRF tricks authenticated browsers into submitting unauthorized requests to third-party sites; prevented by SameSite=Lax/Strict cookie flags, anti-CSRF tokens, and custom header checks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does storing auth tokens in localStorage increase vulnerability to XSS?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "web_workers",
        "difficulty": "medium",
        "question_text": "When and how would you use Web Workers in a frontend application? What limitations exist when running code inside a Web Worker?",
        "expected_answer": "Web Workers run scripts on a background thread without freezing the main UI thread (ideal for processing CSVs, crypto, image filters). Communication uses postMessage and onmessage. Limitations: Workers cannot access the DOM, window, document, or parent page variables directly; they communicate strictly by passing serializable copies or Transferable objects.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between dedicated Web Workers, SharedWorkers, and ServiceWorkers?",
        "code_snippet": "const worker = new Worker('parser.js');\nworker.postMessage(csvText);\nworker.onmessage = (e) => updateUI(e.data);"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "service_workers_pwa",
        "difficulty": "hard",
        "question_text": "What is a Service Worker in Progressive Web Apps (PWAs)? Explain the Service Worker lifecycle (install, activate, fetch) and common caching strategies (Cache First, Network First, Stale-While-Revalidate).",
        "expected_answer": "A Service Worker is a programmable network proxy running in the background. Lifecycle: install (precaching assets), activate (cleanup old caches), and fetch (intercepting network requests). Cache-First serves from cache immediately, falling back to network (ideal for static assets). Network-First tries network, falling back to offline cache (ideal for live data). Stale-While-Revalidate serves cached copy immediately while updating cache from network in background.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why must Service Workers be served strictly over HTTPS?",
        "code_snippet": "self.addEventListener('fetch', (event) => {\n  event.respondWith(\n    caches.match(event.request).then(cached => cached || fetch(event.request))\n  );\n});"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "responsive_design",
        "difficulty": "easy",
        "question_text": "What are Container Queries (@container) in modern CSS, and how do they solve responsive component design better than Viewport Media Queries (@media)?",
        "expected_answer": "Viewport media queries (@media) only respond to the total screen/window width. Container Queries (@container) allow individual components to adapt their layout based on the width of their immediate parent container (container-type: inline-size), enabling true modular design where a card component automatically adjusts whether placed in a narrow sidebar or a wide main column.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you define a container query context using container-type?",
        "code_snippet": ".sidebar { container-type: inline-size; }\n@container (min-width: 400px) {\n  .card { display: flex; }\n}"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "accessibility_wcag",
        "difficulty": "medium",
        "question_text": "What are the four principles of WCAG (POUR: Perceivable, Operable, Understandable, Robust)? How do you ensure accessible keyboard navigation through modals and menus?",
        "expected_answer": "POUR: Perceivable (available to all senses, contrast, alt text), Operable (keyboard navigable, no traps), Understandable (clear language, predictable), Robust (compatible with assistive technologies). For modals: focus must be trapped inside while open, restore focus to the trigger button upon closing, and close on the 'Escape' key.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the minimum color contrast ratio required for normal body text under WCAG AA (4.5:1)?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "state_management",
        "difficulty": "medium",
        "question_text": "How do you decide between Local Component State, Context API, and a Global State Store (Redux Toolkit, Zustand) in modern frontend applications?",
        "expected_answer": "Local state (useState): used for UI state isolated to one component (inputs, toggles). Context API: ideal for low-frequency global settings (theme, auth user, language localization). Global store (Zustand/Redux): needed for complex, high-frequency state shared across disconnected component subtrees where selective subscription prevents unnecessary re-renders.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does Context API trigger re-renders in all consumers when any value on its context object changes?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "intersection_observer",
        "difficulty": "medium",
        "question_text": "How does the Intersection Observer API work in modern JavaScript? How do you implement infinite scrolling and lazy-loading images with it instead of scroll event listeners?",
        "expected_answer": "IntersectionObserver asynchronously observes when a target element enters or exits the viewport (or ancestor container) at specified threshold percentages. Unlike scroll event listeners, it executes off the main thread without causing synchronous layout thrashing. For infinite scrolling, observe a sentinel <div> at the list bottom and trigger fetch on isIntersecting.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the purpose of the 'rootMargin' option in IntersectionObserver?",
        "code_snippet": "const observer = new IntersectionObserver((entries) => {\n  if (entries[0].isIntersecting) loadMoreItems();\n}, { threshold: 1.0 });\nobserver.observe(document.getElementById('sentinel'));"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "web_sockets",
        "difficulty": "medium",
        "question_text": "Compare WebSockets, Server-Sent Events (SSE), and HTTP Long-Polling for real-time frontend applications. Which would you use for a live chat application versus a stock ticker?",
        "expected_answer": "WebSockets provide full-duplex bidirectional TCP communication with minimal framing overhead, best for interactive two-way messaging like live chat. Server-Sent Events (SSE) provide unidirectional server-to-client streaming over standard HTTP with automatic reconnect, simpler and best for stock tickers or live notifications. Long-polling repeatedly re-opens HTTP requests when data arrives, used primarily as legacy fallback.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle reconnecting WebSockets with exponential backoff on client disconnects?",
        "code_snippet": "const socket = new WebSocket('wss://api.example.com/chat');\nsocket.onmessage = (event) => displayMessage(JSON.parse(event.data));"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "css_architecture",
        "difficulty": "easy",
        "question_text": "Compare CSS Modules, Vanilla CSS with custom properties, Tailwind CSS, and CSS-in-JS (Styled Components). What are the trade-offs regarding bundle size and runtime overhead?",
        "expected_answer": "Vanilla CSS + Custom Properties: zero runtime, fast, standard. CSS Modules: scoped class names at build time without runtime cost. Tailwind: utility classes, tiny production bundles via PurgeCSS/compiler, fast workflow. CSS-in-JS (Styled Components): component scoping and dynamic props, but introduces client-side JS runtime style injection overhead and hydration penalties.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why have modern React Server Components shifted away from runtime CSS-in-JS?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "performance_code_splitting",
        "difficulty": "medium",
        "question_text": "What is Route-Based Code Splitting in frontend SPAs, and how do dynamic imports (import()) combined with React.lazy and Suspense reduce Initial Bundle Size?",
        "expected_answer": "Instead of shipping one massive monolithic JavaScript bundle on first page load, code splitting divides code into smaller chunks downloaded on-demand when user visits specific routes. React.lazy(() => import('./Page')) downloads the chunk asynchronously, and <Suspense fallback={<Loader />}> renders a fallback UI during transit.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between vendor chunk splitting and dynamic route splitting?",
        "code_snippet": "const Dashboard = React.lazy(() => import('./Dashboard'));\n<Suspense fallback={<Spinner />}><Dashboard /></Suspense>"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "dom_virtual_dom",
        "difficulty": "medium",
        "question_text": "What is the Virtual DOM and reconciliation algorithm? How do 'keys' in lists help the reconciliation process avoid recreating DOM nodes?",
        "expected_answer": "The Virtual DOM is a lightweight in-memory representation of UI elements. During reconciliation, the framework diffs the new Virtual DOM tree against the previous one and computes the minimal set of real DOM mutations. Keys provide stable identities to list elements across renders: with keys, the diffing engine moves/updates items rather than tearing down and rebuilding entire DOM subtrees.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is using array index as a key an antipattern when lists are reordered, filtered, or deleted?",
        "code_snippet": "items.map(item => <ListItem key={item.id} data={item} />)"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "web_speech_api",
        "difficulty": "medium",
        "question_text": "How does the browser Web Speech API work? Explain the difference between SpeechRecognition and SpeechSynthesis, and how to handle permission denial gracefully.",
        "expected_answer": "SpeechRecognition transcribes user microphone audio into text via browser engine (webkitSpeechRecognition), firing onresult with interim and final transcripts. SpeechSynthesis (speechSynthesis.speak(new SpeechSynthesisUtterance(text))) speaks text aloud. Permission denial fires recognition.onerror with 'not-allowed'; applications must catch this and provide transparent text-based fallbacks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does speech recognition require active user gesture or HTTPS connection in modern browsers?",
        "code_snippet": "const synth = window.speechSynthesis;\nsynth.speak(new SpeechSynthesisUtterance('Hello! Welcome to your interview.'));"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "microfrontends",
        "difficulty": "hard",
        "question_text": "What is a Microfrontend architecture, and how does Webpack 5 / Vite Module Federation allow multiple independently deployed apps to share dependencies at runtime?",
        "expected_answer": "Microfrontends break monolithic frontends into independent applications owned by separate teams. Module Federation allows an application (host) to dynamically load remote modules and shared libraries (like React or design systems) from another deployment at runtime without duplicate bundle downloads, maintaining single shared runtime instances.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle CSS isolation between microfrontends (Shadow DOM, scoped CSS prefixes)?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "browser_caching_headers",
        "difficulty": "medium",
        "question_text": "Explain HTTP Caching headers from a frontend developer perspective: Cache-Control (max-age, immutable, no-cache, no-store) and ETag / 304 Not Modified.",
        "expected_answer": "Cache-Control: max-age=31536000, immutable is applied to hashed assets (app.a8f9c2.js), caching them indefinitely in the browser without revalidation. 'no-cache' forces browser to validate with server before using cached copy (using ETag or If-None-Match, returning 304 if unchanged), ideal for index.html. 'no-store' prevents all caching for sensitive data.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should index.html never be cached with long max-age in Single Page Apps?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "animations_flp",
        "difficulty": "hard",
        "question_text": "Explain the FLIP animation technique (First, Last, Invert, Play) for high-performance layout transitions in JavaScript.",
        "expected_answer": "1) First: measure initial element position (getBoundingClientRect()). 2) Last: trigger layout change and measure final position. 3) Invert: apply transform (translate/scale) and opacity so the element visually appears back at the First position. 4) Play: enable transition and remove the inverted transform, letting GPU animate it smoothly to the Last position at 60fps.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do libraries like Framer Motion automate FLIP transitions with layout animations?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "forms_controlled_uncontrolled",
        "difficulty": "easy",
        "question_text": "Explain the difference between Controlled and Uncontrolled form components in frontend frameworks. When would you use useRef or FormData over state for forms?",
        "expected_answer": "Controlled components bind input value to framework state (value={val} onChange=...), re-rendering on every keystroke, ideal for instant validation and dynamic inputs. Uncontrolled components let the DOM manage input values natively; JavaScript reads values on submit via useRef or new FormData(e.target), significantly reducing re-render overhead on large complex forms.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does React Hook Form leverage uncontrolled inputs for high performance?",
        "code_snippet": "const handleSubmit = (e) => {\n  e.preventDefault();\n  const data = Object.fromEntries(new FormData(e.target));\n};"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "testing_frontend",
        "difficulty": "medium",
        "question_text": "Explain the philosophy of React Testing Library / Vitest: 'The more your tests resemble the way your software is used, the more confidence they can give you.' Why query by role (getByRole) over test IDs?",
        "expected_answer": "Querying by role (getByRole('button', { name: /submit/i })) validates accessibility trees the same way real assistive technologies and end users perceive elements, ensuring elements have accessible names and semantic markup. Querying by test-id or CSS selectors tests implementation details that can change without breaking functionality.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Mock Service Worker (MSW) and why is it preferred for API mocking in tests?",
        "code_snippet": "test('submits interview setup', async () => {\n  render(<InterviewSetup />);\n  await userEvent.type(screen.getByRole('textbox', { name: /role/i }), 'Python Developer');\n  await userEvent.click(screen.getByRole('button', { name: /start/i }));\n});"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "typescript_frontend",
        "difficulty": "medium",
        "question_text": "How does TypeScript improve frontend engineering in large codebases? Explain discriminated unions for modeling state machines (e.g. loading, success, error).",
        "expected_answer": "TypeScript catches runtime typos, missing API fields, and prop mismatches during development. A discriminated union uses a common literal property (type: 'loading' | 'success' | 'error') across types: when switching on state.type, TypeScript narrows the available properties, preventing access to data when loading or error when success.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between 'unknown' and 'any' in TypeScript?",
        "code_snippet": "type AsyncState<T> =\n  | { status: 'idle' }\n  | { status: 'loading' }\n  | { status: 'success'; data: T }\n  | { status: 'error'; error: Error };"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "resilient_error_boundaries",
        "difficulty": "medium",
        "question_text": "What is an Error Boundary in React? What types of errors can it catch, and what errors cannot be caught by Error Boundaries?",
        "expected_answer": "An Error Boundary is a component that catches JavaScript errors anywhere in its child component tree, logs the error, and displays a fallback UI instead of crashing the entire page. It catches rendering errors, lifecycle methods, and constructors. It does NOT catch: event handlers (needs try/catch), async code (setTimeout/fetch), server-side rendering, or errors in the boundary itself.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What lifecycle methods make a component an Error Boundary (componentDidCatch, getDerivedStateFromError)?",
        "code_snippet": ""
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "responsive_images_modern",
        "difficulty": "easy",
        "question_text": "How do you prevent Cumulative Layout Shift (CLS) when loading responsive images and third-party web fonts?",
        "expected_answer": "For images: always include explicit width and height attributes or CSS aspect-ratio so the browser reserves the correct dimensional space before the image binary downloads. For web fonts: use 'font-display: swap' or 'font-display: optional', preload critical font files with rel='preload', and match fallback font metrics with size-adjust to prevent text shift.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between FOIT (Flash of Invisible Text) and FOUT (Flash of Unstyled Text)?",
        "code_snippet": "@font-face {\n  font-family: 'Inter';\n  src: url('/fonts/inter.woff2') format('woff2');\n  font-display: swap;\n}"
    },
    {
        "role": "Frontend Developer",
        "technology": "frontend",
        "category": "practical_component_design",
        "difficulty": "hard",
        "question_text": "Design an accessible, reusable Autocomplete Search Dropdown component. Explain keyboard navigation (ArrowUp, ArrowDown, Enter, Escape), ARIA combobox pattern, and debounced API requests.",
        "expected_answer": "Candidate must address: 1) Input with role='combobox', aria-expanded, aria-controls='listbox-id', aria-autocomplete='list'; 2) Dropdown container with role='listbox' and options with role='option' and aria-selected; 3) Active descendant tracking (aria-activedescendant) as user presses Arrow keys; 4) Escape key closes dropdown; 5) Debounced search queries.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you ensure screen readers announce search results counts using aria-live regions?",
        "code_snippet": "<input role=\"combobox\" aria-expanded={isOpen} aria-controls=\"results\" aria-activedescendant={focusedId} />"
    }
]
