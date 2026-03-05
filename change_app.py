import streamlit as st
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif !important;
    background-color: {BG} !important;
    color: {TEXT} !important;
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
    font-weight: 700 !important;
    font-size: 2.4rem !important;
    color: {TEXT} !important;
    letter-spacing: 0 !important;
    line-height: 1.25 !important;
    margin-bottom: 0.5rem !important;
}}
h2 {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.35rem !important;
    color: {TEXT} !important;
    margin-top: 3rem !important;
    margin-bottom: 1.2rem !important;
    padding-bottom: 0.7rem !important;
    border-bottom: 1px solid {BORDER2} !important;
    letter-spacing: 0 !important;
}}
h3 {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    color: {TEXT} !important;
    margin-top: 0 !important;
    margin-bottom: 0.5rem !important;
    letter-spacing: 0 !important;
}}
h4 {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    color: {MUTED} !important;
    margin-top: 0 !important;
    margin-bottom: 0.4rem !important;
    letter-spacing: 0 !important;
    text-transform: uppercase !important;
    font-size: 0.72rem !important;
}}
p, .stMarkdown p {{
    font-family: 'Inter', sans-serif !important;
    color: {TEXT} !important;
    font-size: 0.95rem !important;
    line-height: 1.75 !important;
}}
[data-testid="stCaptionContainer"] p {{
    color: {MUTED} !important;
    font-size: 0.86rem !important;
    line-height: 1.6 !important;
}}

/* ── CHART CARD SHADOW ── */
.js-plotly-plot {{
    border-radius: 10px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.07), 0 4px 16px rgba(0,0,0,0.06) !important;
    overflow: hidden !important;
}}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {{
    background-color: {SURFACE} !important;
    border-right: 1px solid {BORDER2} !important;
}}
[data-testid="stSidebar"] .block-container {{
    background: transparent !important;
    padding: 1.5rem 1.2rem !important;
}}
[data-testid="stSidebar"] h2 {{
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: {ACCENT} !important;
    border-bottom: 1px solid {BORDER2} !important;
    padding-bottom: 0.5rem !important;
    margin-bottom: 1.2rem !important;
}}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {{
    color: {TEXT} !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
}}
[data-testid="stSidebar"] .stMarkdown h5 {{
    color: {MUTED} !important;
    font-size: 0.7rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    margin: 1.2rem 0 0.4rem 0 !important;
}}
[data-testid="stSidebar"] .stMultiSelect > div > div,
[data-testid="stSidebar"] .stSelectbox > div > div {{
    background-color: {BG} !important;
    border: 1px solid {BORDER2} !important;
    border-radius: 6px !important;
    color: {TEXT} !important;
}}
/* multiselect selected tags (chips) */
[data-testid="stSidebar"] [data-baseweb="tag"] {{
    background-color: rgba(37,99,235,0.1) !important;
    border: 1px solid rgba(37,99,235,0.3) !important;
    border-radius: 4px !important;
    color: {ACCENT} !important;
}}
[data-testid="stSidebar"] [data-baseweb="tag"] span {{
    color: {ACCENT} !important;
    font-size: 0.78rem !important;
}}
[data-testid="stSidebar"] [data-baseweb="tag"] svg {{
    fill: {ACCENT} !important;
}}
/* dropdown popup list */
[data-baseweb="popover"] ul {{
    background-color: {BG} !important;
    border: 1px solid {BORDER2} !important;
}}
[data-baseweb="popover"] li {{
    background-color: {BG} !important;
    color: {TEXT} !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
}}
[data-baseweb="popover"] li:hover {{
    background-color: {SURFACE} !important;
}}
/* multiselect input text */
[data-testid="stSidebar"] [data-baseweb="input"] input {{
    color: {TEXT} !important;
    font-family: 'Inter', sans-serif !important;
    background-color: transparent !important;
}}
[data-testid="stSidebar"] [data-testid="stNotificationContentInfo"] {{
    background-color: rgba(37,99,235,0.06) !important;
    border: 1px solid rgba(37,99,235,0.2) !important;
    border-left: 3px solid {ACCENT} !important;
    color: {TEXT} !important;
    border-radius: 6px !important;
    font-size: 0.8rem !important;
}}

/* ── METRICS ── */
[data-testid="metric-container"] {{
    background: {BG} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 10px !important;
    padding: 1rem 1.2rem !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}}
