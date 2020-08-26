
from database_code.database_load import database_load

from scrap.ZZmain import scrap_handler
import logging
import logging.config
import os.path as path
import os
import datetime



def __main__():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")
    filename = './logs/{}.log'.format(date)
    if path.exists("logs")==False :
        os.mkdir("logs")
    logging.basicConfig(format='%(asctime)s -   %(levelname)s   -   %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S',
                        filename=filename,
                        level=logging.DEBUG)
    print("The program started at {} {}".format(date,time))
    logging.info("The program started at {} {}".format(date,time))

    scrap = scrap_handler(logging)
    scrap.__main__()


    # fs = faculty()
    # fs.__main__()
    # cn = course_names()
    # cn.__main__()
    # cs = courses()
    # cs.__main__()
    # ev = events()
    # ev.__main__()
    # db = database_load()
    # db.__main__()
    # jc = junction_table()
    # jc.__main__()

__main__()