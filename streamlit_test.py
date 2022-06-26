### 1. 仮想環境設定
# venvの構築
# https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

# 仮想環境のアクティブ化、セキュリティエラーの解決
# https://takatomablog.com/vscode_error_active_venv/

### 2. Streamlit参考
# Streamlit を用いたデータ分析アプリ開発
# https://qiita.com/keisuke-ota/items/a18f158389f1585a9aa0

# streamlit run streamlit_test.py

import streamlit as st
import pandas as pd
import numpy as np
#import plotly.graph_objs as go
import altair as alt
#from vega_datasets import data

#タイトル
st.title("My app")

#文書
st.write("Good morning")

#DataFrame
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#MarkDown
st.markdown('# Markdown documents')

#plotly
"""
animals = ['giraffes', 'orangutans', 'monkeys']
populations = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "Animal",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='Title')

st.plotly_chart(fig, use_container_width=True)

#Altair
source = data.cars()

fig = alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).properties(
    width=500,
    height=500
).interactive()

st.write(fig)
"""
# ボタンの表示

answer = st.button('Say hello')


# チェックボタン
if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')

     agree = st.checkbox('I agree')

# ドロップダウン
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.table(options)