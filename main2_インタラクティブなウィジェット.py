import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# ターミナルの場所指定 Dドライブも可 一度実行するのがよいかも
# ★★★最初のみターミナルで次を実行 → streamlit run main2_インタラクティブなウィジェット.py ★★★
# その後は保存→ウェブサイトでF5のみでOK
# 参考サイト API > Input widgets
# https://docs.streamlit.io/library/api-reference/widgets

# タイトルの追加
st.title('Streamlit 超入門')
st.write("Interactive Widgets")

# 01_チェックボックスが入っていれば画像を表示
if st.checkbox('Show Image'):
    img = Image.open(('sample.png'))
    st.image(img, caption='Kohei Imanishi', use_column_width=True)
    
# 02_セレクトボックスで選択した数字を表示
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1, 11))
)
'あなたの好きな数字は、',option,'です。'

# 03_テキスト入力を表示
option2 = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味 : ',option2,'です。'

# 04_スライダー
condition = st.slider('あなたの今の調子は?', 0, 100, 50)
' コンディション: ',condition,

