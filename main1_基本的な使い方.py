import streamlit as st
import numpy as np
import pandas as pd

# ターミナルの場所指定 Dドライブも可 一度実行するのがよいかも
# ★★★最初のみターミナルで次を実行 → streamlit run main1_基本的な使い方.py ★★★
# その後は保存→ウェブサイトでF5のみでOK
# Streamlit 参考サイト API > Data display elements
# https://docs.streamlit.io/library/api-reference

# タイトルの追加
st.title('Streamlit 超入門')

# テキストの追加
st.write('DataFrame')


# ---表---
# 表の追加準備
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# 表のみを通常追加(動的)
st.write(df)

# 表をピクセル単位でサイズ指定して追加
st.dataframe(df, width=100, height=100)  # 正方形

# 列の中で最大のものをハイライト
st.dataframe(df.style.highlight_max(axis=0)) 

# 行の中で最大のものをハイライト
st.dataframe(df.style.highlight_max(axis=1))  

# static(静的)な形状のテーブル
st.table(df.style.highlight_max(axis=0))  

# ---テキスト マークダウン マジックコマンド---
# 参考サイト API > Text elements

""" 
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# ---チャート グラフ 14:05--- Chart elements

# 表の追加準備 20x3の正規分布を元に乱数 0から1
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

# 折れ線グラフでグラフ化
st.line_chart(df2)

# エリアチャートでグラフ化
st.area_chart(df2)

# 棒グラフ化
st.bar_chart(df2)


# ---マップのプロット 19:20---
# 緯度と経度のデータを用意 → 東京新宿付近のマッピング 
# データが大きすぎるのでまずはそれぞれ50で割る
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat','lon']
)

st.map(df3, zoom=12)


# ---画像を表示 24:00--- Media elements
from PIL import Image

# タイトルの追加
st.title('Streamlit 超入門2')   # 途中に挟むことも可能

st.write("Display Image")

img = Image.open(('sample.png'))
st.image(img, caption='Kohei Imanishi', use_column_width=True)

# 画像以外にも音楽、映像などもヒョ時可能

