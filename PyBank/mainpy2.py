import csv
#OUTSTANDING ITEMS - 1. Calculate average delta 2. print all statements under a single command 3. Seperate text file outputs by line

#step 1: identify the csv path
csvfilepath = "Resources/budget_data.csv"

#Set the variables
month_count = 0
total_pl = 0
monthly_profit_delta = 0
previous_pl_value = 0
monthly_delta_value = 0
rolling_delta_value = 0
rolling_sum_value = 0
rolling_delta_value_count = 0
max_value = 0
min_value = 0
max_value_month ="max value month"
min_value_month = "min value month"

#Open the file and let's get started! 
with open(csvfilepath,mode='r',encoding='UTF-8') as csv_file:
    csv_data = csv.reader(csv_file,delimiter=',')

    #Step 0: Skip the headers for all iteration runs!
    headers = next(csv_data)

    #Step 2: Pull csv_data values and push to lists that will be used for iteration runs
    for i in csv_data:
        month_count = month_count + 1
        total_pl = total_pl + int(i[1])
        rolling_delta_value = int(i[1]) - previous_pl_value
        previous_pl_value = int(i[1])
        rolling_sum_value = rolling_delta_value + rolling_sum_value
        rolling_delta_value_count = rolling_delta_value_count + 1
        if rolling_delta_value > max_value:
            max_value = rolling_delta_value
            max_value_month = str(i[0])
        if rolling_delta_value < min_value:
            min_value = rolling_delta_value
            min_value_month = str(i[0])
    
    average_change = rolling_sum_value/rolling_delta_value_count
    #print statements at the end
    
    print("Financial Analysis Challenge")
    print( "---------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total Amount: ${total_pl}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {max_value_month} (${max_value})")
    print(f"Greatest Decrease in Profits: {min_value_month} (${min_value})")

    #write statements to a text file

    text_file_path="Analysis/Summary_Financial_Analysis.txt"

    with open(text_file_path,"w") as text_file:

    #write the respective print statements into the text file
            text_file.write("Financial Analysis Challenge")
            text_file.write( "---------------------------")
            text_file.write(f"Total Months: {month_count}")
            text_file.write(f"Total $: {total_pl}")
            text_file.write(f"Average Change: {average_change}")
            text_file.write(f"Greatest Increase in Profits: {max_value_month} (${max_value})")
            text_file.write(f"Greatest Increase in Profits: {min_value_month} (${min_value})")

