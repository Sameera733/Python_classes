import sys

demo=1
name="Ateeq"
isOnline=True
age=24.78

print(demo)
print("My name is:",name,"I am Online:",isOnline,"and my age is:",age)

# Formatting the string
# Using new line
print(f"My name is :{name},\n I am Online: {isOnline} \n and my age is: {age}")
# Using tab space
print(f"My name is :{name},\t I am Online: {isOnline} \t and my age is: {age}")

#Type of variables

print(type(demo))

print(type(name))

print(type(isOnline))

print(type(age))

print(sys.getsizeof(name))
print(sys.getsizeof(demo))