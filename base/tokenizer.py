from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def tokenize_file(file_path):
    # Get the set of English stopwords from NLTK
    stop_words = set(stopwords.words('english'))
    
    # Additional words to exclude (time-related and number-related)
    stop_words.update(
        {
        'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
        'october', 'november', 'december', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'sunday', 'today', 'yesterday', 'tomorrow', 'year', 'years', 'month', 'week', 'day',
        'hour', 'minute', 'second', 'am', 'pm', 'th', 'st', 'nd', 'rd', '1st', '2nd', '3rd', '4th',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'twenty',
        'thirty', 'forty', 'fifty', 'hundred', 'thousand', 'million', 'billion', 'trillion',
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth',
        'tenth', 'twentieth', 'thirtieth', 'hundredth', 'thousandth', 'millionth', 'billionth',
        'trillionth'
        }
    )

    file_tokens = []

    with open(file_path, 'r') as file:
        for line in file:
            # Tokenize each line using NLTK's word_tokenize
            line_tokens = word_tokenize(line.lower())
            # Filter out stopwords and non-alphanumeric tokens
            filtered_tokens = [token for token in line_tokens if token.isalnum() and 3 < len(token) and token not in stop_words]
            file_tokens.extend(filtered_tokens)
    return file_tokens

def main():
    """
    1. Hover over intended file for analysis in VS-Code
    2. Right Click it
        2a. In the pop-up menu, select "Copy Relative Path"
        2b. The default shortcut for this is "Ctrl+K Ctrl+Shift+C" (not recommended!)
    3. Paste this path into your terminal
        3a. If your unable to copy and paste into your VS-Code terminal, manually type it or
            refer to this guide: https://stackoverflow.com/questions/51521004/in-visual-studio-code-ctrlv-is-not-working
        3b. STRONGLY recommend you just type it in... saves time from reading!
    """
    file_path = input("Enter relative-file path: ").strip()
    print(tokenize_file(file_path))


# Guard to prevent program from executing if its not being ran
if __name__ == "__main__":
    main()