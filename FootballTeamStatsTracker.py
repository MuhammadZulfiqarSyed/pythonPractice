Teams = []
Results = []
Winners = []

for i in range(10):  # repeats for each team
    while True:
        name = input(f"what is team {i+1}'s name: ")  # asks for team name
        if name == "":  # if no name is entered
            print("Please enter a name. Try again")
            continue  # restarts and asks again
        Teams.append(name)  # adds team name to list Teams
        break

while True:
    Played = input(
        "input the number of games played: "
    )  # asks for number of games played
    if not Played.isdigit():  # if not a number
        print("Please enter an integer. Try again")
        continue  # restarts and asks again

    Played = int(Played)  # turns Played into an integer
    if Played < 1 or Played > 18:  # if under 1 or over 18
        print("Please enter an integer between 1 and 18. Try again")
        continue  # restarts and asks again
    break


for i in range(10):
    while True:
        gamesWon = input(
            f"input the number of games team {Teams[i]} won: "
        )  # asks for games won
        if not gamesWon.isdigit():  # if not a number
            print("Please enter an integer. Try again")
            continue  # restarts and asks again

        gamesWon = int(gamesWon)  # makes gamesWon into an integer
        if (
            gamesWon < 0 or gamesWon > Played
        ):  # if less than 0 or more than games played
            print(f"Please enter an integer between 1 and {Played}. Try again")
            continue  # restarts and asks again
        break

    while True:
        gamesDrawn = input(
            f"input the number of games team {Teams[i]} drawn: "
        )  # asks for games drawn
        if not gamesDrawn.isdigit():  # iuf not a number
            print("Please enter an integer. Try again")
            continue  # restarts and asks again

        gamesDrawn = int(gamesDrawn)  # makes gamesDrawn into an integer
        if gamesDrawn < 0 or gamesDrawn > (
            Played - gamesWon
        ):  # if less than 0 or more than games left
            print(
                f"Please enter an integer between 0 and {Played - gamesWon}. Try again"
            )
            continue  # restarts and asks again
        break

    while True:
        gamesLost = input(
            f"input the number of games team {Teams[i]} lost: "
        )  # asks for games lost
        if not gamesLost.isdigit():  # if not a number
            print("Please enter an integer. Try again")
            continue  # restarts and asks again

        gamesLost = int(gamesLost)  # makes gamesLost into an integer
        if gamesLost < 0 or gamesLost > (
            Played - (gamesWon + gamesDrawn)
        ):  # if less than 0 or bigger than games left
            print(f"Please enter {Played - (gamesWon + gamesDrawn)}. Try again")
            continue  # restarts and asks again
        break

    points = (gamesWon * 3) + gamesDrawn  # calculates points

    Results.append([gamesWon, gamesDrawn, gamesLost, points])  # adds it to results


# Bubble sort
n = len(Teams)  # assigns list length to name
for i in range(n - 1):  # repeats list length - 1 times
    for j in range(n - i - 1):  # repeats list length - i - 1 times
        if (
            Results[j][3] < Results[j + 1][3]
        ):  # if before value is greater than after value
            Results[j], Results[j + 1] = (
                Results[j + 1],
                Results[j],
            )  # value switch
            Teams[j], Teams[j + 1] = (
                Teams[j + 1],
                Teams[j],
            )  # value switch

HighestNumberOfPoints = Results[0][
    3
]  # checks how many points team with most amount of points has
for i in range(len(Teams)):  # for each team
    if (
        Results[i][3] == HighestNumberOfPoints
    ):  # if team has same amount of points as highest
        Winners.append(Teams[i])  # adds it to Winners

[print(f"The {Winners.index(x)+1} winner is {x}") for x in Winners]  # lists winners

# [p for y in fruits if "a" in y]

# for i in range(5):
#     print(i)

# a = ["k", "m", "s"]

# for i in a:
#     print(i)

# [print(f"the winner is {i}") for i in a]


# Get-Content test.txt | C:\Users\muham\AppData\Local\Microsoft\WindowsApps\python3.13.exe .\FootballTeamStatsTracker.py
