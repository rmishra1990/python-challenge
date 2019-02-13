import os
import csv

csvpath = os.path.join('../..', 'Instructions','PyPoll','Resources', 'election_data.csv')
output_path = os.path.join('../..', 'Instructions','PyPoll','Output', 'output_pypoll.csv')

#Initialize votes counter variable
total_votes = 0

#Create lists/dictionaries to store data
candidate_options =[]
candidate_votes =[]
percent_votes =[]


with open(csvpath, newline="") as election:
   csvreader = csv.reader(election, delimiter=",") 
   csv_header = next(csvreader)
   for row in csvreader:
       total_votes = total_votes + 1
       #Get the name of the candidate from each row
       candidate_name = row[2]
       #If it does not match any existing candidate during the loop, add to the list and track number of votes
       if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           index = candidate_options.index(candidate_name)
           candidate_votes.append(1)
       else:
           index = candidate_options.index(row[2]) 
           candidate_votes[index] +=1
    #Find the percentages       
   for votes in candidate_votes:
        percentage = (votes/total_votes)*100
        percentage = round(percentage)
        percentage ="%.3f%%" % percentage
        percent_votes.append(percentage)
    #Find the winning candidate
        winner = max(candidate_votes)
        index = candidate_votes.index(winner)
        winning_candidate = candidate_options[index]

with open(output_path, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")       
       
    # Save the final vote count to the text file
    txt_file.write(election_results)  

    for i in range(len(candidate_options)):
        num_votes = (f"{candidate_options[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})\n")  
        print(num_votes)
        line =str(f"{candidate_options[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")

    # Save the candidate votes and percentages to the text file
        txt_file.write('{}\n'.format(line))

    #Print the winner results
    winner_results = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winner_results)

    # Save the candidate votes and percentages to the text file
    txt_file.write(winner_results)        
   

