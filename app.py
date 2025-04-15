import streamlit as st
from utils import get_transcript, summarize_text, generate_wordcloud, translate_text

st.set_page_config(page_title="🎥 YouTube Video Summarizer", layout="centered")

st.title("🎥 AI YouTube Video Summarizer")
st.write("Paste a YouTube video link below. This app transcribes, summarizes, and visualizes top topics from it.")

url = st.text_input("🔗 Enter YouTube Video URL")

if url:
    with st.spinner("⏳ Fetching and transcribing video..."):
        try:
            full_text = get_transcript(url)
            st.success("✅ Transcript fetched successfully!")
        except Exception as e:
            st.error(f"Failed to fetch transcript: {e}")
            st.stop()

    with st.spinner("🧠 Generating summary..."):
        summary = summarize_text(full_text)
        st.subheader("📝 Summary")
        st.write(summary)

    st.subheader("☁️ Keyword WordCloud")
    img_data = generate_wordcloud(full_text)
    st.image(f"data:image/png;base64,{img_data}")

    st.subheader("🌍 Translate Summary")
    lang = st.selectbox("Choose language", ["en", "es", "fr", "de", "te", "hi"])
    translated_summary = translate_text(summary, lang)
    st.write(translated_summary)
