import os
import datetime
import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import pandas as pd

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="CyberSignals — Cyber Risk Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Session state defaults ──────────────────────────────────────────────────
if "_audience" not in st.session_state:
    st.session_state["_audience"] = "simple"
if "_scroll_guides" not in st.session_state:
    st.session_state["_scroll_guides"] = False
if "_nav_tab" not in st.session_state:
    st.session_state["_nav_tab"] = 0

# ─────────────────────────────────────────
# DESIGN TOKENS — light mode
# ─────────────────────────────────────────
BG      = "#ffffff"
SURFACE = "#f1f5f9"
BORDER  = "#e2e8f0"
BORDER2 = "#cbd5e1"
TEXT    = "#0f172a"
MUTED   = "#475569"
ACCENT  = "#2563eb"
ACCENT2 = "#7c3aed"
RED     = "#dc2626"
ORANGE  = "#ea580c"
GREEN   = "#16a34a"
YELLOW  = "#b45309"
PINK    = "#be185d"

# chart-ready bar colors (fully saturated)
C_BLUE  = "#3b82f6"
C_RED   = "#ef4444"
C_GREEN = "#22c55e"
C_AMBER = "#f59e0b"
C_PURP  = "#8b5cf6"

# ─────────────────────────────────────────
# GLOBAL CSS — light theme
# ─────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=block');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif !important;
    background-color: {BG} !important;
    color: {TEXT} !important;
}}
/* Hide the raw "keyboard_double_arrow_*" text inside sidebar collapse spans */
[data-testid="stSidebarCollapseButton"] button span,
[data-testid="collapsedControl"] button span,
[data-testid="stSidebarCollapsedControl"] button span,
section[data-testid="stSidebar"] header button span {{
    font-size: 0 !important;
    width: 0 !important;
    height: 0 !important;
    overflow: hidden !important;
    display: inline-block !important;
    visibility: hidden !important;
    pointer-events: none !important;
}}
/* Inject a clean arrow — collapse button (sidebar open) */
[data-testid="stSidebarCollapseButton"] button::before,
section[data-testid="stSidebar"] header button::before {{
    content: "‹" !important;
    font-size: 20px !important;
    font-family: sans-serif !important;
    color: #ffffff !important;
    line-height: 1 !important;
    pointer-events: none !important;
}}
/* Inject a clean arrow — expand button (sidebar collapsed) */
[data-testid="collapsedControl"] button::before,
[data-testid="stSidebarCollapsedControl"] button::before {{
    content: "›" !important;
    font-size: 20px !important;
    font-family: sans-serif !important;
    color: #cbd5e1 !important;
    line-height: 1 !important;
    pointer-events: none !important;
}}
.stApp {{
    background-color: {BG} !important;
}}
.main .block-container {{
    padding: 2.5rem 3rem 4rem 3rem !important;
    max-width: 1400px !important;
    background: transparent !important;
}}

h1 {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 2rem !important;
    color: {TEXT} !important;
    letter-spacing: -0.01em !important;
    line-height: 1.25 !important;
    margin-bottom: 0.5rem !important;
}}
h2 {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 1.2rem !important;
    color: {TEXT} !important;
    margin-top: 2rem !important;
    margin-bottom: 1rem !important;
    padding-bottom: 0.6rem !important;
    border-bottom: 1px solid {BORDER} !important;
    letter-spacing: 0 !important;
}}
h3 {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
    color: {TEXT} !important;
    margin-top: 0 !important;
    margin-bottom: 0.4rem !important;
    letter-spacing: 0 !important;
}}
h4 {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    color: {TEXT} !important;
    margin-top: 0 !important;
    margin-bottom: 0.35rem !important;
    letter-spacing: 0 !important;
}}
p, .stMarkdown p {{
    font-family: 'Inter', sans-serif !important;
    color: {TEXT} !important;
    font-size: 0.93rem !important;
    line-height: 1.7 !important;
}}
[data-testid="stCaptionContainer"] p {{
    color: {MUTED} !important;
    font-size: 0.83rem !important;
    line-height: 1.6 !important;
}}

/* ── CHART CARD SHADOW ── */
.js-plotly-plot {{
    border-radius: 10px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.07), 0 4px 16px rgba(0,0,0,0.06) !important;
    overflow: hidden !important;
}}

/* ── SIDEBAR BACKGROUND — full height, no white gaps ── */
section[data-testid="stSidebar"] {{
    background-color: #1e293b !important;
    background: #1e293b !important;
    border-right: 1px solid #334155 !important;
    min-height: 100vh !important;
}}
section[data-testid="stSidebar"] > div {{
    background-color: #1e293b !important;
    background: #1e293b !important;
    min-height: 100vh !important;
    /* Keep content anchored to the top, not pushed to the bottom */
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    align-items: stretch !important;
}}
section[data-testid="stSidebar"] > div > div,
section[data-testid="stSidebar"] > div > div > div,
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {{
    background-color: #1e293b !important;
    background: #1e293b !important;
}}
[data-testid="stSidebar"] .block-container {{
    background: #1e293b !important;
    padding: 1rem 0.75rem !important;
}}

/* ── SIDEBAR COLLAPSE BUTTON — style only, let Streamlit control show/hide ── */
/* DO NOT set display/visibility here — Streamlit JS manages that and fights us */
[data-testid="stSidebarCollapseButton"] button {{
    opacity: 1 !important;
    background: rgba(255,255,255,0.12) !important;
    border-radius: 6px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}}
[data-testid="stSidebarCollapseButton"] button:hover {{
    background: rgba(255,255,255,0.22) !important;
}}
/* Collapsed-state re-open button (two possible testids across Streamlit versions) */
[data-testid="collapsedControl"] button,
[data-testid="stSidebarCollapsedControl"] button {{
    opacity: 1 !important;
    background: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 6px !important;
}}

/* ── ALL TEXT IN SIDEBAR WHITE ── */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {{
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
}}
/* Override any white/light background on sidebar children */
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"],
section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"],
section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"],
section[data-testid="stSidebar"] [data-testid="stSidebarContent"],
section[data-testid="stSidebar"] .css-1d391kg,
section[data-testid="stSidebar"] .stElementContainer,
section[data-testid="stSidebar"] .element-container,
section[data-testid="stSidebar"] .stMarkdown {{
    background: transparent !important;
    background-color: transparent !important;
}}
/* Kill the white bottom spacer Streamlit injects */
section[data-testid="stSidebar"] > div > div:last-child,
section[data-testid="stSidebar"] > div:last-child {{
    background: #1e293b !important;
    background-color: #1e293b !important;
}}

/* ── NAV BUTTONS ── */
[data-testid="stSidebar"] .stButton > button,
[data-testid="stSidebar"] .stButton > button p,
[data-testid="stSidebar"] .stButton > button span {{
    background: transparent !important;
    border: none !important;
    border-left: 3px solid transparent !important;
    border-radius: 0 6px 6px 0 !important;
    color: #cbd5e1 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.875rem !important;
    font-weight: 400 !important;
    text-align: left !important;
    width: 100% !important;
    padding: 0.5rem 0.75rem !important;
    margin-bottom: 2px !important;
    justify-content: flex-start !important;
    transition: background 0.15s, color 0.15s !important;
    box-shadow: none !important;
}}
[data-testid="stSidebar"] .stButton > button:hover,
[data-testid="stSidebar"] .stButton > button:hover p,
[data-testid="stSidebar"] .stButton > button:hover span {{
    background: rgba(255,255,255,0.08) !important;
    color: #ffffff !important;
    border-left: 3px solid #3b82f6 !important;
}}
[data-testid="stSidebar"] .stButton > button:focus,
[data-testid="stSidebar"] .stButton > button:active,
[data-testid="stSidebar"] .stButton > button:focus p,
[data-testid="stSidebar"] .stButton > button:focus span {{
    background: rgba(59,130,246,0.18) !important;
    color: #ffffff !important;
    border-left: 3px solid #3b82f6 !important;
    box-shadow: none !important;
    outline: none !important;
}}

/* ── METRICS ── */
[data-testid="metric-container"] {{
    background: {BG} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 10px !important;
    padding: 1rem 1.2rem !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}}
[data-testid="metric-container"] label,
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] > div,
[data-testid="stMetricLabel"] p {{
    color: {MUTED} !important;
    font-size: 0.72rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    font-family: 'Inter', sans-serif !important;
    white-space: normal !important;
    overflow: visible !important;
    text-overflow: unset !important;
    word-break: break-word !important;
    line-height: 1.3 !important;
}}
[data-testid="metric-container"] [data-testid="stMetricValue"] {{
    font-family: 'Inter', sans-serif !important;
    font-size: 1.45rem !important;
    font-weight: 600 !important;
    color: {ACCENT} !important;
}}
[data-testid="metric-container"] [data-testid="stMetricDelta"] {{
    font-size: 0.75rem !important;
    font-family: 'Inter', sans-serif !important;
}}

hr {{
    border: none !important;
    border-top: 1px solid {BORDER2} !important;
    margin: 2.5rem 0 !important;
}}
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: {SURFACE}; }}
::-webkit-scrollbar-thumb {{ background: {BORDER2}; border-radius: 3px; }}

/* ── STICKY BRANDED TOOLBAR ── */
[data-testid="stHeader"] {{
    background-color: #0f172a !important;
    border-bottom: 2px solid rgba(37,99,235,0.5) !important;
    position: sticky !important;
    top: 0 !important;
    z-index: 999999 !important;
}}
[data-testid="stHeader"]::before {{
    content: "🛡️  CyberSignals";
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    color: #ffffff;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 0.9rem;
    letter-spacing: 0.01em;
    white-space: nowrap;
    pointer-events: none;
}}
/* keep Streamlit's own toolbar buttons visible and white against dark bar */
[data-testid="stHeader"] button,
[data-testid="stHeader"] a,
[data-testid="stHeader"] [data-testid="stDecoration"] {{
    position: relative;
    z-index: 1;
    color: #ffffff !important;
}}
[data-testid="stHeader"] button svg,
[data-testid="stHeader"] a svg,
[data-testid="stHeader"] [data-testid="stToolbar"] svg,
[data-testid="stHeader"] [data-testid="stToolbar"] button,
[data-testid="stHeader"] [data-testid="stStatusWidget"] svg,
[data-testid="stHeader"] [data-testid="stStatusWidget"] span,
[data-testid="stHeader"] [data-testid="stStatusWidget"] p {{
    color: #ffffff !important;
    fill: #ffffff !important;
    stroke: #ffffff !important;
}}
[data-testid="stHeader"] button:hover {{
    background: rgba(255,255,255,0.12) !important;
    border-radius: 6px;
}}
/* ── SIDEBAR EXPAND TAB (visible on main bg when sidebar is closed) ── */
[data-testid="stSidebarCollapsedControl"] {{
    background-color: #1e293b !important;
    border-radius: 0 8px 8px 0 !important;
    border-right: 2px solid #3b82f6 !important;
    border-top: 1px solid #334155 !important;
    border-bottom: 1px solid #334155 !important;
    padding: 6px 4px !important;
    min-width: 36px !important;
}}
[data-testid="stSidebarCollapsedControl"] button {{
    color: #ffffff !important;
    background: transparent !important;
    border: none !important;
    border-radius: 4px !important;
    min-width: 30px !important;
    min-height: 30px !important;
}}
[data-testid="stSidebarCollapsedControl"] button:hover {{
    background: rgba(59,130,246,0.3) !important;
}}
[data-testid="stSidebarCollapsedControl"] button span,
[data-testid="stSidebarCollapsedControl"] button svg {{
    color: #ffffff !important;
    fill: #ffffff !important;
    opacity: 1 !important;
}}

