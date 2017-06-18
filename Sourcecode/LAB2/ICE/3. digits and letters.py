s = input("Please enter the string:")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    if c.isalpha():
        l=l+1
    else:
        pass
print("digits:", d)
print("letters", l)



