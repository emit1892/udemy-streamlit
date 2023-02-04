import streamlit as st
import time

# タイトルの追加
st.title('Streamlit 超入門')

# テキストを追加
st.write('プログレスバーの表示')

'Start!!!'

# 空を追加
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    # 1秒止まる
    time.sleep(0.1)

'Done!!!!!!'
    
# 2カラムにする
left_column, right_column = st.columns(2)
# 左カラムにボタンを表示する
button = left_column.button('右カラムの文字を表示')

if button:
    right_column.write('ここは右カラムでっっす！')
    
# にょーんとメニューが出る
expandar = st.expander('問い合わせ')
expandar.write('問い合わせ内容を書く')
