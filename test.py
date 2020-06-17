# print/input operation with data structure protection
x = ["It's just a simple test", "Right now I need your help", "Please input your age"]
print(*x, sep='. ')
inputAge = input()
while not inputAge.isdigit():
    print("It's not an valid number. please input again")
    inputAge = input()

if int(inputAge) >= 18:
    print("Hello, It's seems your are an adult, now I can converse with you now")
else:
    print("I am sorry, your are not an adult", "I can't talk to you", "Bye", sep=". ")

# file read/write operation
with open("log.txt", 'a') as logFile:  # a=append w=overwrite r=read only
    print("The user age:", int(inputAge), file=logFile)

# help(print)    # the syntax to get function help

str = "Hello"

nums = [1,2,3]
reversed(nums)
print(nums)
if len(nums) >=0:
    if nums[0] == nums[len(nums)-1]:
      print("correct")
print("wrong")
