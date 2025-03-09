import asyncio
import os
from aiogram import Bot, Dispatcher
from keep_alive import keep_alive
from handlers import auto_replies, welcome, warnings, schedule, moderation

# Get BOT TOKEN from environment variables
TOKEN = os.getenv("BOT_TOKEN")

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Register handlers
auto_replies.register_handlers(dp)
welcome.register_handlers(dp)
warnings.register_handlers(dp)
schedule.register_handlers(dp)
moderation.register_handlers(dp)

async def main():
    keep_alive()  # Keep bot alive
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
