##########################################
# 11章末問題の考え方解説
##########################################
import xml.etree.ElementTree as et

tree = et.parse('./files/sample11_3.xml') # 相対パス
tree = et.parse('/Users/mori/Documents/Production/private-tutoring/20240113_15回目/files/sample11_3.xml') # 絶対パス

root = tree.getroot()
print(f'ルート要素のタグ名：{root.tag}')
print(f'ルート直下の要素数：{len(root)}')

print('-----')

sum = 0 # 三人の年齢の合計
for person in root:
    # name = person.find('name').text
    age = person.find('age').text
    sum += int(age)
    # gender = person.find('gender').text
    # print(f'名前：{name}, 年齢：{age}, 性別：{gender}')

print (sum / len(root)) # 平均値

##########################################
# 再帰処理の解説
# Nの階乗を求めるプログラムを作りましょう
# （例）５の階乗＝1*2*3*4*5
# （例）５の階乗 = 5*4*3*2*1 = 5*(4の階乗) = 5*(4*(3の階乗)) = 5*(4*(3*(2*1)))
##########################################
# forをつかったパターン
def kaijo_for(n):
    ret = 1
    for i in range(n): # 0,1,2,3,4
        ret = ret * (i+1) # *1,*2,*3,*4,*5
    return ret
print(kaijo_for(5))
# 再帰処理をつかったパターン
def kaijo_saiki(n):
    if n==1:
        return 1
    return n * kaijo_saiki(n-1)

print(kaijo_saiki(5))

##########################################
# 13章の章末問題の考え方
##########################################
def get_html(url, dirname):
    # 1) dirnameの読み込み
    # 3) ファイル書き込み
    # 2) 子にaタグがあるかをみて、あるなら探索
    # 負荷をかけないように時間を空ける
    pass
# 日付のディレクトリがなければ作成する
today = datetime.date.today()
dirname = today.strftime('%Y%m%d')
if not os.path.exists(dirname):
    os.mkdir(dirname)

start_url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'
get_html(start_url, dirname)

# 喜寿するコードの順番によって、結果が変わります
# 1)-2)-3)の順番場合
'''
13_3_2_1_a
13_3_2_1_b
13_3_2_1
13_3_2_2_a
13_3_2_2
13_3_2_3
13_3_2
'''

# 1)-3)-2)の場合
'''
13_3_2
13_3_2_1
13_3_2_1_a
13_3_2_1_b
13_3_2_2
13_3_2_2_a
13_3_2_3
'''