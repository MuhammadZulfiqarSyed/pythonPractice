import random as r


def enterName(num):
    player = input(f"Whats player {num}'s name: ")
    while player == "":
        print("Please input name again: ")
        player = input(f"Whats player {num}'s name: ")
    return player


def generateAndStore():
    num1 = r.randint(1, 6)
    num2 = r.randint(1, 6)

    # 3 4 = score2=2 PASS
    # 4 3 = score1=2
    # 3 3 = both = 1

    global score1
    global score2

    if num1 > num2:
        score1 += 2
    elif num2 > num1:
        score2 += 2
    else:
        score1 += 1
        score2 += 1

    NumberGenerated[0].append(num1)
    NumberGenerated[1].append(num2)
    return score1, score2


player1 = enterName(1)
player2 = enterName(2)
NumberGenerated = [[], []]

score1 = 0
score2 = 0
for i in range(100):
    generateAndStore()

while True:
    if score1 > score2:
        winner = 1
        break
    elif score2 > score1:
        winner = 2
        break
    else:
        generateAndStore()

print(
    f"{player1 if winner == player1 else player2} is the winner with a score of {score1 if winner == 1 else score2} points"
)
print(
    f"{player1 if winner != player1 else player2} is in 2nd place with a score of {score1 if winner != 1 else score2} points"
)
