import streamlit as st
import pandas as pd

df = pd.read_html(
    'https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Btournament%5D=LPL%2F2022+Season%2FSpring+Season&TS%5Bpreload%5D=TournamentByChampion&pfRunQueryFormName=TournamentStatistics')[0]
new_header = df.iloc[1]
df = df[2:]
df.columns = new_header
df = df[['Champion', 'G', 'PB%', 'B', 'W', 'L', 'WR', 'KDA']]
df.columns = ['英雄', 'B+P总次数', '出场次数', '经济',
              'BP率', '被ban次数', '胜场', '负场', '胜率', 'KDA']
df = df[['英雄', 'BP率', 'B+P总次数', '被ban次数', '出场次数', '胜场', '负场', '胜率', 'KDA']]
df.reset_index(drop=True)
st.table(df)
