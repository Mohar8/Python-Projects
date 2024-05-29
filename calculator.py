print("Welcome to the world of mathematics. Input numbers to work your way to the answer.", end="""

""")

def calculator():
    global num1
    global num2
    global result1
    num1 = int(input("Enter your first number: "))
    op = str(input("What is your operator? "))
    num2 = int(input("Enter your second number: "))
    if op == "+":
        result1 = num1 + num2

    elif op == "-":
        result1 = num1 - num2

    elif op == "*":
        result1 = num1 * num2

    elif op == "/":
        result1 = num1 / num2
    else:
        print("Invalid operator")
    print(result1)
calculator()

user_continue_or_no = input("Do you wish to continue? Write Y/N for yes/no : ").upper()

if user_continue_or_no == "Y":

    while user_continue_or_no != "N":

        op2 = str(input("Enter operator: "))
        num_new = int(input("Enter next number: "))
        if op2 == "+":
            result_new = result1 + num_new

        elif op2 == "-":
            result_new = result1 - num_new

        elif op2 == "*":
            result_new = result1 * num_new

        elif op2 == "/":
            result_new = result1 / num_new
        else:
            print("Invalid operator")
        result1 = result_new
        user_continue_or_no = input("Do you wish to continue? Write Y/N for yes/no : ").upper()
    print(result_new)

print("Thank you for using the calculator")