from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

BOT_TOKEN = os.getenv('BOT_TOKEN')
# Replace with your GitHub Pages URL
# Example: https://your-username.github.io
# Or: https://your-username.github.io/repository-name
WEB_APP_URL = os.getenv('WEB_APP_URL', 'https://mizanur7464.github.io/BLum/')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message with a button that opens the web app."""
    await update.message.reply_text(
        "Welcome to Blum Mini App! Click the button below to start:",
        reply_markup={
            "inline_keyboard": [[{
                "text": "Open Blum App",
                "web_app": {"url": WEB_APP_URL}
            }]]
        }
    )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main() 