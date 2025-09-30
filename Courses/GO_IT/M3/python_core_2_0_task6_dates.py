from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    #today = date.today()
    today = date(2025, 3, 24)  # For testing purposes
    end_date = today + timedelta(days=days + 2)
    target_end_date = today + timedelta(days=days + 1)

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
        if today <= birthday_this_year < end_date:
            congratulation_date = adjust_for_weekend(birthday_this_year)

            if today <= congratulation_date < target_end_date:
                congratulation_date_str = date_to_string(congratulation_date)
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays

if __name__ == "__main__":
    users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# Підготовка списку користувачів
    prepared_users = prepare_user_list(users)

# Зміна today на фіксовану дату (2025-03-20, Четвер) для прикладу
# 20.03.2025 - Четвер
# 21.03.2025 - П'ятниця (Стів Джобс)
# 22.03.2025 - Субота (Джинні Лі, Джонні Лі) -> Переноситься на Понеділок (24.03.2025)
# 23.03.2025 - Неділя (Сара Лі) -> Переноситься на Понеділок (24.03.2025)
# 24.03.2025 - Понеділок
# 25.03.2025 - Вівторок (Білл Гейтс)
# 26.03.2025 - Середа



    upcoming = get_upcoming_birthdays(prepared_users)
    print(f"Майбутні дні народження (від 2025.03.20 до 2025.03.26):")
    print(upcoming)

