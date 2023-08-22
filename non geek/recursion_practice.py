def printFun(test):
    if test < 1:
        return 
    else:
        print(test, end=" ")
        printFun(test - 1)
        print(test, end= " ")
        return 


def func2(n):
    if n == 0:
        return 
    print(n, n//2)
    func2(n//2)
    print(n % 2, end=" ")

# Driver code
#test = 3
#printFun(test)
func2(21)