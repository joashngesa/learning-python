#Write functions that:
#return all odd numbers
#return all numbers above 50
#return squares of all numbers
#return sum of numbers manually
#return largest number manually
numbers = [12,34,56,78,12,234,456,789,-22,-34,-4565,100,345,34,123,34,456]

#return all odd numbers
def odd_numbers(numbers):

    odds = [num for num in numbers if num % 2 != 0]
    return odds

odd_numbs = odd_numbers(numbers)
print(odd_numbs)

#remove all negative numbers
def positive_numbers(numbers):

    positives = [pos for pos in numbers if pos > 0]
    return positives

positive_numbs = positive_numbers(numbers)
print(positive_numbs)

#return all numbers 50
def above_50(numbers):

    num_above50 = [abv for abv in numbers if abv > 50]
    return num_above50

num_above_50 = above_50(numbers)
print(num_above_50)

#return squares of all numbers

def square_numbers(numbers):

    squares = [sqr ** 2 for sqr in numbers]
    return squares

square_numb = square_numbers(numbers)
print(square_numb)

#return sum of numbers manually
