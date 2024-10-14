import asyncio
from app.dispatcher import dp
from app.bot import bot
from aiogram.methods.delete_webhook import DeleteWebhook

    
async def start_bot():
    await bot(DeleteWebhook(drop_pending_updates=True))                     # Пропускаем все предыдущие события
    await dp.start_polling(bot)                                             # Запуск полинга


def main():
    asyncio.run(start_bot())                                               # Запускаем бота
    

if __name__ == "__main__":
    main()
