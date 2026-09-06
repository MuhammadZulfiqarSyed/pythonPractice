<<<<<<< HEAD
def run_calculator():
    num1 = take_input("First")
    operand1 = num1

    num2 = take_input("Second")
    operand2 = num2

    decimal1 = binary_to_decimal(num1)
    decimal2 = binary_to_decimal(num2)

    operator, result = operation(decimal1, decimal2)
    Calc_History.append([operand1, operand2, operator, result])

    access_history(Calc_History)


def take_input(a):
    while True:
        # asks for first binary number
        num = input("input " + a + " binary number: ")
        accepted = True
        # checks if no value is entered
        if num != "":
            # loops over each digit in num1
            for bit in num:
                if bit != "0" and bit != "1":
                    #   if its not 0 AND not 1, its a bad bit so:
                    print("only 0s and 1s are allowed \n")
                    accepted = False
                    # breaks for loop, dont care about rest of bits
                    break
            # checks if its a good number, if all bits were good
            if accepted:
                # if all good indeed then it moves on
                return num
        else:
            print("no value entered")
            print("Try again")


def binary_to_decimal(binary_str):
    decimal = int(binary_str, 2)
    return decimal


def decimal_to_binary(decimal_num):
    binary = bin(decimal_num)[2:]
    return binary


def binary_add(d1, d2):
    d1plusd2 = d1 + d2
    result = decimal_to_binary(d1plusd2)
    print(result)
    return result


def binary_subtract(d1, d2):
    d1minusd2 = d1 - d2
    result = decimal_to_binary(d1minusd2)
    print(result)
    return result


def binary_multiply(d1, d2):
    d1timesd2 = d1 * d2
    result = decimal_to_binary(d1timesd2)
    print(result)
    return result


def binary_divide(d1, d2):
    d1divided2 = d1 // d2
    result = decimal_to_binary(d1divided2)
    print(result)
    return result


def operation(decimal1, decimal2):
    while True:
        operator = input(
            "which operator would you like? + for addition,- for subtraction, * for multiplication, / for division: "
        )

        if operator == "+":
            result = binary_add(decimal1, decimal2)
            break
        elif operator == "-":
            result = binary_subtract(decimal1, decimal2)
            break
        elif operator == "*":
            result = binary_multiply(decimal1, decimal2)
            break
        elif operator == "/":
            result = binary_divide(decimal1, decimal2)
            break
        else:
            print("please select one of the available characters")

    return operator, result


def access_history(Calc_History):
    while True:
        access_history_answer = input(
            "Would you like to access the history of your calculations? y/n: "
        ).lower()
        if access_history_answer == "y":
            print(Calc_History)
            while True:
                index_input = input("Which operation do you want? ")
                if index_input.isdigit():
                    index = int(index_input) - 1
                    if 0 <= index < len(Calc_History):
                        print(Calc_History[index])
                        return
                print("Please try again")
        elif access_history_answer == "n":
            print("Exiting Calculator History")
            return
        else:
            print("invalid input, try again")


Calc_History = []

print("Welcome to the Binary Calculator")
while True:
    start_calculator = input("Would you like to start the calculator? y/n: ").lower()
    if start_calculator == "y":
        while True:
            run_calculator()
            Continue = input("Would you like to continue calculating? y/n: ").lower()
            if Continue == "y":
                continue
            elif Continue == "n":
                print("Exiting Binary Calculator")
                break
            else:
                print("invalid input, try again")
        break
    elif start_calculator == "n":
        print("Exiting Binary Calculator")
        break
    else:
        print("invalid input, try again")
=======
def run_calculator():
    num1 = take_input("First")
    operand1 = num1

    num2 = take_input("Second")
    operand2 = num2

    decimal1 = binary_to_decimal(num1)
    decimal2 = binary_to_decimal(num2)

    operator, result = operation(decimal1, decimal2)
    Calc_History.append([operand1, operand2, operator, result])

    access_history(Calc_History)


def take_input(a):
    while True:
        # asks for first binary number
        num = input("input " + a + " binary number: ")
        accepted = True
        # checks if no value is entered
        if num != "":
            # loops over each digit in num1
            for bit in num:
                if bit != "0" and bit != "1":
                    #   if its not 0 AND not 1, its a bad bit so:
                    print("only 0s and 1s are allowed \n")
                    accepted = False
                    # breaks for loop, dont care about rest of bits
                    break
            # checks if its a good number, if all bits were good
            if accepted:
                # if all good indeed then it moves on
                return num
        else:
            print("no value entered")
            print("Try again")


def binary_to_decimal(binary_str):
    decimal = int(binary_str, 2)
    return decimal


def decimal_to_binary(decimal_num):
    binary = bin(decimal_num)[2:]
    return binary


def binary_add(d1, d2):
    d1plusd2 = d1 + d2
    result = decimal_to_binary(d1plusd2)
    print(result)
    return result


def binary_subtract(d1, d2):
    d1minusd2 = d1 - d2
    result = decimal_to_binary(d1minusd2)
    print(result)
    return result


def binary_multiply(d1, d2):
    d1timesd2 = d1 * d2
    result = decimal_to_binary(d1timesd2)
    print(result)
    return result


def binary_divide(d1, d2):
    d1divided2 = d1 // d2
    result = decimal_to_binary(d1divided2)
    print(result)
    return result


def operation(decimal1, decimal2):
    while True:
        operator = input(
            "which operator would you like? + for addition,- for subtraction, * for multiplication, / for division: "
        )

        if operator == "+":
            result = binary_add(decimal1, decimal2)
            break
        elif operator == "-":
            result = binary_subtract(decimal1, decimal2)
            break
        elif operator == "*":
            result = binary_multiply(decimal1, decimal2)
            break
        elif operator == "/":
            result = binary_divide(decimal1, decimal2)
            break
        else:
            print("please select one of the available characters")

    return operator, result


def access_history(Calc_History):
    while True:
        access_history_answer = input(
            "Would you like to access the history of your calculations? y/n: "
        ).lower()
        if access_history_answer == "y":
            print(Calc_History)
            while True:
                index_input = input("Which operation do you want? ")
                if index_input.isdigit():
                    index = int(index_input) - 1
                    if 0 <= index < len(Calc_History):
                        print(Calc_History[index])
                        return
                print("Please try again")
        elif access_history_answer == "n":
            print("Exiting Calculator History")
            return
        else:
            print("invalid input, try again")


Calc_History = []

print("Welcome to the Binary Calculator")
while True:
    start_calculator = input("Would you like to start the calculator? y/n: ").lower()
    if start_calculator == "y":
        while True:
            run_calculator()
            Continue = input("Would you like to continue calculating? y/n: ").lower()
            if Continue == "y":
                continue
            elif Continue == "n":
                print("Exiting Binary Calculator")
                break
            else:
                print("invalid input, try again")
        break
    elif start_calculator == "n":
        print("Exiting Binary Calculator")
        break
    else:
        print("invalid input, try again")
>>>>>>> 791c127e64287aa1ad0e890be8391c3a7404820b
