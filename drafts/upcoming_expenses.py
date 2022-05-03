Jakewebsite = 700.00
ChangesforMoneyDolly = 250.00
Samadara = 500.00
AlbumArtWork  = 1000.00

def upcoming_expenses(Jakewebsite, ChangesforMoneyDolly, Samadara, AlbumArtWork):
    def sum_of_all():
        return 700 + 250 + 500 + 1000

    def add_comma(number):
        return "{:,}".format(number)
    print("Expenses:" + '\n' + '\n')
    print("Jakewebsite = $" + add_comma(Jakewebsite) + ".00")
    print("ChangesforMoneyDolly = $" + add_comma(ChangesforMoneyDolly) + ".00")
    print("Samadara = $" + add_comma(Samadara) + ".00")
    print("AlbumArtWork = $" + add_comma(AlbumArtWork) + ".00")
    print('\n')
    print("Total upcoming expenses = $" + add_comma(sum_of_all()) + ".00")

    # return upcoming_expenses(Jakewebsite, ChangesforMoneyDolly, Samadara, AlbumArtWork)

upcoming_expenses(Jakewebsite, ChangesforMoneyDolly, Samadara, AlbumArtWork)




heartsconnect = 2000.00
heartsconnect_last_week = 1800.00
jake_website = 0000.00
income = [heartsconnect, heartsconnect_last_week, jake_website]

def upcoming_income(income):
    def sum_of_all():
        return sum(income)
    
    def add_comma(number):
        return "{:,}".format(number)
    
    print("Income:" + '\n' + '\n')
    print("heartsconnect = $" + add_comma(heartsconnect) + ".00")
    print("heartsconnect_last_week = $" + add_comma(heartsconnect_last_week) + ".00")
    print("jake_website = $" + add_comma(jake_website) + ".00")
    print('\n')
    print("Total upcoming income = $" + add_comma(sum_of_all()) + ".00")

upcoming_income(income)

        

current_cash = 1281

def current_cash_flow(current_cash):
    def add_comma(number):
        return "{:,}".format(number)
    print("Current Cash Flow:" + '\n' + '\n')
    print("Current Cash = $" + add_comma(current_cash) + ".00")
    print('\n')
    print("Total current cash flow = $" + add_comma(current_cash) + ".00")

current_cash_flow(current_cash)



def total_cash_flow(current_cash, income):
    def sum_of_all():
        return current_cash + sum(income)

    def add_comma(number):
        return "{:,}".format(number)
    print("Total Cash Flow:" + '\n' + '\n')
    print("Current Cash = $" + add_comma(current_cash) + ".00")
    print("Total upcoming income = $" + add_comma(sum(income)) + ".00")
    print('\n')
    print("Total cash flow = $" + add_comma(sum_of_all()) + ".00")

total_cash_flow(current_cash, income)


