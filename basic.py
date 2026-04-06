import streamlit as st
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="CyberSignals - Cyber Risk Intelligence",
    page_icon="🛡️",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS - RISKPAGES INSPIRED DESIGN
# ----------------------------
st.markdown("""
    <style>
    /* Import clean, professional fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Clean white background */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Main content wrapper with subtle shadow */
    .main {
        background-color: #ffffff;
    }
    
    .block-container {
        padding: 2rem 3rem 4rem 3rem;
        max-width: 1400px;
    }
    
    /* Main title - clean and bold */
    h1 {
        color: #1a1a1a !important;
        font-weight: 700 !important;
        font-size: 2.75rem !important;
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem !important;
        line-height: 1.2;
    }
    
    /* Subtitle caption - professional gray */
    [data-testid="stCaptionContainer"] {
        color: #666666 !important;
        font-size: 1.1rem !important;
        font-weight: 400;
        margin-bottom: 1rem !important;
        line-height: 1.6;
    }
    
    /* Description paragraph */
    .stMarkdown p {
        color: #4a4a4a;
        font-size: 1rem;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* Section headers (subheader) - minimal with bottom border */
    h2 {
        color: #1a1a1a !important;
        font-weight: 600 !important;
        font-size: 1.75rem !important;
        margin-top: 3rem !important;
        margin-bottom: 1.5rem !important;
        padding-bottom: 0.75rem !important;
        border-bottom: 2px solid #e0e0e0 !important;
        letter-spacing: -0.01em;
    }
    
    /* Card titles (h3) - clean and simple */
    h3 {
        color: #2a2a2a !important;
        font-weight: 600 !important;
        font-size: 1.25rem !important;
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.01em;
        line-height: 1.4;
    }
    
    /* Card captions */
    .element-container div[data-testid="stCaptionContainer"] {
        color: #737373 !important;
        font-size: 0.95rem !important;
        line-height: 1.5;
        margin-bottom: 1.25rem !important;
        font-weight: 400;
    }
    
    /* Images - clean with minimal border */
    [data-testid="stImage"] {
        border-radius: 4px;
        border: 1px solid #e5e5e5;
        overflow: hidden;
        transition: all 0.2s ease;
        background: #fafafa;
    }
    
    [data-testid="stImage"]:hover {
        border-color: #d0d0d0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
    
    /* Column containers - minimal white cards */
    [data-testid="column"] {
        background: #ffffff;
        padding: 1.75rem;
        border-radius: 4px;
        border: 1px solid #e5e5e5;
        transition: all 0.2s ease;
    }
    
    [data-testid="column"]:hover {
        border-color: #d0d0d0;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    }
    
    /* Sidebar - clean light gray */
    [data-testid="stSidebar"] {
        background-color: #f8f8f8;
        border-right: 1px solid #e5e5e5;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: #f8f8f8;
    }
    
    /* Sidebar header */
    [data-testid="stSidebar"] h2 {
        color: #1a1a1a !important;
        font-weight: 600 !important;
        font-size: 1.25rem !important;
        padding: 1rem 1.5rem !important;
        background-color: #ffffff !important;
        border-radius: 4px !important;
        margin: 0 0 1.5rem 0 !important;
        border: 1px solid #e5e5e5 !important;
        border-bottom: 2px solid #4a4a4a !important;
    }
    
    /* Sidebar section labels */
    [data-testid="stSidebar"] .stMarkdown h5 {
        color: #1a1a1a !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 1.5rem 0 0.5rem 0 !important;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: #4a4a4a !important;
        font-size: 0.95rem;
    }
    
    /* Sidebar inputs */
    [data-testid="stSidebar"] .stMultiSelect > div,
    [data-testid="stSidebar"] .stSelectbox > div {
        background-color: #ffffff !important;
        border: 1px solid #d0d0d0 !important;
        border-radius: 4px !important;
    }
    
    /* Info box in sidebar */
    [data-testid="stSidebar"] [data-testid="stNotificationContentInfo"] {
        background-color: #f0f4f8 !important;
        border: 1px solid #d0e1f0 !important;
        border-left: 3px solid #4a90e2 !important;
        color: #2c5282 !important;
        border-radius: 4px;
        font-size: 0.9rem;
    }
    
    /* Divider - minimal */
    hr {
        margin: 3rem 0 !important;
        border: none !important;
        border-top: 1px solid #e5e5e5 !important;
    }
    
    /* Footer - subtle */
    .main > div > div:last-child [data-testid="stCaptionContainer"] {
        color: #737373 !important;
        font-size: 0.875rem !important;
        text-align: center;
        padding: 1.5rem;
        background-color: #f8f8f8;
        border: 1px solid #e5e5e5;
        border-radius: 4px;
        margin-top: 3rem;
        line-height: 1.6;
    }
    
    /* Remove extra spacing */
    .element-container {
        margin-bottom: 0.5rem;
    }
    
    /* Column gap */
    [data-testid="stHorizontalBlock"] {
        gap: 1.5rem !important;
    }
    
    /* Strong text styling */
    strong {
        color: #1a1a1a;
        font-weight: 600;
    }
    
    /* Link styling - subtle blue */
    a {
        color: #4a90e2;
        text-decoration: none;
    }
    
    a:hover {
        color: #2c5282;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# PATHS
# ----------------------------
BASE = Path(__file__).parent
PH = BASE / "assets" / "placeholders"
VIS = BASE / "assets" / "visuals"

def get_img(name: str) -> Path:
    """Use final visual if it exists, otherwise fallback to placeholder."""
    final = VIS / name
    return final if final.exists() else (PH / name)

# ----------------------------
# HEADER
# ----------------------------
st.title("🛡️ CyberSignals")
st.caption("Comprehensive cyber risk intelligence for sector-level threat monitoring and analysis")

st.markdown(
    """
    CyberSignals is a sector-level cyber risk radar designed to help business and IT audiences 
    understand **which sectors are under pressure**, **what is driving risk**, and 
    **what actions to take next**.
    """
)

# ----------------------------
# SIDEBAR (Clean Filters)
# ----------------------------
st.sidebar.header("Filters & Controls")

st.sidebar.markdown("##### Sector Selection")
st.sidebar.multiselect(
    "Sector",
    ["Communications", "Energy", "Financials", "Healthcare", "Industrials",
     "Materials", "Real Estate", "Retail", "Technology", "Utilities"],
    default=["Energy", "Healthcare", "Retail"]
)

st.sidebar.markdown("##### Time Period")
st.sidebar.selectbox(
    "Time Range",
    ["Last 30 days", "Last Quarter", "Last 12 months"]
)

st.sidebar.markdown("##### Threat Category")
st.sidebar.selectbox(
    "Threat Type",
    ["All", "Ransomware", "Data Theft", "Fraud", 
     "Supply Chain", "Operational Disruption"]
)

st.sidebar.info("**Note:** Filters are placeholders. Production version will drive real-time data filtering and analysis.")

# ----------------------------
# DASHBOARD GRID
# ----------------------------
st.subheader("Dashboard Overview")

cards = [
    ("Sector Risk Radar",
     "Which industries look most exposed right now?",
     "sector_risk_radar.png"),

    ("Incident Pressure",
     "Are incidents increasing? What's driving the pressure?",
     "incident_pressure.png"),

    ("Vulnerability Signals",
     "What weaknesses are being exploited most?",
     "vulnerability_signals.png"),

    ("Forecast Outlook",
     "Which sectors may be at higher risk next (probability-based)?",
     "forecast_outlook.png"),
]

col1, col2 = st.columns(2, gap="large")

for i, (title, desc, img_name) in enumerate(cards):
    target = col1 if i % 2 == 0 else col2
    with target:
        st.markdown(f"### {title}")
        st.caption(desc)
        st.image(str(get_img(img_name)), use_container_width=True)

# ----------------------------
# FULL-WIDTH THREAT TYPE TRENDS
# ----------------------------
st.subheader("Threat Type Trends")
st.caption("What types of cybercrime are trending across sectors?")
st.image(str(get_img("threat_type_trends.png")), use_container_width=True)

# ----------------------------
# FOOTER
# ----------------------------
st.divider()
st.caption(
    "**Disclaimer:** Prototype mockup using illustrative visuals for layout/storytelling. "
    "Final version will use validated sources, documented risk scoring, and live datasets."
)