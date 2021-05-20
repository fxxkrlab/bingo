from telegram.ext import (
    Updater,
    Dispatcher,
    CommandHandler as CH,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    InlineQueryHandler,
)

import __version__
from app import _help as _h, searchALL as sA, inlinequery as ilQuery
from app.modules import load

LOG = load.logger

def main():
    if load._cfg['Servers']['Mod']['mod'] == 'long':
        bot = load.bot
        updater = Updater(bot=bot, use_context=True)

        dp = updater.dispatcher

        dp.add_handler(CH("help", _h._help))
        dp.add_handler(CH('search',sA.searchALL))
        dp.add_handler(InlineQueryHandler(ilQuery.inlinequery,run_async=True))

        '''
        Start TGBOT
        '''

        updater.start_polling()
        LOG.info("Fxxkr LAB :: Bingo" + __version__.__version__ + " is Started")
        updater.idle()

    else:
        print('Wrong Arguments')

if __name__ == "__main__":
    main()