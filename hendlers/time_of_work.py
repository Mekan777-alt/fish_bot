from config import dp, bot
from aiogram import types
from app import btnTime


@dp.message_handler(text=btnTime)
async def time(message: types.Message):
    await bot.send_photo(message.from_user.id, types.InputFile("/Users/mekanmededov/Desktop/fish_bot/photo_2022-05-14 20.04.42.jpeg"))
    await message.answer("Рыбный ресторан европейской кухни\n"
                         "Завтраки с 11:00 до 15:00 каждый день\n"
                         "Скидка 15% с 11:00 до 17:00 по будням на основное меню\n"
                         "☎️ Тел: 226 80 80\n"
                         "\n"
                         "Ромэйн FISH\n"
                         "Татарстан, Казань, Кремлевская 9\n")
    await bot.send_location(message.from_user.id, latitude=55.795183, longitude=49.112349)
