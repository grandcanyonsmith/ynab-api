import requests
from datetime import datetime
import json


headers = {
    'Authorization': 'Bearer 11059c76ab063accae00d9439c417d305fdbb41d45ebcab62785a65065d29992'

}

def get_payee_locations(payee_id):
    url = 'https://api.youneedabudget.com/v1/payees/{}/payee_locations'.format(payee_id)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    return response.json()

