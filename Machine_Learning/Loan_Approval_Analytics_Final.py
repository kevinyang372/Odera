
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic('matplotlib inline')


# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


# In[3]:

train_df   = pd.read_csv('train.csv')
test_df  = pd.read_csv('test.csv')


# In[4]:

train_df.head()


# In[5]:

train_df.head() #female = 0, N = 0


# In[6]:

print(type(train_df["Employer_Category2"][0]))


# In[7]:

train_df['City_Code'] = train_df['City_Code'].astype(str)
train_df['City_Code'] = train_df['City_Code'].map(lambda x: x.lstrip('C'))
train_df['City_Code'] = train_df['City_Code'].astype(float)

train_df['Employer_Code'] = train_df['Employer_Code'].astype(str)
train_df['Employer_Code'] = train_df['Employer_Code'].map(lambda x: x.lstrip('COM'))
train_df['Employer_Code'] = train_df['Employer_Code'].astype(float)


# In[8]:

train_df['Customer_Existing_Primary_Bank_Code'] = train_df['Customer_Existing_Primary_Bank_Code'].astype(str)
train_df['Customer_Existing_Primary_Bank_Code'] = train_df['Customer_Existing_Primary_Bank_Code'].map(lambda x: x.lstrip('B'))
train_df['Customer_Existing_Primary_Bank_Code'] = train_df['Customer_Existing_Primary_Bank_Code'].astype(float)


# In[9]:

train_df['Source'] = train_df['Source'].astype(str)
train_df['Source'] = train_df['Source'].map(lambda x: x.lstrip('S'))
train_df['Source'] = train_df['Source'].astype(float)


# In[10]:

test_df['Source'] = test_df['Source'].astype(str)
test_df['Source'] = test_df['Source'].map(lambda x: x.lstrip('S'))
test_df['Source'] = test_df['Source'].astype(float)


# In[11]:

test_df['City_Code'] = test_df['City_Code'].astype(str)
test_df['City_Code'] = test_df['City_Code'].map(lambda x: x.lstrip('C'))
test_df['City_Code'] = test_df['City_Code'].astype(float)

test_df['Employer_Code'] = test_df['Employer_Code'].astype(str)
test_df['Employer_Code'] = test_df['Employer_Code'].map(lambda x: x.lstrip('COM'))
test_df['Employer_Code'] = test_df['Employer_Code'].astype(float)


# In[12]:

test_df['Customer_Existing_Primary_Bank_Code'] = test_df['Customer_Existing_Primary_Bank_Code'].astype(str)
test_df['Customer_Existing_Primary_Bank_Code'] = test_df['Customer_Existing_Primary_Bank_Code'].map(lambda x: x.lstrip('B'))
test_df['Customer_Existing_Primary_Bank_Code'] = test_df['Customer_Existing_Primary_Bank_Code'].astype(float)


# In[13]:

train_df.head()


# In[14]:

train_df = train_df.drop(["Interest_Rate","EMI"],axis=1)


# In[15]:

train_df = train_df.drop(["ID"],axis=1)


# In[16]:

train_df = train_df.drop(["Lead_Creation_Date"],axis=1)


# In[17]:

train_df = train_df.drop(["Contacted"],axis=1)


# In[18]:

train_df = train_df.drop(["Source_Category"],axis=1)


# In[19]:

test_df = test_df.drop(["Source_Category"],axis=1)


# In[20]:

test_df = test_df.drop(["Contacted"],axis=1)


# In[21]:

test_df = test_df.drop(["Lead_Creation_Date"],axis=1)


# In[22]:

test_df = test_df.drop(["ID"],axis=1)


# In[23]:

test_df = test_df.drop(["Interest_Rate","EMI"],axis=1)


# In[24]:

def dob_dob(df):
    new_column = pd.to_datetime(df["DOB"])
    return pd.DataFrame({"year": new_column.dt.year,
              "month": new_column.dt.month,
              "day": new_column.dt.day,
              "hour": new_column.dt.hour,
              "dayofyear": new_column.dt.dayofyear,
              "week": new_column.dt.week,
              "weekofyear": new_column.dt.weekofyear,
              "dayofweek": new_column.dt.dayofweek,
              "weekday": new_column.dt.weekday,
              "quarter": new_column.dt.quarter,
             })


# In[25]:

train_dates = dob_dob(test_df)


# In[26]:

test_dates = dob_dob(test_df)


# In[27]:

train_df = train_df.drop(["DOB"],1).join(train_dates)


# In[28]:

test_df = test_df.drop(["DOB"],1).join(test_dates)


# In[29]:

train_dates.head()


# In[30]:

train_one_hot = pd.get_dummies(train_df,columns=['City_Category','Employer_Category1','Primary_Bank_Type'])


# In[31]:

test_one_hot = pd.get_dummies(test_df,columns=['City_Category','Employer_Category1','Primary_Bank_Type'])


# In[32]:

train_one_hot = train_one_hot.replace(('Male', 'Female'), (1, 0))


# In[33]:

test_one_hot = test_one_hot.replace(('Male', 'Female'), (1, 0))


# In[34]:

train_one_hot.head()


# In[41]:

train_one_hot = train_one_hot.dropna()


# In[42]:

test_one_hot = test_one_hot.dropna()


# In[35]:

print(type(train_dates["dayofyear"][0]))


# In[9]:

sns.heatmap(train_df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[43]:

from sklearn.model_selection import train_test_split


# In[44]:

from sklearn.preprocessing import Imputer


# In[45]:

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# In[46]:

X_train = train_one_hot.drop(["Approved"],axis=1)
y_train = train_one_hot["Approved"]


# In[47]:

X = X_train
y = y_train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


# In[48]:

from sklearn.ensemble import RandomForestClassifier


# In[141]:

clf = RandomForestClassifier(n_estimators=2)
clf = clf.fit(X_train, y_train)


# In[142]:

train_predictions = clf.predict(X_train)


# In[143]:

print(classification_report(y_train,train_predictions))


# In[144]:

predictions = clf.predict(X_test)


# In[145]:

print(classification_report(y_test,predictions))


# In[146]:

print(confusion_matrix(y_test,predictions))


# In[147]:

y_train.value_counts()


# In[98]:

import xgboost as xgb


# In[100]:

xgtrain = xgb.DMatrix(X_train,y_train)
xgtest = xgb.DMatrix(X_test)


# In[122]:

xgboost_params = { "objective":"multi:softmax",    # binary classification 
              "num_class" :3,    # number of classes 
              "eval_metric" : "merror",    # evaluation metric 
              "nthread" : 4,   # number of threads to be used 
              "max_depth": 40,    # maximum depth of tree 
              "eta" : 0.15
                  }
                  
num_round = 90


# In[123]:

best = xgb.cv(xgboost_params, xgtrain, num_round,nfold=5)    

best["test-merror-mean"].min()         
# get prediction

xgtest.num_row()
                  

bst = xgb.train(xgboost_params, xgtrain, num_round)


# In[124]:

pred = bst.predict(xgtest)


# In[125]:

print(classification_report(y_test,pred))


# In[126]:

print(confusion_matrix(y_test,pred))


# In[ ]:



