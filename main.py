import telebot
import saver
import db
import os
from signal import signal, SIGINT, SIGTERM
bot = telebot.TeleBot("964675929:AAEQKdFRPlEHEfWiWsdxqRwp3u1dQpL9eUI")
print("--------------------")
print("       START")
print("--------------------")


class info:
    folder = None
    downloaded_file = None

inf = info()




@bot.message_handler(commands=["start"])
def hello(message):
    #TODO FINSIH HELLO TEXT
    bot.send_message(message.chat.id, "Hello! I am MEME SAVER BOT.\nMy aim to receive and store your memes.\nSend a picture and its name. Later you will use the name to get your meme.")


@bot.message_handler(content_types=['photo'])
def photo(message):
    print("photo received")
    inf.downloaded_file = bot.download_file(bot.get_file(message.photo[-1].file_id).file_path)
    inf.folder = message.from_user.id

    if message.caption == None:
        bot.send_message(message.chat.id, "Enter tag")
        bot.register_next_step_handler(message, ask_tag)
    else:

        words = [message.caption]
        if "%" in message.caption:
            words = message.caption.split()
            db.add(message.from_user.id, words[1], words[0] + ".jpg")

        with open(f"{words[0]}.jpg", 'wb') as new_file:
            new_file.write(inf.downloaded_file)

        saver.upload({f"{words[0]}.jpg"}, inf.folder)
        bot.send_message(message.chat.id, "Your meme is saved")
        os.remove(f"{words[0]}.jpg")



def ask_tag(message):
    print("asking tag")
    words = [message.text]
    if "%" in message.text:
        words = message.text.split()
        db.add(message.from_user.id, words[1], words[0] + ".jpg")

    with open(f"{words[0]}.jpg", 'wb') as new_file:
        new_file.write(inf.downloaded_file)

    saver.upload({f"{words[0]}.jpg"}, inf.folder)
    bot.send_message(message.chat.id, "Your meme is saved")
    os.remove(f"{words[0]}.jpg")




@bot.message_handler(content_types=["text"])
def handle_text(message):
    print("text received")
    try:
        if "%" in message.text:
            names = [str(message.from_user.id) + "/" + el[2] for el in db.find(430437500, message.text.strip())]
            urls = saver.download(names)
        else:
            urls = saver.download({f"{message.from_user.id}/{message.text}.jpg"})

        for url in urls:
            bot.send_photo(message.chat.id, url)
    except:
        bot.send_message(message.chat.id, "Sorry. No such a meme...")


bot.polling(none_stop=True, interval=0)

