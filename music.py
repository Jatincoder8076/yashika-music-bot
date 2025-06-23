from telegram import Update
from telegram.ext import CallbackContext
from youtubesearchpython import VideosSearch

def music(update: Update, context: CallbackContext):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text("❗Use like: /music love song")
        return

    search = VideosSearch(query, limit=1)
    result = search.result()['result'][0]
    title = result['title']
    link = result['link']

    update.message.reply_text(f"🎶 *{title}*\n🔗 {link}", parse_mode='Markdown')
