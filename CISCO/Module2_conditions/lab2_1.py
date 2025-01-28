def income_tax():
    income = float(input("Enter the annual income: "))

    income_bound = 85528
    tax = 0
    if income <= income_bound:
        tax = income * 0.18 - 556.02
    else:
        tax = 14839.02 + (income - income_bound) * 0.32

    if tax <= 0: tax = 0.
    tax = round(tax, 0)
    print("The tax is: ", tax, " thalers")

def leap_year():
    year = int(input("Enter a year: "))

    if year < 1582:
	    print("Not within the Gregorian calendar period")
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
            print("It's a leap year")
        else:
            print("It's a common year")

    #  Write the if-elif-elif-else block here.


''' As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.


The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

Test your code using the data we've provided. '''



if __name__ == "__main__":
    #income_tax()
    leap_year()

