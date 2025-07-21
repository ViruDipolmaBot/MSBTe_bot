from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
import json
from django.conf import settings
from .models import Syllabus, QuestionPaper
#from telegram import Update, Bot
#from telegram.ext import Dispatcher, CommandHandler

bot = Bot(token="7979851577:AAHgyi8zQ46zQt-CRSo_WRQEdCdvlP520rs")

def start(update, context):
    update.message.reply_text("👋 Hi! I am MSBTE Bot.\nCommands:\n/syllabus <subject>\n/paper <subject> <year>")

def syllabus(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Please send subject name. Example: /syllabus M3")
        return
    subject = " ".join(context.args)
    qs = Syllabus.objects.filter(subject_name__icontains=subject)
    if qs.exists():
        for s in qs:
            bot.send_document(chat_id=update.effective_chat.id, document=s.pdf)
    else:
        update.message.reply_text("❌ Syllabus not found.")

def paper(update, context):
    if len(context.args) < 1:
        update.message.reply_text("Please send subject name. Example: /paper M3")
        return
    subject = context.args[0]
    qs = QuestionPaper.objects.filter(subject_name__icontains=subject)
    if qs.exists():
        for p in qs:
            bot.send_document(chat_id=update.effective_chat.id, document=p.pdf)
    else:
        update.message.reply_text("❌ Papers not found.")

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        update = Update.de_json(data, bot)
        dp = Dispatcher(bot, None, workers=0)
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("syllabus", syllabus))
        dp.add_handler(CommandHandler("paper", paper))
        dp.process_update(update)
        return JsonResponse({"status": "ok"})
    else:
        return HttpResponseForbidden()
