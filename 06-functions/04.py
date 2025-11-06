# 5! = 5 x 4 x 3 x 2 x 1 = 120

# fact 5 if(5==1) false                     = total = 120
    # total = 5 * fact(5-1)                 = 5 * 24 = 120
        #fact(4) if(4==1) false
#           total = 4 * fact(4-1)           = 4 * 6 = 24
            # fact(3) if(3==1) false
#           total = 3 * fact(3-1)           = 3 * 2 = 6
                # fact(2) if(2==1) false
#               total = 2 * fact(2-1)       = 2 * 1 = 2
                    # fact(1) if(1==1) true return a , a=1

# total = 1
def fact(a):
    if(a==1): return a
    total = a * fact(a-1)
    return total
    # print(total, a)

print(fact(5))
