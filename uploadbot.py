from instabot import Bot
import os
import shutil

def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    if os.path.exists(dir):
        try:
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s " % (e.filename, e.strerror))
    if os.path.exsists(remove_me):
        src = os.path.realpath("img\{}".format(i))
        os.rename(remove_me, src)
        
        bot = Bot()
        img = "image url"
        bot.login(username="", password="")
        bot.upload_photo(img, caption = "")