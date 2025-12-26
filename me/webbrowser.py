import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL
url = "https://roozaneh.net/fun/sms/%D8%A8%D9%87%D8%AA%D8%B1%DB%8C%D9%86-%D8%A7%D8%B4%D8%B9%D8%A7%D8%B1-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C/"

# Step 2: Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all blockquote tags
blockquotes = soup.find_all('blockquote')
#print(blockquotes)
poems = []

# Step 4: Extract poem text and check for ending pattern
for block in blockquotes:
    text = block.get_text(strip=True)
    next_sibling = block.find_next_sibling()
    
    # Check if the next sibling contains '***' and is followed by a <div>
    if next_sibling and '***' in next_sibling.get_text():
        div_after = next_sibling.find_next_sibling()
        if div_after and div_after.name == 'div':
            poems.append(text)

# Step 5: Save each poem with a label
with open("poemNew.txt", "w", encoding="utf-8") as file:
    for i, poem in enumerate(poems, start=1):
        file.write(f"شعر {i}:\n{poem}\n\n")

print(f"{len(poems)} poems extracted and saved to poems.txt")
