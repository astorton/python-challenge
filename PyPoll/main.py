import csv

#step 1: identify the csv path

csvfilepath = "Resources/election_data.csv"

vote_count = 0
candidate_dict = {}

#Open the file and let's get started! 
with open(csvfilepath,mode='r',encoding='UTF-8') as csv_file:
    csv_data = csv.reader(csv_file,delimiter=',')

#print a list of all unique keys from the candidate dictionary
#sum each key's total votes (votes per candidate/total votes variable) and print both the count and as a percentage
#iterate through total votes counts and print the key associated with the highest count

    #Step 0: Skip the headers for all iteration runs!
    headers = next(csv_data)

    for i in csv_data:
        vote_count = vote_count + 1
        candidate = i[2]
        candidate_vote_count = 0
        if candidate not in candidate_dict:
            candidate_dict[candidate],[candidate_vote_count] = i[2], candidate_vote_count +1

    print(f"Total Votes {vote_count}")
    print(f"Unique candidates from dictionary: {candidate_dict}")