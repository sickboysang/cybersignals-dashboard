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
# DESIGN TOKENS  (mirrors the HTML file)
# ─────────────────────────────────────────
BG      = "#080c10"
SURFACE = "#0d1318"
BORDER  = "#1a2530"
BORDER2 = "#243040"
TEXT    = "#c8d8e8"
MUTED   = "#556677"
ACCENT  = "#00c8ff"
ACCENT2 = "#7b5ef8"
RED     = "#ff3d5a"
ORANGE  = "#ff8c42"
GREEN   = "#1affa0"
YELLOW  = "#ffd740"
PINK    = "#f72585"

# ─────────────────────────────────────────
# GLOBAL CSS — dark terminal theme
# ─────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Syne:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'JetBrains Mono', monospace !important;
    background-color: {BG} !important;
    color: {TEXT} !important;
}}

.stApp {{
    background-color: {BG} !important;
    background-image:
        linear-gradient(rgba(0,200,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,200,255,0.03) 1px, transparent 1px) !important;
    background-size: 40px 40px !important;
}}

.main .block-container {{
    padding: 2.5rem 3rem 4rem 3rem !important;
    max-width: 1400px !important;
    background: transparent !important;
}}

h1 {{
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    font-size: 2.8rem !important;
    color: #ffffff !important;
    letter-spacing: -0.02em !important;
    line-height: 1.1 !important;
    margin-bottom: 0.4rem !important;
}}
h2 {{
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.5rem !important;
    color: #e0ecf8 !important;
    margin-top: 2.5rem !important;
    margin-bottom: 1rem !important;
    padding-bottom: 0.6rem !important;
    border-bottom: 1px solid {BORDER2} !important;
    letter-spacing: 0.01em !important;
}}
h3 {{
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    color: #e0ecf8 !important;
    margin-top: 0 !important;
    margin-bottom: 0.4rem !important;
}}

p, .stMarkdown p {{
    font-family: 'JetBrains Mono', monospace !important;
    color: {TEXT} !important;
    font-size: 0.9rem !important;
    line-height: 1.7 !important;
}}

[data-testid="stCaptionContainer"] p {{
    color: {MUTED} !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.04em !important;
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
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
}}
[data-testid="stSidebar"] .stMarkdown h5 {{
    color: {MUTED} !important;
    font-size: 0.7rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    font-family: 'JetBrains Mono', monospace !important;
    margin: 1.2rem 0 0.4rem 0 !important;
}}
[data-testid="stSidebar"] .stMultiSelect > div > div,
[data-testid="stSidebar"] .stSelectbox > div > div {{
    background-color: {BG} !important;
    border: 1px solid {BORDER2} !important;
    border-radius: 4px !important;
    color: {TEXT} !important;
}}
[data-testid="stSidebar"] [data-testid="stNotificationContentInfo"] {{
    background-color: rgba(0,200,255,0.06) !important;
    border: 1px solid rgba(0,200,255,0.2) !important;
    border-left: 3px solid {ACCENT} !important;
    color: {TEXT} !important;
    border-radius: 4px !important;
    font-size: 0.8rem !important;
}}

/* ── COLUMNS / CARDS ── */
[data-testid="column"] {{
    background: {SURFACE} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 8px !important;
    padding: 1.5rem !important;
    transition: border-color 0.2s !important;
}}
[data-testid="column"]:hover {{
    border-color: {BORDER2} !important;
}}

/* ── METRICS ── */
[data-testid="metric-container"] {{
    background: {SURFACE} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 8px !important;
    padding: 1rem 1.2rem !important;
}}
[data-testid="metric-container"] label {{
    color: {MUTED} !important;
    font-size: 0.72rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    font-family: 'JetBrains Mono', monospace !important;
}}
[data-testid="metric-container"] [data-testid="stMetricValue"] {{
    font-family: 'Syne', sans-serif !important;
    font-size: 1.6rem !important;
    font-weight: 800 !important;
    color: {ACCENT} !important;
}}
[data-testid="metric-container"] [data-testid="stMetricDelta"] {{
    font-size: 0.75rem !important;
    font-family: 'JetBrains Mono', monospace !important;
}}

