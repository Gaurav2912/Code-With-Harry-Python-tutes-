import random

initial = int(input("Enter initial boundry number: "))
final = int(input("Enter final boundry: "))

rand_num1 = random.randint(initial,final)

i = 0
j  = 0

# Player A
print("Player A")
while True:
    i += 1
    inp_A = int(input("Guess a number: "))
    if inp_A < rand_num1:
        print("Your number is small, guess  again: ")
    elif inp_A > rand_num1:
        print("Your number is large,guess again: ")
    else:
        print(f"Correct answer you guess {i} times")
        break

rand_num2 = random.randint(initial,final)

# Player B
print("Player B")
while True:
    j += 1
    inp_B = int(input("Guess a number: "))
    if inp_B < rand_num2:
        print("Your number is small, guess  again: ")
    elif inp_B > rand_num2:
        print("Your number is large,guess again: ")
    else:
        print(f"Correct answer you guess {j} times")
        break

if i<j:
    print("Player A won the game.")
elif i>j:
    print("Player B won the game.")
else:
    print("Match draw.")