from nltk.corpus import wordnet

import nltk
nltk.download('wordnet')

def are_synonyms(word1, word2):
    synonyms = []

    # Get synsets for both words
    synsets1 = wordnet.synsets(word1)
    synsets2 = wordnet.synsets(word2)

    # Extract synonyms from each synset
    for synset in synsets1:
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())

    # Check if any synonym of word1 matches with word2
    return any(synonym in synonyms for synonym in synsets2)

# Example usage
word1 = "happy"
word2 = "glad"

if are_synonyms(word1, word2):
    print(f"{word1} and {word2} are synonyms.")
else:
    print(f"{word1} and {word2} are not synonyms.")
