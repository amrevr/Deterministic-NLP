from syllables import *

# Input garnered
input = input("Enter a paragraph => ").strip()

# Open a file in read mode
with open(input, 'r') as file:
    # Read the entire contents of the file
    content = file.read()

# Stores all sentences from paragraph in seperate list
container_sentence = file.split(".")

# Popped to remove the blank sentence created
container_sentence.pop()

# ASL 
'''
The original sentence is split using the .split() function into sentences by 
inputting "." as a parameter into .split().

This set of code determines the average sentence length (ASL) by looping through
the container for 
'''
sentence = 0
word_count = 0

while sentence < len(container_sentence):
    word_count += len(container_sentence[sentence].split())
    sentence += 1

asl = word_count/sentence

# PHW
'''
The original paragraph is broken down into a new container that stores words.

This word container is then looped to detect any words with a syllable count greater than OR equal to 3.
    IF the syllable count is greater than 3
        The word is checked to ensure it is not ending with hypens
    IF the syllable count is equal to 3
        The word is checked to ensure it does not end with the prior condition 
        and is checked to ensure it does not end with "es" and "ed"

The words are then appened to a new list, which is then used to find phw
'''
i = 0
hard_words = []
container_words = file.split()

# Used in calculating ASYL
count_syllables = 0
while i < len(container_words):
    syllable_count = find_num_syllables(container_words[i])
    count_syllables += syllable_count

    if syllable_count > 3 and (container_words[i].find("-") == -1):
            hard_words.append(container_words[i])

    if syllable_count == 3 and not(container_words[i].endswith("es"))\
        and not(container_words[i].endswith("ed")) \
        and (container_words[i].find("-") == -1):
            hard_words.append(container_words[i])

    i+=1

phw = len(hard_words)/word_count * 100

# ASYL
asyl = count_syllables/word_count

# Readability Index
gfri = 0.4*(asl + phw)
fkri = 206.835-1.015*asl-86.4*asyl



# Final Output
print("Here are the hard words in this paragraph: \n{}".format(hard_words))
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(asl, phw, asyl))
print("Readability index (GFRI): {:.2f}".format(gfri))
print("Readability index (FKRI): {:.2f}".format(fkri))
