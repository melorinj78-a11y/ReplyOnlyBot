from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = 8787563547:AAEUoB_ccx6WG3kzqm0Uxxqke5fXRme4Kdg


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
