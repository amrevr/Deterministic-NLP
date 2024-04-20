from nltk.corpus import wordnet

def are_synonyms(word1, word2):
    synonyms = []
    for syn in wordnet.synsets(word1):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    
    if word2 in set(synonyms):
        return True
    else:
        return False

