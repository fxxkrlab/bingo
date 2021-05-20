import re

from app.modules import load, tmdb

# ### searchTV payload
def searchTV(query):
    entry_context = query
    mediainfo = {}
    media_list = []
    entry_context = entry_context.replace("tv", "").strip()
    match_year = re.search(load.title_year_regex, entry_context, flags=re.I)
    match_title = re.search(load.title_regex, entry_context, flags=re.I)
    if "y:" in entry_context:
        query = match_year.group(1)
        year = match_year.group(3)
        results = tmdb.search_tvs(query, year)
        r_sum = len(results)
        for res in results:
            mediainfo['tmdb_id'] = res.id
            mediainfo['name'] = res.name
            media_list.append(mediainfo)
            mediainfo ={}
    else:
        results = tmdb.search_tv_by_title(query=entry_context)
        r_sum = len(results)
        for res in results:
            mediainfo['tmdb_id'] = res.id
            mediainfo['name'] = res.name
            media_list.append(mediainfo)
            mediainfo ={}

    return (media_list,r_sum)