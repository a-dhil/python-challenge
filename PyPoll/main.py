#step 1 import necessary modules
import os 
import csv

#step2 store the file path associated with file
csvpath=os.path.join('..','PyPoll', 'Resources', 'election_data.csv')
#Step1.1 to write text file specify the path
output_path=os.path.join("..", "PyPoll", "Analysis", "analysis.txt")
#step1.2 open output file
output_file=open(output_path, "w")

#step 3 open the file in read mode and store/assign the content in variable csvfile
with open(csvpath) as csvfile:

    #step4 it creates csvreader object and specifies the delimited . Delemiter is used to specify how the values in CSV file are seperated from each other.
    #csvreader is not  a list it is an object that knows how to read data from CSV file
    csvreader=csv.reader(csvfile,delimiter=',')

    

    #step 5 it reads the first line of csvreader and assign it to variable csv_header
    csv_header=next(csvreader)

    print("Election Results")
    print("--------------------------")
    #step1.3 write in outputfile the print statements
    output_file.write("Election Results\n")
    output_file.write("--------------------------\n")

    total_votes=0
    candidates_votes={}
    
    for row in csvreader:
        candidate_name=row[2]

        if candidate_name in candidates_votes:
            candidates_votes[candidate_name]+=1
        else:
            candidates_votes[candidate_name]=1

       
        total_votes+=1
    
    print("Total Votes: " + str(total_votes))
    print("------------------------")
    #step1.4  convert print statement to output.writer
    output_file.write("Total Votes: " + str(total_votes)+"\n")
    output_file.write("------------------------\n")

    vote_percentages = {candidate_name: (vote_count / total_votes) * 100 for candidate_name, vote_count in candidates_votes.items()}
    for candidate_name, vote_percentage in vote_percentages.items():
        print(f"{candidate_name}: {vote_percentage:.3f} % ({candidates_votes[candidate_name]})")
        #step1.5 convert print statement
        output_file.write(f"{candidate_name}: {vote_percentage:.3f} % ({candidates_votes[candidate_name]})"+"\n")
    
    max_votes = max(candidates_votes.values())
    winning_candidates = [candidate for candidate, votes in candidates_votes.items() if votes == max_votes]

    print("------------------------")
    print(f"Winner: {winning_candidates[0]}")
    print("------------------------")
    #step 1.6
    output_file.write("------------------------\n")
    output_file.write(f"Winner: {winning_candidates[0]}"+"\n") 
    output_file.write("------------------------\n")

output_file.close()

    
  
       
   
    
    


    


        
