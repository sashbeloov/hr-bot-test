import aiogram
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
import asyncio

TOKEN = "8169645229:AAF1-3yZY4Oo8JLYRm9PCYI0yoHUpagBYBY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}

@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start" or message.text == "Bosh menu" or message.text == "Bosh sahifa":
        await start(message)
    elif message.text == "Biz haqimizda":
        await aboutus(message)
    elif "HolatTil" in user_data[user_id] and message.text == "Orqaga":
        await start(message)
    elif message.text == "Til 🇺🇿/🇷🇺":
        await languages(message)
    elif message.text == "Bo'sh ish o'rinlari":
        await diractions(message)
    elif "diraction" in user_data[user_id]:
        await check_button_diractions(message)




@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="Biz haqimizda"),],
        [types.KeyboardButton(text="Bo'sh ish o'rinlari"), ],
        [types.KeyboardButton(text="Til 🇺🇿/🇷🇺")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "images/korzinka-main.jpg"
    caption_text = (
        "Приветствую Вас, я HR-бот Корзинки.\n\n"
        "🤖Я:\n\n"
        "- расскажу Вам о компании и о преимуществах работы у нас;\n"
        "- помогу найти актуальные вакансии и заполнить анкету.\n\n"
        "Работа в Корзинке все лучше и лучше\n\n"
        "-------------------------------------------------------\n\n"
        "Xush kelibsiz, men HR-bot Korzinka\n\n"
        "🤖Men:\n\n"
        "- sizga kompaniya haqida va biz bilan ishlashning afzalliklari haqida gapirib beraman;\n"
        "- mavjud vakansiyalarni topishga va so'rovnomani to'ldirishga yordam beraman.\n\n"
        "Korzinkada odatdagidan yaxshi ish"
    )
    await message.answer_photo(
                    caption=caption_text,
                    photo=types.FSInputFile(path=file_path),
                    parse_mode="Markdown",
                    reply_markup=keyboard)
    print(user_data)


@dp.message(Command("Biz haqimizda"))
async def aboutus(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = message.text
    button = [
            [types.InlineKeyboardButton(text='Наш сайт',url="https://rabota.korzinka.uz/")]
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer(
        "Anglesey Food (tm: korzinka) 1996-yilda tashkil etilgan va u O‘zbekistondagi birinchi supermarketlar tarmog‘iga aylandi.  Bugun mubolag‘asiz aytish mumkinki, har kuni o‘n minglab mijozlarga xizmat ko‘rsatuvchi “Korzinka” milliy brendga, xalq nomiga aylanib ulgurdi. Biz uchun mijozlarimizning ishonchi va sadoqati katta yutug‘imizdir.\n\n"
                                 "Biz o‘zimiz uchun eng qiziqarli missiyani tanladik - odatiy xarid sayohatini yanada yoqimli va hayajonli narsaga aylantirish.\n\n"
                                 "Biz har kuni o‘zgarib, odatdagidan yaxshiroq bo‘lish uchun o‘z ustimizda tinmay ishlamoqdamiz.  Bizning kuchli tomonlarimiz – iste’molchilar bilan to‘g‘ridan-to‘g‘ri muloqot qilishning innovatsion usullari bilan uyg‘unlashgan xizmat ko‘rsatishning yuqori standartlari, sifatli oziq-ovqat va nooziq-ovqat mahsulotlarining keng assortimenti, unumli narx siyosati va jozibador marketing dasturlari tufayli muvaffaqiyatga erishishda davom etamiz.\n"
                                 "Biz haqimizda [korzinka](https://korzinka.uz) sahifamiz orqali yanada ko‘proq bilib oling", reply_markup=keyboard)
    print(user_data)



@dp.message(Command("Til 🇺🇿/🇷🇺"))
async def languages(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["HolatTil"] = message.text
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"),types.KeyboardButton(text="🇺🇿 O'zbekcha"),],
        [types.KeyboardButton(text="Orqaga")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Tilni o'zgartirish", reply_markup=keyboard)
    print(user_data)


@dp.message(Command("Bo'sh ish o'rinlari"))
async def diractions(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["diraction"] = message.text
    button = [
        [types.KeyboardButton(text="Korzinka magazinlari"),types.KeyboardButton(text="Korzinka Go (Yetkazib berish)"),],
        [types.KeyboardButton(text="Yetkazib berish/Ombor"),types.KeyboardButton(text="Ofis"),],
        [types.KeyboardButton(text="Bosh menu"),types.KeyboardButton(text="Orqaga"),],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Yo'nalishni tanlang", reply_markup=keyboard)
    print(user_data)



async def check_button_diractions(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = message.text
    if message.text == "Korzinka magazinlari":
        await korzinka_stores(message)
    elif message.text == "Korzinka Go (Yetkazib berish)":
        await korzinka_go(message)
    elif message.text == "Yetkazib berish/Ombor":
        await yetkazib_berish_Ombor(message)
    elif message.text == "Ofis":
        await ofis(message)
    elif message.text == "Orqaga":
        await start(message)
    elif message.text == "Toshkent":
        await korzinka_toshkent(message)
    elif message.text == "Orqaga" and "stores" in user_data[user_id]:
        await diractions(message)
    print(user_data)



# diractions funksiyasiga tegishli tugmalarga ishlaydi va ular check_button_diractions funksiyasida tekshiruvga qarab chaqiriladi
@dp.message(Command("Korzinka magazinlari"))
async def korzinka_stores(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["stores"] = "stores"
    button = [
        [types.KeyboardButton(text="Toshkent"),types.KeyboardButton(text="Toshkent viloyati")],
        [types.KeyboardButton(text="Samarqand viloyati"),types.KeyboardButton(text="Farg'ona viloyati")],
        [types.KeyboardButton(text="Namangan viloyati"),types.KeyboardButton(text="Andijon viloyati")],
        [types.KeyboardButton(text="Qashqadaryo viloyati"),types.KeyboardButton(text="Sirdaryo viloyati")],
        [types.KeyboardButton(text="Buxoro viloyati"),types.KeyboardButton(text="Navoiy viloyati")],
        [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Keling, anketagizni yaratamiz", reply_markup=keyboard)
    await message.answer("Qayerda ishlamoqchisiz, hududni tanlang:")
    print(user_data)


# async def check_city(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id]["holat_city"] = "check_city"
#     if message.text == "Toshkent":
#         await korzinka_toshkent(message)
#         print("shu kodgacha kela oldi")
#     elif message.text == "Toshkent viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Samarqand viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Farg'ona viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Namangan viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Andijon viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Qashqadaryo viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Sirdaryo viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Buxoro viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Navoiy viloyati" and "stores" in user_data[user_id]:
#         pass
#     elif message.text == "Orqaga":
#         pass
#     print(user_data)


# bu check_city ni ichida tekshirilmoqda va check_city funksiyasida aynan qaysi komanda kelishiga bu funksiya ishlashi yozilgan
@dp.message(Command("Toshkent"))
async def korzinka_toshkent(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["korzinka_toshkent"] = message.text
    button = [
        [types.KeyboardButton(text="Yunusobo tumani"),types.KeyboardButton(text="Yakkasaroy tumani")],
        [types.KeyboardButton(text="Mirzo Ulug'bek tumani"),types.KeyboardButton(text="Uchtepa tumani")],
        [types.KeyboardButton(text="Olmazor tumani"),types.KeyboardButton(text="Yashnobod tumani")],
        [types.KeyboardButton(text="Sergili tumani"),types.KeyboardButton(text="Shayxontohur tumani")],
        [types.KeyboardButton(text="Mirobod tumani"),types.KeyboardButton(text="Bektemir tumani")],
        [types.KeyboardButton(text="Chilonzor tumani"),types.KeyboardButton(text="Yangi hayot tumani")],
        [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Keling, anketagizni yaratamiz", reply_markup=keyboard)
    await message.answer("Qayerda ishlamoqchisiz, hududni tanlang:",)
    print(user_data)



# diractions funksiyasiga tegishli tugmalarga ishlaydi va ular check_button_diractions funksiyasida tekshiruvga qarab chaqiriladi
@dp.message(Command("Ofis"))
async def ofis(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["Ofis"] = message.text
    button = [
        [types.KeyboardButton(text="Toshkent")],
        [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga"),],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Keling, anketagizni yaratamiz", reply_markup=keyboard)
    await message.answer("Tumanni tanlang:")
    print(user_data)


# diractions funksiyasiga tegishli tugmalarga ishlaydi va ular check_button_diractions funksiyasida tekshiruvga qarab chaqiriladi
@dp.message(Command("Korzinka Go (Yetkazib berish)"))
async def korzinka_go(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["Korzinka-Go"] = message.text
    button = [
        [types.KeyboardButton(text="Toshkent"),types.KeyboardButton(text="Samarqand viloyati"),],
        [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Keling, anketagizni yaratamiz", reply_markup=keyboard)
    await message.answer("Qayerda ishlamoqchisiz, hududni tanlang:",)
    print(user_data)



# diractions funksiyasiga tegishli tugmalarga ishlaydi va ular check_button_diractions funksiyasida tekshiruvga qarab chaqiriladi
@dp.message(Command("Yetkazib berish/Ombor"))
async def yetkazib_berish_Ombor(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["Korzinka-Go"] = message.text
    button = [
        [types.KeyboardButton(text="Toshkent"),types.KeyboardButton(text="Samarqand viloyati"),],
        [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Keling, anketagizni yaratamiz", reply_markup=keyboard)
    await message.answer("Qayerda ishlamoqchisiz, hududni tanlang:",)
    print(user_data)



async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())

