no_of_inp = int(input("Enter the number of input : "))

for i in range(no_of_inp):
    var_1 = input("Enter the number that you want to palindrome: ")
    var_save = var_1

    while True:
        var_1 = int(var_1)
        var_1 = var_1 + 1
        var_1 = str(var_1)
        var_3 = var_1[::-1]
        if var_1 == var_3 :
            break
    
    print(f"The palindrome of {var_save} is {var_1}")
