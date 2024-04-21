import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Sample text
text = "NLTK is a powerful tool for natural language processing."

# Tokenize the text
tokens = word_tokenize(text)

# Perform sentiment analysis using VADER
sia = SentimentIntensityAnalyzer()
sentiment_scores = sia.polarity_scores(text)

# Determine sentiment based on scores
if sentiment_scores['compound'] >= 0.05:
    sentiment = 'Positive'
elif sentiment_scores['compound'] <= -0.05:
    sentiment = 'Negative'
else:
    sentiment = 'Neutral'

print(f"Sentiment: {sentiment}")