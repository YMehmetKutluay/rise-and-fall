# Dependencies
import os
import spacy
# Read file

# Load English NLP decoder
nlp = spacy.load("en_core_web_sm")

# Load after text
file_path = os.path.join(os.getcwd(), "data", "qaddafi", "after.txt")
with open(file_path, 'r') as file:
    text_full = file.read()
# TODO: Count occurrences of \n in text_full to find number of paragraphs
# Get rid of \n
with open(file_path, 'r') as file:
    text_after = file.read().replace("\n", "")
# Tokenize
token_after = nlp(text_after)

# Load before text
file_path = os.path.join(os.getcwd(), "data", "qaddafi", "before.txt")
with open(file_path, 'r') as file:
    text_full = file.read()
# TODO: Count occurrences of \n in text_full to find number of paragraphs
# Get rid of \n
with open(file_path, 'r') as file:
    text_before = file.read().replace("\n", "")
# Tokenize
token_before = nlp(text_before)
