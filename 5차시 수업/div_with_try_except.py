try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a)/int(b)
    print('{}/{} = {}'.format(a, b, result))
except:
    print('수가 정확한지 확인하세요')