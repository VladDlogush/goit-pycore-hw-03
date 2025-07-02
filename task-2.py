import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if quantity > (max - min + 1) or min < 1 or max > 1000:
        return []

    return sorted(random.sample(range(min, max + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)