from course_tracking_status import CourseStatus, LectureStatus, ChapterStatus, TpStatus, ProjectStatus

#########################
### DATABASE FUNCTION ###
#########################

# TODO: ERROR MANAGEMENT

def add_course(conn, cursor, code, name, semester, status, weight):
    """Adds a course to the database."""
    cursor.execute('''INSERT INTO courses (code, name, semester, status, weight)
                      VALUES (?, ?, ?, ?, ?)''', (code, name, semester, status, weight))
    conn.commit()


def get_course_id(cursor, code):
    """Returns the id of the course with the given code."""
    cursor.execute('''SELECT id FROM courses WHERE code=?''', (code,))
    return cursor.fetchone()[0]


def list_courses(cursor):
    """Returns all the courses in the database"""
    cursor.execute('''SELECT * FROM courses''')
    return cursor.fetchall()


def change_course_status(conn, cursor, code, new_status):
    """Changes the status of the course"""
    if new_status in CourseStatus:
        course_id = get_course_id(cursor, code)
        cursor.execute("UPDATE courses SET status=? WHERE id=?", (new_status.value(), course_id))
        conn.commit()


def delete_course(conn, cursor, code):
    """Deletes a course using its code"""
    course_id = get_course_id(cursor, code)
    cursor.execute('''DELETE FROM courses WHERE id=?''', (course_id,))
    conn.commit()


def get_lecture_id(cursor, code, lecture_date):
    """Returns the lecture id"""
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT id FROM course_lecture WHERE course_id=? AND lecture_date=?", (course_id, lecture_date))
    return cursor.fetchone()[0]


def create_lecture(conn, cursor, code, lecture_date, description, status):
    course_id = get_course_id(cursor, code)
    cursor.execute("INSERT INTO course_lectures (course_id, lecture_date, description, status) VALUES (?,?,?,?)",
                   (course_id, lecture_date, description, status))
    conn.commit()


def edit_lecture(conn, cursor, code, lecture_date, description):
    lecture_id = get_lecture_id(cursor, code, lecture_date)
    cursor.execute("UPDATE course_lectures SET description=? WHERE lecture_id=?", (description, lecture_id))
    conn.commit()


def change_lecture_status(conn, cursor, code, lecture_date, new_status):
    if new_status in LectureStatus:
        lecture_id = get_lecture_id(cursor, code, lecture_date)
        cursor.execute("UPDATE course_lectures SET status=? WHERE id=?", (new_status.value(), lecture_id))
        conn.commit()


def delete_lecture(conn, cursor, code, lecture_date):
    lecture_id = get_lecture_id(cursor, code, lecture_date)
    cursor.execute("DELETE FROM course_lectures WHERE lecture_id=?", (lecture_id))
    conn.commit()

def list_lectures(cursor, code):
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT * FROM course_lectures WHERE course_id=?", (course_id,))
    return cursor.fetchall()


def add_chapter(conn, cursor, code, chapter_number, chapter_name, status):
    """Adds a chapter to an existing course"""
    course_id = get_course_id(cursor, code)
    cursor.execute('''INSERT INTO course_chapters (course_id, chapter_number, chapter_name, status)
    VALUES (?,?,?, ?)''', (course_id, chapter_number, chapter_name, status))
    conn.commit()


def get_chapter_id(cursor, code, chapter_number):
    """Returns the chapter's id by using the code of the course and the chapter number"""
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT id FROM course_chapters WHERE course_id=? AND chapter_number=?", (course_id, chapter_number))
    return cursor.fetchone()[0]


def edit_chapter(conn, cursor, code, chapter_number, chapter_name_updated):
    """Updates chapter information"""
    chapter_id = get_chapter_id(cursor, code, chapter_number)
    cursor.execute("UPDATE course_chapters SET chapter_name=? WHERE chapter_id=?", (chapter_name_updated, chapter_id))
    conn.commit()


