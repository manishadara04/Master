from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    # Get the port from the environment variable or use 8000 by default
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
