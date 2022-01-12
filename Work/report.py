import csv
from pprint import pprint

#This is the template. Now we need to refine it.
def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers - next(rows)
        for row in rows:
            nr_shares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

# #TODO New Goal: Make function read portfolio file into list of tuples.

def read_portfolio(filename):
    portfolio = []

    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nr_shares = int(row[1])
            price = float(row[2])
            portfolio.append((row[0], nr_shares, price))
    return portfolio

# print(read_portfolio("Work/Data/portfolio.csv"))

#!TODO Make the Tuples Dictionaries
def read_portfolio_v2(filename):
    portfolio = []

    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {}
            nr_shares = int(row[1])
            price = float(row[2])
            stock["name"] = row[0]
            stock["shares"] = int(row[1])
            stock["price"] = float(row[2])
            portfolio.append(stock)
        return portfolio

# pprint(read_portfolio_v2("Work/Data/portfolio.csv"))


#!TODO Read as a Dictionary prices and tickers from prices.csv

def read_prices(filename):
    with open(filename, "r") as f:
        stock = {}
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 0:
                stock[row[0]] = float(row[1])
    return stock
# a = read_prices("Work/Data/prices.csv")
# print(a["AA"])

#!TODO figure out if the person can retire.

def can_retire():
    portfolio = read_portfolio_v2("Work/Data/portfolio.csv") #list of dictionaries [{name: 'Bank of America'}, {name: "..."}]
    current_prices = read_prices("Work/Data/prices.csv")
    gains = 0
    losses = 0
    for stock in portfolio:
        stockname = stock["name"]
        if stockname in current_prices:
            buy_price = stock["price"]
            shares = stock["shares"]
            sell_price = current_prices[stockname]
            if buy_price > sell_price:
                losses += (buy_price - sell_price) * shares
            if sell_price > buy_price:
                gains += (sell_price - buy_price) * shares
    profit = gains - losses
    return gains, losses, profit

# a, b, c = can_retire()
# print(f"The person made {a:.2f} gains, {b:.2f} losses and overall a profit of {c:.2f}.")
# print("This seems to not be a good day to retire, with 16k losses.")

#!TODO make a new function that takes the list of stocks and dictionary of prices as inputs and returns a list of tuples containing the rows of the above table 

def make_report(stocklist, prices):
    report = []
    for stock in stocklist:
        if stock["name"] in prices:
            shares = stock["shares"]
            price = prices[stock["name"]]
            change = stock["price"] - price
            report.append((stock["name"], shares, price, change))
    return report
portfolio = read_portfolio_v2("Work/Data/portfolio.csv") #list of dictionaries [{name: 'Bank of America'}, {name: "..."}]
current_prices = read_prices("Work/Data/prices.csv")
headers = ("Name", "Shares", "Price", "Change")
reports = make_report(portfolio, current_prices)
print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
print(f"{'-' * 7:>10s} {'-' * 7:>10s} {'-' * 7:>10s} {'-' * 7:>10s}")
for name, share, price, change in reports:
    print(f"{name:>10s} {share:>10d} {'$' + str(price):>10s} {change:>10.2f}")

