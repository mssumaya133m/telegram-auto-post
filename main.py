from pyrogram import Client, filters

API_ID = 33580169
API_HASH = "335b12d8c477f473e515622ae2b02a00"
BOT_TOKEN = "8611793461:AAGlFikLgvHfp04e5ohOBA07mWzaj-_bNSI"

SOURCE_CHAT = "@Getmodpcs"
TARGET_CHAT = "@TC_MAHADI_VIP"

app = Client(
    "auto_post_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.chat(SOURCE_CHAT))
async def auto_forward(client, message):
    try:
        if message.text or message.caption:
            original_text = message.text or message.caption
            
            modified_text = original_text.replace("Getmodpcs", "TC_MAHADI_VIP")
            modified_text = modified_text.replace("https://t.me/Getmodpcs", "https://t.me/TC_MAHADI_VIP")
            
            if message.media:
                await message.copy(
                    chat_id=TARGET_CHAT,
                    caption=modified_text
                )
            else:
                await client.send_message(
                    chat_id=TARGET_CHAT,
                    text=modified_text
                )
        else:
            await message.copy(chat_id=TARGET_CHAT)
            
        print("পোস্ট সফলভাবে আপনার চ্যানেলে পাঠানো হয়েছে!")

    except Exception as e:
        print(f"ত্রুটি ঘটেছে: {e}")

if __name__ == "__main__":
    print("বট সক্রিয় রয়েছে এবং পোস্টের অপেক্ষায় আছে...")
    app.run()
