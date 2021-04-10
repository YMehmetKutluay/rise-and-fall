# Download
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
import re

## Sentiment Analysis with NLTK
# Select political leader from command line
leader = sys.argv[1]
# Initialize sentiment intensity analyzer (see https://www.nltk.org/api/nltk.sentiment.html)
sia = SentimentIntensityAnalyzer()
# Print
print("Loading and analyzing data")
# Get list of all .txt files in relevant directory
all_files = os.listdir(os.path.join(os.getcwd(), "data", leader))
r = re.compile(".*.txt")
all_files = list(filter(r.match, all_files))
# Initialize sentiments dictonary
sentiments = dict()
# Estimate and store sentiments across all articles
for f in all_files:
    # Read file as single string
    file_path = os.path.join(os.getcwd(), "data", leader, f)
    with open(file_path, 'r', encoding = "utf-8") as file:
        file_text = file.read().replace("\n", "")
    # Estimate sentiment score and add to dictionary
    sentiments[f.replace(".txt", "")] = sia.polarity_scores(file_text) 
# Print
print("The NLTK sentiment analysis is as follows:")
for k, y in sentiments.items():
    print(k, "-->", y)

## SpaCy Tokenization
# Print
print("Initiating word type analysis")
# Load English NLP decoder
nlp = spacy.load("en_core_web_sm")
# Initialize word count dictionary and final df
word_count = dict()
final_df = pd.DataFrame()
# Get word analysis dataframe per file
for f in all_files:
    # Get article text and tokenize
    file_path = os.path.join(os.getcwd(), "data", leader, f)
    with open(file_path, 'r', encoding = "utf-8") as file:
        file_text = file.read().replace("\n", "")
    token = nlp(file_text)
    # Initiate pandas dataframe
    df = pd.DataFrame({"word":[], "pos_value":[]})
    # Count adjectives/verbs
    for t in token:
        # Make row of data
        sub_df = pd.DataFrame({"word":str(t), "pos_value":t.pos_}, index = [0])
        # Append to df
        df = df.append(sub_df, ignore_index = True)
        # Group by pos_value and count
    # Take out punctuation
    df = df.loc[df["pos_value"] != "PUNCT"]
    n_rows = len(df)
    df = (
        df
        .groupby("pos_value")
        .agg(count = ("pos_value", "count"))
        .reset_index()
        )
    # Store word count
    word_count[f.replace(".txt", "")] = df[df["pos_value"] != "PUNCT"]["count"].sum()
    # Get relative word type counts
    df[f.replace(".txt", "") + "_relative_count"] = df["count"]/n_rows
    df.drop("count", axis = 1, inplace = True)
    # Add to final df
    if len(final_df) == 0:
        final_df = df
    else:
        final_df = (
            final_df
            .merge(df)
            .round(2)
            )

# Print
print("The overall share of word types in all articles:")
print(final_df.to_string(index = False))