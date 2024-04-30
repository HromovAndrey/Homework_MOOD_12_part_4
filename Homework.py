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