from person import Person


def test_person_creation():
    person = Person("Nicky", 25)
    assert person.name == "Nicky"
    assert person.age == 25
    assert person.score == 0


def test_add_score():
    person = Person("Nicky", 25)
    person.add_score(10)
    assert person.score == 10
    person.add_score(5)
    assert person.score == 15


def test_person_str():
    person = Person("Nicky", 25)
    assert str(person) == "Person(name=Nicky, age=25, score=0)"