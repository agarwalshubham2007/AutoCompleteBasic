# AutoCompleteBasic

**Python version**: 2.7.0<br>
**Python IDE**: PyCharm Professional 2016<br>
**Server**: Flask 0.10.1

# Project files and description
**Data/data.csv**: Contains words and scores in separate lines separated by ‘,’. Please feel free to put your own data in the specified format.<br>
**AutoCompleteMini.py** : This is the main file that starts the server<br>
**Model.py** : This file contains the model of search system that trains(loads and processes data file into memory)
SearchEngine.py: contains the search section code.

# INSTRUCTIONS TO RUN THE PROJECT
1. Open the project folder in PyCharm Pro
2. Run the project on server. 
3. At localhost link, the model trains itself
4. To search a term, write ‘<localhost>/<search_term>’ and press enter.

**NOTE**: You have to train the model only once at the start of the server by hitting the localhost URL

# DATA STRUCTURES DESCRIPTION
- The average length of words in a document is 5. I have taken this as the number of levels in Dictionary tree.
- First level dictionary corresponds to first character of word, second level second character and so on.
- Nodes in dictionary tree are made only when a word in data exists with corresponding prefix. 

# OUTPUT
- Top 10 results are displayed based on their scores. Only words are displayed!
- output is in HTML format with a '\<br\>' tag to display words in separate lines. It will show well on a browser
