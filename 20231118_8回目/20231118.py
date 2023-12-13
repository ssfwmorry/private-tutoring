'''
選択肢は4つ
A. `concat(**words, **options)`      NG
B. `concat(words, sep=options)`      NG
C. `concat(*words, **options)`       OK
D. `concat(args=words, sep=options)` NG
'''

def concat(args, sep="/"):
  print(args)
  print(sep)
  return sep.join(args) # args のそれぞれの文字列を、sepを区切り文字としてつなげる

words = ["span", "hum", "eggs"]
options = {"sep": "&"}

# print('空欄1')
print(concat(words, sep=options))      # B
print(concat(*words, **options))       # C が答えです！















# print(concat(**words, **options))      # A これは、**wordsで渡しているのでだめ
# print(concat(args=words, sep=options)) # D

