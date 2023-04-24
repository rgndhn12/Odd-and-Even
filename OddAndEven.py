#Dahan, Regine Fae M. Dahan BSCPE 1-5 File Handling No.1

#introduction
import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()
the_intro = 'HELLO'
print(Fore.CYAN+pyfiglet.figlet_format(the_intro,font="isometric1"))
time.sleep(1)
border = "—" * 100
print(border)
print(Fore.LIGHTMAGENTA_EX+' This Program is entitled OddAndEven. It will separate the odd and even from twenty integers.')
print(border)
time.sleep(2)

print(Fore.LIGHTRED_EX+pyfiglet.figlet_format("THE INTEGERS ARE...",font="digital"))
time.sleep (2) 

#open numbers.txt
with open("numbers.txt", "r") as integers_file, open ("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:



#read numbers.txt
    for line in integers_file:
        print(line.strip())
        integers_file = int(line)


#if the number is even
        if integers_file % 2 != 1:

#   write it in even.txt
            even_file.write(str(integers_file) +"\n")

#if the number is odd
        else:
            
#   write it in odd.txt
            odd_file.write(str(integers_file) +"\n")

print(border)
time.sleep(2)
print(Fore.CYAN+pyfiglet.figlet_format("The Even Integers...",font="digital"))
time.sleep(2)

#display the even integers
with open ("even.txt", "r") as even_file:
    for line in even_file:
        print("*"*5)
        print(line.strip())

time.sleep(2)
print(Fore.GREEN+pyfiglet.figlet_format("The Odd Integers...",font="digital"))
time.sleep(2)

#display the odd integers
with open("odd.txt", "r") as odd_file:
    for line in odd_file:
        print("*"*5)
        print(line.strip())

#outro
print(border)
time.sleep(2)
print(Fore.CYAN+pyfiglet.figlet_format("THANK YOU",font="isometric1"))


