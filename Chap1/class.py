print("クラス")

class Man:
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        print("Initialized!(インスタンス変数の初期化)")
        
    # メソッド
    def hello(self):
        print("Hello " + self.name + "!")
        
    # メソッド
    def goodbye(self):
        print("Good-bye " + self.name + "!")
    
    # メソッド
    def name_change(self, name):
        self.name = name
        print("インスタンス変数nameを変更しました")
    
# インスタンスの生成（new がないことに注意）    
m = Man("島")
m.hello()
m.goodbye()
m.name_change("田中")
m.hello()
m.goodbye()
