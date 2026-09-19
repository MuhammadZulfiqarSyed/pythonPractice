import random  # gets random

xaxis = random.randint(
    1, 5
)  # gets random valuse between 1 and 5 for the x axis to put X in
yaxis = random.randint(
    1, 5
)  # gets random valuse between 1 and 5 for the y axis to put X in
grid = [xaxis, yaxis]  # adds coordinate to grid
movesleft = 10  # gives the player 10 moves
xaxis = 1  # sets start position to 1 in x axis
yaxis = 1  # sets start position to 1 in y axis
retry = False  # sets false to retry
won = False  # sets false to won
print(
    "the X is in a random cell in the grid, you start at the top left, you need to find the X"
)
print("Input: w to go up, a to go left, s to go down, d to go right")

while True:
    move = input(
        "which move would you like to make (w/a/s/d): "
    ).lower()  # asks for which direction to move and makes it lower case
    if move == "w":  # if user inputted w
        if yaxis == 1:  # checks if the player is trying to go out the border
            print("you cannot go out of the grid. Please try again")
            continue  # goes back to ask again
        yaxis -= 1  # if everything goes well player is moved
        if xaxis == grid[0] and yaxis == grid[1]:  # checks if player in on X
            print("You Win")  # they win
            break  # ends
        movesleft -= 1  # takes 1 away from movesleft
        if movesleft == 0:  # checks if player has run out of moves
            print("You Lose")  # they lose
            break  # ends

    elif move == "a":
        if xaxis == 1:
            print("you cannot go out of the grid. Please try again")
            continue
        xaxis -= 1
        if xaxis == grid[0] and yaxis == grid[1]:
            print("You Win")
            break
        movesleft -= 1
        if movesleft == 0:
            print("You Lose")
            break

    elif move == "s":
        if yaxis == 5:
            print("you cannot go out of the grid. Please try again")
            continue
        yaxis += 1
        if xaxis == grid[0] and yaxis == grid[1]:
            print("You Win")
            break
        movesleft -= 1
        if movesleft == 0:
            print("You Lose")
            break

    elif move == "d":
        if xaxis == 5:
            print("you cannot go out of the grid. Please try again")
            continue
        xaxis += 1
        if xaxis == grid[0] and yaxis == grid[1]:
            print("You Win")
            break
        movesleft -= 1
        if movesleft == 0:
            print("You Lose")
            break
    else:
        print("Input (w/a/s/d). Please try again")
