from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = '7331545811:AAGeRp1rXt1vzkon_4WG-myUmuTZJnX5Tqs'
CHANNEL_ID = '@testbot7676'

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("دریافت ادلیست جدید اسپینر", callback_data='get_spinner')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('لطفا یک گزینه را انتخاب کنید:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'get_spinner':
        keyboard = [
            [InlineKeyboardButton("عضو شدم", callback_data='check_membership')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text="ابتدا در کانال یادآور عضو شوید",
            reply_markup=reply_markup
        )

def check_membership(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    try:
        user_status = context.bot.get_chat_member(CHANNEL_ID, user_id).status
        if user_status in ['member', 'administrator', 'creator']:
            query.edit_message_text(text="https://t.me/addlist/2_spmikbsQI4MWI0")
        else:
            query.edit_message_text(text="شما عضو کانال یادآور نیستید")
    except:
        query.edit_message_text(text="خطایی رخ داده است")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CallbackQueryHandler(check_membership, pattern='^check_membership$'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()