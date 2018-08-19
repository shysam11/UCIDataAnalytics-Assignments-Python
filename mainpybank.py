
#explicitly declare which modules
import os
import csv

# Path to collect data from the Pybank folder
file = os.path.join('..', "Pybank", "budget_data.csv")

#Initialize variables
totalmonths = 0
total=0
grtinc=[]
grtdec=[]
grtincdt=[]
grtdecdt=[]
 # Read CSV file
with open(file, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader, None)
    for row in csvreader:

    # Total number of months
        totalmonths += 1
   
    # Total net amount of Profit/Loss over entire period
        total += int(row[1])

    # Average change in Profit/Loss between months over entire period
        avgchg = total / totalmonths 

    # Greatest increase in Profit date and amount over entire period
        grtinc.append(row[1])
        grtincdt.append(row[0])

    # Greatest decrease in Profit date and amount over entire period
        grtdec.append(row[1])
        grtdecdt.append(row[0])


    # Print out 
    #print(f"-----------------------------")
    #print(f"Total months:  {budget[0]}")
    #print(f"Total: {str(total)}")
    #print(f"Average Change: {str(avgchg)}")
    #print(f"Greatest Increase in Profits: {str(grtinc)}")
    #print(f"Greatest Decrease in Profits: {str(grtdec)}")



# Specify the text file to write to
fileo = os.path.join('..', "Pybank", "mainpybank_out.txt")
with open(fileo, 'w', newline="") as textfile:
    #writer=csv.writer(textfile)
    textfile.write("Financial Analysis \n")
    textfile.write("----------------------------- \n")
    textfile.write('Total months: ' + str(totalmonths) + "\n")
    textfile.write('Total: $' + str(total) + "\n")
    textfile.write('Average Change: $' + str(avgchg) + "\n")
    textfile.write('Greatest Increase in Profits: ' + str(grtincdt) + "($" + max(grtinc) + ")" + "\n")
    textfile.write('Greatest Decrease in Profits: ' + str(grtdecdt) + "($" + min(grtdec) +  ")" + "\n")












