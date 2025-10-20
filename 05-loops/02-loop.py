
listOfstudents = ["ali", "x", "y", "z"]
print(len(listOfstudents))

lengthOflist = len(listOfstudents)

# print(listOfstudents[0])
# print(listOfstudents[1])
# print(listOfstudents[2])


for x in range(0, lengthOflist):
    print(listOfstudents[x])


for x in range(0, lengthOflist):
    user = int(input())
    print(listOfstudents[user])


#tasks
# 1. repeat above program in tuple, dict, string
# 2. create a list, tuple, dict using for loop take user inputs after printing 