import sqlite3

def create_connection(db_file):
    """Creates a connection to the database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def create_course_tracking_tables(conn, cursor):
    """Creates the tables in the database if it doesn't already exist."""

    create_course_table(conn, cursor)
    create_course_lecture(conn, cursor)
    create_course_chapter_table(conn, cursor)
    create_course_tp_table(conn, cursor)
    create_course_project_table(conn, cursor)
    create_course_exam_table(conn, cursor)

def create_course_table(conn, cursor):
    # Check if the table 'courses' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='courses'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Table doesn't exist, so create it
        cursor.execute('''CREATE TABLE IF NOT EXISTS courses
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           code TEXT,
                           name TEXT,
                           semester INTEGER,
                           status INTEGER,
                           weight INTEGER)''')
    conn.commit()

def create_course_lecture(conn, cursor):
    """Creates a table with lectures of a certain course"""
    # Check if the table 'courses' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='courses_lectures'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Table doesn't exist, so create it
        cursor.execute('''CREATE TABLE IF NOT EXISTS courses_lectures
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                               course_id INTEGER,
                               lecture_date DATE,
                               description TEXT,
                               status INTEGER,
                               FOREIGN KEY (course_id) REFERENCES courses(id))''')
    conn.commit()



def create_course_chapter_table(conn, cursor):
    # Check if the table 'course_chapters' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='course_chapters'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Table doesn't exist, so create it
        cursor.execute('''CREATE TABLE IF NOT EXISTS course_chapters
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           course_id INTEGER,
                           chapter_number INTEGER,
                           chapter_name TEXT,
                           status INTEGER,
                           FOREIGN KEY(course_id) REFERENCES courses(id))''')
    conn.commit()

def create_course_tp_table(conn, cursor):
    # Check if the table 'course_tps' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='course_tps'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Table doesn't exist, so create it
        cursor.execute('''CREATE TABLE IF NOT EXISTS course_tps
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           course_id INTEGER,
                           tp_number INTEGER,
                           tp_name TEXT,
                           tp_date DATE,
                           status INTEGER,
                           FOREIGN KEY(course_id) REFERENCES courses(id))''')

    conn.commit()


def create_course_project_table(conn, cursor):
     # Check if the table 'course_projects' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='course_projects'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Table doesn't exist, so create it
        cursor.execute('''CREATE TABLE IF NOT EXISTS course_projects
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           course_id INTEGER,
                           project_name TEXT,
                           project_deadline DATE,
                           status INTEGER,
                           FOREIGN KEY(course_id) REFERENCES courses(id))''')


    conn.commit()

def create_course_exam_table(conn, cursor):
    # Check if the table 'course_exams' exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='course_exams'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Table doesn't exist, so create it
        cursor.execute('''CREATE TABLE IF NOT EXISTS course_exams
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           course_id INTEGER,
                           exam_date DATE,
                           exam_duration INTEGER,
                           exam_room TEXT,
                           exam_mark TEXT,
                           FOREIGN KEY(course_id) REFERENCES courses(id))''')
    conn.commit()