


import whisper
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from src.summarization import summarize_with_tfidf, summarize_with_bart

def extract_video_id(url):
    """Extract YouTube video ID from different URL formats."""
    parsed_url = urlparse(url)
    if parsed_url.netloc == "youtu.be":
        return parsed_url.path[1:]  # Extracts the video ID from shortened URLs
    elif "youtube.com" in parsed_url.netloc:
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]  # Extracts video ID from full URLs
    return None

def download_audio(video_url):
    """Download audio from a YouTube video."""
    yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
    audio_stream = yt.streams.filter(only_audio=True).first()
    
    if not audio_stream:
        raise Exception("No audio stream available for this video.")
    
    audio_path = "audio.mp4"
    audio_stream.download(filename=audio_path)
    return audio_path

def generate_subtitles(audio_file):
    """Generate subtitles using Whisper AI."""
    model = whisper.load_model("base")  # Use "small", "medium", or "large" for better accuracy
    result = model.transcribe(audio_file)
    return result["text"]

def get_subtitle(video_url):
    """Fetch subtitles from YouTube or generate them from audio."""
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL provided."
    
    try:
        # Try fetching subtitles from YouTube directly
        subtitles = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return " ".join([x['text'] for x in subtitles])
    except Exception as e:
        print(f"Error fetching subtitles from YouTube: {e}")
        print("Attempting to generate subtitles from audio...")

        try:
            audio_file = download_audio(video_url)
            return generate_subtitles(audio_file)
        except Exception as audio_error:
            return f"Failed to generate subtitles from audio: {audio_error}"

def summarize_youtube_video(video_url, method="bart"):
    """Summarize a YouTube video using TF-IDF or BART model."""
    subtitle = get_subtitle(video_url)
    
    if not subtitle or "Failed" in subtitle:
        return "Could not fetch or generate subtitles for this video."

    if method == "tfidf":
        return summarize_with_tfidf(subtitle)
    elif method == "bart":
        return summarize_with_bart(subtitle)
    else:
        return "Invalid summarization method."
