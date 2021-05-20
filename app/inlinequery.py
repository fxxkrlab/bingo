import re

from telegram import InlineKeyboardMarkup

from app.modules import load, tmdb, strings as st
from app.modules.keyboard import keyboard
from app.modules.inlinearticle import article

pic_url = "https://image.tmdb.org/t/p"

def inlinequery(update, context):
    query = ""
    year = ""
    query = update.inline_query.query
    mediainfo = {}
    medialist = []
    results = []
    if len(query) > 0:
        if query.startswith("movie"):
            query = query.replace("movie", "").strip()

            match_year = re.match(load.title_year_regex, query, flags=re.I)
            match_title = re.match(load.title_regex, query, flags=re.I)

            if match_year is not None:
                query = match_year.group(1)
                year = match_year.group(3)
                results = tmdb.search_movies(query, year)

            #elif match_year is None and match_title is not None and match_id is None:
            elif match_year is None and match_title is not None:
                results = tmdb.search_movie_by_title(query)

            if len(results) > 0:
                for res in results:
                    medialist.append(
                        article(
                            title=res['title'],
                            description=res["release_date"],
                            thumb_url=f"{pic_url}/w500/{res['poster_path']}",
                            message_text=st.INLINE_MOVIE_STR.format(
                                res["original_title"],
                                res["title"],
                                str(res["release_date"]),
                                str(res["popularity"]),
                                str(res["original_language"]),
                                str(res["vote_average"]),
                                res["overview"][:150]+'...',
                            )
                            + f"<a href='{pic_url}/w500/{res['poster_path']}'>&#xad</a>",
                            reply_markup=InlineKeyboardMarkup(
                                keyboard(mv_id=str(res["id"]))
                            ),
                        )
                    )
        elif query.startswith("tv"):
            query = query.replace("tv", "").strip()
            
            match_year = re.search(load.title_year_regex, query, flags=re.I)
            match_title = re.search(load.title_regex, query, flags=re.I)

            if match_year is not None:
                query = match_year.group(1)
                year = match_year.group(3)
                results = tmdb.search_tvs(query, year)

            elif match_year is None and match_title is not None:
                results = tmdb.search_tv_by_title(query)

            if len(results) > 0:
                for res in results:
                    medialist.append(
                        article(
                            title=res['name'],
                            description=res["first_air_date"],
                            thumb_url=f"{pic_url}/w500/{res['poster_path']}",
                            message_text=st.INLINE_TV_STR.format(
                                res["original_name"],
                                res["name"],
                                res["origin_country"],
                                str(res["first_air_date"]),
                                str(res["popularity"]),
                                str(res["original_language"]),
                                str(res["vote_average"]),
                                res["overview"][:150]+'...',
                            )
                            + f"<a href='{pic_url}/w500/{res['poster_path']}'>&#xad</a>",
                            reply_markup=InlineKeyboardMarkup(
                                keyboard(tv_id=str(res["id"]))
                            ),
                        )
                    )
        else:
            return inlineHELP(update, medialist)

    update.inline_query.answer(medialist[:50], cache_time=10)


def inlineHELP(update, medialist):
    medialist.append(article(
            title="• InlineQuery •命令格式提示",
            description="movie|tv name y:year(optional)\n请根据范例查询或发送本消息获取更多规则",
            message_text=st.INLINE_FORMAT_NOTICE,))
    update.inline_query.answer(medialist[:50])