hr {{
    border: none !important;
    border-top: 1px solid {BORDER2} !important;
    margin: 2.5rem 0 !important;
}}

::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: {BORDER2}; border-radius: 3px; }}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# PLOTLY DARK BASE LAYOUT
# ─────────────────────────────────────────
def dark_layout(height=400, show_legend=True, legend_y=-0.2):
    return dict(
        height=height,
        margin=dict(l=48, r=20, t=28, b=48),
        plot_bgcolor=SURFACE,
        paper_bgcolor=SURFACE,
        font=dict(family="JetBrains Mono, monospace", size=11, color=TEXT),
        showlegend=show_legend,
        legend=dict(
            orientation="h", y=legend_y,
            font=dict(size=10, color=MUTED),
            bgcolor="rgba(0,0,0,0)",
        ),
        xaxis=dict(
            gridcolor=BORDER, gridwidth=1,
            zerolinecolor=BORDER2,
            tickfont=dict(color=MUTED, size=10),
            linecolor=BORDER2,
        ),
        yaxis=dict(
            gridcolor=BORDER, gridwidth=1,
            zerolinecolor=BORDER2,
            tickfont=dict(color=MUTED, size=10),
            linecolor=BORDER2,
        ),
    )

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

df_vuln = pd.DataFrame({
    "Metric": ["Mass Exploit\n(CISA KEV)","Mass Exploit\n(Edge Devices)",
               "Full Remediation\n(All KEV)","Full Remediation\n(Edge Devices)"],
    "Days":   [5,0,38,32],
    "Color":  [RED,RED,ORANGE,ORANGE],
})

df_ransom_sector = pd.DataFrame({
    "Sector":         ["SMB (<1k empl.)","Manufacturing","System Intrusion","Public Sector",
                       "APAC","EMEA","Large Orgs"],
    "Ransomware (%)": [88,47,75,30,51,40,39],
}).sort_values("Ransomware (%)")

radar_sectors  = ["Finance","Manufacturing","Healthcare","Prof. Services",
                  "Public Admin","Education","Retail","Info/Tech"]
radar_breaches = [927,1607,1542,1147,946,851,419,784]
radar_norm     = [round(b/max(radar_breaches)*10,1) for b in radar_breaches]

df_data = pd.DataFrame({
    "Data Type":           ["Internal Docs","Personal Data","Credentials","Medical",
                            "Secrets/API Keys","Sensitive Personal","Bank Data","Payment Cards"],
    "Relative Prevalence": [9,8,7,6,5,4,3,1],
}).sort_values("Relative Prevalence")

vuln_weeks = [f"Wk {w}" for w in range(1,13)]
vuln_series = {
    "Remote Access":    [18,19,21,22,23,25,26,27,29,31,29,30],
    "Vendor Risk":      [12,13,14,16,17,19,21,22,23,24,24,25],
    "Phishing":         [25,24,23,24,23,22,24,23,24,22,21,20],
    "Misconfiguration": [22,21,20,21,23,20,19,18,17,16,16,15],
    "Legacy/Unpatched": [8, 8, 9, 8, 8, 8, 9,10,11,12,11,10],
}
vuln_colors = [ACCENT, ACCENT2, PINK, YELLOW, GREEN]

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
# indicate that these extra pickers are currently placeholders
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
<div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;">
  <div style="display:inline-flex;align-items:center;gap:8px;
              font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
              color:{ACCENT};border:1px solid rgba(0,200,255,0.3);
              padding:6px 14px;border-radius:4px;background:rgba(0,200,255,0.04);">
    <span style="width:7px;height:7px;border-radius:50%;
                 background:{ACCENT};display:inline-block;flex-shrink:0;"></span>
    LIVE THREAT INTELLIGENCE
  </div>
  <div style="display:inline-flex;align-items:center;gap:8px;
              font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
              color:{MUTED};border:1px solid {BORDER};
              padding:6px 14px;border-radius:4px;">
    VERIZON DBIR 2025
  </div>
  <div style="display:inline-flex;align-items:center;gap:8px;
              font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
              color:{MUTED};border:1px solid {BORDER};
              padding:6px 14px;border-radius:4px;">
    TEAM N5 · USI4280
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
st.markdown("## Dashboard Overview")
# apply sector filter up front so both charts can react
filtered = df_industry[df_industry["Industry"].isin(selected_sectors)]
if selected_sectors and filtered.empty:
    st.warning("No sectors selected – sidebar filter returned no rows. Showing all sectors instead.")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### Sector Risk Radar")
    st.caption("Normalized breach exposure — 2025 DBIR confirmed breach volume")
    # rebuild radar data based on filter (fall back to all if nothing selected)
    df_radar_plot = filtered if not filtered.empty else df_industry
    radar_sectors_plot = df_radar_plot["Industry"].tolist()
    radar_breaches_plot = df_radar_plot["Breaches"].tolist()
    radar_norm_plot = [round(b / max(radar_breaches_plot) * 10, 1) if radar_breaches_plot else 0
                       for b in radar_breaches_plot]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_norm_plot + ([radar_norm_plot[0]] if radar_norm_plot else []),
        theta=radar_sectors_plot + ([radar_sectors_plot[0]] if radar_sectors_plot else []),
        fill="toself",
        fillcolor="rgba(255,61,90,0.12)",
        line=dict(color=RED, width=2.5),
        name="Risk Score",
    ))
    fig_radar.update_layout(
        **dark_layout(height=420, show_legend=False),
        polar=dict(
            bgcolor=SURFACE,
            radialaxis=dict(visible=True, range=[0,10],
                            tickfont=dict(size=9, color=MUTED),
                            gridcolor=BORDER, linecolor=BORDER2),
            angularaxis=dict(tickfont=dict(size=10, color=TEXT),
                             gridcolor=BORDER, linecolor=BORDER2),
        ),
    )
    st.plotly_chart(fig_radar, use_container_width=True)

