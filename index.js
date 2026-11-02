/**
 * CodeEditor Pro - Core Architecture & Live Runner (v2.1.0)
 * Modern client-side playground with debounced compilation, isolated
 * sandboxing, virtual console interception, layout modes, and persistence.
 */

// DOM Elements
const htmlInput = document.getElementById("html");
const cssInput = document.getElementById("css");
const jsInput = document.getElementById("js");
const previewFrame = document.getElementById("previewFrame");

const htmlLines = document.getElementById("htmlLines");
const cssLines = document.getElementById("cssLines");
const jsLines = document.getElementById("jsLines");

const runBtn = document.getElementById("runBtn");
const formatBtn = document.getElementById("formatBtn");
const clearBtn = document.getElementById("clearBtn");
const downloadBtn = document.getElementById("downloadBtn");
const autoRunToggle = document.getElementById("autoRunToggle");
const templateSelect = document.getElementById("templateSelect");

const layoutSideBtn = document.getElementById("layoutSideBtn");
const layoutStackBtn = document.getElementById("layoutStackBtn");
const layoutTabsBtn = document.getElementById("layoutTabsBtn");
const editorTabsBar = document.getElementById("editorTabsBar");
const editorsContainer = document.getElementById("editorsContainer");

const toggleConsoleBtn = document.getElementById("toggleConsoleBtn");
const closeConsoleBtn = document.getElementById("closeConsoleBtn");
const clearConsoleBtn = document.getElementById("clearConsoleBtn");
const consoleDrawer = document.getElementById("consoleDrawer");
const consoleBody = document.getElementById("consoleBody");
const consoleBadge = document.getElementById("consoleBadge");
const errorIndicator = document.getElementById("errorIndicator");
const errorCountText = document.getElementById("errorCountText");

const refreshPreviewBtn = document.getElementById("refreshPreviewBtn");
const fullscreenPreviewBtn = document.getElementById("fullscreenPreviewBtn");
const exitFullscreenBtn = document.getElementById("exitFullscreenBtn");

const statusState = document.getElementById("statusState");
const cursorPosition = document.getElementById("cursorPosition");
const statsCount = document.getElementById("statsCount");
const saveIndicator = document.getElementById("saveIndicator");

// State
let compileTimer = null;
let errorCount = 0;
let isTabbedMode = false;
let activeTab = "html";

