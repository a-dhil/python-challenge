#step 1 import necessary modules
import os 
import csv

#step2 store the file path associated with file
csvpath=os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
#Step3.1 to write text file specify the path
output_path=os.path.join("..", "PyBank", "Analysis", "analysis.txt")
#step3.2 open output file
output_file=open(output_path, "w")

#step 4 open the file in read mode and store/assign the content in variable csvfile
with open(csvpath) as csvfile:

    #step5 it creates csvreader object and specifies the delimited . Delemiter is used to specify how the values in CSV file are seperated from each other.
    #csvreader is not  a list it is an object that knows how to read data from CSV file
    csvreader=csv.reader(csvfile,delimiter=',')

    #it prints the CSV reader object
    #print(csvreader)

    #step 6 it reads the first line of csvreader and assign it to variable csv_header and initializing next row
    csv_header=next(csvreader)

    # it prints the csv header
    #print(f"CSV Header: {csv_header}")

    #step 7 print the heading
    print("Financial Analysis")
    print("-----------------------")
    #step3.3 write in outputfile the print statements
    output_file.write("Financial Analysis\n")
    output_file.write("--------------------------\n")

    #Step 8 Initialize the variable to count the months
    total_months=0
    #Step 9 Initialize the variablle to calculate total profit/loss amount
    total_amount=0
    #Step 10 initial change for first month which will be zero
    previous_month_amount=0
    # Step 11 list to hold all the values for monthly change
    monthly_changes_list=[]
    #Step 12 initialize empty list to hold the value fo date and month for the change
    date=[]
    
    #Step 13 loop through the row in csv file
  
    for row in csvreader:
        #Step 14 Increment the total month count for each row
        total_months+=1
        # Step 15 Add profit  loss value to total amount
        total_amount +=int(row[1])
        # Step 16 To get date value from row
        date_value=(row[0])

        # Step 17 Calculate the change in profit loss which will be zero for first month, as there is no change
        if total_months >1:
            change=int(row[1])-previous_month_amount
            # Step 18 add change values to monthly change list and date list
            monthly_changes_list.append(change)
            date.append(date_value)
        # Step 19 Update previous value amount to current value for next iteration
        previous_month_amount=int(row[1])
    #Step 20 Total change will be the sum of  monthly chnage list values  
    total_change=sum(monthly_changes_list)
    # Step 21 Calculate the average by dividing total changes by the number of chnages   
    average_change= round(total_change/ len(monthly_changes_list),2)
    #Step 22 Find the biggest increase and decrease in profits with min and max function with thier respective dates.
    monthly_increase=max(monthly_changes_list)
    monthly_increase_date=date[monthly_changes_list.index(monthly_increase)]
    monthly_decrease=min(monthly_changes_list)
    monthly_decrease_date=date[monthly_changes_list.index(monthly_decrease)]
    #Step  23 Print the total number of months
    print("Total Months: " + str(total_months))
    #Print the total amount 
    print("Total: "+"$" +str(total_amount))
    # print the average change
    print("Average Change: "+"$"+str(average_change))
    # print increase and decrease values
    print("Greatest Increase in Profits: " + str(monthly_increase_date)+" "+"("+"$"+str(monthly_increase)+")")
    print("Greatest Decrease in Profits: " + str(monthly_decrease_date)+" "+"("+"$"+str(monthly_decrease)+")")

    #step3.4 write in output file the print statement
   
    output_file.write("Total Months: " + str(total_months)+"\n")
    output_file.write("Total: "+"$" +str(total_amount)+"\n")
    output_file.write("Average Change: "+"$"+str(average_change)+"\n")
    output_file.write("Greatest Increase in Profits: " + str(monthly_increase_date)+" "+"("+"$"+str(monthly_increase)+")"+"\n")
    output_file.write("Greatest Decrease in Profits: " + str(monthly_decrease_date)+" "+"("+"$"+str(monthly_decrease)+")"+"\n")

#step3.5 need to close write mode file as it was not opened "with" mode
output_file.close()

    


        
