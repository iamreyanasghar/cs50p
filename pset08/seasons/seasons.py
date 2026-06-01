from datetime import datetime, date
import inflect, sys


p = inflect.engine()


def main():
    birth_date = get_date(input("Date of Birth: "))
    print(convert_to_minutes(birth_date))



def get_date(s):
    try:
        pattern = "%Y-%m-%d"
        return datetime.strptime(s, pattern).date()

    except ValueError:
        sys.exit("Invalid date")



def convert_to_minutes(dob):
    minutes = (date.today() - dob).days * 24 * 60
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"



if __name__ == "__main__":
    main()

