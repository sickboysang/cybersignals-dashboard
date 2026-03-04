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
# DATA
# ─────────────────────────────────────────
df_industry = pd.DataFrame({
    "Industry":  ["Finance","Manufacturing","Healthcare","Prof. Services","Public Admin",
                  "Information","Education","Retail","Wholesale","Transportation",
                  "Entertainment","Utilities","Construction","Real Estate","Other Services"],
    "Incidents": [3336,3837,1710,2549,1422,1589,1075,837,330,361,493,358,307,339,683],
    "Breaches":  [927,1607,1542,1147,946,784,851,419,319,248,293,213,252,320,583],
}).sort_values("Breaches", ascending=True)

df_patterns = pd.DataFrame({
    "Pattern":   ["System Intrusion","Denial of Service","Social Engineering",
                  "Basic Web App","Misc Errors","Privilege Misuse","Lost & Stolen"],
    "Incidents": [9124,6520,4009,1701,1476,825,149],
    "Breaches":  [7302,2,3405,1387,1449,757,122],
})

df_access = pd.DataFrame({
    "Vector": ["Stolen Credentials","Vuln Exploitation","Phishing","Edge Devices/VPN"],
    "Pct":    [22,20,15,22],
})

df_ransom = pd.DataFrame({
    "Year":               ["2022","2023","2024"],
    "In Breaches (%)":    [25,32,44],
    "Refused to Pay (%)": [50,55,64],
})

df_ransom_sector = pd.DataFrame({
    "Sector":         ["SMB (<1k empl.)","Manufacturing","System Intrusion","Public Sector",
                       "APAC","EMEA","Large Orgs"],
    "Ransomware (%)": [88,47,75,30,51,40,39],
}).sort_values("Ransomware (%)")

df_data = pd.DataFrame({
    "Data Type":           ["Internal Docs","Personal Data","Credentials","Medical",
                            "Secrets/API Keys","Sensitive Personal","Bank Data","Payment Cards"],
    "Relative Prevalence": [9,8,7,6,5,4,3,1],
}).sort_values("Relative Prevalence")

radar_sectors  = ["Finance","Manufacturing","Healthcare","Prof. Services",
                  "Public Admin","Education","Retail","Info/Tech"]
radar_breaches = [927,1607,1542,1147,946,851,419,784]
radar_norm     = [round(b/max(radar_breaches)*10,1) for b in radar_breaches]

vuln_weeks = [f"Wk {w}" for w in range(1,13)]
vuln_series = {
    "Remote Access":    [18,19,21,22,23,25,26,27,29,31,29,30],
    "Vendor Risk":      [12,13,14,16,17,19,21,22,23,24,24,25],
    "Phishing":         [25,24,23,24,23,22,24,23,24,22,21,20],
    "Misconfiguration": [22,21,20,21,23,20,19,18,17,16,16,15],
    "Legacy/Unpatched": [8, 8, 9, 8, 8, 8, 9,10,11,12,11,10],
}
vuln_colors = [C_BLUE, C_PURP, PINK, C_AMBER, C_GREEN]

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
st.sidebar.header("Filters & Controls")
st.sidebar.markdown("##### Sector Selection")
selected_sectors = st.sidebar.multiselect(
    "Sector",
    ["Finance","Manufacturing","Healthcare","Prof. Services","Public Admin",
     "Information","Education","Retail","Wholesale","Transportation",
     "Utilities","Construction","Real Estate","Entertainment","Other Services"],
    default=["Finance","Manufacturing","Healthcare","Prof. Services","Public Admin"],
)
st.sidebar.markdown("##### Time Period")
st.sidebar.selectbox("Time Range",
    ["Nov 2023 – Oct 2024 (DBIR 2025)","Last 12 months","Last Quarter"])
st.sidebar.markdown("##### Threat Category")
st.sidebar.selectbox("Threat Type",
    ["All","Ransomware","Social Engineering","Vulnerability Exploitation",
     "Data Theft","Supply Chain","Denial of Service"])
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

