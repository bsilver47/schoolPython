from datetime import date

def main():
    gender = int(input("What is your gender? (0 for Male, 1 for Female) "))
    pounds = float(input("How much do you weigh in US pounds? "))
    inches = float(input("How tall are you in US inches? "))
    birth_str = input("What is your date of birth? (YYYY-MM-DD) ")
    
def date_num(date_str):
    dt = date_str.split("-")
    for x in range(2):
        norm_date[x] = int(dt[x])
        print(norm_date[x])
    return norm_date[]

##def compute_age(birth_str):
    dob = date_num(birth_str)
    today = str(date.today())
    now = date_num(today)

    if now[1] > dob[1]:
        age = ((now[0] - dob[0]) - 1)
    elif now[1] < dob[1]:
        age = (now[0] - dob[0])
    else:
        if now[2] > dob[2]:
            age = ((now[0] - dob[0]) - 1)
        elif now[2] < dob[2]:
            age = (now[0] - dob[0])
        else:
            print("Happy Birthday!!")
            age = (now[0] - dob[0])
    return age

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    return kilo_mass

def cm_from_in(inches):
    return centi_height

def body_mass_index(weight, height):
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    return bmr

birth_str = input("What is your date of birth? (YYYY-MM-DD) ")
age = compute_age(birth_str)
print(age)