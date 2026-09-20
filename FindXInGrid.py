import random  # gets random

grid = [["" for i in range(5)] for i in range(5)]
# grid = [
#     ["", "", "", "", ""],
#     ["", "", "X", "", ""],
#     ["", "", "", "", ""],
#     ["", "", "", "", ""],
#     ["", "", "", "", ""],
# ]

# print(grid[2 - 1][3 - 1])


xaxis = 1
yaxis = 1

while xaxis == 1 and yaxis == 1:
    xaxis = random.randint(
        1, 5
    )  # gets random valuse between 1 and 5 for the x axis to put X in
    yaxis = random.randint(
        1, 5
    )  # gets random valuse between 1 and 5 for the y axis to put X in


grid[xaxis - 1][yaxis - 1] = "X"

# grid = [xaxis, yaxis]  # adds coordinate to grid


movesleft = 10  # gives the player 10 moves
xpos = 1  # sets start position to 1 in x axis
ypos = 1  # sets start position to 1 in y axis

print(
    "the X is in a random cell in the grid, you start at the top left, you need to find the X"
)
print("Input: w to go up, a to go left, s to go down, d to go right")

while True:
    move = input(
        "which move would you like to make (w/a/s/d): "
    ).lower()  # asks for which direction to move and makes it lower case
    if move in ["w", "a", "s", "d"]:
        if move == "w":  # if user inputted w
            if ypos == 1:  # checks if the player is trying to go out the border
                print("you cannot go out of the grid. Please try again")
                continue  # goes back to ask again
            ypos -= 1  # if everything goes well player is moved

        elif move == "a":
            if xpos == 1:
                print("you cannot go out of the grid. Please try again")
                continue
            xpos -= 1

        elif move == "s":
            if ypos == 5:
                print("you cannot go out of the grid. Please try again")
                continue
            ypos += 1

        elif move == "d":
            if xpos == 5:
                print("you cannot go out of the grid. Please try again")
                continue
            xpos += 1

        movesleft -= 1  # takes 1 away from movesleft
        if grid[xpos - 1][ypos - 1] == "X":  # checks if player in on X
            print("You Win")  # they win
            break  # ends
        if movesleft == 0:  # checks if player has run out of moves
            print("You Lose")  # they lose
            break  # ends

    else:
        print("Input (w/a/s/d). Please try again")
