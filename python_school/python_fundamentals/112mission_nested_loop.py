
sales = [
    [101, "Laptop", 1000],
    [102, "Phone", -200],
    [103, "Tablet", 500],
    [104, "Monitor", -100],
    [105, "Keyboard", 64],
    [106, "Mouse", 34]
]
#Remove negative prices
def sales_cleaning(sales):
    cleaned_sales = []
    for row in sales:
        if row[2] > 0:
            cleaned_sales.append(row)
    return cleaned_sales

#Increase prices by 10%
def increased_prices(cleaned_sales):
    price_inc_rate = 0.1
    inc_sales = []
    for row in cleaned_sales:
        new_row = [row[0], row[1], round(row[2] * (1 + price_inc_rate))]
        inc_sales.append(new_row)
    return inc_sales

#Calculate total revenue
def revenue_calc(inc_sales):
    income = 0.0
    for row in inc_sales:
        income += row[2]
    return income

#Return products above 800
def sales_above_800(inc_sales):
    above800 = [row for row in inc_sales if row[2] > 800]
    return above800

cleaned = sales_cleaning(sales)
increased = increased_prices(cleaned)
revenue = revenue_calc(increased)
salesover800 = sales_above_800(increased)

print("Cleaned sales: ",cleaned)
print("Increased sales: ",increased)
print("Revenue: ",revenue)
print("Sales above 800: ",salesover800)

#In the results i dont understand why the cleaned sales are presented as already increased
#below are the results..
#Cleaned sales:  [[101, 'Laptop', 1100.0], [103, 'Tablet', 550.0], [105, 'Keyboard', 70.4], [106, 'Mouse', 37.400000000000006]]
#Increased sales:  [[101, 'Laptop', 1100.0], [103, 'Tablet', 550.0], [105, 'Keyboard', 70.4], [106, 'Mouse', 37.400000000000006]]
#Revenue:  1757.8000000000002
#Sales above 800:  [[101, 'Laptop', 1100.0]]

teachers = [
    [1, "John", 80],
    [2, "Mary", 90],
    [3, "Alex", 70]
]
cleaned = sales_cleaning(teachers)
print("Teachers: ",teachers)