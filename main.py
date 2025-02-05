# main.py
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import config as cfg
from utils import chat_request

# Initialize bot
bot = Bot(token=cfg.BOT_TOKEN)

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in cfg.ALLOWED_USERS:
        update.message.reply_text("You are not authorized to use this bot.")
        return
    update.message.reply_text("Hello, I am the DeepSeek R1 Telegram Bot. Chat with me here.")

def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in cfg.ALLOWED_USERS:
        update.message.reply_text("You are not authorized to use this bot.")
        return
    
    prompt = update.message.text
    answer = chat_request(prompt)
    
    if answer:
        update.message.reply_text(answer)
    else:
        update.message.reply_text("Error. Try again.")

def main() -> None:
    updater = Updater(cfg.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    print("Program Started")
    main()
