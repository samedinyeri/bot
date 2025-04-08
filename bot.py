import datetime
import asyncio
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "7947835440:AAFLkWK3VkFm5KWhrB0FOHzu_gHOZWwyQwc"
CHAT_ID = 552927120
tanisma_tarihi = datetime.date(2024, 9, 28)

medyalar = [
    {"tip": "gif", "url": "https://media.giphy.com/media/3orieRzVMx2eL4DaVW/giphy.gif"},
    {"tip": "sticker", "file_id": "CAACAgUAAxkBAAEFQO9kbhXrZ3VnDPUp06d37IQgU7oF4QACgwkAAhZr2VQ7Uxlgh8SGFS8E"}
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Kaç gün oldu?", callback_data="kacgun")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hoş geldin aşk botuna 😍", reply_markup=reply_markup)

async def buton_cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    bugun = datetime.date.today()
    fark = bugun - tanisma_tarihi
    ay = fark.days // 30
    gun = fark.days % 30
    mesaj = f"Bugün {ay}. ay, {gun} gününüz kutlu olsun! 💖\nTanışma günü: {tanisma_tarihi.strftime('%d.%m.%Y')}"
    await query.message.reply_text(mesaj)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buton_cevap))

print("Bot çalışıyo Replit reis 😎")
app.run_polling()
