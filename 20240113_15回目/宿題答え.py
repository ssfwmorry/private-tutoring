def isPrefix(s, t):
    isPrefix = True
    for i in range(len(s)):
        if s[i] != t[i]:
            isPrefix = False
    return isPrefix

def isSufix(s, t):
    isSuffix = True
    # for i in range(len(s)):
    #     if s[len(s)-1-i] != t[len(t)-1-i]:
    #         isSuffix = False
    for i in reversed(range(len(s))):
        # print(i, s[i],t[i+len(t)-len(s)])
        if s[i] == t[i+len(t)-len(s)]:
            isSuffix = False
    return isSuffix
# isSufix('aaa','baaa')
# print('zzzzzz')

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
    #     if isSufix(s,t):
    #         print(2)
    #     else:
    #         print(3)

prefix_suffix_check('abc','abcdefg') # 1 と表示されるのが正解
prefix_suffix_check('abc','aabc')    # 2 と表示されるのが正解
prefix_suffix_check('abc','xyx')     # 3 と表示されるのが正解
prefix_suffix_check('abc','abc')     # 0 と表示されるのが正解
prefix_suffix_check('abc','abc-abc') # 0 と表示されるのが正解
