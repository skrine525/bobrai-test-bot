from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


router = Router()   # Роутер

# Константы сообщений
HELLO_MESSAGE_TEXT = "Привет! Я бот, который подскажет тебе погоду в любом городе мира!\n\nНапиши название города!"


# Команда /start
@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    
    await message.answer(text=HELLO_MESSAGE_TEXT)