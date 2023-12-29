import os

today = datetime.date.today()
dirname = today.strftime('%Y%m%d')
try:
    os.mkdir('20231223')
except:
    print('ディレクトリはすでに存在します')
