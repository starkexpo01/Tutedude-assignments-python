skj = int(input("Enter a number: "))
def factorial(bsj):
    if bsj == 1:
        return 1
    else:
        return bsj * (factorial(bsj -1))
result = factorial(skj)
print("Factorial of",skj,"is:",result)