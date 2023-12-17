# （１）前回宿題の解説
class Item:
    def __init__(self, price, title):
        self.__price = price
        self.__title = title

    def edit(self, price, title):
        self.__price = price
        self.__title = title

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title

class ItemList:
    def __init__(self, sellerName):
        self.__sellerName = sellerName
        self.__list = [] # 空で初期化

    def show(self):
        for item in self.__list:
            print(str(item.price) + '円の' + item.title + 'です')
        print('〜〜〜〜') # 見やすいように区切り線を入れます
    def add(self, item):
        self.__list.append(item)
    def delete(self, price, title):
        for i, item in enumerate(self.__list):
            if item.price == price and item.title == title:
                self.__list.pop(i) # pop()の引数には、「どのインデックスの要素を削除するか」を指定する
    def edit(self, befPrice, befTitle, aftPrice, aftTitle):
        for i, item in enumerate(self.__list):
            if item.price == befPrice and item.title == befTitle:
                self.__list[i].edit(aftPrice,aftTitle) # 注意
                # 以下二つ合わせたものと、44行目は同義
                # item.price = aftPrice
                # item.title = aftTitle

l = ItemList('山田') # アカウント作成時は商品リストが空なので、コンストラクタはアカウント名のみを指定する

l.add(Item(1000, '本'))
l.add(Item(500, '文房具'))
l.add(Item(20000, '家電'))
l.show()

l.delete(500, '文房具')
l.show()

l.edit(1000, '本', 800, '文庫本')
l.show()


# 44行目について、やっていることは以下と同じ
iX = Item(1,'test1')
iY = Item(2,'test2')
arr = [iX, iY] 
print(arr) # [ (1,test1) , (2, test2) ]
arr[1].edit(100,'test100') # iY.edit(100,'test100') 二つ目の要素のみを書き換えている
print(arr) # [ (1,test1) , (100, test100) ]


# （２）8章を口頭で確認
'''
- ブレイクポイントには、４種ある
    - 一行進む
    - 関数の中に入る
    - 関数の中から出る
    - 次のブレイクポイントまで進
- 条件付きのブレイクポイントを作ることができる
- ブレイクポイントとデバッグ実行を駆使することで、不具合を見つけたりしていく
'''

# （３）9章を口頭で確認
'''
python には、「環境」がある。
環境ごとに、ライブラリをインストールする。
インストールするライブラリのバージョン管理（混在して使いたい、特定のバージョンのライブラリを使いたい）をするために、pipが存在する
'''

# （４）10章の章末問題(1)の解き方を解説
num_of_games = 48
num_of_wins = 31

# まずは愚直に
s = 'Winning percentage: ' + str(num_of_wins / num_of_games)
# つぎに、「％」を使うようにする。ひとまず%dとする
s = 'Winning percentage: %d' % (num_of_wins / num_of_games)
# テキストで小数点を示すのに、%.2fを使っているので、それと同じようにする
s = 'Winning percentage: %.2f' % (num_of_wins / num_of_games)
# 今回は、小数第3位までなので、以下にする
s = 'Winning percentage: %.3f' % (num_of_wins / num_of_games)

print(s)

# 補足として、以下の書き方も可能
s = 'Winning percentage: ' + str(round((num_of_wins / num_of_games), 3)) # round()は、四捨五入するための関数