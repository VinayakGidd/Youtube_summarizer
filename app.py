import streamlit as st
from src.youtube_summary import summarize_youtube_video

def main():
    # Set up the Streamlit interface
    st.title("YouTube Video Summarization")

    # Input: YouTube Video URL
    video_url = st.text_input("Enter YouTube Video URL:")

    # Input: Summarization Method
    method = st.selectbox("Choose summarization method", ["tfidf", "bart"])

    # Summarization Button
    if st.button("Generate Summary"):
        if video_url:
            with st.spinner("Generating summary..."):
                try:
                    summary = summarize_youtube_video(video_url, method=method)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error generating summary: {str(e)}")
        else:
            st.warning("Please enter a valid YouTube video URL.")

if __name__ == "__main__":
    main()
