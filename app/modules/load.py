import os, logging, toml
from telegram.utils.request import Request as TGRequest
from telegram import Bot

_cfgFile_RAW = os.path.abspath(os.path.join("bingo", "conf.toml"))
_cfg = toml.load(_cfgFile_RAW)

'''
log setting
'''
if _cfg['Servers']['server']['CONSOLE'] == 'DEBUG':
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )
else:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

logger = logging.getLogger(__name__)
# ### logger END

title_year_regex = r'(^[\uac00-\ud7ff\s\u2E80-\u9FFF_a-zA-Z0-9]+)(y:(\d{4})$)'
title_regex = r'^[\uac00-\ud7ff\s\u2E80-\u9FFF_a-zA-Z0-9]+$'
tmdbid_regex = r'^[0-9]+$'

request = TGRequest(con_pool_size=8)
bot = Bot(token=f"{_cfg['Servers']['BOT']['API_TOKEN']}", request=request)