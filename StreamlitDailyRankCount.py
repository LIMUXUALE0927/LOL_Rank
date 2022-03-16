import streamlit as st
from datetime import datetime, timedelta
from riotwatcher import LolWatcher
import pandas as pd

oneday = timedelta(days=1)
today = datetime.today().date().isoformat() + ' 12:00'
yesterday = datetime.today() - oneday
yesterday = yesterday.date().isoformat() + ' 12:00'


yesterday = int(datetime.fromisoformat(yesterday).timestamp())
today = int(datetime.fromisoformat(today).timestamp())

txt = st.text_area('IDs:')

namelist = str(txt).split(',')
namelist = [i.strip() for i in namelist]
namelist = [i.replace('\xa0', ' ') for i in namelist]

my_api = 'RGAPI-72a071f8-44b1-4b69-8cfc-bc34be3c7421'

lol_watcher = LolWatcher(my_api)
region = 'kr'

list = []

def count_rank(summoner_name):
    summoner = lol_watcher.summoner.by_name(region, summoner_name)
    puuid = summoner['puuid']
    matchlist = lol_watcher.match.matchlist_by_puuid(region='asia', puuid=puuid, type='ranked',
                                                     start_time=yesterday, end_time=today)
    list.append([summoner_name, len(matchlist)])


for i in namelist:
    try:
        count_rank(i)
    except:
        continue

st.table(pd.DataFrame(list, columns=['ID', '排位场数']))
