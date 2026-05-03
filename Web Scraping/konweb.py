import requests
from bs4 import BeautifulSoup

#main code that featches Data
import requests

url = "https://www.savemylanguage.org/sml_v2/pages/dictionary.php?script=devanagari&letter=Z"

#That headers dictionary is basically your way of telling the website who you are and what you want when you send a request.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", #“I am a browser (like Chrome on Windows)” not a robot
    "Accept-Language": "en-US,en;q=0.9", # i Prefer content that are in Enlish
    "Accept": "text/html" #“I want HTML content”
}

response = requests.get(url, headers=headers, timeout=10) #url, your intro + Waits up to 10 seconds for response

soup = BeautifulSoup(response.text, "html.parser") #parser convers code into tree structure
words = soup.find_all("span", class_="word-devanagari")
meanings = soup.find_all("span", class_="word-meaning")

print(f"{'Word Devanagari':<35} | Meaning")
print("-" * 60)

for w, m in zip(words, meanings):
    word = w.text.strip() or w.get("data-itrans")
    meaning = m.text.strip()
    print(f"{word:35} | {meaning}")

#To Convert it to CSV file
import csv

with open("dictionary25.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Word Devanagari", "Meaning"])
    
    # Data
    for w, m in zip(words, meanings):
        word = w.text.strip() or w.get("data-itrans")
        meaning = m.text.strip()
        writer.writerow([word, meaning])

print("CSV file created successfully!")