// ==========================================================================
// 1. Starter Templates
// ==========================================================================
const TEMPLATES = {
  counter: {
    html: `<div class="card">
  <div class="badge">INTERACTIVE APP</div>
  <h1 id="count">0</h1>
  <div class="btn-group">
    <button id="decrement" class="btn btn-danger">-</button>
    <button id="reset" class="btn btn-secondary">Reset</button>
    <button id="increment" class="btn btn-success">+</button>
  </div>
  <p class="hint">Click buttons or use Arrow Up / Down keys</p>
</div>`,
    css: `body {
  margin: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: system-ui, -apple-system, sans-serif;
  background: radial-gradient(circle at top, #1e293b, #0f172a);
  color: #f8fafc;
}

.card {
  background: rgba(30, 41, 59, 0.7);
  backdrop-filter: blur(12px);
  padding: 32px 48px;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}

.badge {
  display: inline-block;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  padding: 4px 12px;
  background: rgba(56, 189, 248, 0.2);
  color: #38bdf8;
  border-radius: 20px;
  font-weight: 700;
  margin-bottom: 12px;
}

h1 {
  font-size: 4.5rem;
  margin: 10px 0 24px;
  font-weight: 800;
  color: #38bdf8;
  transition: transform 0.15s ease;
}

.btn-group {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.btn {
  padding: 10px 24px;
  font-size: 1.1rem;
  font-weight: 600;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn:active {
  transform: scale(0.95);
}

.btn-success { background: #10b981; color: white; }
.btn-danger { background: #ef4444; color: white; }
.btn-secondary { background: #475569; color: white; }

.btn:hover {
  filter: brightness(1.15);
  box-shadow: 0 6px 16px rgba(0,0,0,0.3);
}

.hint {
  font-size: 0.8rem;
  color: #94a3b8;
  margin-top: 20px;
}`,
    js: `const countEl = document.getElementById('count');
const incBtn = document.getElementById('increment');
const decBtn = document.getElementById('decrement');
const resBtn = document.getElementById('reset');

let count = 0;

function updateUI() {
  countEl.textContent = count;
  countEl.style.transform = 'scale(1.15)';
  setTimeout(() => countEl.style.transform = 'scale(1)', 150);
  console.log('Counter updated:', count);
}

incBtn.addEventListener('click', () => { count++; updateUI(); });
decBtn.addEventListener('click', () => { count--; updateUI(); });
resBtn.addEventListener('click', () => { count = 0; updateUI(); });

window.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowUp') { count++; updateUI(); }
  if (e.key === 'ArrowDown') { count--; updateUI(); }
});

console.log('⚡ Counter App ready! Try clicking + / -');`
  },

  card: {
    html: `<div class="card-container">
  <div class="glass-card" id="card">
    <div class="logo">✦</div>
    <h2>Modern UI Card</h2>
    <p>Move your cursor around this card to experience real-time 3D tilt and illumination physics.</p>
    <div class="tags">
      <span>HTML5</span>
      <span>CSS3 3D</span>
      <span>JavaScript</span>
    </div>
  </div>
</div>`,
    css: `body {
  margin: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #090d16;
  font-family: 'Plus Jakarta Sans', sans-serif;
  perspective: 1000px;
}

.card-container {
  padding: 40px;
}

.glass-card {
  width: 320px;
  padding: 36px 30px;
  background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.01));
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 24px;
  box-shadow: 0 30px 60px rgba(0,0,0,0.6);
  transform-style: preserve-3d;
  transition: transform 0.1s ease-out;
  cursor: pointer;
}

.logo {
  font-size: 2rem;
  color: #38bdf8;
  margin-bottom: 12px;
}

h2 {
  color: #fff;
  font-size: 1.4rem;
  margin: 0 0 12px;
}

p {
  color: #94a3b8;
  font-size: 0.9rem;
  line-height: 1.6;
}

.tags {
  display: flex;
  gap: 8px;
  margin-top: 24px;
}

.tags span {
  font-size: 0.75rem;
  padding: 4px 10px;
  border-radius: 8px;
  background: rgba(56, 189, 248, 0.12);
  color: #38bdf8;
  font-weight: 600;
}`,
    js: `const card = document.getElementById('card');

window.addEventListener('mousemove', (e) => {
  const rect = card.getBoundingClientRect();
  const cardX = rect.left + rect.width / 2;
  const cardY = rect.top + rect.height / 2;
  
  const mouseX = e.clientX - cardX;
  const mouseY = e.clientY - cardY;
  
  const rotateY = (mouseX / (window.innerWidth / 2)) * 25;
  const rotateX = -(mouseY / (window.innerHeight / 2)) * 25;
  
  card.style.transform = 'rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg)';
});

window.addEventListener('mouseleave', () => {
  card.style.transform = 'rotateX(0deg) rotateY(0deg)';
});

console.log('✨ 3D Card physics loaded');`
  },

  particles: {
    html: `<canvas id="canvas"></canvas>
<div class="overlay">
  <h1>Interactive Particles</h1>
  <p>Move mouse to connect constellations</p>
</div>`,
    css: `body {
  margin: 0;
  overflow: hidden;
  background: #050508;
  font-family: sans-serif;
}

#canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: white;
  pointer-events: none;
}

h1 {
  font-size: 2.2rem;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
}

p {
  color: #64748b;
  font-size: 0.95rem;
}`,
    js: `const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let w = canvas.width = window.innerWidth;
let h = canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
  w = canvas.width = window.innerWidth;
  h = canvas.height = window.innerHeight;
});

const particles = [];
const count = 65;

for (let i = 0; i < count; i++) {
  particles.push({
    x: Math.random() * w,
    y: Math.random() * h,
    vx: (Math.random() - 0.5) * 1.5,
    vy: (Math.random() - 0.5) * 1.5,
    radius: Math.random() * 2.5 + 1
  });
}

function animate() {
  ctx.clearRect(0, 0, w, h);
  ctx.fillStyle = '#38bdf8';
  ctx.strokeStyle = 'rgba(56, 189, 248, 0.15)';

  for (let i = 0; i < count; i++) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;

    if (p.x < 0 || p.x > w) p.vx *= -1;
    if (p.y < 0 || p.y > h) p.vy *= -1;

    ctx.beginPath();
    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
    ctx.fill();

    for (let j = i + 1; j < count; j++) {
      const p2 = particles[j];
      const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
      if (dist < 110) {
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(animate);
}

animate();
console.log('🌌 Particles running smoothly at 60 FPS');`
  },

  clock: {
    html: `<div class="clock-wrap">
  <div class="neon-time" id="time">00:00:00</div>
  <div class="date" id="date">Loading...</div>
  <div class="mode">CYBERPUNK UTC DIGITAL CLOCK</div>
</div>`,
    css: `body {
  margin: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #06090e;
  font-family: 'Courier New', monospace;
}

.clock-wrap {
  text-align: center;
  padding: 40px 60px;
  background: #0b111a;
  border: 2px solid #00f0ff;
  border-radius: 16px;
  box-shadow: 0 0 30px rgba(0, 240, 255, 0.25), inset 0 0 20px rgba(0, 240, 255, 0.1);
}

.neon-time {
  font-size: 3.8rem;
  font-weight: 800;
  color: #00f0ff;
  text-shadow: 0 0 10px #00f0ff, 0 0 20px #00f0ff;
  letter-spacing: 0.05em;
}

.date {
  font-size: 1.1rem;
  color: #ff007f;
  margin: 12px 0;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.mode {
  font-size: 0.75rem;
  color: #718096;
  letter-spacing: 0.15em;
}`,
    js: `function updateClock() {
  const now = new Date();
  const timeStr = now.toTimeString().split(' ')[0];
  const dateStr = now.toLocaleDateString('en-US', {
    weekday: 'short', month: 'short', day: 'numeric', year: 'numeric'
  });

  document.getElementById('time').textContent = timeStr;
  document.getElementById('date').textContent = dateStr;
}

setInterval(updateClock, 1000);
updateClock();
console.log('⏱️ Cyberpunk clock initialized');`
  },

  blank: {
    html: `<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: sans-serif; padding: 2rem; }
  </style>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>Start editing HTML, CSS, and JS to build something amazing.</p>
</body>
</html>`,
    css: `/* Add your CSS styles */\nbody {\n  background: #f8fafc;\n  color: #1e293b;\n}`,
    js: `// Add your JavaScript logic\nconsole.log('⚡ Ready to code!');`
  }
};

