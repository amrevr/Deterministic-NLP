import re

def tokenize(text):
    # Custom tokenizer to split text into words based on whitespace and punctuation
    tokens = re.findall(r'\w+', text.lower())  # Extract alphanumeric sequences
    return tokens

def calculate_asl(sentences):
    total_words = sum(len(sentence) for sentence in sentences)
    return total_words / len(sentences) if len(sentences) > 0 else 0

def calculate_phw(words):
    hard_words = [word for word in words if syllable_count(word) >= 3]
    return (len(hard_words) / len(words)) * 100 if len(words) > 0 else 0

def syllable_count(word):
    # Simple syllable counting function (example implementation)
    return max(1, sum(1 for char in word if char in 'aeiou'))

def calculate_asyl(words):
    total_syllables = sum(syllable_count(word) for word in words)
    return total_syllables / len(words) if len(words) > 0 else 0

def calculate_gfri(asl, phw):
    return 0.4 * (asl + phw)

def calculate_fkri(asl, asyl):
    return 0.39 * asl + 11.8 * asyl - 15.59

def calculate_confidence(text):
    words = tokenize(text)

    asl = calculate_asl(words)
    phw = calculate_phw(words)
    asyl = calculate_asyl(words)
    gfri = calculate_gfri(asl, phw)
    fkri = calculate_fkri(asl, asyl)

    # Print readability metrics
    print(f"Average Sentence Length (ASL): {asl:.2f} words per sentence")
    print(f"Percentage of Hard Words (PHW): {phw:.2f}%")
    print(f"Average Syllables per Word (ASYL): {asyl:.2f} syllables per word")
    print(f"Gunning Fog Index (GFRI): {gfri:.2f}")
    print(f"Flesch-Kincaid Readability Index (FKRI): {fkri:.2f}")

    # Calculate confidence based on readability metrics
    confidence_score = (100 - phw) * (1 - abs(8 - gfri) / 8) * (1 - abs(6 - fkri) / 6)
    return confidence_score

def main():
    # Read text from a file
    file_path = input("Enter relative file path: ").strip()
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Calculate confidence based on readability metrics
    confidence = calculate_confidence(text)
    print(f"\nConfidence in Text: {confidence:.2f}%")

if __name__ == "__main__":
    main()
