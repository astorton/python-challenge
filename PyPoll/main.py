#step 0: import the csv
import csv

#step 1: identify the csv path

csvfilepath = "Resources/election_data.csv"

#set the variables
total_vote_count = 0
candidate_names = []
candidate_dict = {}
winner = ""
winner_count = 0

#step 3: open the file and let's get started! 
with open(csvfilepath,mode='r',encoding='UTF-8') as csv_file:
    csv_data = csv.reader(csv_file,delimiter=',')

#print a list of all unique keys from the candidate dictionary
#sum each key's total votes (votes per candidate/total votes variable) and print both the count and as a percentage
#iterate through total votes counts and print the key associated with the highest count

    #Step 4: skip the headers for all iteration runs!
    headers = next(csv_data)

#iterate through the records to produce the total amount of votes
    for i in csv_data:
        total_vote_count = total_vote_count + 1
        candidate = i[2]
        #if the next record changes in candidate name, then procieed to add the candidate name to the candidate name list 
        if candidate not in candidate_names:
            candidate_names.append(candidate)
            #Add the new candidate's name as a key to the candidate dictionary with a baseline vote count of 0
            candidate_dict[candidate] = 0
        #continue adding votes until the next candidate name is identified or the iteration runs out
        candidate_dict[candidate] += 1
     
     #iterate through the newly created candidate dictionary and retrieve the value to evaulate which record contains the highest vote count produced from the previous iteration       
    for i in candidate_dict:
        candidate_votes_count = candidate_dict.get(i)
    
        if candidate_votes_count > winner_count:
            winner_count = candidate_votes_count
            #declare the winner of the most votes
            winner = i       
    
    #print print print!
    print("Election Results:")
    print("-----------------------")
    print(f"Total Votes {total_vote_count}")
    print("-----------------------")
    for i, k in candidate_dict.items():
        print(f"{i} {k} {round((k/total_vote_count),5)*100}%")
    print("-----------------------")
    print(f"Winner: {winner}")
    print("-----------------------")