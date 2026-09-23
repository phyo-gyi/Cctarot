import logging
import os
from pathlib import Path

import telebot
from telebot.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Set these as environment variables in your hosting service.
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = "CelestialCards_bot"

# Keep these files in the same folder as app.py, or set custom paths.
BASE_DIR = Path(__file__).resolve().parent
COURSE_IMAGE_PATH = Path(
    os.getenv("COURSE_IMAGE_PATH", str(BASE_DIR / "Flyer.jpg"))
)
RITUAL_AUDIO_PATH = Path(
    os.getenv(
        "RITUAL_AUDIO_PATH",
        str(BASE_DIR / "5_6336721261627973220.ogg"),
    )
)

# Alternatively, a public URL can be used for the course flyer.
COURSE_IMAGE_URL = os.getenv("COURSE_IMAGE_URL", "").strip()

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable မရှိသေးပါ။")

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)


START_TEXT = (
    "✨ <b>Celestial Cards Tarot</b> မှ ကြိုဆိုပါတယ် ✨\n\n"
    "🔮 Tarot မေးမြန်းခြင်း၊ ယတြာနှင့် အစီရင်ဝန်ဆောင်မှုများကို ရယူနိုင်ပါပြီ။\n"
    "အောက်ပါ ခလုတ်များမှ မိမိသိရှိလိုသော ဝန်ဆောင်မှုကို ရွေးချယ်ပေးပါခင်ဗျာ။ 🙏"
)

TAROT_BUTTON_TEXT = "Tarot မေးရန်🔮"
COURSE_BUTTON_TEXT = "Tarot & Rituals သင်တန်းစုံစမ်းရန်🔮"
CONTACT_BUTTON_TEXT = "🍀ကျွန်တော်နှင့်တိုက်ရိုက်ဆက်သွယ်စကားပြောရန်🍀"
RITUAL_BUTTON_TEXT = "အစီရင်အပ်ခြင်းနဲ့ပတ်သတ်ပြီးစုံစမ်းရန်🔮"

TAROT_CALLBACK_DATA = "ask_tarot"
COURSE_CALLBACK_DATA = "ask_course"
CONTACT_CALLBACK_DATA = "contact_directly"
RITUAL_CALLBACK_DATA = "ask_ritual"


CONTACT_TEXT = (
    "🍀 <b>တိုက်ရိုက်ဆက်သွယ်ရန်</b> 🍀\n\n"
    "Telegram - @cctarot999\n"
    "Ph no - 09942244636\n"
    "Viber - 09942244636"
)


TAROT_TEXT = (
    "🔮 <b>Tarot (တားရော့) ဗေဒင်မေးမြန်းရန်</b>\n"
    "✨ <b>ယတြာနှင့် အစီရင်များ ယူရန်</b> ✨\n\n"
    "Tarot ဗေဒင်မေးမြန်းခြင်း၊ ယတြာနှင့် အစီရင်များယူခြင်းအတွက် "
    "<b>အဆင်ပြေသည့် မေတ္တာစေတနာကြေး</b> ဖြင့် ဆောင်ရွက်ပေးပါသည်။ "
    "မေတ္တာစေတနာကြေး မည်မျှပေးရမည်ကိုလည်း မိမိအဆင်ပြေသည့် ပမာဏအတိုင်း "
    "ပြောပြပေးနိုင်ပြီး မိမိအတွက် သင့်တော်အောင် စေတနာအပြည့်ဖြင့် "
    "ဆောင်ရွက်ပေးပါမည်။ 🙏\n\n"
    "လူတိုင်း လက်လှမ်းမီနိုင်စေရန်အတွက် သတ်မှတ်ဈေးနှုန်းမထားဘဲ "
    "<b>မေတ္တာစေတနာကြေးဖြင့်သာ</b> ဟောပြောပေးခြင်း ဖြစ်ပါသည်။ 💜\n\n"
    "ရရှိလာသော မေတ္တာစေတနာကြေးများထဲမှ တစ်စိတ်တစ်ပိုင်းကို "
    "လိုအပ်နေသူများနှင့် လူမှုကူညီရေးဂေဟာများသို့ ပြန်လည်လှူဒါန်းပေးသွားပါမည်။ 🤲\n\n"
    "📌 <b>ဟောကြားပေးရန်အတွက် မိမိ၏</b>\n"
    "👤 အမည်\n"
    "🎂 မွေးနေ့ / နေ့နံ\n"
    "📝 မိမိသိသော အချက်အလက်များ\n"
    "❓ သိလိုသော မေးခွန်းများ\n\n"
    "အထက်ပါအချက်အလက်များကို <b>@cctarot999</b> သို့ ပေးပို့ထားပေးပါခင်ဗျာ။ "
    "ဟောခန်းဝင်ရောက်သည့်အချိန်တွင် မေးမြန်းထားသမျှကို "
    "ပြန်လည်ဖြေကြားပေးပါမည်။ 🔮\n\n"
    "<b>#CelestialCardsTarot</b>\n\n"
    "🍀 <b>တိုက်ရိုက်ဆက်သွယ်ရန်</b> 🍀\n\n"
    "📱 Telegram - @cctarot999\n"
    "📞 Ph no - 09942244636\n"
    "💬 Viber - 09942244636\n\n"
    "🎵 TikTok 1 - @celestialcardstarot\n"
    "🎵 TikTok 2 - @celestialcardstarot9"
)


