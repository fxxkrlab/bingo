from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode
from uuid import uuid4

def article(
    title="", description="", message_text="", thumb_url=None, reply_markup=None
):
    return InlineQueryResultArticle(
        id=uuid4(),
        title=title,
        description=description,
        thumb_url=thumb_url,
        input_message_content=InputTextMessageContent(
            message_text=message_text,parse_mode=ParseMode.HTML,disable_web_page_preview=False
        ),
        reply_markup=reply_markup,
    )