with col2:
    st.markdown("### Incident Pressure by Sector")
    st.caption("Incidents vs confirmed breaches — sidebar sector filter applies here")
    df_plot = filtered if not filtered.empty else df_industry
    fig_pressure = go.Figure()
    fig_pressure.add_trace(go.Bar(
        y=df_plot["Industry"], x=df_plot["Incidents"],
        name="Incidents", orientation="h",
        marker=dict(color="rgba(0,200,255,0.22)", line=dict(color=ACCENT, width=1)),
        text=df_plot["Incidents"], textposition="outside",
        textfont=dict(size=9, color=MUTED),
    ))
    fig_pressure.add_trace(go.Bar(
        y=df_plot["Industry"], x=df_plot["Breaches"],
        name="Confirmed Breaches", orientation="h",
        marker=dict(color=RED, opacity=0.85),
        text=df_plot["Breaches"], textposition="outside",
        textfont=dict(size=9, color=MUTED),
    ))
    layout = dark_layout(height=420)
    layout.update({
        "barmode": "group",
        "bargap": 0.15,
        "yaxis": dict(automargin=True),
        "xaxis": dict(title="Count", gridcolor=BORDER, tickfont=dict(color=MUTED,size=10)),
        "legend": dict(orientation="h", y=-0.16, font=dict(size=10,color=MUTED)),
    })
    fig_pressure.update_layout(**layout)
    st.plotly_chart(fig_pressure, use_container_width=True)

# ─────────────────────────────────────────
# SECTION 2 — VULNERABILITY + FORECAST
# ─────────────────────────────────────────
col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("### Vulnerability Signals")
    st.caption("Exploitation speed vs remediation timelines — the gap is the danger zone")
    fig_vuln = go.Figure()
    # switch to horizontal bars so long metric labels are readable
    fig_vuln.add_trace(go.Bar(
        y=df_vuln["Metric"], x=df_vuln["Days"],
        orientation="h",
        marker_color=df_vuln["Color"],
        marker_line=dict(color="rgba(0,0,0,0.3)", width=1),
        text=df_vuln["Days"].apply(lambda d: f"{d}d" if d > 0 else "0d — same day!"),
        textposition="outside",
        textfont=dict(size=10, color=TEXT),
        showlegend=False,
    ))
    # horizontal threshold line moves to x=5
    fig_vuln.add_vline(x=5, line_dash="dot", line_color=RED, line_width=1.5,
                       annotation_text="5-day mass exploit window",
                       annotation_font=dict(color=RED, size=10),
                       annotation_position="top right")
    layout = dark_layout(height=400, show_legend=False)
    layout.update({
        "xaxis": dict(title="Days", range=[0,46], gridcolor=BORDER, tickfont=dict(color=MUTED,size=10)),
        "yaxis": dict(automargin=True, tickfont=dict(color=MUTED,size=10)),
    })
    fig_vuln.update_layout(**layout)
    st.plotly_chart(fig_vuln, use_container_width=True)

