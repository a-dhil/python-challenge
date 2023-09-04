#step 1 import necessary modules
import os 
import csv

#step 2 store the file path associated with file
csvpath=os.path.join('..','PyPoll', 'Resources', 'election_data.csv')
#Step 3.1 to write text file specify the path
output_path=os.path.join("..", "PyPoll", "Analysis", "analysis.txt")
#step 3.2 open output file
output_file=open(output_path, "w")

#step 4 open the file in read mode and store/assign the content in variable csvfile
with open(csvpath) as csvfile:

    #step 5 it creates csvreader object and specifies the delimited . Delemiter is used to specify how the values in CSV file are seperated from each other.
    #csvreader is not  a list it is an object that knows how to read data from CSV file
    csvreader=csv.reader(csvfile,delimiter=',')

    

    #step 6 it reads the first line of csvreader and assign variable csv_header and initializing next row
    csv_header=next(csvreader)

    #step 7 print the heading
    print("Election Results")
    print("--------------------------")
    #step 3.3 write in outputfile the print statements
    output_file.write("Election Results\n")
    output_file.write("--------------------------\n")

    #step 8 create variable and dictionary
    total_votes=0
    candidates_votes={}
    # step 9 the loop iterates through each row of csvreader
    for row in csvreader:
        candidate_name=row[2]
        #step 10 condition statement check the vote count of each candidate if name already exists it increment the vote count, if not initialize the vote count to 1
        if candidate_name in candidates_votes:
            candidates_votes[candidate_name]+=1
        else:
            candidates_votes[candidate_name]=1

       #step 11 calculating total votes
        total_votes+=1

    #step 12 print the heading
    print("Total Votes: " + str(total_votes))
    print("------------------------")
    #step 3.4  convert print statement to output.writer
    output_file.write("Total Votes: " + str(total_votes)+"\n")
    output_file.write("------------------------\n")

    #step 13 create new dictionary vote_percentages using disctionary comprehension
    #candidate_name: (vote_count / total_votes) * 100 key value pair inside  dictionary comprehension
    #loop helps to extract candidate_name and vote_count in candidates_votes dictionary
    #.items() is a method to iterate over the items of dictionary
    vote_percentages = {candidate_name: (vote_count / total_votes) * 100 for candidate_name, vote_count in candidates_votes.items()}

    #step 14 loop to iterate through vote percent dictionary
    for candidate_name, vote_percentage in vote_percentages.items():
        # step 15 print print candidate name with vote percent and total no of candidate votes
        print(f"{candidate_name}: {vote_percentage:.3f} % ({candidates_votes[candidate_name]})")
        #step 3.5 convert print statement for analysis text file
        output_file.write(f"{candidate_name}: {vote_percentage:.3f} % ({candidates_votes[candidate_name]})"+"\n")
    
    #step 16 determine the winner
    max_votes = max(candidates_votes.values())
    winning_candidates = [candidate for candidate, votes in candidates_votes.items() if votes == max_votes]

    #step 17 print the winner
    print("------------------------")
    print(f"Winner: {winning_candidates[0]}")
    print("------------------------")
    #step 3.6 print the output for analysis text file use write object
    output_file.write("------------------------\n")
    output_file.write(f"Winner: {winning_candidates[0]}"+"\n") 
    output_file.write("------------------------\n")

#step 3.7 need to close write mode file as it was not opened "with" mode
output_file.close()

    
  
       
   
    
    


    


        
