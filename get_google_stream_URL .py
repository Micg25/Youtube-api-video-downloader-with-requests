import requests
from bs4 import BeautifulSoup
import json
import re

video_url="" #put the url video here 

resp = requests.get(video_url)
html_content = resp.text

# Writing the html response in a TXT file
with open("html.txt", "w", encoding="utf8") as file:
    file.write(html_content)

# Creating the BeautifulSoup object with "html parser"
soup = BeautifulSoup(html_content, 'html.parser')

# finding stream data
scripts = soup.find_all("script")
target_script = None
for script in scripts:
    if "ytInitialPlayerResponse" in str(script):
        target_script = str(script)
        break


# Verifica che abbiamo trovato il blocco di script corretto
if not target_script:
    raise Exception("Impossibile to find stream data")

# finding the part of the script that includes:  "ytInitialPlayerResponse"
yt_initial_data = re.search(r'ytInitialPlayerResponse\s*=\s*({.*?});', target_script).group(1)

# Converting yt_initial_data in a python dictionary
player_response = json.loads(yt_initial_data)

# Extracting video and audio stream url
streaming_data = player_response['streamingData']
formats = streaming_data['formats'] + streaming_data['adaptiveFormats']


# Writing each url stream in a txt file
with open("stream.txt", "w", encoding="utf8") as file:
    for format in formats:
        file.write(f"{format['url']}"+str("\n"))

with open("streamingadata.txt", "w", encoding="utf8") as file:
        file.write(str(streaming_data))

    
