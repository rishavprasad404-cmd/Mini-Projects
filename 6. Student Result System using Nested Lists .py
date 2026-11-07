marks = [
    [83, 93, 84],
    [90, 99, 90],
    [85, 88, 80]
]
print("Marks Matrix = ",marks)

for rows in marks :
    for value in rows :
        print(value,end=" ")
    print()

print("Marks of Student 3 = ",marks[2])

print("Marks in Subject 3")
for rows in marks :
    print(rows[2])

marks [0] [0] = 83
print("After Updating")
print(marks)

highest = marks [0] [0]
for rows in marks :
    for value in rows :
        if value > highest :
            highest = value
print("Highest Marks = ",highest)