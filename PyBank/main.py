# Dependencies
import os
import csv

# Variables for program
months = 0
profitLoss = 0
totalProfitLoss = 0
dateList = []
profitLossList = []
changeList = []

# Calculates average for given input (list)
def average(numbers):
    length = len(numbers)
    numbersSum = 0
    for number in numbers:
        numbersSum += number
    return numbersSum / length

# Calculates value of change in profit/loss between months and stores in a list
def averageChange(numbers, dates):
    length = len(numbers)
    maxDecrease = 0
    maxIncrease = 0
    decreaseDate = ""
    increaseDate = ""
    i = 1
    while i < length:
        change = int(int(numbers[i]) - int(numbers[i - 1]))
        changeList.append(change)
        if change < 0:
            if change < maxDecrease:
                maxDecrease = change
                decreaseDate = dates[i]
        elif change > 0:
            if change > maxIncrease:
                maxIncrease = change
                increaseDate = dates[i]
        i += 1
    print(f"Average Change: ${round(average(changeList), 2)}")
    print(f"Greatest Increase in Profits: {increaseDate} (${maxIncrease})")
    print(f"Greatest Decrease in Profits: {decreaseDate} (${maxDecrease})")
    
    # Continues to print summary data to a file named output.txt
    f = open('output.txt', 'a')
    f.write(f"Average Change: ${round(average(changeList), 2)}\n")
    f.write(f"Greatest Increase in Profits: {increaseDate} (${maxIncrease})\n")
    f.write(f"Greatest Decrease in Profits: {decreaseDate} (${maxDecrease})\n")
    f.close()

# Prints summary of data when called
def printSummary():
    f = open('output.txt', 'a')
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${totalProfitLoss}")
    
    # Prints summary to a file named output.txt
    f = open('output.txt', 'a')
    f.write("Financial Analysis\n")
    f.write("------------------\n")
    f.write(f"Total Months: {months}\n")
    f.write(f"Total: ${totalProfitLoss}\n")
    f.close()
    
    averageChange(profitLossList, dateList)

# Path to data in csv file
budgetDataPath = os.path.join("Resources", "budget_data.csv")

# Reads through csv to acquire data for program
with open(budgetDataPath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvReader:
        dateList.append(row[0])
        profitLossList.append(row[1])
        profitLoss = int(row[1])
        totalProfitLoss += profitLoss
        months += 1

# Prints summary of the data
printSummary()