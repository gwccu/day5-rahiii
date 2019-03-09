# File name: problemSetDay5.py
for i in range(4):
    print(i)
for i in range(5,8):
    print(i)
for i in range(5,18,3):
    print(i)
for i in range(0,31,5):
    print(i)

guess1= 0
while guess1 != 5:
    print(guess1)
    guess1 += 1
guess2= 5
while guess2 != 8:
    print(guess2)
    guess2 += 1
guess3= 5
while guess3 != 20:
    print(guess3)
    guess3 += 3
guess4= 0
while guess4 != 35:
    print(guess4)
    guess4 += 5

for i in range(1,8,2):
    print("*"* i)

for i in range(1,8,2):
    print(" " * (4-(i-1)) + "*" * i)

for i in range(1500,1700,5):
    if i%7 == 0:
        print(i)

number= int(input("print a number 1-10"))
print (("*")*number)