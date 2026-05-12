#create tables
#print all rows

students = [
    [1,"Austin",88],
    [2,"Mwas",70],
    [3,"Franky",61],
    [4,"Benja",69],
    [5,"Rowena",85],
    [6,"Cindy",88],
    [7,"Cliff",25],
    [7,"Sygil",36],
    [8,"Enoch",68]
]

for row in students:
    print(row)

#print names only
for row in students:
    print(row[1])

#Print only scores
for now in students:
    print(row[2])

#Return students with score > 75
above_75 = []
for row in students:
    if row[2] > 75:
        above_75.append(row)


#Count how many students scored below 80
below_80 = 0
for row in students:
    if row[2] < 80:
        below_80 += 1

print(below_80)

#Increase all scores by 5%(prints the whole table)
#Create a new list with updated scores (don’t modify original)
score_increase = 0.05
inc_students = []
for row in students:
    new_row =[row[0], row[1], round(row[2] * (1 + score_increase))]
    inc_students.append(new_row)
for row in students:
    print(row)
