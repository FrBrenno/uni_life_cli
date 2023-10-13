from enum import Enum

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
