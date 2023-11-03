from TikTokApi import TikTokApi
import os
import requests
import random

api = TikTokApi.get_instance()
import urllib
results = 10

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.by_trending(count=results, custom_verifyFp="")

for tiktok in trending:
    # Prints the id of the tiktok
    print(tiktok['id'])

print(len(trending))

random.shuffle(trending)

i = random.randint(0,9)
print(trending[i])

# download video
try:
    b = api.get_Video_By_DownloadUrl(trending[i]['itemInfos']['video']['urls'][0])
except:
    b = api.get_video_by_tiktok(trending[i])

open('downloaded/main.mp4', "wb").write(b)

# download cover
cover = str(trending[i]['video']['cover'])

urllib.request.urlretrieve(cover, 'downloaded/cover.jpg')

# Create TXT file

username = str(trending[i]['author']['uniqueId'])
desc = str(trending[i]['desc'])

open("downloaded/desc.txt", "a").write(f"Credits: @{username} \n {desc}")