import synonym_checker
from string import punctuation
from nltk import word_tokenize

# Emotion words to check against
emotion_words = ["happy", "sad", "anger", "disgust", "surprise", "fear"]
emotion_dict = {emotion: 0 for emotion in emotion_words}

def main(input_file_path):
    try:
        # Open and read the input file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            # Read the entire file contents
            file_contents = file.read()

            # Tokenize the file contents into words
            words = word_tokenize(file_contents)

            # Normalize words to lowercase and remove punctuation
            words = [word.lower() for word in words if word not in punctuation]

            # Iterate through each word and check against emotion words
            for word in words:
                # Check if the word is a synonym of any emotion word
                for emotion in emotion_words:
                    if synonym_checker.are_synonyms(word, emotion):
                        print(f"Word '{word}' is a synonym of '{emotion}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")

if __name__ == "__main__":
    file = input("Enter input file relative path: ")
    main(file)