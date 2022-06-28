from gtts import gTTS
language = 'ru'

import telebot
from telebot import types

TOKEN = '5571481281:AAEgvaIHPy0oOS4ICldlx7ULvxVyTHLEU5s'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Start TTS':
        msg = bot.send_message(message.chat.id, 'Enter your text:')
        bot.register_next_step_handler(msg, process_text)
    else:
        bot.send_message(message.chat.id,'Введите "Start TTS"')
def process_text(message):
    
    bot.send_message(message.chat.id,'Обрабатываем ваш текст...')
    text_val = message.text
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save(f'{message.chat.id}.mp3')
    audio = open(f'{message.chat.id}.mp3', 'rb')
    bot.send_voice(message.chat.id, audio, caption = "Ваше аудио")
bot.polling()