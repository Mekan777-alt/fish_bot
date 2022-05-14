from config import dp, bot
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from .menu import btnnaz
from app import btnbar
btnvin_po_bakal = "🍾 АПЕРЕТИВ"
btnvin_bel = "🥂 БЕЛЫЕ ВИНА"
btnvin_kras = "🍷 КРАСНЫЕ ВИНА"
btnviski = "🥃 ВИСКИ, РОМ, КОНЬЯК"
btnvodka = "🍸 ВОДКА, ДЖИН, ТЕКИЛА"
#btnpivo = "🍺 ПИВО"
btnbez = "☕ БЕЗ АЛКОГОЛЬНЫЕ НАПИТКИ"


@dp.message_handler(text=btnbar)
async def catalog(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnvin_po_bakal, btnvin_bel, btnvin_kras).add(btnviski, btnvodka, btnbez).add(btnnaz)
    await message.answer("ВЫБЕРИТЕ РАЗДЕЛ", reply_markup=markup)


@dp.message_handler(text=btnvin_po_bakal)
async def btnvin_pobok(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnvin_po_bakal, btnvin_bel, btnvin_kras).add(btnviski, btnvodka, btnbez).add(btnnaz)
    await message.answer("https://telegra.ph/BAR-05-10-2", reply_markup=markup)


@dp.message_handler(text=btnvin_bel)
async def btn_bel(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnvin_po_bakal, btnvin_bel, btnvin_kras).add(btnviski, btnvodka, btnbez).add(btnnaz)
    await message.answer("https://telegra.ph/BAR-05-10-3", reply_markup=markup)


@dp.message_handler(text=btnvin_kras)
async def btn_kras(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnvin_po_bakal, btnvin_bel, btnvin_kras).add(btnviski, btnvodka, btnbez).add(btnnaz)
    await message.answer("https://telegra.ph/BAR-05-10-4", reply_markup=markup)


@dp.message_handler(text=btnviski)
async def btn_viski(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnvin_po_bakal, btnvin_bel, btnvin_kras).add(btnviski, btnvodka, btnbez).add(btnnaz)
    await message.answer("https://telegra.ph/Bar-05-11", reply_markup=markup)


@dp.message_handler(text=btnvodka)
async def btn_vodka(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnvin_po_bakal, btnvin_bel, btnvin_kras).add(btnviski, btnvodka, btnbez).add(btnnaz)
    await message.answer("https://telegra.ph/BAR-05-13-2", reply_markup=markup)


@dp.message_handler(text=btnbez)
async def btn_bez(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnvin_po_bakal, btnvin_bel, btnvin_kras).add(btnviski, btnvodka, btnbez).add(btnnaz)
    await message.answer("https://telegra.ph/BAR-05-13-3", reply_markup=markup)
