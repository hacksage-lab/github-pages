from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot token

# Links and static data
REGISTRATION_LINK = "https://example.com/register"  # Replace with your form link
PRIZES_INFO = """
🏆 **Prize Pool** 🏆
1st Place: $1000 + Trophy  
2nd Place: $500  
3rd Place: $250  
"""
SCHEDULE_INFO = """
📅 **Upcoming Matches**  
- May 25: Qualifiers Round 1  
- May 28: Quarterfinals  
- June 1: Grand Finals  
"""

# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to *EGC Helper Bot*!\n\n"
        "Available commands:\n"
        "/register - Sign up for the tournament\n"
        "/prizes - View prize details\n"
        "/schedule - Check match dates",
        parse_mode="Markdown",
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📝 Register here: {REGISTRATION_LINK}",
        disable_web_page_preview=True,
    )

async def prizes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PRIZES_INFO, parse_mode="Markdown")

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SCHEDULE_INFO, parse_mode="Markdown")

# Error Handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

# Main Setup
def main():
    app = Application.builder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("prizes", prizes))
    app.add_handler(CommandHandler("schedule", schedule))

    # Error Handler
    app.add_error_handler(error)

    # Start Polling
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
