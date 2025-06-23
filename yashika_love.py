from telegram import Update
from telegram.ext import CallbackContext

def love_yashika(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "yashika" in text:
        update.message.reply_text("🥺 Awww... Yashika is love 💖")
