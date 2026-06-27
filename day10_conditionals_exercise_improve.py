month_input= input('enter the name of the month(example jan, feb, mar, etc): ').lower()
def num_days(month):
    month_31 = {'jan','mar','may','jul','aug','oct','dec'}
    month_30 = {'apr','jun','sep','nov'}
    month_28= {'feb'}
    if month in month_31:
        print(f'number of days in {month.upper()} are: 31')
    elif month in month_30:
        print(f'number of days in {month.upper()} are: 30')
    elif month in month_28:
        print(f'number of days in {month.upper()} are: 28')
    else:
        print('Invalid month')
num_days(month_input)
# optimize/shorten the code in the function
# try to reduce the number of conditionals 
