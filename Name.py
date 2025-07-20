name = input("What is your name? ")
print("Hello, " + name + "!")


# Input can be of different types: string, integer, float, boolean
# When using an integer, it is a whole number
# When using a float, it is a number with a decimal point
# When using a string, it is a sequence of characters
# When using a boolean, it is either True or False
#bool()
# When using a boolean 0 is False and 1 is True
# When using a boolean empty string is False and non-empty string is True

number = input("Enter a number: ")
print(int(number) + 10)

# Most of the functions in python are in-built functions


name = 'Josh'
age = 19
cwa = 90.5
print("My name is " + name + ", I am " + str(age) + " years old and my CWA is " + str(cwa) + ".")


amount = 9999992928362634940402428
print(f"The amount is {amount:,} dollars.")  # Using f-string for formatting with commas
# Using f-string for better readability and performance

print(f"The amount is {amount:,.4f} dollars.")  