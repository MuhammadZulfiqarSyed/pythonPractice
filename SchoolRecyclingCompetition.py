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


CombinedLists = list(
    zip(ItemsRecycled, StudentName)
)  # pairs elements with its corresponding one from the other list
SortedLists = sorted(CombinedLists, key=lambda x: x[0])  # sorts list
SortedNames = [item[1] for item in SortedLists]  # sorts list

SortedNames.reverse()  # reverses the order of the list
SortedItemsRecycled = ItemsRecycled.copy()  # copies items recycled to a new list
SortedItemsRecycled.sort(reverse=True)  # sorts list in descending order


for i in range(30):  # repeats for each student
    if SortedItemsRecycled[i] >= 100:  # checks if items recycled is 100 or above
        GoldAward.append(SortedNames[i])  # adds name to gold award list if 100 or above


print(
    f"The Recycling Champion is {SortedNames[0]} with {SortedItemsRecycled[0]} items recycled!"  # outputs first place
)
print(
    f"The Runner-up is {SortedNames[1]} with {SortedItemsRecycled[1]} items recycled!"  # outputs second place
)
print(
    f"{len(GoldAward)} Gold Certificates must be printed"
)  # outputs how many gold certificates to be printed
