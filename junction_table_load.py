from mysql import connector as mysql
from static import static
import pandas as pd
from tqdm import tqdm
import re

class junction_table :
    def __init__(self):
        pass

    def course_has_faculty(self):
        static_ = static()
        try:
            cnx = mysql.connect(host=static_.host,
                                user=static_.user,
                                passwd=static_.password,
                                db=static_.database)
            cursor = cnx.cursor(buffered=True)

            cnx.commit()
            cnx.close()
        except Exception as err:
            cnx.rollback()
            print('Error: {}'.format(err))


    def __main__(self):
        print("Matching course_has_faculty")