/* ── FORCE LIGHT MODE ON ALL REMAINING DARK ELEMENTS ── */
[data-testid="stAppViewContainer"],
[data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"],
section[data-testid="stMain"],
section[data-testid="stMain"] > div {{
    background-color: {BG} !important;
    color: {TEXT} !important;
}}
/* Select / input widgets */
[data-baseweb="select"] > div,
[data-baseweb="input"] > div,
[data-baseweb="textarea"] > div,
[data-baseweb="base-input"],
[data-baseweb="base-input"] input {{
    background-color: {BG} !important;
    color: {TEXT} !important;
    border-color: {BORDER2} !important;
}}
/* Selectbox dropdown list */
[data-baseweb="menu"],
[data-baseweb="menu"] ul,
[data-baseweb="menu"] li {{
    background-color: {BG} !important;
    color: {TEXT} !important;
}}
[data-baseweb="menu"] li:hover {{
    background-color: {SURFACE} !important;
}}
/* Slider */
[data-testid="stSlider"] [data-baseweb="slider"] {{
    background-color: transparent !important;
}}
/* Tab bar */
[data-testid="stTabs"] [data-baseweb="tab-list"] {{
    background-color: {SURFACE} !important;
    border-bottom: 1px solid {BORDER2} !important;
}}
[data-testid="stTabs"] [data-baseweb="tab"] {{
    background-color: transparent !important;
    color: {MUTED} !important;
}}
[data-testid="stTabs"] [aria-selected="true"] {{
    color: {ACCENT} !important;
    border-bottom: 2px solid {ACCENT} !important;
}}
/* Warning / info / error banners */
[data-testid="stAlert"] {{
    background-color: {SURFACE} !important;
    color: {TEXT} !important;
}}
/* Caption text */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {{
    color: {MUTED} !important;
}}
/* Generic dark overlay fix */
.stApp > header {{ background: transparent !important; }}

/* ── DIALOG / MODAL ── */
[data-testid="stDialog"] > div,
[data-testid="stModal"] > div,
div[role="dialog"] {{
    background-color: {BG} !important;
    color: {TEXT} !important;
    border-radius: 12px !important;
}}
div[role="dialog"] h3,
div[role="dialog"] h4,
div[role="dialog"] p,
div[role="dialog"] span,
div[role="dialog"] label {{
    color: {TEXT} !important;
    font-family: 'Inter', sans-serif !important;
}}
div[role="dialog"] .stMarkdown p {{
    color: {TEXT} !important;
}}

/* ── FULL ANALYSIS BUTTON ── */
button[kind="primary"] {{
    background-color: {ACCENT} !important;
    color: #ffffff !important;
    border: none !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    border-radius: 8px !important;
    padding: 6px 16px !important;
}}
button[kind="primary"]:hover {{
    background-color: #1d4ed8 !important;
    color: #ffffff !important;
}}
</style>
""", unsafe_allow_html=True)

# Inject JS via iframe so it actually executes (st.markdown strips <script> tags)
components.html("""
<script>
(function() {
    function clean() {
        var parentDoc = window.parent.document;
        // Hide raw "keyboard_double_arrow_*" text (shows when Material Symbols font missing)
        var collapseSpanSel = [
            '[data-testid="stSidebarCollapseButton"] button span',
            '[data-testid="collapsedControl"] button span',
            '[data-testid="stSidebarCollapsedControl"] button span',
            'section[data-testid="stSidebar"] header button span'
        ].join(', ');
        parentDoc.querySelectorAll(collapseSpanSel).forEach(function(span) {
            span.style.fontSize      = '0';
            span.style.width         = '0';
            span.style.height        = '0';
            span.style.overflow      = 'hidden';
            span.style.visibility    = 'hidden';
            span.style.display       = 'inline-block';
            span.style.pointerEvents = 'none';
        });
        // Remove tooltip title attributes from collapse/expand buttons
        var collapseBtnSel = [
            '[data-testid="stSidebarCollapseButton"] button',
            '[data-testid="collapsedControl"] button',
            '[data-testid="stSidebarCollapsedControl"] button'
        ].join(', ');
        parentDoc.querySelectorAll(collapseBtnSel).forEach(function(btn) {
            btn.removeAttribute('title');
            btn.setAttribute('aria-label', '');
        });
    }
    clean();
    var obs = new MutationObserver(clean);
    obs.observe(window.parent.document.body, { childList: true, subtree: true });
})();
</script>
""", height=0)

# ─────────────────────────────────────────
# AUDIENCE BADGE HELPER
# ─────────────────────────────────────────
_AUDIENCE_STYLES = {
    "simple":  {"icon": "💡", "label": "Plain & Simple",  "bg": "#fffbeb", "border": "#fde68a", "color": "#92400e"},
    "expert":  {"icon": "⚙️", "label": "Expert Console",  "bg": "#eff6ff", "border": "#bfdbfe", "color": "#1d4ed8"},
    "exec":    {"icon": "💼", "label": "Executive Brief",  "bg": "#f0fdf4", "border": "#bbf7d0", "color": "#15803d"},
}
def audience_badge(key):
    s = _AUDIENCE_STYLES[key]
    return (
        f'<span style="display:inline-flex;align-items:center;gap:5px;'
        f'font-size:0.72rem;font-weight:600;color:{s["color"]};'
        f'background:{s["bg"]};border:1px solid {s["border"]};'
        f'border-radius:20px;padding:3px 10px;font-family:\'Inter\',sans-serif;">'
        f'{s["icon"]} {s["label"]}</span>'
    )

# CHART BASE LAYOUT
# ─────────────────────────────────────────
def chart_layout(height=420, show_legend=True, legend_y=-0.2):
    return dict(
        height=height,
        margin=dict(l=56, r=24, t=36, b=56),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12, color=TEXT),
        showlegend=show_legend,
        legend=dict(
            orientation="h", y=legend_y,
            font=dict(size=11, color=MUTED),
            bgcolor="rgba(0,0,0,0)",
        ),
        xaxis=dict(
            gridcolor="#f1f5f9", gridwidth=1,
            zerolinecolor=BORDER,
            tickfont=dict(color=MUTED, size=11),
            linecolor=BORDER2,
            title_font=dict(size=12, color=MUTED),
        ),
        yaxis=dict(
            gridcolor="#f1f5f9", gridwidth=1,
            zerolinecolor=BORDER,
            tickfont=dict(color=MUTED, size=11),
            linecolor=BORDER2,
            title_font=dict(size=12, color=MUTED),
        ),
    )

# ─────────────────────────────────────────
# CITATION BADGE helper
# ─────────────────────────────────────────
def source_badge(extra="", url=None, label=None):
    """Render a source citation badge.
    Pass url + label to override the default DBIR source with a custom link.
    Pass extra="" with no url/label to use DBIR (backward-compatible default).
    """
    if url and label:
        source_link = (f'<a href="{url}" target="_blank" '
                       f'style="color:{ACCENT};text-decoration:none;">{label}</a>')
        date_str = ""
    else:
        source_link = (f'<a href="https://www.verizon.com/business/resources/reports/dbir/" '
                       f'target="_blank" style="color:{ACCENT};text-decoration:none;">'
                       f'Verizon 2025 Data Breach Investigations Report (DBIR)</a>')
        date_str = " · Nov 2023 – Oct 2024"
    detail = f" · {extra}" if extra else ""
    return f"""
<div style="
    display:flex;align-items:center;gap:10px;
    margin:2px 0 12px 0;
    padding:9px 16px;
    background:#eff6ff;
    border-left:4px solid {ACCENT};
    border-radius:0 8px 8px 0;
">
  <span style="font-size:16px;">📊</span>
  <span style="font-family:'Inter',sans-serif;font-size:0.83rem;font-weight:400;color:{MUTED};">
    Source: {source_link}
    <span style="font-weight:400;">{date_str}{detail}</span>
  </span>
</div>"""

def insight_box(headline, body):
    """Renders a short insight callout below a chart."""
    return f"""
<div style="
    margin:0 0 28px 0;
    padding:14px 18px;
    background:#f8fafc;
    border:1px solid {BORDER};
    border-left:4px solid {ACCENT2};
    border-radius:0 8px 8px 0;
    font-family:'Inter',sans-serif;
">
  <p style="margin:0 0 5px 0;font-size:0.88rem;font-weight:500;color:{TEXT};">💡 {headline}</p>
  <p style="margin:0;font-size:0.84rem;color:{MUTED};line-height:1.7;">{body}</p>
</div>"""

# ─────────────────────────────────────────
# FULL ANALYSIS DIALOG
# ─────────────────────────────────────────
@st.dialog("📊 Full Chart Analysis", width="large")
def show_full_analysis():
    title    = st.session_state.get("_dlg_title",   "Chart Analysis")
    fig_json = st.session_state.get("_dlg_fig",     None)
    source   = st.session_state.get("_dlg_source",  "")
    headline = st.session_state.get("_dlg_headline","")
    body     = st.session_state.get("_dlg_body",    "")
    extended = st.session_state.get("_dlg_extended","")

    # Side-by-side: chart on left, analysis on right — no scrolling needed
    col_chart, col_text = st.columns([3, 2], gap="large")

    with col_chart:
        st.markdown(f"**{title}**")
        if fig_json:
            import plotly.io as pio
            fig_big = pio.from_json(fig_json)
            fig_big.update_layout(height=480, margin=dict(l=40, r=20, t=30, b=40))
            st.plotly_chart(fig_big, use_container_width=True,
                            config={"displayModeBar": False})
        st.markdown(source_badge(source), unsafe_allow_html=True)

    with col_text:
        st.markdown(f"""
<div style="padding:14px 18px;background:#f8fafc;border:1px solid {BORDER};
            border-left:4px solid {ACCENT2};border-radius:0 8px 8px 0;
            font-family:'Inter',sans-serif;margin-bottom:14px;">
  <p style="margin:0 0 6px 0;font-size:0.86rem;font-weight:500;color:{TEXT};">💡 {headline}</p>
  <p style="margin:0;font-size:0.83rem;color:{MUTED};line-height:1.7;">{body}</p>
</div>""", unsafe_allow_html=True)
        if extended:
            st.markdown(f"""
<div style="padding:14px 18px;background:#eff6ff;border:1px solid #bfdbfe;
            border-left:4px solid {ACCENT};border-radius:0 8px 8px 0;
            font-family:'Inter',sans-serif;">
  <p style="margin:0 0 6px 0;font-size:0.86rem;font-weight:500;color:{ACCENT};">🔍 Deeper Dive</p>
  <p style="margin:0;font-size:0.83rem;color:{TEXT};line-height:1.7;">{extended}</p>
</div>""", unsafe_allow_html=True)

def open_analysis_btn(key, fig, title, source, headline, body, extended=""):
    """Renders a small button that opens the full analysis dialog."""
    if st.button("📖 Full Analysis", key=f"dlg_{key}", type="primary",
                 help="Open enlarged chart with extended analysis"):
        st.session_state["_dlg_title"]    = title
        st.session_state["_dlg_fig"]      = fig.to_json()
        st.session_state["_dlg_source"]   = source
        st.session_state["_dlg_headline"] = headline
        st.session_state["_dlg_body"]     = body
        st.session_state["_dlg_extended"] = extended
        show_full_analysis()

# ─────────────────────────────────────────
# DATA
# ─────────────────────────────────────────
df_industry = pd.DataFrame({
    "Industry":  ["Finance","Manufacturing","Healthcare","Professional Services","Public Administration",
                  "Information","Education","Retail","Wholesale","Transportation",
                  "Entertainment","Utilities","Construction","Real Estate","Other Services"],
    "Incidents": [3336,3837,1710,2549,1422,1589,1075,837,330,361,493,358,307,339,683],
    "Breaches":  [927,1607,1542,1147,946,784,851,419,319,248,293,213,252,320,583],
}).sort_values("Breaches", ascending=True)

df_patterns = pd.DataFrame({
    "Pattern":   ["System Intrusion","Denial of Service","Social Engineering",
                  "Basic Web Application","Miscellaneous Errors","Privilege Misuse","Lost & Stolen Assets"],
    "Incidents": [9124,6520,4009,1701,1476,825,149],
    "Breaches":  [7302,2,3405,1387,1449,757,122],
})

df_access = pd.DataFrame({
    "Vector": ["Stolen Credentials","Vulnerability Exploitation","Phishing","Edge Devices & VPNs"],
    "Pct":    [22,20,15,22],
})

df_ransom = pd.DataFrame({
    "Year":               ["2022","2023","2024"],
    "In Breaches (%)":    [25,32,44],
    "Refused to Pay (%)": [50,55,64],
})

df_ransom_sector = pd.DataFrame({
    "Sector":         ["Finance","Public Administration","Information Technology",
                       "Healthcare","Professional Services","Education","Manufacturing"],
    "Ransomware (%)": [18, 30, 32, 35, 38, 50, 47],
}).sort_values("Ransomware (%)")

df_data = pd.DataFrame({
    "Data Type":           ["Internal Documents","Personal Data","Credentials","Medical Records",
                            "Secrets & API Keys","Sensitive Personal Data","Bank Data","Payment Cards"],
    "Relative Prevalence": [9,8,7,6,5,4,3,1],
}).sort_values("Relative Prevalence")

radar_sectors  = ["Finance","Manufacturing","Healthcare","Professional Services",
                  "Public Administration","Education","Retail","Information Technology"]
radar_breaches = [927,1607,1542,1147,946,851,419,784]
radar_norm     = [round(b/max(radar_breaches)*10,1) for b in radar_breaches]

vuln_weeks = [f"Wk {w}" for w in range(1,13)]
vuln_series = {
    "Remote Access":    [18,19,21,22,23,25,26,27,29,31,29,30],
    "Vendor Risk":      [12,13,14,16,17,19,21,22,23,24,24,25],
    "Phishing":         [25,24,23,24,23,22,24,23,24,22,21,20],
    "Misconfiguration": [22,21,20,21,23,20,19,18,17,16,16,15],
    "Legacy & Unpatched Systems": [8, 8, 9, 8, 8, 8, 9,10,11,12,11,10],
}
vuln_colors = [C_BLUE, C_PURP, PINK, C_AMBER, C_GREEN]

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
# selected_sectors consumed by sector chart — include all so chart shows full data
selected_sectors = [
    "Finance","Manufacturing","Healthcare","Professional Services","Public Administration",
    "Information","Education","Retail","Wholesale","Transportation",
    "Utilities","Construction","Real Estate","Entertainment","Other Services",
]

with st.sidebar:
    st.markdown(f"""
<div style="padding:0.5rem 0.25rem 1rem 0.25rem;border-bottom:1px solid rgba(255,255,255,0.1);margin-bottom:0.6rem;">
  <p style="margin:0;font-size:1rem;font-weight:600;color:#ffffff;font-family:'Inter',sans-serif;letter-spacing:-0.01em;">🛡️ CyberSignals</p>
  <p style="margin:2px 0 0 0;font-size:0.68rem;color:rgba(255,255,255,0.4);font-family:'Inter',sans-serif;">Cyber Risk Intelligence</p>
</div>
""", unsafe_allow_html=True)

    _NAV = [
        ("🏠", "Home",           0),
        ("📡", "Sector Risk",    1),
        ("⚔️", "Attack Methods", 2),
        ("🔓", "Ransomware",     3),
        ("🗂️", "Stolen Data",    4),
        ("📈", "Trends",         5),
        ("🏭", "ICS Threats",    6),
    ]
    for _ni, _nl, _nidx in _NAV:
        if st.button(f"{_ni}  {_nl}", key=f"_nav_{_nidx}", use_container_width=True):
            st.session_state["_nav_tab"] = _nidx
            st.rerun()

    st.markdown(f"""
<div style="margin-top:1.2rem;padding-top:0.8rem;border-top:1px solid rgba(255,255,255,0.1);">
  <p style="margin:0 0 3px 0;font-size:0.67rem;color:rgba(255,255,255,0.35);font-family:'Inter',sans-serif;">Verizon DBIR 2025 · 22,052 incidents</p>
  <p style="margin:0 0 3px 0;font-size:0.67rem;color:rgba(255,255,255,0.35);font-family:'Inter',sans-serif;">Kaspersky ICS-CERT Q2 2025</p>
  <p style="margin:0;font-size:0.67rem;color:rgba(255,255,255,0.25);font-family:'Inter',sans-serif;">Team N5 · USI4280</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────
st.markdown(f"""
<div style="display:flex;align-items:center;gap:10px;margin-bottom:20px;flex-wrap:wrap;">
  <div style="display:inline-flex;align-items:center;gap:8px;
              font-size:13px;font-weight:600;letter-spacing:0;
              color:{ACCENT};border:1.5px solid rgba(37,99,235,0.25);
              padding:7px 16px;border-radius:8px;background:rgba(37,99,235,0.05);">
    <span style="width:8px;height:8px;border-radius:50%;background:{ACCENT};display:inline-block;flex-shrink:0;"></span>
    Live Threat Intelligence
  </div>
  <div style="display:inline-flex;align-items:center;
              font-size:13px;font-weight:500;letter-spacing:0;
              color:{MUTED};border:1px solid {BORDER2};padding:7px 16px;border-radius:8px;background:{SURFACE};">
    Verizon DBIR 2025
  </div>
  <div style="display:inline-flex;align-items:center;
              font-size:13px;font-weight:500;letter-spacing:0;
              color:{MUTED};border:1px solid {BORDER2};padding:7px 16px;border-radius:8px;background:{SURFACE};">
    Kaspersky ICS-CERT Q2 2025
  </div>
  <div style="display:inline-flex;align-items:center;
              font-size:13px;font-weight:500;letter-spacing:0;
              color:{MUTED};border:1px solid {BORDER2};padding:7px 16px;border-radius:8px;background:{SURFACE};">
    Team N5 · USI4280
  </div>
</div>
""", unsafe_allow_html=True)

st.title("🛡️ CyberSignals")
st.caption("Cyber risk intelligence · DBIR 2025 · 22,052 incidents · 12,195 breaches")

# ─────────────────────────────────────────
# AUDIENCE GUIDE QUICK ACCESS — above tab bar
# ─────────────────────────────────────────
st.markdown(
    f'<p style="font-size:0.78rem;color:{MUTED};font-family:\'Inter\',sans-serif;margin:0.4rem 0 0.5rem 0;">'
    '📚 Jump straight to an audience guide:</p>',
    unsafe_allow_html=True,
)
_aq1, _aq2, _aq3 = st.columns(3, gap="small")
if _aq1.button("💡 Plain & Simple", use_container_width=True, key="_go_simple"):
    st.session_state["_audience"] = "simple"
    st.session_state["_scroll_guides"] = True
    st.rerun()
if _aq2.button("⚙️ Expert Console", use_container_width=True, key="_go_expert"):
    st.session_state["_audience"] = "expert"
    st.session_state["_scroll_guides"] = True
    st.rerun()
if _aq3.button("💼 Executive Brief", use_container_width=True, key="_go_exec"):
    st.session_state["_audience"] = "exec"
    st.session_state["_scroll_guides"] = True
    st.rerun()

# ─────────────────────────────────────────
# TABS — top-level navigation
# ─────────────────────────────────────────
_tab_home, _tab_sector, _tab_attacks, _tab_ransom, _tab_data, _tab_trends, _tab_ics = st.tabs([
    "🏠  Home",
    "📡  Sector Risk",
    "⚔️  Attack Methods",
    "🔓  Ransomware",
    "🗂️  Stolen Data",
    "📈  Trends",
    "🏭  ICS Threats",
])

# ── Sidebar nav → tab switcher + tooltip remover ─────────────────────────────
_nav_tab_idx = int(st.session_state.get("_nav_tab", 0))
components.html(f"""<script>
(function() {{
    var TARGET = {_nav_tab_idx};

    // Scroll to top then switch tab
    window.parent.scrollTo({{top: 0, behavior: 'instant'}});

    function clickTab() {{
        var tabs = window.parent.document.querySelectorAll(
            '[data-testid="stTabs"] [data-baseweb="tab-list"] button[role="tab"]'
        );
        if (tabs.length > TARGET) {{ tabs[TARGET].click(); }}
        window.parent.scrollTo({{top: 0, behavior: 'instant'}});
    }}
    setTimeout(clickTab, 150);

    // Remove native browser tooltip from sidebar collapse/expand buttons
    function removeTooltips() {{
        var btns = window.parent.document.querySelectorAll(
            '[data-testid="stSidebarCollapseButton"] button, [data-testid="collapsedControl"] button'
        );
        btns.forEach(function(b) {{
            b.removeAttribute('title');
            b.setAttribute('aria-label', '');
        }});
    }}
    setTimeout(removeTooltips, 300);
    setTimeout(removeTooltips, 800);
}})();
</script>""", height=0)

# HOME TAB — hero + welcome
# ─────────────────────────────────────────
with _tab_home:
    st.markdown(f"""
<div style="background:linear-gradient(135deg,#eff6ff 0%,#f8fafc 60%,#f0fdf4 100%);
            border:1px solid #e2e8f0;border-radius:16px;
            padding:2rem 2.4rem 1.6rem 2.4rem;margin-bottom:1.4rem;
            box-shadow:0 2px 12px rgba(37,99,235,0.07);">
  <p style="margin:0 0 0.3rem 0;font-size:0.75rem;font-weight:500;letter-spacing:0.04em;
            color:#2563eb;font-family:'Inter',sans-serif;">
    CyberSignals · Cyber Risk Intelligence Dashboard
  </p>
  <h1 style="margin:0 0 0.6rem 0;font-size:1.75rem;font-weight:600;color:#0f172a;
             font-family:'Inter',sans-serif;line-height:1.2;letter-spacing:-0.01em;">
    Understanding Today's Cyber Threat Landscape
  </h1>
  <p style="margin:0 0 1.4rem 0;font-size:0.93rem;color:#475569;font-family:'Inter',sans-serif;line-height:1.65;max-width:780px;">
    Two 2025 threat intelligence reports — DBIR and Kaspersky ICS-CERT — translated into clear visuals covering sector risk, attack methods, stolen data, and what to do about it.
  </p>
  <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:1.4rem;">
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:0.75rem 1.1rem;flex:1;min-width:140px;text-align:center;">
      <p style="margin:0;font-size:1.35rem;font-weight:600;color:#dc2626;font-family:'Inter',sans-serif;">22,052</p>
      <p style="margin:0;font-size:0.75rem;color:#64748b;font-family:'Inter',sans-serif;">Total incidents (DBIR)</p>
    </div>
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:0.75rem 1.1rem;flex:1;min-width:140px;text-align:center;">
      <p style="margin:0;font-size:1.35rem;font-weight:600;color:#2563eb;font-family:'Inter',sans-serif;">12,195</p>
      <p style="margin:0;font-size:0.75rem;color:#64748b;font-family:'Inter',sans-serif;">Confirmed breaches</p>
    </div>
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:0.75rem 1.1rem;flex:1;min-width:140px;text-align:center;">
      <p style="margin:0;font-size:1.35rem;font-weight:600;color:#d97706;font-family:'Inter',sans-serif;">44%</p>
      <p style="margin:0;font-size:0.75rem;color:#64748b;font-family:'Inter',sans-serif;">Breaches with ransomware</p>
    </div>
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:0.75rem 1.1rem;flex:1;min-width:140px;text-align:center;">
      <p style="margin:0;font-size:1.35rem;font-weight:600;color:#7c3aed;font-family:'Inter',sans-serif;">20.5%</p>
      <p style="margin:0;font-size:0.75rem;color:#64748b;font-family:'Inter',sans-serif;">ICS computers attacked (Q2 2025)</p>
    </div>
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;padding:0.75rem 1.1rem;flex:1;min-width:140px;text-align:center;">
      <p style="margin:0;font-size:1.35rem;font-weight:600;color:#059669;font-family:'Inter',sans-serif;">64%</p>
      <p style="margin:0;font-size:0.75rem;color:#64748b;font-family:'Inter',sans-serif;">Victims refusing to pay ransom</p>
    </div>
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:8px;">
    <span style="background:#eff6ff;border:1px solid #bfdbfe;color:#1d4ed8;padding:4px 12px;border-radius:20px;font-size:0.78rem;font-family:'Inter',sans-serif;font-weight:500;">📡 Sector Risk</span>
    <span style="background:#fef2f2;border:1px solid #fecaca;color:#b91c1c;padding:4px 12px;border-radius:20px;font-size:0.78rem;font-family:'Inter',sans-serif;font-weight:500;">⚔️ Attack Methods</span>
    <span style="background:#fff7ed;border:1px solid #fed7aa;color:#c2410c;padding:4px 12px;border-radius:20px;font-size:0.78rem;font-family:'Inter',sans-serif;font-weight:500;">🔓 Ransomware</span>
    <span style="background:#faf5ff;border:1px solid #e9d5ff;color:#7c3aed;padding:4px 12px;border-radius:20px;font-size:0.78rem;font-family:'Inter',sans-serif;font-weight:500;">🗂️ Stolen Data</span>
    <span style="background:#f0fdf4;border:1px solid #bbf7d0;color:#15803d;padding:4px 12px;border-radius:20px;font-size:0.78rem;font-family:'Inter',sans-serif;font-weight:500;">📈 Trends</span>
    <span style="background:#f5f3ff;border:1px solid #ddd6fe;color:#6d28d9;padding:4px 12px;border-radius:20px;font-size:0.78rem;font-family:'Inter',sans-serif;font-weight:500;">🏭 ICS Threats</span>
  </div>
  <p style="margin:1rem 0 0 0;font-size:0.75rem;color:#94a3b8;font-family:'Inter',sans-serif;">
    Sources: Verizon DBIR 2025 (Nov 2023 – Oct 2024) &nbsp;·&nbsp; Kaspersky ICS-CERT Q2 2025 &nbsp;·&nbsp; Team N5 · USI4280
  </p>
</div>
""", unsafe_allow_html=True)

# TIP OF THE MONTH
# ─────────────────────────────────────────
with _tab_home:
    with st.expander("💡  Tip of the Month", expanded=True):

        _TIPS = {
            1: {
                "month":   "January",
                "threat":  "Tax Season Phishing",
                "icon":    "🎯",
                "risk":    "HIGH",
                "risk_color": "#dc2626",
                "summary": (
                    "Attackers flood inboxes in January impersonating tax authorities (such as the Canada Revenue Agency "
                    "or the Internal Revenue Service) with fake refund notices, T4/W-2 requests, and \"account verification\" "
                    "links. Credential harvesting and identity theft are the primary goals."
                ),
                "prevention": [
                    "Go directly to your tax authority's official website — never click links in unsolicited emails.",
                    "Enable Multi-Factor Authentication on your tax filing and financial accounts.",
                    "File your return early to prevent fraudsters from filing in your name first.",
                    "Shred any physical tax documents before disposal.",
                ],
            },
            2: {
                "month":   "February",
                "threat":  "Romance Scams and Valentine's Day Phishing",
                "icon":    "💌",
                "risk":    "MEDIUM",
                "risk_color": "#d97706",
                "summary": (
                    "February sees a sharp spike in romance scams and brand-impersonation phishing using Valentine's Day "
                    "themes. Attackers create fake dating profiles to build trust over weeks before requesting money or "
                    "personal information. Phishing emails mimic florist, jewellery, and gift card brands."
                ),
                "prevention": [
                    "Reverse image-search profile photos on dating apps to detect stolen identities.",
                    "Never send money or gift cards to someone you have not met in person.",
                    "Hover over links before clicking — check the actual destination URL.",
                    "Report suspicious profiles to the platform immediately.",
                ],
            },
            3: {
                "month":   "March",
                "threat":  "Tax Deadline Phishing and Human Resources Scams",
                "icon":    "📋",
                "risk":    "HIGH",
                "risk_color": "#dc2626",
                "summary": (
                    "March marks peak tax filing season alongside a rise in Human Resources-themed phishing. Attackers "
                    "impersonate payroll teams requesting direct deposit changes, send fake T4 slips with malicious "
                    "attachments, and exploit employees distracted by year-end financial planning. Business Email "
                    "Compromise targeting finance teams also peaks."
                ),
                "prevention": [
                    "Verify any payroll or direct deposit change requests by calling the requester directly using a known number.",
                    "Never open unexpected tax document attachments — download statements only from official portals.",
                    "Train staff to recognize Business Email Compromise — urgent wire transfer requests are a red flag.",
                    "Check your credit report for unexpected accounts opened in your name.",
                ],
            },
            4: {
                "month":   "April",
                "threat":  "Tax Deadline Scams and Travel Booking Fraud",
                "icon":    "✈️",
                "risk":    "HIGH",
                "risk_color": "#dc2626",
                "summary": (
                    "Late tax filing deadlines drive a final wave of tax-themed phishing in April. Simultaneously, "
                    "spring break and early summer travel bookings attract fraudulent hotel, airline, and vacation "
                    "rental scams. Fake booking confirmation emails deliver malware or harvest credit card details."
                ),
                "prevention": [
                    "Book travel exclusively through official airline or hotel websites, not third-party links in emails.",
                    "Use a credit card (not debit) for travel bookings — it offers better fraud protection.",
                    "File your tax return on time to eliminate the window attackers use for late-filer fraud.",
                    "Enable travel alerts on your bank account before any trip.",
                ],
            },
            5: {
                "month":   "May",
                "threat":  "Benefits Enrolment Phishing and Job Offer Scams",
                "icon":    "📑",
                "risk":    "MEDIUM",
                "risk_color": "#d97706",
                "summary": (
                    "May coincides with mid-year benefits review periods and an influx of spring job postings. Attackers "
                    "send phishing emails impersonating Human Resources or benefits providers asking employees to \"re-verify\" "
                    "enrolment. Fraudulent job offers — particularly remote positions — are used to harvest personal "
                    "information or deliver malware via fake onboarding documents."
                ),
                "prevention": [
                    "Access benefits portals only by typing the address directly into your browser.",
                    "Verify job offers through the company's official careers page, not just the recruiter's email.",
                    "Never provide your Social Insurance or Social Security Number during early recruitment stages.",
                    "Report suspicious Human Resources emails to your IT or security team immediately.",
                ],
            },
            6: {
                "month":   "June",
                "threat":  "Credential Theft and Public Wi-Fi Attacks",
                "icon":    "📶",
                "risk":    "MEDIUM",
                "risk_color": "#d97706",
                "summary": (
                    "Summer travel season begins in June, increasing reliance on public Wi-Fi at airports, hotels, and "
                    "cafes. Attackers deploy \"evil twin\" rogue access points to intercept traffic and steal credentials. "
                    "Spam email rates also peak in June, with e-commerce fraud rising alongside summer shopping activity."
                ),
                "prevention": [
                    "Use a Virtual Private Network on all public Wi-Fi connections.",
                    "Avoid accessing banking or sensitive accounts over public networks.",
                    "Enable Multi-Factor Authentication so stolen passwords alone are not enough to access your accounts.",
                    "Verify the exact Wi-Fi network name with venue staff before connecting.",
                ],
            },
            7: {
                "month":   "July",
                "threat":  "Vacation-Themed Phishing and Out-of-Office Exploitation",
                "icon":    "🏖️",
                "risk":    "MEDIUM",
                "risk_color": "#d97706",
                "summary": (
                    "Attackers exploit reduced staffing and out-of-office replies in July to launch Business Email "
                    "Compromise attacks, knowing approvals may be rushed or delegated to less experienced staff. "
                    "Travel phishing peaks with fake airline refund notices, accommodation scams, and fraudulent "
                    "luggage claim links."
                ),
                "prevention": [
                    "Avoid including too many details in out-of-office replies — do not reveal your exact return date or backup contact's email.",
                    "Set up approval workflows that require two people for financial transactions over a set threshold.",
                    "Brief any colleagues covering your role on how to spot social engineering attempts.",
                    "Monitor your accounts more frequently when travelling.",
                ],
            },
            8: {
                "month":   "August",
                "threat":  "Back-to-School Scams and Educational Malware",
                "icon":    "🎒",
                "risk":    "MEDIUM",
                "risk_color": "#d97706",
                "summary": (
                    "August sees a surge in scams targeting parents and students — fake school supply deals, fraudulent "
                    "scholarship offers, and malicious educational apps. Universities face increased credential phishing "
                    "as students log in to new systems. Attackers also distribute malware disguised as textbook PDF "
                    "downloads."
                ),
                "prevention": [
                    "Download educational apps only from official app stores and verify publisher names carefully.",
                    "Obtain textbooks through your institution's library or verified legal sources.",
                    "Students: use your institution's official email and Multi-Factor Authentication from day one.",
                    "Parents: set up parental controls and educate children about phishing before the school year begins.",
                ],
            },
            9: {
                "month":   "September",
                "threat":  "Mobile Malware and One-Time Password Stealers",
                "icon":    "📱",
                "risk":    "HIGH",
                "risk_color": "#dc2626",
                "summary": (
                    "September marks the beginning of a surge in mobile malware — particularly Android trojans designed "
                    "to intercept one-time passwords and bypass Multi-Factor Authentication. Fraudsters begin preparing "
                    "infrastructure for the upcoming holiday shopping season, and SIM-swapping attacks targeting "
                    "high-value individuals increase."
                ),
                "prevention": [
                    "Use an authenticator app (not SMS) for Multi-Factor Authentication wherever possible.",
                    "Contact your mobile carrier to add a port freeze or account PIN to prevent SIM swapping.",
                    "Keep your phone operating system and all apps fully updated.",
                    "Only install apps from official stores and review permissions before granting access.",
                ],
            },
            10: {
                "month":   "October",
                "threat":  "Ransomware Campaigns and Credential Stuffing",
                "icon":    "🔐",
                "risk":    "CRITICAL",
                "risk_color": "#991b1b",
                "summary": (
                    "October is Cybersecurity Awareness Month — but also one of the highest-risk months for ransomware. "
                    "Threat actors ramp up campaigns ahead of the holiday season knowing organizations are distracted. "
                    "Credential stuffing attacks spike as attackers test leaked username-password pairs against streaming, "
                    "retail, and banking sites ahead of Black Friday."
                ),
                "prevention": [
                    "Test and verify your backup restoration process — ransomware is only defeated if backups actually work.",
                    "Use unique passwords for every account; a password manager makes this practical.",
                    "Run a tabletop ransomware incident response exercise with your team this month.",
                    "Patch all internet-facing systems — ransomware actors actively scan for unpatched vulnerabilities.",
                ],
            },
            11: {
                "month":   "November",
                "threat":  "Black Friday and Cyber Monday Shopping Fraud",
                "icon":    "🛒",
                "risk":    "CRITICAL",
                "risk_color": "#991b1b",
                "summary": (
                    "Gift card fraud spikes up to 300% in November. Fake retailer websites, lookalike brand emails, "
                    "and malicious browser extensions designed to steal payment card data all peak around Black Friday "
                    "and Cyber Monday. Ransomware groups deliberately time attacks to hit retailers when their security "
                    "teams are stretched thin and revenue impact is highest."
                ),
                "prevention": [
                    "Shop only on retailer websites you navigate to directly — not links from emails or social media ads.",
                    "Check the website address bar carefully for subtle misspellings (e.g., amaz0n.com).",
                    "Use a virtual or single-use credit card number for online purchases.",
                    "Watch for unsolicited gift card requests — a common scam targeting both individuals and businesses.",
                ],
            },
            12: {
                "month":   "December",
                "threat":  "Holiday Ransomware, Charity Fraud and Phishing (Peak Month)",
                "icon":    "🎄",
                "risk":    "CRITICAL",
                "risk_color": "#991b1b",
                "summary": (
                    "December is consistently the most dangerous month of the year for cyber attacks. Ransomware "
                    "attacks hit their annual peak — a 30% surge above the monthly average — as attackers know "
                    "IT teams are on leave and organizations are reluctant to disrupt operations during the holiday "
                    "period. Charity donation scams, fake shipping notifications, and e-gift fraud also peak sharply."
                ),
                "prevention": [
                    "Ensure at least one security team member is on call throughout the holiday break.",
                    "Donate to charities only through their official websites — search directly, do not click donation links.",
                    "Verify shipping notification emails against your actual order confirmation before clicking any links.",
                    "Set up transaction alerts on all financial accounts so you are notified of any unusual activity instantly.",
                ],
            },
        }

        _now   = datetime.datetime.now()
        _month = _now.month
        _tip   = _TIPS[_month]

        # Build prevention list HTML outside the f-string (backslashes not allowed inside f-string expressions)
        _tip_prevention_html = "".join(
            '<p style="margin:0.35rem 0 0 0;font-size:0.875rem;color:#334155;'
            'font-family:\'Inter\',sans-serif;line-height:1.55;">&#10004;&nbsp;' + t + '</p>'
            for t in _tip["prevention"]
        )

        st.markdown("## 💡 Tip of the Month")
        st.markdown(
    f"""
<div style="
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 6px solid {_tip['risk_color']};
    border-radius: 12px;
    padding: 1.4rem 1.6rem 1.2rem 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
">
  <!-- header row -->
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:0.9rem;">
    <div style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:2rem;line-height:1;">{_tip['icon']}</span>
      <div>
        <p style="margin:0;font-size:0.72rem;font-weight:400;letter-spacing:0.04em;
                  color:#64748b;font-family:'Inter',sans-serif;">
          Threat Focus · {_tip['month']} {_now.year}
        </p>
        <p style="margin:0;font-size:1rem;font-weight:600;color:#0f172a;font-family:'Inter',sans-serif;line-height:1.25;">
          {_tip['threat']}
        </p>
      </div>
    </div>
    <span style="
        padding:4px 14px;border-radius:20px;font-size:0.72rem;font-weight:500;
        letter-spacing:0.03em;font-family:'Inter',sans-serif;
        background:{_tip['risk_color']};color:#ffffff;">
      {_tip['risk']} RISK
    </span>
  </div>

  <!-- body -->
  <p style="margin:0 0 1rem 0;font-size:0.9rem;line-height:1.7;color:#334155;
            font-family:'Inter',sans-serif;">
    {_tip['summary']}
  </p>

  <!-- prevention list -->
  <div style="background:#f1f5f9;border-radius:8px;padding:0.9rem 1.1rem;border:1px solid #e2e8f0;">
    <p style="margin:0 0 0.5rem 0;font-size:0.78rem;font-weight:500;letter-spacing:0;
              color:#2563eb;font-family:'Inter',sans-serif;">
      🛡️ How to Protect Yourself
    </p>
    {_tip_prevention_html}
  </div>

  <!-- footer note -->
  <p style="margin:0.8rem 0 0 0;font-size:0.72rem;color:#94a3b8;
            font-family:'Inter',sans-serif;text-align:right;">
    This tip updates automatically each month &nbsp;·&nbsp; Based on seasonal threat intelligence research
  </p>
</div>
        """,
            unsafe_allow_html=True,
        )

        # ─────────────────────────────────────────
# KPI ROW
# ─────────────────────────────────────────
with _tab_home:
    with st.expander("📊  Key Risk Metrics", expanded=True):

        st.markdown("## Key Risk Metrics")
        st.caption("Each percentage is an independent risk factor — a single breach can involve ransomware, a vulnerability, and a third party at the same time, which is why the figures do not total 100%.")
        m1,m2,m3,m4,m5 = st.columns(5)
        m1.metric("Total Incidents Reported",  "22,052",  "Nov 2023 – Oct 2024")
        m2.metric("Confirmed Data Breaches",   "12,195",  "55% of all incidents")
        m3.metric("Breaches Involved Ransomware", "44%",  "↑37% Year-over-Year",  delta_color="inverse")
        m4.metric("Breaches via Vulnerability",   "20%",  "↑34% Year-over-Year",  delta_color="inverse")
        m5.metric("Breaches via Third Party",     "30%",  "↑100% Year-over-Year", delta_color="inverse")

        # ─────────────────────────────────────────
# SECTION 1 — RADAR + INCIDENT PRESSURE
# ─────────────────────────────────────────
with _tab_sector:
    with st.expander("📡  Sector Risk Analysis", expanded=True):

        st.markdown("## Which Sectors Are Most at Risk?")
        filtered = df_industry[df_industry["Industry"].isin(selected_sectors)]
        if selected_sectors and filtered.empty:
            st.warning("No sectors selected – showing all sectors instead.")

        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("### Breach Exposure by Sector")
            st.caption("Each spoke shows how hard a sector was hit — normalized across 12,195 confirmed breaches")
            st.markdown(audience_badge("exec"), unsafe_allow_html=True)
            df_radar_plot = filtered if not filtered.empty else df_industry
            radar_sectors_plot  = df_radar_plot["Industry"].tolist()
            radar_breaches_plot = df_radar_plot["Breaches"].tolist()
            radar_norm_plot = [round(b / max(radar_breaches_plot) * 10, 1) if radar_breaches_plot else 0
                               for b in radar_breaches_plot]

            # Risk zone background rings (Low / Medium / High)
            _all_theta = radar_sectors_plot + ([radar_sectors_plot[0]] if radar_sectors_plot else [])
            for zone_r, zone_fill, zone_name in [
                ([3]*len(_all_theta),  "rgba(22,163,74,0.07)",   "Low Risk (score 1–3)"),
                ([6]*len(_all_theta),  "rgba(234,88,12,0.07)",   "Medium Risk (score 4–6)"),
                ([10]*len(_all_theta), "rgba(220,38,38,0.07)",   "High Risk (score 7–10)"),
            ]:
                pass  # drawn as filled rings below

            fig_radar = go.Figure()

            # Background zone: High (red) — outermost
            fig_radar.add_trace(go.Scatterpolar(
                r=[10]*len(_all_theta), theta=_all_theta,
                fill="toself", fillcolor="rgba(220,38,38,0.06)",
                line=dict(color="rgba(220,38,38,0.15)", width=1),
                name="High Risk (7–10)", showlegend=True, hoverinfo="skip",
            ))
            # Background zone: Medium (orange)
            fig_radar.add_trace(go.Scatterpolar(
                r=[6]*len(_all_theta), theta=_all_theta,
                fill="toself", fillcolor="rgba(234,88,12,0.08)",
                line=dict(color="rgba(234,88,12,0.2)", width=1),
                name="Medium Risk (4–6)", showlegend=True, hoverinfo="skip",
            ))
            # Background zone: Low (green) — innermost
            fig_radar.add_trace(go.Scatterpolar(
                r=[3]*len(_all_theta), theta=_all_theta,
                fill="toself", fillcolor="rgba(22,163,74,0.10)",
                line=dict(color="rgba(22,163,74,0.25)", width=1),
                name="Low Risk (1–3)", showlegend=True, hoverinfo="skip",
            ))

            # Actual risk data
            _hover_breaches = df_radar_plot["Breaches"].tolist() + ([df_radar_plot["Breaches"].tolist()[0]] if df_radar_plot["Breaches"].tolist() else [])
            fig_radar.add_trace(go.Scatterpolar(
                r=radar_norm_plot + ([radar_norm_plot[0]] if radar_norm_plot else []),
                theta=_all_theta,
                fill="toself",
                fillcolor="rgba(220,38,38,0.18)",
                line=dict(color=RED, width=3),
                name="Sector Risk Score",
                customdata=_hover_breaches,
                hovertemplate="<b>%{theta}</b><br>Risk Score: %{r}/10<br>Confirmed Breaches: %{customdata:,}<extra></extra>",
            ))

            layout_radar = chart_layout(height=460, show_legend=True)
            layout_radar.update({
                "legend": dict(
                    orientation="v", x=1.02, y=1, xanchor="left", yanchor="top",
                    font=dict(size=10, color=MUTED, family="Inter, sans-serif"),
                    bgcolor="rgba(248,250,252,0.95)", bordercolor=BORDER2, borderwidth=1,
                ),
                "margin": dict(l=40, r=140, t=36, b=40),
                "polar": dict(
                    bgcolor="white",
                    radialaxis=dict(visible=True, range=[0,10],
                                    tickfont=dict(size=9, color=MUTED),
                                    tickvals=[3,6,10],
                                    ticktext=["3 — Low","6 — Med","10 — High"],
                                    gridcolor=BORDER, linecolor=BORDER2),
                    angularaxis=dict(tickfont=dict(size=11, color=TEXT),
                                     gridcolor=BORDER, linecolor=BORDER2),
                ),
            })
            fig_radar.update_layout(**layout_radar)
            st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_radar = "22,052 incidents · 12,195 confirmed breaches"
            _hl_radar  = "Why does Manufacturing score so high?"
            _bd_radar  = ("Manufacturing topped confirmed breaches in 2025 for the first time. Ransomware groups deliberately "
                          "target industrial operations because any production downtime creates immediate financial pressure to pay. "
                          "Healthcare follows closely — patient records fetch 10× the price of credit card data on criminal "
                          "markets, making hospitals a permanent high-value target.")
            _ext_radar = ("The score on each spoke is normalised: the sector with the most confirmed breaches scores 10, and all "
                          "others are scaled proportionally. This means the chart shows <em>relative risk</em> — not absolute "
                          "counts. Finance appears lower not because it is safe, but because it has fewer confirmed breaches "
                          "relative to Manufacturing and Healthcare. Finance actually leads in total incidents — it is simply "
                          "better at stopping attacks before data is compromised. The radar shape gives an at-a-glance view of "
                          "which sectors are the most vulnerable overall: a large, jagged shape signals broad systemic risk; "
                          "a narrow shape suggests risk is concentrated in only a few sectors.")
            st.markdown(source_badge(_src_radar), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_radar, _bd_radar), unsafe_allow_html=True)
            open_analysis_btn("radar", fig_radar, "Breach Exposure by Sector",
                              _src_radar, _hl_radar, _bd_radar, _ext_radar)

        with col2:
            st.markdown("### Incidents vs Confirmed Breaches")
            st.caption("Not every incident becomes a breach — this shows which sectors cross that line most often")
            st.markdown(audience_badge("exec"), unsafe_allow_html=True)
            df_plot = filtered if not filtered.empty else df_industry
            fig_pressure = go.Figure()
            fig_pressure.add_trace(go.Bar(
                y=df_plot["Industry"], x=df_plot["Incidents"],
                name="Incidents", orientation="h",
                marker=dict(color=C_BLUE, opacity=0.75, line=dict(color="white", width=0.5)),
                text=df_plot["Incidents"], textposition="outside",
                textfont=dict(size=10, color=TEXT, family="Inter, sans-serif"),
            ))
            fig_pressure.add_trace(go.Bar(
                y=df_plot["Industry"], x=df_plot["Breaches"],
                name="Confirmed Breaches", orientation="h",
                marker=dict(color=C_RED, opacity=0.88, line=dict(color="white", width=0.5)),
                text=df_plot["Breaches"], textposition="outside",
                textfont=dict(size=10, color=TEXT, family="Inter, sans-serif"),
            ))
            layout = chart_layout(height=440)
            layout.update({
                "barmode": "group",
                "bargap": 0.18,
                "yaxis": dict(automargin=True, tickfont=dict(color=TEXT, size=11), gridcolor="#f1f5f9"),
                "xaxis": dict(title="Count", gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11)),
                "legend": dict(orientation="h", y=-0.14, font=dict(size=11, color=TEXT)),
            })
            fig_pressure.update_layout(**layout)
            st.plotly_chart(fig_pressure, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_pres = "15 industries · Nov 2023 – Oct 2024"
            _hl_pres  = "Incident ≠ breach — the gap matters"
            _bd_pres  = ("A large gap between the blue and red bars means a sector detects and stops attacks before data is "
                         "compromised. Finance has many incidents but strong containment. Manufacturing and Healthcare show "
                         "the smallest gaps — nearly every incident they experience ends in a confirmed breach, signalling "
                         "weaker response capabilities or harder-to-patch systems.")
            _ext_pres = ("The blue bar (incidents) represents every event flagged as a potential attack. The red bar (confirmed "
                         "breaches) represents only those where data was actually stolen or exposed. A sector with a large blue "
                         "bar but small red bar — like Finance — has strong detection and containment: attackers get in but "
                         "rarely get out with data. A sector where both bars are nearly equal — like Manufacturing — is "
                         "struggling to stop attacks once they begin. This is partly because industrial control systems run "
                         "legacy software that cannot be easily patched, and Operational Technology environments were never "
                         "designed with network segmentation in mind. The Retail sector's gap is also narrow: point-of-sale "
                         "attacks are quick, automated, and hard to detect before cards are already exfiltrated.")
            st.markdown(source_badge(_src_pres), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_pres, _bd_pres), unsafe_allow_html=True)
            open_analysis_btn("incidents_breaches", fig_pressure, "Incidents vs Confirmed Breaches",
                              _src_pres, _hl_pres, _bd_pres, _ext_pres)

        # ─────────────────────────────────────────
        # SECTION 2 — FORECAST OUTLOOK
        # ─────────────────────────────────────────
        _, col_fore, _ = st.columns([1, 2, 1], gap="large")

        with col_fore:
            st.markdown("### Ransomware Is Rising — But More Victims Are Fighting Back")
            st.caption("Two stories in three years: ransomware doubled in breaches, yet refusal to pay jumped from 50% to 64%")
            st.markdown(audience_badge("exec"), unsafe_allow_html=True)

            fig_fore = go.Figure()

            # Red bars — ransomware involvement
            fig_fore.add_trace(go.Bar(
                x=df_ransom["Year"], y=df_ransom["In Breaches (%)"],
                name="Ransomware involved in breach",
                marker=dict(color=C_RED, opacity=0.88, line=dict(color="white", width=1.5)),
                text=[f"{v}%" for v in df_ransom["In Breaches (%)"]],
                textposition="outside",
                textfont=dict(size=13, color=RED, family="Inter, sans-serif"),
                hovertemplate="<b>%{x}</b><br>Ransomware in breaches: <b>%{y}%</b><extra></extra>",
            ))

            # Green bars — refusal to pay
            fig_fore.add_trace(go.Bar(
                x=df_ransom["Year"], y=df_ransom["Refused to Pay (%)"],
                name="Victims who refused to pay the ransom",
                marker=dict(color=C_GREEN, opacity=0.82, line=dict(color="white", width=1.5)),
                text=[f"{v}%" for v in df_ransom["Refused to Pay (%)"]],
                textposition="outside",
                textfont=dict(size=13, color=GREEN, family="Inter, sans-serif"),
                hovertemplate="<b>%{x}</b><br>Victims who refused to pay: <b>%{y}%</b><extra></extra>",
            ))

            # Annotation — top-left corner, no arrow, clear of all bars
            fig_fore.add_annotation(
                x=0, y=78,
                xref="x", yref="y",
                text="🔺 Ransomware nearly doubled<br>from 2022 to 2024",
                showarrow=False,
                xanchor="center",
                font=dict(size=11, color=RED, family="Inter, sans-serif"),
                bgcolor="rgba(255,240,240,0.95)", bordercolor=C_RED, borderwidth=1, borderpad=6,
            )

            layout = chart_layout(height=440)
            layout.update({
                "barmode": "group",
                "bargap": 0.35,
                "yaxis": dict(
                    title="Percentage of Breaches (%)",
                    range=[0, 88],
                    gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11),
                    ticksuffix="%",
                ),
                "xaxis": dict(
                    title="Reporting Year",
                    tickfont=dict(color=TEXT, size=14, family="Inter, sans-serif"),
                    type="category",
                ),
                "legend": dict(orientation="h", y=-0.22, font=dict(size=11, color=TEXT)),
            })
            fig_fore.update_layout(**layout)
            st.plotly_chart(fig_fore, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_fore = "Ransomware trajectory 2022–2024"
            _hl_fore  = "More ransomware, but victims are fighting back"
            _bd_fore  = ("Ransomware's share of breaches has nearly doubled in three years — from 1 in 4 breaches in 2022 "
                         "to nearly 1 in 2 by 2024. However, the rising refusal-to-pay rate (now 64%) shows organizations "
                         "are learning: paying rarely guarantees full data recovery and often funds the next attack. The DBIR "
                         "notes that median ransom demands grew to $115,000 in 2024, making prevention far cheaper than recovery.")
            _ext_fore = ("The refusal-to-pay trend is significant for the entire ecosystem. When victims pay, they validate "
                         "the business model and fund the next wave of attacks. Law enforcement agencies in Canada, the United "
                         "States, and the United Kingdom now actively discourage payment and in some jurisdictions are exploring "
                         "legislation to prohibit it entirely for critical infrastructure. The 64% refusal rate in 2024 "
                         "suggests that cyber insurance policies — which historically covered ransom payments — are also "
                         "tightening, and that offline backup strategies are becoming more common. The key defensive takeaway: "
                         "a tested offline backup that is isolated from the network renders ransomware economically ineffective. "
                         "Attackers know this, which is why 'double extortion' (stealing data before encrypting it) has "
                         "become the dominant tactic — the threat to publish is a second lever of pressure even when "
                         "backups exist.")
            st.markdown(source_badge(_src_fore), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_fore, _bd_fore), unsafe_allow_html=True)
            open_analysis_btn("ransomware_forecast", fig_fore, "Ransomware Is Rising — But More Victims Are Fighting Back",
                              _src_fore, _hl_fore, _bd_fore, _ext_fore)

        # ─────────────────────────────────────────
