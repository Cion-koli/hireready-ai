"""
Software Engineer Question Bank - HTML Technology
25 distinct technical questions covering document structure, semantics, forms, media, accessibility, and rendering.
"""

SOFTWARE_ENGINEER_HTML_QUESTIONS = [
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "document_structure",
        "difficulty": "easy",
        "question_text": "What does the '<!DOCTYPE html>' declaration do at the top of an HTML document, and what happens if it is omitted in modern web browsers?",
        "expected_answer": "<!DOCTYPE html> instructs the browser that the document is modern HTML5. If omitted, browsers switch into 'Quirks Mode' to emulate legacy 1990s layout behaviors (altering box sizing, table layout, and CSS interpretation) rather than standard Standards Mode.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is 'Almost Standards Mode' in relation to table cell image rendering?",
        "code_snippet": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <title>Document</title>\n</head>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "semantic_elements",
        "difficulty": "easy",
        "question_text": "What is Semantic HTML, and why is it superior to using generic <div> and <span> elements everywhere? Give examples of five core HTML5 semantic tags.",
        "expected_answer": "Semantic HTML conveys meaning to both browser and developer about the nature of content rather than just visual appearance. Benefits include screen reader accessibility, search engine indexing (SEO), readable maintenance, and automated browser features. Examples: <header>, <nav>, <main>, <article>, <section>, <aside>, <footer>.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the semantic difference between <article> and <section>?",
        "code_snippet": "<main>\n  <article>\n    <h2>Tech Article</h2>\n    <p>Content...</p>\n  </article>\n  <aside>Related Links</aside>\n</main>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "display_elements",
        "difficulty": "easy",
        "question_text": "Explain the difference between block-level and inline elements in HTML. How do inline-block elements behave in relation to margins and dimensions?",
        "expected_answer": "Block elements (<div>, <p>, <h1>) start on a new line and take up the full available width of their container, accepting margin, padding, width, and height. Inline elements (<span>, <a>, <strong>) flow within surrounding text and do not respect top/bottom width or height settings. Inline-block flows inline like text but respects width, height, and vertical margins.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does whitespace in HTML source code create gap spacing between inline-block elements?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "forms",
        "difficulty": "easy",
        "question_text": "Why must every form <input> element be associated with a <label> element, and what are the two distinct ways to bind them in HTML?",
        "expected_answer": "Labels provide accessibility for screen readers (announcing the field purpose on focus) and increase the clickable hit target area for checkboxes/radios. Two ways: 1) Using the 'for' attribute matching the input's 'id' (<label for='user-email'>Email</label><input id='user-email'>), or 2) Nesting the input directly inside the label tag (<label>Email <input type='email'></label>).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the purpose of the 'name' attribute versus the 'id' attribute on form inputs?",
        "code_snippet": "<label for=\"email-input\">Work Email</label>\n<input type=\"email\" id=\"email-input\" name=\"email\" required>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "form_validation",
        "difficulty": "medium",
        "question_text": "Explain native HTML5 client-side form validation attributes: required, pattern, min, max, minlength, and step. Why must server-side validation always accompany them?",
        "expected_answer": "HTML5 attributes enforce validation before form submission: required prevents empty submits; pattern takes regex; min/max/step validate numeric and date ranges; minlength/maxlength limit character counts. Client-side validation can easily be bypassed by disabling JavaScript or using curl/Postman, so server-side validation is non-negotiable for security and data integrity.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can you trigger custom validation messages using the JavaScript Constraint Validation API (setCustomValidity)?",
        "code_snippet": "<input type=\"text\" pattern=\"[A-Z]{3}-[0-9]{4}\" title=\"Format: ABC-1234\" required>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "tables_and_lists",
        "difficulty": "easy",
        "question_text": "Describe the structural elements of an accessible HTML table: <table>, <caption>, <thead>, <tbody>, <tfoot>, <th> with scope attribute, and <td>.",
        "expected_answer": "A semantic table uses <caption> to summarize its purpose, <thead> for header rows, <tbody> for data records, and <tfoot> for aggregate summaries. <th> indicates header cells, and the 'scope' attribute (scope='col' or scope='row') clarifies the header axis for assistive technology.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "When should you use a description list (<dl>, <dt>, <dd>) instead of a table or bulleted list?",
        "code_snippet": "<table>\n  <caption>Quarterly Revenue</caption>\n  <thead>\n    <tr><th scope=\"col\">Quarter</th><th scope=\"col\">Revenue</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Q1</td><td>$100k</td></tr>\n  </tbody>\n</table>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "responsive_images",
        "difficulty": "medium",
        "question_text": "How do you implement modern responsive images in HTML using the <img> srcset/sizes attributes and the <picture> element? When would you choose <picture> over srcset?",
        "expected_answer": "srcset and sizes allow the browser to pick the best image resolution/width for the user's screen density and viewport width (resolution switching). The <picture> element with child <source media='...'> tags is used for art direction (cropping or serving different aspect ratios across breakpoints) or format fallback (serving next-gen AVIF/WebP with PNG/JPEG fallback).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What does loading='lazy' and decoding='async' do on an <img> tag?",
        "code_snippet": "<picture>\n  <source srcset=\"hero.avif\" type=\"image/avif\">\n  <source srcset=\"hero.webp\" type=\"image/webp\">\n  <img src=\"hero.jpg\" alt=\"Hero banner\" width=\"800\" height=\"400\" loading=\"lazy\">\n</picture>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "media_elements",
        "difficulty": "easy",
        "question_text": "How do the <video> and <audio> elements work in HTML5? What are the purpose of the 'controls', 'autoplay', 'muted', and <track> elements?",
        "expected_answer": "<video> and <audio> provide native playback without third-party plugins. 'controls' displays native browser playback UI; 'muted' is typically required by browsers to allow 'autoplay'; multiple <source> elements provide codec fallbacks. <track kind='subtitles|captions' srclang='en'> provides timed text tracks for accessibility.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why do mobile browsers restrict unmuted video autoplay?",
        "code_snippet": "<video controls width=\"640\" poster=\"thumb.jpg\">\n  <source src=\"video.mp4\" type=\"video/mp4\">\n  <track src=\"subs.vtt\" kind=\"subtitles\" srclang=\"en\" label=\"English\">\n</video>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "html5_features",
        "difficulty": "medium",
        "question_text": "What is the HTML5 <dialog> element, and how does the native showModal() method differ from show() regarding backdrop and keyboard accessibility?",
        "expected_answer": "<dialog> provides a standardized native modal element. showModal() opens it as a top-layer modal, automatically rendering a ::backdrop pseudo-element, trapping focus, disabling interaction with the rest of the document (inert behavior), and closing on the 'Escape' key. show() opens it as a non-modal popup without backdrop or focus trap.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does a <form method='dialog'> inside a dialog close it without JavaScript?",
        "code_snippet": "<dialog id=\"confirm-modal\">\n  <form method=\"dialog\">\n    <p>Confirm action?</p>\n    <button value=\"cancel\">Cancel</button>\n    <button value=\"confirm\">Confirm</button>\n  </form>\n</dialog>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "template_element",
        "difficulty": "medium",
        "question_text": "What is the purpose of the <template> element in HTML5, and how does its contents behave in the DOM prior to being cloned?",
        "expected_answer": "<template> holds client-side markup that is not rendered on page load and whose scripts/images/styles are inert (images don't download, scripts don't run). JavaScript accesses its content via template.content.cloneNode(true) to stamp out reusable dynamic components efficiently.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does <template> work alongside custom elements and Shadow DOM in Web Components?",
        "code_snippet": "<template id=\"card-tmpl\">\n  <div class=\"card\">\n    <h3 class=\"title\"></h3>\n    <p class=\"desc\"></p>\n  </div>\n</template>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "accessibility_aria",
        "difficulty": "medium",
        "question_text": "What are ARIA attributes (Accessible Rich Internet Applications), and what does the 'First Rule of ARIA' dictate regarding native HTML elements?",
        "expected_answer": "ARIA attributes (aria-label, aria-expanded, role, aria-live) bridge accessibility gaps when custom interactive widgets cannot be built with native tags. The First Rule of ARIA states: 'If you can use a native HTML element or attribute with the semantics and behavior already built in, do so instead of re-purposing an element and adding ARIA.' E.g., use <button> instead of <div role='button'>.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is aria-live='polite' versus aria-live='assertive'?",
        "code_snippet": "<button aria-expanded=\"false\" aria-controls=\"menu-panel\">\n  Menu\n</button>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "seo_metadata",
        "difficulty": "easy",
        "question_text": "What metadata tags should be included in an HTML <head> for optimal search engine optimization (SEO) and social sharing (OpenGraph and Twitter Cards)?",
        "expected_answer": "Essential tags: <title>, <meta name='description'>, <meta name='robots'>, <link rel='canonical'>. For social preview cards: OpenGraph (<meta property='og:title'>, og:description, og:image, og:url, og:type) and Twitter Cards (<meta name='twitter:card'>, twitter:title, twitter:image).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the purpose of structured data using JSON-LD in a <script type='application/ld+json'> tag?",
        "code_snippet": "<meta property=\"og:title\" content=\"HireReady AI\">\n<meta property=\"og:image\" content=\"https://site.com/og.png\">\n<meta name=\"twitter:card\" content=\"summary_large_image\">"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "viewport_settings",
        "difficulty": "easy",
        "question_text": "Explain the role of '<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">' in responsive web design. What happens on mobile devices if it is omitted?",
        "expected_answer": "It instructs mobile browsers to render the viewport at the physical device screen width with a 1:1 scale rather than defaulting to an assumed desktop width (commonly 980px), preventing text and layouts from appearing tiny and requiring pinch-to-zoom.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is user-scalable=no or maximum-scale=1.0 considered an accessibility violation?",
        "code_snippet": "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "dom_structure",
        "difficulty": "medium",
        "question_text": "What is the Document Object Model (DOM), and what is the difference between an HTML element and a DOM node?",
        "expected_answer": "The DOM is a tree representation of the HTML document created by the browser, providing a programmable API for JavaScript. Every element in the DOM is a Node, but nodes also include text nodes (whitespace, text strings), comment nodes, and the document node itself. Elements are a specific type of node (Node.ELEMENT_NODE).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between childNodes and children on a DOM element?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "identifiers",
        "difficulty": "easy",
        "question_text": "Explain the differences and appropriate use cases for the 'id' and 'class' attributes in HTML. Can an element have multiple classes or multiple IDs?",
        "expected_answer": "'id' must be unique per HTML page, used for single fragment navigation (#section), form label associations, and specific element hooks. 'class' is non-unique and can be applied to many elements for shared styling and component categorization. Elements can have multiple space-separated classes, but only a single ID.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What happens in CSS specificity when selecting an element by #id versus .class?",
        "code_snippet": "<button id=\"submit-btn\" class=\"btn btn-primary btn-large\">Submit</button>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "script_loading",
        "difficulty": "hard",
        "question_text": "Compare regular '<script>', '<script async>', and '<script defer>' in terms of HTML parsing blocking, download timing, and execution order.",
        "expected_answer": "Regular <script> blocks HTML parsing while downloading and executing. 'async' downloads in parallel with HTML parsing and executes immediately when downloaded, interrupting HTML parsing and having no guaranteed execution order. 'defer' downloads in parallel with HTML parsing but waits to execute in document order after HTML parsing is complete, just before DOMContentLoaded.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do <script type='module'> scripts load by default?",
        "code_snippet": "<!-- Executes in document order after parse -->\n<script defer src=\"app.js\"></script>\n<!-- Executes as soon as downloaded -->\n<script async src=\"analytics.js\"></script>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "custom_data_attributes",
        "difficulty": "easy",
        "question_text": "What are custom data attributes ('data-*') in HTML, how are they formatted, and how are they accessed in JavaScript and CSS?",
        "expected_answer": "data-* attributes store extra arbitrary data on standard HTML elements without affecting layout. In JavaScript, they are accessed via element.dataset.propertyName (camelCased, so data-user-id becomes dataset.userId). In CSS, they can be selected using attribute selectors (e.g. [data-theme='dark']).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why should sensitive data never be stored in HTML data-* attributes?",
        "code_snippet": "<article id=\"post-1\" data-category=\"tech\" data-author-id=\"42\"></article>\n<script>\n  const cat = document.getElementById('post-1').dataset.category;\n</script>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "form_submission",
        "difficulty": "medium",
        "question_text": "What is the difference between GET and POST in an HTML form's 'method' attribute? What does the 'enctype' attribute do, especially for file uploads?",
        "expected_answer": "method='GET' appends form data as URL query parameters (suitable for idempotent searches, visible in history/logs, size limited). method='POST' sends data in the HTTP request body (suitable for state modifications, passwords, file uploads). When uploading files (<input type='file'>), enctype='multipart/form-data' is required; otherwise only the file name is sent.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the default value of enctype if omitted (application/x-www-form-urlencoded)?",
        "code_snippet": "<form action=\"/upload\" method=\"POST\" enctype=\"multipart/form-data\">\n  <input type=\"file\" name=\"resume\" accept=\".pdf,.docx\">\n  <button type=\"submit\">Upload</button>\n</form>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "storage_concepts",
        "difficulty": "medium",
        "question_text": "Compare HTML client storage mechanisms: Cookies, localStorage, and sessionStorage in terms of capacity, lifecycle, and server communication.",
        "expected_answer": "Cookies store ~4KB, have configurable expiration (or session), and are automatically sent to the server with every HTTP request. localStorage stores ~5-10MB, persists indefinitely until explicitly cleared, and is purely client-side. sessionStorage stores ~5-10MB, persists only for the lifetime of the browser tab, and is also client-side only.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What security flags can be set on cookies (HttpOnly, Secure, SameSite)?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "critical_rendering_path",
        "difficulty": "hard",
        "question_text": "Explain the Critical Rendering Path. How does the browser convert raw HTML bytes into pixels on the screen?",
        "expected_answer": "1) Bytes -> Characters -> Tokens -> Nodes -> DOM Tree. 2) In parallel, CSS bytes are parsed into the CSSOM Tree. 3) DOM + CSSOM are combined into the Render Tree (excluding display:none nodes). 4) Layout (Reflow) calculates precise geometries and coordinates of each node. 5) Paint rasterizes the visual elements into layers. 6) Composite layers are merged on GPU for screen display.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do render-blocking stylesheets affect the First Contentful Paint (FCP)?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "web_security",
        "difficulty": "hard",
        "question_text": "What is Cross-Site Scripting (XSS), and how does proper HTML character entity escaping prevent stored and reflected XSS attacks?",
        "expected_answer": "XSS occurs when malicious scripts are injected into web pages viewed by other users. If untrusted user input is injected into the DOM without escaping, browser HTML parsers interpret it as executable tags (<script> or <img onerror>). Escaping characters like & -> &amp;, < -> &lt;, > -> &gt;, \" -> &quot;, ' -> &#x27; ensures the browser treats them as inert text content, not executable markup.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does the Content Security Policy (CSP) header provide defense-in-depth against XSS?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "iframes",
        "difficulty": "medium",
        "question_text": "What is an <iframe> element, what security risks are associated with it (clickjacking), and how does the 'sandbox' attribute mitigate them?",
        "expected_answer": "An <iframe> embeds an independent HTML document inside the current page. Clickjacking occurs when malicious sites embed your site invisibly to trick users into clicking buttons. The 'sandbox' attribute applies strict restrictions (disabling scripts, forms, popups, and same-origin access) unless specific permissions are whitelisted (sandbox='allow-scripts allow-same-origin').",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does the X-Frame-Options or CSP frame-ancestors header protect a site from being iframed?",
        "code_snippet": "<iframe src=\"https://example.com/widget\" sandbox=\"allow-scripts\" title=\"Widget\"></iframe>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "svg_and_canvas",
        "difficulty": "medium",
        "question_text": "Compare inline <svg> with the HTML5 <canvas> element. When would you choose SVG over Canvas for interactive graphics?",
        "expected_answer": "SVG is XML vector-based, part of the DOM, resolution-independent, styleable with CSS, and individual shapes can have event listeners and accessibility attributes. Canvas is raster bitmap-based with an immediate-mode 2D/WebGL drawing API, fast for rendering thousands of moving objects or game graphics, but without DOM nodes for individual shapes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you make an inline SVG accessible to screen readers?",
        "code_snippet": "<svg viewBox=\"0 0 100 100\" role=\"img\" aria-label=\"Success icon\">\n  <circle cx=\"50\" cy=\"50\" r=\"40\" fill=\"green\" />\n</svg>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "resource_hints",
        "difficulty": "hard",
        "question_text": "Explain resource hints in HTML: rel='preload', rel='prefetch', rel='preconnect', and rel='dns-prefetch'. When should each be used to optimize page performance?",
        "expected_answer": "'preconnect' initiates early DNS, TCP, and TLS handshakes to a third-party origin. 'dns-prefetch' resolves domain IP ahead of time. 'preload' forces high-priority download of a critical resource needed immediately on the current page (e.g. fonts, hero image, critical CSS). 'prefetch' downloads low-priority resources expected to be needed on subsequent page navigations.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What happens if a resource is preloaded using rel='preload' but not used within 3 seconds?",
        "code_snippet": "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n<link rel=\"preload\" href=\"/fonts/inter.woff2\" as=\"font\" type=\"font/woff2\" crossorigin>"
    },
    {
        "role": "Software Engineer",
        "technology": "html",
        "category": "page_structure_scenario",
        "difficulty": "medium",
        "question_text": "Structure an accessible, SEO-optimized HTML5 landing page layout with a skip-link, header, navigation, main hero section, features list, accessible contact form, and footer.",
        "expected_answer": "Candidate should structure: 1) Skip-to-content link (<a href='#main' class='sr-only'>Skip to content</a>), 2) <header> containing logo and <nav aria-label='Main'>, 3) <main id='main'> with <h1> in hero, 4) <section> with <h2> and list for features, 5) <form> with explicit <label> associations and validation, 6) <footer> with copyright and legal links.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is having only one <h1> per page considered a best practice for accessibility and heading hierarchy?",
        "code_snippet": "<body>\n  <a href=\"#main\" class=\"skip-link\">Skip to main content</a>\n  <header><nav aria-label=\"Main navigation\"></nav></header>\n  <main id=\"main\"></main>\n  <footer></footer>\n</body>"
    }
]
