import requests
import json


    # Adds commas to a number
def add_commas(number):
    return '{:,}'.format(number)
    # Rounds a number to 2 decimal places


def round_decimal(number):
    return round(number, 2)


def print_account(account):
    # Prints an account name and balance
    print(account['name'] + " = " + currency_formatter(account_balance([account])))


    # Formats a number as a currency
def currency_formatter(number):
    return '$' + str(add_commas(round_decimal(number)))

    # Returns the balance of a list of accounts
    return accounts[0]['balance'] / 1000 + account_balance(accounts[1:]) if len(accounts) > 1 else accounts[0]['balance'] / 1000 if len(accounts) > 0 else 0 


def get_account_summary(accounts, name, account_ids, index=0, total=0):
    if index < len(accounts): 
        if accounts[index]['id'] in account_ids:
            total += account_balance([accounts[index]])
        get_account_summary(accounts, name, account_ids, index + 1, total) 
    else:
        print(name + " = " + currency_formatter(total)) 

def account_balance(accounts): 
    return accounts[0]['balance'] / 1000 + account_balance(accounts[1:]) if len(accounts) > 1 else accounts[0]['balance'] / 1000 if len(accounts) > 0 else 0

    # Prints the total balance of personal accounts


def get_personal_accounts_summary(accounts):
    # Prints the total balance of Valent accounts
    personal = get_account_summary(accounts, "Personal", ['a301f214-607e-47e7-9e94-90fb426be953', '97f99b64-425d-4407-9491-d223fba06e1f', 'f41de13e-0e7a-4be4-838f-07c059272c68', '3f3cd0a4-37aa-4ced-8ba4-bf8fa0489d11', '3ba80db1-01e3-408a-80ef-ef17d34ac59a'])
    


def get_valent_summary(accounts):
    get_account_summary(accounts, "Valent", ['c909d550-cbdc-4ddc-8fa8-c8b51dca1520', '2504ddd0-0f69-4d69-8e3a-59d63d812202'])
    
    
    
def get_investment_summary(accounts):
    # Prints the total balance of investment accounts
    get_account_summary(accounts, "Investments", ['483ce002-1231-4742-ba7b-5f70cc62731f', 'a5f65be8-bb2d-407b-98fa-ebf5c8f576c5', '83d81f72-d939-4f63-b8de-38a242b024e1'])
    
def get_accounts():
    # Returns a list of accounts
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


headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992',
}

params = (
    ('include_accounts', 'true'),
)

response = requests.get(
    'https://api.youneedabudget.com/v1/budgets', headers=headers, params=params)

accounts = get_accounts()

get_account_summary(accounts, "Personal", ['a301f214-607e-47e7-9e94-90fb426be953', '97f99b64-425d-4407-9491-d223fba06e1f', 'f41de13e-0e7a-4be4-838f-07c059272c68', '3f3cd0a4-37aa-4ced-8ba4-bf8fa0489d11', '3ba80db1-01e3-408a-80ef-ef17d34ac59a'])
get_investment_summary(accounts)
get_valent_summary(accounts)
print("Total =", currency_formatter(account_balance(accounts)))

get_personal_accounts_summary(accounts)


print(get_accounts())
# pretty print json
print(json.dumps(response.json(), indent=4, sort_keys=True))