# SECTION 3 — THREAT TYPE TRENDS
# ─────────────────────────────────────────
with _tab_attacks:
    with st.expander("⚔️  How Attacks Happen", expanded=True):

        st.markdown("## How Attacks Happen")
        st.caption("The most common attack patterns — and how many of those incidents turn into real breaches")

        col5, col6 = st.columns([3,2], gap="large")

        with col5:
            st.markdown("#### Most Common Attack Patterns")
            st.markdown(audience_badge("expert"), unsafe_allow_html=True)
            fig_pat = go.Figure()
            fig_pat.add_trace(go.Bar(
                y=df_patterns["Pattern"], x=df_patterns["Incidents"],
                name="Incidents",
                orientation="h",
                marker=dict(color=C_BLUE, opacity=0.80, line=dict(color="white", width=0.5)),
                text=[f"{v:,}" for v in df_patterns["Incidents"]],
                textposition="outside",
                cliponaxis=False,
                textfont=dict(size=10, color=TEXT, family="Inter, sans-serif"),
                hovertemplate="<b>%{y}</b><br>Incidents: <b>%{x:,}</b><extra></extra>",
            ))
            fig_pat.add_trace(go.Bar(
                y=df_patterns["Pattern"], x=df_patterns["Breaches"],
                name="Confirmed Breaches",
                orientation="h",
                marker=dict(color=C_RED, opacity=0.88, line=dict(color="white", width=0.5)),
                text=[f"{v:,}" for v in df_patterns["Breaches"]],
                textposition="outside",
                cliponaxis=False,
                textfont=dict(size=10, color=TEXT, family="Inter, sans-serif"),
                hovertemplate="<b>%{y}</b><br>Confirmed Breaches: <b>%{x:,}</b><extra></extra>",
            ))
            # Callout annotation for the near-invisible "2 breaches" bar (Denial of Service)
            fig_pat.add_annotation(
                y="Denial of Service", x=400,
                text="★ Only 2 confirmed breaches",
                showarrow=True, arrowhead=2, arrowcolor=C_RED, arrowwidth=1.5,
                ax=160, ay=-40,
                font=dict(size=10, color=RED, family="Inter, sans-serif"),
                bgcolor="rgba(255,240,240,0.95)", bordercolor=C_RED, borderwidth=1, borderpad=5,
                xanchor="left",
            )
            layout = chart_layout(height=420)
            layout.update({
                "barmode": "group",
                "bargap": 0.2,
                "xaxis": dict(
                    title="Number of Reported Cases",
                    gridcolor="#f1f5f9",
                    tickfont=dict(color=MUTED, size=11),
                    tickformat=",",
                    automargin=True,
                ),
                "yaxis": dict(
                    tickfont=dict(color=TEXT, size=11),
                    automargin=True,
                    gridcolor="#f1f5f9",
                ),
                "legend": dict(orientation="h", y=-0.16, font=dict(size=11, color=TEXT)),
                "margin": dict(l=56, r=140, t=36, b=56),
            })
            fig_pat.update_layout(**layout)
            st.plotly_chart(fig_pat, use_container_width=True,
                            config={"displayModeBar": True, "displaylogo": False,
                                    "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_pat = "7 VERIS (Vocabulary for Event Recording and Incident Sharing) incident classification patterns"
            _hl_pat  = "Why does Denial of Service have 6,520 incidents but only 2 breaches?"
            _bd_pat  = ("This is not a data error — it reflects how a breach is defined. The DBIR counts a breach only when "
                        "data confidentiality is violated (something is stolen or exposed). Denial of Service and Distributed "
                        "Denial of Service attacks disrupt <em>availability</em> — they knock systems offline — but they do "
                        "not steal data. Because nothing is taken, they almost never qualify as breaches. System Intrusion "
                        "sits at the opposite extreme: it is purpose-built for exfiltration, converting almost every incident "
                        "into a confirmed breach.")
            _ext_pat = ("System Intrusion is the dominant breach pattern because it is deliberately designed for data theft — "
                        "attackers maintain persistent access, move laterally, and exfiltrate quietly. Social Engineering "
                        "(phishing, pretexting, business email compromise) converts at a high rate too because humans remain "
                        "the most consistent vulnerability across all industries. Privilege Misuse breaches are particularly "
                        "damaging — they are almost always insider threats, meaning the attacker already has legitimate access "
                        "and can bypass many perimeter controls entirely. Miscellaneous Errors (accidental data exposures, "
                        "misconfigurations) converting at near 100% is a reminder that not all breaches are malicious — "
                        "a misconfigured cloud storage bucket can expose millions of records with no attacker involved.")
            st.markdown(source_badge(_src_pat), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_pat, _bd_pat), unsafe_allow_html=True)
            open_analysis_btn("attack_patterns", fig_pat, "Most Common Attack Patterns",
                              _src_pat, _hl_pat, _bd_pat, _ext_pat)

        with col6:
            st.markdown("#### How Attackers Get In")
            st.markdown(audience_badge("expert"), unsafe_allow_html=True)
            fig_pie = go.Figure(go.Pie(
                labels=df_access["Vector"], values=df_access["Pct"], hole=0.50,
                marker=dict(colors=[C_AMBER, C_RED, C_BLUE, C_PURP], line=dict(color="white", width=3)),
                textinfo="percent",
                textposition="inside",
                textfont=dict(size=13, color="white", family="Inter, sans-serif"),
                pull=[0.05, 0.05, 0.03, 0.05],
                showlegend=True,
            ))
            layout_pie = chart_layout(height=430, show_legend=True, legend_y=-0.18)
            layout_pie.update({
                "legend": dict(orientation="h", y=-0.18,
                               font=dict(size=12, color=TEXT, family="Inter, sans-serif"),
                               bgcolor="rgba(0,0,0,0)"),
                "annotations": [dict(text="How they<br>get in", x=0.5, y=0.5,
                                     font=dict(size=12, color=MUTED, family="Inter, sans-serif"),
                                     showarrow=False)],
                "margin": dict(l=24, r=24, t=36, b=80),
            })
            fig_pie.update_layout(**layout_pie)
            st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_pie = "Top initial access vectors in confirmed breaches"
            _hl_pie  = "Edge devices and Virtual Private Networks now tied with stolen credentials"
            _bd_pie  = ("Credential theft has led initial access for years, but Edge Device and Virtual Private Network "
                        "exploitation jumped 34% year over year to draw level. Attackers now scan for unpatched firewalls "
                        "and Virtual Private Network appliances — no phishing email needed, just a known vulnerability and "
                        "an exposed IP address. Organizations with long patch cycles are particularly exposed, especially "
                        "if they use End-of-Life network appliances.")
            _ext_pie = ("Each slice represents a different attack philosophy. Stolen credentials require the least technical "
                        "skill — credentials are bought cheaply on criminal marketplaces and tried at scale (credential "
                        "stuffing). Vulnerability exploitation is increasingly automated; scanning tools identify exposed "
                        "appliances within minutes of a patch being published, and many organizations take weeks to apply "
                        "updates. Phishing remains reliable because it targets human judgement, not technical controls — "
                        "even security-aware employees can be deceived under time pressure or with convincing pretexts. "
                        "The near-equal split across all four vectors is a warning: defenders cannot afford to fix only "
                        "one entry point. A multi-layered strategy — strong credential hygiene, rapid patching, phishing "
                        "simulation, and network segmentation — is required to meaningfully reduce initial access risk.")
            st.markdown(source_badge(_src_pie), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_pie, _bd_pie), unsafe_allow_html=True)
            open_analysis_btn("initial_access", fig_pie, "How Attackers Get In",
                              _src_pie, _hl_pie, _bd_pie, _ext_pie)

        # ─────────────────────────────────────────
