#SCOPE, USER INPUT , CONDITIONS

#input validation warm up
#logical flow;

#ask age→
# check if input is int→
# print selected based on int check
def age_confirmation():
    age_input= input("Enter age: ")

    if age_input.isdigit():
        age = int(age_input)
        print("age format accepted")       
        return age  
    else:
        print("inavlid age")

#Nested voting classification
    #checks if the age is valid
    #checks if the age is >= 18 .
    # ...if the age is >=60 ="senior voter".
    # ...else = "regular voter"
    # .else "too young to vote"
def voting_age_check():
    voter_age = input("Enter your age: ")
    if voter_age.isdigit():
        age = int(voter_age)
        if age >= 18:
            if age >= 60:
                print("senior voter")
            else:
                print("regular voter")
        else:
            print("too young to vote")
    else:
        print("inavlid age format")
voting_age_check()   

#Number analyzer function
    #takes number input
    # .checks the number is int 
    # ...positive
    # ...negative
    # ...zero
def number_analyzer():
    digit_check = input("enter number: ").strip()
    try:
        number = int(digit_check)

        if number > 0:
            print("the number is positive")
        elif number < 0:
            print("the number is negative")
        else:
            print("the number is zero")   
    except ValueError:
        print("invalid number format")

number_analyzer()

#Password gate system
    #input password
    #check if len(password_input) > 6
    # print("access granted") 
    #else("password too short")
def password_gate_system():
    password_input=input("Enter password: ")
    if len(password_input) > 6:
        print("access granted")
    else:
        print("password too short")

password_gate_system()

#Temperature check engine
    #check if input is numeric
    #   check if inputs is >= 30 ~ print("Extremely high temperatures")
    #   check if input >=20 ~ print("Safe temperatures")
    #   else if input is < 20 ~ print("Extremely low temperatures")
def temperature_check_engine():
    temperature_input = input("Enter warehouse temperatures: ")

    try:
        temperatures = float(temperature_input)
        if temperatures >= 30:
            print("Extremely high temperatures")
        elif temperatures >= 20:
            print("Safe temperatures")
        else:
            print("Extremely low temperatures")

    except ValueError:
        print("invalid input format")

temperature_check_engine()



