'''
20.

def value(arg):
    return arg

result1 = value(0) and value(1) and value(2)
# result1 = 0 and 1 and 2
result2 = value(0) or value(1) or value(2)
# result2 = 0 or 1 or 2

print(result1, result2) # 0, 1 / Flase, Ture

x = True and False and True
print(x)

if -1:
    print('e')
# 0 : Flase
# 0以外: True

a=1
b=0
if a==0 or b==1:
    print('r')

'''





def testReturn1():
    return 1


if testReturn1() == 1:
    print('正しい')
else:
    print('正しくない')