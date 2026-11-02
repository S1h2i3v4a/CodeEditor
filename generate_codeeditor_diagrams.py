"""
generate_codeeditor_diagrams.py
Generates high-resolution publication-quality diagrams for the CodeEditor project:
1. codeeditor_flowchart.png: Execution & Compilation Lifecycle Flowchart
2. codeeditor_dfd.png: System Architecture & Data Flow Diagram (DFD Level-1)
3. codeeditor_ui_diagram.png: Modern UI Component Hierarchy & Layout Diagram
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

ASSETS_DIR = r"c:\Users\Shivam Keshari\OneDrive\Desktop\Code_Editor\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

FLOWCHART_FILE = os.path.join(ASSETS_DIR, "codeeditor_flowchart.png")
DFD_FILE = os.path.join(ASSETS_DIR, "codeeditor_dfd.png")
UI_DIAGRAM_FILE = os.path.join(ASSETS_DIR, "codeeditor_ui_diagram.png")


# ==============================================================================
# 1. FLOWCHART GENERATION (Execution & Compilation Lifecycle)
# ==============================================================================
def generate_flowchart():
    fig, ax = plt.subplots(figsize=(8, 12), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 15)
    ax.axis('off')

    c_blue = '#dbeafe'
    c_blue_b = '#2563eb'
    c_yellow = '#fef3c7'
    c_yellow_b = '#d97706'
    c_green = '#d1fae5'
    c_green_b = '#059669'
    c_red = '#fee2e2'
    c_red_b = '#dc2626'
    c_purple = '#f3e8ff'
    c_purple_b = '#7c3aed'

    def draw_box(x, y, w, h, text, bg, border, shape='round', font_size=9.5, bold=False):
        if shape == 'round':
            p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                               boxstyle="round,pad=0.15,rounding_size=0.25",
                               ec=border, fc=bg, lw=1.8)
            ax.add_patch(p)
        elif shape == 'oval':
            p = FancyBboxPatch((x - w/2, y - h/2), w, h,
                               boxstyle="round,pad=0.2,rounding_size=0.45",
                               ec=border, fc=bg, lw=2.0)
            ax.add_patch(p)
        elif shape == 'diamond':
            pts = [[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]]
            p = Polygon(pts, closed=True, ec=border, fc=bg, lw=1.8)
            ax.add_patch(p)

        weight = 'bold' if bold else 'normal'
        ax.text(x, y, text, ha='center', va='center', fontsize=font_size,
                fontfamily='sans-serif', fontweight=weight, color='#0f172a', multialignment='center')

    def draw_arrow(x1, y1, x2, y2, label=None, label_pos=0.5, label_offset=(0.15, 0), color='#1e293b'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(facecolor=color, edgecolor=color, width=1.4, headwidth=6, headlength=7))
        if label:
            lx = x1 + (x2 - x1) * label_pos + label_offset[0]
            ly = y1 + (y2 - y1) * label_pos + label_offset[1]
            ax.text(lx, ly, label, fontsize=8.5, fontweight='bold', color=color,
                    bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none'))

    # Title
    ax.text(5, 14.5, "CodeEditor Execution & Compilation Lifecycle", ha='center', va='center',
            fontsize=13, fontweight='bold', color='#1e293b')

    # Step 1: Start
    draw_box(5, 13.8, 2.6, 0.65, "Start", c_blue, c_blue_b, shape='oval', bold=True)
    draw_arrow(5, 13.475, 5, 12.85)

    # Step 2: User Input
    draw_box(5, 12.4, 6.2, 0.9, "User Types Code (HTML / CSS / JS)\nor Selects a Starter Template", c_blue, c_blue_b)
    draw_arrow(5, 11.95, 5, 11.3)

    # Step 3: Event Triggered
    draw_box(5, 10.85, 6.2, 0.9, "Input Event Triggered\nUpdate Line Numbers & Sync Gutter Scroll", c_purple, c_purple_b)
    draw_arrow(5, 10.4, 5, 9.75)

    # Step 4: Decision: Auto-run active?
    draw_box(5, 9.15, 5.2, 1.2, "Is Auto-Run\nEnabled?", c_yellow, c_yellow_b, shape='diamond', bold=True)
    
    # Yes -> Debounce
    draw_arrow(5, 8.55, 5, 7.85, label="Yes", label_offset=(0.25, 0))
    # No -> Wait for Run Click
    draw_arrow(7.6, 9.15, 8.8, 9.15, label="No", label_offset=(0, 0.2))
    draw_box(8.8, 8.0, 2.0, 0.9, "Wait for Manual\n'Run' or Ctrl+Enter", c_yellow, c_yellow_b, font_size=8.5)
    draw_arrow(8.8, 9.15, 8.8, 8.45)
    draw_arrow(8.8, 7.55, 8.8, 6.85)
    ax.plot([8.8, 8.8], [6.85, 6.85], color='#1e293b')
    draw_arrow(8.8, 6.85, 7.6, 6.85)

    # Step 5: Debounce Timer
    draw_box(5, 7.4, 5.0, 0.9, "Debounce Delay (350ms)\nCancel Previous Pending Timer", c_blue, c_blue_b)
    draw_arrow(5, 6.95, 5, 6.3)

    # Step 6: Construct Sandbox
    draw_box(5, 5.85, 6.4, 0.9, "Construct Isolated HTML Document\nInject Virtual Console Bridge & Error Hook", c_purple, c_purple_b)
    draw_arrow(5, 5.4, 5, 4.75)

    # Step 7: Assign to iframe.srcdoc
    draw_box(5, 4.3, 6.4, 0.9, "Assign Document to iframe.srcdoc\nSandboxed Execution: allow-scripts allow-modals", c_blue, c_blue_b)
    draw_arrow(5, 3.85, 5, 3.2)

    # Step 8: Decision: Execution Status
    draw_box(5, 2.6, 5.2, 1.2, "Runtime Exception\nor Log Intercepted?", c_yellow, c_yellow_b, shape='diamond', bold=True)

    # Error path (Left)
    draw_arrow(2.4, 2.6, 1.3, 2.6, label="Exception", label_offset=(0, 0.2))
    draw_box(1.3, 1.6, 2.2, 0.8, "Post Error via postMessage\nDisplay in Console Drawer", c_red, c_red_b, font_size=8)
    draw_arrow(1.3, 2.6, 1.3, 2.0)

    # Success path (Bottom)
    draw_arrow(5, 2.0, 5, 1.35, label="Success", label_offset=(0.3, 0))
    draw_box(5, 0.9, 4.8, 0.9, "Render Live DOM in Stage\nPersist Code to LocalStorage", c_green, c_green_b, bold=True)

    # Connector from Error to End
    draw_arrow(1.3, 1.2, 1.3, 0.25)
    draw_arrow(1.3, 0.25, 4.0, 0.25)

    # Step 9: End
    draw_arrow(5, 0.45, 5, 0.05)
    draw_box(5, 0.05, 2.4, 0.5, "End", c_blue, c_blue_b, shape='oval', bold=True)

    # Figure Caption
    fig.text(0.5, 0.01, "Fig. 4.1: Flowchart of the CodeEditor Execution & Compilation Lifecycle",
             ha='center', fontsize=10, fontweight='bold', color='#334155')

    plt.tight_layout()
    plt.savefig(FLOWCHART_FILE, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {FLOWCHART_FILE}")


# ==============================================================================
# 2. DATA FLOW DIAGRAM (DFD Level-1 / Architecture)
# ==============================================================================
def generate_dfd():
    fig, ax = plt.subplots(figsize=(11, 6.8), dpi=300)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    c_blue = '#eff6ff'
    c_blue_b = '#3b82f6'
    c_purple = '#faf5ff'
    c_purple_b = '#8b5cf6'
    c_green = '#f0fdf4'
    c_green_b = '#10b981'
    c_amber = '#fffbeb'
    c_amber_b = '#f59e0b'
    c_cyan = '#ecfeff'
    c_cyan_b = '#06b6d4'
    c_gray = '#f8fafc'
    c_gray_b = '#64748b'

    def draw_entity(x, y, w, h, title, subtitle):
        p = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.15,rounding_size=0.2",
                           ec='#1e293b', fc='#10b981', lw=2)
        ax.add_patch(p)
        # Inner fill
        p_inner = FancyBboxPatch((x - w/2 + 0.08, y - h/2 + 0.08), w - 0.16, h - 0.16,
                                 boxstyle="round,pad=0.15,rounding_size=0.15",
                                 ec='none', fc='#ecfdf5')
        ax.add_patch(p_inner)
        ax.text(x, y + 0.2, title, ha='center', va='center', fontsize=11, fontweight='bold', color='#065f46')
        ax.text(x, y - 0.25, subtitle, ha='center', va='center', fontsize=9, color='#047857')

    def draw_process(num, x, y, w, h, title, desc, bg, border):
        p = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.15,rounding_size=0.25",
                           ec=border, fc=bg, lw=1.8)
        ax.add_patch(p)
        # Number badge
        circle = Circle((x - w/2 + 0.35, y + h/2 - 0.35), 0.22, ec=border, fc=border)
        ax.add_patch(circle)
        ax.text(x - w/2 + 0.35, y + h/2 - 0.35, str(num), ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')
        ax.text(x + 0.1, y + 0.22, title, ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1e293b')
        ax.text(x, y - 0.28, desc, ha='center', va='center', fontsize=8.5, color='#475569', multialignment='center')

    def draw_datastore(x, y, w, h, title, desc):
        # Open ended rectangle (data store)
        ax.plot([x - w/2, x + w/2], [y + h/2, y + h/2], color='#d97706', lw=2)
        ax.plot([x - w/2, x + w/2], [y - h/2, y - h/2], color='#d97706', lw=2)
        ax.plot([x - w/2, x - w/2], [y - h/2, y + h/2], color='#d97706', lw=2)
        p = patches.Rectangle((x - w/2, y - h/2), w, h, fc='#fffbeb', ec='none')
        ax.add_patch(p)
        ax.text(x, y + 0.18, title, ha='center', va='center', fontsize=10, fontweight='bold', color='#92400e')
        ax.text(x, y - 0.22, desc, ha='center', va='center', fontsize=8, color='#b45309')

    def draw_flow(x1, y1, x2, y2, text, offset=(0, 0.2), rad=0):
        connectionstyle = f"arc3,rad={rad}" if rad != 0 else "arc3"
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(facecolor='#1e293b', edgecolor='#1e293b', width=1.3,
                                    headwidth=6, headlength=7, connectionstyle=connectionstyle))
        if text:
            mx = (x1 + x2) / 2 + offset[0]
            my = (y1 + y2) / 2 + offset[1]
            ax.text(mx, my, text, fontsize=8, fontweight='semibold', color='#1e293b',
                    bbox=dict(boxstyle='round,pad=0.2', fc='#ffffff', ec='#cbd5e1', lw=0.8),
                    ha='center', va='center')

    # Main Diagram Header
    p_hdr = FancyBboxPatch((2.5, 8.2), 9, 0.7, boxstyle="round,pad=0.1,rounding_size=0.15",
                           ec='#3b82f6', fc='#eff6ff', lw=1.5)
    ax.add_patch(p_hdr)
    ax.text(7.0, 8.55, "Data Flow Diagram (DFD Level-1) - CodeEditor Pro Architecture",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e40af')

    # Entities and Processes
    draw_entity(1.6, 5.2, 2.2, 1.4, "Web Developer", "(User / Client)")

    draw_process(1, 5.0, 6.2, 2.8, 1.3, "Editor Interface", "HTML / CSS / JS Panes\nTab indent, Line Sync", c_blue, c_blue_b)
    draw_process(2, 5.0, 3.8, 2.8, 1.3, "Compilation Engine", "Debounce Timer (350ms)\nDoc Bundler & Sanitizer", c_purple, c_purple_b)

    draw_datastore(5.0, 1.5, 2.8, 0.9, "D1: LocalStorage", "Saved HTML, CSS, JS Buffers")

    draw_process(3, 9.5, 5.2, 3.2, 1.5, "Sandbox Runtime", "IFrame srcdoc Isolation\nScript Execution & Security", c_amber, c_amber_b)
    draw_process(4, 9.5, 2.0, 3.2, 1.3, "Virtual Console Bridge", "postMessage Interceptor\nLogs, Warnings & Exceptions", c_cyan, c_cyan_b)

    draw_process(5, 12.8, 5.2, 1.8, 1.4, "Live Output", "Rendered Stage\nFullscreen View", c_green, c_green_b)

    # Connecting Data Flows
    draw_flow(2.7, 5.6, 3.6, 6.2, "Code Input / Keystroke", offset=(-0.1, 0.25))
    draw_flow(5.0, 5.55, 5.0, 4.45, "Raw Code Strings", offset=(0.85, 0))
    draw_flow(5.0, 3.15, 5.0, 1.95, "Auto-Save Buffer", offset=(0.85, 0))
    draw_flow(3.6, 1.5, 2.0, 4.5, "Restore Code on Load", offset=(-0.3, -0.2), rad=0.2)

    draw_flow(6.4, 4.2, 7.9, 5.0, "Compiled Bundle with Bridge", offset=(0, 0.25))
    draw_flow(11.1, 5.2, 11.9, 5.2, "DOM Output", offset=(0, 0.2))

    draw_flow(9.5, 4.45, 9.5, 2.65, "Console postMessage", offset=(1.1, 0))
    draw_flow(7.9, 2.0, 2.7, 4.7, "Real-Time Terminal Output", offset=(0, -0.3), rad=0.25)

    # Legend
    p_leg = patches.Rectangle((0.5, 0.3), 3.4, 1.0, fc='#f8fafc', ec='#cbd5e1', lw=1)
    ax.add_patch(p_leg)
    ax.text(0.7, 1.05, "Legend:", fontsize=8.5, fontweight='bold', color='#334155')
    ax.plot([0.7, 1.1], [0.8, 0.8], color='#10b981', lw=3)
    ax.text(1.2, 0.8, "External Entity (User)", fontsize=7.5, va='center')
    ax.plot([0.7, 1.1], [0.55, 0.55], color='#3b82f6', lw=3)
    ax.text(1.2, 0.55, "Process Module", fontsize=7.5, va='center')

    plt.tight_layout()
    plt.savefig(DFD_FILE, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {DFD_FILE}")


# ==============================================================================
# 3. UI ARCHITECTURE / MOCKUP DIAGRAM
# ==============================================================================
def generate_ui_diagram():
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Main dark canvas
    bg = patches.Rectangle((0.2, 0.2), 9.6, 5.6, fc='#0d1117', ec='#30363d', lw=2)
    ax.add_patch(bg)

    # Navbar
    nav = patches.Rectangle((0.2, 5.2), 9.6, 0.6, fc='#161b22', ec='#30363d', lw=1)
    ax.add_patch(nav)
    ax.text(0.5, 5.5, "⚡ CodeEditor PRO", fontsize=11, fontweight='bold', color='#38bdf8', va='center')
    ax.text(3.0, 5.5, "Template: [ Counter App ▼ ]", fontsize=8.5, color='#cbd5e1', va='center')
    ax.text(5.5, 5.5, "[▶ Run (Ctrl+Enter)]   [Format]   [Export HTML]", fontsize=8.5, color='#94a3b8', va='center')
    ax.text(9.4, 5.5, "[⛶ Fullscreen]", fontsize=8, color='#38bdf8', va='center', ha='right')

    # 3 Code Panes
    pane_w = 3.05
    # HTML
    p1 = patches.Rectangle((0.4, 2.5), pane_w, 2.5, fc='#090d13', ec='#30363d', lw=1.2)
    ax.add_patch(p1)
    hdr1 = patches.Rectangle((0.4, 4.6), pane_w, 0.4, fc='#161b22', ec='#30363d')
    ax.add_patch(hdr1)
    ax.text(0.6, 4.8, "</> HTML", fontsize=9, fontweight='bold', color='#f97316', va='center')
    ax.text(0.6, 4.2, "1  <div class=\"card\">\n2    <h1 id=\"count\">0</h1>\n3    <button id=\"inc\">+</button>\n4  </div>",
            fontsize=8, fontfamily='monospace', color='#e2e8f0', va='top')

    # CSS
    p2 = patches.Rectangle((3.6, 2.5), pane_w, 2.5, fc='#090d13', ec='#30363d', lw=1.2)
    ax.add_patch(p2)
    hdr2 = patches.Rectangle((3.6, 4.6), pane_w, 0.4, fc='#161b22', ec='#30363d')
    ax.add_patch(hdr2)
    ax.text(3.8, 4.8, "# CSS", fontsize=9, fontweight='bold', color='#06b6d4', va='center')
    ax.text(3.8, 4.2, "1  body { display: flex; }\n2  .card { padding: 30px; }\n3  h1 { color: #38bdf8; }",
            fontsize=8, fontfamily='monospace', color='#e2e8f0', va='top')

    # JS
    p3 = patches.Rectangle((6.8, 2.5), pane_w, 2.5, fc='#090d13', ec='#30363d', lw=1.2)
    ax.add_patch(p3)
    hdr3 = patches.Rectangle((6.8, 4.6), pane_w, 0.4, fc='#161b22', ec='#30363d')
    ax.add_patch(hdr3)
    ax.text(7.0, 4.8, "JS JavaScript", fontsize=9, fontweight='bold', color='#eab308', va='center')
    ax.text(7.0, 4.2, "1  const btn = $('#inc');\n2  let count = 0;\n3  btn.onclick = () => {\n4    console.log(++count);\n5  };",
            fontsize=8, fontfamily='monospace', color='#e2e8f0', va='top')

    # Bottom Split: Live Preview Stage (Left) & Virtual Console (Right)
    stage = patches.Rectangle((0.4, 0.65), 5.4, 1.7, fc='#ffffff', ec='#30363d', lw=1.2)
    ax.add_patch(stage)
    s_hdr = patches.Rectangle((0.4, 2.05), 5.4, 0.3, fc='#f1f5f9', ec='#cbd5e1')
    ax.add_patch(s_hdr)
    ax.text(0.6, 2.2, "● LIVE PREVIEW STAGE (Sandboxed IFrame)", fontsize=8, fontweight='bold', color='#0f172a', va='center')
    # Mini mockup inside preview
    m_box = patches.Rectangle((1.8, 0.8), 2.6, 1.0, fc='#0f172a', ec='#38bdf8', lw=1)
    ax.add_patch(m_box)
    ax.text(3.1, 1.45, "COUNTER APP", fontsize=7.5, color='#38bdf8', ha='center', fontweight='bold')
    ax.text(3.1, 1.15, "0", fontsize=14, color='#ffffff', ha='center', fontweight='bold')
    ax.text(3.1, 0.9, "[ - ]   [ Reset ]   [ + ]", fontsize=7, color='#94a3b8', ha='center')

    # Virtual Console (Right)
    cons = patches.Rectangle((6.0, 0.65), 3.85, 1.7, fc='#030712', ec='#30363d', lw=1.2)
    ax.add_patch(cons)
    c_hdr = patches.Rectangle((6.0, 2.05), 3.85, 0.3, fc='#111827', ec='#374151')
    ax.add_patch(c_hdr)
    ax.text(6.2, 2.2, "⚡ VIRTUAL CONSOLE DRAWER", fontsize=8, fontweight='bold', color='#10b981', va='center')
    ax.text(6.2, 1.85, "• Console initialized. Ready for execution...", fontsize=7.5, fontfamily='monospace', color='#6b7280')
    ax.text(6.2, 1.55, "• Counter App Ready! Try clicking + / -", fontsize=7.5, fontfamily='monospace', color='#d1d5db')
    ax.text(6.2, 1.25, "• Current count value: 1", fontsize=7.5, fontfamily='monospace', color='#38bdf8')
    ax.text(6.2, 0.95, "• Current count value: 2", fontsize=7.5, fontfamily='monospace', color='#38bdf8')

    # Status Bar
    sb = patches.Rectangle((0.2, 0.2), 9.6, 0.35, fc='#080c10', ec='#30363d', lw=1)
    ax.add_patch(sb)
    ax.text(0.4, 0.37, "● Ready   |   JS - Ln 4, Col 12   |   45 lines total", fontsize=7.5, color='#94a3b8', va='center')
    ax.text(9.4, 0.37, "Saved locally  |  ⌨️ Ctrl + Enter to Run", fontsize=7.5, color='#64748b', va='center', ha='right')

    # Figure label
    fig.text(0.5, 0.02, "Fig. 5.1: High-Performance Multi-Pane UI Layout of CodeEditor Pro",
             ha='center', fontsize=9.5, fontweight='bold', color='#334155')

    plt.tight_layout()
    plt.savefig(UI_DIAGRAM_FILE, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {UI_DIAGRAM_FILE}")


if __name__ == "__main__":
    generate_flowchart()
    generate_dfd()
    generate_ui_diagram()