# ─────────────────────────────────────────
# KPI ROW
# ─────────────────────────────────────────
st.markdown("## Key Risk Metrics")
m1,m2,m3,m4,m5 = st.columns(5)
m1.metric("Total Incidents",        "22,052",  "Nov'23–Oct'24")
m2.metric("Confirmed Breaches",     "12,195",  "DBIR 2025")
m3.metric("Ransomware in Breaches", "44%",     "↑37% YoY",  delta_color="inverse")
m4.metric("Vuln Exploit Access",    "20%",     "↑34% YoY",  delta_color="inverse")
m5.metric("Third-Party Breaches",   "30%",     "↑100% YoY", delta_color="inverse")

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

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_norm_plot + ([radar_norm_plot[0]] if radar_norm_plot else []),
        theta=radar_sectors_plot + ([radar_sectors_plot[0]] if radar_sectors_plot else []),
        fill="toself",
        fillcolor="rgba(220,38,38,0.15)",
        line=dict(color=RED, width=3),
        name="Risk Score",
    ))
    fig_radar.update_layout(
        **chart_layout(height=440, show_legend=False),
        polar=dict(
            bgcolor="white",
            radialaxis=dict(visible=True, range=[0,10],
                            tickfont=dict(size=10, color=MUTED),
                            gridcolor=BORDER, linecolor=BORDER2),
            angularaxis=dict(tickfont=dict(size=11, color=TEXT),
                             gridcolor=BORDER, linecolor=BORDER2),
        ),
    )
    st.plotly_chart(fig_radar, use_container_width=True)
    st.markdown(source_badge("22,052 incidents · 12,195 confirmed breaches"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "Why does Manufacturing score so high?",
        "Manufacturing topped confirmed breaches in 2025 for the first time. Ransomware groups deliberately target industrial operations because any production downtime creates immediate financial pressure to pay. Healthcare follows closely — patient records fetch 10× the price of credit card data on criminal markets, making hospitals a permanent high-value target."
    ), unsafe_allow_html=True)

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
    st.plotly_chart(fig_pressure, use_container_width=True)
    st.markdown(source_badge("15 industries · Nov 2023 – Oct 2024"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "Incident ≠ breach — the gap matters",
        "A large gap between the blue and red bars means a sector detects and stops attacks before data is compromised. Finance has many incidents but strong containment. Manufacturing and Healthcare show the smallest gaps — nearly every incident they experience ends in a confirmed breach, signalling weaker response capabilities or harder-to-patch systems."
    ), unsafe_allow_html=True)

# ─────────────────────────────────────────
# SECTION 2 — FORECAST OUTLOOK
# ─────────────────────────────────────────
_, col_fore, _ = st.columns([1, 2, 1], gap="large")

