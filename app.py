import streamlit as st
from tweet_generator import generate_tweets
from brand_analyzer import analyze_brand_voice
from hashtag_generator import generate_hashtags
import pandas as pd

# Page settings
st.set_page_config(
    page_title="AI Brand Tweet Generator",
    page_icon="🚀",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

body {
background-color:#0f172a;
}

.hero{
background: linear-gradient(90deg,#2563eb,#7c3aed);
padding:30px;
border-radius:12px;
color:white;
margin-bottom:30px;
}

.hero-title{
font-size:42px;
font-weight:700;
}

.hero-sub{
font-size:18px;
opacity:0.9;
}

.tweet-card{
background:#111827;
padding:20px;
border-radius:12px;
margin-bottom:15px;
border:1px solid #374151;
transition:0.3s;
}

.tweet-card:hover{
transform:scale(1.02);
border:1px solid #3b82f6;
}

.hash-badge{
background:#1f2937;
padding:8px 14px;
border-radius:20px;
margin-right:8px;
display:inline-block;
margin-top:8px;
color:#60a5fa;
font-weight:600;
}

.char-count{
color:#9ca3af;
font-size:12px;
margin-top:8px;
}

.sidebar-title{
font-size:20px;
font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------- Hero Header ----------
st.markdown("""
<div class="hero">
<div class="hero-title">🚀 AI Brand Tweet Generator</div>
<div class="hero-sub">
Generate AI-style tweets, brand voice insights and marketing hashtags instantly.
</div>
</div>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.markdown('<div class="sidebar-title">Brand Information</div>', unsafe_allow_html=True)

brand = st.sidebar.text_input("Brand Name")
industry = st.sidebar.text_input("Industry")

campaign = st.sidebar.selectbox(
    "Campaign Objective",
    ["Engagement","Promotion","Awareness"]
)

style = st.sidebar.selectbox(
    "Tweet Style",
    ["Professional","Luxury","Friendly","Bold","Inspirational"]
)

product = st.sidebar.text_area("Product Description")

generate = st.sidebar.button("🚀 Generate Tweets")

# ---------- Main Logic ----------
if generate:

    if brand == "":
        st.warning("Please enter a brand name.")
        st.stop()

    st.subheader("🧠 Brand Voice Analysis")

    voice = analyze_brand_voice(brand, industry, product)

    for v in voice:
        st.write("•", v)

    st.divider()

    st.subheader("🐦 Generated Tweets")

    tweets = generate_tweets(brand, industry, campaign, product, style)

    col1, col2 = st.columns(2)

    for i, tweet in enumerate(tweets):

        char_count = len(tweet)

        tweet_html = f"""
        <div class="tweet-card">
        {tweet}
        <div class="char-count">{char_count}/280 characters</div>
        </div>
        """

        if i % 2 == 0:
            with col1:
                st.markdown(tweet_html, unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(tweet_html, unsafe_allow_html=True)

    st.divider()

    st.subheader("🔥 Suggested Hashtags")

    hashtags = generate_hashtags(brand, industry)

    for tag in hashtags:
        st.markdown(f'<span class="hash-badge">{tag}</span>', unsafe_allow_html=True)

    st.divider()

    # Download CSV
    df = pd.DataFrame(tweets, columns=["Generated Tweets"])

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Tweets CSV",
        csv,
        "generated_tweets.csv",
        "text/csv"
    )

else:
    st.info("👉 Enter brand details in the sidebar and click **Generate Tweets** to start.")