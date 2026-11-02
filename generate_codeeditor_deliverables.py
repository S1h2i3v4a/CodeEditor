"""
generate_codeeditor_deliverables.py
Generates official, highly structured academic project deliverables for CodeEditor:
1. CodeEditor_Project_Report.pdf (14-page report, starting directly from Index, no college name, embedded flowchart & UI architecture)
2. CodeEditor_Presentation.pdf (Widescreen 16:9 presentation, direct Table of Contents / clean title, zero college branding, embedded DFD & flowchart)
3. CodeEditor_Presentation.pptx (Editable PowerPoint version)
"""

import os
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

BASE_DIR = r"c:\Users\Shivam Keshari\OneDrive\Desktop\Code_Editor"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

FLOWCHART_PATH = os.path.join(ASSETS_DIR, "codeeditor_flowchart.png")
DFD_PATH = os.path.join(ASSETS_DIR, "codeeditor_dfd.png")
UI_DIAGRAM_PATH = os.path.join(ASSETS_DIR, "codeeditor_ui_diagram.png")

REPORT_PDF_PATH = os.path.join(DOCS_DIR, "CodeEditor_Project_Report.pdf")
REPORT_PDF_ROOT = os.path.join(BASE_DIR, "CodeEditor_Project_Report.pdf")

PRES_PDF_PATH = os.path.join(DOCS_DIR, "CodeEditor_Presentation.pdf")
PRES_PDF_ROOT = os.path.join(BASE_DIR, "CodeEditor_Presentation.pdf")
PRES_PPTX_PATH = os.path.join(DOCS_DIR, "CodeEditor_Presentation.pptx")

W, H = A4  # 595.27 x 841.89 pt
LEFT_MARGIN = 72
RIGHT_MARGIN = W - 72
CONTENT_WIDTH = RIGHT_MARGIN - LEFT_MARGIN


def draw_bullet(c, x, y, radius=2):
    c.circle(x, y + 3.5, radius, fill=1, stroke=0)


def draw_para(c, text, x, y, font="Times-Roman", font_size=11, leading=15, width=CONTENT_WIDTH, align="left"):
    c.setFont(font, font_size)
    lines = simpleSplit(text, font, font_size, width)
    for line in lines:
        if align == "center":
            c.drawCentredString(W / 2, y, line)
        elif align == "right":
            c.drawRightString(RIGHT_MARGIN, y, line)
        else:
            c.drawString(x, y, line)
        y -= leading
    return y


def draw_page_number(c, num):
    c.setFont("Times-Roman", 10)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawCentredString(W / 2, 40, str(num))


