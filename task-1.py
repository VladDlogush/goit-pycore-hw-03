from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        difference = current_date - date_obj
        return difference.days
    except ValueError:
        return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

print(get_days_from_today("2020-10-09"))