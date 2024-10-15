def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This user does not exist. Enter a valid user name."
        except ValueError:
            return "Invalid input. Please enter valid information."
        except IndexError:
            return "Not enough information provided. Try again."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return wrapper


def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()  # Видаляє зайві пробіли або нові рядки в кінці
    else:
        return "No contacts found"  # Якщо немає контактів
    
@input_error
def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]  # Повертає номер телефону
    else:
        return "Contact not found"  # Якщо ім'я не знайдено
    
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [new phone number]"
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone  # Оновлення номера телефону
        return "Contact updated"
    else:
        return "Contact not found"
    
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Invalid command. Usage: change [name] [new phone number]")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command. Usage: phone [name]")
            else:
                print(show_phone(args[0], contacts))
        elif command == "all":
            print(show_all(contacts))  # Викликаємо функцію show_all
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()