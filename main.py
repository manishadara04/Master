import os
from pyrogram import Client as bot, idle
import asyncio
import logging
from flask import Flask, jsonify
from config import Config  # Import Config class here

app = Flask(__name__)
app.config.from_object(Config)  # Apply the config to the app

@app.route('/')
def home():
    return "Hello, World!"

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")

plugins = dict(root="plugins")
bot_instance = bot(
    "Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=120,
    plugins=plugins,
    workers=10,
)

async def main():

        await bot.start()

        bot_info = await bot.get_me()

        LOGGER.info(f"<--- @{bot_info.username} Started --->")

        for user_id in Config.AUTH_USERS:

            try:

                await bot.send_message(chat_id=user_id, text=f"__Congrats! You Are DRM member ... if You get any error then contact me -  {Config.CREDIT}__ ")

            except Exception as e:

                LOGGER.error(f"Failed to send message to user {user_id}: {e}")

                continue

        await idle()

    asyncio.get_event_loop().run_until_complete(main())

    LOGGER.info("<---🦅 Stopped 💞 --->")

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(start_bot())
    loop.run_forever()

if __name__ == '__main__':
    # Run Flask app and bot in parallel
    from multiprocessing import Process

    bot_process = Process(target=run_bot)
    bot_process.start()

    app.run(host='0.0.0.0', port=8080, debug=False)
    bot_process.join()
