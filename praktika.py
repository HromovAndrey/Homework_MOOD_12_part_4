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
                target_node.fines[index] = new_fineclass TaxDatabase:

    def update_fine(self, pin, old_fine, new_fine):
        target_node = self._find_node_by_pin(self.root, pin)
        if target_node:
            if old_fine in target_node.fines:
                index = target_node.fines.index(old_fine)
                target_node.fines[index] = new_fine
                print("Fine updated successfully.")
            else:
                print("Fine not found for person with PIN {}.".format(pin))





class Node:
    def __init__(self, pin):
        self.pin = pin
        self.personal_data = {}
        self.fines = []


class TaxDatabase:
    def __init__(self):
        self.root = None

    def add_person(self, pin, personal_data):
        new_node = Node(pin)
        new_node.personal_data = personal_data
        if not self.root:
            self.root = new_node
        else:
            self._add_person(self.root, new_node)



    def add_fine(self, pin, fine):
        target_node = self._find_node_by_pin(self.root, pin)
        if target_node:
            target_node.fines.append(fine)
            print("Fine added successfully.")
        else:
            print("Person with PIN {} not found.".format(pin))

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

    def print_by_city(self,current_node, city):
        if "city" in current_node.personal_data and current_node.personal_data["city"] == city:
                print("PIN:", current_node.pin)
                print("Personal Data:", current_node.personal_data)
                print("Fines:", current_node.fines)
        self.print_by_city(current_node.left, city)
        self.print_by_city(current_node.right, city)
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
        else:
            print("Person with PIN {} not found.".format(pin))