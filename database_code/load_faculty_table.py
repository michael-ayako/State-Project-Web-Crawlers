from mysql import connector as mysql
from static import static
import pandas as pd
from termcolor import colored
from tqdm import tqdm
import re

class load_faculty_table:
    def __init__(self, logger):
        self.logger = logger

    def conn(self):
        static_ = static()
        cnx = mysql.connect(host=static_.host,
                            user=static_.user,
                            passwd=static_.password,
                            db=static_.database)
        return cnx

    def update(self):
        pass

    def data_check(self, email):
        query = 'SELECT * FROM faculty WHERE email = "{}";'\
            .format(email)
        return query

    def insert(self, firstname, lastname, dept, title, email, phone, campus):
        query = 'INSERT INTO faculty (firstname,lastname,department,title,email,phone,campus_id) ' \
                'VALUES("{}","{}","{}","{}","{}","{}","{}");'\
            .format(firstname, lastname, dept, title, email, phone, campus)
        return query

    def __main__(self):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(buffered=True)
            data = pd.read_json('./data/faculty_data.json')
            size = data.campus_id.size
            for x in tqdm(range(size)):
                name = data['name'][x]
                firstname = name.split()[0]
                lastname = name.split()[1]
                title = data['title'][x].strip()
                dept = data['dept'][x].strip()
                email = data['email'][x]
                phone = data['phone'][x].strip()
                campus = data['campus_id'][x]
                if phone == "":
                    phone = 0
                else:
                    phone = re.sub(r"[()-]", "", phone)

                cursor.execute(self.data_check(email))
                m = cursor.fetchone()
                if m == None:
                    cursor.execute(self.insert(firstname, lastname, dept, title, email, phone, campus))
            cnx.commit()
            cnx.close()
        except Exception as err:
            print(colored('Error discovered loading faculty table', 'red'))
            self.logger.warning("/database_code/ZZmain/load_faculty_table: {}".format(err))