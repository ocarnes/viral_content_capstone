# Need to use python 2 for this
from pattern.en import sentiment
import pandas as pd
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

def pols(doc):
    return sentiment(doc)[0]

def subj(doc):
    return sentiment(doc)[1]

def plot_sentiment(df):
        plt.scatter(scale(df.pos), df.views, alpha=0.5, label='Polarity')
        plt.scatter(scale(df.subj), df.views, alpha = 0.5, label='Subjectivity')
        # plt.bar(df.views, scale(df.pos), alpha=0.5, label='Polarity')
        # plt.bar(df.views, scale(df.subj), alpha = 0.5, label='Subjectivity')

        plt.legend()
        plt.xlabel('Sentiment')
        plt.ylabel('Views')
        plt.title('Sentiment Analysis by Article', fontsize=16)
        plt.tight_layout()
        plt.savefig('sentiment.png')
        plt.show()

if __name__=='__main__':
    # df = pd.read_csv('df_topics_all.csv')
    # df['pos'] = df.processed_text.apply(pols)
    # df['subj'] = df.processed_text.apply(subj)

    plot_sentiment(df)

    # df.to_csv('df_sentiment_all.csv')
