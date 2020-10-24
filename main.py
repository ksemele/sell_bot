from config import TOKEN, ADMIN_ID
import logging
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp, ft_send_to_admin

    executor.start_polling(dp, on_startup=ft_send_to_admin)