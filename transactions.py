import requests
import json
import datetime
from datetime import timedelta
import time

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992',
}

params = (
    ('since_date', (datetime.datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")),
)

response = requests.get('https://api.youneedabudget.com/v1/budgets/72f55793-a9fc-4538-92fe-63be2c1cdddc/transactions', headers=headers, params=params).json()['data']['transactions']
transactions = []


def remove_period_from_payee_name(payee_name):
    if payee_name.find(".") == -1:
        return payee_name
    payee_name = payee_name[:payee_name.find(".")]
    return remove_period_from_payee_name(payee_name)

#create a function to format the payee_name as camel case:
def format_payee_name_as_camel_case(payee_name):
    #format payee_name as camel case and return the payee_name:
    return ''.join(x.title() for x in payee_name.split(' '))



#go through each transaction in the response:
for x in response:
    #if the amount is negative then skip it and go to the next transaction:
    if '-' in str(x['amount']):
        #get the payee_name from the transaction:
        payee_name = x['payee_name']
        #remove any words from the payee_name that contain any digit
        payee_name = ' '.join(word for word in payee_name.split() if not any(char.isdigit() for char in word))
        #get the amount from the transaction:
        amount = (int(x['amount'])/1000)
        #get the account name from the transaction:
        account_name = x['account_name']
        #format the payee_name:
        payee_name = remove_period_from_payee_name(payee_name)
        payee_name = format_payee_name_as_camel_case(payee_name)

        #get the date from the transaction:
        date = x['date']
        #create a dictionary with the payee_name, amount, date, and account name
        data = {"payee_name": str(payee_name), "amount": amount, "date": date, "account": account_name}
        #add the dictionary to the transactions list
        transactions.append(data)


# print all of the transactions
for x in transactions:
    print("\n\n" + x['payee_name']+ ' $' + str(x['amount']) + ' ' + x['date'] + ' ' + x['account'] + "\n\n")

# create a function to get the sum of the transactions
def get_sum(data):
    # create a dictionary with the payee_name as the key and the amount as the value
    sum_dict = {}
    # go through each transaction in the data list
    for i in data:
        # if the payee_name is already in the dictionary then add the amount to the value, otherwise add it to the dictionary
        sum_dict[i['payee_name']] = sum_dict.get(i['payee_name'], 0) + i['amount']

    return sum_dict #return the dictionary



#make a list of the last 7 days in format YYYY-MM-dd then print it:
last_7_days = []
last_30_days = []
#get today's date
today = datetime.date.today()
print("\n\n" + str(today) + "\n\n")
#get the last 7 days
for x in range(7):
    day = (today - timedelta(days=x)).strftime("%Y-%m-%d")
    last_7_days.append(str(day))

#get the last 30 days
for x in range(30):
    day = (today - timedelta(days=x)).strftime("%Y-%m-%d")
    last_30_days.append(str(day))


#go through each day in the last_7_days list
for x in reversed(last_7_days):
    print("\n\n")
    #format date as the first three letters of the month and then the day (Example: 2022-02-14 = Feb. 14)
    print(time.strftime("%b. %d", time.strptime(x, "%Y-%m-%d")) + " ("+ time.strftime("%a", time.strptime(x, "%Y-%m-%d"))+")\n\n\n\n")

    #get all of the transactions for that day and group them by payee_name
    transactions_that_day = [y for y in transactions if x == y['date']]
    #group the transactions by payee_name
    grouped_transactions_by_name = get_sum(transactions_that_day)

    #print the payee_name and the amount
    for y in grouped_transactions_by_name:
        #print the total for the day
        print(f'{y}: $' + '{:,.2f}'.format((grouped_transactions_by_name[y])))

    #get the total for the day
    total_for_day = sum(int(x['amount']) for x in transactions_that_day)
    #print the total for the day
    print("Total: $" + '{:,.2f}'.format(total_for_day) + "\n\n\n\n")

#print total for the week:
def get_all():
    total_for_week = sum(int(x['amount']) for x in transactions if x['date'] in last_7_days)
    total_for_week_formatted = '${:,.2f}'.format(total_for_week)
    print(f"Total for the week: {total_for_week_formatted}")
    total_for_past_30_days = sum(int(x['amount']) for x in transactions if x['date'] in last_30_days)
    total_for_past_30_days_formatted = '${:,.2f}'.format(total_for_past_30_days)

    print(f"Total for the past 30 days: {total_for_past_30_days_formatted}")

    return total_for_past_30_days_formatted
    

get_all()

# TODO:
# 1. Create a function that will get the total for the past 30 days
# 2. Create a function that will get the total for the past 7 days
# 3. Create a function that will get the total for the past 30 days and the past 7 days
