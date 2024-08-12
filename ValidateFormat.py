# Validation and Formatting Functions
# Including:
    # Validating Phone Number
    # Validating Email Address
    # Formatting Phone Number


import re


def validate_phone_number(phone_number):
    pattern = r"^\([1-9]{3}\)\s\d{3}-\d{4}"
    if re.match(pattern, phone_number):
        return True
    else:
        return False


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False
    

def validate_date(date):
    # YYYY-MM-DD
    pattern1 = r"(\d{4})-(\d{2})-(\d{2})"
    if re.match(pattern1, date):
        return True
    else:
        return False


def format_phone_number(phone_number):
    numbers = re.sub(r"\D", "", phone_number)
    pattern1 = r"^[1-9]{3}"
    area_code = re.search(pattern1, numbers).group()
    numbers = numbers[3:]
    formatted_number = f"({area_code}) {numbers[:3]}-{numbers[3:]}"
    return formatted_number


def format_date(date):
    # DD.MM.YYYY
    pattern3 = r"((\d{2})\.(\d{2})\.(\d{4}))"
    # DD/MM/YYYY
    pattern2 = r"(\d{2})/(\d{2})/(\d{4})"
    standard = r"\3-\2-\1"
    if re.match(pattern3, date):
        formatted_date = re.sub(pattern3, standard, date)
        return formatted_date
    elif re.match(pattern2, date):
        formatted_date = re.sub(pattern2, standard, date)
        return formatted_date
    else:
        return date
    

def validate_and_format_input(key, value):
    if key == 'Phone Number':
        if validate_phone_number(value):
            return value
        else:
            formatted_value = format_phone_number(value)
            if validate_phone_number(formatted_value):
                return formatted_value
            else:
                print("\nInvalid phone number format.")
                print("Please use (XXX) XXX-XXXX.")
                return None
            
    elif key == 'Email Address':
        if validate_email(value):
            return value
        else:
            print("\nInvalid email address format.")
            print("Please try again.")
            return None
        
    elif key == 'Birthday':
        if validate_date(value):
            return value
        else:
            formatted_value = format_date(value)
            if validate_date(formatted_value):
                return formatted_value
            else:
                print("\nInvalid birthday format.")
                print("Please use YYYY-MM-DD.")
                return None
            
    elif key == 'Anniversary':
        if validate_date(value):
            return value
        else:
            formatted_value = format_date(value)
            if validate_date(formatted_value):
                return formatted_value
            else:
                print("\nInvalid date format.")
                print("Please use YYYY-MM-DD.")
                return None

    else:
        return value