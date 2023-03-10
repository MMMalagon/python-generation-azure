from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from enum import Enum


# Instead of Enum, we could use these values inside Course class, build a tuple
# and check if difficulty is in it. If not raising a ValueError exception.
# We coulud also use assertions with that tuple.
class CourseDifficulty(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Course:
    HIGH, MEDIUM, LOW = 3, 2, 1

    def __init__(self, name: str, difficulty: CourseDifficulty | int | str) -> None:
        self.name = name
        self.difficulty = difficulty if isinstance(difficulty, CourseDifficulty) else CourseDifficulty(
            difficulty if isinstance(difficulty, int) else int(difficulty))

    def __str__(self) -> str:
        return f"{self.name} (difficulty level: {int(self.difficulty.value)})"


class Alumni:
    '''Docs about Alumni class'''
    BIRTHDATE_FORMAT = "%Y-%m-%d"

    def __init__(self, name: str, surname: str, country, birthdate: date | str, birthdate_format: str = None) -> None:
        self.name = name
        self.surname = surname
        self.country = country
        self.set_birthdate(birthdate, birthdate_format)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, born on {self.birthdate.strftime(Alumni.BIRTHDATE_FORMAT)} in {self.country}"

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def set_birthdate(self, birthdate: date | str, birthdate_format: str = None) -> bool:
        # default values for function parameters are evaluated when the function is defined, not when it’s called
        # that's why i'm using None as a default birthdate_format and then changing to BIRTHDATE_FORMAT if needed
        # i'm also doing this because i can avoid some inconsistencies when another class inherits from this class
        birthdate_format = Alumni.BIRTHDATE_FORMAT if birthdate_format is None else birthdate_format

        self.birthdate = birthdate if isinstance(birthdate, date) else datetime.strptime(
            birthdate, birthdate_format).date()

    def get_age(self) -> int:
        return relativedelta(datetime.now().date(), self.birthdate).years


class Student(Alumni):
    '''Docs about Student which inherits form Alumni'''

    '''
    def __init__(self, name: str, surname: str, country, birthdate: date | str, birthdate_format: str = None, course: Course = None) -> None:
        super().__init__(name, surname, country, birthdate, birthdate_format)
        self.course = course
    '''

    def __init__(self, alumni: Alumni, course: Course = None) -> None:
        super().__init__(alumni.name, alumni.surname, alumni.country, alumni.birthdate)
        self.course = course

    def __str__(self) -> str:
        return super().__str__() + " - " + self.course.__str__()


def main():
    alumni = Alumni('Manuel', 'Martín-Malagón',
                    'Spain', '01-01-1998', "%d-%m-%Y")
    print(alumni.get_full_name())
    print(alumni)

    course = Course("Azure Developer Associate", CourseDifficulty.MEDIUM)
    student = Student(alumni, course)
    print(student.get_full_name())
    print(Alumni.get_full_name(student))
    print(student)
    print(Alumni.__str__(student))

    '''
    new_course = Course("Power Platform App Maker Associate", 2)
    student.course = new_course
    print(student)

    student.course = Course("DevOps Engineer Expert", "3")
    print(student)

    student.course = None
    print(student)
    '''


if __name__ == "__main__":
    main()
