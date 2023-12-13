# def deco(func):
#     def wrapper(*args, **kwargs):      # args:(10, 20), kwargs:{}
#         print('*args:', args)          # *args: (10 ,20)
#         print('**kwargs:', kwargs)     # **kwargs: {}
#         result = func(*args, **kwargs) # result = 30
#         print('result:', result)       # 30
#         return result
#     return wrapper

# @deco
# def add(a, b):
#     return a + b

# add(10, 20)
# # add(b=30, a=40)






# def deco2(func): # 「deco2 は囲まれた処理をするもの、とします」 宣言・定義
#     def wrapper():
#         print('bbb')
#         func() # print('aaa')
#     return wrapper

# @deco2
# def funcP():
#     print('aaa')

# funcP() ## 実行



# class Person:
#     def greet(self):
#         print('greet')

#     @classmethod
#     def info(cls):
#         print('info')

# alice = Person()
# bob = Person()

# alice.greet()

# Person.info()
# # alice.info()
# # bob.info()


# class Animal:
#     def eat(self):
#         print('eat')

# class Cat(Animal):
#     def eat(self):
#         super().eat()

# c = Cat()
# c.eat()
# c.eat_animal()




j = Japanese()
c = Chainese()

list = [j,c]

def func(list):
    for p in list:
        p.greet()