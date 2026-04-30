def validate_name_and_contact(func):
    def wrapper(name, contact_number):
        if not name or not isinstance(name, str):
            return "Name must be a non-empty string"
        if len(contact_number) !=10 or not contact_number.isdigit():
            return "Contact number must be a 10 digit number"
        return func(name, contact_number)
    return wrapper

@validate_name_and_contact
def register_user(name, contact_number):
    return f"User {name} with contact number {contact_number} has been successfully registered."


print(register_user("Raj","9737304831"))
print(register_user("","9737304831"))
print(register_user("Raj","97373041"))
print(register_user("Raj","97373abc831"))


