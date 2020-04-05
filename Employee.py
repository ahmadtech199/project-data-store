from Person import Person


class Employee(Person):

    def __init__(self, name, phone, gender, salary, working_time):
        super().__init__(name, phone, gender)
        self.salary = salary
        self.working_time = working_time
