import unittest
from src.youtube_summary import summarize_youtube_video

class TestSummarizer(unittest.TestCase):
    def test_summarize_with_tfidf(self):
        video_url = "https://www.youtube.com/watch?v=Y8Tko2YC5hA"
        summary = summarize_youtube_video(video_url, method="tfidf")
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

    def test_summarize_with_bart(self):
        video_url = "https://www.youtube.com/watch?v=Y8Tko2YC5hA"
        summary = summarize_youtube_video(video_url, method="bart")
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

if __name__ == "__main__":
    unittest.main()