// ==========================================================================
// 2. High-Performance Compiler & Live Renderer
// ==========================================================================
function compileCode() {
  statusState.className = "status-pill status-compiling";
  statusState.innerHTML = '<span class="dot"></span> Compiling...';

  // Reset errors on compile
  errorCount = 0;
  consoleBadge.style.display = "none";
  errorIndicator.style.display = "none";

  const html = htmlInput.value;
  const css = cssInput.value;
  const js = jsInput.value;

  // Interceptor script to bridge iframe console & errors to parent drawer
  const consoleScript = `
    <script>
      (function() {
        const _origLog = console.log;
        const _origWarn = console.warn;
        const _origError = console.error;
        const _origInfo = console.info;

        function serialize(arg) {
          if (arg === null) return 'null';
          if (arg === undefined) return 'undefined';
          if (typeof arg === 'object') {
            try { return JSON.stringify(arg, null, 2); }
            catch(e) { return String(arg); }
          }
          return String(arg);
        }

        function sendMsg(type, args) {
          try {
            const formatted = Array.from(args).map(serialize).join(' ');
            if (window.parent && window.parent !== window) {
              window.parent.postMessage({ type: 'CONSOLE_LOG', level: type, msg: formatted }, '*');
            }
          } catch(e) {}
        }

        console.log = function() { sendMsg('log', arguments); _origLog.apply(console, arguments); };
        console.warn = function() { sendMsg('warn', arguments); _origWarn.apply(console, arguments); };
        console.error = function() { sendMsg('error', arguments); _origError.apply(console, arguments); };
        console.info = function() { sendMsg('info', arguments); _origInfo.apply(console, arguments); };

        window.onerror = function(message, source, lineno, colno, error) {
          try {
            if (window.parent && window.parent !== window) {
              window.parent.postMessage({
                type: 'CONSOLE_LOG',
                level: 'error',
                msg: 'Error: ' + message + (lineno ? ' (Line ' + lineno + ')' : '')
              }, '*');
            }
          } catch(e) {}
          return false;
        };
      })();
    <\/script>
  `;

  // Build complete isolated document
  const fullDocument = `
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        ${consoleScript}
        <style>
          ${css}
        </style>
      </head>
      <body>
        ${html}
        <script>
          window.addEventListener('DOMContentLoaded', function() {
            try {
              ${js}
            } catch (err) {
              console.error(err.stack || err.message);
            }
          });
          // Also execute immediately for inline scripts
          try {
            ${js}
          } catch (err) {
            // Handled in DOMContentLoaded
          }
        <\/script>
      </body>
    </html>
  `;

  // Assign to iframe srcdoc
  previewFrame.srcdoc = fullDocument;

  // Save to storage
  saveToStorage();

  setTimeout(() => {
    statusState.className = "status-pill status-ready";
    statusState.innerHTML = '<span class="dot"></span> Ready';
  }, 250);
}

