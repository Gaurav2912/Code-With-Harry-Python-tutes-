num1 = int(input("Enter a number "))

for i in range (2,num1):
    if num1 % i == 0 :
        print("Not a prime")
        break
else:
        print("Prime")