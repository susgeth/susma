def prime(nu):
    if nu > 1:
        for i in range(2,nu):
            if (nu % i) == 0:return "no"
            else: return "yes"
    else:return "no"
print(prime(int(input("Enter the Number"))))
