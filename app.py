import streamlit as st
import random
import time

# Page configuration for an elite presentation
st.set_page_config(
    page_title="StadiumPulse 2026 | Next-Gen Smart Stadium",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Premium Neon Sport Cyberpunk Layout
st.markdown("""
    <style>
    /* Full Page Background Override */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1e1b4b 0%, #090d16 60%, #020617 100%) !important;
        background-attachment: fixed !important;
        color: #f8fafc !important;
    }
    
    /* TOTAL BULLETPROOF SIDEBAR GLASS OVERRIDE */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%) !important;
        background-color: #0f172a !important;
        border-right: 2px solid rgba(56, 189, 248, 0.2) !important;
        box-shadow: 5px 0 25px rgba(0, 0, 0, 0.6) !important;
    }
    
    /* Target regular text fields inside sidebar container */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebarSectionHeader"] * {
        color: #f1f5f9 !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
    }

    /* CRITICAL FIX: Hide the leaked raw text icon indicator string */
    [data-testid="stSidebar"] button span {
        display: none !important;
    }
    
    /* Fix Streamlit column wrapping to ensure symmetric boxes */
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 0% !important;
        padding: 0 10px !important;
    }
    
    /* Premium Glassmorphic Symmetric KPI Boxes */
    .metric-card {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(56, 189, 248, 0.15);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.4);
        transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        text-align: left;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(56, 189, 248, 0.6);
        box-shadow: 0 15px 35px 0 rgba(56, 189, 248, 0.25);
        background: rgba(30, 41, 59, 0.75);
    }
    
    /* Clean custom headers without markdown anomalies */
    .custom-title {
        font-size: 1.9rem;
        font-weight: 800;
        color: #ffffff;
        margin-top: 10px;
        margin-bottom: 5px;
        letter-spacing: -0.02em;
    }
    .custom-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-bottom: 25px;
    }
    
    /* Animated Dynamic Title Text */
    @keyframes flowingChroma {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .gradient-text {
        background: linear-gradient(-45deg, #38bdf8, #2563eb, #8b5cf6, #ec4899);
        background-size: 300% 300%;
        animation: flowingChroma 6s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 3.6rem;
        letter-spacing: -0.03em;
        margin-bottom: 0px;
    }
    
    /* Heartbeat Radar Dot */
    @keyframes heartbeatGlow {
        0% { opacity: 0.4; transform: scale(0.95); }
        50% { opacity: 1; transform: scale(1.1); }
        100% { opacity: 0.4; transform: scale(0.95); }
    }
    .pulse-node {
        display: inline-block;
        color: #22c55e;
        animation: heartbeatGlow 2s infinite ease-in-out;
        margin-right: 6px;
    }
    
    /* Sleek Action Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Dashboard Architecture Layout
st.markdown('<h1 class="gradient-text">⚽ StadiumPulse 2026</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 1.25rem; font-weight: 400; margin-bottom: 2rem;">GenAI-Driven Infrastructure & Tournament Operations Orchestrator • FIFA World Cup 2026</p>', unsafe_allow_html=True)
st.markdown("---")

# Navigation Control Center Sidebar
st.sidebar.markdown("<h2 style='font-size:1.4rem; font-weight:700; color:#ffffff; margin-top:10px; margin-bottom:15px;'>🎛️ Strategic Core</h2>", unsafe_allow_html=True)
persona = st.sidebar.radio(
    "Select Operational Interface Node:",
    ("🌐 International Fan Hub", "📊 Command Center Dashboard", "🚨 Rapid Response & Crowd Safety")
)

st.sidebar.markdown("---")
st.sidebar.markdown("<h3 style='font-size:1.15rem; font-weight:600; color:#ffffff; margin-bottom:10px;'>📡 Telemetry Stream Matrix</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='margin-bottom:8px;'><span class='pulse-node'>●</span> <strong>GenAI Core:</strong> Operational</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='margin-bottom:8px;'>🟢 <strong>Latency Pipeline:</strong> 0.2s Live</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='margin-bottom:8px;'>⚽ <strong>Tournament Stage:</strong> Quarter Finals</p>", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# INTERFACE 1: INTERNATIONAL FAN HUB
# -------------------------------------------------------------------------
if persona == "🌐 International Fan Hub":
    st.markdown('<div class="custom-title">🌐 Multilingual Fan Experience Companion</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-subtitle">Real-time hyper-localized translation and navigation assistance powered by LLM orchestration.</div>', unsafe_allow_html=True)
    
    col_lang, col_space = st.columns([1, 2])
    with col_lang:
        lang = st.selectbox("Select Native Language Profile", ["English", "Español (Spanish)", "Português (Portuguese)", "Français (French)", "Deutsch (German)"])
    
    st.markdown('<div style="font-size:1.2rem; font-weight:700; color:#ffffff; margin-top:15px; margin-bottom:10px;">💬 Engage Stadium AI Assistant</div>', unsafe_allow_html=True)
    user_query = st.text_input("Type your question or request navigation support:", placeholder="Ask about transit hubs, medical facilities, or seating sectors...", label_visibility="collapsed")
    
    if user_query:
        loading_bar = st.progress(0)
        for segment in range(100):
            time.sleep(0.003)
            loading_bar.progress(segment + 1)
        loading_bar.empty()
            
        query_lower = user_query.lower()
        if "medical" in query_lower or "first aid" in query_lower or "doctor" in query_lower:
            reply = "The primary First Aid Hub near your current zone is behind Section 104, adjacent to elevator bank B. Floor indicators have been dynamically highlighted in neon green for you."
        elif "transit" in query_lower or "bus" in query_lower or "train" in query_lower or "uber" in query_lower:
            reply = "The Rapid Transit Terminal is situated outside East Gate E. Dedicated high-frequency shuttles depart every 3 minutes. Follow the illuminated blue terminal corridors."
        else:
            reply = "Welcome to the 2026 FIFA World Cup! Your current location shows optimal egress via Portal 4. Refreshments, concessions, and smart water stations are located exactly 15 meters to your direct left."
        
        greetings = {"English": "Hello! ", "Español (Spanish)": "¡Hola! ", "Português (Portuguese)": "Olá! ", "Français (French)": "Bonjour! ", "Deutsch (German)": "Hallo! "}
        
        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.55); backdrop-filter: blur(12px); padding: 26px; border-left: 5px solid #3b82f6; border-radius: 14px; margin-top: 20px; box-shadow: 0 15px 35px -5px rgba(0,0,0,0.4);">
            <span style="color: #38bdf8; font-weight: 700; font-size: 1.05rem; text-transform: uppercase; letter-spacing: 0.08em;">GenAI Response Layer ({lang}):</span><br/>
            <p style="color: #f1f5f9; font-size: 1.25rem; margin-top: 10px; line-height: 1.6; font-weight: 400;">{greetings[lang]}{reply}</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# INTERFACE 2: COMMAND CENTER DASHBOARD
# -------------------------------------------------------------------------
elif persona == "📊 Command Center Dashboard":
    st.markdown('<div class="custom-title">📊 Operational Intelligence Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-subtitle">Predictive GenAI insights generated by cross-referencing computer vision telemetry and gate metrics.</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""<div class="metric-card">
            <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Live Venue Load</span>
            <span style="font-size: 2.3rem; font-weight: 900; color: #ffffff; margin: 8px 0; display:block;">74,820</span>
            <span style="color: #22c55e; font-size: 0.9rem; font-weight: 600;">▲ 96% Capacity Peak</span>
        </div>""", unsafe_allow_html=True)
        
    with col2:
        st.markdown("""<div class="metric-card">
            <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Gate E Delay</span>
            <span style="font-size: 2.3rem; font-weight: 900; color: #f43f5e; margin: 8px 0; display:block;">28 Mins</span>
            <span style="color: #f43f5e; font-size: 0.9rem; font-weight: 600;">⚠️ Flow Congestion</span>
        </div>""", unsafe_allow_html=True)
        
    with col3:
        st.markdown("""<div class="metric-card">
            <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Resource Diversion</span>
            <span style="font-size: 2.3rem; font-weight: 900; color: #38bdf8; margin: 8px 0; display:block;">89.4%</span>
            <span style="color: #22c55e; font-size: 0.9rem; font-weight: 600;">✔ Sustainability Target</span>
        </div>""", unsafe_allow_html=True)
        
    with col4:
        st.markdown("""<div class="metric-card">
            <span style="color: #94a3b8; font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Tactical Deployments</span>
            <span style="font-size: 2.3rem; font-weight: 900; color: #a855f7; margin: 8px 0; display:block;">412 Units</span>
            <span style="color: #38bdf8; font-size: 0.9rem; font-weight: 600;">● Network Balanced</span>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-top:35px; margin-bottom:15px;">💡 AI Resource Optimization Protocol Matrix</div>', unsafe_allow_html=True)
    if st.button("Execute Automated Resource Balancing"):
        with st.spinner("🤖 Evaluating multi-agent optimization vector loops..."):
            time.sleep(0.7)
            st.markdown("""
            <div style="background: rgba(30, 41, 59, 0.35); border: 1px solid rgba(255,255,255,0.06); padding: 25px; border-radius: 16px; margin-top:10px;">
            <h3 style="color: #38bdf8; font-weight: 800; margin-top:0;">🛠️ GenAI Autonomous Operational Directives:</h3>
            <ul style="list-style-type: none; padding-left: 0; margin-bottom:0;">
                <li style="margin-bottom: 16px; font-size: 1.15rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 12px;"><strong style="color: #f43f5e;">🚨 Crowd Redirection Protocol:</strong> Computer vision shows structural saturation at <strong>Gate E</strong>. <em>Action:</em> Dynamically updated infrastructure digital routing indicators to distribute traffic streams into <strong>Gate F and Gate G</strong> (Wait matrix &lt; 4 minutes).</li>
                <li style="margin-bottom: 16px; font-size: 1.15rem; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 12px;"><strong style="color: #a855f7;">🏃 Human Resource Scaling:</strong> Reallocated 12 multi-lingual support operators from VIP Zone sections directly into Main Transit Terminal Checkpoint Bravo.</li>
                <li style="margin-bottom: 0px; font-size: 1.15rem;"><strong style="color: #38bdf8;">🍃 Infrastructure Efficiency:</strong> High-density sensor telemetry picked up sub-optimal baseline load levels on Cluster 4 distribution pipes. Automatically adjusted utility routing to conserve critical resources.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# INTERFACE 3: RAPID RESPONSE & CROWD SAFETY
# -------------------------------------------------------------------------
else:
    st.markdown('<div class="custom-title">🚨 Rapid Response & Predictive Safety Matrix</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-subtitle">Anonymized crowd density tracking and emergency decision-support framework.</div>', unsafe_allow_html=True)
    
    target_sector = st.selectbox("Select Core Infrastructure Diagnostic Node", ["Concourse Zone Alpha (Gate A Hub)", "Concourse Zone Bravo (Central Food Terminal)", "Concourse Zone Delta (Gate E Egress)"])
    
    st.markdown('<div style="font-size:1.25rem; font-weight:700; color:#ffffff; margin-top:20px; margin-bottom:10px;">🧠 Real-Time Predictive Risk Computations</div>', unsafe_allow_html=True)
    if st.button("Generate Threat Vector Analysis"):
        with st.spinner("Calculating fluid crowd flow vector equations..."):
            time.sleep(0.6)
            risk = random.randint(75, 95)
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #7f1d1d 0%, #450a0a 100%); border: 1px solid #f87171; padding: 26px; border-radius: 16px; margin-bottom: 25px; box-shadow: 0 15px 40px rgba(239, 68, 68, 0.25);">
                <h3 style="color: #fca5a5; margin: 0; font-weight: 900; letter-spacing: -0.01em;">⚠️ HIGH DENSITY SURGE PATTERN DETECTED: Score {risk}%</h3>
                <p style="color: #fef2f2; margin-top: 10px; font-size: 1.15rem; line-height: 1.6; margin-bottom:0;">AI system flags structural flow limits approaching critical parameters. Immediate mitigation protocols deployed.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.4); padding: 24px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.06);">
                <h5 style="font-size: 1.25rem; font-weight: 800; color: #38bdf8; margin-top:0; margin-bottom: 15px;">Automated Active Safety Interventions:</h5>
                <ol style="padding-left: 20px; color: #cbd5e1; font-size: 1.1rem; line-height: 1.75; margin-bottom:0;">
                    <li style="margin-bottom: 10px;"><strong>📢 Adaptive Audio Controls:</strong> Stadium internal speakers initialized to issue gentle velocity-control sound directives.</li>
                    <li style="margin-bottom: 10px;"><strong>🗺️ Dynamic Panel Matrix Swaps:</strong> Instantly updated primary routing boards to illuminate structural bypass corridors.</li>
                    <li style="margin-bottom: 0px;"><strong>🚒 Defensive Emergency Positioning:</strong> Alerted Medical Emergency Quick-Response Team 3 to establish stand-by formation at Forward Node Alpha-2.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

# Footer Layout
st.markdown("---")
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.95rem; font-weight: 500;'>Developed for Hack2Skill Virtual: PromptWars - Challenge 4 Submission</p>", unsafe_allow_html=True)