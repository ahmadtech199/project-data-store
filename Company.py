from Client import Client
from Employee import Employee
from Product import Product


class Company:
    persons = []
    products = []
    orders = []

    def add_product(self, product):
        self.products.append(product)
        print("it's add product new:", product.name)
        print("------------------------")

    def add_person(self, person):
        self.persons.append(person)
        print("it's add person new:", person.name)
        print("------------------------")

    def add_order(self, order):
        self.orders.append(order)
        print("it's add order new:", order.id)
        print("------------------------")

    def remove_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                is_true = True
        if is_true == True:
            print("it's remove:", product.name)
            print("------------------------")

        else:
            print("it's", id, "not found!")
            print("------------------------")

    def remove_person(self, id):
        for person in self.persons:
            if person.id == id:
                self.persons.remove(person)
                is_true = True
        if is_true == True:
            print("it's remove:", person.name)
        else:
            print("it's", id, "not found!")

    def remove_order(self, id):
        for order in self.orders:
            if order.id == id:
                self.orders.remove(order)
                is_true = True
        if is_true == True:
            print("it's remove:", order.id)
            print("------------------------")

        else:
            print("it's", id, "not found!")
            print("------------------------")

    def print_person_info(self, id):
        for person in self.persons:
            if person.id == id:
                print("id:", id)
                print("name:", person.name)
                print("phone:", person.phone)
                print("gender:", person.gender)

                if isinstance(person, Client):
                    print("email:", person.email)
                elif isinstance(person, Employee):
                    print("salary:", person.salary)
                    print("working_time:", person.working_time)
                print("------------------------")
                return
        print("it's", id, "not found!")
        print("------------------------")

    def print_product_details(self, id):
        for product in self.products:
            if product.id == id:
                print("id:", product.id)
                print("name:", product.name)
                print("phone:", product.price)
                print("------------------------")
                return
        print("it's", id, "not found!")
        print("------------------------")

    def print_order_details(self, id):
        total_sum = 0
        for order in self.orders:
            if order.id == id:
                print("id:", order.id)
                print("date:", order.date)
                print("is paid:", "Yes" if order.is_paid else "No")
                print("order by:", order.person.name)
                print("Products:")
                for product in order.products:
                    total_sum += product.price
                    print("- " + product.name + ": " +
                          str(product.price) + "$")

                #  و الذي يمثل ثمن كل المشتريات الموضوعة في الفاتورة و من ثم الخروج من الدالة total_sum هنا سيتم عرض ناتج الجمع الذي تم تخزينه في المتغير
                print("Total Price: " + str(total_sum) + "$")
                print("----------------------")
                return
        # الذي تم تمريره للدالة سيتم طباعة الجملة التالية id يملك نفس رقم الـ orders في حال لم يتم إيجاد أي كائن في المصفوفة
        print("Order with id", id, "is not found!")
        print("----------------------")

    def print_person_orders(self, id):
        is_person_exist = False
        person_name = ""
        for person in self.persons:
            if person.id == id:
                is_person_exist = True
                break
        if not is_person_exist:
            print("Person with id", id, "is not found!")
            print("----------------------")
            return
        else:
            print("All orders made by person with id:", id)
        for order in self.orders:
            if order.person.id == id:
                print("> Ordre: #", order.id)
                print("Date:", order.date)
                print("Is paid:", "Yes" if order.is_paid else "No")
                print("Order by:", order.person.name)
                print("Products:")
                total_sum = 0
                for product in order.products:
                    
                    total_sum += product.price
                    print(f"- {product.name}:{product.price}$")
                print(f"Totla Price: {total_sum}$")
                print("----------------------")
