from telegram import InlineKeyboardButton


def keyboard(
    tv_id=None,
    mv_id=None,
):
    """
    Attach InlineKeyboardButton dynamically from data
    """

    keyblist = [[]]

    if tv_id:
        keyblist.append(
            [
                InlineKeyboardButton(
                    text="查阅TMDB详情",
                    url=f"https://www.themoviedb.org/tv/{tv_id}",
                )
            ]
        )

    if mv_id:
        keyblist.append(
            [
                InlineKeyboardButton(
                    text="查阅TMDB详情",
                    url=f"https://www.themoviedb.org/movie/{mv_id}",
                )
            ]
        )

    return keyblist