def change_chapter_status(conn, cursor, code, chapter_number, new_status):
    """Changes the status of the course"""
    if new_status in ChapterStatus:
        chapter_id = get_chapter_id(cursor, code, chapter_number)
        cursor.execute("UPDATE course_chapters SET status=? WHERE id=?", (new_status.value(), chapter_id))
        conn.commit()


def delete_chapter(conn, cursor, code, chapter_number):
    """Deletes a chapter"""
    chapter_id = get_chapter_id(cursor, code, chapter_number)
    cursor.execute("DELETE FROM course_chapters WHERE chapter_id=?", (chapter_id))
    conn.commit()

def list_chapters(cursor, code):
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT * FROM course_chapters WHERE course_id=?", (course_id,))
    return cursor.fetchall()

def get_tp_id(cursor, code, tp_number):
    """Returns the tp id"""
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT id FROM course_tps WHERE course_id=? AND tp_number=?", (course_id, tp_number))
    return cursor.fetchone()[0]


def create_tp(conn, cursor, code, tp_number, tp_name, tp_date, status):
    """Creates a tp of a course"""
    course_id = get_course_id(cursor, code)
    cursor.execute("INSERT INTO course_tps (course_id, tp_number, tp_name, tp_date, status) VALUES (?,?,?,?,?)", (course_id, tp_number, tp_name, tp_date, status))
    conn.commit()


def edit_tp(conn, cursor, code, tp_number, tp_name_updated, tp_date_updated):
    """Updates tp information"""
    tp_id = get_tp_id(cursor, code, tp_number)
    cursor.execute("UPDATE course_tps SET tp_name=?, tp_date=? WHERE id=?", (tp_name_updated, tp_date_updated, tp_id))
    conn.commit()


def change_tp_status(conn, cursor, code, tp_number, new_status):
    """Changes the status of the tp"""
    if new_status in TpStatus:
        tp_id = get_tp_id(cursor, code, tp_number)
        cursor.execute("UPDATE course_tps SET status=? WHERE id=?", (new_status.value(), tp_id))
        conn.commit()


def delete_tp(conn, cursor, code, tp_number):
    """Deletes a tp"""
    tp_id = get_tp_id(cursor, code, tp_number)
    cursor.execute("DELETE FROM course_tps WHERE id=?", (tp_id))
    conn.commit()

def list_tps(cursor, code):
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT * FROM course_tps WHERE course_id=?", (course_id,))
    return cursor.fetchall()

def create_project(conn, cursor, code, project_name, project_deadline, status):
    course_id = get_course_id(cursor, code)
    cursor.execute("INSERT INTO course_projects(course_id, project_name, project_deadline, status) VALUES (?, ?, ?, ?)",(course_id, project_name, project_deadline, status))
    conn.commit()


def get_project_id(cursor, code, project_name):
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT id FROM course_projects WHERE course_id=? AND project_name=?", (course_id, project_name))
    return cursor.fetchone()[0]


def change_project_status(conn, cursor, code, project_name, new_status):
    """Changes the status of the project"""
    if new_status in ProjectStatus:
        project_id = get_project_id(cursor, code, project_name)
        cursor.execute("UPDATE course_projects SET status=? WHERE id=?", (new_status.value(), project_id))
        conn.commit()


def edit_project_deadline(conn,cursor, code, project_name, project_deadline):
    project_id = get_project_id(cursor, code, project_name)
    cursor.execute("UPDATE course_projects SET project_deadline=? WHERE project_id=?", (project_deadline, project_id))
    conn.commit()


def delete_project(conn, cursor, code, project_name):
    project_id = get_project_id(cursor, code, project_name)
    cursor.execute("DELETE FROM course_projects WHERE project_id=?", (project_id))
    conn.commit()

def list_projects(cursor, code):
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT * FROM course_projects WHERE course_id=?", (course_id,))
    return cursor.fetchall()