# SECTION 4 — RANSOMWARE + THREAT ACTORS
# ─────────────────────────────────────────
with _tab_ransom:
    with st.expander("🔓  Ransomware and Threat Actors", expanded=True):

        st.markdown("## Ransomware & Who Is Behind Attacks")
        col7, col8 = st.columns(2, gap="large")

        with col7:
            st.markdown("#### Ransomware Involvement Rate by Industry Sector")
            st.caption("Percentage of breaches in each sector that involved ransomware — each sector shown in its own distinct colour")
            st.markdown(audience_badge("exec"), unsafe_allow_html=True)
            bar_colors = ["#3b82f6","#10b981","#f59e0b","#8b5cf6","#ef4444","#06b6d4","#f97316"]
            fig_rs = go.Figure(go.Bar(
                y=df_ransom_sector["Sector"], x=df_ransom_sector["Ransomware (%)"],
                orientation="h",
                marker=dict(color=bar_colors, opacity=0.88, line=dict(color="white", width=0.5)),
                text=[f"{v}%" for v in df_ransom_sector["Ransomware (%)"]],
                textposition="outside", textfont=dict(size=11, color=TEXT, family="Inter, sans-serif"),
            ))
            fig_rs.add_vline(x=44, line_dash="dash", line_color=ACCENT, line_width=2,
                             annotation_text="Global avg: 44%",
                             annotation_font=dict(color=BG, size=11, family="Inter, sans-serif"),
                             annotation_bgcolor=ACCENT,
                             annotation_bordercolor=ACCENT,
                             annotation_borderpad=5,
                             annotation_position="bottom right")
            layout = chart_layout(height=400, show_legend=False)
            layout.update({
                "xaxis": dict(title="% of Breaches with Ransomware", range=[0,105],
                              gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11), automargin=True),
                "yaxis": dict(tickfont=dict(color=TEXT, size=11), automargin=True, gridcolor="#f1f5f9"),
            })
            fig_rs.update_layout(**layout)
            st.plotly_chart(fig_rs, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_rs = "Ransomware involvement across sectors"
            _hl_rs  = "Why does Manufacturing rank so high — and Finance so low?"
            _bd_rs  = ("Manufacturing plants are difficult to patch because taking Operational Technology systems offline "
                       "halts production, giving attackers leverage and operators little choice but to pay. Education "
                       "institutions store sensitive student records but often run outdated infrastructure with limited "
                       "security budgets. Finance, by contrast, invests heavily in network segmentation and offline backups "
                       "— making ransomware far less effective even when attackers gain initial access. Public "
                       "Administration's lower rate partly reflects government policies that restrict ransom payments.")
            _ext_rs = ("The global average of 44% means nearly one in two breaches now involves ransomware. Sectors above "
                       "this line face elevated risk and should prioritize offline backup testing, network segmentation, "
                       "and incident response planning. Sectors below the line are not immune — Finance's 18% still "
                       "represents hundreds of incidents globally. The colour coding (green/orange/red) reflects deviation "
                       "from that 44% average. The most actionable insight: if your organization is in Education or "
                       "Manufacturing, ransomware is statistically more likely than not to be involved in any breach you "
                       "experience. Offline, tested backups and a rehearsed response plan are the two highest-return "
                       "investments available.")
            st.markdown(source_badge(_src_rs), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_rs, _bd_rs), unsafe_allow_html=True)
            open_analysis_btn("ransom_sector", fig_rs, "Ransomware Involvement Rate by Industry Sector",
                              _src_rs, _hl_rs, _bd_rs, _ext_rs)

        with col8:
            st.markdown("#### Who Is Behind the Attacks?")
            st.caption("External actors rose 163% in espionage-driven breaches — the most significant shift reported in 2025")
            st.markdown(audience_badge("expert"), unsafe_allow_html=True)
            actor_labels = ["External","Internal","Partner/3rd-party","State-sponsored"]
            actor_vals   = [80,20,30,15]
            actor_colors = [C_RED, C_AMBER, C_PURP, "#6b7280"]
            fig_act = go.Figure(go.Bar(
                x=actor_labels, y=actor_vals,
                marker=dict(color=actor_colors, opacity=0.88, line=dict(color="white", width=0.5)),
                text=[f"{v}%" for v in actor_vals],
                textposition="outside", textfont=dict(size=12, color=TEXT, family="Inter, sans-serif"),
                width=0.55,
            ))
            fig_act.add_annotation(
                x="External", y=85, text="163% rise in espionage",
                showarrow=False, font=dict(color=RED, size=11, family="Inter, sans-serif"),
                bgcolor="rgba(255,255,255,0.95)", bordercolor=BORDER2, borderwidth=1, borderpad=4,
            )
            layout = chart_layout(height=400, show_legend=False)
            layout.update({
                "yaxis": dict(title="Prevalence in Breaches (%)", range=[0,105],
                              gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11)),
                "xaxis": dict(tickfont=dict(color=TEXT, size=12), gridcolor="#f1f5f9"),
            })
            fig_act.update_layout(**layout)
            st.plotly_chart(fig_act, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_act = "Threat actor categories across all breaches"
            _hl_act  = "The 163% spike in espionage is the report's starkest shift"
            _bd_act  = ("Nation-state actors — primarily linked to Russia, China, Iran and North Korea — dramatically "
                        "increased targeting of intellectual property and critical infrastructure in 2024. The boundary "
                        "between organized crime and state-sponsored hacking is blurring: some groups operate freely in "
                        "exchange for intelligence-sharing with their governments. For organizations, this means attacks "
                        "are better-resourced, more patient, and harder to detect than purely financial attacks.")
            _ext_act = ("External actors dominate breaches because they have the greatest motivation, resources, and "
                        "scale. However, the 20% internal figure is deceptively significant — insider threats cause "
                        "disproportionate damage because insiders already have authorized access and can bypass perimeter "
                        "controls entirely. Malicious insiders are often motivated by financial gain (selling data to "
                        "competitors or criminal groups) or grievance. Partner and third-party breaches are the fastest-"
                        "growing category: supply chain compromises give attackers access to dozens of organizations "
                        "through a single point of entry — one compromised vendor credential can open doors across an "
                        "entire partner ecosystem. State-sponsored actors at 15% are often the hardest to detect and "
                        "remove — they operate with long time horizons, prioritize stealth over speed, and are backed "
                        "by substantial intelligence resources.")
            st.markdown(source_badge(_src_act), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_act, _bd_act), unsafe_allow_html=True)
            open_analysis_btn("threat_actors", fig_act, "Who Is Behind the Attacks?",
                              _src_act, _hl_act, _bd_act, _ext_act)

        # ─────────────────────────────────────────
