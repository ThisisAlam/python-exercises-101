msg= "Welcome to python's exercises 101!"
print(msg)
print(msg+msg)
print(msg*2)
print(msg,msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.count('python'))
print(msg.count('o'))
# msg= "Welcome to python's exercises 101!"
      # 0123456789...
print(msg[0])
print(msg[-1])
print(msg[-3])
print(msg[2:])
print(msg[2:7])
print(msg[:7])
# print(msg[welcome])

msg_2= "Welcome to Python 101: Strings"
msg_2= msg_2.lower()
one_start= msg_2.find('1')
w_start= msg_2.find('welcome')
r_start= msg_2.find('ring')
t_start= msg_2.find('to')
name='tyler'

msg_new= (
    msg_2[one_start] + " " + 
    msg_2[w_start:w_start+7].title() + " " +
    msg_2[r_start:r_start+4].title() + " " +
    msg_2[t_start:t_start+2] + " " +
    name.title()
)

print(msg_new)
# # Should return "1 Welcone Ring to Tyler"

# string = "Welcome to Python 101: Strings"
# Can you print:
# sgnirtS

string = "Welcome to Python 101: Strings"
string= string.lower()
start= string.find('string')
word_string= string[start:start+7].title() 
reversed_word_string=word_string[::-1]
print(reversed_word_string)

sentc = "Google is you friend"
reverse_sentc = sentc[::-1]
print(reverse_sentc)