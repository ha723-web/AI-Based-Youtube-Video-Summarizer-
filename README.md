# 🎥 AI-Based YouTube Video Summarizer

A Streamlit web app that lets you paste a YouTube video URL, transcribes the video, summarizes its content using NLP, and visualizes keywords.

---

## 🚀 Features

- 🔗 Accepts **YouTube video URL**
- 📜 Transcribes using `YouTubeTranscriptAPI`
- ✨ Summarizes using `facebook/bart-large-cnn`
- ☁️ Generates **keyword cloud**
- 🌍 Multilingual summary translation using `deep-translator`
- ✅ Built with **Python**, **Streamlit**, **Hugging Face**, and `Torch`

---

## 🛠️ Tech Stack

| Category            | Technology                              |
|---------------------|------------------------------------------|
| **Language**        | Python 3.10+ / 3.13                     |
| **Web Framework**   | Streamlit                              |
| **NLP Models**      | Hugging Face Transformers (`BART`)     |
| **Transcription**   | YouTubeTranscriptAPI                   |
| **Summarization**   | `facebook/bart-large-cnn`              |
| **Translation**     | Deep Translator (Google API wrapper)   |
| **Visualization**   | WordCloud, Matplotlib                  |
| **Device Support**  | MPS for Apple Silicon / CPU            |

---

## 📁 Project Structure

```yaml
AI-Based-Youtube-Video-Summarizer/
├── app.py                # Streamlit main app
├── utils.py              # Functions for summarization, transcription, translation, etc.
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


✅ 💻 Installation


# Step 1: Clone the repo
git clone https://github.com/ha723-web/AI-Based-Youtube-Video-Summarizer-.git
cd AI-Based-Youtube-Video-Summarizer-

# Step 2: Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Upgrade pip tools
pip install --upgrade pip setuptools wheel

# Step 4: Install dependencies
pip install streamlit youtube-transcript-api transformers torch torchvision torchaudio
pip install wordcloud matplotlib langdetect deep-translator
