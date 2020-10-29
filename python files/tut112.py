def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

n = int(input("Enter the number of test cases\n"))
num_list = []

for i in range(n):    
    num_list.append(int(input("Enter the number:\n")))

print(f"Next palindrome for {[num_list[i] if num_list[i] <10 else next_palindrome(num_list[i]) for i in range(n)]}")

# for i in range(n):
#     if num_list[i] > 9 :
#         print(f"Next palindrome for {num_list[i]} is {next_palindrome(num_list[i])}") 
#     else:            
#         print(f"palindrome for {num_list[i]} is {num_list[i]}")