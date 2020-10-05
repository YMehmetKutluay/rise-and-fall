# Download
# import nltk
# nltk.download('vader_lexicon')
# Inspiration: https://amiham-singh.github.io/ 
# Small example: https://towardsdatascience.com/https-towardsdatascience-com-algorithmic-trading-using-sentiment-analysis-on-news-articles-83db77966704
# Dependencies
# Print 
print("Initializing sentiment analyzer")
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
import pandas as pd
import sys

## Sentiment Analysis with NLTK
# Select political leader from command line
leader = sys.argv[1]
# Initialize sentiment intensity analyzer (see https://www.nltk.org/api/nltk.sentiment.html)
sia = SentimentIntensityAnalyzer()
# Print
print("Loading data")
# Get rise and fall text files as single strings
file_path = os.path.join(os.getcwd(), "data", leader, "fall.txt")
with open(file_path, 'r', encoding = "utf-8") as file:
    fall = file.read().replace("\n", "")
file_path = os.path.join(os.getcwd(), "data", leader, "rise.txt")
with open(file_path, 'r', encoding = "utf-8") as file:
    rise = file.read().replace("\n", "")
# Get sentiment score dictionaries
sentiments = {
    "rise" : sia.polarity_scores(rise),
    "fall" : sia.polarity_scores(fall)
    }    
# Print
print("The NLTK sentiment analysis is as follows:")
for k, y in sentiments.items():
    print(k, "-->", y)
## SpaCy Tokenization
# Print
print("Initiating word type analysis")
# Load English NLP decoder
nlp = spacy.load("en_core_web_sm")
# Tokenize
token_before = nlp(rise)
token_after = nlp(fall)
## Count adjectives and verbs for both articles
# For rise article
# Initiate pandas dataframe
pd_rise = pd.DataFrame({"word":[], "pos_value":[]})
for token in token_before:
    # Make row of data
    sub_pd = pd.DataFrame({"word":str(token), "pos_value":token.pos_}, index = [0])
    # Append to pd_rise
    pd_rise = pd_rise.append(sub_pd, ignore_index = True)
# Group by pos_value and count
n_rows = len(pd_rise)
pd_rise = (
    pd_rise
    .groupby("pos_value")
    .agg(rise_count = ("pos_value", "count"))
    .reset_index()
    )
# Get word count
before_word_count = pd_rise[pd_rise["pos_value"] != "PUNCT"]["rise_count"].sum()
# Get relative word type counts
pd_rise["rise_relative_count"] = pd_rise["rise_count"]/n_rows

# For fall article
# Initiate pandas dataframe
pd_fall = pd.DataFrame({"word":[], "pos_value":[]})
for token in token_after:
    # Make row of data
    sub_pd = pd.DataFrame({"word":str(token), "pos_value":token.pos_}, index = [0])
    # Append to pd_rise
    pd_fall = pd_fall.append(sub_pd, ignore_index = True)
# Group by pos_value and count
n_rows = len(pd_fall)
pd_fall = (
    pd_fall
    .groupby("pos_value")
    .agg(fall_count = ("pos_value", "count"))
    .reset_index()
    )
# Get word count
after_word_count = pd_fall[pd_fall["pos_value"] != "PUNCT"]["fall_count"].sum()
# Get relative word type counts
pd_fall["fall_relative_count"] = pd_fall["fall_count"]/n_rows

# Make into one general dataframe
pd_both = (
        pd_rise
        .merge(pd_fall)
        # Drop columns
        .drop(["rise_count", "fall_count"], axis = 1)
        # Make decimals easier to read
        .round(2)
        )
# Print
print("The overall share of word types in both articles:")
print(pd_both.to_string(index = False))