
import requests
import os
import datetime
from reportlab.pdfgen import canvas
from transactions import get_all

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992',
}
params = (
    ('include_accounts', 'true'),
)
response = requests.get(

    'https://api.youneedabudget.com/v1/budgets', headers=headers, params=params)

def add_commas(number):
    return '{:,}'.format(round(number, 2))

def round_decimal(number):
    return round(number, 2)

def print_account(account):
    print(account['name'])


def currency_formatter(number):
    return '$' + str(add_commas(round_decimal(number)))

def get_account_summary(accounts, name, account_ids, index=0, total=0):
    if index < len(accounts): 
        if accounts[index]['id'] in account_ids:
            total += account_balance([accounts[index]])
        return get_account_summary(accounts, name, account_ids, index + 1, total) 
    else:
        print(name + " = " + currency_formatter(total)) 

def account_balance(accounts): 
    return accounts[0]['balance'] / 1000 + account_balance(accounts[1:]) if len(accounts) > 1 else accounts[0]['balance'] / 1000 if len(accounts) > 0 else 0

def get_valent_balance():
    valent_accounts = [
        'c909d550-cbdc-4ddc-8fa8-c8b51dca1520',
        '2504ddd0-0f69-4d69-8e3a-59d63d812202'
    ]
    return sum([account['balance'] / 1000 for account in response.json()['data']['budgets'][0]['accounts'] if account['id'] in valent_accounts])

def get_investment_balance():
    investment_accounts = [
        '483ce002-1231-4742-ba7b-5f70cc62731f',
        'a5f65be8-bb2d-407b-98fa-ebf5c8f576c5',
        '83d81f72-d939-4f63'
    ]
    return sum([account['balance'] / 1000 for account in response.json()['data']['budgets'][0]['accounts'] if account['id'] in investment_accounts])

def get_personal_balance():
    personal_accounts = [ 
        'a301f214-607e-47e7-9e94-90fb426be953',
        '97f99b64-425d-4407-9491-d223fba06e1f',
        'f41de13e-0e7a-4be4-838f-07c059272c68',
        '3f3cd0a4-37aa-4ced-8ba4-bf8fa0489d11',
        '3ba80db1-01e3-408a-80ef-ef17d34ac59a'
    ]
    return sum([account['balance'] / 1000 for account in response.json()['data']['budgets'][0]['accounts'] if account['id'] in personal_accounts])

def get_personal_accounts_summary(accounts):
    personal_accounts = [
        'a301f214-607e-47e7-9e94-90fb426be953',
        '97f99b64-425d-4407-9491-d223fba06e1f',
        'f41de13e-0e7a-4be4-838f-07c059272c68',
        '3f3cd0a4-37aa-4ced-8ba4-bf8fa0489d11',
        '3ba80db1-01e3-408a-80ef-ef17d34ac59a',
        '3ba80db1-01e3-408a-80ef-ef17d34ac59a'
    ]
    return sorted([account['name'] + " = " + currency_formatter(account_balance([account])) for account in accounts if account['id'] in personal_accounts], reverse=True)

def get_valent_summary(accounts):
    valent_accounts = [
        'c909d550-cbdc-4ddc-8fa8-c8b51dca1520',
        '2504ddd0-0f69-4d69-8e3a-59d63d812202'
    ]
    return sorted([account['name'] + " = " + currency_formatter(account_balance([account])) for account in accounts if account['id'] in valent_accounts], reverse=True)

def get_investment_summary(accounts):
    investment_accounts = [
        '483ce002-1231-4742-ba7b-5f70cc62731f',
        'a5f65be8-bb2d-407b-98fa-ebf5c8f576c5',
        '83d81f72-d939-4f63-b8de-38a242b024e1'
    ]
    return sorted([account['name'] + " = " + currency_formatter(account_balance([account])) for account in accounts if account['id'] in investment_accounts], reverse=True)

def get_accounts():
    accounts = []
    personal_accounts = [
        'a301f214-607e-47e7-9e94-90fb426be953',
        '97f99b64-425d-4407-9491-d223fba06e1f',
        'f41de13e-0e7a-4be4-838f-07c059272c68',
        '3f3cd0a4-37aa-4ced-8ba4-bf8fa0489d11',
        '3ba80db1-01e3-408a-80ef-ef17d34ac59a'
    ]
    investment_accounts = [
        '483ce002-1231-4742-ba7b-5f70cc62731f',
        'a5f65be8-bb2d-407b-98fa-ebf5c8f576c5',
        '83d81f72-d939-4f63-b8de-38a242b024e1'
    ]
    valent_accounts = [
        'c909d550-cbdc-4ddc-8fa8-c8b51dca1520',
        '2504ddd0-0f69-4d69-8e3a-59d63d812202'
    ]
    for account in response.json()['data']['budgets'][0]['accounts']:
        if account['id'] in personal_accounts:
            accounts.append(account)
        if account['id'] in investment_accounts:
            accounts.append(account)
        if account['id'] in valent_accounts:
            accounts.append(account)
    return accounts


get_personal_accounts_summary(get_accounts())

# Creates a PDF 
def create_pdf(accounts):
    expenses = str(get_all())
    c = canvas.Canvas("report.pdf")
    c.setLineWidth(.3)
    c.drawString(480, 750, datetime.date.today().strftime("%B %d, %Y"))
    c.line(480, 747, 580, 747)
    c.drawString(100, 750, "Personal Balance: " + currency_formatter(get_personal_balance()))
    # Print the 3 sub-accounts of personal accounts under the Personal heading
    list_to_string = get_personal_accounts_summary(accounts)
    y = 0
    for i in range(len(list_to_string)):
        print(list_to_string[i])
        c.drawString(130, 720 - (i * 20), "- " + list_to_string[i])
        y = y + 20
    c.drawString(100, 600, "Investment Balance: " + currency_formatter(get_investment_balance()))   
    list_to_string = get_investment_summary(accounts)
    y = 0
    for i in range(len(list_to_string)):
        print(list_to_string[i])
        c.drawString(130, 550 - (i * 20), "- " + list_to_string[i])
        
    c.drawString(100, 400, "Valent Balance: " + currency_formatter(get_valent_balance())) 
    list_to_string = get_valent_summary(accounts)
    for i in range(len(list_to_string)):
        print(list_to_string[i])
        c.drawString(130, 380 - (i * 20), "- " + list_to_string[i])

    c.drawString(100, 100, "Total Expenses this week: " + expenses)
    c.showPage()
    c.save() 
    os.system("open report.pdf")

    
#
# accounts = get_accounts()
# print(accounts)
# get_account_summary(accounts, "Personal", ['a301f214-607e-47e7-9e94-90fb426be953', '97f99b64-425d-4407-9491-d223fba06e1f', 'f41de13e-0e7a-4be4-838f-07c059272c68', '3f3cd0a4-37aa-4ced-8ba4-bf8fa0489d11', '3ba80db1-01e3-408a-80ef-ef17d34ac59a'])
# get_valent_summary(accounts)
# print("Total =", currency_formatter(account_balance(accounts)))
# create_pdf(accounts)
#
# print(get_valent_balance())
# print(get_valent_summary(accounts))
# print(get_investment_summary(accounts))

# TODO:
# 1. Create a PDF report
# 2. Create a function that returns the total amount spent this week
# 3. Create a function that returns the total amount spent this month
# 4. Create a function that will show where the money is spent & how much