function scheduleCompile() {
  if (autoRunToggle.checked) {
    clearTimeout(compileTimer);
    compileTimer = setTimeout(compileCode, 350);
  }
}

// ==========================================================================
// 3. Line Numbering & Gutter Sync
// ==========================================================================
function updateLineNumbers(textarea, gutter) {
  const lines = textarea.value.split("\n").length;
  let numbers = "";
  for (let i = 1; i <= lines; i++) {
    numbers += i + "<br>";
  }
  gutter.innerHTML = numbers;
}

function syncScroll(textarea, gutter) {
  gutter.scrollTop = textarea.scrollTop;
}

function updateAllLines() {
  updateLineNumbers(htmlInput, htmlLines);
  updateLineNumbers(cssInput, cssLines);
  updateLineNumbers(jsInput, jsLines);

  const totalLines =
    htmlInput.value.split("\n").length +
    cssInput.value.split("\n").length +
    jsInput.value.split("\n").length;

  statsCount.textContent = `${totalLines} lines total`;
}

// ==========================================================================
// 4. Tab Key Handling & Cursor Position Tracking
// ==========================================================================
function setupEditorEvents(textarea, gutter, lang) {
  textarea.addEventListener("input", () => {
    updateLineNumbers(textarea, gutter);
    scheduleCompile();
  });

  textarea.addEventListener("scroll", () => {
    syncScroll(textarea, gutter);
  });

  function updateCursor() {
    const text = textarea.value.substr(0, textarea.selectionStart);
    const line = text.split("\n").length;
    const col = text.split("\n").pop().length + 1;
    cursorPosition.textContent = `${lang.toUpperCase()} - Ln ${line}, Col ${col}`;
  }

  textarea.addEventListener("keyup", updateCursor);
  textarea.addEventListener("click", updateCursor);

  textarea.addEventListener("keydown", (e) => {
    if (e.key === "Tab") {
      e.preventDefault();
      const start = textarea.selectionStart;
      const end = textarea.selectionEnd;
      const val = textarea.value;

      textarea.value = val.substring(0, start) + "  " + val.substring(end);
      textarea.selectionStart = textarea.selectionEnd = start + 2;
      updateLineNumbers(textarea, gutter);
      scheduleCompile();
    }

    // Ctrl + S / Cmd + S
    if ((e.ctrlKey || e.metaKey) && e.key === "s") {
      e.preventDefault();
      compileCode();
    }

    // Ctrl + Enter
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      compileCode();
    }
  });
}

