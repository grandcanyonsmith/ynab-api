from import_transactionsV2 import import_transactions
from balance import *

# Main function
url = "https://api.youneedabudget.com/v1/budgets/72f55793-a9fc-4538-92fe-63be2c1cdddc/transactions/import"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992"
}


def main():
    # Import transactions
    transactions = import_transactions(url, headers)

main()
    
