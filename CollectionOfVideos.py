import numpy as np

Video = [["", "", "", ""] for _ in range(10000)]
Results = []
n = 0
# a=[1,2,3]
# a[2]=4
# print(a)


def add_vid(n):
    while True:
        # restart = False
        VidTitle = input("What is the video title: ")
        if VidTitle == "":
            print("Incorrect input. Please try again.")
            continue
        break

        # for i in range(len(Video)):
        #     repeats = Video[i][0].count(VidTitle)
        #     if repeats == 20:
        #         restart = True
        #         print("Too many of the same title added (max 20). Please try again.")
        #     break

        # if restart:
        #     continue
        # break

    while True:
        VidFormat = input(
            "What is the video format. choose from 4K Blue-ray disc (a), standard Blu-ray disc (b), DVD (c), digital download (d). Pick (a/b/c/d): "
        ).lower()
        if VidFormat == "a":
            VidFormat = "4K Blue-ray disc"
            break
        elif VidFormat == "b":
            VidFormat = "standard Blu-ray disc"
            break
        elif VidFormat == "c":
            VidFormat = "DVD"
            break
        elif VidFormat == "d":
            VidFormat = "digital download"
            break
        else:
            print("Incorrect input. Please try again.")

    while True:
        VidRelease = input("What is the video release year: ")
        if VidRelease.isdigit():
            break
        print("Incorrect input. Please try again.")

    while True:
        VidStorage = input("What is the video storage code: ")
        if VidStorage == "":
            print("Incorrect input. Please try again.")
            continue
        break

    # Video.append([VidTitle, VidFormat, VidRelease, VidStorage])
    Video[n] = [VidTitle, VidFormat, VidRelease, VidStorage]
    n = n + 1


def find_vid(Results):
    while True:
        WhichVid = input("Which video whould you like to search for: ")
        if WhichVid == "":
            print("Incorrect input. Please try again.")
            continue
        values = np.array(Video)
        index = np.where(values == WhichVid)[0]
        if index.size == 0:
            print("Video name not found")
            return

        Results = [["", "", "", ""] for _ in range(20)]
        for i in range(20):
            Results[i] = Video[index[i]]
        print(Results)
        Results = []
        return Results


while True:
    choice = input(
        "Do you want to add a new video to the library (a), search for an existing video by title (b), or stop the program (c). Pick (a/b/c): "
    ).lower()
    if choice == "a":
        if n == 9999:
            print(
                "too many videos added (max 10,000 videos), please pick another option"
            )
        else:
            add_vid(n)
    elif choice == "b":
        find_vid(Results)
    elif choice == "c":
        print("stopping program")
        break
    else:
        print("Incorrect input. Please try again.")
