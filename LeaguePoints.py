import streamlit as st
from riotwatcher import LolWatcher, ApiError
import pandas as pd

st.title('韩服排位分数批量查询程序')
st.write('在下方文本框中输入要查询的韩服ID列表，注意各个ID之间要用英文逗号(,)分隔，但最后一个ID之后不要加逗号。')

lol_watcher = LolWatcher(st.secrets["my_api"])
region = 'kr'

txt = st.text_area('IDs to search',
                   '''
BRO Morgan, KT Harp, chenzebin, MIDGOD 12
'''
                   )

namelist = txt.split(',')
namelist = [i.strip() for i in namelist]
namelist = [i.replace('\xa0', ' ') for i in namelist]

stats = pd.DataFrame()
for name in namelist:
    summoner_id = lol_watcher.summoner.by_name(region, name)['id']
    data = lol_watcher.league.by_summoner(region, summoner_id)
    stats = stats.append(data, ignore_index=True)

st.table(stats[['summonerName', 'tier', 'rank', 'leaguePoints']])
