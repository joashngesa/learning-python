#remove negatives
#reduce each by 5%
#calculate total
#return values above 200

sales = [120, -40, 300, 80, -10, 500]

#removing the negatives
def clean_sales(sales):

    cleaned_sales = [cln for cln in sales if cln > 0]
    return cleaned_sales

#reduce each by 5%
def reduced_sales(cleaned_sales):

    after_reduction = [(rdc * (1-0.05)) for rdc in cleaned_sales]
    return after_reduction

#calculate total

def totals(after_reduction):

    total = 0

    for tot in after_reduction:
        total += tot
    return total

#return values above 200
def above_200(after_reduction):

    above200 = [abv for abv in after_reduction if abv > 200 ]
    return above200

cleaned = clean_sales(sales)
reduced = reduced_sales(cleaned)
total_sales = totals(reduced)
sales_above_200 = above_200(reduced)

print("Cleaned data: ",cleaned)
print("Reduced sales: ",reduced)
print("Total sales: ",total_sales)
print("Sales above 200: ",sales_above_200)


#all in one function
def data_pipeline(sales):
    
    cleaned_sales = [cld for cld in sales if cld > 0]

    discount = 0.05
    discounted_sales = [(dis * (1-discount)) for dis in cleaned_sales]

    revenue = 0
    for rev in discounted_sales:
        revenue += rev
    
    sales_above_200 = [sls for sls in discounted_sales if sls > 200]

    return cleaned_sales, discounted_sales, revenue, sales_above_200

sales = [120, -40, 300, 80, -10, 500]

cleaned_sales, discounted_sales, revenue, sales_above_200 = data_pipeline(sales)

print("Cleaned sales: ",cleaned_sales)
print("Discounted sales: ",discounted_sales)
print("Revenue: ",revenue)
print("Sales above 200: ",sales_above_200)



