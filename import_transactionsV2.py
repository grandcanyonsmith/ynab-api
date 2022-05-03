import requests

def import_transactions(url, headers):
    url = "https://api.youneedabudget.com/v1/budgets/72f55793-a9fc-4538-92fe-63be2c1cdddc/transactions/import"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992"
    }
    response = requests.request("POST", url, headers=headers)
    print(response.text)