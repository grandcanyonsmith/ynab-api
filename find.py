data =  [{'payee_name': 'Southwes', 'amount': -361.98, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Geico', 'amount': -197.56, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Fiverr', 'amount': -131.88, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -121.21, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': '7-Eleven', 'amount': -95.2, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Chevron', 'amount': -43.63, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Apple', 'amount': -34.29, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Service', 'amount': -30.0, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Csa', 'amount': -25.48, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': '7-Eleven', 'amount': -20.0, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Transaction', 'amount': -15.0, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -13.38, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Jetbrains', 'amount': -9.55, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Netflix', 'amount': -8.99, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -8.57, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -4.28, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Maverik', 'amount': -2.67, 'date': '2022-02-14', 'account': 'Zions Main'}, {'payee_name': 'Venmo', 'amount': -275.88, 'date': '2022-02-15', 'account': 'Zions Main'}, {'payee_name': 'Jasper', 'amount': -59.0, 'date': '2022-02-15', 'account': 'Zions Main'}, {'payee_name': 'Jasper', 'amount': -59.0, 'date': '2022-02-15', 'account': 'Zions Main'}, {'payee_name': 'Land', 'amount': -6.13, 'date': '2022-02-15', 'account': 'Zions Main'}, {'payee_name': 'Slc', 'amount': -3.59, 'date': '2022-02-15', 'account': 'Zions Main'}, {'payee_name': 'Walgreens', 'amount': -63.99, 'date': '2022-02-16', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -35.38, 'date': '2022-02-16', 'account': 'Zions Main'}, {'payee_name': 'Apple', 'amount': -21.44, 'date': '2022-02-16', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -5.77, 'date': '2022-02-16', 'account': 'Zions Main'}, {'payee_name': 'Clickup', 'amount': -165.85, 'date': '2022-02-17', 'account': 'Zions Main'}, {'payee_name': 'Target', 'amount': -81.8, 'date': '2022-02-17', 'account': 'Zions Main'}, {'payee_name': 'Apple', 'amount': -48.25, 'date': '2022-02-17', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -26.35, 'date': '2022-02-17', 'account': 'Zions Main'}, {'payee_name': 'Payoneer', 'amount': -20.61, 'date': '2022-02-17', 'account': 'Zions Main'}, {'payee_name': 'Payoneer', 'amount': -20.61, 'date': '2022-02-17', 'account': 'Zions Main'}, {'payee_name': 'Amazon', 'amount': -11.32, 'date': '2022-02-17', 'account': 'Zions Main'}]

#get the sum of each payee_name with the same name:
def get_sum(data): 
    sum_dict = {}
    for i in data:
        if i['payee_name'] in sum_dict:
            sum_dict[i['payee_name']] += i['amount']
        else:
            sum_dict[i['payee_name']] = i['amount']
    print(sum_dict)
    return sum_dict

get_sum(data)