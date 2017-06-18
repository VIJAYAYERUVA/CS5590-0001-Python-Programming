input = input("enter the string : ")

def counts(input):
    dict = {}
    for char in input:
        dict[char] =0
        #print(dict)
    for char in input:
        dict[char] +=1
        #print(dict)
    print(dict)

counts(input)