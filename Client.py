from Person import Person


class Client(Person):
    def __init__(self, name, phone, gender, email):
        super().__init__(name, phone, gender)
        self.email = email
