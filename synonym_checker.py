import nltk
from nltk.corpus import wordnet

def are_synonyms(word1, word2):
    # Get synsets for each word
    synsets1 = wordnet.synsets(word1)
    synsets2 = wordnet.synsets(word2)

    # Check for common synonyms
    for synset1 in synsets1:
        for synset2 in synsets2:
            if synset1 == synset2:  # Check if the synsets are the same
                return True
            # Check if there's any lemma in common between the synsets
            for lemma1 in synset1.lemmas():
                for lemma2 in synset2.lemmas():
                    if lemma1.name() == lemma2.name():
                        return True

    return False

# Example usage
word1 = "happy"
word2 = "glad"

if are_synonyms(word1, word2):
    print(f"{word1} and {word2} are synonyms.")
else:
    print(f"{word1} and {word2} are not synonyms.")