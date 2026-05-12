#Print all names
students = [
    [1, "Austin", 88],
    [2, "Mwas", 70],
    [3, "Franky", 61],
    [4, "Benja", 69],
    [5, "Rowena", 85]
]

for tutee in students:
    print(tutee[1])

#Return students with score > 75
above_75 = [tutee for tutee in students if tutee[2] > 75]
print(above_75)

#Count students below 70
below_70 = 0
for tutee in students:
    if tutee[2] < 70:
        below_70 += 1
print(below_70)

#Calculate average score manually
total_scores = 0
if len(students) == 0:
        average_score = 0
else:
        for tutee in students:
            total_scores += tutee[2]

average_score = total_scores / len(students)
print(average_score)

#Create a NEW table with scores increased by 10%
increased_scores = []
increase_rate = 0.1
for tutee in students:
    inc_row = [tutee[0], tutee[1], round(tutee[2] * (1 + increase_rate),2)]
    increased_scores.append(inc_row)

print(increased_scores)
print(students)