# SECTION 5 — DATA TYPES + MFA BYPASS
# ─────────────────────────────────────────
with _tab_data:
    with st.expander("🗂️  Stolen Data and Security Controls", expanded=True):

        st.markdown("## What Gets Stolen and How Attackers Bypass Security Controls")
        col9, col10 = st.columns(2, gap="large")

        with col9:
            st.markdown("#### Most Commonly Stolen Data")
            st.caption("Ranked by how often each data type appears in confirmed breach incidents — each data type shown in its own distinct colour")
            st.markdown(audience_badge("simple"), unsafe_allow_html=True)
            data_colors = ["#6366f1","#ec4899","#14b8a6","#f43f5e","#84cc16","#a78bfa","#fb923c","#0ea5e9"]
            fig_dt = go.Figure(go.Bar(
                y=df_data["Data Type"], x=df_data["Relative Prevalence"],
                orientation="h",
                marker=dict(color=data_colors, opacity=0.88, line=dict(color="white", width=0.5)),
                text=df_data["Relative Prevalence"].apply(lambda v: f"  Score {v}/9"),
                textposition="outside", textfont=dict(size=11, color=TEXT, family="Inter, sans-serif"),
            ))
            layout = chart_layout(height=400, show_legend=False)
            layout.update({
                "xaxis": dict(title="Relative Prevalence Score", range=[0,12],
                              gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11)),
                "yaxis": dict(tickfont=dict(color=TEXT, size=11), gridcolor="#f1f5f9"),
            })
            fig_dt.update_layout(**layout)
            st.plotly_chart(fig_dt, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_dt = "Data categories stolen in confirmed breaches"
            _hl_dt  = "Internal documents overtook personal data — ransomware's 'double extortion' is why"
            _bd_dt  = ("Ransomware operators now exfiltrate files before encrypting them, threatening to publish sensitive "
                       "internal documents if the ransom is not paid. This 'double extortion' tactic made internal documents "
                       "the most stolen category for the first time. Credentials rank highly because a single set of stolen "
                       "logins can be resold dozens of times and used across multiple organizations.")
            _ext_dt = ("Understanding what attackers steal reveals what they value most. Internal documents (contracts, "
                       "M&A plans, strategic roadmaps) are highly prized by both financial criminals and nation-state actors "
                       "— publishing them creates regulatory, reputational, and competitive damage independent of any ransom "
                       "payment. Personal data retains value because it is resold for identity fraud, synthetic identity "
                       "creation, and targeted phishing. Medical records command the highest individual price — up to $1,000 "
                       "per record — because they contain immutable identifiers (date of birth, health history) that cannot "
                       "be changed like a credit card number. Credentials are the 'key' category: stolen credentials feed "
                       "directly into future attacks, creating a compounding risk cycle. An organization that loses "
                       "credentials in one breach may find them used to breach a partner organization months later. "
                       "Payment card data, while historically the top target, has declined in relative value as card "
                       "networks improve real-time fraud detection.")
            st.markdown(source_badge(_src_dt), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_dt, _bd_dt), unsafe_allow_html=True)
            open_analysis_btn("data_types", fig_dt, "Most Commonly Stolen Data",
                              _src_dt, _hl_dt, _bd_dt, _ext_dt)

        with col10:
            st.markdown("#### How Attackers Bypass Multi-Factor Authentication")
            st.caption("Three techniques, each accounting for roughly one-third of Multi-Factor Authentication bypass incidents")
            st.markdown(audience_badge("expert"), unsafe_allow_html=True)
            fig_mfa = go.Figure(go.Pie(
                labels=["Token Theft","Prompt Bombing","Adversary-in-the-Middle"],
                values=[31,31,31], hole=0.52,
                marker=dict(colors=[C_RED, C_AMBER, C_PURP], line=dict(color="white", width=3)),
                textinfo="percent",
                textposition="inside",
                textfont=dict(size=14, color="white", family="Inter, sans-serif"),
                pull=[0.04, 0.04, 0.04],
                showlegend=True,
            ))
            layout_mfa = chart_layout(height=400, show_legend=True, legend_y=-0.18)
            layout_mfa.update({
                "legend": dict(orientation="h", y=-0.18,
                               font=dict(size=12, color=TEXT, family="Inter, sans-serif"),
                               bgcolor="rgba(0,0,0,0)"),
                "annotations": [dict(text="Bypass<br>Methods", x=0.5, y=0.5,
                                     font=dict(size=13, color=MUTED, family="Inter, sans-serif"),
                                     showarrow=False)],
                "margin": dict(l=24, r=24, t=36, b=80),
            })
            fig_mfa.update_layout(**layout_mfa)
            st.plotly_chart(fig_mfa, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
            _src_mfa = "Social engineering & Multi-Factor Authentication bypass tactics"
            _hl_mfa  = "Three equal bypass techniques mean no single fix is sufficient"
            _bd_mfa  = ("Token Theft steals the session cookie after a successful login — Multi-Factor Authentication was "
                        "passed, then hijacked. Prompt Bombing floods a user's phone with approval requests until one is "
                        "accidentally accepted. Adversary-in-the-Middle intercepts the real authentication flow in real time. "
                        "The equal split signals attackers rapidly switch methods when one is defended, which is why "
                        "Multi-Factor Authentication alone is no longer a complete control — session protection and "
                        "phishing-resistant authentication (FIDO2) are the next step.")
            _ext_mfa = ("Token Theft has surged because modern authentication correctly validates Multi-Factor Authentication "
                        "at login — but session tokens issued afterwards are often long-lived and stored insecurely in "
                        "browsers. Stealing the token bypasses the need to defeat Multi-Factor Authentication at all. "
                        "The defence is short session lifetimes, continuous re-authentication, and device-bound tokens. "
                        "Prompt Bombing exploits push-notification fatigue: users receiving 20 approval requests in a row "
                        "sometimes approve one just to stop the interruptions. The defence is number-matching (the app "
                        "shows a code the user must match) rather than simple approve/deny. Adversary-in-the-Middle attacks "
                        "use real-time proxy servers that sit between the victim and the legitimate site, relaying "
                        "credentials and Multi-Factor Authentication codes as they are entered. The only effective defence "
                        "against this technique is phishing-resistant authentication — hardware security keys or passkeys "
                        "that are cryptographically bound to the legitimate domain and cannot be proxied.")
            st.markdown(source_badge(_src_mfa), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_mfa, _bd_mfa), unsafe_allow_html=True)
            open_analysis_btn("mfa_bypass", fig_mfa, "How Attackers Bypass Multi-Factor Authentication",
                              _src_mfa, _hl_mfa, _bd_mfa, _ext_mfa)

    st.markdown(f"""
<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:8px;">
  <div style="background:{SURFACE};border:1px solid {BORDER2};border-radius:10px;padding:14px 20px;
              box-shadow:0 1px 3px rgba(0,0,0,0.06);flex:1;min-width:110px;">
    <span style="color:{MUTED};font-size:12px;display:block;font-weight:500;margin-bottom:4px;">Business Email Compromise Losses 2024</span>
    <span style="color:{RED};font-family:'Inter',sans-serif;font-size:24px;font-weight:700;">$6.3B</span>
  </div>
  <div style="background:{SURFACE};border:1px solid {BORDER2};border-radius:10px;padding:14px 20px;
              box-shadow:0 1px 3px rgba(0,0,0,0.06);flex:1;min-width:110px;">
    <span style="color:{MUTED};font-size:12px;display:block;font-weight:500;margin-bottom:4px;">AI-Written Lures</span>
    <span style="color:{ORANGE};font-family:'Inter',sans-serif;font-size:24px;font-weight:700;">~10%</span>
  </div>
  <div style="background:{SURFACE};border:1px solid {BORDER2};border-radius:10px;padding:14px 20px;
              box-shadow:0 1px 3px rgba(0,0,0,0.06);flex:1;min-width:110px;">
    <span style="color:{MUTED};font-size:12px;display:block;font-weight:500;margin-bottom:4px;">Espionage Motive</span>
    <span style="color:{PINK};font-family:'Inter',sans-serif;font-size:24px;font-weight:700;">52%</span>
  </div>
</div>
        """, unsafe_allow_html=True)

        # ─────────────────────────────────────────
# SECTION 6 — VULNERABILITY EXPLOITATION THEMES
# ─────────────────────────────────────────
with _tab_trends:
    with st.expander("📈  Exploitation Trends", expanded=True):

        st.markdown("## How Exploitation Trends Have Shifted Over 12 Weeks")
        st.caption("Weekly incident volume by exploitation type — hover over the chart to compare categories")
        st.markdown(audience_badge("expert"), unsafe_allow_html=True)

        fig_trends = go.Figure()
        for (name, vals), color in zip(vuln_series.items(), vuln_colors):
            r,g,b = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
            fig_trends.add_trace(go.Scatter(
                x=vuln_weeks, y=vals,
                mode="lines+markers",
                name=name,
                line=dict(color=color, width=3),
                marker=dict(size=8, color=color, line=dict(color="white", width=2)),
                fill="tozeroy",
                fillcolor=f"rgba({r},{g},{b},0.09)",
                hovertemplate=f"<b>{name}</b><br>%{{x}}: %{{y}} incidents<extra></extra>",
            ))

        layout = chart_layout(height=460, show_legend=True)
        layout.update({
            "xaxis": dict(gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11), automargin=True),
            "yaxis": dict(title="Incidents / Week", gridcolor="#f1f5f9",
                          tickfont=dict(color=MUTED, size=11), automargin=True),
            "hovermode": "x unified",
            "legend": dict(
                orientation="v",
                x=1.01, y=1,
                xanchor="left", yanchor="top",
                font=dict(size=12, color=TEXT, family="Inter, sans-serif"),
                bgcolor="rgba(248,250,252,0.95)",
                bordercolor=BORDER2,
                borderwidth=1,
            ),
            "margin": dict(l=56, r=160, t=36, b=56),
        })
        fig_trends.update_layout(**layout)
        st.plotly_chart(fig_trends, use_container_width=True, config={"displayModeBar": True, "displaylogo": False, "modeBarButtonsToAdd": ["toggleFullscreen"]})
        _src_tr = "Weekly incident trend by exploitation theme — 12-week window"
        _hl_tr  = "Remote Access and Vendor Risk are growing — Phishing is surprisingly stable"
        _bd_tr  = ("Remote Access exploitation is rising because hybrid work permanently expanded the Virtual Private "
                   "Network and Remote Desktop Protocol attack surface. Vendor Risk is climbing as attackers pivot to "
                   "Managed Service Providers and third-party integrations — compromising one supplier grants access to "
                   "dozens of clients simultaneously (the MOVEit and SolarWinds playbook). Phishing staying flat reflects "
                   "a grim truth: despite years of awareness training, humans remain a consistent and reliable target.")
        _ext_tr = ("The 12-week window reveals trajectory, not just snapshot. Remote Access exploitation will likely "
                   "continue rising as more organizations extend Virtual Private Network access to contractors and "
                   "remote workers without enforcing the same security controls applied to full-time employees. "
                   "Legacy and Unpatched Systems are climbing steadily — this reflects a structural problem: "
                   "as software libraries age and vendors end support, the pool of unpatched, exploitable systems "
                   "grows faster than organizations can remediate. Misconfiguration is declining slightly — cloud "
                   "providers are improving default-secure configurations and tooling that automatically flags "
                   "exposed storage buckets and open ports. Phishing's stability near 20–25 incidents per week "
                   "despite widespread training investment is a reminder that it is a people problem as much as "
                   "a technology problem — phishing-resistant authentication (hardware keys, passkeys) is more "
                   "effective than training alone at stopping credential theft via phishing.")
        st.markdown(source_badge(_src_tr), unsafe_allow_html=True)
        st.markdown(insight_box(_hl_tr, _bd_tr), unsafe_allow_html=True)
        open_analysis_btn("trends", fig_trends, "How Exploitation Trends Have Shifted Over 12 Weeks",
                          _src_tr, _hl_tr, _bd_tr, _ext_tr)
        # ─────────────────────────────────────────
