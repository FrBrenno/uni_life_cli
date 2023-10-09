from db_manager import create_connection, create_course_tracking_tables
from enum import Enum
from rich import print
import argparse

###################
### STATUS ENUM ###
###################

class CourseStatus(Enum):
    """Enum for the status of a course.
    Unactive:
        Course is not being presented now
    Active:
        Course is being presented now
    """
    UNACTIVE = 0
    ACTIVE = 1

class LectureStatus(Enum):
    """Enum for the status of a course.
    Not happened:
        Lecture have not yet taken place.
    Happened not seen:
        Lecture took place but the user has not yet seen it.
    Seen:
        Lecture took place and the user has seen it.
    Ignored:
        Lecture took place but the user has chosen to ignore it.
    """
    NOT_HAPPENED = 0
    HAPPENED_NOT_SEEN = 1
    SEEN = 2
    IGNORED = 3

class ChapterStatus(Enum):
    """Enum for the status of a course.
    Not Seen:
        This status indicates that the chapter has not yet been viewed in the lectures or coursework.
    In Progress:
        Use this status when the user is currently viewing the chapter but has not completed it.
    Lectures Complete, Notes Not Started:
        This status represents situations where the user has completed the lectures for the chapter but has not yet started taking notes.
    Lectures Complete, Notes In Progress:
        When the user has finished the lectures and is actively taking notes for the chapter, you can use this status.
    Lectures Complete, Notes Complete, Not Reviewed:
        Use this status when the user has finished both the lectures and the notes for the chapter but has not reviewed them.
    Lectures Complete, Notes Complete, Reviewed:
        This status indicates that the chapter is finished, notes are complete, and the user has reviewed them.
        """
    NOT_SEEN = 0
    IN_PROGRESS = 1
    LECTURES_COMPLETED_NOTES_NOT_STARTED = 2
    LECTURES_COMPLETED_NOTES_IN_PROGRESS = 3
    LECTURES_COMPLETED_NOTES_COMPLETED_NOT_REVIEWED = 4
    LECTURES_COMPLETED_NOTES_COMPLETED_REVIEWED = 5

def TpStatus(Enum):
    """Enum for the status of a tp.
    Not happened:
        TP have not yet taken place.
    Happened not attended:
        TP took place but the user has not attended it.
    Attended:
        TP took place and the user attended it.
    Reviewed:
        TP was reviewed by the user.

    """
    NOT_HAPPENED = 0
    HAPPENED_NOT_ATTENDED = 1
    ATTENDED = 2
    REVIEWED = 3

def ProjectStatus(Enum):
    """Enum for the status of a project.
    Not started:
        Project has not yet started.
    In progress:
        Project is in progress
    Completed:
        Project is completed.
    """
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

#########################
### DATABASE FUNCTION ###
#########################

# TODO: ERROR MANAGEMENT

## COURSE FUNCTIONS ##
def add_course(conn, cursor, code, name, semester, status, weight):
    """Adds a course to the database."""
    cursor.execute('''INSERT INTO courses (code, name, semester, status, weight)
                      VALUES (?, ?, ?, ?, ?)''', (code, name, semester, status, weight))
    conn.commit()

def get_course_id(cursor, code):
    """Returns the id of the course with the given code."""
    cursor.execute('''SELECT id FROM courses WHERE code=?''', (code,))
    return cursor.fetchone()[0]

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

## LECTURE FUNCTIONS ##
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

## CHAPTER FUNCTIONS ##
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

## TP FUNCTIONS ##
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

## Project Functions ##

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

###########################
### COMMANDS DEFINITION ###
###########################

# TODO: ERROR MANAGEMENT + VERIFICATION

## COURSE COMMANDS ##
def add_course_command(conn, cursor, args):
    # Call the function to add a course
    add_course(conn, cursor, args.code, args.name, args.semester, args.status, args.weight)
    print(f"Course [bold] {args.code} [/bold] added successfully.")

def delete_course_command(conn, cursor, args):
    delete_course(conn, cursor, args.code)
    print(f"Course [bold] {args.code} [/bold] deleted successfully.")

## LECTURE COMMANDS ##

# TODO: LECTURE COMMANDS

## CHAPTER COMMANDS ##

# TODO: CHAPTER COMMANDS

## TP COMMANDS ##

# TODO: TP COMMANDS

## PROJECT COMMANDS ##

# TODO: PROJECT COMMANDS

def main():
    conn = create_connection('course_tracking.db')
    cursor = conn.cursor()
    # Create the tables if they don't already exist
    create_course_tracking_tables(conn, cursor)

    parser = argparse.ArgumentParser(
        prog="Course Tracking App - UniLife",
        description="This program allows you to better organize your academic life and monitor its progress",
    )

    # Create subparsers for different subcommands
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Command to add a new course
    add_course_parser = subparsers.add_parser("add_course", help="Add a new course")
    add_course_parser.add_argument("code", help="Course code")
    add_course_parser.add_argument("name", help="Course name")
    add_course_parser.add_argument("semester", type=int, help="Course semester")
    add_course_parser.add_argument("status", type=int, help="Course status")
    add_course_parser.add_argument("weight", type=float, help="Course weight")
    add_course_parser.set_defaults(func=add_course)

    args = parser.parse_args()

    # Call the appropriate function based on the subcommand
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


