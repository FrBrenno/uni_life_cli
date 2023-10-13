from course_tracking_database_functions import add_course, list_courses, change_course_status, delete_course
from db_manager import create_connection, create_course_tracking_tables
from rich import print
import argparse

###########################
### COMMANDS DEFINITION ###
###########################

# TODO: ERROR MANAGEMENT + VERIFICATION

## COURSE COMMANDS ##
def add_course_command(conn, cursor, args):
    # Call the function to add a course
    add_course(conn, cursor, args.code, args.name, args.semester, args.status, args.weight)
    print(f"Course [bold]{args.code}[/bold] added successfully.")

def delete_course_command(conn, cursor, args):
    delete_course(conn, cursor, args.code)
    print(f"Course [bold]{args.code}[/bold] deleted successfully.")

def change_course_status_command(conn, cursor, args):
    change_course_status(conn, cursor, args.code, args.status)
    print(f"Course [bold]{args.code}[/bold] status changed successfully.")

def list_courses_command(conn, cursor, args):
    courses = list_courses(cursor)
    print(courses)


## LECTURE COMMANDS ##

# TODO: LECTURE COMMANDS

## CHAPTER COMMANDS ##

# TODO: CHAPTER COMMANDS

## TP COMMANDS ##

# TODO: TP COMMANDS

## PROJECT COMMANDS ##

# TODO: PROJECT COMMANDS

######################
## HELPER FUNCTIONS ##
######################
def setup_course_commands(course_parser):



if __name__ == "__main__":

    # Domain
    domain_list = ["course", "lecture", "chapter", "tp", "project"]
    general_commands = ["add", "delete", "status", "list", "edit"]

    # Create the connection to the database
    conn = create_connection('course_tracking.db')
    cursor = conn.cursor()
    # Create the tables if they don't already exist
    create_course_tracking_tables(conn, cursor)

    # Create the parser
    parser = argparse.ArgumentParser(
        prog="Course Tracking App - UniLife",
        description="This program allows you to better organize your academic life and monitor its progress",
    )

    # Create subparsers for different subcommands
    subparsers = parser.add_subparsers(title="Domains of tracking", dest="domain")

    course_parser = subparsers.add_parser("course", help="Course-related commands")
    lecture_parser = subparsers.add_parser("lecture", help="Lecture-related commands")
    chapter_parser = subparsers.add_parser("chapter", help="Chapter-related commands")
    tp_parser = subparsers.add_parser("tp", help="TP-related commands")
    project_parser = subparsers.add_parser("project", help="Project-related commands")

    # Define the arguments for each subparser
    setup_course_commands(course_parser)




    args = parser.parse_args()

    # Call the appropriate function based on the subcommand
    if hasattr(args, "func"):
        args.func(conn, cursor, args)
    else:
        parser.print_help()


