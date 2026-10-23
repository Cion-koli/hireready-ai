"""
Software Engineer Question Bank - CSS Technology
25 distinct technical questions covering box model, layout systems, specificity, responsiveness, and performance.
"""

SOFTWARE_ENGINEER_CSS_QUESTIONS = [
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "box_model",
        "difficulty": "easy",
        "question_text": "Explain the standard CSS Box Model. How does 'box-sizing: border-box' differ from 'box-sizing: content-box', and why is border-box widely set as a global default in modern resets?",
        "expected_answer": "The box model consists of Content, Padding, Border, and Margin. In content-box (default), width/height apply strictly to content, so padding and border add to the element's rendered width. In border-box, width/height include padding and border, making responsive grid and percentage calculations intuitive and predictable.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do margins affect the total space taken by an element under border-box?",
        "code_snippet": "*, *::before, *::after {\n  box-sizing: border-box;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "specificity",
        "difficulty": "medium",
        "question_text": "How does CSS Specificity calculate which rule wins when conflicting declarations target the same element? Rank: inline styles, ID selectors, class/pseudo-class/attribute selectors, and element/pseudo-element selectors. How does '!important' affect this?",
        "expected_answer": "Specificity follows a 4-category hierarchy (a, b, c, d): a = inline styles (1000); b = IDs (0100); c = classes, attributes, pseudo-classes (0010); d = elements and pseudo-elements (0001). Highest specificity rule wins. '!important' overrides normal specificity declarations, and can only be overridden by another '!important' with equal or higher specificity.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the specificity of the universal selector (*) and the :where() pseudo-class?",
        "code_snippet": "/* Specificity: 0, 1, 1, 1 */\n#header .nav a {\n  color: blue;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "margin_collapse",
        "difficulty": "medium",
        "question_text": "What is Margin Collapsing in CSS, in what scenarios does it occur, and how can it be prevented?",
        "expected_answer": "Margin collapsing occurs when vertical margins of adjacent block elements combine into a single margin equal to the largest margin. It occurs between adjacent siblings, parent and first/last child with no intervening padding/border, and empty blocks. It does NOT occur on flex items, grid items, floats, or absolute positioned elements.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does creating a Block Formatting Context (BFC) prevent child margin collapsing?",
        "code_snippet": "h1 { margin-bottom: 30px; }\np { margin-top: 20px; }\n/* Total space between them is 30px, not 50px */"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "positioning",
        "difficulty": "medium",
        "question_text": "Explain the differences between the CSS position values: static, relative, absolute, fixed, and sticky. What determines the containing block for 'position: absolute'?",
        "expected_answer": "static: normal document flow. relative: normal flow, offset relative to itself without affecting siblings. absolute: removed from normal flow, positioned relative to nearest ancestor with position other than static (or root). fixed: removed from flow, positioned relative to viewport. sticky: hybrid relative/fixed, toggles based on scroll position within its parent container.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does a sticky element fail to stick if an ancestor has 'overflow: hidden'?",
        "code_snippet": ".parent { position: relative; }\n.badge { position: absolute; top: -5px; right: -5px; }"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "flexbox_basics",
        "difficulty": "easy",
        "question_text": "Explain the concept of Main Axis and Cross Axis in CSS Flexbox. How do 'justify-content' and 'align-items' control element distribution along these axes?",
        "expected_answer": "Flex container axes depend on flex-direction: if 'row' (default), main axis is horizontal and cross axis is vertical; if 'column', main axis is vertical and cross axis is horizontal. 'justify-content' aligns and distributes items along the main axis. 'align-items' aligns items along the cross axis.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between align-items and align-content in flexbox?",
        "code_snippet": ".container {\n  display: flex;\n  flex-direction: row;\n  justify-content: space-between;\n  align-items: center;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "flexbox_sizing",
        "difficulty": "medium",
        "question_text": "Explain the three properties represented by the 'flex' shorthand: flex-grow, flex-shrink, and flex-basis. What does 'flex: 1' mean?",
        "expected_answer": "flex-grow: relative proportion of remaining available space this item should absorb. flex-shrink: ability to contract when total items exceed container space. flex-basis: default size of item before space distribution. 'flex: 1' expands to 'flex: 1 1 0%', meaning items start at 0 basis and grow equally to share space.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why might a flex item with flex-grow: 1 fail to shrink if content overflows?",
        "code_snippet": ".col {\n  flex: 1 1 auto;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "css_grid",
        "difficulty": "medium",
        "question_text": "Compare CSS Grid and CSS Flexbox. When is CSS Grid the superior choice, and how do fractional units ('fr') work in grid-template-columns?",
        "expected_answer": "Flexbox is one-dimensional (row OR column), ideal for content-first alignment and UI components (navbars, card headers). Grid is two-dimensional (simultaneous rows AND columns), ideal for layout-first page skeletons and dashboards. The 'fr' unit represents a fraction of remaining free space in the grid container after fixed tracks are allocated.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do grid-template-areas improve layout readability?",
        "code_snippet": ".grid {\n  display: grid;\n  grid-template-columns: 200px 1fr 2fr;\n  gap: 1.5rem;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "grid_auto_fit",
        "difficulty": "hard",
        "question_text": "Explain the difference between 'auto-fill' and 'auto-fit' when used with repeat() and minmax() in CSS Grid for responsive layouts without media queries.",
        "expected_answer": "Both create responsive column tracks using 'repeat(auto-fill|auto-fit, minmax(250px, 1fr))'. auto-fill creates as many tracks as can physically fit into the container, even if empty. auto-fit creates the tracks, but collapses any empty tracks down to 0px, causing the occupied tracks to stretch to fill the entire container width.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is minmax(min(100%, 250px), 1fr) useful on small mobile viewports?",
        "code_snippet": ".cards-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n  gap: 1rem;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "units",
        "difficulty": "easy",
        "question_text": "Explain the difference between rem and em units in CSS. When should you use rem versus em for typography, padding, and component scalability?",
        "expected_answer": "rem is relative to the root <html> element's font-size (usually 16px by default), making it consistent and immune to cascading compounding. em is relative to the immediate parent's (or current element's) font-size, which compounds in nested lists or trees. Best practice: rem for typography and layout margins; em for component padding/margins that should scale proportionally with local font-size.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What are viewport units (vw, vh, dvh, svh, lvh) and why were dynamic viewport units introduced for mobile browsers?",
        "code_snippet": "html { font-size: 16px; }\n.btn { font-size: 1rem; padding: 0.5em 1em; }"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "pseudo_classes_elements",
        "difficulty": "medium",
        "question_text": "What is the difference between a pseudo-class (single colon, e.g. :hover) and a pseudo-element (double colon, e.g. ::before)? How does the 'content' property work with ::before and ::after?",
        "expected_answer": "Pseudo-classes select elements based on state or DOM position (:hover, :focus, :nth-child). Pseudo-elements create virtual DOM sub-elements that don't exist in HTML source (::before, ::after, ::placeholder). ::before and ::after require the 'content: \"\"' property (even if empty) to render, functioning like inline children of the selected element.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between :nth-child(n) and :nth-of-type(n)?",
        "code_snippet": ".badge::after {\n  content: '';\n  display: inline-block;\n  width: 8px; height: 8px;\n  border-radius: 50%;\n  background: red;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "centering",
        "difficulty": "easy",
        "question_text": "Demonstrate three modern ways to perfectly center an element both horizontally and vertically inside a parent container.",
        "expected_answer": "1) Flexbox: parent has display: flex; justify-content: center; align-items: center; 2) Grid: parent has display: grid; place-items: center; 3) Absolute + transform: child has position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); (or margin: auto on flex/grid child).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why was vertical centering notoriously difficult before Flexbox?",
        "code_snippet": ".parent {\n  display: grid;\n  place-items: center;\n  min-height: 100vh;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "stacking_context",
        "difficulty": "hard",
        "question_text": "What is a Stacking Context in CSS, and why doesn't setting 'z-index: 999999' on an element guarantee it appears above everything else on the page?",
        "expected_answer": "A Stacking Context is a 3D conceptual layer containing child elements. Elements within a stacking context are layered relative to each other; their z-index cannot break out of their parent stacking context. New stacking contexts are formed by: opacity < 1, transform/filter/will-change, position relative/absolute with z-index, position: fixed, or isolation: isolate.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does 'isolation: isolate' prevent z-index leakage in modern CSS?",
        "code_snippet": "/* Parent creates new stacking context */\n.modal-host {\n  isolation: isolate;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "visibility_comparison",
        "difficulty": "easy",
        "question_text": "Compare 'display: none', 'visibility: hidden', and 'opacity: 0' in terms of layout reflow, accessibility screen-reader announcement, and click event handling.",
        "expected_answer": "display: none removes the element from render tree completely, takes 0 space, causes reflow, is invisible to screen readers, and cannot receive click events. visibility: hidden keeps its physical space in layout, causes repaint without reflow, is hidden from screen readers, and cannot receive click events. opacity: 0 keeps space in layout, is accessible to screen readers, and still receives click events unless pointer-events: none is set.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is 'display: none' impossible to animate directly with CSS transitions?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "custom_properties",
        "difficulty": "medium",
        "question_text": "How do CSS Custom Properties (variables) work? Explain scope, inheritance, fallback values, and how they simplify dark mode / light mode theming.",
        "expected_answer": "CSS variables are declared with '--name: value' and consumed with 'var(--name, fallback)'. They cascade and inherit through the DOM tree. Defining them in :root allows global theming; dark mode can be implemented cleanly by overriding custom property values inside a '@media (prefers-color-scheme: dark)' block or '[data-theme=\"dark\"]' selector.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can JavaScript read and update CSS custom properties at runtime (getPropertyValue / setProperty)?",
        "code_snippet": ":root {\n  --bg-primary: #ffffff;\n  --text-primary: #0f172a;\n}\n[data-theme=\"dark\"] {\n  --bg-primary: #070b14;\n  --text-primary: #f8fafc;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "transitions_animations",
        "difficulty": "medium",
        "question_text": "What is the difference between a CSS transition and a CSS keyframe animation (@keyframes)? When should you use each?",
        "expected_answer": "Transitions animate property changes smoothly between two states (from A to B) triggered by an event (:hover, class toggle). Keyframe animations (@keyframes) can run autonomously on page load, loop infinitely, and define multiple intermediate waypoints (0%, 25%, 50%, 100%) with fine-grained control over direction, delay, and fill-mode.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What does 'animation-fill-mode: forwards' do?",
        "code_snippet": "@keyframes spin {\n  from { transform: rotate(0deg); }\n  to { transform: rotate(360deg); }\n}\n.loader { animation: spin 1s linear infinite; }"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "performance",
        "difficulty": "hard",
        "question_text": "Why are animating 'transform' and 'opacity' considered high-performance (60fps), while animating 'width', 'top', or 'margin' can cause jank? Explain Reflow vs Repaint.",
        "expected_answer": "Changing 'width', 'top', or 'margin' triggers Reflow (Layout recalculations) and Repaint (rasterizing pixels) across affected document geometry, processed on the CPU main thread. 'transform' and 'opacity' bypass layout and paint, executing directly on the GPU during the Composite phase via hardware acceleration without blocking the main JavaScript thread.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What does the 'will-change' property do, and why should it be used sparingly?",
        "code_snippet": "/* High performance GPU transform */\n.card:hover {\n  transform: translateY(-4px);\n  opacity: 0.95;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "responsive_design",
        "difficulty": "medium",
        "question_text": "Explain the 'Mobile-First' design strategy in CSS. Why are 'min-width' media queries preferred over 'max-width' in production style architectures?",
        "expected_answer": "Mobile-First writes baseline styles for small screens first without media queries, then progressively enhances layout for larger screens using min-width queries (@media (min-width: 768px)). This delivers faster initial render on mobile devices by avoiding rule overriding, reduces CSS bloat, and aligns with mobile web traffic dominance.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the new CSS Range Syntax for media queries (@media (width >= 768px))?",
        "code_snippet": "/* Mobile base */\n.grid { grid-template-columns: 1fr; }\n/* Tablet+ */\n@media (min-width: 768px) {\n  .grid { grid-template-columns: repeat(2, 1fr); }\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "accessibility_focus",
        "difficulty": "medium",
        "question_text": "Why is removing focus outlines with 'outline: none' without a replacement an accessibility violation? Explain the ':focus-visible' pseudo-class.",
        "expected_answer": "Keyboard navigation users rely on focus indicators to know which element is currently active. Removing outline makes the site unusable for keyboard users (WCAG 2.4.7 failure). The :focus-visible pseudo-class applies outlines selectively only when the user is navigating via keyboard or assistive tech, avoiding outline distraction on mouse clicks while preserving accessibility.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you style a high-contrast focus indicator using outline-offset?",
        "code_snippet": ":focus:not(:focus-visible) {\n  outline: none;\n}\n:focus-visible {\n  outline: 2px solid #6366f1;\n  outline-offset: 2px;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "overflow",
        "difficulty": "easy",
        "question_text": "Explain the values of the CSS 'overflow' property: visible, hidden, scroll, and auto. What is the difference between 'overflow: scroll' and 'overflow: auto'?",
        "expected_answer": "visible (default): content bleeds outside the container. hidden: content is clipped, no scrollbars provided. scroll: clips content and always shows scrollbars even if content fits. auto: clips content and only renders scrollbars when content exceeds container boundaries.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do overflow-x and overflow-y permit independent horizontal/vertical scrolling?",
        "code_snippet": ".scroll-container {\n  overflow-y: auto;\n  overflow-x: hidden;\n  max-height: 400px;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "modern_pseudo_classes",
        "difficulty": "hard",
        "question_text": "Explain modern CSS pseudo-classes: :is(), :where(), and :has(). Why is :has() considered a 'parent selector'?",
        "expected_answer": ":is() and :where() group selector lists compactly; :is() takes the specificity of its most specific argument, while :where() always has 0 specificity. :has() is the relational parent selector: it selects an element if it contains or is followed by elements matching its argument (e.g. 'article:has(img)' styles articles containing an image).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does form:has(:invalid) allow styling form containers based on input validity?",
        "code_snippet": "/* Select card only if it contains a featured badge */\n.card:has(.badge-featured) {\n  border-color: gold;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "clipping_and_masking",
        "difficulty": "medium",
        "question_text": "What is the CSS clip-path property, and how does it differ from border-radius for creating complex shapes?",
        "expected_answer": "clip-path cuts an element into non-rectangular shapes (polygons, circles, ellipses, SVG paths). Unlike border-radius which only rounds corners, clip-path physically discards outer pixels, preventing clicks on clipped regions, and allows arbitrary geometric masks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Can clip-path polygons with identical vertex counts be animated smoothly?",
        "code_snippet": ".hero-diagonal {\n  clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "typography_clamping",
        "difficulty": "medium",
        "question_text": "Explain fluid typography using the clamp() function: clamp(minimum, preferred, maximum). How does it eliminate rigid breakpoint font sizes?",
        "expected_answer": "clamp(MIN, VAL, MAX) clamps a value between lower and upper bounds. In fluid typography (e.g. font-size: clamp(1.5rem, 4vw, 3rem)), the font scales dynamically with viewport width (4vw) without exceeding the minimum (1.5rem on mobile) or maximum (3rem on wide desktop), eliminating jumpy media query changes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do min() and max() work in CSS mathematical expressions?",
        "code_snippet": "h1 {\n  font-size: clamp(2rem, 5vw + 1rem, 4.5rem);\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "print_styling",
        "difficulty": "easy",
        "question_text": "How do you design a print stylesheet using '@media print', and what common styles should be applied for clean physical document printing?",
        "expected_answer": "'@media print' targets physical printing or PDF export. Best practices: hide navigational bars, buttons, and decorative elements (.no-print { display: none; }); set light background and black text; reset fixed or scrollable containers; and use 'break-inside: avoid' to prevent cards from splitting across page breaks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can you print URLs next to anchor links using CSS (a::after { content: ' (' attr(href) ')'; })?",
        "code_snippet": "@media print {\n  nav, footer, .btn { display: none !important; }\n  body { background: white; color: black; }\n  .card { break-inside: avoid; }\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "aspect_ratio",
        "difficulty": "easy",
        "question_text": "How does the modern 'aspect-ratio' property solve responsive container sizing, and how was this achieved historically using the padding-bottom hack?",
        "expected_answer": "'aspect-ratio: 16 / 9' instructs the browser to automatically maintain an element's dimensional proportions as its width changes, preventing Cumulative Layout Shift (CLS). Historically, developers had to use a zero-height container with 'padding-top: 56.25%' (9/16 * 100%) and position child elements absolutely inside it.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does preserving aspect ratio on image containers reduce Cumulative Layout Shift (CLS)?",
        "code_snippet": ".video-wrapper {\n  width: 100%;\n  aspect-ratio: 16 / 9;\n}"
    },
    {
        "role": "Software Engineer",
        "technology": "css",
        "category": "glassmorphism_filters",
        "difficulty": "medium",
        "question_text": "Explain how the 'backdrop-filter: blur()' property creates glassmorphism UI effects. How does backdrop-filter differ from the standard 'filter' property?",
        "expected_answer": "filter: blur() blurs the target element itself and all of its child content. backdrop-filter: blur() blurs the content and background lying *behind* the target element, leaving the element's foreground text and borders crisp and readable. Glassmorphism combines semi-transparent background (rgba), subtle border, and backdrop-filter: blur().",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is a background color with opacity < 1 essential for backdrop-filter to be visible?",
        "code_snippet": ".glass-card {\n  background: rgba(17, 28, 53, 0.75);\n  backdrop-filter: blur(16px);\n  border: 1px solid rgba(255, 255, 255, 0.1);\n}"
    }
]
