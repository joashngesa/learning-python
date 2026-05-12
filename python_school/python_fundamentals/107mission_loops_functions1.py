#Write functions that:
#return all odd numbers
#return all numbers above 50
#return squares of all numbers
#return sum of numbers manually
#return largest number manually
numbers = [12,34,56,78,12,234,456,789,-22,-34,-4565,100,345,34,123,34,456]

#return all odd numbers
def odd_numbers(numbers):
    odds = []
    for number in numbers:
        if number % 2 != 0:
            odds.append(number)
    return odds

odd_num = odd_numbers(numbers)
print(odd_num)


#return all numbers above 50
def num_above50(numbers):
    above50 = []
    for a in numbers:
        if a > 50:
            above50.append(a)
    return above50

numbers_above50 = num_above50(numbers)
print(numbers_above50)

#return squares of all numbers
def square_numbers(numbers):
    squares = []
    for sqr in numbers:
        squares.append(sqr ** 2)
    return squares

square_num = square_numbers(numbers)
print(square_num)
    
#return sum of numbers manually
def numbers_sum(numbers):
    totals = 0
    for tot in numbers:
        totals += tot
    return totals

numbers_total = numbers_sum(numbers)
print(numbers_total)

#return largest number manually
def largest_number(numbers):
    largest_num = numbers[0]
    for lar in numbers:
        if lar > largest_num:
            largest_num = lar
    return largest_num

largest_num = largest_number(numbers)
print(largest_num)

print(max(numbers))