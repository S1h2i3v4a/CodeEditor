# ⚡ CodeEditor Pro

> A blazing fast, modern, and developer-friendly in-browser playground for HTML, CSS, and JavaScript with debounced live reload, integrated virtual console, and local persistence.

🌐 **Live Demo**: [https://codeeditor-7b92ehw0x-shivam990.vercel.app/](https://codeeditor-7b92ehw0x-shivam990.vercel.app/)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Vanilla JS](https://img.shields.io/badge/Vanilla-JavaScript-F7DF1E?logo=javascript&logoColor=black)](index.js)
[![Modern CSS](https://img.shields.io/badge/CSS3-Modern_Glassmorphism-264de4?logo=css3&logoColor=white)](index.css)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)](#)

---

## ✨ Features

- **🚀 Real-Time Live Preview**: Debounced live compilation with safe `srcdoc` isolation and iframe sandboxing.
- **🛠️ Integrated Virtual Console**: Intercepts `console.log`, `console.error`, `console.warn`, and `window.onerror` directly into an in-editor developer drawer.
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
├── index.html        # Modern semantic markup, accessible toolbar & panes
├── index.css         # Dark theme, glassmorphic UI & responsive layouts
├── index.js          # Compiler, sandbox runner, virtual console & templates
└── README.md         # Documentation & guide
```

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).
Feel free to fork, customize, and build upon it!
