from random import choice
from re import sub

from spongemock.spongemock import mock as mock_text
from telegram import Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from zalgo_text.zalgo import zalgo

from telebot import dispatcher, log


@run_async
def runs(update: Update, context: CallbackContext):
    log(update, "runs")
    update.effective_message.reply_markdown("I'm a cute kitty, and here we have a fat pussy.")
    update.effective_chat.send_sticker("CAACAgUAAxkBAAIJK19CjPoyyX9QwwHfNOZMnqww1hxXAALfAAPd6BozJDBFCIENpGkbBA")


@run_async
def mock(update: Update, context: CallbackContext):
    log(update, "mock")

    if update.effective_message.reply_to_message:
        update.effective_message.reply_to_message.reply_text(mock_text(update.effective_message.reply_to_message.text))
    else:
        update.effective_message.reply_text("I don't see anything to mock here other than your ugly face...")


@run_async
def zalgofy(update: Update, context: CallbackContext):
    log(update, "zalgofy")

    if update.effective_message.reply_to_message:
        update.effective_message.reply_to_message.reply_text(
            zalgo().zalgofy(update.effective_message.reply_to_message.text)
        )
    else:
        update.effective_message.reply_text("Gimme a message to zalgofy before I claw your tits off...")


faces = [
    "```\n(・`ω´・)\n```",
    "```\n;;w;;\n```",
    "```\nowo\n```",
    "```\nUwU\n```",
    "```\n>w<\n```",
    "```\n^w^\n```",
    "```\n" + r"\(^o\) (/o^)/" + "\n```",
    "```\n( ^ _ ^)∠☆\n```",
    "```\n(ô_ô)\n```",
    "```\n~:o\n```",
    "```\n;____;\n```",
    "```\n(*^*)\n```",
    "```\n(>_\n```",
    "```\n(♥_♥)\n```",
    "```\n*(^O^)*\n```",
    "```\n((+_+))\n```",
]


@run_async
def owo(update: Update, context: CallbackContext):
    log(update, "owo")

    if not update.effective_message.reply_to_message:
        update.effective_message.reply_text(
            "Gommenye, I don't nyaruhodo what normie text you want to henshin into the moe weeb dialect"
        )
        return

    try:
        reply_text = sub(r'[rl]', "w", update.effective_message.reply_to_message.text_markdown)
        reply_text = sub(r'[ｒｌ]', "ｗ", reply_text)
        reply_text = sub(r'[RL]', 'W', reply_text)
        reply_text = sub(r'[ＲＬ]', 'Ｗ', reply_text)
        reply_text = sub(r'n([aeiouａｅｉｏｕ])', r'ny\1', reply_text)
        reply_text = sub(r'ｎ([ａｅｉｏｕ])', r'ｎｙ\1', reply_text)
        reply_text = sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
        reply_text = sub(r'Ｎ([ａｅｉｏｕＡＥＩＯＵ])', r'Ｎｙ\1', reply_text)
        reply_text = sub(r'!+', ' ' + choice(faces), reply_text)
        reply_text = sub(r'！+', ' ' + choice(faces), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text = reply_text.replace("ｏｖｅ", "ｕｖ")
        reply_text += "\n" + choice(faces)

        update.effective_message.reply_to_message.reply_markdown(reply_text)

    except BadRequest:
        update.effective_message.reply_text(
            "Gommenye, I over-owo'd myself.... please try again. "
            "If it still doesn't work, then this must be the language of god's you're trying to translate...."
        )


__help__ = """
/mock <reply> : MoCk LikE sPOnGEbob
/zalgofy <reply> : cͩ͠o̴͕r͌̈ȓ͡ṵ̠p̟͜tͯ͞ t̷͂ḣ͞ȩ͗ t̪̉e̢̪x̨͑t̼ͨ
/owo <reply> : translate normie to moe weeb
"""

__mod_name__ = "memes"

dispatcher.add_handler(CommandHandler("runs", runs))
dispatcher.add_handler(CommandHandler("mock", mock))
dispatcher.add_handler(CommandHandler("zalgofy", zalgofy))
dispatcher.add_handler(CommandHandler("owo", owo))