import json
import ynab_api
from pprint import pprint
from ynab_api.api import accounts_api
'''
secrets.json should be manually generated as:

{
   "budget_id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
   "api_key":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

To get an api_key:
Sign in to the YNAB web app
and go to the "Account Settings" page
and then to the "Developer Settings" page.
Under the "Personal Access Tokens" section,
click "New Token", enter your password
and click "Generate" to get an access token.

To get your budget_id:
Sign in to the YNAB web app and go the budget of interest.
Copy YOUR_BUDGET_ID from the url:
https://app.youneedabudget.com/YOUR_BUDGET_ID/budget

Or, populate the fields directly in your code.
'''

with open('secrets.json') as f:
    # secrets = json.load(f)
    budget_id = "72f55793-a9fc-4538-92fe-63be2c1cdddc"
    api_key = "11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992"
    print(budget_id)
    print(api_key)

configuration = ynab_api.Configuration(
    host="https://api.youneedabudget.com/v1")
configuration.api_key['bearer'] = api_key
configuration.api_key_prefix['bearer'] = 'Bearer'

with ynab_api.ApiClient(configuration) as api_client:
    api_instance = accounts_api.AccountsApi(api_client)


    try:
        api_response = api_instance.get_accounts(budget_id)
        print(len(api_response['data']['accounts']))
        for x in api_response['data']['accounts']:
            print(x['name'])
            balance = (int(x['balance'])/10)
            print(f"${str(balance)}")
                    
            
            # pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception: %s\n" % e)
# curl -X GET "https://api.youneedabudget.com/v1/budgets/72f55793-a9fc-4538-92fe-63be2c1cdddc/accounts" -H "accept: application/json" -H "Authorization: Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992"


