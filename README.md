# ⚡ CodeEditor Pro

> A blazing fast, modern, and developer-friendly in-browser playground for HTML, CSS, and JavaScript with debounced live reload, integrated virtual console, and local persistence.

🌐 **Live Demo (Production)**: [https://codeeditor-shivam990.vercel.app/](https://codeeditor-shivam990.vercel.app/)  
🚀 **GitHub Pages Demo**: [https://s1h2i3v4a.github.io/CodeEditor/](https://s1h2i3v4a.github.io/CodeEditor/)  
🔗 **Vercel Preview**: [https://codeeditor-7b92ehw0x-shivam990.vercel.app/](https://codeeditor-7b92ehw0x-shivam990.vercel.app/)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Vanilla JS](https://img.shields.io/badge/Vanilla-JavaScript-F7DF1E?logo=javascript&logoColor=black)](index.js)
[![Modern CSS](https://img.shields.io/badge/CSS3-Modern_Glassmorphism-264de4?logo=css3&logoColor=white)](index.css)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success?logo=github)](https://s1h2i3v4a.github.io/CodeEditor/)

---

## 📑 Project Documentation & Deliverables

Comprehensive, structured project documentation tailored specifically for **CodeEditor Pro** (starts directly from Index, zero college branding, high-resolution architecture diagrams and lifecycle flowcharts):

- 📄 **Project Report PDF**: [`docs/CodeEditor_Project_Report.pdf`](docs/CodeEditor_Project_Report.pdf) (14 pages, Direct Index start, Chapter 1 to 6, embedded Flowchart & UI Diagrams)
- 📊 **Project Presentation PDF**: [`docs/CodeEditor_Presentation.pdf`](docs/CodeEditor_Presentation.pdf) (11 widescreen slides, Direct Table of Contents, embedded DFD & Flowchart)
- 💻 **Project Presentation PPTX**: [`docs/CodeEditor_Presentation.pptx`](docs/CodeEditor_Presentation.pptx) (Editable PowerPoint Presentation deck)

---

## ✨ Features

- **🚀 Real-Time Live Preview**: Debounced live compilation with safe `srcdoc` isolation and iframe sandboxing (`allow-scripts allow-modals`).
- **🛠️ Integrated Virtual Console**: Intercepts `console.log`, `console.error`, `console.warn`, and `window.onerror` directly into an in-editor developer drawer via `postMessage`.
- **🔢 Line Numbers & Gutter Sync**: Synchronized line numbering that dynamically updates with your code.
- **⌨️ Code Editor Ergonomics**:
  - `Tab` key indents 2 spaces without losing cursor focus.
  - `Ctrl + Enter` / `Cmd + Enter` to force compile and execute.
  - `Ctrl + S` / `Cmd + S` to save and trigger live execution.
- **🎨 Starter Templates**:
  - `🚀 Counter App`: Interactive stateful counter with animations.
  - `✨ 3D Hover Card`: Real-time mouse tracking and 3D illumination tilt.
  - `🌌 Canvas Particles`: 60 FPS interactive constellation physics.
  - `⏱️ Cyberpunk Clock`: Glowing neon live UTC digital clock.
  - `📄 Clean Blank Canvas`: Empty canvas ready for scratch experiments.
- **💾 Auto-Save & Persistence**: Never lose your work — writes automatically to browser `localStorage`.
- **📦 One-Click Project Export**: Download your bundled project as a standalone HTML file containing styles and scripts.
- **📱 Responsive Layout Switching**: Toggle between 3-column split view and single-tabbed view for small screens or focused editing.
- **🖥️ Fullscreen Preview**: Expand the preview stage to full browser viewport with a single click.

---

## 📊 System Architecture & Workflow

### 1. Execution & Compilation Lifecycle
```text
[User Types Code] ──► [Input Event] ──► [Auto-Run Active?]
                                                │
                                    ┌───────────┴───────────┐
                                    ▼ Yes                   ▼ No
                           [Debounce (350ms)]       [Wait for Run/Ctrl+Enter]
                                    │                       │
                                    └───────────┬───────────┘
                                                ▼
                                   [Construct Isolated Doc]
                                   [Inject Console Proxy]
                                                │
                                                ▼
                                    [Assign to iframe.srcdoc]
                                                │
                                                ▼
                                  [Post Logs via postMessage]
                                  [Render Live DOM in Stage]
```

---

## 🚀 Quick Start

No build tools or `npm install` needed! Simply clone and open:

```bash
# Clone the repository
git clone https://github.com/S1h2i3v4a/CodeEditor.git

# Navigate into the folder
cd CodeEditor

# Open in your preferred browser
start index.html     # On Windows
open index.html      # On macOS
xdg-open index.html  # On Linux
```

> **Note on Browser Caching**: If you have opened an older version in your browser, press `Ctrl + F5` (or `Cmd + Shift + R`) to hard-refresh and load the newest styles and scripts!

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| `Ctrl + Enter` / `Cmd + Enter` | Force compile and run code |
| `Ctrl + S` / `Cmd + S` | Save locally and compile |
| `Tab` | Indent with 2 spaces |
| `Escape` | Exit Fullscreen Preview |

---

## 📁 File Structure

```text
CodeEditor/
├── .github/workflows/deploy.yml          # Automated GitHub Pages CI/CD
├── assets/                               # High-res diagrams & flowcharts
│   ├── codeeditor_dfd.png
│   ├── codeeditor_flowchart.png
│   └── codeeditor_ui_diagram.png
├── docs/                                 # Project report & presentation deliverables
│   ├── CodeEditor_Project_Report.pdf     # 14-page report (Direct Index, No College Name)
│   ├── CodeEditor_Presentation.pdf       # 11-slide presentation PDF
│   └── CodeEditor_Presentation.pptx      # PowerPoint deck
├── index.html                            # Modern semantic markup & accessible toolbar
├── index.css                             # Dark theme, glassmorphic UI & responsive layouts
├── index.js                              # Compiler, sandbox runner, virtual console & templates
├── vercel.json                           # Vercel deployment cache-invalidation rules
└── README.md                             # Documentation, architecture & deliverable links
```

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).
Feel free to fork, customize, and build upon it!
