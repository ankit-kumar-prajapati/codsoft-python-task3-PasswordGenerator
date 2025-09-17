import sys
import random
try :
    length=int(input("Enter the length of the password : "))
    if length<=0:
        raise Exception("Wrong length entered!")
except ValueError:
    print("Invalid input! Try again.")
    sys.exit(0)
except :
    print("Wrong length entered! Try again")
    sys.exit(0)
small_alpha='abcdefghijklmnopqrstuvwxyz'
capital_alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
random_characters='!@#$%^&*()-_+=:;.'
char=small_alpha+capital_alpha+digits+random_characters
password=''
while(length>0):
    password=password+random.choice(char)
    length-=1
print(f'The password is {password}')
