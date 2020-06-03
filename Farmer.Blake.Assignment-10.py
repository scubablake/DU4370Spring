#!/usr/bin/python3
# Blake Farmer
# Python Version: 3.7.7.
# Week 5 Programming Assignment: Using Classes - ICT-4370
# Take stock information as nested dictionary and bond as list to report on investor stock earnings.
# Uses: https://docs.python.org/3.7/library/datetime.html#datetime.date

# import Functions
import datetime, random

# Stock Class
class Stock():
	"""Initialize company stock attributes"""
	def __init__(self, symbol, shares, purchase_price, current_value, purchase_date):
		self.symbol = symbol
		self.shares = shares
		self.purchase_price = purchase_price
		self.current_value = current_value
		self.purchase_date = purchase_date

	# Calculate the Earnings and loss
	# Reference stock attributes
	def EarningsLossCalc(self):
		earnings_loss = (float(self.current_value) - float(self.purchase_price)) * int(self.shares)
		return earnings_loss

	# Calculate Anual earnings
	# Reference stock attributes
	def YearlyEarningsLoss(self):
		date_format = "%m/%d/%Y"
		current_date = datetime.date.today().strftime(date_format)
		purchase_date_days = datetime.datetime.strptime(self.purchase_date, date_format)
		current_date_days = datetime.datetime.strptime(current_date, date_format)
		ownership_years = ((current_date_days - purchase_date_days).days/365.2524)
		yearly_earnings_loss = ((((float(self.current_value) - float(self.purchase_price))/float(self.purchase_price))/float(ownership_years))*100)
		return yearly_earnings_loss


class Investor():
	"""Initialize investor"""
	def __init__(self, name, address, phone):
		self.name = name
		self.address = address
		self.phone_number = phone

# Inhertied class from stock
class Bond(Stock):
	"""This is where we create Bond information."""
	def __init__(self, symbol, quantity, purchase_price, current_value, purchase_date, coupon=0, yield_percent='0'):
		super().__init__(symbol, quantity, purchase_price, current_value, purchase_date)
		self_bond_quantity = quantity
		self_purchase_price = purchase_price
		self_current_value = current_value
		self.coupon = coupon
		self.yield_percent = yield_percent

	# Method pointing to class Stock() attributes
	def BondValue(self):
		bond_earnings = (int(self.quantity) * float( float(self.current_value) - float(self.purchase_price)))
		return bond_earnings

	# Method calculating bond percentage calculation
	def PercentBond(self):
		date_str = self.date
		datefmt = '%m/%d/%Y'
		date_obj = datetime_strptime(date_str, datefmt)
		today_date = datetime.now()
		days = (today_date - date_obj).days
		daily = ((((self.current_value - self.purchase_price) / self.purchase_price)/ ((days)) * 100))
		return daily
		yearly = ((((self.current_value - self.purchase_price) / self.purchase_price)/ ((days)/365) * 100))
		return yearly

# Get a random word from the linux system dictionary file
def getWord():
    word = random.choice(list(open('/usr/share/dict/words')))
    return word

# Generate seven random digits for temporary telephone password, value is returned.
def generateTelPass():
    c = ''
    for i in range(0,7):
        b = random.randint(0,9)
        c += str(b)
    temporary_telephone_pass = ''.join(c.split())
    return temporary_telephone_pass

# Investor Information as list
financial_investor = Investor('Bob Smith', '2150 E Evans Ave, CO 80208', '303.871.3707')

bob_smith_portfolio = { \
'stock_1': {'stock_symbol':'GOOGL', 'shares':'125', 'purchase_price':'772.88', 'current_value':'941.53', 'purchase_date': '8/1/2015'}, \
'stock_2': {'stock_symbol':'MSFT', 'shares':'85', 'purchase_price':'56.60', 'current_value':'73.04', 'purchase_date': '8/1/2015'}, \
'stock_3': {'stock_symbol':'RDS-A', 'shares':'400', 'purchase_price':'49.58', 'current_value':'55.74', 'purchase_date': '8/1/2015'}, \
'stock_4': {'stock_symbol':'AIG', 'shares':'235', 'purchase_price':'54.21', 'current_value':'65.27', 'purchase_date': '8/1/2015'}, \
'stock_5': {'stock_symbol':'FB', 'shares':'150', 'purchase_price':'124.31', 'current_value':'172.45', 'purchase_date': '8/1/2015'}, \
'stock_6': {'stock_symbol':'M', 'shares':'425', 'purchase_price':'30.30', 'current_value':'23.98', 'purchase_date': '1/10/2017'}, \
'stock_7': {'stock_symbol':'F', 'shares':'85', 'purchase_price':'12.58', 'current_value':'10.95', 'purchase_date': '2/17/2017'}, \
'stock_8': {'stock_symbol':'IBM', 'shares':'80', 'purchase_price':'150.37', 'current_value':'145.30', 'purchase_date': '5/12/2017'} \
}

# Bob Smith Bonds
bond_portfolio = Bond('GT2:GOV', '200', '100.02', '100.05', '08/01/2017', '1.38', '1.35')

dash = '-' * 79
print("Stock Ownership for " + financial_investor.name)
print(dash)
print("STOCK\t\tSHARE#\t\tEARNINGS/LOSS\t\tYEARLY%EARNINGS/LOSS")
print(dash)

for portfolio_line in bob_smith_portfolio.values():
	portfolio = Stock(portfolio_line['stock_symbol'],portfolio_line['shares'],portfolio_line['purchase_price'],portfolio_line['current_value'],portfolio_line['purchase_date'])
	print(portfolio.symbol,"\t\t",portfolio.shares,"\t\t",(portfolio.EarningsLossCalc()),"\t\t",(portfolio.YearlyEarningsLoss()))

print(dash)
print("\n")
print("Bond Ownership for " + financial_investor.name)
print(dash)
print("\n")
print("Bond          Quantity         EARNINGS/LOSS")
print(dash)
print(bond_portfolio.symbol,"\t",bond_portfolio.shares,"\t\t",bond_portfolio.EarningsLossCalc())
print(dash)
print("\n\n")
print("Use this code with your ID on the telephone system for easy identification")
print("One Time Telephone ID code: ",generateTelPass() )
print("\n\n")
print(dash)
print("\n\n")
print("Random word of the day",getWord())
