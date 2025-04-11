from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive
import os
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def send1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.delete()
    msg_text = ' '.join(context.args)
    if msg_text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg_text)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a message.")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("send1", send1))
    print("Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    keep_alive()
    asyncio.run(main())
