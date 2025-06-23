from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

OWNER_ID = 7676386584  # Replace with your actual Telegram numeric user ID (for Jatin)

async def about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("• DESCRIPTION •", callback_data="desc"),
         InlineKeyboardButton("• ALL BOTS •", url="https://t.me/myself_jatin")],
        [InlineKeyboardButton("• SUPPORT •", url="https://t.me/+STjhSo9Tl1Q1M2Jl")]
    ]
    await query.edit_message_text(
        text="👋 Welcome to Yashika Music Bot Info Panel!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def about_description(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    desc = "🎶 *Bot Features:*\n\n" \
       "• Music Search (YouTube)\n" \
       "• Fun Games (Tic Tac Toe, One Word)\n" \
       "• 24/7 Hosting, Lag Free\n" \
       "• Group Commands: /gban /gbroadcast\n" \
       "• Built with 💖 by @myself_jatin""
    await query.edit_message_text(desc, parse_mode="Markdown")

# Admin Commands
async def gban(update: Update, context: CallbackContext):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ You are not authorized to use this.")
        return
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /gban user_id reason")
        return
    user_id = int(context.args[0])
    reason = ' '.join(context.args[1:])
    # Placeholder DB action
    await update.message.reply_text(f"✅ User {user_id} has been globally banned.
Reason: {reason}")

async def gunban(update: Update, context: CallbackContext):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ You are not authorized to use this.")
        return
    if len(context.args) < 1:
        await update.message.reply_text("Usage: /gunban user_id")
        return
    user_id = int(context.args[0])
    await update.message.reply_text(f"✅ User {user_id} has been globally unbanned.")

async def gbroadcast(update: Update, context: CallbackContext):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ You are not authorized to use this.")
        return
    msg = ' '.join(context.args)
    # Placeholder broadcast simulation
    await update.message.reply_text(f"📣 Broadcasting to all groups:

{msg}")
