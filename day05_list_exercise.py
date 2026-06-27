sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

# Selling lemonade
# You sell lemonade over two weeks, the lists show the number of lemonades sold per week.
# Profit for each lemonade sold is $1.5.
# Add another day to the week 2 list by capturing a number as input.
sales_w2.append(int(input("Week 2 last day sale: ")))
# Combine the two lists into the list called sales.
# sales= sales_w1 + sales_w2
sales= sales_w1.copy()
sales.extend(sales_w2)
# Calculate/print how much you have earned on:

# Best day
best_day_sale= max(sales)
best_day= sales.index(best_day_sale)
best_day_profit = best_day_sale * 1.5
print(f'In two weeks best day is {best_day+1}th day with best sale of ${best_day_profit:.2f}.')
# Worst day
worst_day_sale= min(sales)
worst_day= sales.index(worst_day_sale)
worst_day_profit = worst_day_sale * 1.5
print(f'In two weeks worst day is {worst_day+1}th day with worst sale of ${worst_day_profit:.2f}.')
# Separately and in total
total_sales_w1=sum(sales_w1)*1.5
print(f'Total sales of first week are ${total_sales_w1:.2f}')
total_sales_w2=sum(sales_w2)*1.5
print(f'Total sales of second week are ${total_sales_w2:.2f}')
# Hint: 3 prints in total.