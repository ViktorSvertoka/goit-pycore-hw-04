def add_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 2:
            raise ValueError("Exactly 2 arguments (name and phone) are required.")
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error occurred while adding contact: {type(e).__name__}, {e}"


def change_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 2:
            raise ValueError("Exactly 2 arguments (name and phone) are required.")
        name, phone = args
        if name not in contacts:
            return "Contact does not exist"
        contacts[name] = phone
        return "Contact updated."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error occurred while changing contact: {type(e).__name__}, {e}"


def get_contact(args: list, contacts: dict) -> str:
    try:
        if len(args) != 1:
            raise ValueError("Exactly 1 argument (name) is required.")
        name = args[0]
        if name not in contacts:
            return "Contact does not exist"
        return contacts[name]
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error occurred while getting contact: {type(e).__name__}, {e}"


def get_all_contacts(contacts: dict) -> str:
    if not contacts:
        return "Contacts are empty"
    else:
        output = "Contacts:"
        for name, phone in contacts.items():
            output += f"\n{name}: {phone}"
        return output
