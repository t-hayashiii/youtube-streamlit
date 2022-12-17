import streamlit as st
import time   # タイムライブラリの追加

# ターミナルの場所指定 Dドライブも可 一度実行するのがよいかも
# ★★★最初のみターミナルで次を実行 → streamlit run main4_プログレスバー.py ★★★
# その後は保存→ウェブサイトでF5のみでOK
# 参考サイト API > Status Elements
# https://docs.streamlit.io/library/api-reference/status

# タイトルの追加
st.title('Streamlit 超入門')
st.write("プログレスバーの表示")

'Start!!'

latest_iteration = st.empty()  # 空
bar = st.progress(0)

for i in range(100):   # 0~99
    latest_iteration.text(f'少々お待ち下さい {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'Done!!!!!'




# ---03_エクスパンダー---
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')

expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

