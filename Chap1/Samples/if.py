# これはif文のサンプルです
# __name__ 属性
# モジュールのテストコードを記述
# モジュールをコマンドとして利用
if __name__ == "__main__":
    print("Start")

a = 15
if a % 15 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else:
    print(a)
