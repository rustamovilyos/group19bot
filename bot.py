from telegram import Update, ForceReply, ReplyKeyboardMarkup, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import dont_add_git
from bot_funksiyalari import faktorial, fibo_son, int_to_roman, roman_to_int, mobil_operator, teskariMatn


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Salom {user.mention_markdown_v2()} \! \n'
        f"Botda turli foydali funksiyalar bor\."
        f"Ularni ko'rish uchun /functions buyrug'ini bosing",
        # f'Bot istalgan sonning Faktorialni hisoblaydi ixtiyoriy son kiriting: ',
        reply_markup=ForceReply(selective=True)
    )
    print(update.message.from_user.name)

users = {}
bot = Bot(dont_add_git.SAQLA)


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the c-ommand /help is issued."""
    print(update.message.from_user.name)
    update.message.reply_text("Sizga qanday yordam kerak?")

def funksiyalar(update: Update, _: CallbackContext) -> None:
    keyboard_commands = [["Arabic ➡ Roman"], ["Roman ➡ Arabic"], ["Fibonacci numbers"],
                         ["Check Mob Op 👨🏻‍💻"], ["Reverse text ◀"], ["Factorial !"]
                         ]
    update.message.reply_text(
        "Kerakli funksiyani tanlang👇",
        reply_markup=ReplyKeyboardMarkup(keyboard_commands, one_time_keyboard=True),
    )
    # if users[update.message.from_user.id]["status"] == "Factorial !":
    #
    #     bot.sendMessage(update.message.from_user.id, str(faktorial(update.message.text)))
    # else:
    #     update.message.reply_text("Xatoo")
    if update.message.from_user.id not in users:
        users.update({update.message.from_user.id: {'status': 'funksiyalar'}})

    if update.message.text == "Arabic ➡ Roman":
        users[update.message.from_user.id]["status"] = "Arabic ➡ Roman"
        bot.sendMessage(update.message.from_user.id, f"Siz arab raqamlarini rim raqamlariga"
                                                     f" o'tkazuvchi funksiyani tanladingiz \n"
                                                     f"Arab raqami(odatiy raqamlar) kiriting 👇")
    elif users[update.message.from_user.id]['status'] == "Arabic ➡ Roman":
        natija = str(f"Natija: {int_to_roman(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)

    if update.message.text == "Roman ➡ Arabic":
        users[update.message.from_user.id]["status"] = "Roman ➡ Arabic"
        bot.sendMessage(update.message.from_user.id, f"Siz rim raqamlarini arab raqamlariga"
                                                     f" o'tkazuvchi funksiyani tanladingiz \n"
                                                     f"Rim raqamini kiriting👇")
    elif users[update.message.from_user.id]['status'] == "Roman ➡ Arabic":
        natija = str(f"Natija: {roman_to_int(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)

    if update.message.text == "Fibonacci numbers":
        users[update.message.from_user.id]['status'] = "Fibonacci numbers"
        bot.sendMessage(update.message.from_user.id, f"Siz Fibonachi sonlarini hisoblovchi funksiyani tanladingiz \n"
                                                     f"Nechchiga bo'lgan Fibonachi sonlarini topamiz ?")
    elif users[update.message.from_user.id]['status'] == "Fibonacci numbers":
        natija = str(f"Fibonachi sonlari: {fibo_son(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)

    if update.message.text == "Check Mob Op 👨🏻‍💻":
        users[update.message.from_user.id]["status"] = "Check Mob Op 👨🏻‍💻"
        bot.sendMessage(update.message.from_user.id, f"Siz O'zbekiston raqamlarinig operatorlarini tekshirish"
                                                     f" funksiyasini tanladingiz\n"
                                                     f"Raqamingizni tekshirish uchun 99894 kabi kiriting👇")
    elif users[update.message.from_user.id]["status"] == "Check Mob Op 👨🏻‍💻":
        raqam = str(f"Sizning operatoringiz: {mobil_operator(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, raqam)

    if update.message.text == "Reverse text ◀":
        users[update.message.from_user.id]["status"] = "Reverse text ◀"
        bot.sendMessage(update.message.from_user.id, f"Siz kiritilgan matnni o'ngdan chapga(teskari) yozib beruvchi"
                                                     f" funksiyasini tanladingiz\n"
                                                     f"Kerakli matnni kiriting👇")
    elif users[update.message.from_user.id]["status"] == "Reverse text ◀":
        raqam = str(f"Siz kiritgan matnning teskari shakli :) >> {teskariMatn(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, raqam)

    if update.message.text == "Factorial !":
        users[update.message.from_user.id]['status'] = "Factorial !"
        bot.sendMessage(update.message.from_user.id, f"Siz sonning Faktorialini hisoblovchi funksiyani tanladingiz \n"
                                                     f"Qanday sonning faktorialini hisoblaymiz ?")
    elif users[update.message.from_user.id]['status'] == "Factorial !":
        natija = str(f"Natija: {faktorial(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)
    # if users[update.message.from_user.id]['status'] == "Factorial !":
    #     natija = str(f"Natija: {faktorial(update.message.text)}")
    #     bot.sendMessage(update.message.from_user.id, natija)
    # if users[update.message.from_user.id]['status'] == "Fibonacci":
    #     natija = str(f"Fibonachi sonlari: {fibo_son(update.message.text)}")
    #     bot.sendMessage(update.message.from_user.id, natija)
    # elif update.message.text == "Factorial !":
    #     users[update.message.from_user.id]['status'] = "Factorial !"
    #     bot.sendMessage(update.message.from_user.id, f"Siz sonning Faktorialini hisoblovchi funksiyani tanladingiz \n"
    #                                                  f"Qanday sonning faktorialini hisoblaymiz ?")
    # elif update.message.text == "Fibonacci numbers":
    #     users[update.message.from_user.id]['status'] = "Fibonacci numbers"
    #     bot.sendMessage(update.message.from_user.id, f"Siz Fibonachi sonlarini hisoblovchi funksiyani tanladingiz \n"
    #                                                  f"Nechchiga bo'lgan Fibonachi sonlarini topamiz ?")



def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""

    if update.message.text == "Arabic ➡ Roman":
        users[update.message.from_user.id]["status"] = "Arabic ➡ Roman"
        bot.sendMessage(update.message.from_user.id, f"Siz arab raqamlarini rim raqamlariga"
                                                     f" o'tkazuvchi funksiyani tanladingiz \n"
                                                     f"Arab raqami(odatiy raqamlar) kiriting 👇")
    elif users[update.message.from_user.id]['status'] == "Arabic ➡ Roman":
        natija = str(f"Natija: {int_to_roman(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)

    if update.message.text == "Roman ➡ Arabic":
        users[update.message.from_user.id]["status"] = "Roman ➡ Arabic"
        bot.sendMessage(update.message.from_user.id, f"Siz rim raqamlarini arab raqamlariga"
                                                     f" o'tkazuvchi funksiyani tanladingiz \n"
                                                     f"Rim raqamini kiriting👇")
    elif users[update.message.from_user.id]['status'] == "Roman ➡ Arabic":
        natija = str(f"Natija: {roman_to_int(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)

    if update.message.text == "Fibonacci numbers":
        users[update.message.from_user.id]['status'] = "Fibonacci numbers"
        bot.sendMessage(update.message.from_user.id, f"Siz Fibonachi sonlarini hisoblovchi funksiyani tanladingiz \n"
                                                     f"Nechchiga bo'lgan Fibonachi sonlarini topamiz ?")
    elif users[update.message.from_user.id]['status'] == "Fibonacci numbers":
        natija = str(f"Fibonachi sonlari: {fibo_son(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)

    if update.message.text == "Check Mob Op 👨🏻‍💻":
        users[update.message.from_user.id]["status"] = "Check Mob Op 👨🏻‍💻"
        bot.sendMessage(update.message.from_user.id, f"Siz O'zbekiston raqamlarinig operatorlarini tekshirish"
                                                     f" funksiyasini tanladingiz\n"
                                                     f"Raqamingizni tekshirish uchun 99894 kabi kiriting👇")
    elif users[update.message.from_user.id]["status"] == "Check Mob Op 👨🏻‍💻":
        raqam = str(f"Sizning operatoringiz: {mobil_operator(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, raqam)

    if update.message.text == "Reverse text ◀":
        users[update.message.from_user.id]["status"] = "Reverse text ◀"
        bot.sendMessage(update.message.from_user.id, f"Siz kiritilgan matnni o'ngdan chapga(teskari) yozib beruvchi"
                                                     f" funksiyasini tanladingiz\n"
                                                     f"Kerakli matnni kiriting👇")
    elif users[update.message.from_user.id]["status"] == "Reverse text ◀":
        raqam = str(f"Siz kiritgan matnning teskari shakli :) >> {teskariMatn(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, raqam)

    if update.message.text == "Factorial !":
        users[update.message.from_user.id]['status'] = "Factorial !"
        bot.sendMessage(update.message.from_user.id, f"Siz sonning Faktorialini hisoblovchi funksiyani tanladingiz \n"
                                                     f"Qanday sonning faktorialini hisoblaymiz ?")
    elif users[update.message.from_user.id]['status'] == "Factorial !":
        natija = str(f"Natija: {faktorial(update.message.text)}")
        bot.sendMessage(update.message.from_user.id, natija)
    print(update.message.from_user.name)
    print(update.message.text)
    # if update.message.from_user.id not in users:
    #     users.update({update.message.from_user.id: ' '})
    #     users.update({update.message.from_user.id: {
    #         "status": "komandalar"
    #     }})


    # try:
    #     x = faktorial(update.message.text)
    #     update.message.reply_text(f"{update.message.text}! = {x}")
    # except ValueError:
    #     update.message.reply_text("Faktorial faqat raqamlarda xisoblanadi :) ")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(dont_add_git.SAQLA)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("functions", funksiyalar))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()