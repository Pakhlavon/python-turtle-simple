from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

city = 1
if city == 1:
    t = requests.get('https://sinoptik.ua/погода-ташкент')
elif city == 2:
    t = requests.get('https://sinoptik.ua/погода-наманган')
elif city == 3:
    t = requests.get('https://sinoptik.ua/погода-фергана')
elif city == 4:
    t = requests.get('https://sinoptik.ua/погода-андижан')
elif city == 5:
    t = requests.get('https://sinoptik.ua/погода-джизак')
elif city == 6:
    t = requests.get('https://sinoptik.ua/погода-самарканд')
elif city == 7:
    t = requests.get('https://sinoptik.ua/погода-бухара')
elif city == 8:
    t = requests.get('https://sinoptik.ua/погода-навои')
elif city == 9:
    t = requests.get('https://sinoptik.ua/погода-карши')
elif city == 10:
    t = requests.get('https://sinoptik.ua/погода-карши')
elif city == 11:
    t = requests.get('https://sinoptik.ua/погода-гулистан')

htm = BS(t.content, 'html.parser')

for el in htm.select('#content'):
     min = el.select('.temperature .min')[0].text
     max = el.select('.temperature .max')[0].text
t_min = min[4:]
t_max = max[5:]

print(t_min, t_max)

def cities():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"01")],
        [InlineKeyboardButton("Namangan", callback_data=f"02")],
        [InlineKeyboardButton("Farg'ona", callback_data=f"03")],
        [InlineKeyboardButton("Andijon", callback_data=f"04")],
        [InlineKeyboardButton("Jizzax", callback_data=f"05")],
        [InlineKeyboardButton("Samarqand", callback_data=f"06")],
        [InlineKeyboardButton("Buxoro", callback_data=f"07")],
        [InlineKeyboardButton("Navoiy", callback_data=f"08")],
        [InlineKeyboardButton("Qashqadaryo", callback_data=f"09")],
        [InlineKeyboardButton("Surxondaryo", callback_data=f"10")],
        [InlineKeyboardButton("Guliston", callback_data=f"11")],
    ]
def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]

def inline_handler(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "02":
        query.message.edit_text(f"Bugun Namangan shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "03":
        query.message.edit_text(f"Bugun Farg'ona shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "04":
        query.message.edit_text(f"Bugun Andijon shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "05":
        query.message.edit_text(f"Bugun Jizzax shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "06":
        query.message.edit_text(f"Bugun Samarqand shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "07":
        query.message.edit_text(f"Bugun Buxoro shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "08":
        query.message.edit_text(f"Bugun Navoiy shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "09":
        query.message.edit_text(f"Bugun Qashqadaryo shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "10":
        query.message.edit_text(f"Bugun Surxondaryo shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "11":
        query.message.edit_text(f"Bugun Guliston shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0]  == "back1":
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanla 👇",
            reply_markup=InlineKeyboardMarkup(cities())
        )


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} 🖐🏻\nBu yerdan Shahar yoki Viloyatni tanla 👇""",
                              reply_markup=InlineKeyboardMarkup(cities())
                              )


def main():
    Token  = "5928799789:AAGQqju6VnyWAL1AvcrqQvj0uPDEmN_qCsk"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    updater.start_polling()
    updater.idle()


if __name__ =='__main__':
    main()

