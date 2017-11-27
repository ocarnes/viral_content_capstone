import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore', category=DeprecationWarning, module='.*/IPython/.*')
warnings.filterwarnings('ignore', category=DeprecationWarning, module='pyLDAvis')

import pyLDAvis
import pyLDAvis.sklearn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def get_top_words(model, feature_names, n_top_words):
    top_words = {}
    for topic_idx, topic in enumerate(model.components_):
        _top_words = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        top_words[str(topic_idx)] = _top_words
    return(top_words)

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

if __name__ == '__main__':

    df = pd.read_csv('articles.csv', parse_dates=['post_published'])
    text = df['processed_text'].values.tolist()
max_features = 5000
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=3,
                                max_features=max_features,
                                stop_words='english')
tf = tf_vectorizer.fit_transform(text)
print("ready")

n_topics = 18
lda_model = LatentDirichletAllocation(n_components=n_topics, max_iter=5,
                                      learning_method='online',
                                      learning_offset=50.,
                                      random_state=0)

    lda_model.fit(tf)
    # pyLDAvis.enable_notebook()
    # pyLDAvis.sklearn.prepare(lda_model,tf, tf_vectorizer, R=20, mds='tsne')

        ## get the token to topic matrix
word_topic = np.zeros((max_features,n_topics),)
print(n_topics)
lda_model.components_
for topic_idx, topic in enumerate(lda_model.components_):
    word_topic[:,topic_idx] = topic

print("token-topic matrix",word_topic.shape)

    ## create a matrix of the top words used to define each topic
top_words = 20
tf_feature_names = np.array(tf_vectorizer.get_feature_names())
top_words = get_top_words(lda_model,tf_feature_names,top_words)
all_top_words = np.array(list(set().union(*[v for v in top_words.values()])))

for key,vals in top_words.items():
    print(key," ".join(vals))
print("total words: %s"%len(all_top_words))

top_word_inds = [np.where(tf_feature_names == tw)[0][0] for tw in all_top_words]

df_topics = pd.DataFrame(lda_model.transform(tf))
df = df.join(df_topics)

    latent_topics = ['Celebrity Bodies', 'Young Adult Television', 'Politics',
     'Movie / TV Trailers', 'Eclipse / Space', 'Medical / Death', 'Sports',
     'Teen Mom', 'Reality TV Recaps / Rumors', 'Tech', 'Daytime TV',
     'Southern Charm', 'Kardashian', 'Music', 'Rape', 'Brangelina', 'First Families',
     'Terrorism']

plt.figure(figsize=(10, 6), dpi=250)
ax = plt.subplot(111)
ax.axis('off')
ax.patch.set_visible(False)
X = lda_model.components_
y = range(n_topics)
X_norm = (X - X.min())/(X.max() - X.min())
lda_transformed = pd.DataFrame(lda_model.fit_transform(X_norm, y))
c = get_cmap(n_topics)
# x, y = lda_transformed[:,0], lda_transformed[:,1]
# for i in range(clusters):
#     plt.scatter(x[(prediction==i)&(views<thresh)],y[(prediction==i)&(views<thresh)], marker='.',alpha = 0.15, color = c[i])
#     plt.scatter(x[(prediction==i)&(views>=thresh)],y[(prediction==i)&(views>=thresh)], marker='o',alpha = 0.5,label = categories[i], color=c[i])
#         # for xp, yp, m in zip(X[index,0],X[index,1] marks)
for i in y:
    plt.scatter(lda_transformed[y==i][0], lda_transformed[y==i][1], label=laten_topics[i], color = c[i], alpha=0.5)

plt.legend()
plt.xticks([]), plt.yticks([])
plt.ylim([-0.1,1.1])
plt.xlim([-0.1,1.1])
plt.title('LDA Viz', fontsize=16)
plt.tight_layout()
plt.show()

df['cluster'] = df[df.columns[30:48]].idxmax(axis=1)


sns.violinplot(x='tops', y='views', data=df2, hue='Sentiment', split=True,scale="count", inner="quartile")
plt.xticks(rotation=45)
plt.xlabel('Latent Topics')
plt.ylabel('Page Views')
plt.tight_layout()
plt.show()