# SECTION — INDUSTRIAL CONTROL SYSTEMS (ICS)
# ─────────────────────────────────────────
with _tab_ics:
    with st.expander("🏭  Industrial Control System Cyber Threats", expanded=True):

        _ICS_DIR = os.path.join(os.path.dirname(__file__), "ics_data")
        _ICS_SRC = ("Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025 · "
                    "ics-cert.kaspersky.com")

        df_ics_region   = pd.read_csv(os.path.join(_ICS_DIR, "02_regional_overall.csv"))
        df_ics_industry = pd.read_csv(os.path.join(_ICS_DIR, "03_industry_breakdown.csv"))
        df_ics_hist     = pd.read_csv(os.path.join(_ICS_DIR, "06_historical_quarterly_trends.csv"))
        df_ics_src_h    = pd.read_csv(os.path.join(_ICS_DIR, "07_threat_sources_historical.csv"))

        st.markdown("---")
        st.markdown("## Industrial Control System Cyber Threats")
        st.caption(
            "Data from Kaspersky ICS-CERT covering Q2 2025 (April – June 2025). "
            "Percentages show the share of ICS computers on which malicious objects were blocked during the quarter."
        )

        ics_col1, ics_col2 = st.columns(2, gap="large")

        # ── Chart 1 : ICS Attack Rate by Region ────────────────────────────────────
        with ics_col1:
            st.markdown("### ICS Attack Rate by Region (Q2 2025)")
            st.caption("Percentage of ICS computers on which threats were blocked, by region — each region shown in its own distinct colour")
            st.markdown(audience_badge("expert"), unsafe_allow_html=True)

            _df_r    = df_ics_region[df_ics_region["Region"] != "World"].sort_values("Q2_2025_Pct")
            _world_r = float(df_ics_region.loc[df_ics_region["Region"] == "World", "Q2_2025_Pct"].iloc[0])
            _palette_r = ["#0ea5e9","#10b981","#f59e0b","#ef4444","#8b5cf6",
                          "#ec4899","#14b8a6","#f97316","#6366f1","#84cc16",
                          "#a78bfa","#06b6d4","#f43f5e"]
            _colors_r = _palette_r[:len(_df_r)]

            fig_ics_region = go.Figure(go.Bar(
                x=_df_r["Q2_2025_Pct"], y=_df_r["Region"], orientation="h",
                marker_color=_colors_r,
                text=[f"{v:.1f}%" for v in _df_r["Q2_2025_Pct"]],
                textposition="outside",
                hovertemplate="<b>%{y}</b><br>ICS Computers Attacked: %{x:.1f}%<extra></extra>",
            ))
            fig_ics_region.add_vline(
                x=_world_r, line_dash="dash", line_color=ORANGE, line_width=2,
                annotation_text=f"Global avg: {_world_r}%",
                annotation_position="bottom right",
                annotation_font=dict(color=ORANGE, size=11),
            )
            _lay_r = chart_layout(height=440)
            _lay_r.update({
                "xaxis": dict(title="% of ICS Computers Attacked", ticksuffix="%",
                              range=[0, _df_r["Q2_2025_Pct"].max() * 1.22]),
                "yaxis": dict(title=""),
                "showlegend": False,
                "margin": dict(l=155, r=64, t=36, b=48),
            })
            fig_ics_region.update_layout(**_lay_r)
            st.plotly_chart(fig_ics_region, use_container_width=True,
                            config={"displayModeBar": True, "displaylogo": False,
                                    "modeBarButtonsToAdd": ["toggleFullscreen"]})

            _hl_icsr = "Africa and South-East Asia face the highest industrial cyber risk"
            _bd_icsr = ("In Q2 2025, 27.8% of ICS computers in Africa and 26.8% in South-East Asia were targeted — "
                        "nearly 2.5 times the rate seen in Northern Europe (11.2%). High attack rates in these regions "
                        "often reflect older, unpatched equipment and limited dedicated industrial cybersecurity staff.")
            _ext_icsr = ("The disparity between regions reflects differences in industrial modernisation and patching cycles. "
                         "Western and Northern Europe benefit from stricter regulatory environments (such as the European Union "
                         "Network and Information Security Directive) and higher investment in operational technology security. "
                         "Africa and South-East Asia often operate legacy programmable logic controllers and supervisory "
                         "control and data acquisition systems that cannot be updated without production downtime. "
                         "Central Asia recorded the largest single-quarter improvement (−3.6 percentage points), suggesting "
                         "targeted remediation efforts. Australia and New Zealand and Northern Europe both saw small increases, "
                         "which may reflect broader detection capability expansion rather than a true rise in attacks.")
            st.markdown(source_badge(url="https://ics-cert.kaspersky.com/publications/reports/2025/09/11/threat-landscape-for-industrial-automation-systems-q2-2025/", label="Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025"), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_icsr, _bd_icsr), unsafe_allow_html=True)
            open_analysis_btn("ics_region", fig_ics_region,
                              "ICS Attack Rate by Region (Q2 2025)",
                              _ICS_SRC, _hl_icsr, _bd_icsr, _ext_icsr)

        # ── Chart 2 : ICS Attack Rate by Industry ──────────────────────────────────
        with ics_col2:
            st.markdown("### ICS Attack Rate by Industry Sector (Q2 2025)")
            st.caption("Percentage of ICS computers on which threats were blocked, by industry — each sector shown in its own distinct colour")
            st.markdown(audience_badge("exec"), unsafe_allow_html=True)

            _df_i    = df_ics_industry[df_ics_industry["Industry"] != "World"].sort_values("Q2_2025_Pct")
            _world_i = float(df_ics_industry.loc[df_ics_industry["Industry"] == "World", "Q2_2025_Pct"].iloc[0])
            _palette_i = ["#f43f5e","#3b82f6","#f59e0b","#a78bfa","#06b6d4","#84cc16","#fb923c"]
            _colors_i = _palette_i[:len(_df_i)]

            fig_ics_industry = go.Figure(go.Bar(
                x=_df_i["Q2_2025_Pct"], y=_df_i["Industry"], orientation="h",
                marker_color=_colors_i,
                text=[f"{v:.1f}%" for v in _df_i["Q2_2025_Pct"]],
                textposition="outside",
                hovertemplate="<b>%{y}</b><br>ICS Computers Attacked: %{x:.1f}%<extra></extra>",
            ))
            fig_ics_industry.add_vline(
                x=_world_i, line_dash="dash", line_color=ORANGE, line_width=2,
                annotation_text=f"Global avg: {_world_i}%",
                annotation_position="bottom right",
                annotation_font=dict(color=ORANGE, size=11),
            )
            _lay_i = chart_layout(height=440)
            _lay_i.update({
                "xaxis": dict(title="% of ICS Computers Attacked", ticksuffix="%",
                              range=[0, _df_i["Q2_2025_Pct"].max() * 1.22]),
                "yaxis": dict(title=""),
                "showlegend": False,
                "margin": dict(l=175, r=64, t=36, b=48),
            })
            fig_ics_industry.update_layout(**_lay_i)
            st.plotly_chart(fig_ics_industry, use_container_width=True,
                            config={"displayModeBar": True, "displaylogo": False,
                                    "modeBarButtonsToAdd": ["toggleFullscreen"]})

            _hl_icsi = "Biometrics and Building Automation top the ICS attack chart"
            _bd_icsi = ("Biometrics (27.2%) and Building Automation (23.4%) recorded the highest share of attacked ICS "
                        "computers in Q2 2025. Oil and Gas (16.1%) and Manufacturing (16.7%) sit below the global average, "
                        "possibly reflecting stronger perimeter controls following high-profile pipeline incidents.")
            _ext_icsi = ("Biometrics systems are often network-connected for centralised identity management, making them "
                         "an overlooked entry point into physical security infrastructure. Building Automation systems "
                         "(heating, ventilation, air conditioning, access control) are increasingly Internet-connected but "
                         "frequently managed by facilities teams rather than cybersecurity professionals, creating gaps. "
                         "The relatively lower rates for Oil and Gas and Manufacturing may reflect increased investment "
                         "following the 2021 Colonial Pipeline incident, which drove sector-wide adoption of air-gapping, "
                         "network segmentation, and Purdue Model enforcement. Electric Power sits close to the global "
                         "average, consistent with ongoing nation-state interest in energy infrastructure.")
            st.markdown(source_badge(url="https://ics-cert.kaspersky.com/publications/reports/2025/09/11/threat-landscape-for-industrial-automation-systems-q2-2025/", label="Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025"), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_icsi, _bd_icsi), unsafe_allow_html=True)
            open_analysis_btn("ics_industry", fig_ics_industry,
                              "ICS Attack Rate by Industry Sector (Q2 2025)",
                              _ICS_SRC, _hl_icsi, _bd_icsi, _ext_icsi)

        ics_col3, ics_col4 = st.columns(2, gap="large")

        # ── Chart 3 : Historical ICS Attack Trend ──────────────────────────────────
        with ics_col3:
            st.markdown("### Global ICS Attack Rate Trend (2022 – 2025)")
            st.caption("Share of ICS computers attacked worldwide per quarter, with key threat category overlays")
            st.markdown(audience_badge("expert"), unsafe_allow_html=True)

            fig_ics_hist = go.Figure()
            fig_ics_hist.add_trace(go.Scatter(
                x=df_ics_hist["Quarter_Label"], y=df_ics_hist["Overall_ICS_Attacked_Pct"],
                name="Overall ICS Attack Rate", mode="lines+markers",
                line=dict(color=RED, width=3), marker=dict(size=6),
                hovertemplate="<b>%{x}</b><br>Overall Attacked: %{y:.1f}%<extra></extra>",
            ))
            fig_ics_hist.add_trace(go.Scatter(
                x=df_ics_hist["Quarter_Label"], y=df_ics_hist["Malicious_Scripts_Pct"],
                name="Malicious Scripts and Phishing Pages", mode="lines+markers",
                line=dict(color=C_BLUE, width=2, dash="dot"), marker=dict(size=5),
                hovertemplate="<b>%{x}</b><br>Malicious Scripts: %{y:.2f}%<extra></extra>",
            ))
            fig_ics_hist.add_trace(go.Scatter(
                x=df_ics_hist["Quarter_Label"], y=df_ics_hist["Spyware_Pct"],
                name="Spyware, Backdoors, and Keyloggers", mode="lines+markers",
                line=dict(color=ORANGE, width=2, dash="dash"), marker=dict(size=5),
                hovertemplate="<b>%{x}</b><br>Spyware: %{y:.2f}%<extra></extra>",
            ))
            fig_ics_hist.add_trace(go.Scatter(
                x=df_ics_hist["Quarter_Label"], y=df_ics_hist["Denylisted_Resources_Pct"],
                name="Denylisted Internet Resources", mode="lines+markers",
                line=dict(color=C_GREEN, width=2, dash="dashdot"), marker=dict(size=5),
                hovertemplate="<b>%{x}</b><br>Denylisted Resources: %{y:.2f}%<extra></extra>",
            ))
            _lay_h = chart_layout(height=440, show_legend=True)
            _lay_h.update({
                "xaxis": dict(title="Quarter", tickangle=-45, type="category"),
                "yaxis": dict(title="% of ICS Computers Affected", ticksuffix="%"),
                "legend": dict(orientation="h", y=-0.38, x=0, font=dict(size=10,
                               color=MUTED, family="Inter, sans-serif")),
                "margin": dict(l=56, r=24, t=36, b=110),
            })
            fig_ics_hist.update_layout(**_lay_h)
            st.plotly_chart(fig_ics_hist, use_container_width=True,
                            config={"displayModeBar": True, "displaylogo": False,
                                    "modeBarButtonsToAdd": ["toggleFullscreen"]})

            _hl_icsh = "Global ICS attack rates have fallen 22% since their 2022 – 2023 peak"
            _bd_icsh = ("The share of ICS computers attacked worldwide dropped from 26.8% in Q2 2023 to 20.5% in "
                        "Q2 2025 — a 6.3 percentage point reduction. Malicious scripts and phishing pages remain "
                        "the leading threat category but have also declined steadily from 9.96% (Q1 2023) to 6.49%.")
            _ext_icsh = ("The downward trend reflects increased investment in operational technology security following "
                         "a wave of high-profile industrial incidents in 2021 – 2022. Endpoint protection improvements, "
                         "stronger network segmentation between IT and operational technology networks, and greater "
                         "awareness of industrial security frameworks have all contributed. However, while the volume of "
                         "attacked computers is declining, malware sophistication is increasing — spyware and backdoors "
                         "enable persistent, long-term access. Denylisted Internet Resources spiked in Q1 2023 (8.89%) "
                         "likely driven by increased scanning activity after major vulnerability disclosures, before "
                         "normalising. Ransomware in ICS environments remains low in percentage terms (0.14%), but targets "
                         "operational technology directly — with the potential for physical disruption to critical "
                         "infrastructure, unlike traditional IT ransomware.")
            st.markdown(source_badge(url="https://ics-cert.kaspersky.com/publications/reports/2025/09/11/threat-landscape-for-industrial-automation-systems-q2-2025/", label="Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025"), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_icsh, _bd_icsh), unsafe_allow_html=True)
            open_analysis_btn("ics_hist", fig_ics_hist,
                              "Global ICS Attack Rate Trend (2022 – 2025)",
                              _ICS_SRC, _hl_icsh, _bd_icsh, _ext_icsh)

        # ── Chart 4 : Threat Delivery Pathways ─────────────────────────────────────
        with ics_col4:
            st.markdown("### How Threats Reach Industrial Systems (2024 – 2025)")
            st.caption("Percentage of ICS computers attacked via each delivery pathway over the last three quarters")
            st.markdown(audience_badge("expert"), unsafe_allow_html=True)

            _df_s = df_ics_src_h[df_ics_src_h["Quarter_Label"].isin(["Q2 2024", "Q1 2025", "Q2 2025"])]
            _qtrs = _df_s["Quarter_Label"].tolist()

            fig_ics_src = go.Figure()
            for _col, _label, _color in [
                ("Internet_Pct",       "Internet",                    C_BLUE),
                ("Email_Clients_Pct",  "Email Clients",               RED),
                ("Removable_Media_Pct","Removable Media",             ORANGE),
                ("Network_Folders_Pct","Shared Network Folders",      C_GREEN),
            ]:
                fig_ics_src.add_trace(go.Bar(
                    name=_label, x=_qtrs, y=_df_s[_col],
                    marker_color=_color,
                    text=[f"{v:.2f}%" for v in _df_s[_col]],
                    textposition="auto",
                    hovertemplate=f"<b>{_label}</b><br>%{{x}}: %{{y:.2f}}%<extra></extra>",
                ))
            _lay_s = chart_layout(height=440, show_legend=True)
            _lay_s.update({
                "barmode": "group",
                "xaxis": dict(title="Quarter", type="category"),
                "yaxis": dict(title="% of ICS Computers Reached", ticksuffix="%"),
                "legend": dict(orientation="h", y=-0.28, x=0, font=dict(size=10,
                               color=MUTED, family="Inter, sans-serif")),
                "margin": dict(l=56, r=24, t=36, b=90),
            })
            fig_ics_src.update_layout(**_lay_s)
            st.plotly_chart(fig_ics_src, use_container_width=True,
                            config={"displayModeBar": True, "displaylogo": False,
                                    "modeBarButtonsToAdd": ["toggleFullscreen"]})

            _hl_icss = "The internet is the primary gateway into industrial systems — and email threats are rising"
            _bd_icss = ("In Q2 2025, 9.76% of ICS computers were attacked via internet connections — nearly three "
                        "times the email rate (3.06%). However, email-borne threats are the only pathway showing "
                        "consistent growth: up from 2.72% in Q4 2024 to 3.06% in Q2 2025. Removable media and "
                        "shared network folders continue their multi-year decline.")
            _ext_icss = ("The decline of removable media (from 2.66% in Q2 2022 to 0.37% in Q2 2025) reflects "
                         "widespread enforcement of device-control policies following the Stuxnet era, where removable "
                         "media was the primary mechanism for bridging air gaps into isolated industrial networks. "
                         "Shared Network Folders are now a negligible pathway at 0.05%, reflecting improved "
                         "lateral-movement controls. The consistent rise in email-delivered threats is significant: "
                         "it indicates that ICS workstations are increasingly connected to corporate IT networks and "
                         "that engineering staff are using email on machines that also run industrial software — a "
                         "dangerous convergence of IT and operational technology environments. Dedicated operational "
                         "technology workstations with no email client access are a recommended mitigation.")
            st.markdown(source_badge(url="https://ics-cert.kaspersky.com/publications/reports/2025/09/11/threat-landscape-for-industrial-automation-systems-q2-2025/", label="Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025"), unsafe_allow_html=True)
            st.markdown(insight_box(_hl_icss, _bd_icss), unsafe_allow_html=True)
            open_analysis_btn("ics_sources", fig_ics_src,
                              "How Threats Reach Industrial Systems (2024 – 2025)",
                              _ICS_SRC, _hl_icss, _bd_icss, _ext_icss)

        # ─────────────────────────────────────────
        # CONTRIBUTORS
        # ─────────────────────────────────────────

        # LinkedIn SVG logo (official blue)
LI_LOGO = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="#0a66c2">
  <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136
  1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85
  3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065
  2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225
  0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2
  24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
        </svg>"""

        # ─────────────────────────────────────────
# AUDIENCE GUIDES — Separate section below main dashboard
# ─────────────────────────────────────────
st.divider()
# Scroll anchor — JS targets this element when a top button is clicked
st.markdown('<div id="audience-anchor" style="scroll-margin-top:72px;"></div>', unsafe_allow_html=True)

# Trigger scroll if the user came from a top button
if st.session_state.get("_scroll_guides"):
    st.session_state["_scroll_guides"] = False
    components.html("""<script>
setTimeout(function() {
    var el = window.parent.document.getElementById('audience-anchor');
    if (el) { el.scrollIntoView({behavior: 'smooth', block: 'start'}); }
}, 250);
</script>""", height=0)

st.markdown("## 📚 Audience Guides")
st.caption("The same data — explained three different ways. Pick the view that suits you.")

_AUDIENCE_KEYS   = ["simple", "expert", "exec"]
_AUDIENCE_LABELS = ["💡  Plain & Simple", "⚙️  Expert Console", "💼  Executive Brief"]
_current_idx = _AUDIENCE_KEYS.index(st.session_state.get("_audience", "simple"))
_chosen_label = st.radio(
    "Select audience guide:",
    _AUDIENCE_LABELS,
    index=_current_idx,
    horizontal=True,
    label_visibility="collapsed",
)
_chosen_key = _AUDIENCE_KEYS[_AUDIENCE_LABELS.index(_chosen_label)]
st.session_state["_audience"] = _chosen_key

# ─────────────────────────────────────────
# PLAIN & SIMPLE — For Everyone
# ─────────────────────────────────────────
if _chosen_key == "simple":
    st.markdown(f"""
<div style="background:linear-gradient(135deg,#fffbeb 0%,#fefce8 100%);
            border:1px solid #fde68a;border-radius:16px;
            padding:2rem 2.4rem 1.6rem 2.4rem;margin-bottom:1.4rem;
            box-shadow:0 2px 12px rgba(245,158,11,0.08);">
  <p style="margin:0 0 0.4rem 0;font-size:0.8rem;font-weight:700;letter-spacing:0.08em;
            color:#92400e;text-transform:uppercase;font-family:'Inter',sans-serif;">
    💡 Plain & Simple · No tech knowledge needed
  </p>
  <h2 style="margin:0 0 0.6rem 0;font-size:1.7rem;font-weight:800;color:#0f172a;
             font-family:'Inter',sans-serif;border:none;padding:0;margin-top:0;">
    What Is Cyber Crime — And Should You Worry?
  </h2>
  <p style="margin:0;font-size:1rem;color:#475569;font-family:'Inter',sans-serif;line-height:1.7;max-width:780px;">
    Think of this like a neighbourhood watch report — but for the internet.
    This page breaks down everything on this dashboard into plain, everyday language.
    No passwords required to understand it. No tech degree needed.
  </p>
</div>
""", unsafe_allow_html=True)

    _simple_tips = {
        1:  ("🏦", "Watch Out for Fake Tax Emails",
             "Scammers send emails pretending to be the Canada Revenue Agency saying you owe money or have a refund waiting. "
             "The government will NEVER email you asking for your banking details. If you get one of these, delete it and call the CRA directly using the number on their official website."),
        2:  ("💌", "Be Careful With Online Romance",
             "Scammers create fake dating profiles and build a friendship over weeks before asking for money. "
             "If someone you have only met online asks for gift cards or a wire transfer — it is a scam. Always. No exceptions."),
        3:  ("📋", "Your Employer Will Never Email You Asking for Your Password",
             "If you get an email that looks like it is from IT or payroll asking you to verify your account details, call them on the phone first. "
             "Real IT teams do not ask for passwords by email, ever."),
        4:  ("✈️", "Book Travel Only on Official Websites",
             "Fake travel deal websites steal your credit card details. "
             "Always type the airline or hotel's web address yourself instead of clicking links in emails or social media ads."),
        5:  ("📑", "Protect Your SIN Number Like It Is Cash",
             "Your Social Insurance Number is as valuable as cash to a thief. "
             "Never give it out during a job interview or to anyone who calls you unexpectedly — a real employer will only ask for it after you are hired, through a secure system."),
        6:  ("📶", "Free Wi-Fi at the Coffee Shop Can Be Dangerous",
             "Hackers set up fake Wi-Fi networks with names like 'Tim Hortons Free WiFi'. "
             "Once connected, they can see everything you do online. Avoid doing banking or anything personal on public Wi-Fi."),
        7:  ("🏖️", "Set Up Alerts on Your Bank Account",
             "Ask your bank to send you a text message every time money moves in or out of your account. "
             "That way you will know immediately if something suspicious happens while you are away on vacation."),
        8:  ("🎒", "Talk to Your Kids About Online Scams Before School Starts",
             "Children are targeted with fake app downloads and 'free game' links that install viruses on the family computer. "
             "A quick 10-minute conversation about not clicking unknown links can save a lot of trouble."),
        9:  ("📱", "Use an App for Your Security Codes — Not Text Messages",
             "Those 6-digit codes sent by text to confirm your login can be stolen by hackers. "
             "Apps like Google Authenticator or Microsoft Authenticator are much safer. Ask your bank if they support it."),
        10: ("🔐", "Back Up Your Photos and Important Files Today",
             "Ransomware is like a digital padlock a criminal puts on all your files — then demands money to unlock them. "
             "A simple USB drive backup or free cloud backup (like Google Photos) means you would never need to pay."),
        11: ("🛒", "If a Deal Looks Too Good to Be True — It Is",
             "Fake shopping websites surge every Black Friday. Before buying from an unfamiliar website, "
             "search the store name plus the word 'scam' and look very carefully at the web address for subtle misspellings."),
        12: ("🎄", "Gift Card Requests Are Always a Scam",
             "No government agency, grandchild, or employer will ever ask you to buy iTunes or Google Play gift cards to solve a problem. "
             "If someone asks this — hang up immediately and tell a family member."),
    }
    _sm = _simple_tips[datetime.datetime.now().month]
    st.markdown("### 🗓️ Your Safety Tip This Month")
    st.markdown(f"""
<div style="background:#fffbeb;border:1px solid #fde68a;border-left:5px solid #f59e0b;
            border-radius:10px;padding:1.3rem 1.5rem;margin-bottom:1.5rem;">
  <p style="margin:0 0 6px 0;font-size:1.6rem;">{_sm[0]}</p>
  <p style="margin:0 0 8px 0;font-size:1.05rem;font-weight:700;color:#0f172a;font-family:'Inter',sans-serif;">{_sm[1]}</p>
  <p style="margin:0;font-size:0.95rem;color:#334155;font-family:'Inter',sans-serif;line-height:1.75;">{_sm[2]}</p>
