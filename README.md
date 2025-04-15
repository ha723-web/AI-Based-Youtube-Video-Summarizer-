# 📽️ AI-Based YouTube Video Summarizer

A Streamlit web app that lets you paste a YouTube video URL, transcribes the video, summarizes its content using NLP, and visualizes keywords.

## 🚀 Features

- 🔗 Accepts YouTube video URL
- 📜 Transcribes using `YouTubeTranscriptAPI`
- 🧠 Summarizes using `facebook/bart-large-cnn`
- ☁️ Generates keyword cloud
- 🌍 Multilingual summary translation
- ✅ Built with Python, Streamlit, Hugging Face, and Google Translate

## 💻 Installation

```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
pip install -r requirements.txt

## Project Structure


youtube-summarizer/
├── app.py                # Main Streamlit application
├── utils.py              # Helper functions for summarization, transcription, translation, etc.
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


## 💻 Commands to Run
# Navigate to your project folder
cd "/Users/harshiniakunuri/Desktop/Git Projects/AI-Based-Youtube-Video-Summarizer"

# Activate virtual env
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip setuptools wheel
pip install streamlit youtube-transcript-api transformers torch torchvision torchaudio wordcloud matplotlib langdetect deep-translator

# Run the Streamlit app
streamlit run app.py
