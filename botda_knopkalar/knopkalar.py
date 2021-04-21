from telegram import Update, ForceReply, ReplyKeyboardMarkup, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from bot_tokeni import SAQLA3
from bot_funksiyalari1 import User_uchun, save_user, faktorial, fibo_son, kub, int_to_roman, roman_to_int,\
    mobil_operator, teskariMatn




users = {}
bot = Bot(SAQLA3)
main = {"matem": ["Faktorial", "Fibonachi sonlari", "Sonning kubi"],
        "konver": ["Arab raqamini -> Rim raqamiga", "Rim raqamini -> Arab raqamiga"],
        "others": ["Matnni teskarilash", "Telefon raqami operatori(kompaniyasi) tekshirish"]
        }
knopka = {"main_menu":
    [
        [InlineKeyboardButton("MATEMATIKA", callback_data="matem")],
        [InlineKeyboardButton("KONVENTATORLAR", callback_data="konver")],
        [InlineKeyboardButton("BOSHQA", callback_data="other")]
    ]
        }
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    print(update.message.from_user.first_name)
    save_user(update.message.from_user.first_name)

    if update.message.from_user.id in users:

        knopka = [
            [InlineKeyboardButton("MATEMATIKA", callback_data="matem")],
            [InlineKeyboardButton("KONVENTATORLAR", callback_data="konver")],
            [InlineKeyboardButton("BOSHQA", callback_data="other")]
        ]

        knopkani_korsatish = InlineKeyboardMarkup(knopka)

        k = update.message.reply_text("Kerakli bo'limni tanlang!", reply_markup=knopkani_korsatish)

    else:
        user = User_uchun(update.message.from_user.id, update.message.from_user.first_name, "start")
        users.update({update.message.from_user.id: user})

        knopka = [
            [InlineKeyboardButton("MATEMATIKA", callback_data="matem")],
            [InlineKeyboardButton("KONVENTATORLAR", callback_data="konver")],
            [InlineKeyboardButton("BOSHQA", callback_data="other")]
        ]

        knopkani_korsatish = InlineKeyboardMarkup(knopka)

        k = update.message.reply_text("Kerakli bo'limni tanlang!", reply_markup=knopkani_korsatish)

def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    print(update.message.from_user.name)
    name = update.message.from_user.name
    update.message.reply_text(f'{name}, sizga qanday yordam kerak?')


def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    try:
        user = users[update.message.from_user.id]
        if user.position == "sonning kubi":
            # bot.send_video(update.message.from_user.id, update.message.text)

            keyboard = [
                [InlineKeyboardButton("Back", callback_data='nazad')],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text(kub(update.message.text), reply_markup=reply_markup)
        elif user.position == 'faktorial':

            keyboard = [
                [InlineKeyboardButton("Back", callback_data='nazad')],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text(faktorial(update.message.text), reply_markup=reply_markup)
        elif user.position == 'fibonachi sonlari':

            keyboard = [
                [InlineKeyboardButton("Back", callback_data='nazad')],
            ]
        
            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text(fibo_son(update.message.text), reply_markup=reply_markup)
    except KeyError:
        bot.send_message(update.message.chat_id, 'Iltimos, avval /start ni yuboring!')


def callback_command(update: Update, _: CallbackContext):
    try:
        user = users[update.callback_query.from_user.id]

        if update.callback_query.data == 'matem':
            knopka = [
                [InlineKeyboardButton("Faktorial", callback_data="faktorial")],
                [InlineKeyboardButton("Fibonachi sonlari", callback_data="fibonachi sonlari")],
                [InlineKeyboardButton("Sonning kubi", callback_data="sonning kubi")]
            ]

            knopkani_korsatish = InlineKeyboardMarkup(knopka)

            # k = update.message.reply_text("Kerakli funksiyanni tanlang!", reply_markup=knopkani_korsatish)
            bot.send_message(chat_id=user.user__id,text="Kerakli funksiyanni tanlang!",reply_markup=knopkani_korsatish)
            user.position = 'matem'

        elif update.callback_query.data == 'sonning kubi':

            bot.send_message(chat_id=user.user__id, text="Raqamni kiriting va uni kubini hisoblab beramiz:")
            user.position = 'sonning kubi'
        elif update.callback_query.data == 'faktorial':

            bot.send_message(chat_id=user.user__id, text="Raqamni kiriting va uni faktorialini hisoblab beramiz:")
            user.position = 'faktorial'
        elif update.callback_query.data == 'fibonachi sonlari':

            bot.send_message(chat_id=user.user__id, text="Raqamni kiriting va uni fibonachi sonlarini hisoblab beramiz:")
            user.position = 'fibonachi sonlari'
        elif update.callback_query.data == 'nazad':
            user.position = 'Start'
            knopka = [
                [InlineKeyboardButton("Faktorial", callback_data="faktorial")],
                [InlineKeyboardButton("Fibonachi sonlari", callback_data="fibonachi sonlari")],
                [InlineKeyboardButton("Sonning kubi", callback_data="sonning kubi")]
            ]

            knopkani_korsatish = InlineKeyboardMarkup(knopka)

            # k = update.message.reply_text("Kerakli funksiyanni tanlang!", reply_markup=knopkani_korsatish)
            bot.send_message(chat_id=user.user__id, text="Kerakli funksiyanni tanlang!",
                             reply_markup=knopkani_korsatish)
            user.position = 'matem'

    except KeyError:
        bot.send_message(update.callback_query.from_user.id, 'Iltimos, avval /start ni bosing!')



    # elif user['menu'] == 'menu':
    #     user['menu'] = update.callback_query.data
    #     kb = []
    #     for k in menu[user['lang']][update.callback_query.data]:
    #         kb.append([InlineKeyboardButton(k, callback_data=k)])
    #
    #     reply_markup = InlineKeyboardMarkup(kb)
    #     bot.editMessageText(text='Please choose:', chat_id=user_id, message_id=user['message_id'],
    #     reply_markup=reply_markup)
    #     user['menu'] = 'News'
    #     users[user_id] = user
    #
    # elif user['menu'] == 'News':
    #     user['lang'] = update.callback_query.data
    #     kb = []
    #     for k in menu[user['lang']['News']]:
    #         kb.append([InlineKeyboardButton(k, callback_data=k)])
    #
    #     reply_markup = InlineKeyboardMarkup(kb)
    #     bot.editMessageText(text='Please choose:', chat_id=user_id, message_id=user['message_id'],
    #     reply_markup=reply_markup)
    #     # user['menu'] = 'menu'
    #     users[user_id] = user





def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(SAQLA3)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.photo | Filters.audio, echo))

    #test
    dispatcher.add_handler(CallbackQueryHandler(callback_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
