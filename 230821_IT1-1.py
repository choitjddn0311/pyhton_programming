#함수기반
# def fact(n):
#     out = 1 #결과값
#     for i in range(1,n+1):
#         out*=i
#     return out

# print(fact(5))

#재귀함수 기반 
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n *fact(n-1)

# print(fact(5))

#15p
# dictionary = {
#     1:1,
#     2:2
# }

# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     else:
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output
    
# print("fibonacci(10):", fibonacci(10))
# print("fibonacci(20):", fibonacci(20))
# print("fibonacci(30):", fibonacci(30))
# print("fibonacci(40):", fibonacci(40))
# print("fibonacci(50):", fibonacci(50))


def flatten(data):
    out = [] #결과 리스트 저장(평탄화)
    for item in data:
        if type(item) == list:
            out = out+flatten(item)
        else:
            out.append(item)
    return out

   
example = [[1,2,3],[4,[5,6]],7,[8,9]] 
print("원본:",example)
print("변환:",flatten(example))