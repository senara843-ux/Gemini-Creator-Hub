import streamlit as st
import os
from dotenv import load_dotenv

# --- KEY LOADING BLOCK: Loads key securely from .env or Streamlit Secrets ---
LOCAL_API_KEY = None

# 1. Try to get the key from the local .env file first
try:
    load_dotenv()
    LOCAL_API_KEY = os.getenv("GEMINI_API_KEY")
except Exception:
    # If python-dotenv fails, just continue
    pass

# 2. Check Streamlit Cloud secrets (fallback for deployed version)
if not LOCAL_API_KEY:
    try:
        LOCAL_API_KEY = st.secrets["GEMINI_API_KEY"]
    except:
        pass

# 3. Final check: If key is missing, stop the app and show an error
if not LOCAL_API_KEY:
    st.error("❌ ERROR: Gemini API Key is missing. Please set GEMINI_API_KEY in your local .env file or Streamlit Cloud Secrets.")
    st.stop()
    
# Import functions (These imports now happen successfully after the key check)
from creator_ai import (
    generate_script_outline, 
    generate_captions_and_hashtags, 
    generate_thumbnail_ideas, 
    generate_video_titles
)
# --- END KEY LOADING BLOCK ---


st.set_page_config(page_title="Gemini Creator Hub", layout="wide")
st.title("✍️ Gemini Creator Hub: Your AI Content Toolkit")
st.markdown("Kickstart your content creation process with AI-powered brainstorming!")
st.markdown("---")

content_topic = st.text_area(
    "1️⃣ Enter your core content topic or idea here:",
    height=100
)

if content_topic:
    st.subheader("2️⃣ Choose Your Content Tool")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Script Outline", 
        "📸 Captions & Hashtags", 
        "🖼️ Thumbnail Ideas", 
        "🎬 Video Titles"
    ])

    # --- TAB 1: Script Outline ---
    with tab1:
        st.markdown("#### Generate a Structured Video/Blog Script")
        audience = st.text_input("Target Audience (e.g., 'new parents', 'tech enthusiasts'):", value="general", key="audience_input")
        if st.button("Generate Script Outline", key="script_btn"):
            with st.spinner("Crafting your script outline..."):
                try:
                    # PASS THE API KEY HERE
                    outline = generate_script_outline(content_topic, audience, api_key=LOCAL_API_KEY)
                    st.markdown("### Generated Outline")
                    st.markdown(outline)
                except Exception as e:
                    st.error(f"Error calling Gemini: {e}")

    # --- TAB 2: Captions & Hashtags ---
    with tab2:
        st.markdown("#### Create Engaging Social Media Posts")
        platform = st.selectbox("Platform:", ["Instagram", "TikTok", "Facebook", "Twitter"], key="platform_select")
        tone = st.selectbox("Tone:", ["friendly", "professional", "humorous", "exciting"], key="tone_select")
        if st.button("Generate Captions & Hashtags", key="caption_btn"):
            with st.spinner(f"Generating {platform} captions and hashtags..."):
                try:
                    # PASS THE API KEY HERE
                    captions_hashtags = generate_captions_and_hashtags(content_topic, platform, tone, api_key=LOCAL_API_KEY)
                    st.markdown("### Generated Captions & Hashtags")
                    st.markdown(captions_hashtags)
                except Exception as e:
                    st.error(f"Error calling Gemini: {e}")

    # --- TAB 3: Thumbnail Ideas ---
    with tab3:
        st.markdown("#### Brainstorm Click-Worthy Thumbnails")
        num_thumbnails = st.slider("Number of ideas:", 1, 5, 3, key="thumb_slider")
        if st.button("Generate Thumbnail Ideas", key="thumbnail_btn"):
            with st.spinner("Brainstorming visual concepts..."):
                try:
                    # PASS THE API KEY HERE
                    thumbnails = generate_thumbnail_ideas(content_topic, num_thumbnails, api_key=LOCAL_API_KEY)
                    st.markdown("### Generated Thumbnail Ideas")
                    st.markdown(thumbnails)
                except Exception as e:
                    st.error(f"Error calling Gemini: {e}")

    # --- TAB 4: Video Titles ---
    with tab4:
        st.markdown("#### Generate Catchy, Optimized Video Titles")
        num_titles = st.slider("Number of titles:", 3, 10, 5, key="titles_slider")
        if st.button("Generate Video Titles", key="titles_btn"):
            with st.spinner("Creating amazing titles..."):
                try:
                    # PASS THE API KEY HERE
                    titles = generate_video_titles(content_topic, num_titles, api_key=LOCAL_API_KEY)
                    st.markdown("### Generated Video Titles")
                    st.markdown(titles)
                except Exception as e:
                    st.error(f"Error calling Gemini: {e}")
else:
    st.info("💡 Enter your idea above to unlock the Gemini Creator Hub tools!")