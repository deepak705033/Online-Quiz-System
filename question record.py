import csv
Serial_No = int(input("Enter Sr.No: "))
Question = " Cursor is a ?"
A = "Pixel"
B = "Thin blinking line"
C = "black dot"
D = "Pointing device"
Answer = "D"

file =open("question.csv", "a", newline= "")

writer = csv.writer(file)
writer.writerow([
    Serial_No,
    Question,
    A,
    B,
    C,
    D,
    Answer
])
