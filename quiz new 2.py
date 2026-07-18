import csv
Name = input("Enter name: ")
Class = int(input("Enter class: "))
gender = input("Enter gender: ")
Ques_1 = "C"
Ques_2 = "A"
Ques_3 = "B"
Ques_4 = "D"
Ques_5 = "B"
Ques_6 = "B"
Ques_7 = "D"
Ques_8 = "A"
Ques_9 = "A"
Ques_10 ="D"

Obtained_marks = 5
Total_marks = 10

file = open("record.csv", "a", newline="")
writer = csv.writer(file)
writer.writerow([
    Name,
    Class,
    gender,
    Ques_1,
    Ques_2,
    Ques_3,
    Ques_4,
    Ques_5,
    Ques_6,
    Ques_7,
    Ques_8,
    Ques_9,
    Ques_10,
    Obtained_marks,
    Total_marks
])