marks = int(input())

if marks<=50 and marks>=0: 
    print("Fail")
elif marks>=90 and marks<=100:
    print("S Grade")
elif marks>=80 and marks<=89:
    print("A Grade")
elif marks>=70 and marks<=79:
    print("A+ Grade")
elif marks>=60 and marks<=69:
    print("B Grade")
else:
    print("maybe!")