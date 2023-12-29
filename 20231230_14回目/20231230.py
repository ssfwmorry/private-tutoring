def isPrefix(s, t):
    isPrefix = true
    for i in range(len(s)):
        if s[i] != t[i]:
            isPrefix = false # 違う文字の場合には接頭辞ではないとする
def isSufix(s, t):
    isPrefix = true
    for i in range(len(s)):
        if s[i] != t[i]:
            isPrefix = false # 違う文字の場合には接頭辞ではないとする

def prefix_suffix_check(s, t):
    if isPrefix(s,t) and isSufix(s,t):
        print(1)
    elif isPrefix(s,t) and not isSufix(s,t):
        print(2)
    elif not isPrefix(s,t) and isSufix(s,t):
        print(3)
    else:
        print(0)

print(prefix_suffix_check('abc','abcdefg')) # 1 と表示されるのが正解
print(prefix_suffix_check('abc','aabc'))    # 2 と表示されるのが正解
print(prefix_suffix_check('abc','xyx'))     # 3 と表示されるのが正解
print(prefix_suffix_check('abc','abc'))     # 0 と表示されるのが正解
print(prefix_suffix_check('abc','abc-abc')) # 0 と表示されるのが正解
