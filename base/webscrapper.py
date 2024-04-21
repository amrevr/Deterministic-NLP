import requests
from bs4 import BeautifulSoup

def get_synonyms(word):
    url = f"https://www.merriam-webster.com/thesaurus/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        synonym_lists = soup.find_all(class_="thes-list-content")
        
        if synonym_lists:
            synonyms = set()
            for synonym_list in synonym_lists:
                synonyms.update(syn.text.strip() for syn in synonym_list.find_all("a") if (len(syn.text.strip()) <= 5) and syn.text.strip())
            return synonyms
        else:
            return set()
    else:
        print(f"Failed to fetch synonyms for {word}.")
        return set()

def main():
    emotion_dict = {}
    emotions = ["happy", "sad", "fear", "surprise", "disgust", "anger"]
    for emotion in emotions: 
        emotion_dict[emotion] = get_synonyms(emotion)

# Guard to prevent program from executing if its not being ran
if __name__ == "__main__":
    main()
 
