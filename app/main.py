from aiogram import Bot, Dispatcher, executor
from app.config import load_config
from app.bot.handlers import register_handlers

# Загрузка конфигурации
config = load_config()

# Создание бота и диспетчера
bot = Bot(token=config.TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

# Регистрация обработчиков
register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
