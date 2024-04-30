# Завдання 1
# Реалізуйте базу даних зі штрафами податкової
# інспекції. Ідентифікувати кожну конкретну людину буде
# персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання.
class Fine:
    def __init__(self, fine_type, amount):
        self.fine_type = fine_type
        self.amount = amount
        self.next = None


class Person:
    def __init__(self, pin, name, city):
        self.pin = pin
        self.name = name
        self.city = city
        self.fines_head = None


class TreeNode:
    def __init__(self, person):
        self.person = person
        self.left = None
        self.right = None


class TaxDatabase:
    def __init__(self):
        self.root = None

    def print_database(self):
        self._print_database(self.root)

    def _print_database(self, node):
        if node is not None:
            self._print_database(node.left)
            self._print_person(node.person)
            self._print_database(node.right)

    def _print_person(self, person):
        print("PIN:", person.pin)
        print("Name:", person.name)
        print("City:", person.city)
        print("Fines:")
        self._print_fines(person.fines_head)
        print()

    def _print_fines(self, fine):
        current = fine
        while current is not None:
            print("Type:", current.fine_type)
            print("Amount:", current.amount)
            current = current.next

    def print_by_pin(self, pin):
        node = self._find_person(self.root, pin)
        if node is not None:
            self._print_person(node.person)
        else:
            print("Person with PIN {} not found.".format(pin))

    def print_by_fine_type(self, fine_type):
        self._print_by_fine_type(self.root, fine_type)

    def _print_by_fine_type(self, node, fine_type):
        if node is not None:
            self._print_by_fine_type(node.left, fine_type)
            self._print_fines_by_type(node.person.fines_head, fine_type, node.person.pin)
            self._print_by_fine_type(node.right, fine_type)

    def _print_fines_by_type(self, fine, fine_type, pin):
        current = fine
        while current is not None:
            if current.fine_type == fine_type:
                print("PIN:", pin)
                print("Type:", current.fine_type)
                print("Amount:", current.amount)
            current = current.next

    def print_by_city(self, city):
        self._print_by_city(self.root, city)

    def _print_by_city(self, node, city):
        if node is not None:
            self._print_by_city(node.left, city)
            if node.person.city == city:
                self._print_person(node.person)
            self._print_by_city(node.right, city)

    def add_person(self, pin, name, city):
        new_person = Person(pin, name, city)
        new_node = TreeNode(new_person)
        if self.root is None:
            self.root = new_node
        else:
            self._add_person(self.root, new_node)

    def _add_person(self, current_node, new_node):
        if current_node.person.pin == new_node.person.pin:
            print("Person with PIN {} already exists.".format(new_node.person.pin))
        elif current_node.person.pin < new_node.person.pin:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._add_person(current_node.right, new_node)
        else:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._add_person(current_node.left, new_node)

    def add_fine(self, pin, fine_type, amount):
        node = self._find_person(self.root, pin)
        if node is not None:
            new_fine = Fine(fine_type, amount)
            if node.person.fines_head is None:
                node.person.fines_head = new_fine
            else:
                current = node.person.fines_head
                while current.next is not None:
                    current = current.next
                current.next = new_fine
        else:
            print("Person with PIN {} not found.".format(pin))

    def remove_fine(self, pin, fine_type):
        node = self._find_person(self.root, pin)
        if node is not None:
            if node.person.fines_head is None:
                print("Person with PIN {} has no fines.".format(pin))
            elif node.person.fines_head.fine_type == fine_type:
                node.person.fines_head = node.person.fines_head.next
            else:
                current = node.person.fines_head
                while current.next is not None and current.next.fine_type != fine_type:
                    current = current.next
                if current.next is None:
                    print("Fine type {} not found for person with PIN {}.".format(fine_type, pin))
                else:
                    current.next = current.next.next
        else:
            print("Person with PIN {} not found.".format(pin))

    def replace_person_info(self, pin, name, city):
        node = self._find_person(self.root, pin)
        if node is not None:
            node.person.name = name
            node.person.city = city
        else:
            print("Person with PIN {} not found.".format(pin))

    def _find_person(self, node, pin):
        if node is None or node.person.pin == pin:
            return node
        elif pin < node.person.pin:
            return self._find_person(node.left, pin)
        else:
            return self._find_person(node.right, pin)


tax_db = TaxDatabase()

tax_db.add_person("1234567890", "John Doe", "New York")
tax_db.add_person("9876543210", "Jane Smith", "Los Angeles")

tax_db.add_fine("1234567890", "Parking violation", 100)
tax_db.add_fine("1234567890", "Late tax payment", 200)
tax_db.add_fine("9876543210", "Speeding", 150)

tax_db.remove_fine("1234567890", "Late tax payment")

tax_db.replace_person_info("9876543210", "Jane Johnson", "San Francisco")

print("Full database:")
tax_db.print_database()

print("\nData for PIN 1234567890:")
tax_db.print_by_pin("1234567890")

print("\nData for fine type 'Speeding':")
tax_db.print_by_fine_type("Speeding")

print("\nData for city 'San Francisco':")
tax_db.print_by_city("San Francisco")
