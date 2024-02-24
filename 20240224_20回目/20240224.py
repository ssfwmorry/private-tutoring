'''
1. すべての文字列に対して、1 文字目は H , D , C , S のどれかである。
2. すべての文字列に対して、2 文字目は A , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , T , J , Q , K のどれかである。
3. すべての文字列は相異なる。
'''

def isInclude(s, list):
    for i in list:
        if i == s:
            return True
    return False

# 1. すべての文字列に対して、1 文字目は H , D , C , S のどれかである。
# 例: (4, ['H3','DA','D3','SK'])
def ueHantei(n, list):
    ret = True # 一旦Trueとする
    # どれかひとつでも満たさない場合は、Falseとする
    for i in range(n):
        s = list[i] # H3, DA, D3, SK
        # if sの一文字目がH , D , C , S のどれかでではない
        if not s[0] in ['H', 'D', 'C', 'S']:
        # if isInclude(s[0], ['H', 'D', 'C', 'S']):
            ret = False
    return ret

# 2. すべての文字列に対して、2 文字目は A , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , T , J , Q , K のどれかである。
def mannakaHantei(n, list):
    ret = True
    # どれかひとつでも満たさない場合は、Falseとする
    for i in range(n):
        s = list[i]
        if not s[1] in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            ret = False
    return ret

# 3. すべての文字列は相異なる。
def shitaHantei(n, list):
    ret = True
    for i in range(len(list)):
        for j in range(len(list)):
            # 同じインデックスを参照しているとき、次のループにいく
            if i == j:
                continue
            # 同じものがある場合
            if list[i] == list[j]:
                ret = False
        ''' 以下のコードは、ループごとに回数を減らす場合
        # i = 0 のとき j = [1, 2, 3]
        # i = 1 のとき j = [   2, 3]
        # i = 2 のとき j = [      3]
        # i = 3 のとき j = [       ]
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                ret = False
        '''
    return ret

def resolve(n, list):
    ret = False
    if ueHantei(n,list) == True and mannakaHantei(n,list) == True and shitaHantei(n,list) == True:
        ret = True
    else:
        ret = False
    print(ret) # True or False
    ''' 以下のコードは、if文を分岐させる場合
    if ueHantei(n,list) == False:
        print(False)
        return
    elif mannakaHantei(n,list) == False:
        print(False)
        return
    elif shitaHantei(n,list) == False:
        print(False)
        return
    else:
        print(True)
        return
    '''


#resolve(4, ['H3','DA','D3','SK'])      # True となるのが正解。
#resolve(5, ['H3','DA','CK','H3','S7']) # False となるのが正解。'H3' が 3. を満たしていないため
#resolve(4, ['3H','AD','3D','KS'])      # False となるのが正解。'3H' が 1. と 2. を満たしていないため
#resolve(5, ['00','AA','XX','YY','ZZ']) # False となるのが正解。'00' が 1. を満たしていないため
