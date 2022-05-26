from logging.config import valid_ident
import os
import csv

# field names 
fields = ['date' 'Profit_losses']

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(os.path.abspath(budget_csv)) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #print(budget_csv)

    csv_header = next(csv_reader)
    #print(f"header: {csv_header}")

    #total = 0 
    data = []
    for row in csv_reader:
        #rows.append(row)
        #print(row)
        data.append(row)
       
    print(f'total number of months: {len(data)}')

    #The net total amount of "Profit/Losses" over the entire period

    i = int(0)
    for row in data:
        i = i + int(row[1])

    print(f'net total amount of profit\loss {i}')

#The average of the changes in "Profit/Losses" over the entire period

    change = int(0)
    prev = int(0)
    first = bool(True)
    min = int(0)
    minDate = str("")
    max = int(0)
    maxDate = str("")
    for row in data:
        val = int(row[1])
        if first == False:
            change = change + (val - prev)
            if min > (val - prev):
                min = (val - prev)
                minDate = str(row[0])
            if max < (val - prev):
                max = (val - prev)
                maxDate = str(row[0])
        prev = val
        first = False
        
    print(f'Average change: {change / (len(data) - 1)}')
    print(f'Greatest Increase in Profits:  {maxDate} ({max})')
    print(f'Greatest Decrease in Profits:  {minDate} ({min})')


       

   

#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period