// ==========================================================================
// 5. Virtual Console Interception
// ==========================================================================
window.addEventListener("message", (event) => {
  if (event.data && event.data.type === "CONSOLE_LOG") {
    const { level, msg } = event.data;
    const msgDiv = document.createElement("div");
    msgDiv.className = `console-log-msg console-${level}`;

    let icon = "•";
    if (level === "error") {
      icon = "✖";
      errorCount++;
      consoleBadge.style.display = "inline-block";
      consoleBadge.textContent = errorCount;
      errorIndicator.style.display = "inline-flex";
      errorCountText.textContent = `${errorCount} ${errorCount === 1 ? 'Error' : 'Errors'}`;
    } else if (level === "warn") {
      icon = "▲";
    } else if (level === "info") {
      icon = "ℹ";
    }

    msgDiv.textContent = `${icon} ${msg}`;
    consoleBody.appendChild(msgDiv);
    consoleBody.scrollTop = consoleBody.scrollHeight;
  }
});

toggleConsoleBtn.addEventListener("click", () => {
  consoleDrawer.classList.toggle("open");
});

errorIndicator.addEventListener("click", () => {
  consoleDrawer.classList.add("open");
});

closeConsoleBtn.addEventListener("click", () => {
  consoleDrawer.classList.remove("open");
});

clearConsoleBtn.addEventListener("click", () => {
  consoleBody.innerHTML = '<div class="console-log-msg console-system">⚡ Console cleared.</div>';
  errorCount = 0;
  consoleBadge.style.display = "none";
  errorIndicator.style.display = "none";
});

// ==========================================================================
// 6. Format Code (Robust Indenter)
// ==========================================================================
function formatCode() {
  function formatHTML(text) {
    const lines = text.split("\n");
    let indent = 0;
    return lines.map(raw => {
      let l = raw.trim();
      if (!l) return "";
      if (l.startsWith("</")) {
        indent = Math.max(0, indent - 1);
      }
      const res = "  ".repeat(indent) + l;
      if (l.startsWith("<") && !l.startsWith("</") && !l.endsWith("/>") && !l.includes("</")) {
        indent++;
      }
      return res;
    }).join("\n");
  }

  function formatCSS(text) {
    const lines = text.split("\n");
    let indent = 0;
    return lines.map(raw => {
      let l = raw.trim();
      if (!l) return "";
      if (l.startsWith("}")) {
        indent = Math.max(0, indent - 1);
      }
      const res = "  ".repeat(indent) + l;
      if (l.endsWith("{")) {
        indent++;
      }
      return res;
    }).join("\n");
  }

  function formatJS(text) {
    const lines = text.split("\n");
    let indent = 0;
    return lines.map(raw => {
      let l = raw.trim();
      if (!l) return "";
      if (l.startsWith("}") || l.startsWith("]")) {
        indent = Math.max(0, indent - 1);
      }
      const res = "  ".repeat(indent) + l;
      if (l.endsWith("{") || l.endsWith("[")) {
        indent++;
      }
      return res;
    }).join("\n");
  }

  htmlInput.value = formatHTML(htmlInput.value);
  cssInput.value = formatCSS(cssInput.value);
  jsInput.value = formatJS(jsInput.value);

  updateAllLines();
  compileCode();
}

formatBtn.addEventListener("click", formatCode);

// ==========================================================================
// 7. Templates & Local Storage Persistence
// ==========================================================================
function loadTemplate(key) {
  const template = TEMPLATES[key] || TEMPLATES.counter;
  htmlInput.value = template.html;
  cssInput.value = template.css;
  jsInput.value = template.js;

  // Reset dropdown placeholder
  templateSelect.value = "";

  updateAllLines();
  compileCode();
}

templateSelect.addEventListener("change", (e) => {
  if (e.target.value) {
    loadTemplate(e.target.value);
  }
});

function saveToStorage() {
  try {
    localStorage.setItem("code_editor_html", htmlInput.value);
    localStorage.setItem("code_editor_css", cssInput.value);
    localStorage.setItem("code_editor_js", jsInput.value);
    saveIndicator.textContent = "Saved locally";
  } catch (e) {
    saveIndicator.textContent = "Auto-save off";
  }
}

