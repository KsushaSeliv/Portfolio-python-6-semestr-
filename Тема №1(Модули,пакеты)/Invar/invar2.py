#Создание пользовательского пакета для приложения «Гостевая книга» с прототипами методов,
#позволяющих взаимодействовать с JSON-файлом (создание, удаление, переименование, чтение, запись). 


class GuestBook():

    def __init__(self):
        self.guests = list()


    def add(self, name, surname, age, country): #добавляем человечка с нужными нам параметрами(имя,фамилия,возраст,страна)
        self.guests.append({"guests_name": name,"guests_surname": surname, "guests_age": age, "guests_country": country})
    
    def udal(self, name): #тут удаляем человечка по нужному нам параметру, в данном случае у нас страна
        for guests in self.guests:
            if guests.get("guests_country") == country: 
                self.guests.remove(guests) 

    def zapis(self): #записываем всё в файлик
        import json
        with open("file1.json", 'a') as file:
            json_data = { "Guests": self.guests }
            file.write(json.dumps(json_data, indent=4))
            
if __name__ == "__main__":
    GuestBook = GuestBook()
    GuestBook.add("Ksenia", "Selivanova", 20, "Russia")
    GuestBook.add("Ktoto", "Esho", 25, "Russia")
    
    GuestBook.zapis()


# In[ ]:
