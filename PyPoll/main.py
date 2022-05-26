from logging.config import valid_ident
import os
import csv
from telnetlib import theNULL

election_csv = os.path.join("Resources", "election_data.csv")
Election_Result = os.path.join("Analysis", "election_Result.txt")
candidates = []
with open(os.path.abspath(election_csv)) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)

    #track our candidates in a dictionary
    
    #while looping through rows keep track of votes for later
    totalVotes = int(0)
    for row in csv_reader:
        #use the variable found to flag if we need to add a candidate to the dictionary or not
        found = False
        totalVotes = totalVotes + 1
        #if we dont have any candidates to start, proceed to adding the first one
        if len(candidates) > 0:
            for subrow in candidates:
                #while looping through our candidates we check the name is present and then  pdate the candidates votes if a match is found
                if subrow["Name"] == row[2]:
                    #if we find a match ensure we change our flag to prevent trying to add new candidate
                    found = True
                    subrow["Total"] = subrow["Total"] + 1 
        #If we have 0 candidates to start or we couldnt find a matcon names in our dictionary, we add them here
        if found == False:
            candidate = {
                "Name" : row[2],
                "Total" : 1
                }
            candidates.append(candidate)

    print('Election Results')
    print('----------------------')
    print(f'Total Votes: {totalVotes}')
    print("----------------------")
    #loop through our dictionary one more time to calculate percentages from our candidates totals in the previous loop
    Winner = str('')
    Max = int(0)
    for row in candidates:
        #Find the maximum vote while calculateing the percentage of each votes and track the name
        if Max < row["Total"]:
            Max = row["Total"]
            Winner = row["Name"]
        #output the percentage votes along other details  as we loop
        print(f'{row["Name"]}: {round((row["Total"] / totalVotes) * 100, 3)}% ({row["Total"]})')
 
    #output the winners name obtained from the previos for loop
    print('----------------------')
    print(f'Winner: {Winner}')

    #I tried to create the text file with the result but was not able to  - thge code is below 

    #with open(Election_Result, "w") as txt_file:
        #Election_Result = (
           # f"\'Election Results\n"
           # f"----------------------\n"
            #f"f'Total Votes: {totalVotes}\n"
           # f"----------------------\n")
       # txt_file.write(Election_Result)
        #for row in candidates:
            #Find the maximum vote while calculateing the percentage of each votes and track the name
           # if Max < row["Total"]:
              #  Max = row["Total"]
              #  Winner = row["Name"]
            #output the percentage votes along other details  as we loop
       # Percentage = (
       # f"{row["Name"]}: {round((row["Total"] / totalVotes) * 100, 3)}% ({row["Total"]}\n"
       # f"----------------------\n")
       # txt_file.write(Percentage) 
       # Winner =(f'Winner: {Winner}')
      #  txt_file.write(Winner) 
       



#print(candidates)
#   for row in candidates