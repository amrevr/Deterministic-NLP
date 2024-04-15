# Define the URL of the file
file_url = "https://ptrckprry.com/course/ssd/data/negative-words.txt"

import urllib.request

# Function to read words from file and create a dictionary
def create_word_dict_from_file(url):
    word_dict = {}
    
    try:
        # Open the file from URL
        with urllib.request.urlopen(url) as file:
            # Iterate over each line (word) in the file
            for line in file:
                # Decode the line and remove leading/trailing whitespace
                word = line.decode('utf-8').strip()
                
                # Skip empty lines and comments
                if word and not word.startswith(';'):
                    # Add word to dictionary with a value (e.g., True)
                    word_dict[word] = True
    
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return word_dict

# Call the function to create the dictionary
negative_words_dict = create_word_dict_from_file(file_url)