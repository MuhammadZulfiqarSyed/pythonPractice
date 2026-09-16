Teams = []
Results = []
Winners = []

for i in range(10):
    while True:
        name = input(f"what is team {i+1}'s name: ")
        if name == "":
            print("Please enter a name. Try again")
            continue
        Teams.append(name)
        break

while True:
    Played = input("input the number of games played: ")
    if not Played.isdigit():
        print("Please enter an integer. Try again")
        continue

    Played = int(Played)
    if Played < 1 or Played > 18:
        print("Please enter an integer between 1 and 18. Try again")
        continue
    break


for i in range(10):
    while True:
        gamesWon = input(f"input the number of games team {Teams[i]} won: ")
        if not gamesWon.isdigit():
            print("Please enter an integer. Try again")
            continue

        gamesWon = int(gamesWon)
        if gamesWon < 0 or gamesWon > Played:
            print(f"Please enter an integer between 1 and {Played}. Try again")
            continue
        break

    while True:
        gamesDrawn = input(f"input the number of games team {Teams[i]} drawn: ")
        if not gamesDrawn.isdigit():
            print("Please enter an integer. Try again")
            continue

        gamesDrawn = int(gamesDrawn)
        if gamesDrawn < 0 or gamesDrawn > (Played - gamesWon):
            print(
                f"Please enter an integer between 0 and {Played - gamesWon}. Try again"
            )
            continue
        break

    while True:
        gamesLost = input(f"input the number of games team {Teams[i]} lost: ")
        if not gamesLost.isdigit():
            print("Please enter an integer. Try again")
            continue

        gamesLost = int(gamesLost)
        if gamesLost < 0 or gamesLost > (Played - (gamesWon + gamesDrawn)):
            print(f"Please enter {Played - (gamesWon + gamesDrawn)}. Try again")
            continue
        break

    points = (gamesWon * 3) + gamesDrawn

    Results.append([gamesWon, gamesDrawn, gamesLost, points])


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

HighestNumberOfPoints = Results[0][3]
for i in range(len(Teams)):
    if Results[i][3] == HighestNumberOfPoints:
        Winners.append(Teams[i])

[print(f"The {Winners.index(x)+1} winner is {x}") for x in Winners]

# [p for y in fruits if "a" in y]

# for i in range(5):
#     print(i)

# a = ["k", "m", "s"]

# for i in a:
#     print(i)

# [print(f"the winner is {i}") for i in a]


# Get-Content test.txt | C:\Users\muham\AppData\Local\Microsoft\WindowsApps\python3.13.exe .\FootballTeamStatsTracker.py
