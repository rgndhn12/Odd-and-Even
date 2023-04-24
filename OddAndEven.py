#Dahan, Regine Fae M. Dahan BSCPE 1-5 File Handling No.1

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
        
#   write it in odd.txt

