from telegram import Update
from telegram.ext import CallbackContext

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = "❌"

def draw_board():
    return f"{board[0]} | {board[1]} | {board[2]}\n" \
           f"{board[3]} | {board[4]} | {board[5]}\n" \
           f"{board[6]} | {board[7]} | {board[8]}"

def tictac(update: Update, context: CallbackContext):
    global board, turn
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    turn = "❌"
    update.message.reply_text(f"🎮 *Tic Tac Toe Game!*\n\n{draw_board()}\n\nReply with number (1–9) to play.", parse_mode='Markdown')

def move(update: Update, context: CallbackContext):
    global turn
    text = update.message.text.strip()
    if text in board:
        index = board.index(text)
        board[index] = turn
        turn = "⭕" if turn == "❌" else "❌"
        update.message.reply_text(f"{draw_board()}\n\nNow it's {turn}'s turn")
