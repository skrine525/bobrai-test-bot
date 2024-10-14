from aiogram import Dispatcher
from app.routers.start_command import router as start_command_router


dp = Dispatcher()                       # Диспетчер


# Добавляем роутеры в диспетчер
dp.include_router(start_command_router)