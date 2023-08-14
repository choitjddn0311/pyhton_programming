# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# print_3_times()

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요" , 2000)

# def print_n_times(n , *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(3, "안녕하세요", "즐거운" , "파이썬 프로그래밍")

# values = input("함수 값을 입력하세요")
# def print_n_times(values , n):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
# print_n_times(values , 3)

# n = int(input("출력할 횟수를 입력하세요.:"))
# def  print_n_times(n , *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(n , "안" , "녕" , "하")

# def return_test():
#     return 3*2


# value = return_test()
# print(value)

def mul(*values):
    out = 1
    for value in values: ## values 가변 함수에 입력값을 따로 받기
        out = out * value
    return out

print(mul(5, 7, 9, 10))


### 수행 평가 ###
## 확인문제 처럼 문제를 출제하고 문제 풀기 안되면 영상 녹화 코드 설명##