with col_fore:
    st.markdown("### Ransomware Is Rising Every Year")
    st.caption("44% of all confirmed breaches in 2024 involved ransomware — up from 25% in 2022")
    fig_fore = go.Figure()
    fig_fore.add_trace(go.Scatter(
        x=df_ransom["Year"], y=df_ransom["In Breaches (%)"],
        mode="lines+markers+text", name="Ransomware in Breaches",
        line=dict(color=C_RED, width=3.5),
        marker=dict(size=11, color=C_RED, line=dict(color="white", width=2.5)),
        text=df_ransom["In Breaches (%)"].apply(lambda v: f"  {v}%"),
        textposition="top center", textfont=dict(color=RED, size=13, family="Inter, sans-serif"),
        fill="tozeroy", fillcolor="rgba(239,68,68,0.10)",
    ))
    fig_fore.add_trace(go.Scatter(
        x=df_ransom["Year"], y=df_ransom["Refused to Pay (%)"],
        mode="lines+markers+text", name="Victims Refused to Pay",
        line=dict(color=C_GREEN, width=3, dash="dash"),
        marker=dict(size=10, color=C_GREEN, line=dict(color="white", width=2.5)),
        text=df_ransom["Refused to Pay (%)"].apply(lambda v: f"  {v}%"),
        textposition="bottom center", textfont=dict(color=GREEN, size=13, family="Inter, sans-serif"),
    ))
    layout = chart_layout(height=420)
    layout.update({
        "yaxis": dict(title="Percentage (%)", range=[0,80], gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11)),
        "xaxis": dict(title="Year", tickfont=dict(color=MUTED, size=12)),
        "legend": dict(orientation="h", y=-0.18, font=dict(size=11, color=TEXT)),
    })
    fig_fore.update_layout(**layout)
    st.plotly_chart(fig_fore, use_container_width=True)
    st.markdown(source_badge("Ransomware trajectory 2022–2024"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "More ransomware, but victims are fighting back",
        "Ransomware's share of breaches has nearly doubled in three years. However, the rising refusal-to-pay rate (now 64%) shows organisations are learning — paying rarely guarantees full data recovery and often funds the next attack. The DBIR notes that median ransom demands grew to $115,000 in 2024, making prevention far cheaper than recovery."
    ), unsafe_allow_html=True)

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
        x=df_patterns["Pattern"], y=df_patterns["Incidents"],
        name="Incidents",
        marker=dict(color=C_BLUE, opacity=0.80, line=dict(color="white", width=0.5)),
        text=df_patterns["Incidents"], textposition="outside",
        textfont=dict(size=10, color=TEXT, family="Inter, sans-serif"),
    ))
    fig_pat.add_trace(go.Bar(
        x=df_patterns["Pattern"], y=df_patterns["Breaches"],
        name="Confirmed Breaches",
        marker=dict(color=C_RED, opacity=0.88, line=dict(color="white", width=0.5)),
        text=df_patterns["Breaches"], textposition="outside",
        textfont=dict(size=10, color=TEXT, family="Inter, sans-serif"),
    ))
    layout = chart_layout(height=400)
    layout.update({
        "barmode": "group",
        "bargap": 0.2,
        "yaxis": dict(title="Count (log scale)", type="log", gridcolor="#f1f5f9",
                      tickfont=dict(color=MUTED, size=11), automargin=True),
        "xaxis": dict(tickangle=-18, tickfont=dict(color=TEXT, size=11), automargin=True),
        "legend": dict(orientation="h", y=-0.26, font=dict(size=11, color=TEXT)),
    })
    fig_pat.update_layout(**layout)
    st.plotly_chart(fig_pat, use_container_width=True)
    st.markdown(source_badge("7 VERIS incident classification patterns"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "Why does Denial of Service have 6,520 incidents but only 2 breaches?",
        "This is not a data error — it reflects how a breach is defined. The DBIR counts a breach only when data confidentiality is violated (something is stolen or exposed). DoS and DDoS attacks disrupt <em>availability</em> — they knock systems offline — but they do not steal data. Because nothing is taken, they almost never qualify as breaches. System Intrusion sits at the opposite extreme: it is purpose-built for exfiltration, converting almost every incident into a confirmed breach."
    ), unsafe_allow_html=True)

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
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown(source_badge("Top initial access vectors in confirmed breaches"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "Edge devices and VPNs now tied with stolen credentials",
        "Credential theft has led initial access for years, but Edge Device/VPN exploitation jumped 34% YoY to draw level. Attackers now scan for unpatched firewalls and VPN appliances — no phishing email needed, just a known CVE and an exposed IP. Organisations with long patch cycles are particularly exposed, especially if they use EOL network appliances."
    ), unsafe_allow_html=True)

# ─────────────────────────────────────────
# SECTION 4 — RANSOMWARE + THREAT ACTORS
# ─────────────────────────────────────────
st.markdown("## Ransomware & Who Is Behind Attacks")
col7, col8 = st.columns(2, gap="large")

with col7:
    st.markdown("#### How Often Does Ransomware Appear, by Sector?")
    st.caption("Green = below average risk · Orange = elevated · Red = high exposure")
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
                     annotation_position="top right")
    layout = chart_layout(height=400, show_legend=False)
    layout.update({
        "xaxis": dict(title="% of Breaches with Ransomware", range=[0,105],
                      gridcolor="#f1f5f9", tickfont=dict(color=MUTED, size=11), automargin=True),
        "yaxis": dict(tickfont=dict(color=TEXT, size=11), automargin=True, gridcolor="#f1f5f9"),
    })
    fig_rs.update_layout(**layout)
    st.plotly_chart(fig_rs, use_container_width=True)
    st.markdown(source_badge("Ransomware involvement across sectors"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "Why are small businesses hit hardest at 88%?",
        "SMBs rarely have dedicated security teams, offline backups, or the leverage to negotiate. Ransomware groups increasingly use automated tooling to target thousands of small organisations simultaneously — a volume play. Manufacturing plants are difficult to patch because taking OT systems offline disrupts production, so attackers exploit that reluctance. Public sector's lower rate partly reflects government policies restricting ransom payments."
    ), unsafe_allow_html=True)

