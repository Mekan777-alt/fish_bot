from config import dp
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from app import btnMenu, btnbar, btnTime, btnBrn
btnkitchen = "🍱 ХОЛОДНЫЕ ЗАКУСКИ"
btndes = "🍮 ДЕСЕРТЫ"
btnkaptil = "🦐 ГОРЯЧИЕ ЗАКУСКИ И КОПТИЛЬНЯ"
btnmors = "🦀 МОРСКИЕ ГАДЫ И КРАБ"
btnpasta = "🍝 ПАСТА, РИЗОТТО И ВОК"
btnbzn = "🥗 САЛАТЫ"
btnsup = "🍲 СУПЫ"
btngor = "🥙 ОСНОВНЫЕ ГОРЯЧИЕ БЛЮДА"
btnsous = "🍽 ГАРНИРЫ"
btnnaz = "🔙 НАЗАД"


@dp.message_handler(text=btnMenu)
async def cmd_menu(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("ВЫБЕРИТЕ РАЗДЕЛ", reply_markup=markup)


@dp.message_handler(text=btnkitchen)
async def btn_kitchen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-09-2", reply_markup=markup)


@dp.message_handler(text=btnmors)
async def btn_kitchen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-10-3", reply_markup=markup)

@dp.message_handler(text=btnbzn)
async def btn_bzn(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-10-8", reply_markup=markup)


@dp.message_handler(text=btnkaptil)
async def btn_gril(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-14-5", reply_markup=markup)


@dp.message_handler(text=btngor)
async def btn_gor(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-14-6", reply_markup=markup)


@dp.message_handler(text=btnsup)
async def btn_sup(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-10-4", reply_markup=markup)


@dp.message_handler(text=btnpasta)
async def btn_kids(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-10-5", reply_markup=markup)


@dp.message_handler(text=btnsous)
async def btn_sous(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-10-7", reply_markup=markup)


@dp.message_handler(text=btndes)
async def btn_des(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnkaptil, btnbzn).add(btngor, btnsup, btnmors).add(btnpasta, btnsous, btndes).add(btnnaz)
    await message.answer("https://telegra.ph/MENYU-05-10-10", reply_markup=markup)


@dp.message_handler(text=btnnaz)
async def btn_naz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnMenu, btnbar, btnTime).add(btnBrn)
    await message.answer("ПЕРЕХОД НА ГЛАВНОЕ МЕНЮ", reply_markup=markup)
