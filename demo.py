import streamlit as st
import pandas as pd

from riotwatcher import LolWatcher, ApiError

st.title('选手韩服Rank查询程序')
summoner_name = st.text_input('请输入韩服ID')
count_num = st.slider('选择获取的排位场数:', 0, 100, 50)

# 创建一个lol_watcher对象
lol_watcher = LolWatcher(st.secrets["my_api"])

# 玩家的信息
region = 'kr' # Riot API开发文档里有写到各个服务器的region缩写

# 创建一个lol_watcher下的summoner对象
summoner = lol_watcher.summoner.by_name(region, summoner_name)

puuid = summoner['puuid']

# 提取matchlist
matchlist = lol_watcher.match.matchlist_by_puuid(region='asia', puuid=puuid, type='ranked', count=count_num)

@st.cache(show_spinner=False, suppress_st_warning=True)
def get_time_stamp(matchid):
    return lol_watcher.match.by_id('asia', matchid)['info']['gameEndTimestamp']


list = []
for matchid in matchlist:
    list.append(get_time_stamp(matchid))

# 把UNIX时间戳转换成datetime

import time
from datetime import datetime

def timestamp_to_strtime(timestamp):
    #local_str_time = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M')
    local_str_time = datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d')
    return local_str_time

time = []
for i in list:
    time.append(timestamp_to_strtime(i))

time = pd.DataFrame(time, columns = ['Count'])

df = time['Count'].value_counts().sort_index(ascending=False)

df.index.name = 'Date'

st.table(df.reset_index())
