string = (input("enter the string: "))

rev_string=(string[::-1])
if string==rev_string:
    print("palindrome")
else:
    print("not a palindrome")