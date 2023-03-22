import csv

#step 1: identify the csv path

csvfilepath = "Resources/budget_data.csv"

#Establish the known lists for use in iteration runs
total_pl = []
total_months = []
monthly_profit_delta = []

#Open the file and let's get started! 
with open(csvfilepath,mode='r',encoding='UTF-8') as csv_file:
    csv_data = csv.reader(csv_file,delimiter=',')

    #Step 0: Skip the headers for all iteration runs!
    headers = next(csv_data)
    
    #Step 1: print count of total, non-header records
    #months_count = str((len(list(csv_data))))

    #Step 2: Pull csv_data values and push to lists that will be used for iteration runs

    for record in csv_data:
        total_months.append(record[0])
         #This help will calculate net total P/L over ENTIRE period
        total_pl.append(int(record[1]))
          
    #Step 3: Gather monthly change in profit(s)
    for record in range(len(total_pl)-1):
        monthly_profit_delta.append(total_pl[record+1]-total_pl[record])

#Step 4: Pull out the respective min/max decrease and increase from the monthly_profit_delta list
min_value = min(monthly_profit_delta)
max_value = max(monthly_profit_delta)

#Step 5: Using index method() - assign the month variable with the min/max value of the delta list based on the relative min/max values 
min_value_month = monthly_profit_delta.index(min(monthly_profit_delta))
max_value_month = monthly_profit_delta.index(max(monthly_profit_delta))

total_pl_output = str(sum(total_pl))

#Step 6: Print Print Print the outputs!
print("Financial Analysis")
print("----------------------------------------------")
print("Total Months :"+ month_count)
print("Total: $"+ total_pl_output)

#Step 7: Write Write Write the outputs!