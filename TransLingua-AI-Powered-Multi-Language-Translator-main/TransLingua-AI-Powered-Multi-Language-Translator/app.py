from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="TransLingua – AI Translation Platform",
    page_icon="🌍",
    layout="centered"
)

# =========================
# Custom CSS Styling
# =========================
st.markdown("""
<style>

/* App background */
.stApp {
    background: linear-gradient(135deg, #0b132b, #1c2541, #3a506b);
    color: white;
}

/* Center container card */
.block-container {
    background: rgba(15, 23, 42, 0.85);
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
}

/* Main title */
h1 {
    text-align: center;
    color: #ffffff;
    font-weight: 800;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cbd5f5;
    margin-bottom: 25px;
}

/* Labels */
label {
    color: #e5e7eb !important;
    font-weight: 600;
}

/* Text area */
textarea {
    background-color: #020617 !important;
    color: #ffffff !important;
    border-radius: 14px !important;
    border: 1px solid #38bdf8 !important;
    padding: 14px;
    font-size: 16px;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background-color: #020617 !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid #38bdf8 !important;
}

/* Button */
button[kind="primary"] {
    background: linear-gradient(90deg, #38bdf8, #06b6d4);
    color: black !important;
    border-radius: 40px;
    height: 3.4em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    margin-top: 20px;
}

/* Button hover */
button[kind="primary"]:hover {
    background: linear-gradient(90deg, #06b6d4, #38bdf8);
    transform: scale(1.02);
}

/* Output text */
.stMarkdown, .stText {
    font-size: 18px;
    line-height: 1.7;
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 14px;
    font-size: 16px;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 30px;
    font-size: 14px;
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# App Title
# =========================
st.markdown("""
<h1>🌍 TransLingua</h1>
<p class="subtitle">
AI-Powered Universal Language Translation Platform
</p>
""", unsafe_allow_html=True)

# =========================
# Load Environment Variables
# =========================
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# =========================
# Initialize Gemini Model
# =========================
model = genai.GenerativeModel("models/gemini-flash-latest")

# =========================
# Translation Function
# =========================
def translate_text(text, source_language, target_language):
    if source_language == "Auto Detect":
        prompt = f"Detect the language and translate the following text to {target_language}: {text}"
    else:
        prompt = f"Translate the following text from {source_language} to {target_language}: {text}"

    response = model.generate_content(prompt)
    return response.text

# =========================
# Main App Logic
# =========================
def main():

    text = st.text_area("📝 Enter text to translate:")

    languages = [
        # Auto
        "Auto Detect",

        # Global
        "English", "Spanish", "French", "German", "Italian", "Portuguese",
        "Dutch", "Swedish", "Norwegian", "Danish", "Finnish", "Polish",
        "Czech", "Slovak", "Hungarian", "Romanian", "Greek", "Bulgarian",
        "Ukrainian", "Russian","Serbian",

        # Asian
        "Chinese", "Japanese", "Korean", "Hindi", "Tamil", "Telugu",
        "Marathi", "Bengali", "Gujarati", "Punjabi", "Urdu", "Kannada",
        "Malayalam", "Odia", "Assamese", "Nepali", "Sanskrit",
        "Thai", "Vietnamese", "Malay", "Indonesian", "Filipino",

        # Middle East
        "Arabic", "Hebrew", "Persian (Farsi)", "Turkish",

        # African
        "Swahili", "Amharic", "Yoruba", "Zulu", "Hausa", "Igbo",

        # Others
        "Latin", "Esperanto"
    ]

    source_language = st.selectbox("🌍 Select source language:", languages)
    target_language = st.selectbox("🌍 Select target language:", languages[1:])

    if st.button("🔁 Translate"):
        if text.strip():
            try:
                translated_text = translate_text(text, source_language, target_language)
                st.subheader("🗣️ Translated Text:")
                st.write(translated_text)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
        else:
            st.warning("⚠️ Please enter text to translate.")

# =========================
# Run App
# =========================
main()