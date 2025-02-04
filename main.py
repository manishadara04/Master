import os
from pyrogram import Client as bot, idle
import asyncio
import logging
from flask import Flask, jsonify
from config import Config  # Import Config class here

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Apply the config to the app

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/start', methods=['GET'])
def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())
    return jsonify({"status": "Bot Started"})

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

async def run_bot():
    await bot_instance.start()
    bot_info = await bot_instance.get_me()
    LOGGER.info(f"<--- @{bot_info.username} Started --->")
    for user_id in Config.AUTH_USERS:
        try:
            await bot_instance.send_message(chat_id=user_id, text=f"__Congrats! You Are DRM member ... if You get any error then contact me -  {Config.CREDIT}__ ")
        except Exception as e:
            LOGGER.error(f"Failed to send message to user {user_id}: {e}")
            continue
    await idle()

def run_flask():
    app.run(host='0.0.0.0', port=5001, debug=False)  # Use a different port, e.g., 5001

if __name__ == '__main__':
    # Run Flask app and bot in parallel
    from multiprocessing import Process

    flask_process = Process(target=run_flask)
    flask_process.start()

    bot_process = Process(target=asyncio.run, args=(run_bot(),))
    bot_process.start()

    flask_process.join()
    bot_process.join()