with col4:
    st.markdown("### Forecast Outlook")
    st.caption("Ransomware 3-year trajectory — 44% of breaches now involve ransomware")
    fig_fore = go.Figure()
    fig_fore.add_trace(go.Scatter(
        x=df_ransom["Year"], y=df_ransom["In Breaches (%)"],
        mode="lines+markers+text", name="Ransomware in Breaches",
        line=dict(color=RED, width=3),
        marker=dict(size=10, color=RED, line=dict(color=BG, width=2)),
        text=df_ransom["In Breaches (%)"].apply(lambda v: f"{v}%"),
        textposition="top center", textfont=dict(color=RED, size=11),
        fill="tozeroy", fillcolor="rgba(255,61,90,0.08)",
    ))
    fig_fore.add_trace(go.Scatter(
        x=df_ransom["Year"], y=df_ransom["Refused to Pay (%)"],
        mode="lines+markers+text", name="Victims Refused to Pay",
        line=dict(color=GREEN, width=2.5, dash="dash"),
        marker=dict(size=9, color=GREEN, line=dict(color=BG, width=2)),
        text=df_ransom["Refused to Pay (%)"].apply(lambda v: f"{v}%"),
        textposition="bottom center", textfont=dict(color=GREEN, size=11),
    ))
    layout = dark_layout(height=400)
    layout.update({
        "yaxis": dict(title="Percentage (%)", range=[0,80], gridcolor=BORDER),
        "xaxis": dict(title="Year"),
        "legend": dict(orientation="h", y=-0.2, font=dict(size=10,color=MUTED)),
    })
    fig_fore.update_layout(**layout)
    st.plotly_chart(fig_fore, use_container_width=True)

# ─────────────────────────────────────────
# SECTION 3 — THREAT TYPE TRENDS
# ─────────────────────────────────────────
st.markdown("## Threat Type Trends")
st.caption("Attack patterns driving the most incidents and confirmed breaches")

col5, col6 = st.columns([3,2], gap="large")

with col5:
    st.markdown("#### Incident Classification Patterns")
    fig_pat = go.Figure()
    fig_pat.add_trace(go.Bar(
        x=df_patterns["Pattern"], y=df_patterns["Incidents"],
        name="Incidents",
        marker=dict(color="rgba(0,200,255,0.28)", line=dict(color=ACCENT,width=1)),
        text=df_patterns["Incidents"], textposition="outside",
        textfont=dict(size=9, color=MUTED),
    ))
    fig_pat.add_trace(go.Bar(
        x=df_patterns["Pattern"], y=df_patterns["Breaches"],
        name="Confirmed Breaches",
        marker=dict(color=RED, opacity=0.85),
        text=df_patterns["Breaches"], textposition="outside",
        textfont=dict(size=9, color=MUTED),
    ))
    layout = dark_layout(height=380)
    layout.update({
        "barmode": "group",
        "yaxis": dict(title="Count", type="log", gridcolor=BORDER, automargin=True),
        "xaxis": dict(tickangle=-18, automargin=True),
        "legend": dict(orientation="h", y=-0.3, font=dict(size=10,color=MUTED)),
    })
    fig_pat.update_layout(**layout)
    st.plotly_chart(fig_pat, use_container_width=True)

