import telebot
from telebot import types
import json

TOKEN = "8438543254:AAEys8nz326llYGy46n-ztKqoQ5UVMRwUI0"
bot = telebot.TeleBot(TOKEN)


with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)


def load_users():
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_users(data):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def send_question(chat_id):
    users = load_users()

    if str(chat_id) not in users:
        return

    index = users[str(chat_id)]["index"]

    if index >= len(questions):
        score = users[str(chat_id)]["score"]
        bot.send_message(
            chat_id,
            f"🎉 Викторина закончена!\n"
            f"Ваш результат: {score} из {len(questions)}"
        )
        return

    q = questions[index]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for answer in q["answers"]:
        keyboard.add(types.KeyboardButton(answer))

    bot.send_message(chat_id, f"❓ {q['question']}", reply_markup=keyboard)



@bot.message_handler(commands=["start"])
def start(message):
    chat_id = str(message.chat.id)

    users = load_users()

    users[chat_id] = {
        "index": 0,
        "score": 0
    }

    save_users(users)

    bot.send_message(chat_id, "🚀 Викторина началась!")
    send_question(chat_id)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    chat_id = str(message.chat.id)
    users = load_users()

    if chat_id not in users:
        return

    index = users[chat_id]["index"]

    if index >= len(questions):
        return

    correct_answer = questions[index]["correct"]

    if message.text == correct_answer:
        users[chat_id]["score"] += 1
        bot.send_message(chat_id, "✅ Верно!")
    else:
        bot.send_message(
            chat_id,
            f"❌ Неверно! Правильный ответ: {correct_answer}"
        )

    users[chat_id]["index"] += 1
    save_users(users)

    send_question(chat_id)


bot.polling(none_stop=True)