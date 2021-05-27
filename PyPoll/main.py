#import file
import os
import csv

#filepath
election_file = os.path.join(os.getcwd(),'Resources','election_data.csv')

#initialize variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#create the loop
with open(election_file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #skip header row
    csv_header = next(csvfile)
    
    #loop through data for total_votes
    for row in csvreader:
        total_votes += 1
        #calculate votes for each candidate
        if (row[2] == 'Khan'):
            khan_votes +=1
        elif (row[2] == 'Correy'):
            correy_votes += 1
        elif (row[2] == 'Li'):
            li_votes += 1
        else:
            otooley_votes += 1
            
    #show number of votes as percentages
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    #calculate the winner
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)
    
    if winner == khan_votes:
        winner_name = 'Khan'
    elif winner == correy_votes:
        winner_name = 'Correy'
    elif winner == li_votes: 
        winner_name = 'Li'
    else:
        winner_name = "O'Tooley"
        
#To terminal
print(f'Election Results')
print(f'*****************************')
print(f'Total Votes: {total_votes}')
print(f'*****************************')
print(f'Khan: {khan_percent:%}({khan_votes})')
print(f'Correy: {correy_percent:%}({correy_votes})')
print(f'Li: {li_percent:%}({li_votes})')
print(f"O'Tooley: {otooley_percent:%}({otooley_votes})")
print(f'*****************************')
print(f'Winner: {winner_name}')
print(f'Congratulations, {winner_name}!!!')    


#write to text file
output_file = os.path.join('election_data_final.text')

with open(output_file, 'w') as txtfile:
    txtfile.write(f'Election Results\n')
    txtfile.write(f'*****************************\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write(f'*****************************')
    txtfile.write(f'Khan: {khan_percent:%}({khan_votes})\n')
    txtfile.write(f'Correy: {correy_percent:%}({correy_votes})\n')
    txtfile.write(f'Li: {li_percent:%}({li_votes})\n')
    txtfile.write(f"O'Tooley: {otooley_percent:%}({otooley_votes})\n")
    txtfile.write(f'*****************************\n')
    txtfile.write(f'Winner: {winner_name}\n')
    txtfile.write(f'Congratulations, {winner_name}!!!\n')
    
