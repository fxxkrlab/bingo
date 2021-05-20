from tmdbv3api import TMDb,Movie, Discover, Search, TV

from app.modules import load

# ### Settings
tmdb = TMDb()
tmdb.api_key = load._cfg['extension']['tmdb']['API_TOKEN']
tmdb.language = 'zh-CN'
tmdb.debug = False
movie = Movie()
discover = Discover()
search = Search()
tv = TV()

# ### Movies
def search_movie_by_title(query):

    result_movie = movie.search(query)

    return result_movie

def search_movies(query, year):
    result_movie = search.movies({"query": query, "year": year})

    return result_movie

# ### TMDb_ID
def search_movie_details(query):
    result_details = movie.details(query)

    return result_details

# ### TV_Shows
def search_tv_by_title(query):
    result_tv = tv.search(query)

    return result_tv

def search_tvs(query, year):
    result_tv = search.tv_shows({"query": query, "first_air_date_year": year})

    return result_tv