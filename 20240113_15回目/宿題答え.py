def isPrefix(s, t):
    isPrefix = True
    for i in range(len(s)):
        if s[i] != t[i]:
            isPrefix = False
    return isPrefix

# isSufixは以下の4通りの解がある
def isSufix_1_1(s,t):
    isPrefix = True
    for i in range(len(s)): # 0,1
        if s[len(s) - 1 - i] != t[len(t) - 1 - i]: # 0: s[1]!=t[3], 1: s[0]!=t[2]
            isPrefix = False
    return isPrefix
def isSufix_1_2(s,t):
    isPrefix = True
    for i in range(0, len(s), 1): # 1,2
        if s[len(s) - i] != t[len(t) - i]: # 0: s[1]!=t[3], 1: s[0]!=t[2]
            isPrefix = False
    return isPrefix
def isSufix_2_1(s,t):
    isPrefix = True
    for i in reversed(range(len(s))): # 1,0
        if s[ i - len(s) ] != t[ - (len(s) - i) ]:# 1: s[-1]!=s[-1], 0: s[-2]!=t[-2]
            isPrefix = False
    return isPrefix
def isSufix_2_2(s,t):
    isPrefix = True
    for i in reversed(range(len(s))): # 1,0
        # if s[ ? ] != t[ ?]:# 1: s[1]!=t[3], 0: s[0]!=t[2] # ? を埋めたい
        if s[ i ] != t[ i + (len(t)-len(s))]:# 1: s[1]!=t[3], 0: s[0]!=t[2]
            isPrefix = False
    return isPrefix

print(isSufix_2_2('xy','abxy'))     # True とでるのが正解
print(isSufix_2_2('bbbb','bbbb'))   # True とでるのが正解
print(isSufix_2_2('bb','baaa'))     # False とでるのが正解

def prefix_suffix_check(s, t):
    if isPrefix(s,t) and isSufix(s,t):
        print(0)
    elif isPrefix(s,t) and not isSufix(s,t):
        print(1)
    elif not isPrefix(s,t) and isSufix(s,t):
        print(2)
    else:
        print(3)
    # if isPrefix(s,t):
    #     if isSuffix(s,t):
    #         print(0)
    #     else:
    #         print(1)
    # else:
    #     if isSufix_N_N(s,t):
    #         print(2)
    #     else:
    #         print(3)

# prefix_suffix_check('abc','abcdefg') # 1 と表示されるのが正解
# prefix_suffix_check('abc','aabc')    # 2 と表示されるのが正解
# prefix_suffix_check('abc','xyx')     # 3 と表示されるのが正解
# prefix_suffix_check('abc','abc')     # 0 と表示されるのが正解
# prefix_suffix_check('abc','abc-abc') # 0 と表示されるのが正解
