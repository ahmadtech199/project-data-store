class Person:
    _id = 0

    def __init__(self, name, phone, gender):
        Person._id += 1
        self.id = Person._id
        self.name = name
        self.phone = phone
        self.gender = gender
