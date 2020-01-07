# Dependencies
import os
import csv

# Variables for program
totalVotes = 0
khanVote = 0
correyVote = 0
liVote = 0
oTooleyVote = 0

# Function for printing summary of votes. Includes rounded percentage and total votes per candidate
def printSummary():
    print(f"Khan: {round((khanVote/totalVotes)*100)}.000% ({khanVote})")
    print(f"Correy: {round((correyVote/totalVotes)*100)}.000% ({correyVote})")
    print(f"Li: {round((liVote/totalVotes)*100)}.000% ({liVote})")
    print(f"O'Tooley: {round((oTooleyVote/totalVotes)*100)}.000% ({oTooleyVote})")

    # Writes summary to a file named output.txt
    f = open('output.txt', 'a')
    f.write(f"Khan: {round((khanVote/totalVotes)*100)}.000% ({khanVote})\n")
    f.write(f"Correy: {round((correyVote/totalVotes)*100)}.000% ({correyVote})\n")
    f.write(f"Li: {round((liVote/totalVotes)*100)}.000% ({liVote})\n")
    f.write(f"O'Tooley: {round((oTooleyVote/totalVotes)*100)}.000% ({oTooleyVote})\n")
    f.close()

# Function for determining winner by checking vote counts against each other
def printWinner():
    winner = ""

    if oTooleyVote > khanVote and oTooleyVote > correyVote and oTooleyVote > liVote:
        winner = "oTooley"
    elif khanVote > oTooleyVote and khanVote > correyVote and khanVote > liVote:
        winner = "Khan"
    elif liVote > oTooleyVote and liVote > correyVote and liVote > khanVote:
        winner = "Li"
    elif correyVote > oTooleyVote and correyVote > liVote and correyVote > khanVote:
        winner = "Correy"
    print("------------------")
    print(f"Winner: {winner}")
    print("------------------")

    # Writes summary to a file named output.txt
    f = open('output.txt', 'a')
    f.write("------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("------------------\n")
    f.close()

# Path to data in csv file
voterDataPath = os.path.join("Resources", "election_data.csv")

# Reads through csv to acquire data for program
with open(voterDataPath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvReader:
        totalVotes += 1
        if row[2] == "Khan":
            khanVote += 1
        elif row[2] == "Correy":
            correyVote += 1
        elif row[2] == "Li":
            liVote += 1
        elif row[2] == "O'Tooley":
            oTooleyVote += 1

# Prints final summary of election results
print("Election Results")
print("------------------")
print(f"Total Votes: {totalVotes}")

# Prints final summary results header and votes to a file named output.txt
f = open('output.txt', 'a')
f.write("Election Results\n")
f.write("------------------\n")
f.write(f"Total Votes: {totalVotes}\n")
f.close()

printSummary()
printWinner()