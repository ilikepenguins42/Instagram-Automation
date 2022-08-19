from instabot import Bot
import pandas 
import csv
import time
import os 
import base64

#use the below code if a cookie error comes otherwise leave it hashed
#if os.path.isfile("path/to/config/file.json"):
#   os.remove("path/to/config/file.json")

bot = Bot()
bot.login(username="", password="")


#upload pictures??
with open(r"insertfilepath",'rb') as file:
    image = int(float(file.read()))
    
#here "rb" means reading it in bytes    
    
while image < 10000: photo = str(image) 
bot.upload_photo(f"{photo}.png") 
time.sleep(3600) 
image += 1    

#follow?
bot.follow("jetairways")

#message someone?
bot.send_message("", ['',''])

#follower info??
my_followers = bot.get_user_followers("")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()
