#step 1 import necessary modules
import os 
import csv

#step2 store the file path associated with file
csvpath=os.path.join('..','PyBank', 'Resources', 'budget_data.csv')

#step 3 open the file in read mode and store/assign the content in variable csvfile
with open(csvpath) as csvfile:

    #step4 it creates csvreader object and specifies the delimited . Delemiter is used to specify how the values in CSV file are seperated from each other.
    #csvreader is not  a list it is an object that knows how to read data from CSV file
    csvreader=csv.reader(csvfile,delimiter=',')

    #step 5 it prints the CSV reader object
    #print(csvreader)

    #step 6 it reads the first line of csvreader and assign it to variable csv_header
    csv_header=next(csvreader)

    #step 7 it prints the csv header
    #print(f"CSV Header: {csv_header}")

    #print the heading
    print("Financial Analysis")
    print("-----------------------")

    #Initialize the variable to count the months
    total_months=0
    total_amount=0
    
    #loop through the row in csv file
    for row in csvreader:
        #Increment the total month count for each row
        total_months+=1
        total_amount +=int(row[1])

    #Print the total number of months
    print("Total Months: " + str(total_months))
    print("Total: "+"$" +str(total_amount))

   
    


        
