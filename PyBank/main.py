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
    #Initialize the variablle to calculate total profit/loss amount
    total_amount=0
    # initial chnage for first month
    previous_month_amount=0
    # list to hold all the values for monthly change
    monthly_changes_list=[]
    total_change=0
    date=[]
    
    #loop through the row in csv file
  
    for row in csvreader:
        #Increment the total month count for each row
        total_months+=1
        # Add profit  loss value to total amount
        total_amount +=int(row[1])
        date_value=(row[0])

        
        #profit_loss=int(row[1])
        if total_months >1:
            change=int(row[1])-previous_month_amount
            monthly_changes_list.append(change)
            date.append(date_value)
        previous_month_amount=int(row[1])
        
    total_change=sum(monthly_changes_list)
        
    average_change= round(total_change/ len(monthly_changes_list),2)

    monthly_increase=max(monthly_changes_list)
    monthly_increase_date=date[monthly_changes_list.index(monthly_increase)]
    monthly_decrease=min(monthly_changes_list)
    monthly_decrease_date=date[monthly_changes_list.index(monthly_decrease)]
    #Print the total number of months
    print("Total Months: " + str(total_months))
    #Print the total amount 
    print("Total: "+"$" +str(total_amount))
    print("Average Change: "+"$"+str(average_change))
    print("Greatest Increase in Profits: " + str(monthly_increase_date)+" "+"$"+str(monthly_increase))
    print("Greatest Decrease in Profits: " + str(monthly_decrease_date)+" "+"$"+str(monthly_decrease))



    


        
