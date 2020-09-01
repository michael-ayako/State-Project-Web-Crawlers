from scrap.ZZmain import scrap_handler
from database_code.ZZmain import database_handler
import logging
import os.path as path
import os
from termcolor import colored
import datetime



def __main__():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")
    filename = './logs/{}.log'.format(date)
    if path.exists("logs")==False :
        os.mkdir("logs")
        print(colored("Logs folder created",'yellow'))
    if path.exists("data")==False :
        os.mkdir("data")
        print(colored("data folder created",'yellow'))

    logging.basicConfig(format='%(asctime)s -   %(levelname)s   -   %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S',
                        filename=filename,
                        level=logging.DEBUG)
    print(colored("The program started at {} {}".format(date, time), 'green'))
    logging.info("The program started at {} {}".format(date, time))

    scrap = scrap_handler(logging)
    scrap.__main__()
    database_load = database_handler(logging)
    database_load.__main__()

    print(colored("The program ended at {} {}".format(date, time), 'green'))
    logging.info("The program ended at {} {}".format(date, time))


__main__()