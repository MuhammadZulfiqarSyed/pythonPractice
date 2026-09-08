StudentName = [f"student {sn + 1}" for sn in range(30)]  # adds students 1-30
ItemsRecycled = []
GoldAward = []

# uncomment the code below if you want to input student names yourself
# StudentName.clear() #clears all student names from before
# for i in range(30): #repeats for each student
#     while True: #starts a loop
#         name = input(f"enter student {i + 1}'s name: ") #asks for student names
#         if name == "": #checks if user input a name
#             print("Please input a name. Try again") #asks user to try again if no name is input
#             continue #restarts loop
#         StudentName.append(name) #adds student name to list
#         break #exits loop


for i in range(30):  # repeats for each student
    while True:  # starts loop
        NumberOfItemsRecycled = input(
            f"Enter the number of items student {i+1} has recycled: "  # asks for items recycled
        )
        if NumberOfItemsRecycled.isdigit():  # checks if number input is a number
            NumberOfItemsRecycled = int(NumberOfItemsRecycled)  # makes it an integer
            if 0 <= NumberOfItemsRecycled <= 500:  # checks it it is between 0 and 500
                ItemsRecycled.append(NumberOfItemsRecycled)  # adds it to the list
                break  # exits loop
        print(
            "Please input an integer between 0 and 500. Try again"
        )  # asks user to try again if incorrect value is entered

# Bubble sort
# a full pass
# "MISTAKE IN LINE 9, what is it?"
# implement, swapping a parallel array
n = len(ItemsRecycled)
for i in range(n - 1):
    for j in range(n - i - 1):
        if ItemsRecycled[j] > ItemsRecycled[j + 1]:
            ItemsRecycled[j], ItemsRecycled[j + 1] = (
                ItemsRecycled[j + 1],
                ItemsRecycled[j],
            )
            StudentName[j], StudentName[j + 1] = StudentName[j + 1], StudentName[j]

StudentName.reverse()
ItemsRecycled.reverse()


for i in range(30):  # repeats for each student
    if ItemsRecycled[i] >= 100:  # checks if items recycled is 100 or above
        GoldAward.append(StudentName[i])  # adds name to gold award list if 100 or above


print(
    f"The Recycling Champion is {StudentName[0]} with {ItemsRecycled[0]} items recycled!"  # outputs first place
)
print(
    f"The Runner-up is {StudentName[1]} with {ItemsRecycled[1]} items recycled!"  # outputs second place
)
print(
    f"{len(GoldAward)} Gold Certificates must be printed"
)  # outputs how many gold certificates to be printed
