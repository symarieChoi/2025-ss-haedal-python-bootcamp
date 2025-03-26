age = 0
age = int(input("정수 age를 입력하세요: "))

if 0 <= age <= 12:
    print(500)
elif 13 <= age <=18:
    print(1000)
elif 19 <= age <= 64:
    print(2000)
elif age >= 65:
    print(0)
