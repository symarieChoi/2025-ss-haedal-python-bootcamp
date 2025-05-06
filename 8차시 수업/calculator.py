from tkinter import *

IVORY = "#FFF8EA"
PINK = "#EEA6C8"
BLUE = "#A6D1FF"
GREEN = "#28917C"

# 함수 생성
def clicked(digit):
    if digit == "←":
        # 하나씩 숫자 삭제
        input_entry.delete(len(input_entry.get())-1)
    else:
        input_entry.insert(END, digit)
    
def del_digit():
    input_entry.delete(0, END)
    result_label.config(text="")

def calculate():
    # 예외처리
    try:
        result = eval(input_entry.get())
    except:
        result_label.config(text="계산식 오류")
    else:
        result_label.config(text=result)

def return_key(event):
    calculate()

# window 창 생성
window = Tk()
window.title("계산기")
window.resizable(False, False)
window.config(padx=10, pady=10, bg=IVORY)

digits = [
    ['7', '8', '9', '*'],
    ['4', '5', '6', '/'],
    ['1', '2', '3', '-'],
    ['0', '.', '←', '+']
]

# 엔트리 생성
input_entry = Entry(window, width=30, font=("나눔바른펜", 20),
                    bg=IVORY, justify=RIGHT)
input_entry.grid(column=0, row=0, columnspan=4)
input_entry.focus()

# 레이블 생성
result_label = Label(window, text="test", width=20, font=("나눔바른펜", 30), bg = IVORY)
result_label.grid(column=0, row=1, columnspan=4, pady=15)

# 버튼 배치
for r in range(4):
    for c in range(4):
        digit = digits[r][c]
        button = Button(window, text=digit, width=8, font=("나눔바른펜", 15),
                        bg = PINK, command = lambda x = digit:clicked(x))
        button.grid(row=r+2, column=c, pady=2)

# 추가 버튼 생성(clear, calculate)
clear_button = Button(window, text="C", width=17, font=("나눔바른펜", 15, "bold"),
                      bg=BLUE, command=del_digit)
clear_button.grid(column=0, row=6, columnspan=2, pady=5)
cal_button = Button(window, text="=", width=17, font=("나눔바른펜", 15, "bold"),
                      bg=BLUE, command=calculate)
cal_button.grid(column=2, row=6, columnspan=2, pady=5)

# 엔터키 먹히게 적용
window.bind("<Return>", return_key)

window.mainloop()