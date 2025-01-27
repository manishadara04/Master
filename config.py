import os
class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
    API_ID = int(os.environ.get("API_ID", '27536109'))
    API_HASH = os.environ.get("API_HASH", 'b84d7d4dfa33904d36b85e1ead16bd63')
    AUTH_USER = os.environ.get('AUTH_USERS','6428531614').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    WEBHOOK = True  # Don't change this
    PORT = int(os.environ.get("PORT", '8080'))  # Default to 8000 if not set
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌"#Here You Can Change with Your Name  or any custom name or title you prefer

