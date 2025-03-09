from aiogram import types, Router
from aiogram.filters import Command

router = Router()
auto_replies = {"hello": "Hey there! How can I help you?"}

@router.message(Command("autoreply"))
async def set_auto_reply(message: types.Message):
    args = message.text.split(" ", 2)
    if len(args) < 3:
        await message.reply("Usage: /autoreply trigger response", parse_mode="HTML")
        return
    trigger, response = args[1], args[2]
    auto_replies[trigger.lower()] = response
    await message.reply(f"🤖 <b>Auto-Reply:</b>
<i>{response}</i>", parse_mode="HTML")

def register_handlers(dp):
    dp.include_router(router)
