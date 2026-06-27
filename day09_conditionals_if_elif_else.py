print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
value_a= float(input('Enter first value: '))
value_b= float(input('Enter Second value: '))
operator= (input('Enter the operator(example +,-,*,/): '))
if(operator == '+'):
    print(value_a + value_b)
elif(operator == '-'):
    print(value_a - value_b)
elif(operator == '*'):
    print(value_a * value_b)
elif operator == '/':
    print(value_a / value_b)
else:
    print("Invalid operator!")

print("Now lets convert the temperature from celcuius to fahrenheit")
temperature_celsius= float(input('Enter the temperature in Celcius(C): '))
temperature_fahrenheit= (
    (temperature_celsius*float(9/5)) + 32
)
print(temperature_fahrenheit)
