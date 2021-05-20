from telegram import ParseMode

from app import searchMovie, searchTV
from app.modules import load, tmdb

# ### search workflow
def searchALL(update, context):
    entry_cmd = update.message.text
    entry_context = entry_cmd[7:].strip()
    mediainfo = {}
    media_list = []
    if entry_context.startswith("tv"):
        category = "tv"
        media_list,r_sum = searchTV.searchTV(query=entry_context)

    elif entry_context.startswith("movie"):
        category = "movie"
        media_list,r_sum = searchMovie.searchMovie(query=entry_context)

    else:
        update.message.reply("滚")

    mediainfo_dump = ""
    for each in media_list:
        mediainfo_dump +='• <a href="{}">{}</a>'.format(f"https://www.themoviedb.org/{category}/{str(each['tmdb_id'])}",f"{each['name']}") + "<b>&lt;TMDb_ID:</b>" + f"<em>{str(each['tmdb_id'])}</em><b>&gt;</b>"  + "\n"

    update.message.reply_text(text=(str(mediainfo_dump + f'\n共检索到{r_sum}个结果')),parse_mode=ParseMode.HTML,disable_web_page_preview=True,)