import telebot
from telebot import types

BOT_TOKEN = "8965802700:AAHkyL8frV06Of_Z2S6CKhmjGYqTPO0Fy5U"

bot = telebot.TeleBot(BOT_TOKEN)

# Taomlar ma'lumotlari
FISH_MENU = [
    {"nomi": "🐟 Qovurilgan Zog'ora (Sazan)", "narx": "65 000 so'm / por", "tavsif": "Maxsus ziravorlar bilan pishirilgan mazali zog'ora baliq."},
    {"nomi": "🐟 Sudak filesi", "narx": "75 000 so'm / por", "tavsif": "Suyaksiz, qarsildoq qilib qovurilgan sudak baliq filesi."},
    {"nomi": "🐟 Tandirda pishirilgan Laqqa", "narx": "80 000 so'm / por", "tavsif": "Tandirda dudlangan xushbo'y laqqa baliq."},
    {"nomi": "🍲 Baliq sho'rva (Uxa)", "narx": "40 000 so'm", "tavsif": "Yangi baliqdan tayyorlangan to'yimli va foydali sho'rva."}
]

SOMSA_MENU = [
    {"nomi": "🥟 Go'shtli Tandir Somsa", "narx": "12 000 so'm / dona", "tavsif": "Mayin mol go'shti va dumba yog'i bilan tayyorlangan tandir somsa."},
    {"nomi": "🥟 ZAR Maxsus Baliqli Somsa", "narx": "15 000 so'm / dona", "tavsif": "Restoranimizning maxsus baliq go'shtli tansiq somsasi."},
    {"nomi": "🥟 Qatlama Qovurma Somsa", "narx": "10 000 so'm / dona", "tavsif": "Qarsildoq qatlama xamirdan tayyorlangan shirin somsa."},
    {"nomi": "🥟 Ko'k Somsa (Mavsumiy)", "narx": "8 000 so'm / dona", "tavsif": "Yangi ko'katlar va maxsus ziravorlar bilan tayyorlangan."}
]

def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_fish = types.KeyboardButton("🐟 Baliq taomlari")
    btn_somsa = types.KeyboardButton("🥟 Somsa menyusi")
    btn_order = types.KeyboardButton("📞 Buyurtma berish")
    btn_info = types.KeyboardButton("📍 Manzil va Ish vaqti")
    markup.add(btn_fish, btn_somsa)
    markup.add(btn_order, btn_info)
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = (
        f"Assalomu alaykum, <b>{message.from_user.first_name}</b>!\n\n"
        f"👑 <b>«ZAR BALIQ»</b> restorani rasmiy botiga xush kelibsiz!\n\n"
        f"Bizda eng mazali, yangi baliq taomlari va qarsildoq issiq somsalar sizni kutmoqda.\n\n"
        f"Kerakli bo'limni tanlang 👇"
    )
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: message.text == "🐟 Baliq taomlari")
def fish_menu_handler(message):
    text = "🐟 <b>«ZAR BALIQ» - Baliq taomlari menyusi:</b>\n\n"
    for item in FISH_MENU:
        text += f"▪️ <b>{item['nomi']}</b>\n   Narxi: <i>{item['narx']}</i>\n   {item['tavsif']}\n\n"
    bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "🥟 Somsa menyusi")
def somsa_menu_handler(message):
    text = "🥟 <b>«ZAR BALIQ» - Somsa menyusi:</b>\n\n"
    for item in SOMSA_MENU:
        text += f"▪️ <b>{item['nomi']}</b>\n   Narxi: <i>{item['narx']}</i>\n   {item['tavsif']}\n\n"
    bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "📞 Buyurtma berish")
def order_handler(message):
    text = (
        "📞 <b>Buyurtma va Yetkazib berish:</b>\n\n"
        "Buyurtma berish yoki stol band qilish uchun biz bilan bog'laning:\n"
        "☎️ Telefon: +998 90 123 45 67\n"
        "☎️ Qo'shimcha: +998 71 200 00 00\n"
        "👤 Telegram admin: @zar_baliq_admin\n\n"
        "<i>Yetkazib berish xizmati mavjud!</i>"
    )
    bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "📍 Manzil va Ish vaqti")
def info_handler(message):
    text = (
        "📍 <b>«ZAR BALIQ» Restorani haqida:</b>\n\n"
        "🏢 Manzil: Toshkent shahri, Zar Baliq restorani (Mo'ljal: asosiy yo'l yoqasida)\n"
        "⏰ Ish vaqti: Har kuni 10:00 dan 23:00 gacha\n"
        "🚗 Avtoturargoh va oilaviy shinam xonalar mavjud!"
    )
    bot.send_message(message.chat.id, text, parse_mode='HTML')

if __name__ == "__main__":
    print("ZAR BALIQ boti ishga tushirildi...")
    bot.infinity_polling()
