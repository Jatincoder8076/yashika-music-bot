from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from tictac import tictac, move
from oneword import oneword, check_word
from music import music
from yashika_love import love_yashika
from about import about_callback, about_description, gban, gunban, gbroadcast

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton("• OWNER •", url="https://t.me/myself_jatin")],
        [InlineKeyboardButton("• ABOUT •", callback_data="about"),
         InlineKeyboardButton("• MODE •", callback_data="mode")],
        [InlineKeyboardButton("• TAP TO SEE MAGIC •", callback_data="magic")]
    ]
    caption = f"""
╭───────────────────▣
│❍ ʜᴇʏ {user} •
│❍ ɪ ᴀᴍ ˹𝙔ᴀsʜɪᴋᴀ ✘ 𝙈ᴜꜱɪᴄ˼ ♪ •
├───────────────────▣
│❍ ʙᴇsᴛ ǫᴜᴀʟɪᴛʏ ғᴇᴀᴛᴜʀᴇs •
│   sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ ʙᴏᴛ 
╰───────────────────▣
    """
    await update.message.reply_photo(photo=open("start.jpg", "rb"), caption=caption, reply_markup=InlineKeyboardMarkup(keyboard))

app = ApplicationBuilder().token("7965234747:AAGTvkPKEp1InJLYBBMX4UxpbBCzfGwjkM8").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tictac", tictac))
app.add_handler(CommandHandler("oneword", oneword))
app.add_handler(CommandHandler("music", music))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, move))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_word))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, love_yashika))

app.add_handler(CallbackQueryHandler(about_callback, pattern="about"))
app.add_handler(CallbackQueryHandler(about_description, pattern="desc"))
app.add_handler(CommandHandler("gban", gban))
app.add_handler(CommandHandler("gunban", gunban))
app.add_handler(CommandHandler("gbroadcast", gbroadcast))

print("🤖 Bot running...")
app.run_polling()
