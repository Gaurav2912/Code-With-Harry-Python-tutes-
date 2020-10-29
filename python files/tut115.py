import random

def guess_num(initial,final,rand_num):
    n_guess = 0
    while True:
        n_guess += 1
        inp = int(input(f"Guess a number between {initial} and {final}:  "))
        if inp < rand_num:
            print("Your number is small.")
        elif inp > rand_num:
            print("Your number is large.")
        else:
            print(f"Correct answer you guess {n_guess} times")
            break
    return n_guess


initial = int(input("Enter initial boundry number: "))
final = int(input("Enter final boundry: "))
rand_num1 = random.randint(initial, final)
rand_num2 = random.randint(initial, final)


# Player A
print("Player A")
gA = guess_num(initial,final,rand_num1)

# Player B
print("Player B")
gB = guess_num(initial,final,rand_num2)


if gA<gB:
    print("Player A won the game.")
elif gA>gB:
    print("Player B won the game.")
else:
    print("Match draw.")
