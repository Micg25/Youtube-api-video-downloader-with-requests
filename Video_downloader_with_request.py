import requests
from urllib.parse import urlparse, parse_qs
import time
start_time = time.time()

url=""  #add the google url here


user_agent = {
 #add your user agent infos 
}
print("Start...")
session = requests.Session()
total_size = session.head(url).headers.get('content-length', 0)
print("size: ",total_size)

try:
    response = requests.get(url,headers=user_agent)
    print(response.status_code)
except:
    print(" RICHIESTA NON VA")
    pass


if response.status_code == 200:
    with open("video.mp4", "wb") as f:
        f.write(response.content)
    print("Video downloaded")
else:
    print("Can't download the video:", response.status_code)

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")

