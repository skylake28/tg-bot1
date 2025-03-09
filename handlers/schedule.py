import asyncio
from aiogram import types, Router
from aiogram.filters import Command

router = Router()
scheduled_messages = {}

@router.message(Command("schedule"))
async def schedule_announcement(message: types.Message):
    args = message.text.split(" ", 2)
    if len(args) < 3:
        await message.reply("Usage: /schedule time_in_seconds message", parse_mode="HTML")
        return
    delay = int(args[1])
    scheduled_messages[message.chat.id] = (args[2], asyncio.get_event_loop().time() + delay)
    await message.reply(f"✅ Announcement scheduled in {delay} seconds.", parse_mode="HTML")

def register_handlers(dp):
    dp.include_router(router)
