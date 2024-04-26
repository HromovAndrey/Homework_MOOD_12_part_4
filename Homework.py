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
        self.fines = None

    def add_person(self, personal_id, name, city ):#додавання особи
        if personal_id not in self.fines:
            self.fines[personal_id] = {"name": name, "city": city, "penalties": None}
    def add_penalty(self, persona_id, penalty_type, penalty_amount):
        if persona_id in self.fines:
            self.fines[persona_id]["penalties"].append({"type":penalty_type, "amount": penalty_amount})
        else:
            print("собу не знайдено")
    def remove_penalty(self, person_id, penalty_index):#удаление штрафа
        if person_id in self.fines and 0 <= penalty_index < len (self.fines[person_id]["penalties"][penalty_index]):
            del self.fines[person_id]["penalties"][penalty_index]
        else:
             print("Недійсна особа або штрафний індекс")

    def print_full_fines(self):
        for person_id, data, in self.fines.items():
            print("Peraonal ID", person_id)
            print("Name", data["city"])
            print("City:", data["city"])
            print("Penalties:")
            for penalty in data["penalties"]:
                print("Type:", penalty["type"])
                print("Amount:", penalty["amount"])
                print()
    def print_by_personal_id(self, personal_id):
        if personal_id in self.fines: data = self.fines[personal_id]
        if personal_id in self.fines: city = self.fines[personal_id]
        print("Personal ID:", personal_id)
        print("Name:", data ["name"])
        print("City:", city["city"])
        print("Penalties:")
        for penalty in data["penalties"]:
            print("Type", penalty["type"])
            print("Amount", penalty["amount"])
            print()
        else:
             print("Особа не знайдена у штрафах")

    def by_penalty_type(self,penalty_type):#тип штрафа
        found = False
        for personal_id, data in self.fines.items():
             for penalty in data["penalties"]:
                 if penalty["type"] == penalty_type:
                     if not found:
                         print("Penalties of type", penalty_type + ":")
                         found = True
                         print("Penalties of type", penalty_type + ":")
                         found = True
                         print("Name", data["city"])
                         print("City", data ["city"])
                         print("Amount", penalty["amount"])
                         print()
             if not found:
                 print("No penalties of type", penalty_type)
    def by_city (self, city):
        found = False
        for personal_id , data in self.fines.items():
            if  data["city"] == city:
                if not found:
                    print("penalty for resident of", city + ":")
                    found = True
                    print("Personal Id")
                    print("Name", data["name"])
                    print("Penalty:" )
                    for penalty in data["penalties"]:
                        print("Amount", penalty["amount"])
                        print()
                        if not found:
                            print("no rezidents found in", city)
    def update_personal_info(self, personal_id, new_name = None, new_city=None):
        if personal_id in self.fines:
            if new_name:
                self.fines[personal_id] ["city"] = new_city
        else:
            print("Особа не знайдена")
    def update_penalty_info(self, personal_id, penalty_index, new_penalty_type = None, new_penalty_amount = None):
        if personal_id in self.fines and 0 <= penalty_index < len(self.fines[personal_id]["penalties"]):
           if new_penalty_type:
               self.fines[personal_id]["penalties"] [penalty_index]["type"] = new_penalty_type
               if new_penalty_amount:
                   self.fines[personal_id]["penalties"][penalty_index]["amount"] = new_penalty_amount
               else:
                   print("Недійсний ідентифікатор особи або штрафний індекс")

fines = TaxPenaltyDatabase
#Додавання особи
fines.add_person("23","Андрій","Миколаїв")
#Додавання штрафів
fines.add_penalty("123", "Порушення", 500)
#Видалення повної бази данних
print("Full fines")
fines.print_full_fines()
print()
#Виведення даних за персональним кодом
fines.by_penalty_type("Додаток на не рухомість")
print()
#виведення данних за місто
print("Data for city")
fines.by_city("Миколаїв")
print()
#Додавання нової особи з інформацією
fines.add_personal("28", "Олена Сидорова", "Одесса")
print("Додавання нової особи Олена Сидорова з Одесси")
#Оновлення інформації про особу та штрафи
fines.update_personal_info("45", new_city="London")
fines.update_personal_info("283", 123, new_penalty_type="Податок на доходи")
#Виведення оновленої бази данних
print()
fines.print_full_fines