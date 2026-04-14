class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result_list = []
    for p in people:
        new_person = Person(p["name"], p["age"])
        result_list.append(new_person)
    for p in people:
        current_person = Person.people[p["name"]]
        if "wife" in p and p["wife"] is not None:
            wife_name = p["wife"]
            current_person.wife = Person.people[wife_name]
        if "husband" in p and p["husband"] is not None:
            husband_name = p["husband"]
            current_person.husband = Person.people[husband_name]
    return result_list
