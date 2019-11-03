import os
import csv

csvpath = "py-bank.csv"
csvwrite = "bank1.txt"

total_net = 0 
totalmonths = 0
month = 0 
net_change_list = []
#for every row, net change is calculated:
#use if statements to find max/min? w/ correct index ranges:
increase = [0, 0]
decrease = [0, 99999999]

with open(csvpath, newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader) 
    first_row = next(reader)
    total_net += int(first_row[1])
    previousmonth = int(first_row[1])


    for row in reader:
        #net total''''''''''''''''''''' 
        total_net = total_net + int(row[1])

        #total months'''''''''''''''''''''''
        #month = list(reader)
        #totalmonths = len(month) + 1

        #average of changes''''''''''''
        net_change = int(row[1]) - previousmonth
        net_change_list = net_change_list + [net_change]

        if net_change > increase[1]: 
            increase[0] = row[0]
            increase[1] = net_change
        if net_change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_change

average_of_changes = sum(net_change_list) / len(net_change_list) 
        
finalized = ( 
    f"\nFinancial Analysis\n"
    f"-------------------------------------\n"
    #f"Total Months: {totalmonths}\n"
    f"Net Total: ${total_net}\n"
    f"Average Change: ${average_of_changes}\n"
    f"Greatest Increase: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease: {decrease[0]} (${decrease[1]})\n"
)

print(finalized)

with open("bankpy1.txt", "w", newline="") as txt_file:
    txt_file.write(finalized)