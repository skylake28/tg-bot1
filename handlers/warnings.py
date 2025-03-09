from aiogram import types, Router

router = Router()
banned_words = ["spamword1", "spamword2"]
warnings = {}

@router.message()
async def check_bad_words(message: types.Message):
    if message.text is None:
        return
    user_id = message.from_user.id
    for word in banned_words:
        if word in message.text.lower():
            warnings[user_id] = warnings.get(user_id, 0) + 1
            await message.reply(f"⚠️ Warning {warnings[user_id]}/3: Please avoid using banned words!", parse_mode="HTML")
            break

def register_handlers(dp):
    dp.include_router(router)
