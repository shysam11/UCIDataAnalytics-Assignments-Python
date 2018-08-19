#Similar to Pybank but extra output requested on each candidates
#explicitly declare which modules
import os
import csv

# Path to collect data from the Pybank folder
file = os.path.join('..', "PyPoll", "election_data.csv")

#Initialize the variables
tot_votenum = 0
candlist=[]
pct_votes=[]
tot_votewon=0
winner=[]

 # Read CSV file
with open(file, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader, None)
    for row in csvreader:

    # Total number of votes
        tot_votenum += 1
   
    # Complete list of candidates who received votes
    #?????? Not sure how to get name once ??????
        candlist.append(row[2])


    # Percentage of votes each candidate won
        


# Specify the text file to write to
fileo = os.path.join('..', "PyPoll", "mainpypoll_out.txt")
with open(fileo, 'w', newline="") as textfile:
    #writer=csv.writer(textfile)
    textfile.write("Election Results \n")
    textfile.write("----------------------------- \n")
    textfile.write('Total votes: ' + str(tot_votenum) + "\n")
    textfile.write("----------------------------- \n")
    #Print out total votes won by each candidate
    #
    #
    textfile.write("----------------------------- \n")
    #Print out the winner
    textfile.write("----------------------------- \n")













