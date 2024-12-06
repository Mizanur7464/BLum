# BLUM Mini App

A Telegram Mini App for gaming and crypto farming.

## Project Structure
```
BLUM--main/
├── bot/              # Telegram bot files
│   ├── bot.py       # Bot main script
│   ├── .env         # Environment variables
│   └── requirements.txt
│
├── web/             # Web app files
│   ├── index.html   # Main HTML file
│   ├── styles.css   # Global styles
│   ├── script.js    # Main JavaScript
│   ├── earn/        # Earn feature
│   ├── friends/     # Friends feature
│   ├── memepad/     # Memepad feature
│   └── wallet/      # Wallet feature
```

## Setup Instructions

1. **Bot Setup**:
   ```bash
   cd bot
   pip install -r requirements.txt
   python bot.py
   ```

2. **Web Setup**:
   - Host the web directory on a web server
   - Update WEB_APP_URL in bot.py with your hosted URL

3. **Environment Variables**:
   - Create .env file in bot directory
   - Add your BOT_TOKEN from @BotFather

## Features
- Drop Game
- Crypto Farming
- Friend System
- Wallet Management
- Memepad Integration 