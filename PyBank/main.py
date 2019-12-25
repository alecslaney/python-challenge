import os
import csv

months = 0
profitLoss = 0
totalProfitLoss = 0
profitLossList = []
changeAverage = []

#Average Change function
def average(numbers):
    length = len(numbers)
    numbersSum = 0.0
    for number in numbers:
        numbersSum += number
    return numbersSum / length

def change(myList):
    lengthList = len(myList)
    i = 1
    while i < lengthList: 
        change = int(int(myList[i]) - int(myList[i - 1]))
        changeAverage.append(change)
        i += 1

#Path to data in csv file
budgetDataPath = os.path.join("Resources", "budget_data.csv")

with open(budgetDataPath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    #Store and skip header
    csvHeader = next(csvfile)
    for row in csvReader:
        profitLoss = int(row[1])
        profitLossList.append(row[1])
        totalProfitLoss += profitLoss
        months += 1

change(profitLossList)

# Printing summary of data
print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")
print(f"Total: ${totalProfitLoss}")
print(f"Average Change: ${round(average(changeAverage), 2)}")