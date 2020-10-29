try:
    n_app =  int(input("Enter the number of apples: "))
    mn = int(input("Enter the minimum numbers of students: "))
    mx = int(input("Enter maximum number of student: "))
    if mn<=mx:
        for i in range(mn,mx+1) :
            if n_app % i == 0 :
                print(i," is divisor of ",n_app)
            else:
                print(i," is not divisor of ",n_app)
    else :
        print("minmum number should be less then or equal to maximum number.")

except Exception as e :
    print("Input should be Integer")