</div>""", unsafe_allow_html=True)

    _simple_sections = [
        ("🏠", "Who Is Getting Targeted?",
         "Imagine thieves deciding which neighbourhood to rob. They look for the easiest targets with the most valuable stuff. "
         "On the internet, hackers do exactly the same thing. Last year, <strong>Manufacturing companies had the most confirmed break-ins (1,607 cases)</strong>, "
         "followed by Healthcare (1,542) and Finance (927). Why manufacturing? Because their computers control machines — "
         "and stopping a factory floor is incredibly expensive. That gives hackers more bargaining power when they demand money.",
         "🏭 Manufacturing · 🏥 Healthcare · 🏦 Finance are the three most targeted sectors",
         "📡 Sector Risk"),
        ("🔑", "How Do Hackers Get In?",
         "Think of your home: most burglars do not break a window — they try the door if it is unlocked. Hackers are the same. "
         "The most common way in is <strong>stolen passwords (22% of cases)</strong> — often from old data leaks where your email and password were already exposed online. "
         "The second most common method is <strong>unpatched security gaps (20%)</strong> — like a broken lock no one bothered to fix. "
         "Phishing emails (fake messages that trick you into clicking a link) account for 15% of break-ins.",
         "💡 Use a different password for every account. A free password manager like Bitwarden makes this easy.",
         "⚔️ Attack Methods"),
        ("🔒", "What Is Ransomware — And Why Is It Everywhere?",
         "Ransomware is like a digital padlock a thief puts on your files. They lock everything — your photos, your work documents, everything — "
         "and demand money to unlock it. <strong>In 2024, nearly 1 in every 2 data breaches involved ransomware (44%)</strong>. That has doubled in just three years. "
         "The good news: <strong>64% of victims now refuse to pay</strong>, and experts say this is the right call — "
         "paying rarely gets your files back and only funds the next attack. The solution is simple: keep regular backups.",
         "✅ Back up your important files to an external USB drive or free cloud storage regularly.",
         "🔓 Ransomware"),
        ("📂", "What Do Hackers Actually Steal?",
         "Hackers are after information they can sell or use. Think of it like which drawer a burglar goes for first. "
         "<strong>Internal work documents (contracts, plans, confidential emails)</strong> are now the most stolen type of data — "
         "because companies will pay handsomely to keep them private. Personal information like your name, address, and birthdate is also highly valued "
         "because it can be used to open credit cards in your name. Medical records are worth up to $1,000 each — "
         "because unlike a credit card, you cannot change your health history.",
         "🏥 Protect your Medicare card number and medical records as carefully as your credit card number.",
         "🗂️ Stolen Data"),
        ("🌍", "What About Factories and Power Plants?",
         "Industrial facilities like water treatment plants, electricity grids, and factories are increasingly targeted by hackers. "
         "In the spring of 2025, <strong>1 in 5 industrial computers worldwide had a cyber threat blocked on it</strong>. "
         "The main way in is through the internet — because more factory computers are connected online than ever before. "
         "Parts of Africa had the highest attack rates. Northern Europe was the safest region.",
         "🔌 Industrial cyberattacks affect everyone — an attack on a power grid or water supply is a public safety issue, not just a business problem.",
         "🏭 ICS Threats"),
        ("🤝", "Who Is Actually Doing This?",
         "You might picture hackers as lone individuals in dark rooms. The reality in 2024 is very different. "
         "<strong>80% of attacks come from organized criminal groups</strong> — run like businesses, with customer service teams for ransomware victims and HR departments. "
         "State-sponsored groups (hackers funded by foreign governments) increased their activity by 163% in 2024, targeting research, government, and critical infrastructure. "
         "This is not random — attacks are deliberate, targeted, and increasingly professional.",
         "🏛️ Governments and large organizations bear responsibility for protecting infrastructure — but individuals can protect themselves too.",
         "⚔️ Attack Methods"),
    ]

    for icon, title, body, takeaway, label in _simple_sections:
        st.markdown(f"""
<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;
            padding:1.3rem 1.5rem;margin-bottom:1rem;
            box-shadow:0 1px 4px rgba(0,0,0,0.05);">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px;">
    <p style="margin:0;font-size:1.5rem;">{icon}</p>
    <span style="font-size:0.72rem;font-weight:600;color:#475569;background:#f1f5f9;
                 border:1px solid #e2e8f0;border-radius:20px;padding:3px 10px;
                 font-family:'Inter',sans-serif;white-space:nowrap;">{label}</span>
  </div>
  <p style="margin:0 0 10px 0;font-size:1.05rem;font-weight:700;color:#0f172a;font-family:'Inter',sans-serif;">{title}</p>
  <p style="margin:0 0 12px 0;font-size:0.93rem;color:#334155;font-family:'Inter',sans-serif;line-height:1.8;">{body}</p>
  <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:9px 14px;">
    <p style="margin:0;font-size:0.88rem;color:#15803d;font-family:'Inter',sans-serif;font-weight:500;">{takeaway}</p>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Charts for Plain & Simple ──────────────────────────────────────────
    st.markdown("---")
    st.markdown("### 📊 The Charts — In Plain Terms")
    st.caption("These are the actual data visualisations from the dashboard. They look complex but the numbers tell a simple story.")

    _ps_c1, _ps_c2 = st.columns(2, gap="large")
    with _ps_c1:
        st.markdown("#### Which sectors get hit hardest by ransomware?")
        st.caption(
            "Each bar shows what share of hacks in that industry involved ransomware — criminals who lock your "
            "files and demand money to unlock them. A longer bar means that industry gets hit more often. "
            "Manufacturing and Education show up near the top because they often rely on older computers "
            "that are harder to update and protect."
        )
        st.plotly_chart(fig_rs, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)
    with _ps_c2:
        st.markdown("#### Is ransomware getting worse — or are people fighting back?")
        st.caption(
            "The rising bars show that ransomware attacks have been increasing over the past few years. "
            "But there's good news too — more and more victims are choosing NOT to pay the ransom. "
            "Paying doesn't guarantee you get your files back, and refusing to pay makes it less profitable "
            "for attackers to keep doing it."
        )
        st.plotly_chart(fig_fore, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)

    st.markdown("#### What do hackers actually steal?")
    st.caption(
        "When a hack is successful, this chart shows what kind of information gets taken most often. "
        "Passwords and login details are the most common target because they unlock everything else. "
        "Personal details like your name, address, or ID numbers come next. "
        "If you've ever had an account breached, the information in this chart is probably what was stolen."
    )
    st.plotly_chart(fig_dt, use_container_width=True, config={"displayModeBar": False})
    st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)

