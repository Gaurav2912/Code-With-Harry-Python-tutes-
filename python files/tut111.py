def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

if __name__ == "__main__":
    
    n = int(input("Enter the number of test cases\n"))
    num_list = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        num_list.append(number)

    for i in range(n):
        print(f"Next palindrome for {num_list[i]} is {next_palindrome(num_list[i])}")
