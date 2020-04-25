import random


x = input("Would you like to rolle the die y or n \n")

while x == 'y':

 number = random.randint(1,6) #Number needs to be inside the loop so it can generate repeatabily 

 if number == 1:
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")

 if number == 2:
        print("----------")
        print("|        |")
        print("|   0 0  |")
        print("|        |")
        print("----------")
    

 if number == 3:
        print("----------")
        print("|    0   |")
        print("|    0   |")
        print("|    0   |")
        print("----------")
    
 if number == 4:
        print("----------")
        print("|  0   0 |")
        print("|        |")
        print("|  0   0 |")
        print("----------")

 if number == 5:
        print("----------")
        print("|  0   0 |")
        print("|    0   |")
        print("|  0   0 |")
        print("----------")
    
 if number == 6:
        print("----------")
        print("|  0   0 |")
        print("|  0   0 |")
        print("|  0   0 |")
        print("----------")

 x = input("Would you like to roll again?\n")


print("Goodbye")