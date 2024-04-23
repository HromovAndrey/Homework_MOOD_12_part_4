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
class Person:
    def __init__(self, personal_id, name, city):
        self.personal_id = personal_id
        self.name = name
        self.city = city
        self.fines = []

    def add_fine(self, fine):
        self.fines.append(fine)

    def remove_fine(self, fine):
        if fine in self.fines:
            self.fines.remove(fine)

    def update_info(self, name=None, city=None):
        if name:
            self.name = name
        if city:
            self.city = city

class Fine:
    def __init__(self, fine_type, amount):
        self.fine_type = fine_type
        self.amount = amount

class TaxInspectorateDatabase:
    def __init__(self):
        self.people = {}

    def add_person(self, personal_id, name, city):
        if personal_id not in self.people:
            self.people[personal_id] = Person(personal_id, name, city)

    def add_fine_to_person(self, personal_id, fine_type, amount):
        if personal_id in self.people:
            fine = Fine(fine_type, amount)
            self.people[personal_id].add_fine(fine)

    def remove_fine_from_person(self, personal_id, fine):
        if personal_id in self.people:
            self.people[personal_id].remove_fine(fine)

    def update_person_info(self, personal_id, name=None, city=None):
        if personal_id in self.people:
            self.people[personal_id].update_info(name, city)

    def print_database(self):
        for personal_id, person in self.people.items():
            print(f"Personal ID: {personal_id}")
            print(f"Name: {person.name}")
            print(f"City: {person.city}")
            print("Fines:")
            for fine in person.fines:
                print(f"- Type: {fine.fine_type}, Amount: {fine.amount}")
            print()

    def print_data_by_personal_id(self, personal_id):
        if personal_id in self.people:
            person = self.people[personal_id]
            print(f"Personal ID: {personal_id}")
            print(f"Name: {person.name}")
            print(f"City: {person.city}")
            print("Fines:")
            for fine in person.fines:
                print(f"- Type: {fine.fine_type}, Amount: {fine.amount}")
            print()
        else:
            print("Person not found in the database.")

    def print_data_by_fine_type(self, fine_type):
        found = False
        for personal_id, person in self.people.items():
            for fine in person.fines:
                if fine.fine_type == fine_type:
                    found = True
                    print(f"Personal ID: {personal_id}")
                    print(f"Name: {person.name}")
                    print(f"City: {person.city}")
                    print(f"Fine Type: {fine.fine_type}, Amount: {fine.amount}")
                    print()
        if not found:
            print("No fines of this type found in the database.")

    def print_data_by_city(self, city):
        found = False
        for personal_id, person in self.people.items():
            if person.city == city:
                found = True
                print(f"Personal ID: {personal_id}")
                print(f"Name: {person.name}")
                print(f"City: {person.city}")
                print("Fines:")
                for fine in person.fines:
                    print(f"- Type: {fine.fine_type}, Amount: {fine.amount}")
                print()
        if not found:
            print("No people found from this city in the database.")


def main():
    database = TaxInspectorateDatabase()

    database.add_person("12345", "John Doe", "New York")
    database.add_person("67890", "Alice Smith", "Los Angeles")

    database.add_fine_to_person("12345", "Parking violation", 50)
    database.add_fine_to_person("12345", "Speeding", 100)
    database.add_fine_to_person("67890", "Parking violation", 75)

    print("Printing full database:")
    database.print_database()

    print("Printing data for personal ID 12345:")
    database.print_data_by_personal_id("12345")

    print("Printing data for 'Parking violation' fines:")
    database.print_data_by_fine_type("Parking violation")

    print("Printing data for people from New York:")
    database.print_data_by_city("New York")


if __name__ == "__main__":
    main()
