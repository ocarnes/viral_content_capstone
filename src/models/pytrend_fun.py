# Uses pytrends to pull google trends on article keywords
from pytrends.request import TrendReq
import pandas as pd
from string import punctuation
from datetime import timedelta
import numpy as np
import time

PUNCT_DICT = {ord(punc): None for punc in punctuation if punc not in ['_', '*', ',']}

cols = ['post_published', 'tags', 'date-7','date-6', 'date-5', 'date-4', 'date-3', 'date-2', 'date-1',
'date-0', 'date+1', 'date+2', 'date+3', 'date+4', 'date+5', 'date+6', 'date+7']

df = pd.read_csv('df_sentiment_all.csv', parse_dates=['post_published'])
# df_trends = pd.read_csv('df_trends4.csv', parse_dates=['post_published'])

# for i in range(df.shape[0]):
# i = 3687
# i = 5336
# i = 6965
# i = 9417
for i in range(i, df.shape[0]):
    if i % 10 == 0:
        print(i)
    time.sleep(3)
    kw_list = df.tags[i].translate(PUNCT_DICT).split(', ')
    if kw_list == ['']:
        df_trends = df_trends.append(pd.DataFrame(data=[np.append([df.post_published[i], df.tags[i]], np.nan*np.empty((1,15)))], columns=cols))
    elif '2017' in kw_list:
        kw_list.remove('2017')
    else:
        time_start = str(df.post_published[i].date() - timedelta(days=7))
        time_stop = str(df.post_published[i].date() + timedelta(days=7))

        timeframe = time_start+' '+time_stop

        pytrends = TrendReq(hl='en-US', tz=360)

        pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')

        trends = pytrends.interest_over_time()
        if trends.shape[0] < 15:
            kw_list = kw_list[0].split()
            pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')
            trends = pytrends.interest_over_time()
        trends.sum(axis=1)

        df_trends = df_trends.append(pd.DataFrame(data=[np.append([df.post_published[i],df.tags[i]],trends.sum(axis=1).values)], columns=cols))
