# Initilization of list
list_food = []

#Take input as a list
while True :
    inp = input("Enter a to add item in list. c to close the list: ")
    if inp == 'a':
        item = input("Enter name of food: ")
        list_food.append(item)
    elif inp == 'c':
        break
    else:
        print("Wrond input")

print(list_food)

#Reverse list by first method
rev_1 = list_food[:]
rev_1.reverse()
print("By first method",rev_1)

#Reverse list by secound method
rev_2 = list_food[:]
print("By secound method",rev_2[::-1])

#Reverse list by third method
rev_3 = list_food[:]
n = len(rev_3)
i = 0
while (i<n/2):
    it = rev_3[i]
    rev_3[i] = rev_3[n-1-i] 
    rev_3[n-1-i] = it
    i = i+1 
print("By third method",rev_3)