str = 0
for i in range(0,int(input())):
    for j in range(0,i+2):
        print(chr(j+65), end=" ")
        str += 1
    print()