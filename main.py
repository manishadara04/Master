from pyrogram import Client as bot, idle
import asyncio
import logging
from config import Config  # Import Config class here
from flask import Flask
import os
import sys

# Create Flask app
app = Flask(__name__)

# Define a simple route for testing
@app.route('/')
def home():
    return "Welcome to the production-ready Flask app!"

# Debug mode is only enabled when running locally
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
logging.basicConfig(
    level=logging.INFO,    
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")

plugins = dict(root="plugins")

if __name__ == "__main__":
    bot = bot(
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
        # Entry point
if __name__ == "__main__":
    asyncio.run(main())
