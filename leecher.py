# Code By mrsploit
# t.me/mrsploit
# t.me/zoneh
from instabot import Bot
import os, getpass

logo = '''
\033[0;35m
            ──▄█████████████████████████▄──
            ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░█░█░█░░░░░░░░░░░░░░█████░░█
            █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
            ███████████▀▀░░░░░▀▀███████████
            █░░░░░░░██░░▄█████▄░░██░░░░░░░█
            █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
            █░░░░░░░██░██░░░░░██░██░░░░░░░█
            █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
            █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
            █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
            █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
            ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
            ──▀█████████████████████████▀──
\033[0;34m
           +---  Instagram User Leecher ---+ \033[0;32m
           https://jilrot.com
           t.me/jailbreakandroot


  ### Login ###

'''

print(chr(27)+'[2j')
print('\033c')
print('\x1bc'
print (logo)

user = input("Username: ")
passwd = getpass.getpass("Password: ")
print
account = input("Account to extract user: ")

bot = Bot()
bot.login(username=user, password=passwd, ask_for_code=True)
user_id = bot.get_user_id_from_username(account)
followers = bot.get_user_followers(user_id)

f = open("usernames.lst", "w")

for user_id in followers:
    username = bot.get_username_from_user_id(user_id)
    print (username)
    f.write(username+'\n')

f.close()

os.system("rm -rf *log *txt config *json *.checkpoint")
