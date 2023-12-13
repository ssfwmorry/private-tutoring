def adder(a):
    def inner(x):
        # xは関数内関数の引数、aはadder呼び出し時の引数
        return x + a
    return inner # a に対して何かを足す関数

# # クロージャを作成し、add3, add5に代入する
add3 = adder(3) # 3に対して"何か"を足す関数
add5 = adder(5)

# # add3, add5に代入されたクロージャを呼び出す
# print(add3(10))
# print(add5(10))

# print(add3(10))
# # は以下と同じ
# print((adder(3))(10))

# print(innner(10))
# print (10 + 3) # 13


def func(**kwargs):
    print(kwargs)

func()                   # {}
func(a=1, b=2)           # {'a': 1, 'b': 2}
func(a=1, b=2, c=3, d=4) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
func(**{'a': 1, 'b': 2, 'c': 3, 'd': 4}) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
