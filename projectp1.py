Practical01:Program Demonstrating control statements


print("Welcome to the quiz")
playing=input("Do you want to play?")
if playing != "yes":
    quit()
print("okay let's play!!")
points=0
answer=input("What does CPU stands for?")
if answer == "central processing unit":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("Who is known as the father of computer")
if answer == "Dennis Richie":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("What is the brain of a computer system called?")
if answer == "CPU":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("What is the fullform of RAM?")
if answer == "Random Access Memory":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("Fullform of ALU?")
if upper.answer() == "Arithmatic Logical Unit":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("Fullform of ROM?")
if answer == "Read Only Memory":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("Smallest unit of memory?")
if answer == "Bit":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("What does SSD stands for?")
if answer == "Solid state Drive":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("Is printer input or output device?")
if answer == "Output":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()

answer=input("Which is the current version of windows")
if answer == "Windows11":
    print("Corret!")
    points=points+1
else :
    print("Incorrect !")
    print(points)
    quit()
print(points)