import aiogram
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
import asyncio
from lists import sets

TOKEN = "7702041998:AAGYq7SjeufGnJQ4OFAr2zrzqVP7VyD6nCM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Bu yerda `dp` obyektini yaratdik

user_data = {}


@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start":
        await start(message)
    elif message.text == "🇺🇿 O'zbekcha":
        await asosiymenu(message)
    elif message.text == "🇺🇸 English":
        await main_menu(message)
    elif message.text == "🍱 Setlar":
        await setlar(message)
    elif message.text in sets:
        await choosen_item(message)
    elif message.text == "📥 Savat":
        await show_cart(message)




@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
         types.KeyboardButton(text="🇺🇸 English")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n\n"
        "Здравствуйте! Добро пожаловать в службу доставки Les Ailes.\n\n"
        "Hello! Welcome to Les Ailes delivery service.",
        reply_markup=keyboard)
    print(1, user_data)


@dp.message(Command("🇺🇿 O'zbekcha"))
async def asosiymenu(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="↩️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="🍱 Setlar"), types.KeyboardButton(text="🍗 Tovuq")],
        [types.KeyboardButton(text="🍟 Sneklar"), types.KeyboardButton(text="🌯 Lesterlar")],
        [types.KeyboardButton(text="🍔 Burgerlar"), types.KeyboardButton(text="🌭 Longerlar/Hot-dog")],
        [types.KeyboardButton(text="🥤 Ichimliklar"), types.KeyboardButton(text="🥗 Salatlar")],
        [types.KeyboardButton(text="🍩 Ponchiklar"), types.KeyboardButton(text="👶 Bolajonlarga")],
        [types.KeyboardButton(text="🍅 Souslar")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)


@dp.message(Command("🇺🇸 English"))
async def main_menu(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="↩️ back"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="🍱 Sets"), types.KeyboardButton(text="🍗 Chickens")],
        [types.KeyboardButton(text="🍟 Sneks"), types.KeyboardButton(text="🌯 Lesters")],
        [types.KeyboardButton(text="🍔 Burgerlars"), types.KeyboardButton(text="🌭 Longers/Hot-dog's")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("how do we start ?", reply_markup=keyboard)



@dp.message(Command("🍱 Setlar"))
async def setlar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "Setlar"
    button = [
        [types.KeyboardButton(text="↪️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Kombo set"), types.KeyboardButton(text="1+1 Barbekyu burger")],
        [types.KeyboardButton(text="1+1 Sezar burger"), types.KeyboardButton(text="Yangi set")],
        [types.KeyboardButton(text="Klassik set"), types.KeyboardButton(text="Skulll set")],
        [types.KeyboardButton(text="Do'stlar 1x"), types.KeyboardButton(text="Do'stlar 1x, achchiq")],
        [types.KeyboardButton(text="Qiyqiriq set"), types.KeyboardButton(text="Longer rings set")],
        [types.KeyboardButton(text="Lester set"), types.KeyboardButton(text="Big set")],
        [types.KeyboardButton(text="Snek set"), types.KeyboardButton(text="Do'stlar 2x")],
        [types.KeyboardButton(text="Do'stlar 2x, achchiq"), types.KeyboardButton(text="4 Friends Hot-dog")],
        [types.KeyboardButton(text="4 Friends Klassik burger"), types.KeyboardButton(text="4 Friends Longer chiz")],
        [types.KeyboardButton(text="4 Friends Lester chiz"), types.KeyboardButton(text="Do'stlar 4x")],
        [types.KeyboardButton(text="Do'stlar 4x, achchiq")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)
    print(user_data)




async def choosen_item(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = message.text
    # user_data[user_id]["name"] = message.text
    sms = message.text
    button = [
                [types.InlineKeyboardButton(text=f"-", callback_data=f"minus_{sms}"),
                 types.InlineKeyboardButton(text=f"1", callback_data=f"miqdor_{sms}"),
                 types.InlineKeyboardButton(text=f"+", callback_data=f"plus_{sms}"), ],
                [types.InlineKeyboardButton(text=f"📥Savatga qo'shish✅", callback_data=f"add_{sms}"), ],
            ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    if sms in sets:
        file_path = sets[sms]   #["Fri kartoshkasiCoca-cola 0.5",55000,"images/komboset.jpg"]
        file_path = file_path[2]
        name = f"{sms}\n{sets[sms][0]}"
        user_data[user_id]["name"] = name
        price = sets[sms][1]
        caption_text = f"Nomi: {name}\nNarxi: {price} so'm"

        user_data[user_id]["price"] = price
        await message.answer(f"Miqdorini belgilang")

        await message.reply_photo(
            caption=caption_text,
            photo=types.FSInputFile(path=file_path),
            parse_mode="Markdown",
            reply_markup=keyboard
        )
        user_data[user_id]["count"] = 1


# button = [
#                 [types.InlineKeyboardButton(text=f"-", callback_data=f"minus_{sms}"),
#                  types.InlineKeyboardButton(text=f"1", callback_data=f"miqdor_{sms}"),
#                  types.InlineKeyboardButton(text=f"+", callback_data=f"plus_{sms}"), ],
#                 [types.InlineKeyboardButton(text=f"📥Savatga qo'shish✅", callback_data=f"add_{sms}"), ],]
#
#             qolgan funkisyalarda ham callback_data ni oxiriga minus_{sms};miqdor_{sms};plus_{sms}; shunaqa yozilsa bularning xammasi
#             check_item funksiyasiga kelib tekshiriladi bu degani bosh check_item funksiyasini yozishga xojat yoq


@dp.callback_query(lambda c: c.data.startswith(('plus', 'minus', 'add')))
async def check_item(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    command,item_name = callback.data.split("_")
    user_data[user_id]['item_name'] = item_name
    print(1,command)
    print(2,item_name)
    count = user_data[user_id]["count"]
    price = user_data[user_id]["price"]
    if command == 'plus':
        count += 1
    elif command == 'minus':
        if count > 1:
            count -= 1
    elif command == 'add':
        if 'basket' not in user_data[user_id]:
            user_data[user_id]['basket'] = {item_name: count}
        else:
            if item_name in user_data[user_id]['basket']:
                user_data[user_id]['basket'][item_name] += count
            else:
                user_data[user_id]['basket'][item_name] = count
        print(f"nomi:soni --> {user_data[user_id]['basket']}")
        await callback.message.answer(f"Mahsulot: {item_name} savatga muvaffaqiyatli qo'shildi ✅\n"
                                      "Davom etamizmi?")
    button = [
        [types.InlineKeyboardButton(text=f"-", callback_data=f"minus_{item_name}"),
         types.InlineKeyboardButton(text=f"{count}", callback_data=f"miqdor_{item_name}"),
         types.InlineKeyboardButton(text=f"+", callback_data=f"plus_{item_name}"), ],
        [types.InlineKeyboardButton(text=f"📥Savatga qo'shish✅", callback_data=f"add_{item_name}"), ],
    ]
    price *= count
    user_data[user_id]["price"] = price
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    try:
        name = user_data[user_id]["name"]
        await callback.message.edit_caption(
            caption=f"Nomi: {name}\n"
                    f"Narxi: {price} so'm",
            reply_markup=keyboard
        )

    except aiogram.exceptions.TelegramBadRequest as e:
        if "message is not modified" in str(e):
            print("Xabar o'zgarmaganligi sababli yangilash o'tkazib yuborildi.")
        else:
            print(f"Xato yuz berdi: {e}")
    print(user_data)


@dp.message(Command("📥 Savat"))
async def show_cart(message: types.Message):
    user_id = message.from_user.id
    if "basket" in user_data[user_id] and user_data[user_id]["basket"]:
        nomi = user_data[user_id]["name"]
        narxi = user_data[user_id]["price"]
        button = [
            [types.InlineKeyboardButton(text=f"{nomi}", callback_data=f"text"),],
             [types.InlineKeyboardButton(text=f"{narxi}", callback_data=f"text"),],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
        await message.answer(f"Yana mahsulot qoshasizmi yoki tolov qismiga o'tasizmi?",reply_markup=keyboard)
    else:
        await message.answer("Savatingiz xali bo'sh")


async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())
