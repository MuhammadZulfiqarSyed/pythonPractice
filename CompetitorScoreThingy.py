CompetitorName = []
CompetitorScore = []
numOfPlayers = 2
for i in range(numOfPlayers):  # adds numOfPlayers sublist
    CompetitorScore.append([])
Points = []
values = [[], [], [], [], []]
value1 = []
value2 = []
value3 = []
value4 = []
value5 = []


def add_competitor_name():
    for i in range(numOfPlayers):  # repeats numOfPlayers times
        # name = input(f"Enter competitor {i+1} name: ")  # asks for name
        CompetitorName.append(f"member {i+1}")  # adds name to CompetitorName list


def add_competitor_scores(a, n):
    # adds the scores to the CompetitorScore list,
    # checks that the value entered is correct
    while True:
        score = input(
            f"enter score for event {a}, competitor {n} (0-100 pts): "
        )  # asks for score for each competitor for each event
        if score.isnumeric():  # check is score is a number
            score = int(score)  # makes score and integer
            if 0 <= score <= 100:  # checks if score is between 0 and 100
                CompetitorScore[n - 1].append(score)
                # adds the scores to separate lists based on their event
                eval(f"value{a}").append(CompetitorScore[n - 1][a - 1])
                values[a - 1].append(CompetitorScore[n - 1][a - 1])
                # adds score to CompetitorScore list
                return
            else:
                print(
                    "Incorrect value entered, it must be between 0 and 100. Please try again."
                )
        else:
            print("Incorrect value entered, it must be a number. Please try again")


add_competitor_name()

for i in range(
    5
):  # gets scores for numOfPlayers competitors for 5 rounds each #ERRORS HERE
    print(f"event {i+1}")
    for j in range(numOfPlayers):  # gets score for each competitor for each event
        add_competitor_scores(i + 1, j + 1)

for i in range(numOfPlayers):  # adds up 5 scores to one total for each competitor
    pT = sum((CompetitorScore[i]))
    Points.append(pT)  # adds total score to Points list


highestT = max(Points)  # prints which competitor got the highest total
index = Points.index(highestT)
print(
    f"{CompetitorName[index]} got the most amount of points! They got {highestT} points!"
)

# prints which competitors got the highest points from separate events

highest1 = max(value1)
index = value1.index(highest1)  # for event 1
# index1=values[0].index(highest1)
print(
    f"{CompetitorName[index]} got the most amount of points in event 1! They got {highest1} points!"
)
# print(f"{CompetitorName[index1]} got the most amount of points in event 1!")


highest2 = max(value2)
index = value2.index(highest2)  # for event 2
# index2=values[1].index(highest2)
print(
    f"{CompetitorName[index]} got the most amount of points in event 2! They got {highest2} points!"
)
# print(f"{CompetitorName[index2]} got the most amount of points in event 2!")

highest3 = max(value3)
index = value3.index(highest3)  # for event 3
# index3=values[2].index(highest3)
print(
    f"{CompetitorName[index]} got the most amount of points in event 3! They got {highest3} points!"
)
# print(f"{CompetitorName[index3]} got the most amount of points in event 3!")

highest4 = max(value4)
index = value4.index(highest4)  # for event 4
# index4=values[3].index(highest4)
print(
    f"{CompetitorName[index]} got the most amount of points in event 4! They got {highest4} points!"
)
# print(f"{CompetitorName[index4]} got the most amount of points in event 4!")

highest5 = max(value5)
index = value5.index(highest5)  # for event 5
# index5=values[4].index(highest5)
print(
    f"{CompetitorName[index]} got the most amount of points in event 5! They got {highest5} points!"
)
# print(f"{CompetitorName[index5]} got the most amount of points in event 5!")
