# 5! = 5 x 4 x 3 x 2 x 1 = 120
# total 1 x 1 = 1
# total 1 x 2 = 2
# total 2 x 3 = 6
# total 6 x 4 = 24
# total 24 x 5 = 120

a = int(input())
total = 1

for i in range(1, a+1):
    total = total * i
    print(i, total)

print("Factorial of", a ," is = ", total)