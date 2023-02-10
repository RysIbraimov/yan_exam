from celery import shared_task
import telebot

bot = telebot.TeleBot("6056156320:AAFeKgSp8PhbG7723O4kKLxeCi9lNHQ7M6o", parse_mode=None)

@shared_task
def send_message(message):
    bot.send_message(1662858165,message)



