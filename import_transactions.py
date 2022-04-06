import datetime
import requests
from datetime import timedelta
import time


# Get transactions from YNAB API.
# budget_id: YNAB budget ID.
# month: Month to get transactions for.
# return: List of transactions.
def get_transactions(budget_id, month):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992',
    }

    params = (
        ('since_date', (datetime.datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")),
    )

    response = requests.get('https://api.youneedabudget.com/v1/budgets/' + budget_id + '/transactions', headers=headers, params=params).json()

    if month == 'all':
        return response
    else:
        return [i for i in response if month in i['date']]

transactions = get_transactions('72f55793-a9fc-4538-92fe-63be2c1cdddc', 'all')
print(transactions)

def format_transactions(transactions):
    for i in transactions:
        i['date'] = i['date'][:10]
    return transactions

    
def get_sum_of_income(data):
    sum_dict = {}
    for i in data:
        sum_dict[i['payee_name']] = sum_dict.get(i['payee_name'], 0) + float(i['amount'])/1000

    return sum_dict
# Prints the income for a given date.
income = get_sum_of_income(transactions)
print(income)

def print_income_for_date(date, transactions, level, date_format, date_format_for_strptime, print_total):
    print("\n\n" + time.strftime(date_format, time.strptime(date, date_format_for_strptime)) + " " + level + ":")

    transactions_that_date = [x for x in transactions if date == x['date']]

    grouped_transactions_by_name = get_sum_of_income(transactions_that_date)

    if print_total:
        total_for_date = sum(float(x['amount']) for x in transactions_that_date)
        print("Total: $" + '{:,.2f}'.format(total_for_date)) 

    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])))
        
print_income_for_date('2022-04-01', transactions, 'day', "%b. %d (%a)", "%Y-%m-%d", True)

def print_income_for_date(date, transactions, level, date_format, date_format_for_strptime, print_total):
    print("\n\n" + time.strftime(date_format, time.strptime(date, date_format_for_strptime)) + " " + level + ":")

    transactions_that_date = [x for x in transactions if date in x['date']]

    grouped_transactions_by_name = get_sum_of_income(transactions_that_date)

    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])) + " " + level)

    if print_total:
        total_for_date = sum(float(x['amount']) for x in transactions_that_date)
        print("Total: $" + '{:,.2f}'.format(total_for_date))
    
print_income_for_date('2022-04', transactions, 'month', "%B", "%Y-%m", True)

def print_income_for_year(year, transactions, level, date_format, date_format_for_strptime):
    print("\n\n" + time.strftime(date_format, time.strptime(year, date_format_for_strptime)) + " " + level)
    transactions_that_year = [x for x in transactions if year in x['date']]

    grouped_transactions_by_name = get_sum_of_income(transactions_that_year)

    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])) + " " + level)

    total_for_year = sum(float(x['amount']) for x in transactions_that_year)
    print("Total: $" + '{:,.2f}'.format(total_for_year))

print_income_for_year('2022', transactions, 'year', "%Y", "%Y")
