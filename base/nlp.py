import webscrapper as wb
import tokenizer as tk
import readability as rd
import os

def nlp(emotion_words, tokens):
    emotion_scores = {emotion: 0 for emotion in emotion_words}  # Initialize emotion scores

    for token in tokens:
        for emotion, related_words in emotion_words.items():
            if token in related_words:
                emotion_scores[emotion] += 1  # Increment score for positive emotion word match
            else:
                emotion_scores[emotion] -= 1

     # Determine the most expressed emotion(s)
    if emotion_scores:
        max_score = max(emotion_scores.values())
        most_expressed_emotions = [emotion for emotion, score in emotion_scores.items() if score == max_score]

        # Returns multitude of emotions if a tie occurs
        return ", ".join(most_expressed_emotions) if len(most_expressed_emotions) > 1 else most_expressed_emotions[0]
    else:
        return None  # No emotions detected, theoritically should never happen

def main():
    print("Hello! Please be patient while the emotions are being processed...")
    # Find synonyms for our "emotions"
    emotion_dict = {}
    emotions = ["happy", "sad", "fear", "surprise", "disgust", "anger"]
    for emotion in emotions: 
        emotion_dict[emotion] = wb.get_synonyms(emotion)
    print("Finished processing emotion synonyms...")

    # Process and tokenize file
    file_path = input("Enter relative-file path: ").strip()
    file_tokens = tk.tokenize_file(file_path)
    print("Finished tokenizing file...")
    # "NLP"
    most_expressed_emotion = nlp(emotion_dict, file_tokens)
    os.system("cls") # Will only work with powershell

    if most_expressed_emotion.find(",") == True:
        print(f"The most expressed emotions are: {most_expressed_emotion}")
    else:
        print(f"The most expressed emotion is: {most_expressed_emotion}")

    # Confidence in results based on readability of text
    print(f"\nReadability Metrics:")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Calculate confidence based on readability metrics
    confidence = rd.calculate_confidence(text)
    print(f"\nConfidence in Text: {confidence:.2f}%")

# Guard to prevent program from executing if its not being ran
if __name__ == "__main__":
    main()

