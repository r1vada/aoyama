import telebot
import random

TOKEN = "8438543254:AAEys8nz326llYGy46n-ztKqoQ5UVMRwUI0"

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот случайных чисел.\n"
        "/random — получить случайное число\n"
        "/dice — бросить кубик"
    )

# Команда /random
@bot.message_handler(commands=['random'])
def random_number(message):
    number = random.randint(1, 100)
    bot.send_message(message.chat.id, f"Ваше число: {number}")

# Команда /dice
@bot.message_handler(commands=['dice'])
def dice(message):
    dice_roll = random.randint(1, 6)
    bot.send_message(message.chat.id, f"Выпало: {dice_roll}")

bot.polling()