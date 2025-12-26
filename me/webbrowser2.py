import requests
from bs4 import BeautifulSoup
import re

# Step 1: Define the URL
url = "https://roozaneh.net/fun/sms/%D8%A8%D9%87%D8%AA%D8%B1%DB%8C%D9%86-%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C/"

# Step 2: Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract and clean the text
raw_text = soup.get_text()
clean_text = raw_text.replace('\n', ' ').replace('\r', ' ').strip()
clean_text = ' '.join(clean_text.split())  # Collapse multiple spaces

# Step 4: Split poems using Persian keywords "اشعار" or "شعر"
poems = re.split(r'\b(?:اشعار|شعر)\b', clean_text)
poems = [poem.strip() for poem in poems if poem.strip()]  # Remove empty entries

# Step 5: Save each poem with an English label
with open("poems.txt", "w", encoding="utf-8") as file:
    for i, poem in enumerate(poems, start=1):
        file.write(f"Poem {i}:\n{poem}\n\n")

print(f"{len(poems)} poems extracted and saved to poems.txt")
