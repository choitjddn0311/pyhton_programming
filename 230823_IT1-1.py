# tuple_test = (10,20,30)

# print(tuple_test[0])
# print(tuple_test[1])
# print(tuple_test[2])

# [a , b] = [10 , 20]
# (c , d) = (10 , 20)

# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)

# tuple_test = 10 ,20 ,30 ,40
# print("# 괄호가 없는 튜플의 값과 자료형 출력")
# print("tuple_test :", tuple_test)
# print(type(tuple_test))
# print()

# a,b,c = 10,20,30
# print("#괄호가 없는 튜플을 활용한 할당")
# print("a:" , a)
# print("b:" , b)
# print("c:" , c)

# numbers = [1, 2, 3, 4, 5, 6]

# print("::".join(map(str,numbers)))

numbers = list(range(1, 10+1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x %2 == 1,numbers)))
print()

print("# 3이상 , 7 미만 추출하기")
print(list(filter(lambda x : 3<=x<7,numbers)))
print()

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda x: x*x<50,numbers)))