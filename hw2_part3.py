"""
The objective of this code is to make a rudimentary "sentimence analysis tool "
that is capable of determing the "happiness" of a statement. 

This is accomplished by garnering an input sentence by the user,
which is then ran through two functions titled...
    number_happy(sentence)
    number_sad(sentence)
These statements use the ".count()" function to check how many "happy" or "sad" words
are present in the inputted statement.

The amount of happy and sad words are tracked by using place holder count variables.

The requested outputs from the prompt...
    Sentiment of the sentence
    Quality of statment
...are then outputted neatly into a print statement using .format()
"""
# Input sentence is taken from user
sentence = input("Enter a sentence => ").strip()
print(sentence)
sentence = sentence.lower()

# Function to count number of happy words
def  number_happy(sentence):    
    happy_count = sentence.count("laugh")
    happy_count += sentence.count("happiness")
    happy_count += sentence.count("love")
    happy_count += sentence.count("excellent")
    happy_count += sentence.count("good")
    happy_count += sentence.count("smile")

    return happy_count

# Function to count number of sad words
def number_sad(sentence):
    sad_count = sentence.count("bad")
    sad_count += sentence.count("sad")
    sad_count += sentence.count("terrible")
    sad_count += sentence.count("horrible")
    sad_count += sentence.count("problem")
    sad_count += sentence.count("hate")
    
    return sad_count 

# Assignment variables for checking count of positivity/sadness in sentence
positivity = "+"*number_happy(sentence)
sadness = "-"*number_sad(sentence)

# Combines "+" and "-" in the order requested
sentiment = positivity + sadness

# Checks to see if sentence is more positve than negative {Sentiment}
determinence = "neutral"
if number_sad(sentence) >  number_happy(sentence):
    determinence = "sad"
if number_sad(sentence) < number_happy(sentence):
    determinence = "happy"

# Final Output
print("""Sentiment: {}
This is a {} sentence.""".format(sentiment, determinence))
