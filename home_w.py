# Функция для чтения данных из файла
def read_contacts(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            contact = line.strip().split(',')
            contacts.append(contact)
    return contacts

# Функция для записи данных в файл
def write_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

# Функция для поиска контакта по имени или фамилии
def search_contact(contacts, query):
    results = []
    for contact in contacts:
        if query in contact[0] or query in contact[1]:
            results.append(contact)
    return results

# Функция для изменения данных контакта
def edit_contact(contacts, query):
    for contact in contacts:
        if query in contact[0] or query in contact[1]:
            print("Найден контакт:", contact)
            new_name = input("Введите новое имя: ")
            new_phone = input("Введите новый номер телефона: ")
            contact[0] = new_name
            contact[2] = new_phone
            print("Контакт успешно обновлен.")
            return

# Функция для удаления контакта
def delete_contact(contacts, query):
    for contact in contacts:
        if query in contact[0] or query in contact[1]:
            print("Найден контакт:", contact)
            confirmation = input("Вы уверены, что хотите удалить этот контакт? (да/нет): ")
            if confirmation.lower() == 'да':
                contacts.remove(contact)
                print("Контакт успешно удален.")
            return

# Основная функция
def main():
    filename = "контакты.txt"
    contacts = read_contacts(filename)

    while True:
        print("\n1. Показать контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            print("Контакты:")
            for contact in contacts:
                print(contact)
        elif choice == '2':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            phone = input("Введите номер телефона: ")
            contacts.append([surname, name, phone])
            write_contacts(filename, contacts)
            print("Контакт успешно добавлен.")
        elif choice == '3':
            query = input("Введите имя или фамилию для поиска: ")
            results = search_contact(contacts, query)
            if results:
                print("Результаты поиска:")
                for result in results:
                    print(result)
            else:
                print("Контакты не найдены.")
        elif choice == '4':
            query = input("Введите имя или фамилию для изменения: ")
            edit_contact(contacts, query)
            write_contacts(filename, contacts)
        elif choice == '5':
            query = input("Введите имя или фамилию для удаления: ")
            delete_contact(contacts, query)
            write_contacts(filename, contacts)
        elif choice == '6':
            print("Выход...")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()
