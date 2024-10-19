


from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import LabelEncoder
import pandas as pd
def getFeatures(df):
    # separate independent & dependent variables

    y2=df["attack_class"]

    le = LabelEncoder()
    df['attack_class'] = le.fit_transform(df['attack_class'])

    print(df['attack_class'] )
    
    y = df["attack_class"]  # target column i.e class
    
    del df["attack_class"]


    X = df  # independent columns

    #print(X)

    # apply SelectKBest class to extract top 20 best features
    bestfeatures = SelectKBest(score_func=chi2, k=20)
    fit = bestfeatures.fit(X, y)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(X.columns)

    # concat two dataframes for better visualization
    featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    featureScores.columns = ['Specs', 'Score']  # naming the dataframe columns
    #print(featureScores.nlargest(11, 'Score'))  # print 10 best features
    featureScores = featureScores.sort_values(by='Score', ascending=False)
    print(featureScores)

    # selecting the 10 most impactful features for the target variable
    features_list = featureScores["Specs"].tolist()[:20]
    print(features_list)
 
    df2=df[features_list]

    df2["attack_class"]=y2
    
    df2.to_csv("features.csv",index=False)


    return features_list,y