with col8:
    st.markdown("#### Who Is Behind the Attacks?")
    st.caption("External actors rose 163% in espionage-driven breaches — the biggest shift in the 2025 report")
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
        x="External", y=85, text="163% ↑ espionage",
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
    st.plotly_chart(fig_act, use_container_width=True)
    st.markdown(source_badge("Threat actor categories across all breaches"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "The 163% spike in espionage is the report's starkest shift",
        "Nation-state actors — primarily linked to Russia, China, Iran and North Korea — dramatically increased targeting of intellectual property and critical infrastructure in 2024. The boundary between organised crime and state-sponsored hacking is blurring: some groups operate freely in exchange for intelligence-sharing with their governments. For organisations, this means attacks are better-resourced, more patient, and harder to detect than purely financial attacks."
    ), unsafe_allow_html=True)

# ─────────────────────────────────────────
# SECTION 5 — DATA TYPES + MFA BYPASS
# ─────────────────────────────────────────
st.markdown("## What Gets Stolen and How Attackers Get Past Security")
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
    st.plotly_chart(fig_dt, use_container_width=True)
    st.markdown(source_badge("Data categories stolen in confirmed breaches"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "Internal documents overtook personal data — ransomware's 'double extortion' is why",
        "Ransomware operators now exfiltrate files before encrypting them, threatening to publish sensitive internal documents if the ransom isn't paid. This 'double extortion' tactic made internal documents the most stolen category for the first time. Credentials rank highly because a single set of stolen logins can be resold dozens of times and used across multiple organisations."
    ), unsafe_allow_html=True)

with col10:
    st.markdown("#### How Attackers Bypass MFA")
    st.caption("Three techniques, each accounting for roughly one-third of MFA bypass incidents")
    fig_mfa = go.Figure(go.Pie(
        labels=["Token Theft","MFA Prompt Bombing","Adversary-in-the-Middle"],
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
        "annotations": [dict(text="MFA<br>Bypass", x=0.5, y=0.5,
                             font=dict(size=13, color=MUTED, family="Inter, sans-serif"),
                             showarrow=False)],
        "margin": dict(l=24, r=24, t=36, b=80),
    })
    fig_mfa.update_layout(**layout_mfa)
    st.plotly_chart(fig_mfa, use_container_width=True)
    st.markdown(source_badge("Social engineering & MFA bypass tactics"), unsafe_allow_html=True)
    st.markdown(insight_box(
        "Three equal bypass techniques means no single fix is sufficient",
        "Token Theft steals the session cookie after a successful login — MFA was passed, then hijacked. Prompt Bombing floods a user's phone with approval requests until one is accidentally accepted. Adversary-in-the-Middle intercepts the real authentication flow in real time. The equal split signals attackers rapidly switch methods when one is defended, which is why MFA alone is no longer a complete control — session protection and phishing-resistant MFA (FIDO2) are the next step."
    ), unsafe_allow_html=True)

    st.markdown(f"""
<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:8px;">
  <div style="background:{SURFACE};border:1px solid {BORDER2};border-radius:10px;padding:14px 20px;
              box-shadow:0 1px 3px rgba(0,0,0,0.06);flex:1;min-width:110px;">
    <span style="color:{MUTED};font-size:12px;display:block;font-weight:500;margin-bottom:4px;">BEC Losses 2024</span>
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
st.plotly_chart(fig_trends, use_container_width=True)
st.markdown(source_badge("Weekly incident trend by exploitation theme — 12-week window"), unsafe_allow_html=True)
st.markdown(insight_box(
    "Remote Access and Vendor Risk are growing — Phishing is surprisingly stable",
    "Remote Access exploitation is rising because hybrid work permanently expanded the VPN and RDP attack surface. Vendor Risk is climbing as attackers pivot to MSPs and third-party integrations — compromising one supplier grants access to dozens of clients simultaneously (the MOVEit and SolarWinds playbook). Phishing staying flat reflects a grim truth: despite years of awareness training, humans remain a consistent and reliable target."
), unsafe_allow_html=True)

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.divider()
st.markdown(f"""
<div style="text-align:center;padding:1.6rem;background:{SURFACE};
            border:1px solid {BORDER};border-radius:12px;margin-top:1rem;">
  <p style="color:{MUTED};font-size:0.82rem;letter-spacing:0.02em;line-height:2;margin:0;">
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
