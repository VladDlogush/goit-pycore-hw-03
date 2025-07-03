from datetime import datetime, timedelta

def get_upcoming_birthdays(users: dict) -> dict:
    current_date = datetime.today().date()
    birthday_list_users = []

    for user in users:
        birthday_data_user = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_data_user.replace(year=current_date.year)

        if birthday_this_year < current_date:
             birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        days_to_birthday = (birthday_this_year - current_date).days

        if 0 <= days_to_birthday < 7:
           if birthday_this_year.weekday() >= 5:
               days_to_birthday += 7 - birthday_this_year.weekday()

        congratulation_date = current_date + timedelta(days=days_to_birthday)

        birthday_list_users.append(
            {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            }
        )


    return birthday_list_users

users: list[dict[str, str]] = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings this week:", upcoming_birthdays)