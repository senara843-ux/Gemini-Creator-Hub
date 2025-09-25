import os
from google import genai
import streamlit as st

# The client is initialized inside each function, as it needs the API key
# passed to it from the main app's secure loading mechanism.
MODEL = "gemini-2.5-flash" 

def initialize_gemini_client(api_key):
    """Initializes and returns the Gemini client."""
    if not api_key:
        # This should have been caught earlier, but is a final safety check
        raise ValueError("Gemini client initialization failed: API Key is missing.")
    client = genai.Client(api_key=api_key)
    return client

# --- 1. Script Outline Function ---
def generate_script_outline(topic, audience="general", api_key=None):
    """Generates a structured script outline for a given topic."""
    client = initialize_gemini_client(api_key)
    prompt = (
        f"You are a professional content writer. Generate a detailed script outline for a video about '{topic}'. "
        f"Tailor it for a {audience} audience. "
        "Include: A catchy hook, 3 main points with brief explanations, "
        "and a strong call to action. Format the output using markdown headings and lists."
    )
    response = client.models.generate_content(model=MODEL, contents=prompt, config={"temperature": 0.7})
    return response.text

# --- 2. Caption & Hashtag Function ---
def generate_captions_and_hashtags(content_summary, platform="Instagram", tone="friendly", api_key=None):
    """Generates social media captions and relevant hashtags."""
    client = initialize_gemini_client(api_key)
    prompt = (
        f"Generate 3 {tone} captions and 7 relevant hashtags for a {platform} post. "
        f"The content is summarized as: '{content_summary}'. "
        "Captions should be short and engaging. Hashtags should be a mix of broad and niche."
    )
    response = client.models.generate_content(model=MODEL, contents=prompt, config={"temperature": 0.8})
    return response.text

# --- 3. Thumbnail Idea Function ---
def generate_thumbnail_ideas(video_topic, count=3, api_key=None):
    """Brainstorms visual thumbnail ideas for a video."""
    client = initialize_gemini_client(api_key)
    prompt = (
        f"Brainstorm {count} distinct, visually descriptive thumbnail ideas for a video about '{video_topic}'. "
        "For each idea, describe the main image, the emotional mood, and the text overlay (e.g., 'BIG TEXT HERE')."
    )
    response = client.models.generate_content(model=MODEL, contents=prompt, config={"temperature": 0.9})
    return response.text

# --- 4. Video Title Function ---
def generate_video_titles(video_topic, count=5, api_key=None):
    """Generates catchy video titles for YouTube or similar platforms."""
    client = initialize_gemini_client(api_key)
    prompt = (
        f"Generate {count} catchy and click-worthy video titles for a video about '{video_topic}'. "
        "Titles should include power words and numbers where appropriate. Output as a numbered list."
    )
    response = client.models.generate_content(model=MODEL, contents=prompt, config={"temperature": 0.9})
    return response.text