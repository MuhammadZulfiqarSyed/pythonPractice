MemberID = []
Name = [[], []]


def take_member_code():
    while True:
        NewID = input("Enter your membership code: ")
        if len(NewID) == 6 and NewID.isalnum():
            if NewID in MemberID:
                print("Membership code already exists. Please try again.")
                continue
            if len(MemberID) > 1000:
                print(
                    "Maximum number of members reached. Cannot accept new membership code."
                )
                continue
            MemberID.append(NewID)
            print("Membership code accepted.")
            break
        print("Invalid membership code. Please try again.")


def take_name(a):
    while True:
        Name = input("Enter your " + a + " name: ")
        if Name.isalpha():
            print("Name accepted.")
            break
        print("Invalid " + a + " name. Please try again.")
    return Name


def add_new_member():
    take_member_code()

    Name1 = take_name("first")
    Name[0].append(Name1)

    Name2 = take_name("last")
    Name[1].append(Name2)


while True:
    choice = input(
        "Do you want to input a new member, output a list of membership codes and names, or exit. (a/b/c): "
    ).lower()
    if choice == "a":
        add_new_member()
        continue
    elif choice == "b":
        print("Membership Codes and Names:")
        for i in range(len(MemberID)):
            print(f"{MemberID[i]}: {Name[0][i]} {Name[1][i]}")
        continue
    elif choice == "c":
        confirm = input("are you sure you want to exit? y/n: ").lower()
        if confirm == "y":
            print("Exiting the program.")
            break
    else:
        print("Invalid choice. Please try again.")
