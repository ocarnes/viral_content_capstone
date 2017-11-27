import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from string import punctuation
from sklearn.model_selection import train_test_split
nlp = spacy.load('en')

# Create custom stoplist
STOPLIST = set(list(ENGLISH_STOP_WORDS) + ["n't", "'s", "'m", "ca", "'", "'re", "getty_images", "getty images"])
PUNCT_DICT = {ord(punc): None for punc in punctuation if punc not in ['_', '*']}


def clean_article(article):
    doc = nlp(article)

    # Let's merge all of the proper entities
    for ent in doc.ents:
        if ent.root.tag_ != 'DT':
            ent.merge(ent.root.tag_, ent.text, ent.label_)
        else:
            # Keep entities like 'the New York Times' from getting dropped
            ent.merge(ent[-1].tag_, ent.text, ent.label_)

    # Part's of speech to keep in the result
    pos_lst = ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB'] # NUM?

    tokens = [token.lemma_.lower().replace(' ', '_') for token in doc if token.pos_ in pos_lst]

    return ' '.join(token for token in tokens if token not in STOPLIST).replace("'s", '').translate(PUNCT_DICT)


if __name__=='__main__':
    df = pd.read_csv('../../data/df_final_v2.csv', parse_dates=['post_published'])
    # df = pd.read_csv('npr_articles.csv', parse_dates=['date_published'])
    df = df[df['article_id'] != 4326814]
    df['processed_title'] = df['post_title'].apply(clean_article)

    df.to_csv('titles.csv', index=False)
    #
    # train, test = train_test_split(df, test_size=0.2)
    #
    # train.to_csv('train.csv', index=False)
    # test.to_csv('test.csv', index=False)
