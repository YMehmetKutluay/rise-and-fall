# Welcome to before-and-after!
This is a repository for making simple text analyses of news articles and storing the PDF documents that store the notes. The text analyses are done using [SpaCy](https://spacy.io/), a Python package, and the PDF documents are compiled using [R Markdown](https://rmarkdown.rstudio.com/).

# Getting Started: Text Analysis

## Dependencies

Simply run the `pip install spacy` command via Anaconda prompt. Since the articles are all in English, be sure to also install the English submodule. This is done by running the `python -m spacy download en_core_web_sm` command, again via Anaconda prompt.

All the Python code is written on plain .py scripts, thus they are accessible by any Python IDE ([Spyder](https://www.spyder-ide.org/), [PyCharm](https://www.jetbrains.com/pycharm/), [VS](https://code.visualstudio.com/) etc.). Notebooks are *not* used. Eventually the code in the main.py script will be re-factored into functions with unit tests.

## Pipeline

To be filled in, once the above-mentioned re-factoring is done.

# Getting Started: R Markdown

[R Markdown](https://rmarkdown.rstudio.com/) is RStudio's interface into writing Markdown documents. It is very user friendly and can be used to run code snippets from multiple languages - R, Python and bash included. Be sure that you have [R](https://cran.r-project.org/bin/windows/base/) and [RStudio](https://rstudio.com/) installed. After this, it is very easy to install R Markdown as can be seen in the instructions [here](https://rmarkdown.rstudio.com/authoring_quick_tour.html#Installation). 

The Markdown document is found in the markdown directory, with the .Rmd extension. Open this file within RStudio and start typing away. In order to compile the document and see the PDF output, simply click "Knit" or press Ctrl + Shift + K.