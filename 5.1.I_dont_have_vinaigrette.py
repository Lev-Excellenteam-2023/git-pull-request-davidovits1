# David Ovits
# exercise 5.1 I don't have vinaigrette

import random
import datetime


def validate(str_date):
    """
    Check date validity
    :param str_date: str of date
    :return: True or False
    """
    try:
        datetime.date.fromisoformat(str_date)
        return True
    except ValueError:
        return False


def random_date(first_date, second_date):
    """
    The function receives 2 dates and returns a random date in the range between them
    :param first_date: first date
    :param second_date: second date
    :return: random date in the range between them
    """
    start_date = datetime.date.fromisoformat(first_date)
    end_date = datetime.date.fromisoformat(second_date)
    date = start_date + (end_date - start_date) * random.random()
    return date


def main():
    first_date = ""
    while not validate(first_date):
        first_date = input("enter first date 'YYYY-MM-DD'\n")

    second_date = ""
    while not validate(second_date):
        second_date = input("enter second date 'YYYY-MM-DD'\n")

    date = random_date(first_date, second_date)
    print(date)
    if date.isoweekday() == 1:  # Monday
        print("I have no vinaigrette!")


if __name__ == "__main__":
    main()
