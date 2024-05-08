# Introduction
This repository houses a deterministic Natural Language Processing (NLP) project, which I developed in collaboration with a peer for my end-of-year Cognitive Science project.

The objective of this NLP is to analyze emotions, specifically focusing on the six basic emotions discussed during our lectures:

- Happiness
- Anger
- Fear
- Disgust
- Sadness
- Surprise

These emotions are considered "emotive," making them easier to discern when a person is describing them. 
Thus, it is well-suited for a tool like NLP to analyze any given text and determine the overall emotion(s) being portrayed.

We presented this data to our professors towards the end of the semester (recording is avaliable upon request).

# Libraries and Coding Methodology
This NLP was implemented using Python, due to prioritizing learning and creation
over efficiency. Some of the libraries we utilized include NLTK and Beautiful Soup.

NLTK was employed for certain aspects of the tokenization step in our program, where a given .txt file is converted from unstructured text into a format suitable for analysis. 
To ascertain if any of our tokenized characters represent a given emotion, we created a database by scraping data from merriam-webster.com. 
This database stores the most commonly used synonyms for each emotion. If a character matches a synonym in the database, a weightage is assigned to the associated emotion. 
The emotion with the highest weightage is considered the most prevalent in the text.

