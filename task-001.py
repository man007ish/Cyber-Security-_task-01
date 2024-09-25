import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exercise_0(file):
    pass

def exercise_1(df):
    pass

def exercise_2(df, k):
    pass

def exercise_3(df, k):
    pass

def exercise_4(df):
    pass

def exercise_5(df):
    pass

def exercise_6(df):
    pass

def exercise_7(df):
    pass

def visual_1(df):
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass


# In[2]:


df = pd.read_csv("transactions.csv")


# In[3]:


df.columns


# In[4]:


df.head()


# In[5]:


df.sample(5)


# In[6]:


df.type.unique()


# In[7]:


df.nameDest.value_counts().head(10)


# In[8]:


df[df.isFraud == 1]


# In[9]:


df.groupby("nameDest")["newbalanceDest"].agg("mean").sort_values(ascending=False)



sns.countplot(x=df.type)
plt.title("Transaction types bar chart")
plt.show()





sns.countplot(x=df.type, hue=df.isFraud)
plt.title("Transaction types bar chart")
plt.show()


def exercise_custom(df):
    # TODO
    pass
    
def visual_custom(df):
    # TODO
    pass


