# これは型キャストのサンプルです
if __name__ == "__main__":
    print("型キャスト")

num = 10
string = '20'
print("数字と文字列の算術演算")
print(num + int(string))
print(num + float(string))
print(float(num) + int(string))

print("文字列と数字の文字列連結")
print(str(1) + "23")
print("01" + str(5))