# Caption sent together with the Button 4 voice message.
RITUAL_AUDIO_CAPTION = (
    "🔮 အစီရင်အပ်ခြင်းနှင့် ပတ်သက်သော အသေးစိတ်အချက်အလက်များကို "
    "အသံဖိုင်တွင် နားထောင်နိုင်ပါတယ်။"
)


def start_keyboard() -> InlineKeyboardMarkup:
    """Create the welcome-menu keyboard."""
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            TAROT_BUTTON_TEXT,
            callback_data=TAROT_CALLBACK_DATA,
        ),
        InlineKeyboardButton(
            COURSE_BUTTON_TEXT,
            callback_data=COURSE_CALLBACK_DATA,
        ),
        InlineKeyboardButton(
            CONTACT_BUTTON_TEXT,
            callback_data=CONTACT_CALLBACK_DATA,
        ),
        InlineKeyboardButton(
            RITUAL_BUTTON_TEXT,
            callback_data=RITUAL_CALLBACK_DATA,
        ),
    )
    return markup


def send_image(
    chat_id: int,
    image_path: Path,
    image_url: str,
    caption: str,
    missing_message: str,
) -> None:
    """Send an image from a public URL or local file."""
    if image_url:
        bot.send_photo(chat_id, image_url, caption=caption, parse_mode="HTML")
        return

    if image_path.is_file():
        with image_path.open("rb") as image_file:
            bot.send_photo(chat_id, image_file, caption=caption, parse_mode="HTML")
        return

    logger.warning("Image was not found: %s", image_path)
    bot.send_message(chat_id, missing_message)


def send_course_image(chat_id: int) -> None:
    send_image(
        chat_id=chat_id,
        image_path=COURSE_IMAGE_PATH,
        image_url=COURSE_IMAGE_URL,
        caption=(
            "🔮 Tarot & Rituals သင်တန်းအကြောင်း အသေးစိတ်\n\n"
            "🎓✨ <b>သင်တန်းအပ်နှံရန် ဆက်သွယ်ရန်</b> ✨🎓\n\n"
            "📱 Telegram - @cctarot999\n"
            "📞 Ph no - 09942244636\n"
            "💬 Viber - 09942244636\n"
            "🎵 TikTok 1 - @celestialcardstarot\n"
            "🎵 TikTok 2 - @celestialcardstarot9"
        ),
        missing_message=(
            "သင်တန်း flyer ဖိုင် မတွေ့ပါ။ Flyer.jpg ကို app.py နဲ့အတူ ထည့်ပြီး ပြန် run ပေးပါ။"
        ),
    )


