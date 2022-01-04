import streamlit as st
from riotwatcher import LolWatcher
from datetime import date, datetime, timedelta
import pandas as pd

# yesterday = int(datetime.fromisoformat('2021-12-26 12:00').timestamp())
# today = int(datetime.fromisoformat('2021-12-27 12:00').timestamp())

today = datetime.today().date()
oneday = timedelta(days=1)
yesterday = today - oneday

st.title('选手韩服Rank批量查询程序')

namelist = str(st.text_area('IDs:')).split(',')
namelist = [i.strip() for i in namelist]
namelist = [i.replace('\xa0', ' ') for i in namelist]

d = st.date_input(
    "请选择要查询的时间段：",
    (yesterday, today))

start = int(datetime.fromisoformat(d[0].strftime('%Y-%m-%d')).timestamp())
end = int(datetime.fromisoformat(d[1].strftime('%Y-%m-%d')).timestamp())


lol_watcher = LolWatcher(st.secrets["my_api"])
region = 'kr'

df = pd.DataFrame([])


# def count_rank(summoner_name):
#     summoner = lol_watcher.summoner.by_name(region, summoner_name)
#     puuid = summoner['puuid']
#     matchlist = lol_watcher.match.matchlist_by_puuid(region='asia', puuid=puuid, type='ranked',
#                                                      start_time=start, end_time=end)
#     data = {"name": i, 'count': len(matchlist)}
#     df = df.append(data, ignore_index=True)


for i in namelist:
    try:
        summoner = lol_watcher.summoner.by_name(region, i)
        puuid = summoner['puuid']
        matchlist = lol_watcher.match.matchlist_by_puuid(region='asia', puuid=puuid, type='ranked',
                                                         start_time=start, end_time=end)
        data = {"name": i, 'count': len(matchlist)}
        df = df.append(data, ignore_index=True)
    except:
        continue

df['count'] = df['count'].astype(int)
st.table(df)
