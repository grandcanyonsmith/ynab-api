import requests
from datetime import datetime
import json


headers = {
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992'

}

def get_payee_locations(payee_id):
    url = f'https://api.youneedabudget.com/v1/payees/{payee_id}/payee_locations'
    response = requests.get(url, headers=headers)
    return None if response.status_code != 200 else response.json()

