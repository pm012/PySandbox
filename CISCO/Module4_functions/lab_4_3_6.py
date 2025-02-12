def day_of_year(year, month, day):
    # Check if the year, month, and day are valid
    if not (1 <= month <= 12):  # Invalid month
        return None
    if not (1 <= day <= days_in_month(year, month)):  # Invalid day
        return None
    
    # Calculate the day of the year
    day_of_year = sum(days_in_month(year, m) for m in range(1, month)) + day
    return day_of_year

# Previously written functions

def is_year_leap(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def days_in_month(year, month):
    months_with_30_days = {4, 6, 9, 11}
    
    if month == 2:
        return 29 if is_year_leap(year) else 28
    elif month in months_with_30_days:
        return 30
    else:
        return 31

# Test cases
test_cases = [
    (1900, 2, 28),  # Non-leap year, February 28th
    (2000, 2, 29),  # Leap year, February 29th
    (2016, 2, 29),  # Leap year, February 29th
    (1987, 1, 1),   # January 1st
    (2024, 12, 31), # December 31st in a leap year
    (2023, 12, 31), # December 31st in a non-leap year
    (2001, 4, 15),  # April 15th
    (2015, 6, 30),  # June 30th
    (2023, 9, 31),  # Invalid day (September 31st)
    (2023, 13, 1),  # Invalid month (13th month)
    (2023, 4, 31)   # Invalid day (April 31st)
]

for year, month, day in test_cases:
    result = day_of_year(year, month, day)
    print(f"Year: {year}, Month: {month}, Day: {day} -> Day of Year: {result if result is not None else 'Invalid Input'}")