[data-testid="metric-container"] label {{
    color: {MUTED} !important;
    font-size: 0.72rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    font-family: 'Inter', sans-serif !important;
}}
[data-testid="metric-container"] [data-testid="stMetricValue"] {{
    font-family: 'Syne', sans-serif !important;
    font-size: 1.7rem !important;
    font-weight: 800 !important;
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
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 0.01em;
    white-space: nowrap;
    pointer-events: none;
}}
/* keep Streamlit's own toolbar buttons visible */
[data-testid="stHeader"] button,
[data-testid="stHeader"] a,
[data-testid="stHeader"] [data-testid="stDecoration"] {{
    position: relative;
    z-index: 1;
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

# ─────────────────────────────────────────
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
def source_badge(extra=""):
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
  <span style="font-family:'Inter',sans-serif;font-size:0.88rem;font-weight:600;color:{TEXT};">
    Source: <a href="https://www.verizon.com/business/resources/reports/dbir/" target="_blank"
      style="color:{ACCENT};text-decoration:none;">Verizon 2025 Data Breach Investigations Report (DBIR)</a>
    <span style="color:{MUTED};font-weight:400;"> · Nov 2023 – Oct 2024{detail}</span>
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
  <p style="margin:0 0 5px 0;font-size:0.9rem;font-weight:600;color:{TEXT};">💡 {headline}</p>
  <p style="margin:0;font-size:0.86rem;color:{MUTED};line-height:1.75;">{body}</p>
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
  <p style="margin:0 0 6px 0;font-size:0.88rem;font-weight:600;color:{TEXT};">💡 {headline}</p>
  <p style="margin:0;font-size:0.82rem;color:{MUTED};line-height:1.75;">{body}</p>
</div>""", unsafe_allow_html=True)
        if extended:
            st.markdown(f"""
<div style="padding:14px 18px;background:#eff6ff;border:1px solid #bfdbfe;
            border-left:4px solid {ACCENT};border-radius:0 8px 8px 0;
            font-family:'Inter',sans-serif;">
  <p style="margin:0 0 6px 0;font-size:0.88rem;font-weight:600;color:{ACCENT};">🔍 Deeper Dive</p>
  <p style="margin:0;font-size:0.82rem;color:{TEXT};line-height:1.75;">{extended}</p>
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
st.sidebar.header("Filters & Controls")
st.sidebar.markdown("##### Sector Selection")
selected_sectors = st.sidebar.multiselect(
    "Sector",
    ["Finance","Manufacturing","Healthcare","Professional Services","Public Administration",
     "Information","Education","Retail","Wholesale","Transportation",
     "Utilities","Construction","Real Estate","Entertainment","Other Services"],
    default=["Finance","Manufacturing","Healthcare","Professional Services","Public Administration"],
)
st.sidebar.markdown("##### Time Period")
st.sidebar.selectbox("Time Range",
    ["Nov 2023 – Oct 2024 (DBIR 2025)","Last 12 months","Last Quarter"])
st.sidebar.markdown("##### Threat Category")
st.sidebar.selectbox("Threat Type",
    ["All","Ransomware","Social Engineering","Vulnerability Exploitation",
     "Data Theft","Supply Chain Attack","Denial of Service"])
st.sidebar.markdown("<em>Other filters are decorative — only sector selection is wired up.</em>", unsafe_allow_html=True)
st.sidebar.info(
    "**Source:** Verizon 2025 DBIR\n\n"
    "22,052 incidents · 12,195 confirmed breaches\n\n"
    "Nov 2023 – Oct 2024"
)

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
    Team N5 · USI4280
  </div>
</div>
""", unsafe_allow_html=True)

st.title("🛡️ CyberSignals")
st.caption(
    "Sector-level cyber risk radar · 22,052 incidents · "
    "12,195 confirmed breaches · Nov 2023 – Oct 2024"
)
st.markdown(
    "Tracks **which sectors are under pressure**, **what is driving risk**, "
    "and **what actions to take next** — powered by DBIR 2025 CSV data."
)
st.markdown(
    f'<p style="font-size:0.8rem;color:{MUTED};font-family:\'Inter\',sans-serif;margin-top:-8px;">'
    "💡 <strong>Tip:</strong> Hover over any chart and click the <strong>⤢ expand icon</strong> "
    "in the top-right corner to view it full screen.</p>",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────
# KPI ROW
# ─────────────────────────────────────────
st.markdown("## Key Risk Metrics")
m1,m2,m3,m4,m5 = st.columns(5)
m1.metric("Total Incidents",        "22,052",  "Nov'23–Oct'24")
m2.metric("Confirmed Breaches",     "12,195",  "DBIR 2025")
m3.metric("Ransomware in Breaches", "44%",     "↑37% Year-over-Year",  delta_color="inverse")
m4.metric("Vulnerability Exploitation",    "20%",     "↑34% Year-over-Year",  delta_color="inverse")
m5.metric("Third-Party Breaches",   "30%",     "↑100% Year-over-Year", delta_color="inverse")

# ─────────────────────────────────────────
# SECTION 1 — RADAR + INCIDENT PRESSURE
# ─────────────────────────────────────────
st.markdown("## Which Sectors Are Most at Risk?")
filtered = df_industry[df_industry["Industry"].isin(selected_sectors)]
if selected_sectors and filtered.empty:
    st.warning("No sectors selected – showing all sectors instead.")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### Breach Exposure by Sector")
    st.caption("Each spoke shows how hard a sector was hit — normalized across 12,195 confirmed breaches")
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
                 "to nearly 1 in 2 by 2024. However, the rising refusal-to-pay rate (now 64%) shows organisations "
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
st.markdown("## How Attacks Happen")
st.caption("The most common attack patterns — and how many of those incidents turn into real breaches")

col5, col6 = st.columns([3,2], gap="large")

with col5:
    st.markdown("#### Most Common Attack Patterns")
    fig_pat = go.Figure()
    fig_pat.add_trace(go.Bar(
        y=df_patterns["Pattern"], x=df_patterns["Incidents"],
        name="Incidents",
        orientation="h",
        marker=dict(color=C_BLUE, opacity=0.80, line=dict(color="white", width=0.5)),
        text=[f"{v:,}" for v in df_patterns["Incidents"]],
        textposition="outside",
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
        textfont=dict(size=10, color=TEXT, family="Inter, sans-serif"),
        hovertemplate="<b>%{y}</b><br>Confirmed Breaches: <b>%{x:,}</b><extra></extra>",
    ))
    # Callout annotation for the near-invisible "2 breaches" bar (Denial of Service)
    fig_pat.add_annotation(
        y="Denial of Service", x=400,
        text="★ Only 2 confirmed breaches",
        showarrow=True, arrowhead=2, arrowcolor=C_RED, arrowwidth=1.5,
        ax=160, ay=28,
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
        "margin": dict(l=56, r=80, t=36, b=56),
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
                "an exposed IP address. Organisations with long patch cycles are particularly exposed, especially "
                "if they use End-of-Life network appliances.")
    _ext_pie = ("Each slice represents a different attack philosophy. Stolen credentials require the least technical "
                "skill — credentials are bought cheaply on criminal marketplaces and tried at scale (credential "
                "stuffing). Vulnerability exploitation is increasingly automated; scanning tools identify exposed "
                "appliances within minutes of a patch being published, and many organisations take weeks to apply "
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
st.markdown("## Ransomware & Who Is Behind Attacks")
col7, col8 = st.columns(2, gap="large")

with col7:
    st.markdown("#### Ransomware Involvement Rate by Industry Sector")
    st.caption("Percentage of breaches in each sector that involved ransomware · Green = below average · Orange = elevated · Red = high")
    bar_colors = [C_GREEN if v < 40 else (C_AMBER if v < 60 else C_RED)
                  for v in df_ransom_sector["Ransomware (%)"]]
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
               "this line face elevated risk and should prioritise offline backup testing, network segmentation, "
               "and incident response planning. Sectors below the line are not immune — Finance's 18% still "
               "represents hundreds of incidents globally. The colour coding (green/orange/red) reflects deviation "
               "from that 44% average. The most actionable insight: if your organisation is in Education or "
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
                "between organised crime and state-sponsored hacking is blurring: some groups operate freely in "
                "exchange for intelligence-sharing with their governments. For organisations, this means attacks "
                "are better-resourced, more patient, and harder to detect than purely financial attacks.")
    _ext_act = ("External actors dominate breaches because they have the greatest motivation, resources, and "
                "scale. However, the 20% internal figure is deceptively significant — insider threats cause "
                "disproportionate damage because insiders already have authorised access and can bypass perimeter "
                "controls entirely. Malicious insiders are often motivated by financial gain (selling data to "
                "competitors or criminal groups) or grievance. Partner and third-party breaches are the fastest-"
                "growing category: supply chain compromises give attackers access to dozens of organisations "
                "through a single point of entry — one compromised vendor credential can open doors across an "
                "entire partner ecosystem. State-sponsored actors at 15% are often the hardest to detect and "
                "remove — they operate with long time horizons, prioritise stealth over speed, and are backed "
                "by substantial intelligence resources.")
    st.markdown(source_badge(_src_act), unsafe_allow_html=True)
    st.markdown(insight_box(_hl_act, _bd_act), unsafe_allow_html=True)
    open_analysis_btn("threat_actors", fig_act, "Who Is Behind the Attacks?",
                      _src_act, _hl_act, _bd_act, _ext_act)

# ─────────────────────────────────────────
# SECTION 5 — DATA TYPES + MFA BYPASS
# ─────────────────────────────────────────
st.markdown("## What Gets Stolen and How Attackers Bypass Security Controls")
col9, col10 = st.columns(2, gap="large")

with col9:
    st.markdown("#### Most Commonly Stolen Data")
    st.caption("Ranked by how often each data type appears in confirmed breach incidents")
    data_colors = [C_BLUE if v >= 7 else (C_PURP if v >= 5 else "#94a3b8")
                   for v in df_data["Relative Prevalence"]]
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
               "logins can be resold dozens of times and used across multiple organisations.")
    _ext_dt = ("Understanding what attackers steal reveals what they value most. Internal documents (contracts, "
               "M&A plans, strategic roadmaps) are highly prized by both financial criminals and nation-state actors "
               "— publishing them creates regulatory, reputational, and competitive damage independent of any ransom "
               "payment. Personal data retains value because it is resold for identity fraud, synthetic identity "
               "creation, and targeted phishing. Medical records command the highest individual price — up to $1,000 "
               "per record — because they contain immutable identifiers (date of birth, health history) that cannot "
               "be changed like a credit card number. Credentials are the 'key' category: stolen credentials feed "
               "directly into future attacks, creating a compounding risk cycle. An organisation that loses "
               "credentials in one breach may find them used to breach a partner organisation months later. "
               "Payment card data, while historically the top target, has declined in relative value as card "
               "networks improve real-time fraud detection.")
    st.markdown(source_badge(_src_dt), unsafe_allow_html=True)
    st.markdown(insight_box(_hl_dt, _bd_dt), unsafe_allow_html=True)
    open_analysis_btn("data_types", fig_dt, "Most Commonly Stolen Data",
                      _src_dt, _hl_dt, _bd_dt, _ext_dt)

with col10:
    st.markdown("#### How Attackers Bypass Multi-Factor Authentication")
    st.caption("Three techniques, each accounting for roughly one-third of Multi-Factor Authentication bypass incidents")
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
st.markdown("## How Exploitation Trends Have Shifted Over 12 Weeks")
st.caption("Weekly incident volume by exploitation type — hover over the chart to compare categories")

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
           "continue rising as more organisations extend Virtual Private Network access to contractors and "
           "remote workers without enforcing the same security controls applied to full-time employees. "
           "Legacy and Unpatched Systems are climbing steadily — this reflects a structural problem: "
           "as software libraries age and vendors end support, the pool of unpatched, exploitable systems "
           "grows faster than organisations can remediate. Misconfiguration is declining slightly — cloud "
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
# FOOTER
# ─────────────────────────────────────────
st.divider()
st.markdown(f"""
<div style="text-align:center;padding:1.6rem;background:{SURFACE};
            border:1px solid {BORDER};border-radius:12px;margin-top:1rem;">
  <p style="color:{MUTED};font-size:0.82rem;line-height:2;margin:0;font-family:'Inter',sans-serif;">
    <strong style="color:{TEXT};">Data Source:</strong>
    Verizon 2025 Data Breach Investigations Report (DBIR) ·
    22,052 incidents · 12,195 confirmed breaches · Nov 2023 – Oct 2024
    <br/>
    <strong style="color:{TEXT};">CyberSignals</strong> ·
    Industrial Cyber Risk Radar · Team N5 · USI4280 ·
    All charts rendered from DBIR CSV data · No placeholder images
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
    padding:6px 10px;flex:1;min-width:130px;
  ">
    <p style="margin:0;font-size:0.75rem;font-weight:500;color:{TEXT};
              font-family:'Inter',sans-serif;white-space:nowrap;">{name}</p>
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