# ==============================================================================
# 1. REPORT PDF GENERATION (CodeEditor Pro)
# ==============================================================================
def build_report_pdf():
    c = canvas.Canvas(REPORT_PDF_PATH, pagesize=A4)

    # -------------------------------------------------------------------------
    # PAGE 1: INDEX (TABLE OF CONTENTS) - Direct Start, No College Name
    # -------------------------------------------------------------------------
    y = H - 85
    c.setFont("Times-Bold", 22)
    c.setFillColor(colors.black)
    c.drawCentredString(W / 2, y, "Index")

    y -= 45
    table_top = y
    row_heights = [32, 28, 28, 28, 28, 28, 28, 28, 28, 28]
    total_table_height = sum(row_heights)
    col_x = [LEFT_MARGIN, LEFT_MARGIN + 45, RIGHT_MARGIN - 70, RIGHT_MARGIN]

    # Outer Border
    c.setStrokeColor(colors.black)
    c.setLineWidth(0.8)
    c.rect(col_x[0], table_top - total_table_height, CONTENT_WIDTH, total_table_height)

    # Vertical Column Lines
    for x in col_x[1:-1]:
        c.line(x, table_top, x, table_top - total_table_height)

    index_rows = [
        ("S.\nNo", "Topic", "Page No."),
        ("1", "Introduction", "1"),
        ("2", "Requirement", "2"),
        ("3", "Conceptual Background", "3 to 5"),
        ("4", "Implementation", "6"),
        ("4.1", "Coding", "6 to 9"),
        ("4.2", "Flow Chart", "10"),
        ("5", "User Interface & Architecture", "11"),
        ("6", "Conclusion", "12"),
        ("", "References", "13")
    ]

    curr_y = table_top
    for r_idx, (sno, topic, pg) in enumerate(index_rows):
        rh = row_heights[r_idx]
        c.line(col_x[0], curr_y, col_x[-1], curr_y)

        is_header = (r_idx == 0)
        c.setFont("Times-Bold" if is_header else "Times-Roman", 11 if not is_header else 11.5)

        if "\n" in sno:
            c.drawCentredString((col_x[0] + col_x[1]) / 2, curr_y - 12, "S.")
            c.drawCentredString((col_x[0] + col_x[1]) / 2, curr_y - 24, "No")
        else:
            c.drawCentredString((col_x[0] + col_x[1]) / 2, curr_y - rh / 2 - 4, sno)

        indent = 15 if "." in sno else 8
        c.drawString(col_x[1] + indent, curr_y - rh / 2 - 4, topic)
        c.drawString(col_x[2] + 10, curr_y - rh / 2 - 4, pg)
        curr_y -= rh

    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 2 (Body Page 1): CHAPTER-1 INTRODUCTION & PROBLEM STATEMENT
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-1")
    y -= 18
    c.drawCentredString(W / 2, y, "Introduction")

    y -= 30
    intro_p1 = (
        "Modern web development requires fast, responsive, and friction-free feedback loops during the code "
        "authoring and experimentation process. In conventional development environments, developers must set "
        "up local project directories, maintain continuous build processes, manage local servers, and switch between "
        "code editors and browser windows. This workflow introduces latency and friction when testing micro-interactions, "
        "prototyping frontend components, or learning foundational technologies such as HTML5, CSS3, and JavaScript."
    )
    y = draw_para(c, intro_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=15)
    y -= 12

    intro_p2 = (
        "Web-based code playgrounds, also known as browser IDEs, solve these bottlenecks by providing an integrated, "
        "zero-install development platform accessible through standard web browsers. By evaluating and executing code "
        "entirely on the client side, such playgrounds eliminate network roundtrips, provide instantaneous visual output, "
        "and foster rapid creative prototyping."
    )
    y = draw_para(c, intro_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=15)
    y -= 12

    intro_p3 = (
        "The CodeEditor Pro project is a high-performance, browser-based web playground engineered to provide real-time, "
        "debounced live compilation of HTML5 markup, CSS3 styling, and JavaScript logic. The application features an "
        "isolated sandboxing architecture that executes untrusted user scripts securely without compromising the host "
        "page session, while maintaining high execution efficiency."
    )
    y = draw_para(c, intro_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=15)
    y -= 12

    intro_p4 = (
        "In addition to real-time rendering, CodeEditor Pro features an integrated virtual developer console that "
        "intercepts standard logging operations and runtime exceptions from the sandboxed frame, dynamic line numbering, "
        "tab indentation handling, starter design templates, one-click standalone bundle export, and local persistence."
    )
    y = draw_para(c, intro_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=15)

    y -= 22
    c.setFont("Times-Bold", 12.5)
    c.drawCentredString(W / 2, y, "Problem Statement")

    y -= 20
    ps_p1 = (
        "Existing lightweight online code editors frequently suffer from severe architectural limitations. The most "
        "common flaw is the unrestricted appending of style elements and script tags directly to the preview DOM on "
        "every keystroke. This behavior causes unbounded memory growth, duplicate variable collisions, and stale event "
        "listener accumulation, resulting in browser tab crashes."
    )
    y = draw_para(c, ps_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=15)
    y -= 12

    ps_p2 = (
        "Furthermore, many client-side playgrounds lack in-editor developer consoles, forcing users to open external "
        "browser dev tools to view console output and syntax errors. Others lack essential code-editing ergonomics, "
        "such as Tab indentation support, synchronized line gutters, code formatting, and offline persistence."
    )
    y = draw_para(c, ps_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=15)
    y -= 12

    ps_p3 = (
        "There is a need for a modern, self-contained, and architecturally sound web playground that guarantees safe "
        "sandboxed evaluation, debounced execution lifecycle management, and a rich developer experience without heavy "
        "framework dependencies or backend servers."
    )
    y = draw_para(c, ps_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=15)

    draw_page_number(c, 1)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 3 (Body Page 2): CHAPTER-2 REQUIREMENT
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-2")
    y -= 18
    c.drawCentredString(W / 2, y, "Requirement")

    y -= 30
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "2.1 Hardware Requirements")
    y -= 18

    c.setFont("Times-Roman", 10.5)
    c.drawString(LEFT_MARGIN, y, "The system runs entirely on standard consumer hardware without requiring dedicated GPU or server infrastructure:")
    y -= 16

    hw_items = [
        "Device: Desktop, laptop, tablet, or smartphone.",
        "Processor: Dual-core 1.6 GHz modern x86/ARM CPU or higher.",
        "RAM: Minimum 2 GB memory; 4 GB or higher recommended for multi-tab browsing.",
        "Display: Minimum 1024 x 768 resolution for optimal split-view display; fully responsive for mobile.",
        "Input: Standard keyboard and mouse, trackpad, or touch interface.",
        "Storage: Under 5 MB disk space (zero installation overhead)."
    ]
    for item in hw_items:
        draw_bullet(c, LEFT_MARGIN + 15, y)
        c.drawString(LEFT_MARGIN + 25, y, item)
        y -= 16

    y -= 18
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "2.2 Software Requirements")
    y -= 18

    c.setFont("Times-Roman", 10.5)
    c.drawString(LEFT_MARGIN, y, "The CodeEditor Pro platform is built using modern open web standards:")
    y -= 16

    sw_items = [
        ("HTML5: ", "Provides semantic structure, textarea editors, canvas runtime, and sandboxed iframe container."),
        ("CSS3 (Modern CSS): ", "Implements CSS custom properties, glassmorphism backdrop-filter, flexbox, CSS grid, and responsive themes."),
        ("JavaScript (ES6+): ", "Executes application logic, debounce timers, line number sync, console proxying, and event listeners."),
        ("Web Storage API: ", "Enables offline code buffer persistence via localStorage across browser sessions."),
        ("PostMessage & Window API: ", "Enables bi-directional cross-origin messaging between parent editor and isolated iframe."),
        ("Web Browser: ", "Google Chrome, Mozilla Firefox, Microsoft Edge, Safari, or Chromium-based modern browsers.")
    ]
    for tag, desc in sw_items:
        draw_bullet(c, LEFT_MARGIN + 15, y)
        c.setFont("Times-Bold", 10.5)
        c.drawString(LEFT_MARGIN + 25, y, tag)
        tag_w = c.stringWidth(tag, "Times-Bold", 10.5)

        lines = simpleSplit(desc, "Times-Roman", 10.5, CONTENT_WIDTH - 25 - tag_w)
        c.setFont("Times-Roman", 10.5)
        c.drawString(LEFT_MARGIN + 25 + tag_w, y, lines[0])
        y -= 14
        for sub_l in lines[1:]:
            c.drawString(LEFT_MARGIN + 25, y, sub_l)
            y -= 14
        y -= 4

    draw_page_number(c, 2)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 4 (Body Page 3): CHAPTER-3 CONCEPTUAL BACKGROUND (PART 1)
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-3")
    y -= 18
    c.drawCentredString(W / 2, y, "Conceptual Background")

    y -= 28
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.1 In-Browser Code Playgrounds")
    y -= 16

    cb_p1 = (
        "In-browser playgrounds provide an interactive, real-time feedback environment for writing and executing "
        "code. Unlike traditional server-side execution systems, a client-side playground synthesizes HTML, CSS, and "
        "JavaScript into an in-memory document tree and delegates execution to the browser's native JavaScript engine (V8, "
        "SpiderMonkey, or JavaScriptCore) and layout rendering engine."
    )
    y = draw_para(c, cb_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    cb_p2 = (
        "This architectural choice yields sub-millisecond execution latency, enables offline execution, and removes "
        "the need for costly backend compute servers. However, client-side execution requires rigorous sandboxing to prevent "
        "arbitrary code execution from corrupting the host application environment."
    )
    y = draw_para(c, cb_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.2 Sandboxing and IFrame Isolation")
    y -= 16

    sb_p1 = (
        "An iframe (Inline Frame) creates an isolated browsing context nested inside the host webpage. In HTML5, the "
        "'sandbox' attribute enforces a strict security perimeter around the nested frame. By default, a sandboxed iframe "
        "restricts script execution, disables form submissions, blocks popups, and prevents access to the parent window's "
        "DOM or localStorage."
    )
    y = draw_para(c, sb_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    sb_p2 = (
        "In CodeEditor Pro, the sandbox is configured with 'allow-scripts allow-modals allow-same-origin', permitting "
        "user-written JavaScript to run while isolating the host editor session. The modern 'srcdoc' attribute is utilized "
        "to directly inject synthesized HTML documents without writing temporary files to disk or generating bloated Data URLs."
    )
    y = draw_para(c, sb_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.3 Event Debouncing and Compilation Lifecycle")
    y -= 16

    db_p1 = (
        "During live typing, input events fire on every single keystroke. Rebuilding the document DOM and re-executing "
        "JavaScript on each keystroke degrades performance and can trigger race conditions. Debouncing is an optimization "
        "technique that delays function execution until a specified duration of inactivity has elapsed."
    )
    y = draw_para(c, db_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    db_p2 = (
        "CodeEditor Pro implements a 350-millisecond debounce window. When the user types, any existing timer is cleared, "
        "and a new timer is started. Only when typing ceases for 350ms does the compilation pipeline trigger, ensuring "
        "butter-smooth responsiveness even on low-powered mobile devices."
    )
    y = draw_para(c, db_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    draw_page_number(c, 3)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 5 (Body Page 4): CHAPTER-3 CONCEPTUAL BACKGROUND (PART 2)
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.4 Virtual Console Proxying via PostMessage")
    y -= 16

    con_p1 = (
        "Inside an isolated iframe, console statements (e.g., console.log, console.error) write directly to the browser's "
        "hidden developer console. Users without access to dev tools cannot inspect program state or debug runtime errors."
    )
    y = draw_para(c, con_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    con_p2 = (
        "To solve this, CodeEditor Pro injects a lightweight console proxy script into the head of every compiled iframe. "
        "This script wraps console.log, console.warn, console.error, console.info, and window.onerror. When invoked, it "
        "serializes arguments into JSON strings and dispatches them across the frame boundary to the parent window using "
        "the HTML5 Window.postMessage() API."
    )
    y = draw_para(c, con_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    con_p3 = (
        "The parent window listens for these dispatched messages, formats them with appropriate severity icons (e.g., "
        "error badges, warnings, info pills), and renders them in an interactive terminal drawer at the bottom of the editor."
    )
    y = draw_para(c, con_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.5 Code Editor Ergonomics & Line Number Synchronization")
    y -= 16

    erg_p1 = (
        "Standard HTML textarea elements lack essential code-editing affordances. Specifically, pressing the Tab key moves "
        "keyboard focus to the next form element instead of inserting indentation spaces. CodeEditor Pro intercepts the "
        "keydown event, prevents default focus cycling, and inserts two space characters at the current selection caret, "
        "preserving cursor continuity."
    )
    y = draw_para(c, erg_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    erg_p2 = (
        "Similarly, dynamic line number gutters are implemented by tracking newline splits in each input buffer. A dedicated "
        "gutter column renders line numbers that remain in perfect vertical synchronization with textarea scroll positions "
        "via passive scroll event listeners."
    )
    y = draw_para(c, erg_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.6 Local Persistence and Project Export")
    y -= 16

    exp_p1 = (
        "Accidental page refreshes can cause loss of uncommitted code in web applications. To guarantee data preservation, "
        "the editor continuously commits active HTML, CSS, and JS strings to browser localStorage during every compilation. "
        "On subsequent page loads, cached buffers are automatically restored."
    )
    y = draw_para(c, exp_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    exp_p2 = (
        "The project also provides a standalone HTML bundle exporter. By packaging HTML markup, inline stylesheet tags, "
        "and script wrappers into an in-memory Blob, users can download complete, production-ready single-file web applications "
        "with a single click."
    )
    y = draw_para(c, exp_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    draw_page_number(c, 4)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 6 (Body Page 5): CHAPTER-3 CONCEPTUAL BACKGROUND (PART 3)
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.7 Responsive Multi-View Architecture")
    y -= 16

    mv_p1 = (
        "Developers work across varying display dimensions, from ultra-wide 4K monitors to compact laptop screens and mobile "
        "devices. A fixed three-column layout becomes unreadable on narrow viewports."
    )
    y = draw_para(c, mv_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    mv_p2 = (
        "To accommodate all form factors, CodeEditor Pro implements a dual-mode layout engine: a 3-Column Split View for "
        "desktop displays, and a Single Tabbed View with active language indicators for mobile and compact viewports. Layout "
        "transitions occur dynamically without interrupting live execution."
    )
    y = draw_para(c, mv_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.8 Template Management System")
    y -= 16

    tm_p1 = (
        "To provide immediate value to novice developers and accelerate prototyping, CodeEditor Pro embeds a curated repository "
        "of production-grade web starter templates directly in client memory:"
    )
    y = draw_para(c, tm_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    tmpl_list = [
        ("Counter App: ", "Demonstrates state management, DOM event listeners, and interactive button bindings."),
        ("3D Hover Card: ", "Demonstrates CSS 3D perspective transforms and real-time mouse coordinate calculations."),
        ("Canvas Particles: ", "Demonstrates high-performance HTML5 2D Canvas rendering, constellation physics, and 60 FPS animation loops."),
        ("Cyberpunk Clock: ", "Demonstrates setInterval timer loops, ISO string formatting, and glowing neon CSS filters."),
        ("Clean Blank Canvas: ", "Provides an unopinionated boilerplate for custom development and scratch experimentation.")
    ]
    for tag, desc in tmpl_list:
        draw_bullet(c, LEFT_MARGIN + 15, y)
        c.setFont("Times-Bold", 10.5)
        c.drawString(LEFT_MARGIN + 25, y, tag)
        tw = c.stringWidth(tag, "Times-Bold", 10.5)
        lines = simpleSplit(desc, "Times-Roman", 10.5, CONTENT_WIDTH - 25 - tw)
        c.setFont("Times-Roman", 10.5)
        c.drawString(LEFT_MARGIN + 25 + tw, y, lines[0])
        y -= 14
        for sub_l in lines[1:]:
            c.drawString(LEFT_MARGIN + 25, y, sub_l)
            y -= 14
        y -= 3

    draw_page_number(c, 5)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 7 (Body Page 6): CHAPTER-4 IMPLEMENTATION (PART 1: CODING)
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter -4")
    y -= 18
    c.drawCentredString(W / 2, y, "Implementation")

    y -= 26
    c.setFont("Times-Roman", 10)
    c.drawString(LEFT_MARGIN, y, "Key architectural extracts from index.js illustrating isolated compilation and console proxying:")
    y -= 18

    code_p1 = [
        "// 1. Debounced Live Compilation & Sandbox Assembly",
        "function compileCode() {",
        '    statusState.className = "status-pill status-compiling";',
        '    statusState.innerHTML = \'<span class="dot"></span> Compiling...\';',
        "",
        "    const html = htmlInput.value;",
        "    const css = cssInput.value;",
        "    const js = jsInput.value;",
        "",
        "    // Interceptor script bridging iframe console to parent drawer",
        "    const consoleScript = `",
        "        <script>",
        "          (function() {",
        "            const _origLog = console.log;",
        "            const _origWarn = console.warn;",
        "            const _origError = console.error;",
        "            const _origInfo = console.info;",
        "",
        "            function serialize(arg) {",
        "              if (arg === null) return 'null';",
        "              if (arg === undefined) return 'undefined';",
        "              if (typeof arg === 'object') {",
        "                try { return JSON.stringify(arg, null, 2); }",
        "                catch(e) { return String(arg); }",
        "              }",
        "              return String(arg);",
        "            }",
        "",
        "            function sendMsg(type, args) {",
        "              const formatted = Array.from(args).map(serialize).join(' ');",
        "              window.parent.postMessage({ type: 'CONSOLE_LOG', level: type, msg: formatted }, '*');",
        "            }",
        "",
        "            console.log = function() { sendMsg('log', arguments); _origLog.apply(console, arguments); };",
        "            console.warn = function() { sendMsg('warn', arguments); _origWarn.apply(console, arguments); };",
        "            console.error = function() { sendMsg('error', arguments); _origError.apply(console, arguments); };",
        "            console.info = function() { sendMsg('info', arguments); _origInfo.apply(console, arguments); };"
    ]
    c.setFont("Courier", 9.2)
    for line in code_p1:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 13.5

    draw_page_number(c, 6)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 8 (Body Page 7): CHAPTER-4 IMPLEMENTATION (PART 2: CODING)
    # -------------------------------------------------------------------------
    y = H - 75
    code_p2 = [
        "            window.onerror = function(message, source, lineno, colno, error) {",
        "              window.parent.postMessage({",
        "                type: 'CONSOLE_LOG',",
        "                level: 'error',",
        "                msg: 'Error: ' + message + (lineno ? ' (Line ' + lineno + ')' : '')",
        "              }, '*');",
        "              return false;",
        "            };",
        "          })();",
        "        </script>",
        "    `;",
        "",
        "    // Build complete isolated document",
        "    const fullDocument = `",
        "      <!DOCTYPE html>",
        '      <html lang="en">',
        "        <head>",
        '          <meta charset="UTF-8">',
        '          <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        "          ${consoleScript}",
        "          <style>${css}</style>",
        "        </head>",
        "        <body>",
        "          ${html}",
        "          <script>",
        "            try {",
        "              ${js}",
        "            } catch (err) {",
        "              console.error(err.message);",
        "            }",
        "          </script>",
        "        </body>",
        "      </html>",
        "    `;",
        "",
        "    // Safely assign to iframe srcdoc and persist buffer",
        "    previewFrame.srcdoc = fullDocument;",
        "    saveToStorage();",
        "}"
    ]
    c.setFont("Courier", 9.2)
    for line in code_p2:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 13.5

    draw_page_number(c, 7)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 9 (Body Page 8): CHAPTER-4 IMPLEMENTATION (PART 3: CODING)
    # -------------------------------------------------------------------------
    y = H - 75
    code_p3 = [
        "// 2. Tab Key Handling & Cursor Position Tracking",
        "function setupEditorEvents(textarea, gutter, lang) {",
        '    textarea.addEventListener("input", () => {',
        "        updateLineNumbers(textarea, gutter);",
        "        scheduleCompile();",
        "    });",
        "",
        '    textarea.addEventListener("scroll", () => {',
        "        syncScroll(textarea, gutter);",
        "    });",
        "",
        '    textarea.addEventListener("keydown", (e) => {',
        '        if (e.key === "Tab") {',
        "            e.preventDefault();",
        "            const start = textarea.selectionStart;",
        "            const end = textarea.selectionEnd;",
        "            const val = textarea.value;",
        "",
        '            textarea.value = val.substring(0, start) + "  " + val.substring(end);',
        "            textarea.selectionStart = textarea.selectionEnd = start + 2;",
        "            updateLineNumbers(textarea, gutter);",
        "            scheduleCompile();",
        "        }",
        "",
        '        if ((e.ctrlKey || e.metaKey) && e.key === "s") {',
        "            e.preventDefault();",
        "            compileCode();",
        "        }",
        "",
        '        if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {',
        "            e.preventDefault();",
        "            compileCode();",
        "        }",
        "    });",
        "}"
    ]
    c.setFont("Courier", 9.2)
    for line in code_p3:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 13.5

    draw_page_number(c, 8)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 10 (Body Page 9): CHAPTER-4 IMPLEMENTATION (PART 4: CODING)
    # -------------------------------------------------------------------------
    y = H - 75
    code_p4 = [
        "// 3. Virtual Console Message Dispatch Receiver",
        'window.addEventListener("message", (event) => {',
        '    if (event.data && event.data.type === "CONSOLE_LOG") {',
        "        const { level, msg } = event.data;",
        '        const msgDiv = document.createElement("div");',
        "        msgDiv.className = `console-log-msg console-${level}`;",
        "",
        '        let icon = "•";',
        '        if (level === "error") {',
        '            icon = "✖";',
        "            errorCount++;",
        '            consoleBadge.style.display = "inline-block";',
        "            consoleBadge.textContent = errorCount;",
        '        } else if (level === "warn") {',
        '            icon = "▲";',
        '        } else if (level === "info") {',
        '            icon = "ℹ";',
        "        }",
        "",
        "        msgDiv.textContent = `${icon} ${msg}`;",
        "        consoleBody.appendChild(msgDiv);",
        "        consoleBody.scrollTop = consoleBody.scrollHeight;",
        "    }",
        "});",
        "",
        "// 4. One-Click Project Exporter",
        'downloadBtn.addEventListener("click", () => {',
        "    const fullHtml = `<!DOCTYPE html>",
        '<html><head><style>${cssInput.value}</style></head>',
        "<body>${htmlInput.value}<script>${jsInput.value}</script></body></html>`;",
        "",
        '    const blob = new Blob([fullHtml], { type: "text/html" });',
        "    const url = URL.createObjectURL(blob);",
        '    const a = document.createElement("a");',
        "    a.href = url;",
        '    a.download = "index.html";',
        "    a.click();",
        "    URL.revokeObjectURL(url);",
        "});"
    ]
    c.setFont("Courier", 9.2)
    for line in code_p4:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 13.5

    draw_page_number(c, 9)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 11 (Body Page 10): 4.2 FLOW CHART
    # -------------------------------------------------------------------------
    if os.path.exists(FLOWCHART_PATH):
        c.drawImage(FLOWCHART_PATH, (W - 390) / 2, 65, width=390, height=710, preserveAspectRatio=True)

    draw_page_number(c, 10)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 12 (Body Page 11): CHAPTER-5 USER INTERFACE & ARCHITECTURE
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-5")
    y -= 18
    c.drawCentredString(W / 2, y, "User Interface & Architecture")

    y -= 26
    c.setFont("Times-Roman", 10.5)
    ui_desc1 = (
        "The CodeEditor Pro user interface features a triple-pane code editor, live sandboxed preview stage, "
        "and integrated developer console drawer with responsive split and tabbed modes."
    )
    y = draw_para(c, ui_desc1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 10
    if os.path.exists(UI_DIAGRAM_PATH):
        c.drawImage(UI_DIAGRAM_PATH, (W - 400) / 2, y - 200, width=400, height=200, preserveAspectRatio=True)
        y -= 215

    c.setFont("Times-Bold", 11)
    c.drawCentredString(W / 2, y, "(Fig 5.1: Multi-Pane User Interface Layout)")
    y -= 24

    ui_desc2 = (
        "The Data Flow Diagram illustrates the event-driven lifecycle: user input triggers debounced compilation, "
        "synthesizes isolated iframe documents, and bridges terminal logs to the virtual console."
    )
    y = draw_para(c, ui_desc2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 10
    if os.path.exists(DFD_PATH):
        c.drawImage(DFD_PATH, (W - 400) / 2, y - 200, width=400, height=200, preserveAspectRatio=True)
        y -= 215

    c.setFont("Times-Bold", 11)
    c.drawCentredString(W / 2, y, "(Fig 5.2: System Architecture & Level-1 Data Flow Diagram)")

    draw_page_number(c, 11)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 13 (Body Page 12): CHAPTER-6 CONCLUSION
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-6")
    y -= 18
    c.drawCentredString(W / 2, y, "Conclusion")

    y -= 28
    conc_p1 = (
        "The CodeEditor Pro project demonstrates the practical application of client-side web technologies, "
        "sandboxed execution architectures, and modern user interface design in building a zero-install in-browser "
        "playground for frontend developers."
    )
    y = draw_para(c, conc_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 10

    conc_p2 = (
        "By replacing destructive DOM-append operations with isolated, debounced iframe.srcdoc synthesis, the application "
        "eliminates memory leaks, script re-execution conflicts, and performance bottlenecks. The addition of a virtual "
        "developer console, synchronized line numbers, tab indentation ergonomics, starter templates, and offline "
        "persistence elevates the project to an industry-grade web development playground."
    )
    y = draw_para(c, conc_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 10

    conc_p3 = (
        "The project successfully validates that modern browsers possess sufficient native computing power to execute "
        "rich developmental workflows entirely on the client, eliminating the necessity for heavy servers or third-party "
        "cloud dependencies."
    )
    y = draw_para(c, conc_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 10

    conc_p4 = (
        "Future enhancements include integration with the Monaco Editor engine for advanced IntelliSense, WebAssembly-based "
        "compilers for TypeScript and Sass, multi-file virtual directory trees, and WebRTC-powered peer-to-peer collaborative "
        "pair-programming sessions."
    )
    y = draw_para(c, conc_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    draw_page_number(c, 12)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 14 (Body Page 13): REFERENCES
    # -------------------------------------------------------------------------
    y = H - 75
    c.setFont("Times-Bold", 15)
    c.drawCentredString(W / 2, y, "References")

    y -= 40
    c.setFont("Times-Roman", 10.5)

    refs = [
        "[1] World Wide Web Consortium (W3C), \"HTML5: A vocabulary and associated APIs for HTML and XHTML,\" W3C Recommendation.",
        "[2] Mozilla Developer Network (MDN), \"The Inline Frame element (iframe) and sandbox security attributes,\" available at: https://developer.mozilla.org/",
        "[3] ECMA International, \"ECMAScript 2024 Language Specification (ECMA-262),\" available at: https://tc39.es/ecma262/",
        "[4] WHATWG, \"HTML Living Standard: Cross-document messaging and Window.postMessage API,\" available at: https://html.spec.whatwg.org/",
        "[5] Google Developers, \"Debounce and Throttle Patterns in Web Applications,\" Google Web Fundamentals.",
        "[6] Microsoft, \"Monaco Editor & VS Code Web Architecture Guidelines,\" available at: https://github.com/microsoft/monaco-editor",
        "[7] Vercel, \"Vercel Edge Platform and Static Deployments Documentation,\" available at: https://vercel.com/docs"
    ]

    for ref in refs:
        lines = simpleSplit(ref, "Times-Roman", 10.5, CONTENT_WIDTH)
        for line in lines:
            c.drawString(LEFT_MARGIN, y, line)
            y -= 16
        y -= 8

    draw_page_number(c, 13)
    c.showPage()

    c.save()
    # Also copy to root
    import shutil
    shutil.copyfile(REPORT_PDF_PATH, REPORT_PDF_ROOT)
    print(f"[OK] CodeEditor Report PDF generated: {REPORT_PDF_PATH} and {REPORT_PDF_ROOT}")


# ==============================================================================
# 2. PRESENTATION PDF GENERATION (Widescreen 16:9, Direct Table of Contents)
# ==============================================================================
def build_presentation_pdf():
    w, h = 960, 540
    c = canvas.Canvas(PRES_PDF_PATH, pagesize=(w, h))

    navy = colors.HexColor('#102C57')
    crimson = colors.HexColor('#2563EB')
    charcoal = colors.HexColor('#202124')
    gray_bg = colors.HexColor('#F8F9FA')
    border_color = colors.HexColor('#DADCE0')

    def draw_clean_header(title_text):
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(50, h - 45, title_text)
        c.setStrokeColor(crimson)
        c.setLineWidth(2.5)
        c.line(50, h - 64, w - 50, h - 64)

    def draw_footer():
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#70757a"))
        c.drawString(50, 18, "CodeEditor Pro: Modern In-Browser Web Development Playground")
        c.drawRightString(w - 50, 18, "Shivam Keshari | Web Architecture Mini-Project")

    # Slide 1: Direct Table of Content (Index)
    draw_clean_header("Table of Content")

    toc_items = [
        "1.  Introduction & Problem Statement",
        "2.  Objectives & Goals",
        "3.  Technology Stack",
        "4.  System Architecture & DFD",
        "5.  Compilation Lifecycle & Flowchart",
        "6.  Key UI Features & Innovations",
        "7.  Engineering Challenges Solved",
        "8.  Future Scope & Conclusion"
    ]

    c.setFillColor(charcoal)
    c.setFont("Helvetica-Bold", 14.5)
    for idx, item in enumerate(toc_items[:4]):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(80, h - 140 - idx * 75, 360, 55, 6, fill=1, stroke=1)
        c.setFillColor(navy)
        c.drawString(100, h - 105 - idx * 75, item)

    for idx, item in enumerate(toc_items[4:]):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(500, h - 140 - idx * 75, 360, 55, 6, fill=1, stroke=1)
        c.setFillColor(navy)
        c.drawString(520, h - 105 - idx * 75, item)

    draw_footer()
    c.showPage()

    # Slide 2: Introduction & Problem Statement
    draw_clean_header("Introduction & Problem Statement")

    intro_bullets = [
        "CodeEditor Pro is a high-performance in-browser web playground for live HTML5, CSS3, and JavaScript authoring.",
        "It eliminates local build configurations and terminal servers, executing entire frontend pipelines in-memory.",
        "Provides instantaneous visual feedback with debounced compiling, sandboxed iframes, and an in-editor terminal.",
        "Features starter design templates, dynamic line-gutter sync, tab key indentation, and local persistence."
    ]

    y = h - 95
    c.setFont("Helvetica", 12)
    c.setFillColor(charcoal)
    for b in intro_bullets:
        c.drawString(55, y, "•  " + b)
        y -= 22

    y -= 10
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(navy)
    c.drawString(55, y, "Problem Statement")
    c.setStrokeColor(crimson)
    c.setLineWidth(1.5)
    c.line(55, y - 4, 195, y - 4)

    y -= 26
    c.setFont("Helvetica", 11.5)
    c.setFillColor(charcoal)
    ps1 = "Traditional in-browser editors suffer from memory leaks caused by appending unbounded <style> and <script> tags to the preview document on every keystroke. This causes variable pollution, stale event listeners, and tab freezes."
    for line in simpleSplit(ps1, "Helvetica", 11.5, w - 110):
        c.drawString(55, y, line)
        y -= 18

    y -= 8
    ps2 = "CodeEditor Pro solves these vulnerabilities through debounced lifecycle management, secure iframe.srcdoc sandboxing, and postMessage terminal interception, creating a robust, crash-resilient developer playground."
    for line in simpleSplit(ps2, "Helvetica", 11.5, w - 110):
        c.drawString(55, y, line)
        y -= 18

    draw_footer()
    c.showPage()

    # Slide 3: Objectives
    draw_clean_header("Project Objectives")

    objs = [
        "To build a zero-dependency, ultra-fast client-side code editor running natively in modern web browsers.",
        "To implement safe iframe.srcdoc sandboxing that prevents security cross-origin leaks while allowing script execution.",
        "To engineer a 350ms debounced compilation lifecycle preventing CPU throttling and memory accumulation.",
        "To integrate a real-time virtual developer console that intercepts console.log, warnings, and unhandled errors.",
        "To optimize developer ergonomics with Tab indentation, line gutters, starter templates, and export capabilities."
    ]

    y = h - 120
    for idx, obj in enumerate(objs):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(55, y - 10, w - 110, 48, 6, fill=1, stroke=1)

        c.setFillColor(navy)
        c.circle(85, y + 14, 14, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(85, y + 10, str(idx + 1))

        c.setFillColor(charcoal)
        c.setFont("Helvetica", 12.5)
        c.drawString(115, y + 10, obj)
        y -= 70

    draw_footer()
    c.showPage()

    # Slide 4: Technology Used
    draw_clean_header("Technology Stack & Architecture")

    tech_table = [
        ("Technology", "Purpose"),
        ("HTML5", "Semantic layout, multi-pane textareas, and sandboxed iframe runtime"),
        ("Modern CSS3", "Dark-mode glassmorphic aesthetics, flexbox, CSS Grid & custom scrollbars"),
        ("Vanilla JavaScript (ES6+)", "Debounced compiler, gutter sync, terminal proxying, and event listeners"),
        ("IFrame Sandbox API", "Security boundary isolating untrusted user scripts (allow-scripts allow-modals)"),
        ("Window.postMessage API", "Bi-directional cross-frame message bridge forwarding console logs to editor"),
        ("Web Storage API", "Automatic local persistence guaranteeing zero data loss on page reloads"),
        ("Blob & URL API", "One-click compilation and standalone single-file index.html project export")
    ]

    y = h - 115
    col1_w = 240
    col2_w = 560
    row_h = 42

    for r_idx, (t, p) in enumerate(tech_table):
        if r_idx == 0:
            c.setFillColor(navy)
            c.rect(80, y, col1_w + col2_w, row_h, fill=1, stroke=0)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 13)
            c.drawString(100, y + 15, t)
            c.drawString(340, y + 15, p)
        else:
            bg = gray_bg if r_idx % 2 == 1 else colors.white
            c.setFillColor(bg)
            c.setStrokeColor(border_color)
            c.rect(80, y, col1_w + col2_w, row_h, fill=1, stroke=1)
            c.setFillColor(navy)
            c.setFont("Helvetica-Bold", 11.5)
            c.drawString(100, y + 15, t)
            c.setFillColor(charcoal)
            c.setFont("Helvetica", 11)
            c.drawString(340, y + 15, p)
        y -= row_h

    draw_footer()
    c.showPage()

    # Slide 5: Data Flow Diagram (DFD Level-1)
    draw_clean_header("Data Flow Diagram (DFD Level-1)")

    if os.path.exists(DFD_PATH):
        c.drawImage(DFD_PATH, 50, 45, width=860, height=415, preserveAspectRatio=True)

    draw_footer()
    c.showPage()

    # Slide 6: Flowchart of Compilation Lifecycle
    draw_clean_header("Compilation & Execution Lifecycle Flowchart")

    if os.path.exists(FLOWCHART_PATH):
        c.drawImage(FLOWCHART_PATH, (w - 320) / 2, 40, width=320, height=430, preserveAspectRatio=True)

    draw_footer()
    c.showPage()

    # Slide 7: UI Features & Dashboard
    draw_clean_header("User Interface Architecture & Features")

    if os.path.exists(UI_DIAGRAM_PATH):
        c.drawImage(UI_DIAGRAM_PATH, (w - 740) / 2, 60, width=740, height=400, preserveAspectRatio=True)

    draw_footer()
    c.showPage()

    # Slide 8: Key Engineering Solutions
    draw_clean_header("Key Engineering Challenges Solved")

    challenges = [
        ("Memory Leak Prevention:", "Replaced infinite appendChild(style/script) with complete isolated iframe.srcdoc overwrite."),
        ("Keystroke Throttling:", "Engineered 350ms debounce timer to prevent CPU spikes and redundant re-renders."),
        ("Console Output Bridging:", "Hooked console.log/error/warn and window.onerror via JSON serialization and postMessage."),
        ("Editor Indentation:", "Intercepted Tab key to prevent focus cycling and insert 2 spaces at caret."),
        ("Zero Data Loss:", "Continuous synchronization of HTML/CSS/JS buffers to browser localStorage.")
    ]

    y = h - 120
    for idx, (title, desc) in enumerate(challenges):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(55, y - 10, w - 110, 48, 6, fill=1, stroke=1)

        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(75, y + 12, title)

        c.setFillColor(charcoal)
        c.setFont("Helvetica", 11.5)
        c.drawString(255, y + 12, desc)
        y -= 70

    draw_footer()
    c.showPage()

    # Slide 9: Future Scope & Roadmap
    draw_clean_header("Future Scope & Enhancements")

    scopes = [
        "Integrate Microsoft Monaco Editor engine for full VS Code IntelliSense and syntax highlighting.",
        "Incorporate WebAssembly compilers for real-time TypeScript, Sass, and Less compilation in-browser.",
        "Add multi-tab virtual file explorer supporting multi-component modern frameworks (React / Vue).",
        "Implement WebRTC-powered peer-to-peer live collaborative pair programming and code sharing.",
        "Integrate direct GitHub Gist and repository export via GitHub REST API OAuth."
    ]

    y = h - 120
    for idx, sc in enumerate(scopes):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(55, y - 10, w - 110, 48, 6, fill=1, stroke=1)

        c.setFillColor(navy)
        c.circle(85, y + 14, 14, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(85, y + 10, str(idx + 1))

        c.setFillColor(charcoal)
        c.setFont("Helvetica", 12.5)
        c.drawString(115, y + 10, sc)
        y -= 70

    draw_footer()
    c.showPage()

    # Slide 10: Conclusion & References
    draw_clean_header("Conclusion & Summary")

    conclusions = [
        "CodeEditor Pro demonstrates the power of modern client-side web APIs in delivering a fast, zero-install IDE.",
        "Debounced compilation and iframe isolation ensure crash-resilient, secure execution of arbitrary code.",
        "Ergonomic improvements including virtual console proxying and local auto-save provide a desktop-grade feel.",
        "The project stands as a fully functioning, production-ready frontend playground deployable anywhere."
    ]

    y = h - 120
    for idx, c_text in enumerate(conclusions):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(55, y - 10, w - 110, 48, 6, fill=1, stroke=1)

        c.setFillColor(navy)
        c.circle(85, y + 14, 14, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(85, y + 10, str(idx + 1))

        c.setFillColor(charcoal)
        c.setFont("Helvetica", 12.5)
        c.drawString(115, y + 10, c_text)
        y -= 70

    draw_footer()
    c.showPage()

    # Slide 11: Thank You
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(w / 2, h / 2 + 30, "Thank You")

    c.setStrokeColor(crimson)
    c.setLineWidth(3)
    c.line(w / 2 - 120, h / 2 + 10, w / 2 + 120, h / 2 + 10)

    c.setFillColor(charcoal)
    c.setFont("Helvetica", 18)
    c.drawCentredString(w / 2, h / 2 - 30, "Questions & Discussion")

    draw_footer()
    c.showPage()

    c.save()
    import shutil
    shutil.copyfile(PRES_PDF_PATH, PRES_PDF_ROOT)
    print(f"[OK] CodeEditor Presentation PDF generated: {PRES_PDF_PATH} and {PRES_PDF_ROOT}")


# ==============================================================================
# 3. PRESENTATION PPTX GENERATION (CodeEditor Pro)
# ==============================================================================
def build_presentation_pptx():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    navy_rgb = RGBColor(16, 44, 87)
    blue_rgb = RGBColor(37, 99, 235)
    charcoal_rgb = RGBColor(32, 33, 36)

    def add_slide_header(slide, title_text):
        tx = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.8))
        tf = tx.text_frame
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = navy_rgb

    # Slide 1: Direct Table of Content
    s1 = prs.slides.add_slide(blank_layout)
    add_slide_header(s1, "Table of Content")
    tx1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(5.0))
    tf1 = tx1.text_frame
    tocs = [
        "1.  Introduction & Problem Statement",
        "2.  Objectives & Goals",
        "3.  Technology Stack & Architecture",
        "4.  Data Flow Diagram (DFD Level-1)",
        "5.  Compilation Lifecycle & Flowchart",
        "6.  Key UI Features & Innovations",
        "7.  Engineering Challenges Solved",
        "8.  Future Scope & Conclusion"
    ]
    for idx, t in enumerate(tocs):
        p = tf1.paragraphs[0] if idx == 0 else tf1.add_paragraph()
        p.text = t
        p.font.size = Pt(17)
        p.space_after = Pt(14)
        p.font.color.rgb = navy_rgb

    # Slide 2: Introduction
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "Introduction & Problem Statement")
    tx2 = s2.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(5.2))
    tf2 = tx2.text_frame
    tf2.word_wrap = True
    intros = [
        "•  CodeEditor Pro is a high-performance in-browser web playground for live HTML5, CSS3, and JavaScript authoring.",
        "•  It eliminates local build configurations and terminal servers, executing entire frontend pipelines in-memory.",
        "•  Provides instantaneous visual feedback with debounced compiling, sandboxed iframes, and an in-editor terminal.",
        "•  Features starter design templates, dynamic line-gutter sync, tab key indentation, and local persistence.",
        "",
        "Problem Statement:",
        "Traditional in-browser editors suffer from memory leaks caused by appending unbounded <style> and <script> tags to the preview document on every keystroke. CodeEditor Pro solves these vulnerabilities through debounced lifecycle management, secure iframe.srcdoc sandboxing, and postMessage terminal interception."
    ]
    for idx, t in enumerate(intros):
        p = tf2.paragraphs[0] if idx == 0 else tf2.add_paragraph()
        p.text = t
        p.font.size = Pt(14) if "•" in t or "Problem" in t else Pt(13)
        if "Problem" in t:
            p.font.bold = True
            p.font.color.rgb = blue_rgb
        p.space_after = Pt(6)

    # Slide 3: Objectives
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "Project Objectives")
    tx3 = s3.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(5.2))
    tf3 = tx3.text_frame
    objs = [
        "1.  To build a zero-dependency, ultra-fast client-side code editor running natively in modern web browsers.",
        "2.  To implement safe iframe.srcdoc sandboxing that prevents security cross-origin leaks while allowing script execution.",
        "3.  To engineer a 350ms debounced compilation lifecycle preventing CPU throttling and memory accumulation.",
        "4.  To integrate a real-time virtual developer console that intercepts console.log, warnings, and unhandled errors.",
        "5.  To optimize developer ergonomics with Tab indentation, line gutters, starter templates, and export capabilities."
    ]
    for idx, o in enumerate(objs):
        p = tf3.paragraphs[0] if idx == 0 else tf3.add_paragraph()
        p.text = o
        p.font.size = Pt(15)
        p.space_after = Pt(18)

    # Slide 4: DFD
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "Data Flow Diagram (DFD Level-1)")
    if os.path.exists(DFD_PATH):
        s4.shapes.add_picture(DFD_PATH, Inches(1.2), Inches(1.5), Inches(10.9), Inches(5.4))

    # Slide 5: Flowchart
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "Compilation & Execution Lifecycle Flowchart")
    if os.path.exists(FLOWCHART_PATH):
        s5.shapes.add_picture(FLOWCHART_PATH, Inches(4.5), Inches(1.3), Inches(4.3), Inches(5.8))

    # Slide 6: UI Overview
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "User Interface & Dashboard Architecture")
    if os.path.exists(UI_DIAGRAM_PATH):
        s6.shapes.add_picture(UI_DIAGRAM_PATH, Inches(1.6), Inches(1.4), Inches(10.1), Inches(5.5))

    # Slide 7: Thank You
    s7 = prs.slides.add_slide(blank_layout)
    tx7 = s7.shapes.add_textbox(Inches(2.0), Inches(2.8), Inches(9.3), Inches(2.5))
    tf7 = tx7.text_frame
    p_ty = tf7.paragraphs[0]
    p_ty.text = "Thank You"
    p_ty.font.size = Pt(40)
    p_ty.font.bold = True
    p_ty.font.color.rgb = navy_rgb
    p_ty.alignment = PP_ALIGN.CENTER

    p_sub = tf7.add_paragraph()
    p_sub.text = "CodeEditor Pro — Questions & Discussion"
    p_sub.font.size = Pt(18)
    p_sub.font.color.rgb = blue_rgb
    p_sub.alignment = PP_ALIGN.CENTER

    prs.save(PRES_PPTX_PATH)
    print(f"[OK] CodeEditor Presentation PPTX generated: {PRES_PPTX_PATH}")


def main():
    print("=" * 70)
    print("GENERATING CODEEDITOR DELIVERABLES (DIRECT INDEX, NO COLLEGE NAME)")
    print("=" * 70)
    build_report_pdf()
    build_presentation_pdf()
    build_presentation_pptx()
    print("=" * 70)
    print("ALL CODEEDITOR DELIVERABLES SUCCESSFULLY GENERATED!")
    print("=" * 70)


if __name__ == "__main__":
    main()
