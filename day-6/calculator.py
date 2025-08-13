print("1. Add\n2. Substract\n3. divide\n4. multiplay 5. Modulus \n6. power\n7. exit")
n = int(input("Enter the choice : "))
while n != 7:
    print("Enter two numbers")
    a = int(input("Entre the first number : "))
    b = int(input("Entre the Second number : "))
    if n == 1:
        print(a+b)
    elif n == 2:
        print(a-b)
    elif n == 3:
        print(a/b)
    elif n == 4:
        print(a*b)
    elif n == 5:
        print(a%b)
    elif n==6:
        print(a**b)    
    else:
        print("Invalid opction")
    
    print("1. Add\n2. Substract\n3. divide\n4. multiplay 5. Modulus \n6. power\n7. exit")
    n = int(input("Enter the choice : "))

print("Calculator exited.")
