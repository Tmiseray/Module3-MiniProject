# Validation and Formatting Functions
# Including:
    # Validating Phone Number
    # Validating Email Address
    # Formatting Phone Number


import re
import os


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
    

def validate_birthday(birthday):
    # YYYY-MM-DD
    pattern1 = r"(\d{4})-(\d{2})-(\d{2})"
    if re.match(pattern1, birthday):
        return True
    else:
        return False


def format_phone_number(phone_number):
    numbers = re.sub("\D", "", phone_number)
    pattern1 = r"^[1-9]{3}"
    area_code = re.search(pattern1, numbers).group()
    numbers = numbers[3:]
    formatted_number = f"({area_code}) {numbers[:3]}-{numbers[3:]}"
    return formatted_number


def format_birthday(birthday):
    # DD.MM.YYYY or DD/MM/YYYY
    pattern3 = r"((\d{2})\.(\d{2})\.(\d{4})|(\d{2})/(\d{2})/(\d{4}))"
    # # DD/MM/YYYY
    # pattern2 = r"(\d{2})/(\d{2})/(\d{4})"
    standard = r"\3-\2-\1"
    if re.match(pattern3, birthday):
        formatted_birthday = re.sub(pattern3, standard, birthday)
        return formatted_birthday
    # elif re.match(pattern2, birthday):
    #     formatted_birthday = re.sub(pattern2, standard, birthday)
    #     return formatted_birthday
    else:
        return birthday