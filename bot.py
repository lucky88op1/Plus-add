from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = 34964564          # apna api id
API_HASH = "8a97e889da92079dbf90c59cee767e5b"     # apna api hash
BOT_TOKEN = "8527111367:AAFi2LscCvNIExMbk2HpxsboHrciawNyByQ"   # apna bot token

app = Client(
    "plus_number_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# =========================
# TEXT MESSAGE HANDLER
# =========================
@app.on_message(filters.text & filters.private)
async def add_plus_text(client, message: Message):
    text = message.text.strip()

    # commas remove + split by space/newline
    numbers = text.replace(",", " ").split()

    result = []
    for number in numbers:
        number = number.strip()
        if number:
            if number.startswith("+"):
                result.append(number)
            else:
                result.append("+" + number)

    await message.reply_text("\n".join(result))


# =========================
# TXT FILE HANDLER
# =========================
@app.on_message(filters.document & filters.private)
async def add_plus_file(client, message: Message):

    if not message.document.file_name.endswith(".txt"):
        return await message.reply_text("❌ Sirf .txt file bhejo")

    file_path = await message.download()
    new_file = "output.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    numbers = content.replace(",", " ").split()

    with open(new_file, "w", encoding="utf-8") as f:
        for number in numbers:
            number = number.strip()
            if number:
                if number.startswith("+"):
                    f.write(number + "\n")
                else:
                    f.write("+" + number + "\n")

    await message.reply_document(new_file)

    os.remove(file_path)
    os.remove(new_file)


# =========================
print("Bot Running...")
app.run()