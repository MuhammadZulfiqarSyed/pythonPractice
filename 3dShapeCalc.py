import math  # imports math to get Pi


def Calc_Cuboid():
    cuboid = "cuboid"  # assigns string name to variable
    base = "base"
    depth = "depth"
    height = "height"
    # gets the lengths after it has been input validated
    base = input_validaiton(base, cuboid)
    depth = input_validaiton(depth, cuboid)
    height = input_validaiton(height, cuboid)
    area = round(base * depth * height, 2)  # calculates area
    return area  # sends area back


def Calc_TriPrism():
    TriPrism = "triangular prism"  # assigns string name to variable
    base = "base"
    depth = "depth"
    height = "height"
    # gets the lengths after it has been input validated
    base = input_validaiton(base, TriPrism)
    depth = input_validaiton(depth, TriPrism)
    height = input_validaiton(height, TriPrism)
    area = round(0.5 * base * depth * height, 2)  # calculates area
    return area  # sends area back


def Calc_Sphere():
    sphere = "sphere"  # assigns string name to variable
    radius = "radius"
    # gets the lengths after it has been input validated
    radius = input_validaiton(radius, sphere)
    # calculates area
    area = round((4 / 3) * round(math.pi, 3) * radius * radius * radius, 2)
    return area  # sends area back


def input_validaiton(side, shape):  # function to make sure the lengths are numbers
    while True:
        # gets length from user input
        inp = input(f"input the {side} length of the {shape}: ")
        if inp.isdigit():  # checks if the string is a number
            inp = float(inp)  # converts it to float for calculating
            return inp  # sends the length back
        else:  # asks the user to try again if input is incorrect
            print("incorrect value entered, must be a number. Please try again")
            continue


while True:
    # asks user what they want to do
    choice = input(
        "Do you want to calculate the volume of a Cuboid (c), Triangular Prism (t), Sphere (s), or stop the program (q). Pick (c/t/s/q)"
    ).lower()
    if choice == "c":
        area = Calc_Cuboid()  # calculates cuboid and prints result
        print(f"The area of the cuboid is {area}")
    elif choice == "t":
        area = Calc_TriPrism()  # calculates triangular prism and prints result
        print(f"The area of the triangular prism is {area}")
    elif choice == "s":
        area = Calc_Sphere()  # calculates sphere and prints result
        print(f"The area of the sphere is {area}")
    elif choice == "q":
        print("quitting")  # quits program
        break
    else:  # asks the user to try again if input is incorrect
        print("Incorrect value entered, Choose from a, b or c. Please try again.")
