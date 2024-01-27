# 以下、宿題解説

def resolve(K, G, M):
    g = 0
    m = 0
    for i in range(K):
        if g == G:
            g = 0
        elif m == 0:
            m = M
        else:
            if G < g + m:
                # グラスが水で満たされる時
                m = m - (G - g) # m = m - (グラスに注いだ量)
                g = G
            else:
                # マグカップが空になる時
                g = g + m
                m = 0
    print(g, m)


resolve(5, 300, 500) # 200 500 と表示されるのが正解 ケース1とする
resolve(5, 150, 200) # 50 200 と表示されるのが正解 ケース2とする
resolve(5, 100, 200) # 0 0 と表示されるのが正解 ケース3とする
