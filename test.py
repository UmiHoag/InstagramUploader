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
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("imgs\{}".format(i))
        os.rename(remove_me, src)

def upload_post(i):
    bot = Bot()

    bot.login(username = "username", password = "password")
    bot.upload_photo("imgs/{}".format(i), caption="First picture")
# bot.follow('person's username')
# Gives the path and name if it is in another directory than the concurrent one
#   bot.upload_photo(" ")

if __name__ == '__main__':
    image_name = ""
    clean_up(image_name)
    upload_post(image_name)