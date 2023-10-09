from db_manager import create_connection, create_course_tracking_tables

## COURSE FUNCTIONS ##
def add_course(conn, cursor, code, name, weight):
    """Adds a course to the database."""
    cursor.execute('''INSERT INTO courses (code, name, weight)
                      VALUES (?, ?, ?)''', (code, name, weight))
    conn.commit()

def get_course_id(cursor, code):
    """Returns the id of the course with the given code."""
    cursor.execute('''SELECT id FROM courses WHERE code=?''', (code,))
    return cursor.fetchone()[0]

def delete_course_by_code(conn, cursor, code):
    """Deletes a course using its code"""
    course_id = get_course_id(cursor, code)
    cursor.execute('''DELETE FROM courses WHERE id=?''', (course_id,))
    conn.commit()

## CHAPTER FUNCTIONS ##
def add_chapter(conn, cursor, code, chapter_number, chapter_name):
    """Adds a chapter to an existing course"""
    course_id = get_course_id(cursor, code)
    cursor.execute('''INSERT INTO course_chapters (course_id, chapter_number, chapter_name)
    VALUES (?,?,?)''', (course_id, chapter_number, chapter_name))
    conn.commit()

def get_chapter_id(cursor, code, chapter_number):
    """Returns the chapter's id by using the code of the course and the chapter number"""
    course_id = get_course_id(cursor, code)
    cursor.execute("SELECT id FROM course_chapters WHERE course_id=? AND chapter_number=?", (course_id, chapter_number))

def edit_chapter(conn, cursor, code, chapter_number, chapter_name_updated):
    """Updates chapter information"""
    chapter_id = get_chapter_id(cursor, code, chapter_number)
    cursor.execute("UPDATE course_chapters SET chapter_name=? WHERE chapter_i")


def main():
    conn = create_connection('course_tracking.db')
    cursor = conn.cursor()
    # Create the tables if they don't already exist
    create_course_tracking_tables(conn, cursor)
