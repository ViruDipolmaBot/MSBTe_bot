from telegram.ext import ApplicationBuilder, CommandHandler
import os, sys, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msbtebot.settings')
django.setup()

BOT_TOKEN = "7979851577:AAHgyi8zQ46zQt-CRSo_WRQEdCdvlP520rs"

# Handlers
async def start(update, context):
    await update.message.reply_text("👋 Hi! I am MSBTE Bot. Send /syllabus or /papers")

async def syllabus(update, context):
    await update.message.reply_text("📘 Here is your syllabus link...")

async def papers(update, context):
    await update.message.reply_text("📄 Here are previous question papers...")

# ✅ NO asyncio.run, just normal run_polling
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("syllabus", syllabus))
    app.add_handler(CommandHandler("papers", papers))
    print("🤖 Bot is running... Press Ctrl+C to stop.")
    app.run_polling()