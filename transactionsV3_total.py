import requests
import json
import datetime
from datetime import timedelta
import time


# Takes a list of dictionaries and returns a dictionary with the sum of the amounts for each payee_name
def get_sum_of_income(data):
    sum_dict = {}
    for i in data:
        sum_dict[i['payee_name']] = sum_dict.get(i['payee_name'], 0) + i['amount']

    return sum_dict

# Prints the income for a given date.

def print_income_for_day(date, transactions):
    print("\n\n" + time.strftime("%b. %d", time.strptime(date, "%Y-%m-%d")) + 
          " (" + time.strftime("%a", time.strptime(date, "%Y-%m-%d")) + ")")

    transactions_that_date = [x for x in transactions 
                              if date == x['date']]

    grouped_transactions_by_name = get_sum_of_income(transactions_that_date)

    total_for_date = sum(float(x['amount']) 
                         for x in transactions_that_date)
    print("Total: $" + '{:,.2f}'.format(total_for_date)) 

    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])))
        
        
def print_income_for_month(month, transactions):
    print("\n\n" + time.strftime("%B", time.strptime(month, "%Y-%m")))

# Prints the income for a given month

    transactions_that_month = []
    for y in transactions:
        if month in y['date']:
            transactions_that_month.append(y)
        else:
            pass
    grouped_transactions_by_name = get_sum_of_income(transactions_that_month)

    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])))

    total_for_month = sum(float(x['amount']) for x in transactions_that_month)
    print("Total: $" + '{:,.2f}'.format(total_for_month))




headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992',
}

params = (
    ('since_date', (datetime.datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")),
)

response = requests.get('https://api.youneedabudget.com/v1/budgets/72f55793-a9fc-4538-92fe-63be2c1cdddc/transactions', headers=headers, params=params).json()['data']['transactions']
transactions = []


for x in response:
    if '-' not in str(x['amount']):  # if the amount is positive
        payee_name = x['payee_name']
        # remove any words from the payee_name that contain any digit
        payee_name = ' '.join(word for word in payee_name.split() if not any(char.isdigit() for char in word))
        amount = (float(x['amount']) / 1000)
        account_name = x['account_name']

        date = x['date']
        data = {"payee_name": str(payee_name), "amount": amount, "date": str(date), "account": account_name}
        transactions.append(data)

    else:
        pass

'''
for x in transactions:
    print(x['payee_name'] + ' $' + str(x['amount']) + ' ' + x['date'] + ' ' + x['account'])
'''


# Returns a list of the last x days

def get_last_days(days):
    last_days = []
    today = datetime.date.today()

    for x in range(days):
        day = (today - timedelta(days=x)).strftime("%Y-%m-%d")

# Prints the income for the last x days
        last_days.append(str(day))
    return last_days

def print_income_for_last_days(last_days, transactions):
    for x in last_days:
        print_income_for_day(x, transactions)


def print_total_for_week(last_days, transactions):

# Prints the total income for the last x days
    print("\n\n")
    total_for_week = sum(float(x['amount']) for x in transactions if x['date'] in last_days)
    total_for_week_formatted = '${:,.2f}'.format(total_for_week)
    print("Total for the week: " + total_for_week_formatted)

# Prints the income for the last month

def print_income_for_last_month(transactions):
    print("\n\n")
    last_month = (datetime.date.today() - timedelta(days=30)).strftime("%Y-%m")
    print_income_for_month(last_month, transactions)

last_days = get_last_days(7)

print_income_for_last_days(last_days, transactions)

print_total_for_week(last_days, transactions)

print_income_for_last_month(transactions)
