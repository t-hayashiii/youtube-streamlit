import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# ターミナルの場所指定 Dドライブも可 一度実行するのがよいかも
# ★★★最初のみターミナルで次を実行 → streamlit run main3_レイアウトを整える.py ★★★
# その後は保存→ウェブサイトでF5のみでOK
# 参考サイト API > Layouts and Containers
# https://docs.streamlit.io/library/api-reference/layout

# タイトルの追加
st.title('Streamlit 超入門')
st.write("レイアウトを整える")

# ---01_サイドバー---
# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# # condition = st.sidebar.slider('あなたの今の調子は?', 0, 100, 50)

# 'あなたの趣味 : ',text,'です。'
# ' コンディション : ',condition,


# ---02_2コラムレイアウト---
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# ---03_エクスパンダー---
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')

expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



# text = st..text_input('あなたの趣味を教えて下さい。')
# condition = st..slider('あなたの今の調子は?', 0, 100, 50)

# 'あなたの趣味 : ',text,'です。'
# ' コンディション : ',condition,


# if st.checkbox('Show Image'):
#     img = Image.open(('sample.png'))
#     st.image(img, caption='Kohei Imanishi', use_column_width=True)
    
# # 02_セレクトボックスで選択した数字を表示
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、',option,'です。'

# # 03_テキスト入力を表示