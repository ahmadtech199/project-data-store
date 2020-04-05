from Person import Person
from Order import Order
from Product import Product
from Company import Company
from Client import Client
from Employee import Employee
from datetime import datetime


company = Company()

person1 = Client("ahmad", "0993893", "male", "ahmad@gmail.com")
person2 = Employee("majed", "46565", "male", 5000, "12 hours")
# person3 = Person("sara", "546852", "female")

client1 = Client("ahmad", "0993893", "male", "ahmad@gmail.com")
client2 = Client("majed", "5645655", "male", "majed@gmail.com")
client3 = Client("sara", "546852", "female", "sara@gmail.com")


employee1 = Employee("majed", "46565", "male", 5000, "12 hours")
employee2 = Employee("abody", "78465", "male", 4000, "8 hours")
employee3 = Employee("amira", "44465", "female", 3000, "4 hours")


product1 = Product("tide", 100)
product2 = Product("fire", 50)
product3 = Product("shambow", 30)

order1 = Order("4524-87-8", True, client1, [product1,product2,product3])
order2 = Order("2010-87-8", True, client1, [product2])
order3 = Order(datetime.now, False, person2, [product1,product3])

company.add_person(client1)
company.add_person(client2)
company.add_person(client3)
company.add_person(employee1)
company.add_person(employee2)
company.add_person(employee3)
company.add_product(product1)
company.add_product(product2)
company.add_product(product3)

company.add_order(order1)
company.add_order(order2)
company.add_order(order3)


# company.print_person_info(1)
# company.print_person_info(2)
# company.print_person_info(3)
# company.print_person_info(4)
# company.print_person_info(5)
# company.print_person_info(6)
# company.print_product_details(1)
# company.print_product_details(2)
# company.print_product_details(3)

company.print_order_details(3)
