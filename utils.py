from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from langdetect import detect
from deep_translator import GoogleTranslator


def get_video_id(youtube_url):
    if "v=" in youtube_url:
        return youtube_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[1]
    return None

def get_transcript(video_url):
    video_id = get_video_id(video_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry["text"] for entry in transcript])
    return full_text

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + " "
    return summary.strip()

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    buffer = BytesIO()
    wordcloud.to_image().save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str


def translate_text(text, target_lang="es"):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

