from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Alumni:
    '''Docs about Alumni class'''
    BIRTHDATE_FORMAT = "%Y-%m-%d"

    def __init__(self, name: str, surname: str, country, birthdate: date | str, birthdate_format: str = BIRTHDATE_FORMAT) -> None:
        self.name = name
        self.surname = surname
        self.country = country
        self.set_birthdate(birthdate, birthdate_format)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, born on {self.birthdate.strftime(Alumni.BIRTHDATE_FORMAT)} in {self.country}"

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def set_birthdate(self, birthdate: date | str, birthdate_format: str = BIRTHDATE_FORMAT) -> bool:
        try:
            self.birthdate = birthdate if isinstance(birthdate, date) else datetime.strptime(
                birthdate, birthdate_format).date()
        except:
            return False
        else:
            return True

    def get_age(self) -> int:
        return relativedelta(datetime.now().date(), self.birthdate).years


def main():
    alumni_1 = Alumni('Manuel', 'Martín-Malagón',
                      'Spain', '01-01-1998', "%d-%m-%Y")
    alumni_2 = Alumni('Test', 'Testing', 'USA', '1999-12-31')
    alumni_3 = Alumni('Testing', 'Test', 'Canada', datetime.now().date())

    print(alumni_1)
    print(alumni_2)
    print(alumni_3)

    alumni_3.set_birthdate('2012-12-21')
    print(alumni_3.birthdate)

    result = alumni_3.set_birthdate('12-12-12')
    if result:
        print("Birthdate modified correctly")
    else:
        print("Unable to modify birthdate")
    print(alumni_3.birthdate)


if __name__ == "__main__":
    main()
