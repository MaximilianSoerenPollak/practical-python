import csv 
from pprint import pprint

#TODO Using enumerate(), modify your pcost.py program so that it prints a line number with the warning message when it encounters bad input. | 2.15

def portfolio_info(filename):
    with open(filename, "r") as f:
        portfolio = []
        rows = csv.reader(f)
        headers = next(rows)
        for row_nr, row_info in enumerate(rows):
            try:
                stock = {}
                nr_shares = int(row_info[1])
                price = float(row_info[2])
                stock["name"] = row_info[0]
                stock["shares"] = int(row_info[1])
                stock["price"] = float(row_info[2])
                portfolio.append(stock)
            except Exception as e:
                print(f"The Error is: {e}, this Error occured in row {row_nr}")
        return portfolio

# pprint(portfolio_info("Work/Data/missing.csv"))

#TODO Make it work even when a new column is there. | 2.16
def portfolio_cost(filename):
    with open(filename, "r") as f:
        total_cost = 0
        rows = csv.reader(f)
        headers = next(rows)
        for row_nr, row_info in enumerate(rows):
            record = dict(zip(headers, row_info))
            try:
                nr_shares = int(record["shares"])
                price = float(record["price"])
                total_cost += nr_shares * price
            except Exception as e:
                print(f"The Error is: {e}, this Error occured in row {row_nr}")
        return total_cost

print(portfolio_cost("Work/Data/portfoliodate.csv"))

