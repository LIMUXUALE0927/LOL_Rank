import streamlit as st
from riotwatcher import LolWatcher
from datetime import date, datetime, timedelta
import pandas as pd

# yesterday = int(datetime.fromisoformat('2021-12-26 12:00').timestamp())
# today = int(datetime.fromisoformat('2021-12-27 12:00').timestamp())

today = datetime.today().date()
oneday = timedelta(days=1)
yesterday = today - oneday

st.title('选手韩服Rank查询程序')

d = st.date_input(
    "请选择要查询的时间段：",
    (yesterday, today))
