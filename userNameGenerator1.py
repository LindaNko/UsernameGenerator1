from xml.dom import UserDataHandler

def user_details():
    """
    Prompt user input
    """
    while True:
        first_name = input("insert your first name: ")
        if first_name.isalpha:
            break
        else:
            print("Invalid input")

    while True:
        last_name = input("insert last name: ")
        if last_name.isalpha:
            break
        else:
            print("invalid input ")    

    while True:
        campus = input("input campus?: ")
        if campus.lower() in ["johannesburg", "cape town","durban","phokeng"]:
            break
        else:
            print("invalid input")


    while True:
        cohort = input("Input cohort?: ")
        if cohort.isdigit():
            break
        else:
            print("invalid cohort ")    

    final_campus = user_campus(campus.lower())
    username = create_user_name(first_name, last_name, cohort, final_campus)
    print("Final username:")
    print(username)       


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    username = first_name[:3] +"_" + last_name[-3:]+"_"+cohort+final_campus
    if username <="3":
        username == first_name +"o"
    if last_name <="3":
        username == last_name + "oo"
    
    return username

def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    if campus.lower() == "johannesburg":
        return "JHB"
    elif campus.lower() == "cape town":
        return "CPT"
    elif campus.lower() == "durban":
        return "DBN"
    elif campus.lower() == "phokeng":
        return "PHO"
    else:
        return ""

if __name__ == '__main__':
    user_details()
