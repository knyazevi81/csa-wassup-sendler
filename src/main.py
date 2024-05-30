from aiogram.utils import executor

from handlers import identification
#from handlers import root_add_handlers
from setup import dp, database_export
from aiogram.contrib.middlewares.logging import LoggingMiddleware

database_export()

#root_add_handlers.register_handlers(dp)
identification.register_handlers(dp)

#добавить информацию из базы знаний
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    dp.middleware.setup(LoggingMiddleware())