print("*"*25,"Simple Calculator","*"*25)
name = input("Enter your name : ")
print("Hello,",name,"!")

#adding the two numbers
def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}.")

#substracting the twom numbers
def sub(a,b):
    print(f"Substraction of {a} and {b} is {a-b}.")

#multiplication of the two numbers
def mul(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}.")

#division
def div(a,b):

    #validation of dinaminator
    if b == 0 :
        print("The dinaminater is not equal to zero ")
    else:
        print(f"Division of {a} and {b}  is {a/b}")
    

#The main funtion starts here
while True:
    print("_"*50)
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit")
    
    try:
        #taking the user option
        option = int(input("Enter your choice: "))

    except ValueError:
        print("Please Enter valid option .")
    
    match option:
        case 1:
            try:
                #taking numbers from user
                a = int(input("Enter your frist number : "))
                b = int(input("Enter your second number : "))
            except ValueError:
                print("Enter only numbers.")
            add(a,b)
        
        case 2:
            try:
                #taking numbers from user
                a = int(input("Enter your frist number : "))
                b = int(input("Enter your second number : "))
            except ValueError:
                print("Enter only numbers.")
            sub(a,b)
        case 3:
            try:
                #taking numbers from user
                a = int(input("Enter your frist number : "))
                b = int(input("Enter your second number : "))
            except ValueError:
                print("Enter only numbers.")
            mul(a,b)
        case 4:
            try:
                #taking numbers from user
                a = int(input("Enter your frist number : "))
                b = int(input("Enter your second number : "))
            except ValueError:
                print("Enter only numbers.")
            div(a,b)
        case 5:
            print("Thanks for using our calculator app.")
            break
    
    

