print("*"*25,"Simple Calculator","*"*25)
name = input("Enter your name : ")
print("Hello,",name,"!")

number1 , number2 = int(input("Enter your frist number : ")), int(input("Enter your second number : "))

print(
    "1.Additon",
    "2.Substraction",
    "3.Multiplication",
    "4.division",
    sep="\n"
)

option = int(input("Enter your choice :  "))
match option:
    case 1:
        print(f"Additon of {number1} and {number2} is {number1 + number2}")
    case 2:
        print(f"Substraction of {number1} and {number2} is {number1 - number2}")
    case 3:
        print(f"Multiplication of {number1} and {number2} is {number1 * number2}")
    case 4:
        print(f"Division of {number1} and {number2} is {number1/number2}")

