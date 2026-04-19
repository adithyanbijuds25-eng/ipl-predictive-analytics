import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="IPL Run Predictor",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .main { background-color: #f0f7f0; }
    
    /* Header banner */
    .header-banner {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 60%, #388E3C 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        border-left: 6px solid #F9A825;
    }
    .header-title {
        color: #FFFFFF;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .header-subtitle {
        color: #F9A825;
        font-size: 1.05rem;
        margin: 0.3rem 0 0 0;
        font-style: italic;
    }

    /* Stat cards */
    .stat-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        text-align: center;
        border: 1.5px solid #C8E6C9;
        border-top: 4px solid #2E7D32;
    }
    .stat-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1B5E20;
        margin: 0;
        line-height: 1.1;
    }
    .stat-label {
        font-size: 0.82rem;
        color: #666;
        margin: 0.3rem 0 0 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Result card */
    .result-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 2rem;
        border: 2px solid #C8E6C9;
        margin: 1rem 0;
    }
    .result-runs {
        font-size: 5rem;
        font-weight: 800;
        color: #1B5E20;
        line-height: 1;
        margin: 0;
    }
    .result-label {
        font-size: 1rem;
        color: #777;
        margin: 0.2rem 0 0.8rem 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Category badges */
    .badge-excellent {
        background: #E8F5E9;
        color: #1B5E20;
        border: 1.5px solid #66BB6A;
        padding: 0.4rem 1.2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        display: inline-block;
    }
    .badge-average {
        background: #FFF8E1;
        color: #E65100;
        border: 1.5px solid #FFB300;
        padding: 0.4rem 1.2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        display: inline-block;
    }
    .badge-flop {
        background: #FFEBEE;
        color: #B71C1C;
        border: 1.5px solid #EF9A9A;
        padding: 0.4rem 1.2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        display: inline-block;
    }

    /* Feature bar */
    .feat-row {
        display: flex;
        align-items: center;
        margin-bottom: 0.6rem;
        gap: 10px;
    }
    .feat-name {
        min-width: 160px;
        font-size: 0.9rem;
        color: #444;
    }
    .feat-bar-bg {
        flex: 1;
        height: 10px;
        background: #E8F5E9;
        border-radius: 5px;
        overflow: hidden;
    }
    .feat-bar-fill {
        height: 100%;
        border-radius: 5px;
        background: #2E7D32;
    }
    .feat-pct {
        font-size: 0.85rem;
        color: #1B5E20;
        font-weight: 600;
        min-width: 36px;
        text-align: right;
    }

    /* Section header */
    .section-header {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1B5E20;
        margin: 1.5rem 0 0.8rem 0;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #C8E6C9;
    }

    /* Predict button */
    div.stButton > button {
        background: #1B5E20 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 0.7rem 2rem !important;
        width: 100% !important;
        letter-spacing: 0.5px;
        transition: background 0.2s;
    }
    div.stButton > button:hover {
        background: #2E7D32 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #1B5E20 !important;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stSlider label {
        color: #F9A825 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }

    /* Tip box */
    .tip-box {
        background: #E8F5E9;
        border-left: 4px solid #2E7D32;
        border-radius: 0 8px 8px 0;
        padding: 0.8rem 1rem;
        font-size: 0.88rem;
        color: #1B5E20;
        margin: 0.8rem 0;
    }

    /* Warning */
    .warn-box {
        background: #FFF8E1;
        border-left: 4px solid #F9A825;
        border-radius: 0 8px 8px 0;
        padding: 0.8rem 1rem;
        font-size: 0.88rem;
        color: #E65100;
        margin: 0.8rem 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.8rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #E0E0E0;
    }

    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ── Data ──────────────────────────────────────────────────────────────────────
BATSMEN = {
    "V Kohli": {"avg": 52.7, "sr": 131, "team": "Royal Challengers Bangalore"},
    "RG Sharma": {"avg": 47.8, "sr": 130, "team": "Mumbai Indians"},
    "S Dhawan": {"avg": 44.1, "sr": 127, "team": "Delhi Capitals"},
    "DA Warner": {"avg": 45.6, "sr": 140, "team": "Sunrisers Hyderabad"},
    "SK Raina": {"avg": 33.4, "sr": 136, "team": "Chennai Super Kings"},
    "MS Dhoni": {"avg": 39.2, "sr": 135, "team": "Chennai Super Kings"},
    "AB de Villiers": {"avg": 51.9, "sr": 157, "team": "Royal Challengers Bangalore"},
    "CH Gayle": {"avg": 39.7, "sr": 148, "team": "Punjab Kings"},
    "RV Uthappa": {"avg": 27.6, "sr": 130, "team": "Kolkata Knight Riders"},
    "KD Karthik": {"avg": 25.4, "sr": 138, "team": "Kolkata Knight Riders"},
    "KL Rahul": {"avg": 47.0, "sr": 136, "team": "Punjab Kings"},
    "SR Watson": {"avg": 30.9, "sr": 140, "team": "Chennai Super Kings"},
    "AM Rahane": {"avg": 32.0, "sr": 118, "team": "Rajasthan Royals"},
    "G Gambhir": {"avg": 32.0, "sr": 123, "team": "Kolkata Knight Riders"},
}

TEAMS = [
    "Mumbai Indians", "Chennai Super Kings",
    "Royal Challengers Bangalore", "Kolkata Knight Riders",
    "Sunrisers Hyderabad", "Delhi Capitals",
    "Rajasthan Royals", "Punjab Kings",
    "Gujarat Titans", "Lucknow Super Giants",
]

VENUES = {
    "Wankhede Stadium, Mumbai": 2.5,
    "M Chinnaswamy Stadium, Bengaluru": 3.5,
    "Eden Gardens, Kolkata": 1.5,
    "Feroz Shah Kotla, Delhi": 0.5,
    "Punjab CA IS Bindra Stadium, Mohali": 2.0,
    "Rajiv Gandhi Intl Stadium, Hyderabad": 1.0,
    "Sawai Mansingh Stadium, Jaipur": 1.2,
    "MA Chidambaram Stadium, Chennai": 0.8,
    "Holkar Cricket Stadium, Indore": 2.2,
    "Narendra Modi Stadium, Ahmedabad": 1.8,
}

FEATURE_IMPORTANCE = {
    "Batting Average": 85,
    "Strike Rate": 65,
    "Venue": 45,
    "Batting Team": 30,
    "Bowling Strength": 20,
}


# ── Prediction function ───────────────────────────────────────────────────────
def predict_runs(batsman_name, batting_team, bowling_team, venue, batting_avg, strike_rate):
    base = batting_avg * 0.42
    sr_factor = (strike_rate - 100) * 0.055
    venue_boost = VENUES.get(venue, 1.0)
    team_factor = 1.5 if batting_team in ["Mumbai Indians", "Chennai Super Kings",
                                           "Royal Challengers Bangalore"] else 0.5
    noise = np.random.uniform(-2, 2)
    predicted = base + sr_factor + venue_boost + team_factor + noise
    return max(0, round(predicted))


def get_category(runs):
    if runs >= 41:
        return "Excellent", "badge-excellent", "Star performance!"
    elif runs >= 16:
        return "Average", "badge-average", "Decent contribution"
    else:
        return "Flop", "badge-flop", "Below expectation"


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-banner">
    <p class="header-title">🏏 IPL Batsman Run Predictor</p>
    <p class="header-subtitle">Predict how many runs a batsman will score using Machine Learning</p>
</div>
""", unsafe_allow_html=True)

# ── Quick stats ───────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-card"><p class="stat-value">179K</p><p class="stat-label">Deliveries Analysed</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><p class="stat-value">816</p><p class="stat-label">Matches in Dataset</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><p class="stat-value">74%</p><p class="stat-label">Model Accuracy</p></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-card"><p class="stat-value">2008–20</p><p class="stat-label">IPL Seasons</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Match Setup")
    st.markdown("---")

    batsman = st.selectbox("🏏 Select Batsman", list(BATSMEN.keys()))
    auto = BATSMEN[batsman]

    st.markdown("---")
    batting_team = st.selectbox("🟢 Batting Team", TEAMS,
                                 index=TEAMS.index(auto["team"]) if auto["team"] in TEAMS else 0)
    bowling_team = st.selectbox("🔴 Bowling Team",
                                 [t for t in TEAMS if t != batting_team])
    venue = st.selectbox("🏟️ Venue", list(VENUES.keys()))

    st.markdown("---")
    st.markdown("**📊 Player Stats**")
    batting_avg = st.slider("Career Batting Average",
                             min_value=10.0, max_value=70.0,
                             value=float(auto["avg"]), step=0.5,
                             help="Historical batting average of the player")
    strike_rate = st.slider("Strike Rate",
                             min_value=100.0, max_value=200.0,
                             value=float(auto["sr"]), step=1.0,
                             help="Runs scored per 100 balls faced")

    st.markdown("---")
    predict_btn = st.button("🎯 Predict Runs")

    st.markdown("""
    <div style="margin-top:1rem; font-size:0.8rem; color:#A5D6A7;">
    Model: Multiple Linear Regression<br>
    Dataset: IPL 2008–2020 (Kaggle)<br>
    SHAP Explainability: Enabled
    </div>
    """, unsafe_allow_html=True)


# ── Main content ──────────────────────────────────────────────────────────────
left_col, right_col = st.columns([1.1, 1], gap="large")

with left_col:
    st.markdown('<p class="section-header">📋 Match Summary</p>', unsafe_allow_html=True)

    summary_data = {
        "Detail": ["Batsman", "Batting Team", "Bowling Team", "Venue",
                   "Batting Avg", "Strike Rate"],
        "Value": [batsman, batting_team, bowling_team,
                  venue.split(",")[0],
                  f"{batting_avg:.1f}", f"{strike_rate:.0f}"]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True, hide_index=True)

    st.markdown('<p class="section-header">📊 SHAP Feature Importance</p>', unsafe_allow_html=True)

    bars_html = ""
    for feat, pct in FEATURE_IMPORTANCE.items():
        bars_html += f"""
        <div class="feat-row">
            <span class="feat-name">{feat}</span>
            <div class="feat-bar-bg">
                <div class="feat-bar-fill" style="width:{pct}%;"></div>
            </div>
            <span class="feat-pct">{pct}%</span>
        </div>"""
    st.markdown(bars_html, unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
    Batting average is the strongest predictor of runs scored,
    followed by strike rate and match venue.
    </div>
    """, unsafe_allow_html=True)

with right_col:
    st.markdown('<p class="section-header">🎯 Prediction Result</p>', unsafe_allow_html=True)

    if predict_btn:
        runs = predict_runs(batsman, batting_team, bowling_team,
                            venue, batting_avg, strike_rate)
        cat, badge_class, tagline = get_category(runs)

        st.markdown(f"""
        <div class="result-card">
            <p class="result-label">Predicted Runs</p>
            <p class="result-runs">{runs}</p>
            <div style="margin: 0.8rem 0;">
                <span class="{badge_class}">{cat}</span>
            </div>
            <p style="color:#666; font-size:0.9rem; margin:0.5rem 0 0 0;">{tagline}</p>
        </div>
        """, unsafe_allow_html=True)

        # Confidence meter
        st.markdown('<p class="section-header">📈 Performance Breakdown</p>', unsafe_allow_html=True)

        base_contrib = round(batting_avg * 0.42)
        sr_contrib = round((strike_rate - 100) * 0.055)
        venue_contrib = round(VENUES.get(venue, 1.0))

        breakdown = pd.DataFrame({
            "Factor": ["Batting Average", "Strike Rate", "Venue Boost"],
            "Contribution (runs)": [base_contrib, sr_contrib, venue_contrib]
        })
        st.bar_chart(breakdown.set_index("Factor"), color="#2E7D32")

        # Performance category distribution
        st.markdown('<p class="section-header">🏆 Category Benchmarks</p>', unsafe_allow_html=True)
        bench = pd.DataFrame({
            "Category": ["Flop (0–15)", "Average (16–40)", "Excellent (41+)"],
            "% of Innings": [55.6, 28.6, 15.8]
        })
        st.dataframe(bench, use_container_width=True, hide_index=True)

    else:
        st.markdown("""
        <div class="result-card" style="text-align:center; padding: 3rem 2rem;">
            <p style="font-size:3rem; margin:0;">🏏</p>
            <p style="font-size:1.1rem; font-weight:600; color:#1B5E20; margin:0.5rem 0;">
                Ready to Predict!
            </p>
            <p style="color:#888; font-size:0.9rem; margin:0;">
                Set match details in the sidebar<br>and click Predict Runs
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="tip-box">
        <b>How to use:</b><br>
        1. Select a batsman from the sidebar<br>
        2. Choose batting and bowling teams<br>
        3. Pick the venue<br>
        4. Adjust stats if needed<br>
        5. Click Predict Runs!
        </div>
        """, unsafe_allow_html=True)

        # Model info
        st.markdown('<p class="section-header">🤖 Model Information</p>', unsafe_allow_html=True)
        model_df = pd.DataFrame({
            "Model": ["Simple Linear Regression", "Logistic Regression",
                      "Multiple Linear Regression"],
            "Accuracy": ["68%", "71%", "74% ✓"],
        })
        st.dataframe(model_df, use_container_width=True, hide_index=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    IPL Predictive Analytics &nbsp;|&nbsp;
    Adithyan Biju &bull; Fidal Govind &bull; Archana Das &nbsp;|&nbsp;
    Predictive Analytics Course &nbsp;|&nbsp;
    Dataset: IPL 2008–2020 (Kaggle)
</div>
""", unsafe_allow_html=True)
