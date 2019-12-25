import os
import csv

months = 0

#Path to data in csv file
budgetDataPath = os.path.join("Resources", "budget_data.csv")

with open(budgetDataPath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    #Store and skip header
    csvHeader = next(csvfile)
    for row in csvReader:
        months += 1

# Printing summary of data
print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")