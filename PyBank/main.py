#step 0: import the csv
import csv

#step 1: identify the csv path
csvfilepath = "Resources/budget_data.csv"

#Set the variables
month_count = 0
total_pl = 0
monthly_profit_delta = 0
previous_pl_value = 0
monthly_delta_value = 0
rolling_delta_value = 0
rolling_change_list = []
rolling_delta_value_count = 0
max_value = 0
min_value = 0
max_value_month ="max value month"
min_value_month = "min value month"

#step 3: open the file and let's get started! 
with open(csvfilepath,mode='r',encoding='UTF-8') as csv_file:
    csv_data = csv.reader(csv_file,delimiter=',')

    #Step 4: Skip the headers for all iteration runs!
    headers = next(csv_data)
    
    #Step 5: Pull csv_data values and push to lists that will be used for iteration runs

    for i in csv_data:
        month_count = month_count + 1
        total_pl = total_pl + int(i[1])
        #produce a rolling monthly change value as an output of each iteration
        rolling_delta_value = int(i[1]) - previous_pl_value
        #identify the highest value by comparing the latest claimant of the title. 
        if rolling_delta_value > max_value:
            max_value = rolling_delta_value
            max_value_month = str(i[0])
        #identify the lowest value by comparing the latest claimant of the title. 
        if rolling_delta_value < min_value:
            min_value = rolling_delta_value
            min_value_month = str(i[0])
        #as we iterate, add to the rolling change list with all monthly changes produced at the beginning of the for loop
        rolling_change_list.append(int(rolling_delta_value))
        #update the previous_profit/loss value with the current iteration value so the next run can evaluate the next row against the current to identify the next change
        previous_pl_value = int(i[1])

    #prep for the average change of all change values by removing 1 from total month count to get the same count of change values produced
    rolling_delta_value_count = month_count - 1
    #remove the first p/l value that was unintentionally included in the change values list so it doesn't inflate the average
    rolling_change_list.pop(0)
    #calculate the average change as an output of the sum of all change values mod count of change values; rounding to second decimal value.
    average_change = round(sum(rolling_change_list)/(rolling_delta_value_count),2)
    
    #print print print!

    print("Financial Analysis Challenge")
    print( "---------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total Amount: ${total_pl}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_value_month} (${max_value})")
    print(f"Greatest Decrease in Profits: {min_value_month} (${min_value})")

    #write write write!

    text_file_path="Analysis/Summary_Financial_Analysis.txt"

    with open(text_file_path,"w") as text_file:

            text_file.write("Financial Analysis Challenge\n")
            text_file.write( "---------------------------\n")
            text_file.write(f"Total Months: {month_count}\n")
            text_file.write(f"Total $: {total_pl}\n")
            text_file.write(f"Average Change: ${average_change}\n")
            text_file.write(f"Greatest Increase in Profits: {max_value_month} (${max_value})\n")
            text_file.write(f"Greatest Increase in Profits: {min_value_month} (${min_value})\n")

