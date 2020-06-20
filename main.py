# Download
# import nltk
# nltk.download('vader_lexicon')
# Inspiration: https://amiham-singh.github.io/ 
# Small example: https://towardsdatascience.com/https-towardsdatascience-com-algorithmic-trading-using-sentiment-analysis-on-news-articles-83db77966704
# Dependencies
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy

## Sentiment Analysis with NLTK
# Initialize sentiment intensity analyzer (see https://www.nltk.org/api/nltk.sentiment.html)
sia = SentimentIntensityAnalyzer()
# Get before and after text files as single strings
file_path = os.path.join(os.getcwd(), "data", "qaddafi", "after.txt")
with open(file_path, 'r') as file:
    after = file.read().replace("\n", "")
file_path = os.path.join(os.getcwd(), "data", "qaddafi", "before.txt")
with open(file_path, 'r') as file:
    before = file.read().replace("\n", "")
# Get sentiment score dictionaries
sentiments= {
    "before" : sia.polarity_scores(before),
    "after" : sia.polarity_scores(after)
    }    

## SpaCy Tokenization
# Load English NLP decoder
nlp = spacy.load("en_core_web_sm")
# Tokenize
token_before = nlp(before)
token_after = nlp(after)
# TODO: Count adjectives/verbs