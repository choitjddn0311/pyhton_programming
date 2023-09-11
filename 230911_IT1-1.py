import random

rn = random.randrange(1,10,2)
print("랜덤 : {}".format(rn))
num = int(input("숫자를 입력하세요. :"))
print(num)

if rn == num:
    print("같은 숫자입니다.")
else:
    print("다른 숫자입니다.")