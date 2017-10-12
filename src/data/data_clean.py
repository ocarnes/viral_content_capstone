post_published,
post_id,
post_title,
post_url,
postAuthor_id,
postAuthor_name,
date_viewed,
day_since_publication,
page_views,
revenue

import pandas as pd

df = pd.read_csv('../../data/Capstone_Data_Olivia.csv')

df.drop(df['day_since_publication'] < 0, axis=0)
