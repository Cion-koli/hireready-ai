"""
QA / Software Tester Question Bank - 25 distinct technical questions.
Covers test design techniques, bug lifecycles, automation frameworks (Selenium, Playwright, Cypress), API testing, performance testing, and CI/CD pipelines.
"""

QA_TESTER_QUESTIONS = [
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "test_design",
        "difficulty": "easy",
        "question_text": "Explain Equivalence Partitioning (EP) and Boundary Value Analysis (BVA). If an input field accepts age from 18 to 65, what test values would you select using BVA?",
        "expected_answer": "EP divides input domain into valid and invalid partitions where test values are assumed to behave similarly. BVA tests the extreme boundary limits where bugs occur most frequently. For age 18-65 (inclusive), BVA test cases: 17 (just below min, invalid), 18 (min, valid), 19 (just above min, valid), 64 (just below max, valid), 65 (max, valid), 66 (just above max, invalid).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you apply 2-value vs 3-value boundary testing according to ISTQB standards?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "defect_management",
        "difficulty": "easy",
        "question_text": "What is the difference between Bug Severity and Bug Priority? Give an example of a defect with High Severity but Low Priority, and another with Low Severity but High Priority.",
        "expected_answer": "Severity reflects the technical impact of the defect on system functionality/stability. Priority reflects how urgently the business needs the defect fixed. High Severity, Low Priority: system crashes when importing obscure legacy 1995 file format used by 1 customer once a year. Low Severity, High Priority: company logo is missing or misspelled on the public homepage header.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What steps make a bug report reproducible and unambiguous for engineers?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "test_types",
        "difficulty": "easy",
        "question_text": "Contrast Smoke Testing, Sanity Testing, and Regression Testing. At what stages of the CI/CD pipeline are they executed?",
        "expected_answer": "Smoke testing (build verification) tests critical core workflows to verify if the build is stable enough for deeper testing. Sanity testing is a quick, focused subset testing specific bug fixes or minor features in a stable build. Regression testing is comprehensive testing across the entire application to verify that new changes didn't break existing functionality. Smoke runs on every build commit; regression runs before releases.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you select an optimized regression test suite when test run time is constrained?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "api_testing",
        "difficulty": "medium",
        "question_text": "How do you test a RESTful API endpoint beyond checking for HTTP status 200 OK? What assertions should be included in an automated API test suite?",
        "expected_answer": "A thorough API test checks: 1. Status code matches expected (200, 201, 400, 401, 403, 404, 500). 2. Response schema matches JSON schema (field names, types, mandatory fields). 3. Response payload data correctness and calculations. 4. Response headers (Content-Type, caching, CORS, security headers). 5. Response time / latency SLA. 6. Negative cases (missing headers, invalid auth, boundary values).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you automate chaining authentication bearer tokens between API requests in Postman or PyTest?",
        "code_snippet": "# Pytest API validation:\ndef test_create_order(api_client):\n    res = api_client.post('/orders', json={'item_id': 5, 'qty': 2})\n    assert res.status_code == 201\n    data = res.json()\n    assert 'order_id' in data\n    assert data['total_price'] == 40.0"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "automation_frameworks",
        "difficulty": "medium",
        "question_text": "What is the Page Object Model (POM) pattern in test automation, and why is it superior to writing inline locator queries in test scripts?",
        "expected_answer": "POM is an architectural design pattern that creates an object repository for web UI elements. Each web page is represented by a class containing element locators and user action methods (e.g. loginPage.enterUsername()). POM eliminates code duplication, improves readability, and makes tests resilient: when a UI selector changes, you update it in a single page class rather than in 50 tests.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does POM differ from the Screenplay Pattern?",
        "code_snippet": "class LoginPage:\n    def __init__(self, page):\n        self.page = page\n        self.username_input = page.locator('#username')\n        self.login_btn = page.locator('button[type=\"submit\"]')\n    async def login(self, username, password):\n        await self.username_input.fill(username)\n        await self.login_btn.click()"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "automation_playwright",
        "difficulty": "medium",
        "question_text": "How do Playwright and Cypress handle asynchronous element waiting compared to legacy Selenium WebDriver Implicit and Explicit Waits?",
        "expected_answer": "Selenium requires explicit WebDriverWait with ExpectedConditions, or unreliable implicit thread sleeps, which cause flakiness. Playwright and Cypress provide built-in Auto-Waiting: before performing actions (click, fill), they automatically wait for elements to be attached to the DOM, visible, stable (no ongoing CSS animations), and enabled before clicking, drastically reducing flaky test failures.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is hard-coded time.sleep() or Thread.sleep() considered an anti-pattern in test automation?",
        "code_snippet": "// Playwright automatically awaits visibility and actionability:\nawait page.getByRole('button', { name: 'Submit' }).click();"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "locators",
        "difficulty": "medium",
        "question_text": "Compare CSS Selectors versus XPath in web automation. Which is faster, and when is XPath strictly required?",
        "expected_answer": "CSS selectors are generally faster, have cleaner syntax, and are natively supported across all modern browsers. XPath allows bi-directional tree navigation (e.g. traversing from a child element up to its parent using /.. or ancestor::) and text-matching (//button[text()='Submit']), which CSS selectors cannot do natively in standard CSS2/CSS3 specifications.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why are accessible role selectors (getByRole, getByLabel) now preferred over both CSS and XPath?",
        "code_snippet": "-- XPath traversing to parent container:\n//input[@name='email']/ancestor::div[@class='form-group']\n-- CSS selector:\ndiv.form-group input[name='email']"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "flaky_tests",
        "difficulty": "hard",
        "question_text": "What is a 'Flaky Test'? What are the primary root causes of test flakiness in CI pipelines, and how do you systematically diagnose and fix them?",
        "expected_answer": "A flaky test passes and fails intermittently on the identical codebase without code changes. Causes: 1. Asynchronous race conditions and timing issues (elements not ready). 2. Test interdependencies / shared state (tests polluting database or local storage). 3. Network latency / 3rd-party API fluctuations. 4. Resource contention in CI containers. Fixes: proper auto-waits, database rollbacks/isolated test fixtures, mocking external services, and retries with artifacts (video/trace recordings).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do Playwright traces help debug intermittent CI failures after the run completes?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "test_pyramid",
        "difficulty": "easy",
        "question_text": "Explain the Testing Pyramid (Unit, Integration, End-to-End). Why is an inverted testing pyramid (the 'Ice Cream Cone' anti-pattern) problematic?",
        "expected_answer": "The pyramid suggests having a broad base of fast, cheap Unit tests, a moderate layer of Integration tests, and a small peak of high-value End-to-End (E2E) UI tests. The Ice Cream Cone anti-pattern occurs when teams rely heavily on manual or E2E tests with few unit tests. This results in slow CI builds (hours), high maintenance cost, flaky tests, and difficult bug localization.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Where do Contract Tests (e.g. Pact) fit into the modern testing pyramid?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "performance_testing",
        "difficulty": "medium",
        "question_text": "What is the difference between Load Testing, Stress Testing, and Spike Testing? What key metrics (p95 latency, throughput RPS, error rate) define pass/fail criteria?",
        "expected_answer": "Load Testing tests system behavior under expected normal and peak traffic loads. Stress Testing pushes traffic beyond maximum capacity until system breaks to find the breaking point and recovery mechanism. Spike Testing applies sudden, extreme bursts of traffic to test elasticity. Pass/fail metrics: Response time (p95/p99 under 500ms), Throughput (requests/sec sustained), and Error rate (<0.1% HTTP 5xx errors).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is 95th percentile (p95) latency a better measure than average response time?",
        "code_snippet": "# Locust load test file example:\nfrom locust import HttpUser, task\nclass UserBehavior(HttpUser):\n    @task\n    def load_home(self):\n        self.client.get('/api/products')"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "security_testing",
        "difficulty": "medium",
        "question_text": "How does a QA tester test for Cross-Site Scripting (XSS) and SQL Injection vulnerabilities during manual and automated functional testing?",
        "expected_answer": "For XSS: inject script payloads (<script>alert(1)</script>, <img src=x onerror=alert(1)>) into input fields (search, comments, user profile) and verify they are escaped as text entities rather than rendered as executable DOM. For SQL injection: inject characters like ' OR '1'='1' -- or ' UNION SELECT in login and query inputs and check if database syntax errors or unauthorized records are revealed.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do DAST tools like OWASP ZAP integrate into CI/CD security regression pipelines?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "ci_cd",
        "difficulty": "medium",
        "question_text": "How do you configure automated parallel test execution in GitHub Actions or Jenkins to reduce test execution time from 40 minutes to 5 minutes?",
        "expected_answer": "Configure matrix strategy or parallel runners in the pipeline configuration (e.g. matrix: [shard: [1/4, 2/4, 3/4, 4/4]]). Split the test suite evenly across container runners using test runners like Pytest-xdist or Playwright shard option (--shard=1/4). Each container runs its slice simultaneously, and the CI server aggregates the test results into a unified JUnit report.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you manage test database isolation when tests run concurrently?",
        "code_snippet": "# GitHub Actions matrix:\nstrategy:\n  matrix:\n    shard: [1, 2, 3, 4]\nsteps:\n  - run: npx playwright test --shard=${{ matrix.shard }}/4"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "mocking",
        "difficulty": "medium",
        "question_text": "What is the difference between Mocks, Stubs, and Spies in automated testing? When should external third-party payment gateways (Stripe, PayPal) be mocked?",
        "expected_answer": "A Stub provides canned pre-programmed answers to calls made during tests. A Spy records information about calls (number of times called, arguments passed). A Mock is pre-configured with expectations that specify which calls will be received, verifying interaction behavior. Third-party payment gateways should be mocked in automated CI to prevent real financial transactions, avoid network flakiness, and simulate edge failure cases.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you test the real integration with payment gateways in staging environments?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "accessibility_testing",
        "difficulty": "easy",
        "question_text": "What is WCAG 2.1 compliance? How do you test web accessibility for keyboard navigation, screen readers, and color contrast?",
        "expected_answer": "WCAG (Web Content Accessibility Guidelines) defines standards for accessible web content based on four principles: Perceivable, Operable, Understandable, Robust (POUR). Testing: 1. Keyboard navigation (Tab/Shift+Tab, visible focus indicator, Escape to close modals). 2. Screen reader testing (NVDA, VoiceOver checking alt text, ARIA roles, form labels). 3. Automated contrast checking (minimum 4.5:1 ratio for normal text via Axe Core or Lighthouse).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you automate accessibility regression testing using @axe-core/playwright?",
        "code_snippet": "import AxeBuilder from '@axe-core/playwright';\ntest('page should not have accessibility violations', async ({ page }) => {\n    await page.goto('/dashboard');\n    const accessibilityScanResults = await new AxeBuilder({ page }).analyze();\n    expect(accessibilityScanResults.violations).toEqual([]);\n});"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "test_data_management",
        "difficulty": "medium",
        "question_text": "What are best practices for Test Data Management in automated testing? Why is hardcoding test user accounts in shared environments risky?",
        "expected_answer": "Hardcoding test accounts leads to state collision: parallel tests overwrite each other's credentials or shopping carts, causing false failures. Best practices: 1. Generate unique dynamic test data on the fly (UUIDs, Faker libraries). 2. Seed atomic test fixtures via API before each test and clean up in teardown. 3. Use database transactions with rollback after test completion. 4. Isolate data by tenant or environment.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do factories (e.g. factory_boy in Python) simplify test data setup?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "mobile_testing",
        "difficulty": "medium",
        "question_text": "How does mobile app testing (iOS / Android with Appium) differ from desktop browser testing? What mobile-specific test scenarios must be validated?",
        "expected_answer": "Mobile testing involves native gestures (swipe, pinch, double-tap), device fragmentation (screen sizes, OS versions), hardware interrupts (incoming phone calls, low battery alerts, push notifications), orientation changes (portrait/landscape), network variations (switching 4G/5G/Airplane mode/offline mode), and app lifecycle transitions (backgrounding, foregrounding, force kill).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between testing on Emulators/Simulators versus Real Device Clouds (SauceLabs, BrowserStack)?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "test_metrics",
        "difficulty": "easy",
        "question_text": "What is Defect Density, Defect Leakage, and Test Coverage? How do these metrics guide quality improvements across sprints?",
        "expected_answer": "Defect Density is the number of confirmed defects per size of the module (e.g. bugs per 1,000 lines of code or story points). Defect Leakage is the percentage of defects that slipped past QA and were discovered by end users in production ((UAT/Prod Bugs / Total Bugs) * 100). Test Coverage measures the percentage of requirements or code paths executed by tests. High leakage signals gaps in test suites.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why can 100% code coverage give a false sense of security without boundary assertion testing?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "exploratory_testing",
        "difficulty": "easy",
        "question_text": "What is Exploratory Testing, and how does Session-Based Test Management (SBTM) provide structure and accountability to exploratory sessions?",
        "expected_answer": "Exploratory testing is simultaneous learning, test design, and test execution without scripted step-by-step instructions. SBTM structures exploratory testing by defining Charters (specific objective and mission), fixed timeboxes (typically 60-90 minutes), uninterrupted focus, and a debrief report summarizing bugs found, risks discovered, and areas covered.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What heuristics (e.g. SFDIPOT) help guide exploratory testers?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "bdd",
        "difficulty": "medium",
        "question_text": "Explain Behavior-Driven Development (BDD) and Gherkin syntax (Given-When-Then). What are the benefits and potential pitfalls of cucumber-based test suites?",
        "expected_answer": "BDD promotes collaboration between product owners, developers, and QA by writing requirements in human-readable Given (precondition), When (action), Then (expected outcome) format. Benefits: clear living documentation shared across business stakeholders. Pitfalls: overhead of maintaining regex glue code, slow execution, and brittle step definitions if overused for technical unit tests.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do Scenario Outlines parameterize data tables in Gherkin?",
        "code_snippet": "Scenario Outline: Login with invalid credentials\n  Given the user is on the login page\n  When they enter username <user> and password <pass>\n  Then an error message <error> should be displayed\n  Examples:\n    | user   | pass     | error            |\n    | admin  | wrong    | Invalid password |\n    | locked | pass123  | Account locked   |"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "state_transition",
        "difficulty": "medium",
        "question_text": "What is State Transition Testing? Draw a state diagram concept for an E-commerce Order (Draft, Placed, Shipped, Delivered, Cancelled) and explain negative transition testing.",
        "expected_answer": "State transition testing verifies that a system transitions correctly between valid states based on specific input events, and rejects invalid transitions. For an order: Draft -> Placed -> Shipped -> Delivered. Valid transitions include Draft -> Cancelled, Placed -> Cancelled. Negative transition testing attempts invalid actions: trying to transition an order from 'Delivered' to 'Cancelled' or 'Draft' to 'Shipped' directly.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you represent state transition coverage in a 2D matrix?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "cross_browser",
        "difficulty": "easy",
        "question_text": "What causes Cross-Browser Compatibility issues (Chrome vs Firefox vs Safari), and how do you organize a cross-browser testing strategy?",
        "expected_answer": "Different browser rendering engines (Blink/Chrome, Gecko/Firefox, WebKit/Safari) have variations in CSS support (subtle flexbox/grid bugs), JavaScript engine quirks (Safari Date parsing), and media codecs. Strategy: Identify top browser analytics usage for the target audience, run automated smoke tests across Chrome, Firefox, and WebKit in headless CI, and conduct manual exploratory checks on Safari on real iOS/macOS devices.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does testing on headless Chromium not catch WebKit-specific bugs?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "database_testing",
        "difficulty": "medium",
        "question_text": "How do you conduct Database Testing for backend data integrity during a financial transaction workflow?",
        "expected_answer": "Database testing validates: 1. Data integrity (foreign key constraints, nullability, unique indexes). 2. ACID transaction compliance (if an error occurs midway, debit and credit rollback atomically). 3. Data precision (preventing floating point rounding errors on monetary columns). 4. Audit logging (rows created in ledger tables with correct timestamps and user IDs).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you verify trigger logic during automated backend tests?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "graphql_testing",
        "difficulty": "hard",
        "question_text": "How does testing a GraphQL API differ from testing a REST API? How do you test error responses when GraphQL endpoints always return HTTP status 200 OK?",
        "expected_answer": "Unlike REST which uses multiple endpoints and HTTP status codes (404, 500), GraphQL uses a single POST /graphql endpoint and returns HTTP 200 OK even when errors occur, containing an 'errors' array in the response body. QA must assert: res.status == 200, res.data.errors is empty for happy paths, and inspect errors[0].extensions.code for specific business error validation.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you test query depth and complexity limits to prevent GraphQL denial-of-service?",
        "code_snippet": "assert response.status_code == 200\nbody = response.json()\nassert 'errors' in body\nassert body['errors'][0]['message'] == 'User not found'"
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "shift_left",
        "difficulty": "easy",
        "question_text": "What does 'Shift-Left Testing' mean in Agile DevOps, and how does participating in sprint requirement grooming reduce defects earlier?",
        "expected_answer": "Shift-left moves testing activities earlier into the software development lifecycle (during design and requirement phases) rather than waiting until the end of the sprint. By reviewing user stories during grooming, QA identifies ambiguous acceptance criteria, missing edge cases, and architectural risks before developers write a single line of code, reducing the exponential cost of fixing bugs later.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the relative cost of fixing a bug in requirement phase vs production?",
        "code_snippet": None
    },
    {
        "role": "QA / Software Tester",
        "technology": "qa_testing",
        "category": "websocket_testing",
        "difficulty": "hard",
        "question_text": "How do you test real-time WebSocket applications (e.g. live chat or stock tickers) for connection drops, reconnection resilience, and message ordering?",
        "expected_answer": "Testing WebSockets requires: 1. Verifying handshake upgrade (HTTP 101 Switching Protocols). 2. Testing bidirectional message serialization and schema. 3. Simulating network drops (killing connection) to test heartbeat ping/pong and automatic client reconnection with backoff. 4. Validating message sequencing and deduping when re-establishing connection without lost messages.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What tools or libraries exist to simulate thousands of concurrent WebSocket connections?",
        "code_snippet": None
    }
]