function restoreFromStorage() {
  const savedHtml = localStorage.getItem("code_editor_html");
  const savedCss = localStorage.getItem("code_editor_css");
  const savedJs = localStorage.getItem("code_editor_js");

  // If saved buffer is non-empty, restore it; otherwise load starter template
  const hasContent = (savedHtml && savedHtml.trim().length > 0) ||
                     (savedCss && savedCss.trim().length > 0) ||
                     (savedJs && savedJs.trim().length > 0);

  if (hasContent) {
    htmlInput.value = savedHtml || "";
    cssInput.value = savedCss || "";
    jsInput.value = savedJs || "";
  } else {
    loadTemplate("counter");
  }

  updateAllLines();
  compileCode();
}

// ==========================================================================
// 8. Toolbar Actions: Run, Copy, Export, Clear, Fullscreen
// ==========================================================================
runBtn.addEventListener("click", () => {
  compileCode();
});

refreshPreviewBtn.addEventListener("click", () => {
  compileCode();
});

fullscreenPreviewBtn.addEventListener("click", () => {
  document.body.classList.toggle("preview-fullscreen");
});

exitFullscreenBtn.addEventListener("click", () => {
  document.body.classList.remove("preview-fullscreen");
});

document.querySelectorAll(".copy-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const editor = btn.dataset.editor;
    const input = document.getElementById(editor);
    navigator.clipboard.writeText(input.value).then(() => {
      const orig = btn.textContent;
      btn.textContent = "Copied!";
      btn.style.color = "var(--accent-green)";
      setTimeout(() => {
        btn.textContent = orig;
        btn.style.color = "";
      }, 1500);
    });
  });
});

downloadBtn.addEventListener("click", () => {
  const fullHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exported Project</title>
  <style>
${cssInput.value}
  </style>
</head>
<body>
${htmlInput.value}
  <script>
${jsInput.value}
  <\/script>
</body>
</html>`;

  const blob = new Blob([fullHtml], { type: "text/html" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "index.html";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});

clearBtn.addEventListener("click", () => {
  if (confirm("Reset all editors to a blank canvas?")) {
    loadTemplate("blank");
  }
});

// Layout Switchers
function setLayoutMode(mode) {
  layoutSideBtn.classList.toggle("active", mode === "side");
  layoutStackBtn.classList.toggle("active", mode === "stack");
  layoutTabsBtn.classList.toggle("active", mode === "tabs");

  if (mode === "side") {
    document.body.classList.add("layout-side");
    document.body.classList.remove("layout-stack");
    editorTabsBar.style.display = "none";
    editorsContainer.classList.remove("tabbed-mode");
    document.querySelectorAll(".pane").forEach((p) => (p.style.display = "flex"));
  } else if (mode === "stack") {
    document.body.classList.add("layout-stack");
    document.body.classList.remove("layout-side");
    editorTabsBar.style.display = "none";
    editorsContainer.classList.remove("tabbed-mode");
    document.querySelectorAll(".pane").forEach((p) => (p.style.display = "flex"));
  } else if (mode === "tabs") {
    editorTabsBar.style.display = "flex";
    editorsContainer.classList.add("tabbed-mode");
    switchTab(activeTab);
  }
}

layoutSideBtn.addEventListener("click", () => setLayoutMode("side"));
layoutStackBtn.addEventListener("click", () => setLayoutMode("stack"));
layoutTabsBtn.addEventListener("click", () => setLayoutMode("tabs"));

function switchTab(tab) {
  activeTab = tab;
  document.querySelectorAll(".editor-tab").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.target === tab);
  });
  document.querySelectorAll(".pane").forEach((pane) => {
    pane.style.display = pane.dataset.pane === tab ? "flex" : "none";
  });
}

document.querySelectorAll(".editor-tab").forEach((tabBtn) => {
  tabBtn.addEventListener("click", () => {
    switchTab(tabBtn.dataset.target);
  });
});

// Keyboard Shortcuts
window.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    e.preventDefault();
    compileCode();
  }
  if (e.key === "Escape" && document.body.classList.contains("preview-fullscreen")) {
    document.body.classList.remove("preview-fullscreen");
  }
});

// ==========================================================================
// 9. Initialize
// ==========================================================================
setupEditorEvents(htmlInput, htmlLines, "html");
setupEditorEvents(cssInput, cssLines, "css");
setupEditorEvents(jsInput, jsLines, "js");

restoreFromStorage();
