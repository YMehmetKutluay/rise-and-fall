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
    text_combined = file.read().replace("\n", "")
# Tokenize
doc = nlp(text_combined)
for token in doc:
    print(token.text, token.pos_, token.dep_)
