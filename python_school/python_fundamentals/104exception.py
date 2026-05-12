#Safe integer input
    #check the validity of integer input and return:
    #   return "valid integer"
    #   return "invalid integer format"
def safe_integer_input():
    integer_input = input("Enter number: ")
    try:
        return int(integer_input)
    except ValueError:
        return None
       
number_check = safe_integer_input()
if number_check is None:
    print("invalid_integer_format")
else:
    print("valid integer")


#Safe division 
    #Input numerator
    #input denominator
    #   check for ValueError 
    #   check for ZeroDivisionError
def Safe_division():
    try:
       numerator_input = int(input("Enter the numerator: "))
       denominator_input = int(input("Enter the denominator: "))
       division = numerator_input / denominator_input
       print(division)
       return division
    except ValueError:
       print("Please enter right number format")
    except ZeroDivisionError:
       print("You can not divide by zero")


#float temperature handler
    #Check the input if float
    #   check if input >= 30 ~ print("hot zone")
    #   check if input >= 20 ~ print("normal temperature zone")
    #   else ~ print("low temperature zone")
    #except ValueError:
def float_temperature_handler():

    try:
        temperature_input = float(input("Enter warehouse temperature: "))
        if temperature_input >= 30:
            print("hot zone")
        elif temperature_input >= 20:
            print("nomal temperature zone")
        else:
            print("low temperature zone")
    except ValueError:
        print("Please enter correct temperature format")



#REUSABLE INTEGER FUNCTION
    #ask for integer input
    #check if number is integer and return
    #except: return none
    #call the function
    #print("valid number format: ")
    #print("invalid number format")

def reusable_number_function():
        
    number_input = input("Enter number: ")
    try:
        return int(number_input)
        
    except ValueError:
        return None

number = reusable_number_function()
if number is None:
    print("Invalid number format")
else:
    print("valid number format:",number)


#NUMBER ANALYZER
    #request for input, try: int(input)
    #   check if the input is positive
    #   check if input is negative
    #   check if input is zero
    #except: print("invalid number format")

def number_analyzer():
    integer_input = input("Enter number: ")
    try:
        integer = int(integer_input)
        if integer > 0:
            return "Positive number"
        elif integer < 0:
            return "Negative number"
        else:
            return "Equal to zero"
    except ValueError:
        return "Invalid number format"

result = number_analyzer()
print(result)

#CALCULATOR ENGINE
    #request for number
    #request for operator
    #request for number2
    #   except ValueError
    #   except ZeroDivisionError
    #   except "Unsupported operand"

def calculator():
    try:
        number1 = float(input("Enter the first number: "))
        operand= input("Enter the operand:").strip()
        number2 = float(input("Enter the second number:"))

        if operand =="+":
            result = number1 + number2
        elif operand =="-":
            result = number1 - number2
        elif operand =="*":
            result = number1 * number2
        elif operand =="/":
            result = number1 / number2
        else:
            print("please use correct operation")
            return
        
        print("The result is:",result)
        return result
    except ValueError:
        print("Enter the right number format")
    except ZeroDivisionError:
        print("Can not divide number by zero")
 

#LIST INDEX ACCESS
    #create list numbers = [10, 20, 30, 40]
    #ask for value of index
    #print the value of index

def list_acces():
    try:
        
        numbers = [10,20,30,40]
        index = int(input("Enter index: "))
        print("value of index:",numbers[index])
       
    except ValueError:
        print("Enter the right value format")
    except IndexError:
        print("index provided should be within range")

#DATA ENTRY VALIDATION
    #ask for user name
    #ask for age
    #if age is integer
    #   if age >= 18 ~ ("name",adult)
    #   else ~ ("name",youth)
    #except ValueError

def data_entry():
    try:
        user_name = input("Enter name: ").strip()
        user_age = int(input("Enter age: "))
        if user_age >= 18:
            print(f"{user_name}: adult")
        else:
            print(f"{user_name}: youth")
    
    except ValueError:
        print("Enter age in the right number format")

#BATCH INPUT SIMULATION
    #create a list
    #add only valid integers inputs to the list
    #   input1 
    #   input2
    #   input3 
    
def input_simulation():
    try:
        batch_list = []
        batch1 = int(input("Enter number: "))
        batch2 = int(input("Enter second number: "))
        batch3 = int(input("Enter third number: "))
        add_list = [batch1,batch2,batch3]
        batch_list.extend(add_list)
        print(batch_list)
        return
    
    except ValueError:
        print("please insert numbers only")

#RETRY MECHANISM
    #ask for integer
    #keep asking untill the right integer is given
    #   exit-when integer is right ~("correct integer provided, input.")

def integer_check():

    while True:
        try:
            integer_input = input ("Enter integer to check: ")
            integer = int(integer_input)
            break
        except:
            print("incorrect integer format, try again please")
        
    print("Correct integer provided;",integer)
