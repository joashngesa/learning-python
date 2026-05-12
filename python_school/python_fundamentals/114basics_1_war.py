#Tests for pure fundamentals(lists and loops)
#1. Print all numbers
numbers = [12, 5, 8, 21, 3, 18, 7]
for num in numbers:
    print(num)

#2. Return only even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)

#3. Count numbers greater than 10
above_10 = 0
for num in numbers:
    if num > 10:
        above_10 += 1
print(above_10)

#4. Find sum manually
totals = 0
for num in numbers:
    totals += num
print(totals)

#5. Find largest number manually
largest_num = 0
for num in numbers:
    if num > largest_num:
        largest_num = num

print(largest_num)