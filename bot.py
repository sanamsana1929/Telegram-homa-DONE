
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from config import TOKEN, ADMIN_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("رزرو وقت", callback_data="reserve")],
        [InlineKeyboardButton("پشتیبانی", callback_data="support")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("به ربات خوش آمدید! لطفا یک گزینه را انتخاب کنید:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "support":
        await query.edit_message_text("برای پشتیبانی با @Homa_Psychology در ارتباط باشید📩")
    elif query.data == "reserve":
        await query.edit_message_text("لطفا برای رزرو وقت با ارسال بیعانه اقدام کنید.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
