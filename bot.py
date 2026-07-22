import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

import os

TOKEN = os.getenv("8787563547:AAFHDXVOY1XjZt-257A6MdAJ5Eu3Q1WnfsE")

async def reply_only(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if message.reply_to_message:
        return

    try:
        await message.delete()
    except:
        pass


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL & (~filters.StatusUpdate.ALL), reply_only)
)

app.run_polling()
