number = int(input("Enter a number to check Prime or Not: "))
flag = 0
if number <= 1:
    print("Prime starts from 2")
else:
    for X in range(2, number+1):
        if number % X == 0:
            flag += 1

if flag==1:
    print("Prime Number")   
else:
    print("It's Not a Prime Number")