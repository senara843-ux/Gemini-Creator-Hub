# Gemini-Creator-Hub
AI Content Creator Toolkit using Gemini and Streamlit. Generates structured script outlines, social media captions, and thumbnail ideas from a single topic.
# ✍️ Gemini Creator Hub: AI Content Assistant

This project is a multi-functional toolkit designed to rapidly accelerate the content creation process. Leveraging the **Google Gemini API**, it helps creators quickly brainstorm and structure various content assets—from long-form video scripts to short-form social media captions and titles—all from a single topic input.

### ✨ Key Features

The application is built around four primary tools, each accessible via a dedicated tab:

1.  **📝 Script Outline Generator:** Creates a professional structure for videos or blogs (Hook, 3 Main Points, CTA).
2.  **📸 Caption & Hashtag Creator:** Generates multiple captions and optimized hashtags tailored for platforms like Instagram or TikTok.
3.  **🖼️ Thumbnail Idea Brainstormer:** Provides distinct, visually descriptive concepts (image subject, mood, text overlay) that can be passed directly to an image generation AI.
4.  **🎬 Video Title Generator:** Generates a list of catchy, click-worthy titles optimized for engagement.

### ⚙️ Technology Stack

* **Core AI:** **Google Gemini API** (`gemini-2.5-flash` model) for advanced, creative text generation and structuring.
* **Web Framework:** **Streamlit** for rapid development and deployment of the interactive user interface.
* **Security:** API Key managed securely using **Streamlit Cloud Secrets** and `python-dotenv` for local development.

### 🚀 Deployment & Access

The Gemini Creator Hub is live and fully accessible on the Streamlit Community Cloud.

**[Add Your Public Streamlit URL Here]** (e.g., `https://[your-username]-gemini-creator-hub.streamlit.app/`)

### 🗂️ Files in this Repository

| File Name | Description |
| :--- | :--- |
| `creator_hub_app.py` | The main Streamlit application file containing the UI layout, tabs, and buttons. |
| `creator_ai.py` | The backend Python logic containing the four core functions that call the Gemini API with specific prompts. |
| `requirements.txt` | Lists all necessary Python dependencies (streamlit, google-genai, etc.) for the cloud host to install. |
| `LICENSE` | The **MIT License** governing the open-source reuse of this project's code. |
