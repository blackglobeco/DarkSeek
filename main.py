from telethon import TelegramClient, events
import config as cfg
from utils import chat_request

app = TelegramClient('UserBot_Session', api_id=None, api_hash=None).start(bot_token=cfg.BOT_TOKEN)

@app.on(events.NewMessage(incoming=True))
async def on_incoming_message(event: events.NewMessage.Event):
    user_id = event.message.sender_id
    
    if user_id not in cfg.ALLOWED_USERS:
        await event.message.reply("You are not authorized to use this bot.")
        return
    
    prompt = event.message.message
    
    if prompt == "/start":
        await event.message.reply("Hello, I am the DeepSeek R1 Telegram Bot. Chat with me here.")
        return
    
    answer = chat_request(prompt)

    if answer:
        await event.message.reply(answer)
    else:
        await event.message.reply("Error. Try again.")

if __name__ == "__main__":
    try:
        print("Program Started")
        app.run_until_disconnected()
    except KeyboardInterrupt:
        print("Program Finished")
