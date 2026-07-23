"""Unit testing for sentiment_analysis.py file"""
import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    """inherit TestCase class in TestSentimentAnalyzer class"""
    def test_sentiment_analyzer(self):
        """Function to test sentiment_analyzer function"""
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result_1["label"], "SENT_POSITIVE")
        result_2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result_2["label"], "SENT_NEGATIVE")
        result_3 = sentiment_analyzer("I am neural on Python")
        self.assertEqual(result_3["label"], "SENT_NEUTRAL")
unittest.main()
