import os
import csv
with open('/Users/tanneramman/Downloads/election_data.csv', encoding='utf') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    
    csvHeader = next(csvFile)
    
    totalVotes = 0
    candidates = []
    voteCount = []
    candidateDict = {}
    maxVotes = 0
        
    for row in csvReader:
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidateDict[candidate] = 0
        if candidate in candidates:
            candidateDict[candidate] += 1
        totalVotes += 1

maxVotes = max(candidateDict, key = candidateDict.get)

outputFile = "PyPoll.txt"
with open(outputFile, "w") as txt_file:
    print("Election Results", file = txt_file)
    print("-" * 30, file = txt_file)
    print("Total Votes: " + str(totalVotes), file = txt_file)
    print("-" * 30, file = txt_file)
    for x in candidates:
        percentageVotes = round((candidateDict[x]/totalVotes) * 100, 3)
        print(f"{x}: {str(percentageVotes)}% ({str(candidateDict[x])})", file = txt_file)
    print("-" * 30, file = txt_file)
    print("Winner: " + maxVotes, file = txt_file)
    print("-" * 30, file = txt_file)       
