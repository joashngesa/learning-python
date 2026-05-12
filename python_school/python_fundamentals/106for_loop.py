#Create a list of 5 numbers and print each one
list=[2,34,56,432,3]
for item in list:
    print(item)

#Print only the last element
print(list[-1])

#Print first 3 elements using slicing
print(list[:3])

#Add a number to a list using append()
list.append(28)
print(list)

#Remove the second element
list.pop(1)
print(list)

#Loop through a list and print all values
legends=["wenger","mandela","diaby","tom mboya"]
for legend in legends:
    print(legend)

#Print only even numbers
list2 = [1,45,3,6,7,34,56,678,64,4,56]
for num in list2:
    if num % 2 == 0:
        print(num)
#Print only even numbers-using list of comprehension
evens = [num for num in list2 if num % 2 == 0 ]
print(evens)
#Count how many numbers are greater than 10
largest = list2[0]
for num in list2:
    if num > largest:
        largest = num

print(largest)

#Count how many numbers are greater than 10-using list of comprehension  
above10 = [num for num in list2 if num > 10]

print(len(above10))

#Find the sum manually (NO sum())
subsidy = [20,10,23,34,12]

total_subsidy = 0

for amount in subsidy:
    total_subsidy += amount

print(total_subsidy)

#Find the largest number manually
largest_number = list2[0]
for n in list2:
    if n > largest_number:
        largest_number = amount

print(largest_number)


#Create a list of numbers
#Return a new list with only numbers > 5
numbers = [2,34,6,7,8,98,6,5,43,5,6,2,3,45,6,5]
above5 = [integer for integer in numbers if integer > 5]
print(above5)

#Convert all numbers to their square
numberz = []
for number in numbers:
    numberz.append(number ** 2)

print(numbers)
#Convert all numbers to their square-using list of comprehensions
squares = [digit ** 2 for digit in numbers]
print(squares)
  
#Replace all negative numbers with 0
negatives_list = [-23,-3,3,2,6,5,-2,-4,45,56,67]
negatives = [0 if dig < 0 else dig for dig in negatives_list]
print(negatives)

#Count how many times a number appears
#count of 2 in the list
count_two = len([numb for numb in numbers if numb == 2])
print(count_two)
#using the function count
numbers_to_count = 2
fcn_count_two = numbers.count(numbers_to_count)
print(fcn_count_two)

#create a function that returns only even numbers
def get_even_numbers(list_name):

    evens_list = [e for e in list_name if e % 2 == 0]
    return evens_list

#create safe average function
#Handle empty list safely
def safe_average(numbers):
    if len(numbers) == 0:
        return None
    
    list_sum = sum(numbers)
    list_count = len(numbers)
    average_result = list_sum / list_count
    return average_result

#data engineering simulation
orders = [100, 200, -50, 300, -20, 150]

#clean data; remove negative values
def cleaning_orders(orders):
    clean_orders = [order for order in orders if order > 0]
    return clean_orders

#Apply 10% tax to each value
def taxing_orders(clean_orders):
    tax = 0.1
    orders_after_tax = [(ord * (1 - tax)) for ord in clean_orders]
    return orders_after_tax

#total revenue
def revenue_calc(orders_after_tax):
    revenue = 0
    for od in orders_after_tax:
        revenue += od
        return revenue

#Count how many orders > 200
def ordersabove200(orders_after_tax):
    orders_above200 = [purchase for purchase in orders_after_tax if purchase > 200]
    return orders_above200

cleaned = cleaning_orders(orders)
after_tax = taxing_orders(cleaned)
revenue = revenue_calc(after_tax)
above_200 = ordersabove200(after_tax)

print("Cleaned orders: ",cleaned)
print("Orders after tax: ",after_tax)
print("Calculated revenue: ",revenue)
print("Orders above 200: ",above_200)



#Final pipeleine function
def process_orders(orders):
    clean_orders = [order for order in orders if order > 0]

    tax = 0.1
    orders_after_tax = [order * (1 - tax) for order in clean_orders]

    revenue = 0
    for order in orders_after_tax:
        revenue += order

    above_200 = [order for order in orders_after_tax if order > 200]

    return clean_orders, orders_after_tax, revenue, above_200

april_orders = [12,234,3,-45,56,-5,6,-7,300,900,2,34,56,678,2000,-678,65,34]

cleaned,after_tax,revenue,above_200 = process_orders(april_orders)

print("Cleaned orders: ",cleaned)
print("Orders after tax: ",after_tax)
print("Calculated revenue: ",revenue)
print("Orders above 200: ",above_200)