while(True):
    print("---------------------------")
    print("Welcome to the Quiz System")
    print("---------------------------")
    print("Develop By Deepak")
    print("---------------------------")
    result = 0
    name = str(input("Enter your name: "))
    clas = int(input("Enter your class: "))

    if clas>=10:
        print()
        print("=============================================================")
        print("Congratulation.", name,"! You are eligible for amazing quiz.")
        print("=============================================================")
        print("Lets start..")
        y = ()
        n = ()
        print("Press Y for Start a quiz")
        print("Press N for Exit a quiz")
        click = str(input())
        if click=="y":
            print()
            print("All the Best", name,"! Ready for the questions")
            print()
            print("Ques-1: Computer is a ?")
            print("options: ")
            A = "System software"
            B = "Operating system"
            C = "Electronic device"
            D = "Applicaton software"
            print("A: ",A)
            print("B: ",B)
            print("C: ",C)
            print("D: ",D)
            x = str(input("Enter your answer = ")).upper()
            if x=="C":
                print(C, "is a correct answer")
                result+=1
            elif x=="B":
                print(B, "is a incorrect answer")
            elif x=="A":
                print(A, "is a incorrect answer")
            elif x=="D":
                print(D, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-2: Full Form of CPU is ?")
            print("Options: ")
            A = "Control Processing Unit"
            B = "Central Processing Unit"
            C = "Central Processing unity"
            D = "Common Operating System"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            a = str(input("Enter your answer = ")).upper()
            if a=="B":
                print(B, "is a correct answer")
                result+=1
            elif a=="A":
                print(A, "is a incorrect answer")
            elif a=="C":
                print(C, "is a incorrect answer")
            elif a=="D":
                print(D, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-3: Smallest unit of data in computer is ?")
            print("Options: ")
            A = "Byte"
            B = "Mega Byte"
            C = "Giga byte"
            D = "Bit"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            b = str(input("Enter your answer = ")).upper()
            if b=="D":
                print(D, "is a correct answer")
                result+=1
            elif b=="A":
                print(A, "is a incorrect answer")
            elif b=="B":
                print(B, "is a incorrect answer")
            elif b=="C":
                print(C, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-4: Full Form of RAM is ?")
            print("Options: ")
            A = "Read access memory"
            B = "Raghav access memory"
            C = "Random access memory"
            D = "rabbit control memory"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            c = str(input("Enter your answer = ")).upper()
            if c=="C":
                print(C, "is a correct answer")
                result+=1
            elif c=="A":
                print(A, "is a incorrect answer")
            elif c=="B":
                print(B, "is a incorrect answer")
            elif c=="D":
                print(D, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-5: Keyboard is a ?")
            print("Options: ")
            A = "Input device"
            B = "Output device"
            C = "Storage device"
            D = "Control device"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            d = str(input("Enter your answer = ")).upper()
            if d=="A":
                print(A, "is a correct answer")
                result+=1
            elif d=="B":
                print(B, "is a incorrect answer")
            elif d=="C":
                print(C, "is a incorrect answer")
            elif d=="D":
                print(D, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-6: Projector is a ?")
            print("Options: ")
            A = "Input device"
            B = "Output device"
            C = "Processing device"
            D = "Storage device"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            e = str(input("Enter your answer = ")).upper()
            if e=="B":
                print(B, "is a correct answer")
                result+=1
            elif e=="A":
                print(A, "is a incorrect answer")
            elif e=="C":
                print(C, "is a incorrect answer")
            elif e=="D":
                print(D, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-7: 1 GB =  ?")
            print("Options: ")
            A = "1000 B"
            B = "1028 MB"
            C = "1024 Byte"
            D = "1024 MB"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            f = str(input("Enter your answer = ")).upper()
            if f=="D":
                print(D, "is a correct answer")
                result+=1
            elif f=="A":
                print(A, "is a incorrect answer")
            elif f=="B":
                print(B, "is a incorrect answer")
            elif f=="C":
                print(C, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-8: Transform one interface into another interface ?")
            print("Options: ")
            A = "Adapter"
            B = "Data"
            C = "Program"
            D = "Coder"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            g = str(input("Enter your answer = ")).upper()
            if g=="B":
                print(B, "is a correct answer")
                result+=1
            elif g=="A":
                print(A, "is a incorrect answer")
            elif g=="C":
                print(C, "is a incorrect answer")
            elif g=="D":
                print(D, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-9: CRO stands for ?")
            print("Options: ")
            A = "Cathode ray oscilloscope"
            B = "Chief Risk system"
            C = "Cathode ray system"
            D = "Circle ray oscilloscope"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            h = str(input("Enter your answer = ")).upper()
            if h=="A":
                print(A, "is a correct answer")
                result+=1
            elif h=="B":
                print(B, "is a incorrect answer")
            elif h=="C":
                print(C, "is a incorrect answer")
            elif h=="D":
                print(D, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("Ques-10: Cursor is a ?")
            print("Options: ")
            A = "Pixel"
            B = "Thin blinking line"
            C = "black dot"
            D = "Pointing device"
            print("A: ", A)
            print("B: ", B)
            print("C: ", C)
            print("D: ", D)
            i = str(input("Enter your answer = ")).upper()
            if i=="D":
                print(D, "is a correct answer")
                result+=1
            elif i=="A":
                print(A, "is a incorrect answer")
            elif i=="B":
                print(B, "is a incorrect answer")
            elif i=="C":
                print(C, "is a incorrect answer")
            else:
                print("none.")
            print()
            print("====================================================")
            print("Thank you", name, "! For participating in quiz.")
            print("====================================================")
            print()
            print("--------------------------")
            print("Obtained Marks: ", result)
            print("Total: 10")
            print("---------------------------")
            print("-----------------------------------------------------------------------------------------------------------------")
        else:
            print(name, "You are not interested in Quiz")
            break
        print("---------------------------------------------------------------------------------------------------------------------")
    else:
        print("Sorry", name, "! You are not applicable for Quiz.")
        print("Thank You..")
    print("-------------------------------------------------------------------------------------------------------------------------")
