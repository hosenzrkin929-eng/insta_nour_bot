import telebot
from insta_insights import get_instagram_profile

# 🔑import telebot
from insta_insights import get_instagram_profile

# 🔑 ضع هنا التوكن الخاص ببوتك من BotFather
TOKEN = "ضع_هنا_التوكن_الخاص_بك"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً! أرسل لي اسم مستخدم إنستغرام وسأحلله لك 🔍")

@bot.message_handler(func=lambda m: True)
def analyze_instagram(message):
    username = message.text.strip().replace("@", "")
    data = get_instagram_profile(username)

    result = "\n".join([f"{k}: {v}" for k, v in data.items()])
    bot.reply_to(message, f"📊 النتائج:\n{result}")

print("✅ البوت جاهز للعمل...")
bot.infinity_polling() BotFather
TOKEN = "7997992845:AAE5Ui71zloLbfCPs0yTXIIaJpwnvfy7n-c"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً! أرسل لي اسم مستخدم إنستغرام وسأحلله لك 🔍")

@bot.message_handler(func=lambda m: True)
def analyze_instagram(message):
    username = message.text.strip().replace("@", "")
    data = get_instagram_profile(username)

    result = "\n".join([f"{k}: {v}" for k, v in data.items()])
    bot.reply_to(message, f"📊 النتائج:\n{result}")

print("✅ البوت جاهز للعمل...")
bot.infinity_polling()