def send_ritual_audio(chat_id: int) -> None:
    """Send the supplied OGG file as a Telegram voice message."""
    if not RITUAL_AUDIO_PATH.is_file():
        logger.warning("Ritual audio was not found: %s", RITUAL_AUDIO_PATH)
        bot.send_message(
            chat_id,
            "အသံဖိုင် မတွေ့ပါ။ 5_6336721261627973220.ogg ကို app.py နဲ့အတူ ထည့်ပြီး ပြန် run ပေးပါ။",
        )
        return

    with RITUAL_AUDIO_PATH.open("rb") as audio_file:
        bot.send_voice(
            chat_id,
            audio_file,
            caption=RITUAL_AUDIO_CAPTION,
        )


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    """Show the welcome message and all four buttons."""
    bot.send_message(
        message.chat.id,
        START_TEXT,
        parse_mode="HTML",
        reply_markup=start_keyboard(),
    )


@bot.callback_query_handler(func=lambda call: call.data == TAROT_CALLBACK_DATA)
def tarot_button_clicked(call: CallbackQuery):
    """Reply with the Tarot service information when button 1 is pressed."""
    try:
        bot.answer_callback_query(call.id, "Tarot အချက်အလက်ကို ပို့ပေးနေပါတယ် 🔮")
        bot.send_message(
            call.message.chat.id,
            TAROT_TEXT,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    except Exception:
        logger.exception("Failed to send the Tarot information")
        bot.send_message(
            call.message.chat.id,
            "Tarot အချက်အလက်ပို့ရာတွင် အခက်အခဲရှိနေပါသည်။ ခဏအကြာတွင် ပြန်စမ်းပေးပါ။",
        )


@bot.callback_query_handler(func=lambda call: call.data == COURSE_CALLBACK_DATA)
def course_button_clicked(call: CallbackQuery):
    """Reply with the course flyer when button 2 is pressed."""
    try:
        bot.answer_callback_query(call.id, "သင်တန်းအချက်အလက်ကို ပို့ပေးနေပါတယ် 🔮")
        send_course_image(call.message.chat.id)
    except Exception:
        logger.exception("Failed to send the course flyer")
        bot.send_message(
            call.message.chat.id,
            "သင်တန်းဖိုင်ပို့ရာတွင် အခက်အခဲရှိနေပါသည်။ ခဏအကြာတွင် ပြန်စမ်းပေးပါ။",
        )


@bot.callback_query_handler(func=lambda call: call.data == CONTACT_CALLBACK_DATA)
def contact_button_clicked(call: CallbackQuery):
    """Reply with direct contact details when button 3 is pressed."""
    try:
        bot.answer_callback_query(call.id, "ဆက်သွယ်ရန်အချက်အလက်ကို ပို့ပေးနေပါတယ် 🍀")
        bot.send_message(
            call.message.chat.id,
            CONTACT_TEXT,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    except Exception:
        logger.exception("Failed to send contact details")
        bot.send_message(
            call.message.chat.id,
            "ဆက်သွယ်ရန်အချက်အလက် ပို့ရာတွင် အခက်အခဲရှိနေပါသည်။ ခဏအကြာတွင် ပြန်စမ်းပေးပါ။",
        )


@bot.callback_query_handler(func=lambda call: call.data == RITUAL_CALLBACK_DATA)
def ritual_button_clicked(call: CallbackQuery):
    """Reply with the ritual-enquiry voice file when button 4 is pressed."""
    try:
        bot.answer_callback_query(call.id, "အသံဖိုင်ကို ပို့ပေးနေပါတယ် 🔮")
        send_ritual_audio(call.message.chat.id)
    except Exception:
        logger.exception("Failed to send the ritual voice file")
        bot.send_message(
            call.message.chat.id,
            "အသံဖိုင်ပို့ရာတွင် အခက်အခဲရှိနေပါသည်။ ခဏအကြာတွင် ပြန်စမ်းပေးပါ။",
        )


@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    """Guide users back to the welcome menu for other private-chat messages."""
    if message.chat.type == "private":
        bot.send_message(
            message.chat.id,
            "အောက်က ခလုတ်တစ်ခုကို ရွေးချယ်ပေးပါ 🔮",
            reply_markup=start_keyboard(),
        )


if __name__ == "__main__":
    logger.info("%s is starting with long polling...", BOT_NAME)
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)
