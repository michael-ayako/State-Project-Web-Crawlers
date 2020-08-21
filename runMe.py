from faculty_scrap import faculty
from course_name_scrap import course_names
from courses_scrap import courses
from database_load import database_load
from scrap_events import events
from junction_table_load import junction_table

def __main__():
    fs = faculty()
    fs.__main__()
    cn = course_names()
    cn.__main__()
    cs = courses()
    cs.__main__()
    ev = events()
    ev.__main__()
    db = database_load()
    db.__main__()
    # jc = junction_table()
    # jc.__main__()

__main__()