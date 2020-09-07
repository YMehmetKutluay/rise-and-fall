# Welcome to before-and-after!
This is the repository that contains the Python and markdown scripts that are used in 
making the [Rise and Fall](https://anchor.fm/rise-and-fall) podcast - created by 
Mehmet Kutluay and Guilherme Oliveira. The podcast is about analyzing news articles 
from the first and last day of selected political leaders.

Here you can find the code and data used to make the quantitative analyses discussed 
in the podcast episodes. The NLP packages that are utilized are [SpaCy](https://spacy.io/) and 
[NLTK](https://www.nltk.org/). 

Feel free to fork/clone and comment on possible improvements, by opening up issues. 
All feedback is welcome!

# Getting Started

## Where is What

The directory holds the following folders:

1. `data` - Holds the text files of the news articles that are analyzed
2. `local_files` - Notes regarding the qualitative analyses between the articles
3. `other_analysis` - Miscallenous analyses
4. `python_scripts` - Python scripts to run the quantitative analyses
5. `reading_scripts` - Reading scripts for the podcast, compiled via [R Markdown](https://rmarkdown.rstudio.com/)

## Run the NLP Analysis

Simply write in the political leader you are interested in (and that is available) into 
the `leader` variable in the `python_scripts/main.py` script. After that, run said script.
