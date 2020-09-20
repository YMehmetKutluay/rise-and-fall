# Dependencies
import os
import spacy
import pandas as pd
from sentiment_analysis_spanish import sentiment_analysis

# Select political leader
leader = "lula"

# Get before and after text files as single strings
file_path = os.path.join(os.getcwd(), "data", leader, "before.txt")
with open(file_path, 'r', encoding = "utf-8") as file:
    str_before = file.read()

file_path = os.path.join(os.getcwd(), "data", leader, "after.txt")
with open(file_path, 'r', encoding = "utf-8") as file:
    str_after = file.read()

# Sentiment analysis, see https://pypi.org/project/sentiment-analysis-spanish/
# Initialize sentiment analysis class
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
# Make before article into paragraph-based list and do sentiment analysis
para_before = str_before.split("\n")
before_sentiment = list()
for i in range(len(para_before)):
    before_sentiment.append(sentiment.sentiment(para_before[i]))
print("Average sentiment for before article is {:.4f}".format(
    sum(before_sentiment)/len(before_sentiment), 2))
# Make after article into paragraph-based list and do sentiment analysis
para_after = str_after.split("\n")
after_sentiment = list()
for i in range(len(para_after)):
    after_sentiment.append(sentiment.sentiment(para_after[i]))
print("Average sentiment for after article is {:.4f}".format(
    sum(after_sentiment)/len(after_sentiment), 2))

# Get ratio based result to see after/before sentiment
print("Ratio of after/before sentiment is thus {:.4f}".format(
    (sum(after_sentiment)/len(after_sentiment))/(sum(before_sentiment)/len(before_sentiment))))

# Now do this per sentence
sen_before = str_before.replace("\n", "").split(".")
before_sentiment = list()
for i in range(len(sen_before)):
    before_sentiment.append(sentiment.sentiment(sen_before[i]))
print("Average sentiment for before article is {:.4f}".format(
    sum(before_sentiment)/len(before_sentiment), 2))

sen_after = str_after.replace("\n", "").split(".")
after_sentiment = list()
for i in range(len(sen_after)):
    after_sentiment.append(sentiment.sentiment(sen_after[i]))
print("Average sentiment for after article is {:.4f}".format(
    sum(after_sentiment)/len(after_sentiment), 2))
# Get ratio based result to see after/before sentiment
print("Ratio of after/before sentiment is thus {:.4f}".format(
    (sum(after_sentiment)/len(after_sentiment))/(sum(before_sentiment)/len(before_sentiment))))


