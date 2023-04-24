#Dahan, Regine Fae M. Dahan BSCPE 1-5 File Handling No.1

#open numbers.txt
with open("numbers.txt") as integers_file:
#read numbers.txt
    for line in integers_file:
        print(line.strip())
#if the number is even
#   write it in even.txt
#if the number is odd
#   write it in odd.txt
