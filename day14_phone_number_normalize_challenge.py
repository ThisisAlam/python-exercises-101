# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
number= input("Enter the 10 digit U.S. phone number: **any format** ")
# 2. Use .strip() to remove any leading/trailing spaces.
number= number.strip()
# 3. Replace common separators (-, (, ), .) with spaces.
number= (
    number.replace('-',' ')
    .replace(')',' ')
    .replace('(',' ')
    .replace('.',' ')
)
# 4. Use .split() to break into chunks, then .join() to merge the digits.
number= number.split()
number= "".join(number)
# # 5. Check if the cleaned number has **exactly 10 digits**.
# 7. If not, print an error message: "Please enter exactly 10 digits."
if len(number) != 10:
    print("Invalid Phone number. The number is not a 10 digit number.")
    print(number, type(number))
else:
    number_str = f'({number[:3]}) {number[3:6]}-{number[6:]}'
    print(number_str, type(number_str))
# 6. If yes, format it like this: (123) 456-7890
# 123(45)-6-7.89)0