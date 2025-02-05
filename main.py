# main.py
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import config as cfg
from utils import chat_request

# Initialize the bot application
app = Application.builder().token(cfg.BOT_TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in cfg.ALLOWED_USERS:
        await update.message.reply_text("You are not authorized to use this bot.")
        return
    await update.message.reply_text("Hi, I am the DarkSeek R1 🐋\n\nI am built to be the dark and unrestricted version of DeepSeek AI model.\n\nHow can I help you?")

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in cfg.ALLOWED_USERS:
        await update.message.reply_text("You are not authorized to use this bot.")
        return

    prompt = update.message.text

    generating_message = await update.message.reply_text("Thinking...")

    # Show "typing..." action
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    answer = chat_request(prompt)

    if answer:
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Error. Try again.")

def main() -> None:
    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling
    print("Program Started")
    app.run_polling()

if __name__ == "__main__":
    main()
