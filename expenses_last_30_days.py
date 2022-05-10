import requests
import datetime
from datetime import timedelta
import time

#1. Get the expeneses for the last 30 days
#2. Group the expenses by name
#3. Sort the expenses by amount
#4. Format the expenses for printing by dividing by 1000
#5. Format the spelling of the payee names for printing
#6. Print the expenses


headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992',
}

params = (
    ('since_date', (datetime.datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")),
)

response = requests.get('https://api.youneedabudget.com/v1/budgets/72f55793-a9fc-4538-92fe-63be2c1cdddc/transactions', headers=headers, params=params).json()['data']['transactions']
transactions = []


# get the expenses for the last 30 days
for i in response:
    if i['amount'] < 0:
        transactions.append(i)
    else:
        pass

# get the expenses for the last 30 days
def get_sum_of_expenses(data):
    sum_dict = {}
    for i in data:
        sum_dict[i['payee_name']] = sum_dict.get(i['payee_name'], 0) + i['amount']
    return sum_dict

# Prints the expenses for a given date.
def print_expenses_for_day(date, transactions):
    print("\n\n" + time.strftime("%b. %d", time.strptime(date, "%Y-%m-%d")) +
            " (" + time.strptime("%a", time.strptime(date, "%Y-%m-%d")) + ")")
    transactions_that_date = [x for x in transactions if date == x['date']]
    grouped_transactions_by_name = get_sum_of_expenses(transactions_that_date)
    total_for_date = sum(float(x['amount']) for x in transactions_that_date)
    print("Total: $" + '{:,.2f}'.format(total_for_date))
    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])))

# Prints the expenses for a given month
def print_expenses_for_month(month, transactions):
    print("\n\n" + time.strftime("%B", time.strptime(month, "%Y-%m")))
    transactions_that_month = []
    for y in transactions:
        if month in y['date']:
            transactions_that_month.append(y)
        else:
            pass

    grouped_transactions_by_name = get_sum_of_expenses(transactions_that_month)
    print("grouped",grouped_transactions_by_name)



    def sort_expenses(transactions):
        sorted_transactions = sorted(transactions, key=lambda k: k['amount'], reverse=True)
        return sorted_transactions

    total_for_month = sum(float(x['amount']) for x in transactions_that_month)
    # print("Total: $" + '{:,.2f}'.format(total_for_month/1000))

    # group the transactions by name
    grouped_transactions_by_name = get_sum_of_expenses(transactions_that_month)


    def sort_expenses(grouped_transactions_by_name):
        sorted_transactions = sorted(  grouped_transactions_by_name, key=lambda k: k['amount'], reverse=True)
        return sorted_transactions



    for i in sort_expenses(transactions_that_month):
        print(i['payee_name'] + ': $' + '{:,.2f}'.format(i['amount']/1000))

    print("Total: $" + '{:,.2f}'.format(total_for_month/1000))


# Prints the expenses for a given year
def print_expenses_for_year(year, transactions):
    print("\n\n" + time.strftime("%Y", time.strptime(year, "%Y")))
    transactions_that_year = []
    for y in transactions:
        if year in y['date']:
            transactions_that_year.append(y)
        else:
            pass
    grouped_transactions_by_name = get_sum_of_expenses(transactions_that_year)
    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])))



print_expenses_for_month((datetime.datetime.now()).strftime("%Y-%m"), transactions)
