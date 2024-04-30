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

    # 1. Повний друк бази даних
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

    # 2. Друк даних за конкретним кодом
    def print_by_pin(self, pin):
        node = self._find_person(self.root, pin)
        if node is not None:
            self._print_person(node.person)
        else:
            print("Person with PIN {} not found.".format(pin))

    # 3. Друк даних за конкретним типом штрафу
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

    # 4. Друк даних за конкретним містом
    def print_by_city(self, city):
        self._print_by_city(self.root, city)

    def _print_by_city(self, node, city):
        if node is not None:
            self._print_by_city(node.left, city)
            if node.person.city == city:
                self._print_person(node.person)
            self._print_by_city(node.right, city)

    # 5. Додавання нової людини з інформацією про неї
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

    # 6. Додавання нових штрафів для вже існуючого запису
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

    # 7. Видалення штрафу
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

    # 8. Заміна інформації про людину та її штрафи
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


# Приклад використання:

tax_db = TaxDatabase()

# Додавання людини
tax_db.add_person("1234567890", "John Doe", "New York")
tax_db.add_person("9876543210", "Jane Smith", "Los Angeles")

# Додавання ш



class TaxDatabase:


    def _add_person(self, current_node, new_node):
        if current_node.pin == new_node.pin:
            # Якщо такий ПІН вже існує, можна розглянути різні варіанти:
            # - Замінити існуючу інформацію про особу
            # - Додати штраф до існуючої особи
            # - Інші можливості, в залежності від ваших вимог
            pass
        elif current_node.pin < new_node.pin:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._add_person(current_node.right, new_node)
        else:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._add_person(current_node.left, new_node)




    def add_fine(self, pin, fine):
        target_node = self._find_node_by_pin(self.root, pin)
        if target_node:
            target_node.fines.append(fine)
            print("Fine added successfully.")
        else:
            print("Person with PIN {} not found.".format(pin))

    def _find_node_by_pin(self, current_node, pin):
        if current_node is None:
            return None
        elif current_node.pin == pin:
            return current_node
        elif current_node.pin < pin:
            return self._find_node_by_pin(current_node.right, pin)
        else:
            return self._find_node_by_pin(current_node.left, pin)


    def remove_fine(self, pin, fine):
        target_node = self._find_node_by_pin(self.root, pin)
        if target_node:
            if fine in target_node.fines:
                target_node.fines.remove(fine)
                print("Fine removed successfully.")
            else:
                print("Fine not found for person with PIN {}.".format(pin))
        else:
            print("Person with PIN {} not found.".format(pin))




    def print_database(self):
        if self.root:
            self._print_node(self.root)
        else:
            print("Tax database is empty.")

    def _print_node(self, current_node):
        if current_node:
            print("PIN:", current_node.pin)
            print("Personal Data:", current_node.personal_data)
            print("Fines:", current_node.fines)
            print()
            self._print_node(current_node.left)
            self._print_node(current_node.right)


    def print_by_pin(self, pin):
        target_node = self._find_node_by_pin(self.root, pin)
        if target_node:
            print("PIN:", target_node.pin)
            print("Personal Data:", target_node.personal_data)
            print("Fines:", target_node.fines)
        else:
            print("Person with PIN {} not found.".format(pin))



    def print_by_fine_type(self, fine_type):
        self._print_by_fine_type_helper(self.root, fine_type)

    def _print_by_fine_type_helper(self, current_node, fine_type):
        if current_node:
            for fine in current_node.fines:
                if fine["type"] == fine_type:
                    print("PIN:", current_node.pin)
                    print("Personal Data:", current_node.personal_data)
                    print("Fine:", fine)
                    print()
            self._print_by_fine_type_helper(current_node.left, fine_type)
            self._print_by_fine_type_helper(current_node.right, fine_type)



    def print_by_city(self, city):
        self._print_by_city_helper(self.root, city)

    def _print_by_city_helper(self, current_node, city):
        if current_node:
            if "city" in current_node.personal_data and current_node.personal_data["city"] == city:
                print("PIN:", current_node.pin)
                print("Personal Data:", current_node.personal_data)
                print("Fines:", current_node.fines)
                print()
            self._print_by_city_helper(current_node.left, city)
            self._print_by_city_helper(current_node.right, city)



    def update_person(self, pin, personal_data):
        target_node = self._find_node_by_pin(self.root, pin)
        if target_node:
            target_node.personal_data.update(personal_data)
            print("Personal data updated successfully.")
        else:
            print("Person with PIN {} not found.".format(pin))



    def update_fine(self, pin, old_fine, new_fine):
        target_node = self._find_node_by_pin(self.root, pin)
        if target_node:
            if old_fine in target_node.fines:
                index = target_node.fines.index(old_fine)
                target_node.fines[index] = new_fine
                print("Fine updated successfully.")
            else:
                print("Fine not found for person with PIN {}.".format(pin))
