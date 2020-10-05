# Welcome to rise-and-fall!
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

You can run the entire NLP analysis on the command line. Go to the main directory of this
repository and run the command `python python_scripts/main.py "leader"`. For the `leader`
argument, fill in the last name, in small letters, of the political leader you would 
like to run the analysis for. For instance, for Sarkozy, you can run `python python_scripts/main.py "sarkozy"`.