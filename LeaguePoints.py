import streamlit as st
from riotwatcher import LolWatcher, ApiError
import pandas as pd

st.title('韩服分数查询程序')

lol_watcher = LolWatcher(st.secrets["my_api"])
region = 'kr'

txt = st.text_area('IDs to analyze')

namelist = txt.split(',')
namelist = [i.strip() for i in namelist]
namelist = [i.replace('\xa0', ' ') for i in namelist]

stats = pd.DataFrame()
for name in namelist:
    summoner_id = lol_watcher.summoner.by_name(region, name)['id']
    data = lol_watcher.league.by_summoner(region, summoner_id)
    stats = stats.append(data, ignore_index=True)

st.table(stats[['summonerName', 'tier', 'rank', 'leaguePoints']])
