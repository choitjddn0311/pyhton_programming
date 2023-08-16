#팩토리얼 함수로 구현하기
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print("5!:" , factorial(5))

#팩토리얼 재귀함수로 구현하기
def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    
print("5!:" , factorial(5))