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
    elif message.text == "Til 🇺🇿/🇷🇺":
        await languages(message)
    elif message.text == "Bo'sh ish o'rinlari":
        await boshishorinlari(message)
    elif message.text == "Korzinka magazinlari":
        await korzinka_stores(message)
    elif message.text == "Toshkent":
        await korzinka_toshkent(message)
    elif message.text == "Ofis":
        await ofis(message)
    elif message.text == "Korzinka Go (Yetkazib berish)":
        await korzinka_go(message)
    elif message.text == "Yetkazib berish/Ombor":
        await yetkazib_berish_Ombor(message)
    elif "korzinka_toshkent" in user_data[user_id]:
        await position(message)
    elif "tuman" in user_data[user_id]:
        await free_position(message)
    elif "choosed_position" in user_data[user_id]:
        await filial(message)




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
async def boshishorinlari(message: types.Message):
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


sets_location = {"Yunusobo tumani","Yakkasaroy tumani","Mirzo Ulug'bek tumani","Uchtepa tumani",
                 "Olmazor tumani","Yashnobod tumani","Sergili tumani","Shayxontohur tumani",
                 "Mirobod tumani","Bektemir tumani","Chilonzor tumani","Yangi hayot tumani"}


async def position(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["tuman"] = message.text
    if message.text in sets_location:
        button = [
            [types.KeyboardButton(text="Yuk tashuvchi"),types.KeyboardButton(text="Tozalik xodimi")],
            [types.KeyboardButton(text="Oshpaz"),types.KeyboardButton(text="Kassir")],
            [types.KeyboardButton(text="Novvoy universal"),types.KeyboardButton(text="Qassob")],
            [types.KeyboardButton(text="Novvoy yordamchisi"),types.KeyboardButton(text="Sotuvchi")],
            [types.KeyboardButton(text="Sotuvchi-kassir"),types.KeyboardButton(text="Avtoturargoh nazoratchisi")],
            [types.KeyboardButton(text="Do'kon menejerining o'rinbosari"),types.KeyboardButton(text="Qo'riqchi")],
            [types.KeyboardButton(text="Do'kon menejeri (do'kon ish boshqaruvchisi)")],
            [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer("Qaysi lavozimda ishlamoqchisiz?", reply_markup=keyboard)
        print(user_data)


chosedposition =["Yuk tashuvchi","Tozalik xodimi","Oshpaz","Kassir",
                 "Novvoy universal","Qassob","Novvoy yordamchisi","Sotuvchi",
                 "Sotuvchi-kassir","Avtoturargoh nazoratchisi","Do'kon menejerining o'rinbosari","Qo'riqchi",
                 "Do'kon menejeri (do'kon ish boshqaruvchisi)"]

async def free_position(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["choosed_position"] = message.text
    if message.text in chosedposition:
        button = [
            [types.KeyboardButton(text="🛒 Sofia"),types.KeyboardButton(text="🛒 Yunusobod")],
            [types.KeyboardButton(text="🛒 Sayram")],
            [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer("Lavozim vazifalari:\n"
                             "• Kassada to'lovlarni qabul qilish va mijozlarning hisob-kitoblarini amalga oshirish;\n"
                             "• Narxlar va aksiyalar bo‘yicha xaridorlarga maslahat berish;\n"
                             "• Kassa joyini tozalikda saqlash.\n\n"
                             "Talablar:\n"
                             "• Yoshi: 18 yoshdan;\n"
                             "• Diqqatlilik, mijozga yo‘naltirilganlik, stressga chidamlilik;\n"
                             "• Hisoblash qobiliyatlari.\n\n"
                             "Ish sharoitlari:\n"
                             "• Tanish-bilishsiz ishga olamiz;\n"
                             "• Mehnat kodeksi bo’yicha ishga qabul qilamiz;\n"
                             "• O’z vaqtida oylik maoshini to’laymiz; \n"
                             "• Tajribasiz bo’lsangiz ham ishga qabul qilamiz va o’zimiz o’rgatamiz;\n"
                             "• Ovqat bilan taminlaymiz;\n"
                             "• OTMlar kontraktini to’lab beramiz.\n", reply_markup=keyboard)
        print(user_data)


filial_dict = {"🛒 Sofia":["📌 Manzil: Adham rahmata, 14a\n\n 🔎 Mo'ljal: “Fleshka” savdo markazi qatori.",41.341398,69.268690],
               "🛒 Yunusobod":["📌 Manzil: Yunusobod 7, st. Quloqtepa.\n\n🔎 Mo'ljal: Zenit zavodi",41.373207,69.272817],
               "🛒 Sayram":["📌Manzil: Yunusobod tumani, 19-kvartal, ko'cha. Yunus ota 15.\n\n🔎 Mo'ljal: eskiSayram bozori.",41.373119,69.311069],
               }


async def filial(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["korzinka_toshkent"] = message.text
    manzil = filial_dict[message.text][0]
    long = filial_dict[message.text][1]
    lat = filial_dict[message.text][2]
    if message.text in filial_dict:
        button = [
            [types.KeyboardButton(text="Bosh sahifa"),types.KeyboardButton(text="Orqaga")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer(f"{manzil}",reply_markup=keyboard)
        await bot.send_location(chat_id=message.from_user.id,
                                longitude=long,
                                latitude=lat)
        await message.answer("Pasportdagi Familiya, Ism va Sharifini kiriting")
        print(user_data)


async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())

