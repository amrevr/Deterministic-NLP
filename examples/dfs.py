import nltk
from nltk.corpus import wordnet as wn

def are_synonyms(word1, word2, depth_limit=2):
    # Initialize a stack for DFS
    stack = [(word1, 0)]
    visited = set()
    
    while stack:
        current_word, depth = stack.pop()
        
        # Check if we have reached the depth limit
        if depth > depth_limit:
            continue
        
        # Mark the current word as visited
        visited.add(current_word)
        
        # Check if the current word is a synonym of the target word
        if word2 in [syn.name() for syn in wn.synsets(current_word)]:
            return True
        
        # Explore synonyms of the current word
        for synset in wn.synsets(current_word):
            for synonym in synset.lemma_names():
                if synonym not in visited:
                    stack.append((synonym, depth + 1))
    
    # If we exhaust the search without finding the synonym
    return False

# Example usage
word1 = "happy"
word2 = "joyful"
result = are_synonyms(word1, word2, depth_limit=2)

if result:
    print(f"{word1} and {word2} are synonyms!")
else:
    print(f"{word1} and {word2} are not synonyms.")
