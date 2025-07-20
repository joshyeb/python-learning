#Loops allow you to run a block of code multiple times.

# For loops
# for iteration in range():
for i in range(1, 11): ## This will iterate from 1 to 10
    print(i)

for i in range(20):   ##This will iterate from 0 to 19
    print(i)

for i in range(1,100,2): ## this will iterate from 0 to 99 with an interval of 2, the 2 is called stepping value
    print(i)


## Even numbers between 1 and 100
for i in range (0,101,2) :  
    print(i)

## Odd numbers between 1 and 100
for i in range (1,100,2):
    print(i)

## However , if you want your range of numbers to count down , your stepping number must be negative
#Example
for i in range (100,1,-2):
    print(i)

