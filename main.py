import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters

# Render-এর জন্য মিনিমাল ওয়েব সার্ভার
app_web = Flask(__name__)


@app_web.route("/")
def home():
  return "Bot is running live!"


def run_web():
  port = int(os.environ.get("PORT", 8080))
  app_web.run(host="0.0.0.0", port=port)


# টেলিগ্রাম বটের কনফিগারেশন
API_ID = 33580169
API_HASH = "335b12d8c477f473e515622ae2b02a00"
BOT_TOKEN = "8611793461:AAGlFikLgvHfp04e5ohOBA07mWzaj-_bNSI"

SOURCE_CHAT = "@Getmodpcs"
TARGET_CHAT = "@TC_MAHADI_VIP"

bot = Client(
    "auto_post_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)


@bot.on_message(filters.chat(SOURCE_CHAT))
async def auto_forward(client, message):
  try:
    if message.text or message.caption:
      original_text = message.text or message.caption

      modified_text = original_text.replace("Getmodpcs", "TC_MAHADI_VIP")
      modified_text = modified_text.replace(
          "https://t.me/Getmodpcs", "https://t.me/TC_MAHADI_VIP"
      )

      if message.media:
        await message.copy(chat_id=TARGET_CHAT, caption=modified_text)
      else:
        await client.send_message(chat_id=TARGET_CHAT, text=modified_text)
    else:
      await message.copy(chat_id=TARGET_CHAT)

    print("পোস্ট সফলভাবে আপনার চ্যানেলে পাঠানো হয়েছে!")

  except Exception as e:
    print(f"ত্রুটি ঘটেছে: {e}")


if __name__ == "__main__":
  # ব্যাকগ্রাউন্ডে ওয়েব সার্ভার চালু করা
  Thread(target=run_web).start()

  print("বট সক্রিয় রয়েছে এবং পোস্টের অপেক্ষায় আছে...")
  bot.run()
