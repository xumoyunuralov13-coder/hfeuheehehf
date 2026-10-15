
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8659764123:AAGC3DMEGyaNthulybwpT_zdE8YB7LRyjnY"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    text = (
        f"Assalomu alaykum, **{user_name}**! 🚀\n\n"
        "Men xavfsiz Trading Signallar botiman.\n"
        "Sizga **Binance (Kripto)**, **Valyutalar** va **Oltin (Gold)** bo'yicha eng aniq signallarni berib boraman.\n\n"
        "Hozircha bot test rejimida ishlayapti. Kerakli bo'limni tanlang:"
    )
    
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="🪙 Binance Signallari", callback_data="crypto")],
            [types.InlineKeyboardButton(text="💱 Valyuta Signallari", callback_data="forex")],
            [types.InlineKeyboardButton(text="🥇 Oltin (Gold) Signali", callback_data="gold")],
            [types.InlineKeyboardButton(text="⭐ VIP Obuna", callback_data="vip")]
        ]
    )
    
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

async def main():
    print("Bot ishga tushdi va buyruqlarni kutyapti...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

















