# ─────────────────────────────────────────
# EXPERT CONSOLE — For IT & Security Professionals
# ─────────────────────────────────────────
elif _chosen_key == "expert":
    st.markdown(f"""
<div style="background:linear-gradient(135deg,#eff6ff 0%,#f8fafc 100%);
            border:1px solid #93c5fd;border-left:6px solid #1d4ed8;border-radius:16px;
            padding:2rem 2.4rem 1.6rem 2.4rem;margin-bottom:1.4rem;
            box-shadow:0 2px 12px rgba(29,78,216,0.08);">
  <p style="margin:0 0 0.4rem 0;font-size:0.8rem;font-weight:700;letter-spacing:0.1em;
            color:#1d4ed8;text-transform:uppercase;font-family:'Inter',sans-serif;">
    ⚙️ Expert Console · Security Practitioner View
  </p>
  <h2 style="margin:0 0 0.6rem 0;font-size:1.7rem;font-weight:800;color:#0f172a;
             font-family:'Inter',sans-serif;border:none;padding:0;margin-top:0;">
    Threat Intelligence Deep Dive — DBIR 2025 & Kaspersky ICS-CERT Q2 2025
  </h2>
  <p style="margin:0;font-size:0.95rem;color:#475569;font-family:'Inter',sans-serif;line-height:1.7;max-width:780px;">
    MITRE ATT&CK mappings, IOC context, technical controls, and detection engineering notes
    for security practitioners, analysts, and engineers.
  </p>
</div>
""", unsafe_allow_html=True)

    _expert_tips = {
        1:  ("🎯", "January: Hunt for Tax-Season Credential Stuffing",
             "Rotate canary credentials in your IdP and monitor authentication failure spikes against financial and payroll applications. "
             "Ingest HIBP breach feeds into your SIEM and alert on accounts appearing in new credential dumps. "
             "Review OAuth token lifetimes — shorten refresh token TTLs ahead of peak phishing season."),
        2:  ("💌", "February: Harden Email Gateway Rules for BEC Season",
             "Enforce DMARC p=reject on all sending domains. Deploy DKIM signing verification on inbound mail. "
             "Tune your SEG to flag lookalike domains using homoglyph detection. "
             "Enable conditional access policies requiring compliant device for finance team email access."),
        3:  ("📋", "March: Audit Privileged Access to Finance & HR Systems",
             "Audit service accounts with standing access to payroll and HRIS systems — enforce just-in-time access via PAM. "
             "Validate all direct deposit change workflows require OOB (out-of-band) callback verification. "
             "Run a BEC tabletop — simulate a CFO impersonation request and measure detection/response time."),
        4:  ("✈️", "April: Validate Patch Coverage Against CISA KEV",
             "CVE exploitation hit 20% of initial access vectors in DBIR 2025, up 34% YoY. "
             "Prioritize CVEs in Ivanti, Fortinet, Citrix, and Cisco VPN products. "
             "Run Shodan/Censys queries against your ASN to enumerate exposed management interfaces. "
             "Validate patch SLA compliance against the CISA Known Exploited Vulnerabilities catalogue."),
        5:  ("📑", "May: Validate MFA Deployment Against Bypass Techniques",
             "DBIR 2025 identifies three equally-prevalent MFA bypass methods: AiTM token theft (Evilginx2/Modlishka), "
             "MFA prompt bombing, and session cookie hijacking. "
             "Deploy phishing-resistant FIDO2/WebAuthn for admin and finance accounts. "
             "Audit Conditional Access gaps — ensure token binding or device compliance is enforced."),
        6:  ("📶", "June: Enumerate and Harden Remote Access Attack Surface",
             "Remote Access exploitation is trending upward across the 12-week vulnerability theme data. "
             "Enumerate all VPN, RDP, and remote desktop gateway endpoints. Enforce NLA on RDP. "
             "Review split-tunnelling policies — ensure all DNS queries route through your resolver. "
             "Deploy honeypot credentials in AD to detect credential stuffing against internal services."),
        7:  ("🏖️", "July: Implement Out-of-Office BEC Mitigations",
             "Configure mail flow rules to suppress internal details from OOO replies to external senders. "
             "Enforce dual-approval on financial transactions above threshold during peak leave periods. "
             "Enable UEBA rules for unusual approval chain deviations. "
             "Brief SOC tier 1 on escalation paths when senior analysts are OOO."),
        8:  ("🎒", "August: Ingest Education Sector Threat Feeds",
             "Education institutions had 851 confirmed breaches in 2024 — disproportionate to their size. "
             "If your org provides services to educational institutions, review third-party access policies. "
             "Ingest MS-ISAC education sector threat feeds. "
             "Scan for exposed LDAP directories and student SSO endpoints in your partner ecosystem."),
        9:  ("📱", "September: Harden Against SIM Swap and OTP Interception",
             "Deploy FIDO2 authenticators to eliminate SMS OTP dependency for high-privilege accounts. "
             "Work with your mobile carrier to enforce SIM lock and account PINs for corporate devices. "
             "Configure your IdP to alert on authentication method downgrade attempts. "
             "Review MDM policies — enforce full-disk encryption and remote wipe on all enrolled devices."),
        10: ("🔐", "October: Run a Full Ransomware Recovery Validation",
             "Verify backup immutability — ensure backup storage cannot be deleted by a compromised account. "
             "Run a purple team exercise simulating TA0010 (exfiltration) + T1486 (data encrypted for impact). "
             "Validate EDR exclusions list is minimal and reviewed. "
             "Test offline bare-metal restoration — do not assume backups work without validation."),
        11: ("🛒", "November: Hunt for Web Skimming and Magecart Indicators",
             "Audit all third-party JavaScript loaded on payment pages. "
             "Implement Subresource Integrity (SRI) hashes on external scripts. "
             "Deploy Content Security Policy (CSP) headers to restrict script execution domains. "
             "Monitor for new DNS A-record resolutions from payment page domains to unexpected CDN endpoints."),
        12: ("🎄", "December: Activate Holiday Incident Response Posture",
             "December sees a 30% ransomware surge above monthly average. "
             "Ensure on-call runbooks are current and all IR contacts are reachable. "
             "Pre-stage IR tooling on critical servers (offline copies of Sysinternals, memory acquisition tools). "
             "Validate SIEM is ingesting holiday-period logs in real time — do not reduce retention or alerting thresholds."),
    }
    _ex = _expert_tips[datetime.datetime.now().month]
    st.markdown("### 🗓️ Practitioner Action — This Month")
    st.markdown(f"""
<div style="background:#eff6ff;border:1px solid #93c5fd;border-left:5px solid #2563eb;
            border-radius:10px;padding:1.3rem 1.5rem;margin-bottom:1.5rem;">
  <p style="margin:0 0 6px 0;font-size:1.6rem;">{_ex[0]}</p>
  <p style="margin:0 0 8px 0;font-size:1.05rem;font-weight:700;color:#1e3a8a;font-family:'Inter',sans-serif;">{_ex[1]}</p>
  <p style="margin:0;font-size:0.9rem;color:#334155;font-family:'Inter',sans-serif;line-height:1.8;">{_ex[2]}</p>
</div>""", unsafe_allow_html=True)

    _expert_sections = [
        ("⚙️", "Initial Access Vector Analysis — MITRE ATT&CK Mapping",
         "<strong>Stolen credentials (22%)</strong> → T1078 Valid Accounts: enforce conditional access, FIDO2, and UEBA logon anomaly detection. "
         "<strong>Vulnerability exploitation (20%, +34% YoY)</strong> → T1190 Exploit Public-Facing Application: prioritize CISA KEV patch queue — Ivanti Connect Secure, Fortinet FortiOS, Citrix NetScaler dominated 2024 exploitation. "
         "<strong>Phishing (15%)</strong> → T1566.001/002: deploy sandbox detonation on all inbound attachments; enforce DMARC p=reject. "
         "<strong>Edge device exploitation (22%)</strong> → T1133 External Remote Services: ASM tooling to enumerate and reduce internet-exposed management interfaces.",
         "🔍 Detection: alert on new service account logons outside business hours, VPN auth from non-compliant devices, and first-seen ASN logons.",
         "⚔️ Attack Methods"),
        ("🔓", "Ransomware — TTPs, IOCs, and Defensive Architecture",
         "44% breach involvement (2024), up from 25% in 2022. Dominant families: LockBit 3.0, BlackCat/ALPHV, Cl0p, Play. "
         "Double-extortion is now standard: T1048 (Exfiltration over Alternative Protocol) precedes T1486 (Data Encrypted for Impact). "
         "64% refusal-to-pay validates non-payment posture. Recovery depends on: (1) immutable backups — test S3 Object Lock or WORM NAS; "
         "(2) offline restoration validated quarterly; (3) network segmentation limiting blast radius. "
         "SMB orgs (<1k employees) accounted for 88% of ransomware breaches — supply chain risk for enterprise.",
         "🔍 Purple team: simulate T1486 + T1070 (log clearing) + T1562 (disabling security tools). Validate EDR detects VSS deletion (vssadmin delete shadows).",
         "🔓 Ransomware"),
        ("🧩", "MFA Bypass — Detection Engineering and Hardening",
         "Three equally-prevalent bypass methods (~31% each): "
         "<strong>(1) AiTM (Adversary-in-the-Middle)</strong> via Evilginx2/Modlishka — bypasses session cookies; detect via impossible travel, new ASN token issuance, session reuse from different IPs. "
         "<strong>(2) MFA Prompt Bombing</strong> — detect via >3 push denials in 5 min per user; auto-block and alert. "
         "<strong>(3) Token Theft</strong> → T1528: enforce token binding and Continuous Access Evaluation (CAE) in Entra ID / Azure AD. "
         "FIDO2/WebAuthn is resistant to all three bypass methods.",
         "🔍 SIEM rule: alert on MFA method downgrade (FIDO2 → TOTP → SMS) — indicates attacker-controlled account recovery flow.",
         "⚔️ Attack Methods"),
        ("🏭", "ICS/OT Threat Intelligence — Kaspersky ICS-CERT Q2 2025",
         "20.5% of ICS computers globally had threats blocked in Q2 2025. Internet-sourced threats dominate (9.76% of ICS computers reached). "
         "Email-borne threats trending upward (+12.5% since Q4 2024) — reflects increasing IT/OT convergence on engineering workstations. "
         "Spyware and backdoors are highest-severity ICS category — enabling persistent APT-pattern access. "
         "Highest-risk sectors: Building Automation (23.5%), Oil & Gas (17.8%), Energy (17.2%). "
         "OT mitigations: unidirectional gateways (data diodes) for historian replication; application allowlisting on HMI/SCADA; Purdue Model enforcement with Layer 3 segmentation.",
         "🔍 Threat hunt: LOLBins executing on OT workstations (PowerShell, WMIC, certutil in industrial environments) are high-fidelity IOCs for initial staging.",
         "🏭 ICS Threats"),
        ("📊", "Data Exfiltration Targeting — Threat Actor Priorities",
         "Internal documents now rank #1 stolen data type — double-extortion makes confidential files a direct extortion lever (T1005 Data from Local System, T1048 Exfiltration). "
         "Credentials rank #3 — stolen credentials are resold and reused across multiple organizations, creating compounding breach cycles. "
         "Medical records command the highest individual market price (up to $1,000/record) due to immutable PII value. "
         "API keys and secrets (rank #5) enable lateral movement into cloud infrastructure and CI/CD pipelines — a growing target as organizations shift to cloud-native architectures.",
         "🔍 DLP rule priority: alert on bulk download of internal documents + credential file patterns (*.kdbx, credentials.json, .env files) outside business hours.",
         "🗂️ Stolen Data"),
        ("🌐", "Espionage and Nation-State Activity — 163% Surge",
         "External actor-driven espionage breaches increased 163% in 2024 (DBIR 2025). Primary attribution: groups linked to Russia (SVR/Cozy Bear), China (APT40, APT41), Iran (Charming Kitten), North Korea (Lazarus Group). "
         "TTPs: Living-off-the-land (T1218 System Binary Proxy Execution), long dwell times (median 200+ days before detection), and supply chain staging (T1195). "
         "The boundary between organized crime and state-sponsored groups is blurring — GRU-linked groups now operate with financial motives alongside intelligence objectives. "
         "Detection priority: anomalous LSASS access, unusual scheduled task creation, and DNS tunnelling (T1071.004) for C2 communication.",
         "🔍 Threat hunt: search for LOLBin execution chains originating from browser processes — a common initial foothold pattern for spear-phishing-delivered payloads.",
         "📡 Sector Risk"),
    ]

    for icon, title, body, note, label in _expert_sections:
        st.markdown(f"""
<div style="background:#ffffff;border:1px solid #bfdbfe;border-left:4px solid #1d4ed8;border-radius:12px;
            padding:1.3rem 1.5rem;margin-bottom:1rem;
            box-shadow:0 1px 4px rgba(29,78,216,0.07);">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px;">
    <p style="margin:0;font-size:1.3rem;">{icon}</p>
    <span style="font-size:0.72rem;font-weight:600;color:#1d4ed8;background:#eff6ff;
                 border:1px solid #bfdbfe;border-radius:20px;padding:3px 10px;
                 font-family:'Inter',sans-serif;white-space:nowrap;">{label}</span>
  </div>
  <p style="margin:0 0 10px 0;font-size:1rem;font-weight:700;color:#1e3a8a;font-family:'Inter',sans-serif;">{title}</p>
  <p style="margin:0 0 12px 0;font-size:0.88rem;color:#334155;font-family:'Inter',sans-serif;line-height:1.85;">{body}</p>
  <div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:8px;padding:9px 14px;">
    <p style="margin:0;font-size:0.83rem;color:#1d4ed8;font-family:'Inter',sans-serif;font-weight:600;">{note}</p>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Charts for Expert Console ──────────────────────────────────────────
    st.markdown("---")
    st.markdown("### 📊 Supporting Telemetry")
    st.caption("Key charts mapped to TTPs and defensive controls — use alongside the technical notes above.")

    _ex_c1, _ex_c2 = st.columns(2, gap="large")
    with _ex_c1:
        st.markdown("#### Initial Access Vector Distribution")
        st.caption(
            "DBIR 2025 initial access breakdown across 12,195 confirmed breaches. Credential compromise "
            "(phishing, credential stuffing, brute-force) and exploitation of public-facing applications "
            "account for ~42% of initial access entries combined — reinforcing the case for phishing-resistant "
            "MFA and aggressive external attack surface management. Map to MITRE ATT&CK TA0001 sub-techniques "
            "T1078, T1190, and T1566."
        )
        st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)
    with _ex_c2:
        st.markdown("#### MFA Bypass Technique Split")
        st.caption(
            "Adversary-in-the-Middle (AiTM) proxy toolkits (Evilginx2, Modlishka), MFA fatigue / push-bombing, "
            "and post-authentication session token theft each represent roughly equal thirds of MFA bypass "
            "incidents. Detection priority: monitor for impossible-travel sign-in events, anomalous OAuth token "
            "grants, and high-volume push notification bursts per-user within short windows."
        )
        st.plotly_chart(fig_mfa, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)

    st.markdown("#### Weekly Exploitation Trend by Attack Category (12-Week Window)")
    st.caption(
        "12-week rolling telemetry across attack categories. Remote-access exploitation (VPN appliances, "
        "RDP, SSH brute-force) is the only vector on a statistically significant upward trajectory — "
        "correlates with mass-exploitation of CVEs in edge devices (Ivanti, Palo Alto, Cisco ASA). "
        "Prioritise patching internet-facing remote-access infrastructure and review conditional-access "
        "policies restricting legacy authentication protocols."
    )
    st.plotly_chart(fig_trends, use_container_width=True, config={"displayModeBar": False})
    st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)

    _ex_c3, _ex_c4 = st.columns(2, gap="large")
    with _ex_c3:
        st.markdown("#### ICS Threat Rate by Region — Q2 2025")
        st.caption(
            "Kaspersky ICS-CERT telemetry: percentage of ICS/SCADA endpoints where at least one malicious "
            "object was blocked during Q2 2025. Africa and Southeast Asia show the highest rates (>40%), "
            "likely reflecting lower EDR/OT-security maturity and delayed patch cycles on engineering "
            "workstations. Cross-reference against your OT network segments and evaluate compensating "
            "controls (network segmentation, application whitelisting on HMIs)."
        )
        st.plotly_chart(fig_ics_region, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025</p>', unsafe_allow_html=True)
    with _ex_c4:
        st.markdown("#### ICS Historical Quarterly Trend")
        st.caption(
            "Quarterly ICS threat volume from Kaspersky ICS-CERT. The Q2 2025 uptick follows a trough in "
            "Q4 2024, consistent with seasonal threat actor activity patterns and increased targeting of "
            "energy and manufacturing sectors post-winter. Use this trend as a leading indicator when "
            "scheduling OT vulnerability assessments and threat-hunting exercises."
        )
        st.plotly_chart(fig_ics_hist, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025</p>', unsafe_allow_html=True)

# ─────────────────────────────────────────
# EXECUTIVE BRIEF — For Business Leaders
# ─────────────────────────────────────────
elif _chosen_key == "exec":
    st.markdown(f"""
<div style="background:linear-gradient(135deg,#f0fdf4 0%,#f8fafc 100%);
            border:1px solid #bbf7d0;border-radius:16px;
            padding:2rem 2.4rem 1.6rem 2.4rem;margin-bottom:1.4rem;
            box-shadow:0 2px 12px rgba(22,163,74,0.07);">
  <p style="margin:0 0 0.4rem 0;font-size:0.8rem;font-weight:700;letter-spacing:0.08em;
            color:#15803d;text-transform:uppercase;font-family:'Inter',sans-serif;">
    💼 Executive Brief · Board & Leadership View
  </p>
  <h2 style="margin:0 0 0.6rem 0;font-size:1.7rem;font-weight:800;color:#0f172a;
             font-family:'Inter',sans-serif;border:none;padding:0;margin-top:0;">
    Cyber Risk in Business Terms — What Leaders Need to Know
  </h2>
  <p style="margin:0;font-size:1rem;color:#475569;font-family:'Inter',sans-serif;line-height:1.7;max-width:780px;">
    Translated from 22,052 incidents and 12,195 confirmed breaches into financial exposure,
    regulatory obligations, and strategic actions for C-suite and board audiences.
  </p>
</div>
""", unsafe_allow_html=True)

    _ex1, _ex2, _ex3, _ex4 = st.columns(4)
    _ex1.metric("Avg. Breach Cost (Global)", "$4.9M USD", "IBM Cost of a Breach 2024", delta_color="inverse")
    _ex2.metric("Ransomware Involvement", "44%", "↑76% since 2022", delta_color="inverse")
    _ex3.metric("Third-Party Breaches", "30%", "↑100% YoY", delta_color="inverse")
    _ex4.metric("Victims Refusing to Pay", "64%", "↑28% vs 2022")

    _exec_tips = {
        1:  ("📋", "January: Review Your Cyber Insurance Coverage",
             "Tax season brings heightened Business Email Compromise risk — $6.3B in BEC losses were recorded in 2024. "
             "Verify your cyber insurance policy covers BEC-related financial losses (many policies exclude social engineering by default). "
             "Confirm that your insurer requires MFA as a coverage condition — and that your organization is compliant."),
        2:  ("🤝", "February: Assess Third-Party Vendor Risk",
             "30% of breaches now involve a third party — doubled year over year. "
             "Request SOC 2 Type II reports from your top 10 vendors by data access volume. "
             "Ensure vendor contracts include mandatory breach notification timelines and right-to-audit clauses."),
        3:  ("📊", "March: Brief Your Board on Ransomware Exposure",
             "Manufacturing boards should note that 47% of breaches in their sector involve ransomware. "
             "Quantify your organization's downtime cost per hour — this is the number ransomware actors use to set their demand. "
             "Ensure the board has approved an incident response retainer with a reputable IR firm before an incident occurs."),
        4:  ("🏢", "April: Establish a Patch Governance KPI",
             "Vulnerability exploitation increased 34% year over year and now equals stolen credentials as a top entry point. "
             "Establish a board-visible KPI for mean time to patch critical vulnerabilities. "
             "Require your CISO to report patch compliance against the CISA Known Exploited Vulnerabilities catalogue quarterly."),
        5:  ("⚖️", "May: Review Your Privacy Breach Obligations",
             "Personal data and credentials are among the top stolen data categories. "
             "Under PIPEDA, organizations must report breaches posing real risk of significant harm to the Office of the Privacy Commissioner. "
             "Quebec Law 25 introduced GDPR-equivalent obligations including 72-hour regulatory notification. Assign a named Privacy Officer now."),
        6:  ("🌐", "June: Map Your Supply Chain Security Exposure",
             "Supply chain breaches give attackers access to dozens of organizations through a single vendor compromise. "
             "Map your critical vendors and assess whether a compromise of any one could affect your operations or clients' data. "
             "Consider requiring vendors to complete the CIS Controls Self-Assessment annually."),
        7:  ("📅", "July: Confirm Holiday Business Continuity Planning",
             "December sees a 30% ransomware surge — planning must start months in advance. "
             "Ensure business continuity plans define minimum viable operations and recovery time objectives. "
             "Confirm that incident response authority is clearly delegated for when key executives are unavailable."),
        8:  ("🎓", "August: Invest in Security Awareness Training",
             "Human judgement failures remain a top attack vector. Security-aware employees are your most cost-effective control. "
             "Mandate phishing simulation training for all staff — organizations running quarterly simulations report 50–70% reductions in click rates. "
             "Prioritize role-based training for finance, HR, and executive assistants — the highest-value Business Email Compromise targets."),
        9:  ("📱", "September: Strengthen Authentication Governance",
             "MFA bypass techniques now affect 1 in 3 MFA-protected accounts. "
             "Direct your CISO to upgrade high-value accounts to phishing-resistant MFA (hardware security keys). "
             "Include authentication standards in your vendor security requirements and supplier onboarding process."),
        10: ("🔐", "October: Commission a Ransomware Readiness Assessment",
             "October is Cybersecurity Awareness Month — and ransomware is now involved in 44% of all breaches. "
             "Commission an independent ransomware readiness assessment covering backup integrity, detection coverage, and response capability. "
             "Share the findings with your cyber insurance broker — it may reduce your premium."),
        11: ("🛒", "November: Protect Peak-Season Revenue",
             "Ransomware groups deliberately time attacks to coincide with peak revenue periods — Black Friday and Cyber Monday. "
             "Define a revenue-impact threshold that triggers executive notification and crisis management protocols. "
             "Ensure e-commerce infrastructure is included in scope for your next penetration test."),
        12: ("🎄", "December: Present the Annual Cyber Risk Report to the Board",
             "Present a year-end cyber risk summary covering incidents year-to-date, threat landscape changes "
             "(ransomware +76% since 2022, espionage +163%), and planned investments for the coming year. "
             "Frame cyber investment as risk quantification — use the FAIR model to express risk in dollar terms the board can act on."),
    }
    _ec = _exec_tips[datetime.datetime.now().month]
    st.markdown("### 🗓️ Leadership Priority — This Month")
    st.markdown(f"""
<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-left:5px solid #16a34a;
            border-radius:10px;padding:1.3rem 1.5rem;margin-bottom:1.5rem;">
  <p style="margin:0 0 6px 0;font-size:1.6rem;">{_ec[0]}</p>
  <p style="margin:0 0 8px 0;font-size:1.05rem;font-weight:700;color:#0f172a;font-family:'Inter',sans-serif;">{_ec[1]}</p>
  <p style="margin:0;font-size:0.93rem;color:#334155;font-family:'Inter',sans-serif;line-height:1.75;">{_ec[2]}</p>
</div>
""", unsafe_allow_html=True)

    _exec_sections = [
        ("📊", "Financial Exposure by Sector",
         "Manufacturing organizations face a 47% ransomware involvement rate — and Operational Technology downtime can cost $100K–$500K per hour for large plants. "
         "Healthcare breaches average the highest cost of any sector globally at $9.8M USD per breach (IBM 2024), driven by regulatory fines, litigation, and operational disruption. "
         "Finance, while heavily targeted (927 breaches), has the lowest ransomware rate (18%) due to investment in segmentation and offline backups — a model other sectors should replicate. "
         "Business Email Compromise generated $6.3B in direct financial losses in 2024 — the single highest-value cybercrime category by dollar impact.",
         "💼 Board benchmark: compare your sector's average breach cost against your current security investment. Industry standard is 10–15% of the total IT budget.",
         "📡 Sector Risk"),
        ("⚖️", "Regulatory and Legal Obligations — Canada",
         "Canadian organizations are subject to PIPEDA (federal) and provincial privacy laws (Quebec Law 25, Alberta PIPA, BC PIPA). "
         "A breach involving personal data triggers mandatory notification to the Office of the Privacy Commissioner and affected individuals when there is real risk of significant harm. "
         "Failure to maintain a breach log or report can result in fines up to $100,000 per violation under PIPEDA. "
         "Quebec Law 25 introduced GDPR-equivalent obligations — including 72-hour regulatory notification and mandatory privacy impact assessments for new technology projects. "
         "Third-party breaches do not reduce your regulatory liability — you remain responsible for data shared with vendors.",
         "💼 Action: Appoint a named Privacy Officer, maintain a breach log, and test your notification process before an incident forces you to use it.",
         "🗂️ Stolen Data"),
        ("🤝", "Third-Party and Supply Chain Risk — The Fastest-Growing Threat",
         "The 100% year-over-year increase in third-party breaches is the most urgent trend for executive teams. "
         "A single compromised vendor credential can provide attackers access to your systems, your clients' data, and your intellectual property simultaneously. "
         "The SolarWinds, MOVEit, and Change Healthcare incidents are examples — each affected thousands of downstream organizations through a single supply chain entry point. "
         "Due diligence actions: annual vendor security questionnaires, contractual breach notification requirements (72-hour notice standard), "
         "and limiting vendor access to only what is necessary (least-privilege principle).",
         "💼 Board question for your CISO: 'What is the worst-case impact if our top three vendors by data access were compromised simultaneously?'",
         "⚔️ Attack Methods"),
        ("🏭", "Industrial and Critical Infrastructure — Direct Operational Risk",
         "20.5% of industrial control system computers globally faced active cyber threats in Q2 2025. "
         "For organizations operating or depending on industrial infrastructure (manufacturing, energy, utilities, building management), "
         "this represents a direct operational continuity risk — not merely a data risk. "
         "A cyberattack on Operational Technology systems can cause physical disruption including equipment damage, production halts, "
         "and in critical infrastructure, public safety impacts. "
         "Cyber-physical incidents are increasingly covered under 'contingent business interruption' clauses — verify your policy explicitly covers OT disruption.",
         "💼 Board priority: ensure your business continuity plan explicitly addresses OT/ICS disruption scenarios — not just IT outages.",
         "🏭 ICS Threats"),
        ("🌍", "Geopolitical Cyber Risk — Espionage Surged 163%",
         "Nation-state actors dramatically increased targeting of intellectual property and critical infrastructure in 2024. "
         "The boundary between organized crime and state-sponsored hacking is blurring — some groups operate freely in exchange for intelligence-sharing with their governments. "
         "Primary state actors: groups linked to Russia, China, Iran, and North Korea. Targets: government contractors, research institutions, energy companies, and financial services. "
         "For organizations with government contracts, proprietary research, or cross-border operations, espionage risk is now a board-level governance issue — not solely an IT concern.",
         "💼 Action: Include geopolitical cyber risk in your enterprise risk register and discuss threat actor targeting of your sector with your CISO annually.",
         "📡 Sector Risk"),
    ]

    for icon, title, body, action, label in _exec_sections:
        st.markdown(f"""
<div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;
            padding:1.3rem 1.5rem;margin-bottom:1rem;
            box-shadow:0 1px 4px rgba(0,0,0,0.05);">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px;">
    <p style="margin:0;font-size:1.3rem;">{icon}</p>
    <span style="font-size:0.72rem;font-weight:600;color:#15803d;background:#f0fdf4;
                 border:1px solid #bbf7d0;border-radius:20px;padding:3px 10px;
                 font-family:'Inter',sans-serif;white-space:nowrap;">{label}</span>
  </div>
  <p style="margin:0 0 10px 0;font-size:1rem;font-weight:700;color:#0f172a;font-family:'Inter',sans-serif;">{title}</p>
  <p style="margin:0 0 12px 0;font-size:0.92rem;color:#334155;font-family:'Inter',sans-serif;line-height:1.8;">{body}</p>
  <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:9px 14px;">
    <p style="margin:0;font-size:0.86rem;color:#1d4ed8;font-family:'Inter',sans-serif;font-weight:500;">{action}</p>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Charts for Executive Brief ─────────────────────────────────────────
    st.markdown("---")
    st.markdown("### 📊 Key Charts for Leadership")
    st.caption("Strategic-level visualisations to support board reporting and risk committee briefings.")

    _eb_c1, _eb_c2 = st.columns(2, gap="large")
    with _eb_c1:
        st.markdown("#### Sector Breach Exposure Radar")
        st.caption(
            "This radar chart maps relative cyber risk across major industries. A larger shape means "
            "higher exposure. Finance and Healthcare show consistently elevated risk due to the high "
            "value of the data they hold. Use this to benchmark your sector's risk profile and "
            "prioritise investment in the control areas where your industry scores highest."
        )
        st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)
    with _eb_c2:
        st.markdown("#### Ransomware Trend: Rising Threat, Rising Refusal")
        st.caption(
            "Ransomware involvement in breaches has nearly doubled over three years — now affecting 44% "
            "of all incidents. The positive signal is that 64% of victims chose not to pay the ransom in "
            "2024, up from 50% in 2022. Organisations with tested backup and recovery plans are driving "
            "this shift. The business case for investing in resilience — not just prevention — is clear."
        )
        st.plotly_chart(fig_fore, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)

    _eb_c3, _eb_c4 = st.columns(2, gap="large")
    with _eb_c3:
        st.markdown("#### Who Is Behind the Attacks?")
        st.caption(
            "Roughly 80% of breaches are carried out by external criminal organisations motivated by "
            "financial gain — not nation-states. This is relevant for risk quantification: these actors "
            "follow the money, targeting organisations with weak controls or valuable data. "
            "A smaller but growing share involves insiders or business partners with legitimate access, "
            "highlighting the importance of access governance and vendor risk management."
        )
        st.plotly_chart(fig_act, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Verizon 2025 Data Breach Investigations Report (DBIR)</p>', unsafe_allow_html=True)
    with _eb_c4:
        st.markdown("#### ICS Attack Rate by Region")
        st.caption(
            "1 in 5 industrial computers globally had a threat blocked in Q2 2025. For organisations "
            "with manufacturing, logistics, or utilities operations, this represents direct operational "
            "and safety risk — not just data loss. Regions with the highest rates often correspond to "
            "facilities with older operational technology. Boards should ask: are our industrial "
            "systems on a separate, monitored network?"
        )
        st.plotly_chart(fig_ics_region, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<p style="font-size:0.72rem;color:#94a3b8;font-family:\'Inter\',sans-serif;margin-top:-10px;">Source: Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025</p>', unsafe_allow_html=True)

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.divider()
st.markdown(f"""
<div style="text-align:center;padding:1.6rem;background:{SURFACE};
            border:1px solid {BORDER};border-radius:12px;margin-top:1rem;">
  <p style="color:{MUTED};font-size:0.82rem;line-height:2;margin:0;font-family:'Inter',sans-serif;">
    <strong style="color:{TEXT};">Data Sources:</strong>
    Verizon 2025 Data Breach Investigations Report (DBIR) ·
    22,052 incidents · 12,195 confirmed breaches · Nov 2023 – Oct 2024
    &nbsp;·&nbsp;
    Kaspersky ICS-CERT — Threat Landscape for Industrial Automation Systems, Q2 2025 ·
    ics-cert.kaspersky.com
    <br/>
    <strong style="color:{TEXT};">CyberSignals</strong> ·
    Industrial Cyber Risk Radar · Team N5 · USI4280 ·
    All charts rendered from DBIR and Kaspersky ICS-CERT data · No placeholder images
  </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# CREATORS  (alphabetical by last name)
# ─────────────────────────────────────────
authors = [
    ("Ayaan Bajwa",            "https://www.linkedin.com/in/ayaan-bajwa-695a93265/"),
    ("Saaketh Potluri",        "https://www.linkedin.com/in/saaketh-potluri/"),
    ("Chinmaya S. Ramani",     "https://www.linkedin.com/in/chinmaya-ramani-b89308254"),
    ("Sangeethan Thevathasan", "https://www.linkedin.com/in/sangeethan-thevathasan-1b8484217/?originalSubdomain=ca"),
    ("Shalin Vaidya",          "https://www.linkedin.com/in/shalin-vaidya/"),
]

author_cards = "".join([f"""
  <div style="
    display:flex;align-items:center;gap:6px;
    background:{SURFACE};border:1px solid {BORDER};border-radius:6px;
    padding:6px 10px;flex:1;min-width:190px;
  ">
    <p style="margin:0;font-size:0.75rem;font-weight:500;color:{TEXT};
              font-family:'Inter',sans-serif;word-break:break-word;">{name}</p>
    <a href="{url}" target="_blank" style="margin-left:auto;flex-shrink:0;
       display:flex;align-items:center;justify-content:center;
       width:22px;height:22px;border-radius:5px;
       background:#e8f0fe;border:1px solid rgba(10,102,194,0.18);"
       title="LinkedIn">
      {LI_LOGO}
    </a>
  </div>""" for name, url in authors])

st.markdown(f"""
<div style="margin-top:0.5rem;">
  <p style="font-size:0.65rem;color:{MUTED};font-family:'Inter',sans-serif;
             margin-bottom:6px;font-weight:500;">Creators</p>
  <div style="display:flex;flex-wrap:wrap;gap:6px;">
    {author_cards}
  </div>
</div>
""", unsafe_allow_html=True)