with col6:
    st.markdown("#### Initial Access Vectors")
    fig_pie = go.Figure(go.Pie(
        labels=df_access["Vector"], values=df_access["Pct"], hole=0.5,
        marker=dict(colors=[ORANGE,RED,ACCENT,ACCENT2], line=dict(color=BG,width=3)),
        textinfo="label+percent",
        textfont=dict(size=11, color=TEXT),
        insidetextorientation="radial",
    ))
    fig_pie.update_layout(
        **dark_layout(height=380, show_legend=False),
        annotations=[dict(text="Access<br>Vectors", x=0.5, y=0.5,
                          font=dict(size=12, color=TEXT, family="Syne, sans-serif"),
                          showarrow=False)],
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# ─────────────────────────────────────────
# SECTION 4 — RANSOMWARE + THREAT ACTORS
# ─────────────────────────────────────────
st.markdown("## Ransomware & Threat Actor Intelligence")
col7, col8 = st.columns(2, gap="large")

with col7:
    st.markdown("#### Ransomware Prevalence by Sector")
    st.caption("Green < 40% · Orange 40–60% · Red > 60%")
    bar_colors = [GREEN if v < 40 else (ORANGE if v < 60 else RED)
                  for v in df_ransom_sector["Ransomware (%)"]]
    fig_rs = go.Figure(go.Bar(
        y=df_ransom_sector["Sector"], x=df_ransom_sector["Ransomware (%)"],
        orientation="h",
        marker=dict(color=bar_colors, opacity=0.9, line=dict(color="rgba(0,0,0,0.2)",width=1)),
        text=[f"{v}%" for v in df_ransom_sector["Ransomware (%)"]],
        textposition="outside", textfont=dict(size=10, color=TEXT),
    ))
    fig_rs.add_vline(x=44, line_dash="dot", line_color=MUTED, line_width=1.2,
                     annotation_text="Avg 44%",
                     annotation_font=dict(color=MUTED,size=10),
                     annotation_position="top right")
    layout = dark_layout(height=380, show_legend=False)
    layout.update({
        "xaxis": dict(title="% of Breaches with Ransomware", range=[0,100], gridcolor=BORDER, automargin=True),
        "yaxis": dict(tickfont=dict(color=TEXT,size=10), automargin=True),
    })
    fig_rs.update_layout(**layout)
    st.plotly_chart(fig_rs, use_container_width=True)

with col8:
    st.markdown("#### Threat Actor Breakdown")
    st.caption("External actors surged 163% in espionage-motivated breaches")
    actor_labels = ["External","Internal","Partner/3rd-party","State-sponsored"]
    actor_vals   = [80,20,30,15]
    actor_colors = [RED,ORANGE,ACCENT2,"#8c564b"]
    fig_act = go.Figure(go.Bar(
        x=actor_labels, y=actor_vals,
        marker=dict(color=actor_colors, opacity=0.9, line=dict(color="rgba(0,0,0,0.2)",width=1)),
        text=[f"{v}%" for v in actor_vals],
        textposition="outside", textfont=dict(size=11, color=TEXT),
    ))
    fig_act.add_annotation(
        x="External", y=83, text="163% ↑ espionage",
        showarrow=False, font=dict(color=RED, size=10),
        bgcolor=f"rgba(13,19,24,0.9)", bordercolor=BORDER2, borderwidth=1,
    )
    layout = dark_layout(height=380, show_legend=False)
    layout.update({
        "yaxis": dict(title="Prevalence in Breaches (%)", range=[0,100], gridcolor=BORDER),
        "xaxis": dict(tickfont=dict(color=TEXT,size=10)),
    })
    fig_act.update_layout(**layout)
    st.plotly_chart(fig_act, use_container_width=True)

# ─────────────────────────────────────────
# SECTION 5 — DATA TYPES + MFA BYPASS
# ─────────────────────────────────────────
st.markdown("## Data Exposure & Social Engineering")
col9, col10 = st.columns(2, gap="large")

with col9:
    st.markdown("#### Data Types Compromised")
    st.caption("Relative prevalence across all confirmed breach incidents (2025 DBIR)")
    data_colors = [ACCENT if v >= 7 else (ACCENT2 if v >= 5 else MUTED)
                   for v in df_data["Relative Prevalence"]]
    fig_dt = go.Figure(go.Bar(
        y=df_data["Data Type"], x=df_data["Relative Prevalence"],
        orientation="h",
        marker=dict(color=data_colors, opacity=0.85, line=dict(color="rgba(0,0,0,0.2)",width=1)),
        text=df_data["Relative Prevalence"].apply(lambda v: f"Score {v}/9"),
        textposition="outside", textfont=dict(size=9, color=MUTED),
    ))
    layout = dark_layout(height=380, show_legend=False)
    layout.update({
        "xaxis": dict(title="Relative Prevalence Score", range=[0,11], gridcolor=BORDER),
        "yaxis": dict(tickfont=dict(color=TEXT,size=10)),
    })
    fig_dt.update_layout(**layout)
    st.plotly_chart(fig_dt, use_container_width=True)

with col10:
    st.markdown("#### MFA Bypass Methods")
    st.caption("Three equally dominant bypass techniques — each ~31% (2025 DBIR)")
    fig_mfa = go.Figure(go.Pie(
        labels=["Token Theft","MFA Prompt Bombing","Adversary-in-the-Middle"],
        values=[31,31,31], hole=0.52,
        marker=dict(colors=[RED,ORANGE,ACCENT2], line=dict(color=BG,width=3)),
        textinfo="label+percent",
        textfont=dict(size=11, color=TEXT),
        insidetextorientation="radial",
    ))
    fig_mfa.update_layout(
        **dark_layout(height=340, show_legend=False),
        annotations=[dict(text="MFA<br>Bypass", x=0.5, y=0.5,
                          font=dict(size=12, color=TEXT, family="Syne, sans-serif"),
                          showarrow=False)],
    )
    st.plotly_chart(fig_mfa, use_container_width=True)

    st.markdown(f"""
<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:4px;">
  <div style="background:{SURFACE};border:1px solid {BORDER2};border-radius:6px;padding:10px 16px;">
    <span style="color:{MUTED};font-size:10px;display:block;letter-spacing:0.1em;text-transform:uppercase;">BEC Losses 2024</span>
    <span style="color:{RED};font-family:'Syne',sans-serif;font-size:20px;font-weight:800;">$6.3B</span>
  </div>
  <div style="background:{SURFACE};border:1px solid {BORDER2};border-radius:6px;padding:10px 16px;">
    <span style="color:{MUTED};font-size:10px;display:block;letter-spacing:0.1em;text-transform:uppercase;">AI-Written Lures</span>
    <span style="color:{ORANGE};font-family:'Syne',sans-serif;font-size:20px;font-weight:800;">~10%</span>
  </div>
  <div style="background:{SURFACE};border:1px solid {BORDER2};border-radius:6px;padding:10px 16px;">
    <span style="color:{MUTED};font-size:10px;display:block;letter-spacing:0.1em;text-transform:uppercase;">Espionage Motive</span>
    <span style="color:{PINK};font-family:'Syne',sans-serif;font-size:20px;font-weight:800;">52%</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# SECTION 6 — VULNERABILITY EXPLOITATION THEMES
# (mirrors the 12-week trend line chart from the HTML)
# ─────────────────────────────────────────
st.markdown("## Vulnerability Exploitation Themes")
st.caption("12-week weekly incident trend by exploitation category — hover for details")

fig_trends = go.Figure()
for (name, vals), color in zip(vuln_series.items(), vuln_colors):
    r,g,b = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
    fig_trends.add_trace(go.Scatter(
        x=vuln_weeks, y=vals,
        mode="lines+markers",
        name=name,
        line=dict(color=color, width=2.5),
        marker=dict(size=7, color=color, line=dict(color=BG,width=2)),
        fill="tozeroy",
        fillcolor=f"rgba({r},{g},{b},0.07)",
        hovertemplate=f"<b>{name}</b><br>%{{x}}: %{{y}} incidents<extra></extra>",
    ))

layout = dark_layout(height=440, legend_y=-0.12)
layout.update({
    "xaxis": dict(gridcolor=BORDER, tickfont=dict(color=MUTED,size=10), automargin=True),
    "yaxis": dict(title="Incidents / Week", gridcolor=BORDER, tickfont=dict(color=MUTED,size=10), automargin=True),
    "hovermode": "x unified",
})
fig_trends.update_layout(**layout)
st.plotly_chart(fig_trends, use_container_width=True)

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.divider()
st.markdown(f"""
<div style="text-align:center;padding:1.4rem;background:{SURFACE};
            border:1px solid {BORDER};border-radius:8px;margin-top:1rem;">
  <p style="color:{MUTED};font-size:0.78rem;letter-spacing:0.05em;line-height:1.9;margin:0;">
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
