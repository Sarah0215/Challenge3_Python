import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Lists to store data, and initialize the variables
date=[]
Profit_Loss=[]
Change_PL=[0]

# Define the function for count the data records
def count_csv_records(budget_data):
    date = str(budget_data[0])
    with open(budget_csv,'r') as file:
        reader = csv.reader(file)
        header =next(reader)
        row_count=sum(1 for row in reader)
    return row_count

#Define the function to calculate the Total profit and Loss
def Sum_Total_PL(budget_data):
    with open(budget_csv,"r") as file:
        reader = csv.reader(file,delimiter=",")
        header=next(reader)
        for row in reader:
            #Add date
            date.append(row[0])

            #Add profit_loss
            Profit_Loss.append(int(row[1]))

            #Sum the profit and Loss
            Total_PL=sum(Profit_Loss)

    return Total_PL

#Define the function to calculate the change and greatest increase and decrease
def Calc_Change(budget_data):
    with open(budget_csv,"r") as file:
        reader = csv.reader(file,delimiter=",")
        header=next(reader)
        for row in range(row_count):    
             
            if row > 0:

                #Calc change over the period
                Change_PL.append(Profit_Loss[row]-Profit_Loss[row-1])

                #Get the total change
                Total_change= sum(Change_PL)

                #Get the greatest increase in profits 
                max_change = max(Change_PL)
                max_index=Change_PL.index(max_change)
                max_date=date[max_index]

                #Get the greatest decrease in profit 
                min_change =min(Change_PL)
                min_index=Change_PL.index(min_change)
                min_date=date[min_index]

    return Total_change, max_change,max_date,min_change,min_date

row_count=count_csv_records(budget_csv)
Total_amount=Sum_Total_PL(budget_csv)
Total_Change,max_change,max_date,min_change,min_date=Calc_Change(budget_csv)

#Print the analysis to the terminal with newlines for readability 

print("Financial Analysis\n----------------------------") 
print("Total Months:",row_count)
print(f"Total: ${int(Total_amount)}")
print(f"Average Change: ${round(Total_Change / (row_count-1),2)}")
print(f"Greatest Increase in Profits: {max_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_date} (${min_change})\n")

# Set the path for the output file 
output_path = os.path.join("analysis", "financial_analysis.txt") 

# Open the output file and write the analysis with newlines 
with open(output_path, "w") as txt_file: 
    txt_file.write("Financial Analysis\n----------------------------\n") 
    txt_file.write(f"Total Months:{row_count}\n") 
    txt_file.write(f"Total: ${int(Total_amount)}\n") 
    txt_file.write(f"Average Change: ${round(Total_Change / (row_count-1),2)}\n") 
    txt_file.write(f"Greatest Increase in Profits: {max_date} (${max_change})\n") 
    txt_file.write(f"Greatest Decrease in Profits: {min_date} (${min_change})\n")