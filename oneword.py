from telegram import Update
from telegram.ext import CallbackContext

last_letter = "a"

def oneword(update: Update, context: CallbackContext):
    global last_letter
    update.message.reply_text("🎮 Let's play One Word Game!\nBot: Apple")
    last_letter = "e"

def check_word(update: Update, context: CallbackContext):
    global last_letter
    word = update.message.text.lower()
    if word.startswith(last_letter):
        last_letter = word[-1]
        update.message.reply_text(f"✅ Good! Now say a word with '{last_letter.upper()}'")
    else:
        update.message.reply_text(f"❌ Word must start with '{last_letter.upper()}'!")
