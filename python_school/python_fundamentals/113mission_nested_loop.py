
students = [
    [1,"Austin",88],
    [2,"Mwas",70],
    [3,"Franky",61],
    [4,"Benja",69],
    [5,"Rowena",85],
    [6,"Cindy",88],
    [7,"Cliff",-25],
    [7,"Sygil",-36],
    [8,"Enoch",68]
]
#cleane data
def process_students(students):
    cleaned_tbl = [row for row in students if row[2] > 0]
            
#updated scores(2%)
    updated_scores = []
    scores_adjustment = 0.02
    for row in cleaned_tbl:
        new_row =row[0], row[1], round(row[2] * (1 + scores_adjustment))
        updated_scores.append(new_row)
#total_scores                           
    total_scores = 0
    for row in updated_scores:
        total_scores += row[2]
#high-scoring students > 75
    high_scorers = [row for row in updated_scores if row[2] > 75]
    

    return cleaned_tbl, updated_scores, total_scores, high_scorers

cleaned_tbl, updated_scores, total_scores, high_scorers = process_students(students)

print("Cleaned table: ",cleaned_tbl)
print("Updated scores: ",updated_scores)
print("total scores: ",total_scores)
print("High scores: ",high_scorers)


