from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import recall_score, precision_score, roc_auc_score, roc_curve, f1_score
# import graphviz
import pickle as pickle
import pprint
from sklearn.preprocessing import scale

def trees_model(model, X_train, X_test, y_train, y_test):
    tree_model = model.fit(X_train, y_train)
    predictions = tree_model.predict(X_test)
    probabilities = tree_model.predict_proba(X_test)
    return tree_model, predictions, probabilities


if __name__ == '__main__':
    df = pd.read_csv('df_sentiment_all.csv')

    X = df[['count_fb', 'count_hyperlinks', 'count_insta',
    'count_quote', 'count_twitter','length', '0', '1',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
    '12', '13', '14', '15', '16', '17', 'pos', 'subj']].values
    cols = ['count_fb', 'count_hyperlinks', 'count_insta',
    'count_quote', 'count_twitter','length', '0', '1',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
    '12', '13', '14', '15', '16', '17', 'pos', 'subj']
    y = df['views'].values

y_new = np.array([])
for view in y:
    if view >= 40000:
        y_new = np.append(y_new, 1)
    else:
        y_new = np.append(y_new, 0)

    X_train, X_test, y_train, y_test = train_test_split(X,y)

print('\n --> Gradient Boosted Forest------------------')
grad_b = GradientBoostingClassifier(learning_rate= 0.5, max_depth= 7, max_features= None, n_estimators= 500)#learning_rate= 0.1, max_depth= 7, max_features= 5, n_estimators= 500)
gb_model, predictions, probabilities = trees_model(grad_b,X_train, X_test, y_train, y_test)
print('------------scoring model GB------------------')
print('recall score: {}'.format(recall_score(y_test, predictions)))
print('accuracy: {}'.format(gb_model.score(X_test, y_test)))
print('precision score: {}'.format(precision_score(y_test, predictions)))
print('f-1 score: {}'.format(f1_score(y_test, predictions)))
print('under_ROC_score: {}'.format(roc_auc_score(y_test, probabilities[:,1])))
print('------------important features GB---------------')
# print('feature_importances: {}, len{}'.format(rf_model.feature_importances_, \
                                                # len(rf_model.feature_importances_)))
important_feats = {}
for i, importance in enumerate(gb_model.feature_importances_):
    important_feats[cols[i]] = importance
sorted_feats = sorted(important_feats.items(), key=lambda x: x[1])[::-1]
pprint.pprint(sorted_feats)

def categories(cluster):
    df_6 = ew_df[ew_df.cluster == cluster]
    X = df_6[df_6.columns[45:49]]
    # X = X[pd.notnull(X['date-7'])]
    cols = X.columns
    # y = ew_df[(pd.notnull(ew_df['date-7']))&(ew_df.cluster == cluster)]['revenue']
    y = ew_df[(ew_df.cluster == cluster)]['revenue']
    y_new = np.array([])
    for rev in y:
        if rev >=120:
            y_new = np.append(y_new, 1)
        else:
            y_new = np.append(y_new, 0)
    X = scale(X)
    X_train, X_test, y_train, y_test = train_test_split(X,y_new)
    print('\n --> Gradient Boosted Forest------------------')
    grad_b = GradientBoostingClassifier(learning_rate= 0.5, max_depth= 7, max_features= None, n_estimators= 500)#learning_rate= 0.1, max_depth= 7, max_features= 5, n_estimators= 500)
    gb_model, predictions, probabilities = trees_model(grad_b,X_train, X_test, y_train, y_test)
    print('------------scoring model GB------------------')
    print('recall score: {}'.format(recall_score(y_test, predictions)))
    print('accuracy: {}'.format(gb_model.score(X_test, y_test)))
    print('precision score: {}'.format(precision_score(y_test, predictions)))
    print('f-1 score: {}'.format(f1_score(y_test, predictions)))
    print('under_ROC_score: {}'.format(roc_auc_score(y_test, probabilities[:,1])))
    # print('Roc curve: {}'.format(roc_curve(y_test, probabilities[:,1])))
    print('------------important features GB---------------')
    # print('feature_importances: {}, len{}'.format(rf_model.feature_importances_, \
                                                    # len(rf_model.feature_importances_)))
    important_feats = {}
    for i, importance in enumerate(gb_model.feature_importances_):
        important_feats[cols[i]] = importance
    sorted_feats = sorted(important_feats.items(), key=lambda x: x[1])[::-1]
    pprint.pprint(sorted_feats)
