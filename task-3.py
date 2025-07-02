import re

def normalize_phone(phone_number: str) -> str:
    normalized_number = re.sub(r"\D", "", phone_number)
    if not normalized_number.startswith("+"):
        normalized_number = "+38" + normalized_number.lstrip("38")

    return normalized_number

raw_numbers: list[str] = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(phone_number) for phone_number in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)