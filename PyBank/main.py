import os
import csv
with open('/Users/tanneramman/Downloads/budget_data.csv', encoding='utf') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    
    csvHeader = next(csvFile)
    
    totalMonths = 0
    totalNet = 0
    change = 0
    changes = []
    greatestIncrease = 0
    greatestDecrease = 0
    previousNet = 0
    giDate = ""
    gdDate = ""
    
    for row in csvReader:
        totalMonths += 1
        totalNet += int(row[1])
        change = int(row[1])-previousNet
        changes.append(change)
        if change > greatestIncrease:
            greatestIncrease = change
            giDate = row[0]
        if change < greatestDecrease:
            greatestDecrease = change
            gdDate = row[0]
        previousNet = int(row[1])
    
    del(changes[0])
    averageChange = round(sum(changes)/len(changes), 2)
    
outputFile = "PyBank.txt"
with open(outputFile, "w") as txt_file:    
    print("Financial Analysis", file = txt_file)
    print("-" * 30, file = txt_file) 
    print("Total Months: " + str(totalMonths), file = txt_file)     
    print("Total: $" + str(totalNet), file = txt_file)
    print("Average Change: $" + str(averageChange), file = txt_file)
    print(f"Greatest Increase in Profits: {giDate} (${str(greatestIncrease)})", file = txt_file)
    print(f"Greatest Decrease in Profits: {gdDate} (${str(greatestDecrease)})", file = txt_file)
    
