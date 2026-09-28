import os
import telebot
from flask import Flask, request

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_USERNAME"]

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "👋 Welcome!\n\n"
        "Get our latest updates and free signals.\n\n"
        "👇 Join our channel:"
    )

    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(
        "📲 JOIN CHANNEL",
        url=f"https://t.me/{CHANNEL.lstrip('@')}"
    )
    markup.add(button)

    bot.send_message(message.chat.id, text, reply_markup=markup)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.data.decode("utf-8"))
    bot.process_new_updates([update])
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
