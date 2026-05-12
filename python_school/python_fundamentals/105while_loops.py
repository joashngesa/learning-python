#print 1 to 10
def print_1to10():
    number = 1
    while number <= 10:
        print(number)
        number += 1


#ask user to enter numbers; exit at 5
#if number is invalid; print(..)
def exit_5():
    while True:
         try:
            enter_number = int(input("Enter number: "))
            if enter_number == 5:
                break
            else:
                print("This is not 5, try again")
         except ValueError:
             print("Enter correct number format")
    print("Exit number inserted, exit granted")
           


#ask for numbers untill user gives a positive integer
#if integer is invalid ~ print(..)
def positive_integer():
    while True:
        try:
            integer = int(input("Enter integer: "))
            if integer > 0:
                return integer
            else:
                print("Use a positive number instead")
        except ValueError:
            print("Enter valid integer input, try again please.")
    
positives = positive_integer()
print("Correct integer provided, the number ",positives," is positive.") 


    
#ask the user for password untill they type 'jesusking'
def python_password():
    while True:
        password = input("Enter password: ").strip()
        if password == 'jesusking':
            return password
        else:
            print("Incorrect password, try again please")

python_password_request = python_password()
print("Access granted!")



#Keep asking for two numbers → Handle:
#   invalid input
#   division by zero
def divide_two_numbers():
    while True:
        try:
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
            result = number1 / number2
            print (f"valid numbers inserted, your answer is {result}. Exit granted")
            break

        except ValueError:
            print("Enter the right number format.")
        except ZeroDivisionError:
            print("You can not divide a number by zero, try again please.")


###
#get integer function that:
#keep asking for integer value
#   exits(return) when a valid input is insert, otherwise;
#       ask for a valid input
def get_integer():
    while True:
        try:
            integer = int(input("Enter integer: "))
            return integer
        except ValueError:
            print("Enter valid integer value, try again")
#create a calculator
#uses get_integer() function
def calculator():
    number1 = get_integer()
    number2 = get_integer()
    result = number1 + number2
    print(result)
    return result
#create safe division function
#get numerator (validated)
#get denominator (validated)
#handle division by zero
#retry until valid
#return result
def safe_division():
    while True:
        try:
            numerator = int(input("Enter numerator: "))
            denominator = int(input("Enter the denominator: "))
            results = numerator / denominator
            print(f"Results:{results}")
            return results
        except ValueError:
            print("Invalid number format, try again please")
        except ZeroDivisionError:
            print("You can not divide number by zero")
# create function that
#   Add numbers
#   Divide numbers
#   Exit
def calc_menu():
    while True:
        try:
            user_selection = int(input("Select one number from the following options:\n" \
            "1. calculator\n" \
            "2. safe_division\n" \
            "3. Exit\n"
            "Enter choice: "))
            if user_selection == 1:
                calculator()
            elif user_selection ==2:
                safe_division()
            elif user_selection ==3:
                print("Exit menu, goodbe king!")
                break
            else:
                print("Select a number from the option list")
        except ValueError:
            print("Enter the right number format")