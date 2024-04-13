# 紙のテキストの問題

## 20

以下の実行結果は？

```python

def value(arg):
    return arg

result1 = value(0) and value(1) and value(2)
result2 = value(0) or value(1) or value(2)

print(result1, result2)
```

## 26

以下の構造の時、`my_app/save/__init__.py` のなかで　`load.py` の中身を読み込むための書き方は?

```txt
my_app/
  __init__.py
  load.py
  save/
    __init__.py
    load.py
    download.py
```

## 35

`python main.py --command=show tokyo osaka` と実行した結果は?

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--command")
parser.add_argument("target", nargs="+")
args = parser.parse_args()
print(args)
```

## 36

謝っている記載は?

```python
import re

s = "tic tac tac toe"
print(re.sub(r"([a-z]+) \1", r"\1", s))
```

1. re モジュールは正規表現で文字列の処理を行える
2. re.sub は、特定のパターンを変換する関数である
3. 出力は、tic tac toe になる
4. `print(s.replace("tac ", ""))` と同じ結果になる

"\1" は一つ目のグループ。書籍の中で解説の見出しに書いてある回答は D になっているが、C の記載が正しい

## 37

`-m unittest` をつけて実行して、以下の結果が得られる時、`# 何` に入るものは?

```python
import unittest

class TestApp(unittest, TestCate):
    def test_one(self):
        actual = selfFunc()
        expected = "Monday"
        assert actual == expected
'''
結果
AssertionError:
'''
```

## 38

コードを実行して、以下の結果が得られる時、`# 何` に入るものは?

```python
# text = [f"{i} sheep jumped a fence." for in range(1, 4)]
text = [ "0 sheep jumped a fence.",
         "1 sheep jumped a fence.",
         "2 sheep jumped a fence.",
         "3 sheep jumped a fence."  ]

# 何

'''
結果
[
    "1 sheep jumped a fence.",
    "2 sheep jumped a fence.",
    "3 sheep jumped a fence."
]
'''
```

1.<br />
`import textwrap` <br />
`print(textwrap.fill(", ".join(text), width=24))`

4.<br />
`print("\n".join(text))`

a= [1,2,3]
(", ".join(text))

0 sheep jumped a fence.,
1 sheep jumped a fence.,
2 sheep jumped a fence.,
3 sheep jumped a fence.
