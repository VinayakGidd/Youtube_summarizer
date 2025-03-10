from src.youtube_summary import summarize_youtube_video

if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL: ")
    method = input("Choose summarization method (tfidf/bart): ").strip().lower()
    
    summary = summarize_youtube_video(video_url, method=method)
    print("nSummary:n")
    print(summary)