from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BRON_CHANNEL = "-1001584257840"
token = '5397545346:AAHMF4YVKC8qAu479WjdVl2Ef1m2y2-tn04'
storage = MemoryStorage()
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

