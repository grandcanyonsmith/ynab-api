import requests
import json
import datetime
from datetime import timedelta
import time


def get_sum_of_income(data):
    sum_dict = {}
    for i in data:
        sum_dict[i['payee_name']] = sum_dict.get(i['payee_name'], 0) + i['amount']

    return sum_dict


def print_income_for_date(date, transactions):
    print("\n\n" + time.strftime("%b. %d", time.strptime(date, "%Y-%m-%d")) + " (" + time.strftime("%a", time.strptime(date, "%Y-%m-%d")) + ")")

    transactions_that_day = []
    for y in transactions:
        if date == y['date']:
            transactions_that_day.append(y)
        else:
            pass
    grouped_transactions_by_name = get_sum_of_income(transactions_that_day)

    for y in grouped_transactions_by_name:
        print(y + ': $' + '{:,.2f}'.format((grouped_transactions_by_name[y])))

    total_for_day = sum(int(x['amount']) for x in transactions_that_day)
    print("Total: $" + '{:,.2f}'.format(total_for_day))


headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992',
}

params = (
    ('since_date', (datetime.datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")),
)

response = requests.get('https://api.youneedabudget.com/v1/budgets/72f55793-a9fc-4538-92fe-63be2c1cdddc/transactions', headers=headers, params=params).json()['data']['transactions']
transactions = []


for x in response:
    if '-' not in str(x['amount']):  # if the amount is positive
        payee_name = x['payee_name']
        # remove any words from the payee_name that contain any digit
        payee_name = ' '.join(word for word in payee_name.split() if not any(char.isdigit() for char in word))
        amount = (int(x['amount']) / 1000)
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

last_7_days = []
today = datetime.date.today()

for x in range(7):
    day = (today - timedelta(days=x)).strftime("%Y-%m-%d")
    last_7_days.append(str(day))

for x in reversed(last_7_days):
    print_income_for_date(x, transactions)

print("\n\n")
total_for_week = sum(int(x['amount']) for x in transactions if x['date'] in last_7_days)
total_for_week_formatted = '${:,.2f}'.format(total_for_week)
print("Total for the week: " + total_for_week_formatted)
