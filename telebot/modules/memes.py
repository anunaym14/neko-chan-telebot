from asyncio import new_event_loop
from io import BytesIO
from os import remove
from pathlib import Path
from random import choice
from random import choice, randint
from re import sub

from PIL import Image
from deeppyer import deepfry
from emoji import emojize
from spongemock.spongemock import mock as mock_text
from telegram import Update, Message
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from zalgo_text.zalgo import zalgo

from telebot import dispatcher, log


@run_async
def runs(update: Update, context: CallbackContext) -> None:
    """
    Insulting reply whenever someone uses /runs
    :param update: object representing the incoming update.
    :param context: object containing data about the command call.
    """
    log(update, "runs")
    update.effective_message.reply_markdown("I'm a cute kitty, and here we have a fat pussy.")
    update.effective_chat.send_sticker("CAACAgUAAxkBAAIJK19CjPoyyX9QwwHfNOZMnqww1hxXAALfAAPd6BozJDBFCIENpGkbBA")


@run_async
def mock(update: Update, context: CallbackContext) -> None:
    """
    Mock a message like spongebob, and reply
    :param update: object representing the incoming update.
    :param context: object containing data about the command call.
    """
    log(update, "mock")

    if update.effective_message.reply_to_message:
        update.effective_message.reply_to_message.reply_text(mock_text(update.effective_message.reply_to_message.text))
    else:
        update.effective_message.reply_text("I don't see anything to mock here other than your ugly face...")


@run_async
def zalgofy(update: Update, context: CallbackContext) -> None:
    """
    Corrupt the way the text looks, and reply
    :param update: object representing the incoming update.
    :param context: object containing data about the command call.
    """
    log(update, "zalgofy")

    if update.effective_message.reply_to_message:
        update.effective_message.reply_to_message.reply_text(
            zalgo().zalgofy(update.effective_message.reply_to_message.text)
        )
    else:
        update.effective_message.reply_text("Gimme a message to zalgofy before I claw your tits off...")


