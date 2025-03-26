n = int(input("정수 n을 입력하시오: "))

for i in range(1, n + 1):
    if i > 100:
        break
    elif i % 7 == 0:
       continue
    print(i)