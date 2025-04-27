fname = input('입력할 파일의 이름: ')

try:
    f = open(fname, 'r') # 파일 열기
    content = f.read()
    print(content)
except FileNotFoundError:
    print(f"{fname} 파일이 존재하지 않습니다.")
except IOError:
    print(f"{fname} 파일을 읽을 수 없습니다.")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    try:
        f.close()
    except:
        pass