from datetime import datetime, timedelta
import requests
# import inspect

"""
Contruye un objeto que permita insertar, actulizar, eliminar y consultar los datos de un Alumno.

    Consultar mediante GET -> api/people/<id> por ejemplo api/people/5 -> Retorna 200 OK
    Consultar listado  GET -> api/people/ -> Retorna 200 OK

    Insertar mediante POST -> api/people + datos en JSON en el Body -> Retorna 201 Created + Id del nuevo alumno

    Actualizar mediante PUT -> api/people/<id> por ejemplo api/people/5 + datos en JSON en el Body -> Retorna 204 NoContent

    Eliminar mediante DELETE -> api/people/<id> por ejemplo api/people/5 -> Retorna 204 NoContent
    ATENCIÓN, eliminar solo los alumnos creados por vosotros

"""


def isoformat(dt: datetime) -> str | None:
    return None if dt is None else dt.isoformat(sep='T', timespec='seconds')

class Person:
    __personID = None
    lastName = None
    firstName = None
    hireDate = None
    enrollmentDate = None

    def __init__(self, personID: int, lastName: str, firstName: str,
                 hireDate: str = None, enrollmentDate: str = None) -> None:
        self.__personID = personID
        self.lastName = lastName
        self.firstName = firstName
        self.hireDate = Person.__convert_datetime_to_string(hireDate)
        self.enrollmentDate = Person.__convert_datetime_to_string(enrollmentDate)

    @classmethod
    def __convert_datetime_to_string(cls, dt_iso: str) -> datetime | None:
        return None if dt_iso is None else datetime.fromisoformat(dt_iso)

    @property
    def personID(self):
        return self.__personID

    def __full_name(self) -> str:
        return f"{self.lastName}, {self.firstName}"

    def __str__(self) -> str:
        return f"#{self.personID:<6} - {self.__full_name():<24} - Hired: {str(isoformat(self.hireDate)):<19} - Enrolled: {str(isoformat(self.enrollmentDate)):<19}"


class PeopleService:
    __url = 'http://localhost/api/people/'

    def __init__(self) -> None:
        self.__session = None

    def connect(self) -> None:
        self.__session = requests.Session()

    def __get_all(self) -> list | None:
        try:
            response = self.__session.get(PeopleService.__url)
            response.raise_for_status()

            people = list()

            for person in response.json():
                people.append(Person(person['personID'],
                                     person['lastName'],
                                     person['firstName'],
                                     person['hireDate'],
                                     person['enrollmentDate']))

            return people

        except:
            return None

    def __get_by_id(self, id: int) -> Person | None:
        try:
            response = self.__session.get(PeopleService.__url + str(id))
            response.raise_for_status()

            person = response.json()

            return Person(person['personID'],
                          person['lastName'],
                          person['firstName'],
                          person['hireDate'],
                          person['enrollmentDate'])

        except:
            return None

    def get(self, id: int = None) -> Person | list | None:
        return self.__get_all() if id is None else self.__get_by_id(id)

    def post(self, lastName: str, firstName: str, hireDate: str = None,
             enrollmentDate: str = None) -> Person | None:
        try:
            person = {
                "lastName": lastName,
                "firstName": firstName,
                "hireDate": hireDate,
                "enrollmentDate": enrollmentDate
            }

            response = self.__session.post(PeopleService.__url, json=person)
            response.raise_for_status()

            person['personID'] = response.json()['personID']

            return Person(person['personID'],
                          person['lastName'],
                          person['firstName'],
                          person['hireDate'],
                          person['enrollmentDate'])

        except:
            return None

    def put(self, id: int, lastName: str, firstName: str, hireDate: str = None,
            enrollmentDate: str = None) -> bool:
        result = False

        try:
            person = {
                "personID": id,
                "lastName": lastName,
                "firstName": firstName,
                "hireDate": hireDate,
                "enrollmentDate": enrollmentDate
            }

            response = self.__session.put(PeopleService.__url + str(id), json=person)
            response.raise_for_status()

        except:
            pass

        else:
            result = True

        return result

    '''
    def post(self, **kwargs) -> Person | None:
        try:
            person = {}

            for key, value in kwargs.items():
                if hasattr(Person, key):
                    person[key] = value

            response = self.__session.post(PeopleService.__url, json=person)
            response.raise_for_status()

            person = response.json()

            return Person(person['personID'],
                          person['lastName'],
                          person['firstName'],
                          person['hireDate'],
                          person['enrollmentDate'])

        except:
            return None

    def put(self, id: int, **kwargs) -> bool:
        try:
            person = {"personID": id}

            for key, value in kwargs.items():
                if hasattr(Person, key):
                    person[key] = value

            response = self.__session.put(PeopleService.__url + str(id), json=person)
            response.raise_for_status()

            return True

        except:
            return False
    '''

    def delete(self, id: int) -> bool:
        result = False

        try:
            response = self.__session.delete(PeopleService.__url + str(id))
            response.raise_for_status()

        except:
            pass

        else:
            result = True

        return result

    def close(self) -> None:
        self.__session.close()


def main():
    # print(inspect.getmembers(Person))
    people_service = PeopleService()

    people_service.connect()

    '''
        HTTP GET
    '''
    print("Get all people:")
    for person in people_service.get():
        print(f"\t{str(person)}")

    input("Press Enter to continue...")

    personID = 1
    print(f"Get #{personID} person:")
    person = people_service.get(personID)
    print(f"\t{str(person)}")

    input("Press Enter to continue...")

    '''
        HTTP POST
    '''
    person_attribs = {
        "lastName": "Wathever",
        "firstName": "Muppet",
        "hireDate": isoformat(datetime.now() - timedelta(weeks=1, days=1)),
        "enrollmentDate": isoformat(datetime.now() - timedelta(days=6))
    }
    print("Post new person:")
    person = people_service.post(**person_attribs)
    print(f"\t{str(person)}")

    input("Press Enter to continue...")

    print(f"Get #{person.personID} person (to check creation):")
    person = people_service.get(person.personID)
    print(f"\t{str(person)}")

    input("Press Enter to continue...")

    '''
        HTTP PUT
    '''
    person_attribs["enrollmentDate"] = isoformat(person.enrollmentDate + timedelta(days=5))

    print(f"Put #{person.personID} person:")
    print(f"Result: {people_service.put(person.personID, **person_attribs)}")

    input("Press Enter to continue...")

    print(f"Get #{person.personID} person (to check modification):")
    person = people_service.get(person.personID)
    print(f"\t{str(person)}")

    input("Press Enter to continue...")


    '''
        HTTP DELETE
    '''
    print(f"Delete #{person.personID} person:")
    print(f"Result: {people_service.delete(person.personID)}")

    input("Press Enter to continue...")

    print("Get all people (to check deletion):")
    for person in people_service.get():
        print(f"\t{str(person)}")

    input("Press Enter to continue...")

    people_service.close()

    exit()


if __name__ == "__main__":
    main()
