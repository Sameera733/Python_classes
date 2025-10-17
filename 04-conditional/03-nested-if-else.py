marks = int(input())

if marks<=50: 
    if marks>=0:
        print("Fail")
    else:
        print("-ve marking is not Allowed!")
elif marks>=90:
    if marks<=100:
        print("S Grade")
    else:
        print("Not Allowed max marks are of 100")
elif marks>=80 and marks<=89:
    print("A Grade")
elif marks>=70 and marks<=79:
    print("A+ Grade")
elif marks>=60 and marks<=69:
    print("B Grade")
else:
    print("maybe!")