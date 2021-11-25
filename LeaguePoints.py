import streamlit as st
from riotwatcher import LolWatcher, ApiError
import pandas as pd

st.title('韩服分数查询程序')
api = st.text_input('请输入Riot API KEY:')
my_api = api

lol_watcher = LolWatcher(my_api)
region = 'kr'

namelist = (
'푹 쉬면서 해요', 'asdzxvc',
'가을의북',
'bilibligaming',
'Kiss myths',
'98kmn', '고독 한 사람', 'swfzyqtx',
'98kiw', 'apolio', 'meimioo',
'yang zhi bu ou', 'Anni',
'98kcfq', 'so sorry mid gap',
'main actor I', 'not my wrong',
'yue xiang yue qi',
'aoeiuU', 'wd tongchu', '1xn fans',
'ZhongYeSanJiu', 'MingRiNai', 'Ruizu',
'xgaozzz',
'suxiaoqiang', 'suxiaoqiang2'
)

stats = pd.DataFrame()
for name in namelist:
    summoner_id = lol_watcher.summoner.by_name(region, name)['id']
    data = lol_watcher.league.by_summoner(region, summoner_id)
    stats = stats.append(data, ignore_index=True)

st.table(stats[['summonerName', 'tier', 'rank', 'leaguePoints']])
