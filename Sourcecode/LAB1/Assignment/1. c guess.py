import random

a = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
a = " ".join(str(x) for x in a)
a = int(a)


N = input('Enter Number to guess:')
N = int(N)

if (N > a):
    print("\nYour answer is high than required")
elif (N < a):
    print("\nYour answer is low than required")
else:
    print("\nYour answer is PERFECT!! Congratulations!")