@run_async
def owo(update: Update, context: CallbackContext) -> None:
    """
    Change a message to look like it was said by a moe weeb
    :param update: object representing the incoming update.
    :param context: object containing data about the command call.
    """
    log(update, "owo")

    if not update.effective_message.reply_to_message:
        update.effective_message.reply_text(
            "Gommenye, I don't nyaruhodo what normie text you want to henshin into the moe weeb dialect"
        )
        return

    # list of all kaomojis to use in owo
    kaomoji = [
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

    try:
        # replace certain characters and add a kaomoji
        reply_text = sub(r'[rl]', "w", update.effective_message.reply_to_message.text_markdown)
        reply_text = sub(r'[ｒｌ]', "ｗ", reply_text)
        reply_text = sub(r'[RL]', 'W', reply_text)
        reply_text = sub(r'[ＲＬ]', 'Ｗ', reply_text)
        reply_text = sub(r'n([aeiouａｅｉｏｕ])', r'ny\1', reply_text)
        reply_text = sub(r'ｎ([ａｅｉｏｕ])', r'ｎｙ\1', reply_text)
        reply_text = sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
        reply_text = sub(r'Ｎ([ａｅｉｏｕＡＥＩＯＵ])', r'Ｎｙ\1', reply_text)
        reply_text = sub(r'!+', ' ' + choice(kaomoji), reply_text)
        reply_text = sub(r'！+', ' ' + choice(kaomoji), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text = reply_text.replace("ｏｖｅ", "ｕｖ")
        reply_text += "\n" + choice(kaomoji)

        # reply to the original message
        update.effective_message.reply_to_message.reply_markdown(reply_text)

    except BadRequest:
        # in case we messed up markdown while replacing characters and adding kaomoji
        update.effective_message.reply_text(
            "Gommenye, I over-owo'd myself.... please try again. "
            "If it still doesn't work, then this must be the language of god's you're trying to translate...."
        )


@run_async
def stretch(update: Update, context: CallbackContext):
    """
    Stretch the vowels in a message by a random count
    :param update: object representing the incoming update.
    :param context: object containing data about the command call.
    """
    log(update, "stretch")

    if not update.effective_message.reply_to_message:
        update.effective_message.reply_text(
            "If you're not gonna give me a message to meme, at least give me some catnip..."
        )

    else:
        update.effective_message.reply_to_message.reply_markdown(
            sub(
                r'([aeiouAEIOUａｅｉｏｕＡＥＩＯＵ])',
                (r'\1' * randint(3, 10)),
                update.effective_message.reply_to_message.text_markdown,
            )
        )


@run_async
def vapor(update: Update, context: CallbackContext):
    """
    Make a message look more ａｅｓｔｈｅｔｉｃ
    :param update: object representing the incoming update.
    :param context: object containing data about the command call.
    """
    log(update, "vapor")

    if not context.args and not (
        update.effective_message.reply_to_message and update.effective_message.reply_to_message.text_markdown
    ):
        update.effective_message.reply_text(
            "If you're not gonna give me something to meme then bring some catnip atleast..."
        )
        return

    # get content to vaporwave
    if context.args:
        text = " ".join(context.args)
    else:
        text = update.effective_message.reply_to_message.text

    aesthetic_text = text.translate(dict((i, i + 0xFEE0) for i in range(0x21, 0x7F)))  # make text more ａｅｓｔｈｅｔｉｃ

    # reply with more ａｅｓｔｈｅｔｉｃｓ
    if context.args:
        update.effective_message.reply_markdown(f"`{aesthetic_text}`")
    else:
        update.effective_message.reply_to_message.reply_markdown(f"`{aesthetic_text}`")


async def _fry(image: Image, msg: Message):
    image = await deepfry(img=image)

    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')

    bio.seek(0)
    msg.reply_photo(bio)
    if Path("sticker.png").is_file():
        remove("sticker.png")


@run_async
def fry(update: Update, context: CallbackContext):
    log(update, "deepfry")

    if update.effective_message.reply_to_message and update.effective_message.reply_to_message.photo:
        image = Image.open(update.effective_message.reply_to_message.photo[-1].get_file().download_as_bytearray())
    elif update.effective_message.reply_to_message and update.effective_message.reply_to_message.sticker:
        context.bot.get_file(update.effective_message.reply_to_message.sticker.file_id).download('sticker.png')
        image = Image.open("sticker.png")
    else:
        update.effective_message.reply_text(
            emojize("Gimme something proper to deepfry before I deepfry your catnip :pouting_cat_face:")
        )
        return

    loop = new_event_loop()
    loop.run_until_complete(_fry(image, update.effective_message.reply_to_message))
    loop.close()


__help__ = """
- /mock `<reply>` : MoCk LikE sPOnGEbob
- /zalgofy `<reply>` : cͩ͠o̴͕r͌̈ȓ͡ṵ̠p̟͜tͯ͞ t̷͂ḣ͞ȩ͗ t̪̉e̢̪x̨͑t̼ͨ
- /owo `<reply>` : translate normie to moe weeb
- /stretch `<reply>` : talk like the sloth from zootopia
- /vapor `[<reply>|<message>]` : ｖａｐｏｒｗａｖｅ ａｅｓｔｈｅｔｉｃｓ
/mock <reply> : MoCk LikE sPOnGEbob
/zalgofy <reply> : cͩ͠o̴͕r͌̈ȓ͡ṵ̠p̟͜tͯ͞ t̷͂ḣ͞ȩ͗ t̪̉e̢̪x̨͑t̼ͨ
/owo <reply> : translate normie to moe weeb
/deepfry <reply photo|sticker> : deepfried memes for the american kitties
"""

__mod_name__ = "memes"

dispatcher.add_handler(CommandHandler("runs", runs))
dispatcher.add_handler(CommandHandler("mock", mock))
dispatcher.add_handler(CommandHandler("zalgofy", zalgofy))
dispatcher.add_handler(CommandHandler("owo", owo))
dispatcher.add_handler(CommandHandler("stretch", stretch))
dispatcher.add_handler(CommandHandler("vapor", vapor))
dispatcher.add_handler(CommandHandler("deepfry", fry))
