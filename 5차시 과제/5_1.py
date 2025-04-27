try:
    a = input("첫 번째 숫자: ")
    b = input("두 번째 숫자: ")
    op = input("연산자(+, -, *, /): ")

    if op == '+':
        result = int(a) + int(b)
    elif op == '-':
        result = int(a) - int(b)
    elif op == '*':
        result = int(a) * int(b)
    elif op == '/':
        result = int(a) / int(b)
except ValueError:
    print("숫자만 입력 가능합니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(f"결과: {result}")
finally:
    print("종료")