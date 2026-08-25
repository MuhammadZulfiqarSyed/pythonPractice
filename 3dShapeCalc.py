Pi = 3.142


def Calc_Cuboid():
    cuboid = "cuboid"  # assigns string name to variable
    base = "base"
    depth = "depth"
    height = "height"
    # gets the lengths after it has been input validated
    base = input_validation(base, cuboid)
    depth = input_validation(depth, cuboid)
    height = input_validation(height, cuboid)
    volume = round(base * depth * height, 2)  # calculates volume
    return volume  # sends volume back


def Calc_TriPrism():
    TriPrism = "triangular prism"  # assigns string name to variable
    base = "base"
    depth = "depth"
    height = "height"
    # gets the lengths after it has been input validated
    base = input_validation(base, TriPrism)
    depth = input_validation(depth, TriPrism)
    height = input_validation(height, TriPrism)
    volume = round(0.5 * base * depth * height, 2)  # calculates volume
    return volume  # sends volume back


def Calc_Sphere():
    sphere = "sphere"  # assigns string name to variable
    radius = "radius"
    # gets the lengths after it has been input validated
    radius = input_validation(radius, sphere)
    # calculates volume
    volume = round((4 / 3) * Pi * radius * radius * radius, 2)
    return volume  # sends volume back


def input_validation(side, shape):  # function to make sure the lengths are numbers
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
        volume = Calc_Cuboid()  # calculates cuboid and prints result
        print(f"The volume of the cuboid is {volume}")
    elif choice == "t":
        volume = Calc_TriPrism()  # calculates triangular prism and prints result
        print(f"The volume of the triangular prism is {volume}")
    elif choice == "s":
        volume = Calc_Sphere()  # calculates sphere and prints result
        print(f"The volume of the sphere is {volume}")
    elif choice == "q":
        print("quitting")  # quits program
        break
    else:  # asks the user to try again if input is incorrect
        print("Incorrect value entered, Choose from a, b or c. Please try again.")
