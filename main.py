# if and else
age = int(input("What is your age: "))
print(age)
if age > 18:
    print("You are eligible to vote :)")
else:
    print("You are not eligible to vote :( \n You can vote after", 18 - age, "years")

if age >= 80:    
    print("You are eligible to vote, but you should consider retirement :)")
 