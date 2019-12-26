import os
import csv

months = 0
profitLoss = 0
totalProfitLoss = 0
greatestDecrease = 0
greatestIncrease = 0
greatestDecreaseDate = "blank"
greatestIncreaseDate = "blank"
dateList = []
profitLossList = []
changeAverage = []

# Calculates average for given input (list)
def average(numbers):
    length = len(numbers)
    numbersSum = 0
    for number in numbers:
        numbersSum += number
    return numbersSum / length

# Calculates value of change in profit/loss between months and stores in a list
def averageChange(numbers, dates):
    global greatestDecrease, greatestIncrease
    length = len(numbers)
    i = 1
    while i < length:
        change = int(int(numbers[i]) - int(numbers[i - 1]))
        changeAverage.append(change)
        if change < 0:
            if change < greatestDecrease:
                #print(dates[i])
                greatestDecrease = change
                greatestDecreaseDate == dates[i]
        elif change > 0:
            if change > greatestIncrease:
                greatestIncrease = change
                greatestIncreaseDate == dates[i]
        i += 1
        
# Path to data in csv file
budgetDataPath = os.path.join("Resources", "budget_data.csv")

with open(budgetDataPath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    # Store and skip header
    csvHeader = next(csvfile)
    for row in csvReader:
        dateList.append(row[0])
        profitLossList.append(row[1])
        profitLoss = int(row[1])
        totalProfitLoss += profitLoss
        months += 1

averageChange(profitLossList, dateList)
#print(f"{dateList}")

# Printing summary of data
print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalProfitLoss}")
print(f"Average Change: ${round(average(changeAverage), 2)}")
print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})")