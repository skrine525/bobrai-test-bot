from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()   # Роутер


# Команда /start
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=f"👋 Привет, {message.from_user.first_name}!\n\n🤖 Я бот, который подскажет вам погоду в любом городе мира!\n\n🏙 Напиши название города.")