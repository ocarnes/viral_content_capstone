# determining readability of an article using Automated Readability index
import pandas as pd
from string import punctuation

def ARI_index(article):
    #automated readability index (ARI)
    words = len(processed_article.split())
    sentences = len([letter for letter in list(article) if letter in '.!?'])
    characters = len([letter for letter in list(processed_article) if letter not in punctuation.join(' ”’')])
    ARI = (4.71*(characters/words))+(0.5*(words/sentences))-21.43
    return ARI

if __name__ == '__main__':

    #Flesch–Kincaid grade level
    # FK = 0.39*(total_words/total_sentences)+11.8*(total_syllables/total_words)-15.59

    df = pd.read_csv('df_trendz_final.csv')
    df['ARI'] = df.article.apply(ARI_index)
