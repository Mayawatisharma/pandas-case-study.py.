#!/usr/bin/env python
# coding: utf-8

# ## Pandas
# 
# *pandas* is a Python library for data analysis. It offers a number of data exploration, cleaning and transformation operations that are critical in working with data in Python. 
# 
# *pandas* build upon *numpy* and *scipy* providing easy-to-use data structures and data manipulation functions with integrated indexing.
# 
# The main data structures *pandas* provides are *Series* and *DataFrames*. After a brief introduction to these two data structures and data ingestion, the key features of *pandas* this notebook covers are:
# * Generating descriptive statistics on data
# * Data cleaning using built in pandas functions
# * Frequent data operations for subsetting, filtering, insertion, deletion and aggregation of data
# * Merging multiple datasets using dataframes
# * Working with timestamps and time-series data
# 
# **Additional Recommended Resources:**
# * *pandas* Documentation: http://pandas.pydata.org/pandas-docs/stable/
# * *Python for Data Analysis* by Wes McKinney
# * *Python Data Science Handbook* by Jake VanderPlas
# 
# Let's get started with our first *pandas* notebook!

# #### Import Libraries

# In[1]:


import pandas as pd


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# Introduction to pandas Data Structures</p>
# <br>
# *pandas* has two main data structures it uses, namely, *Series* and *DataFrames*. 
# 
# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# pandas Series</p>
# 
# *pandas Series* one-dimensional labeled array. 
# 

# In[2]:


ser = pd.Series([100, 'foo', 300, 'bar', 500], ['tom', 'bob', 'nancy', 'dan', 'eric'])


# In[4]:


ser


# In[5]:


ser.index


# In[6]:


ser[1]


# In[7]:


ser[[2]]=500


# In[9]:


ser.loc[['nancy','tom','bob']]


# In[8]:


ser['nancy']=500


# In[16]:


ser


# In[17]:


ser[[1,2,3]]


# In[18]:


ser[[2, 3, 0]]


# In[19]:


ser.iloc[[2,3]]


# In[20]:


'tom' in ser


# In[21]:


'xx' in ser


# In[22]:


ser


# In[23]:


ser * 3


# In[24]:


ser[['tom', 'eric']] ** 3


# In[18]:


ser['tom']=200


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# pandas DataFrame</p>
# 
# *pandas DataFrame* is a 2-dimensional labeled data structure.

# <p style="font-family: Arial; font-size:1.25em;color:#2462C0; font-style:bold">
# Create DataFrame from dictionary of Python Series</p>

# In[25]:


d = {'one' : pd.Series([100., 200., 300.], index=['apple', 'ball', 'clock']),
     'two' : pd.Series([111., 222., 333., 4444.], index=['apple', 'ball', 'cerill', 'dancy'])}


# In[27]:


df = pd.DataFrame(d)
print(df)


# In[16]:


df.index


# In[17]:


df.columns


# In[7]:


pd.DataFrame(d, index=['dancy', 'ball', 'apple','cerill','clock'])


# In[28]:


pd.DataFrame(d, index=['dancy', 'ball', 'apple'], columns=['name', 'age'])


# In[24]:


df


# In[25]:


d  


# In[ ]:





# <p style="font-family: Arial; font-size:1.25em;color:#2462C0; font-style:bold">
# Create DataFrame from list of Python dictionaries</p>

# In[29]:


data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora': 10, 'alice': 20}]


# In[19]:


data


# In[30]:


pd.DataFrame(data)


# In[31]:


data[0]


# In[31]:


pd.DataFrame(data, index=['orange', 'red'])


# In[33]:


pd.DataFrame(data, columns=['joe', 'ema','alice'])


# <p style="font-family: Arial; font-size:1.25em;color:#2462C0; font-style:bold">
# Basic DataFrame operations</p>

# In[32]:


df


# In[33]:


df['two']


# In[34]:


df


# In[34]:


df['three'] = df['one'] * df['two']
df


# In[35]:


df.pop('three')


# In[36]:


df


# In[38]:


df['flag'] = df['two'] >= 65
df


# In[39]:


df.pop('flag')


# In[41]:


df


# In[102]:


del df['two']


# In[43]:


df


# In[41]:


df.insert(1, 'copy_of_one', df['one'])
df


# In[ ]:


df.insert()


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# Case Study: Movie Data Analysis</p>
# <br>This notebook uses a dataset from the MovieLens website. We will describe the dataset further as we explore with it using *pandas*. 
# 
# ## Download the Dataset
# 
# Please note that **you will need to download the dataset**. Although the video for this notebook says that the data is in your folder, the folder turned out to be too large to fit on the edX platform due to size constraints.
# 
# Here are the links to the data source and location:
# * **Data Source:** MovieLens web site (filename: ml-20m.zip)
# * **Location:** https://grouplens.org/datasets/movielens/
# 
# Once the download completes, please make sure the data files are in a directory called *movielens* in your *Week-3-pandas* folder. 
# 
# Let us look at the files in this dataset using the UNIX command ls.
# 

# In[43]:


import os

import pandas as pd

os.chdir('F:\Training Python\ml-latest-small\ml-latest-small')

movies = pd.read_csv('movies.csv')



# In[44]:


movies.head()


# In[45]:


movies.tail()


# In[ ]:





# In[35]:


# Note: Adjust the name of the folder to match your local directory

get_ipython().system('dir .\\movielens')


# In[ ]:





# In[ ]:





# In[ ]:





# In[33]:


get_ipython().system('head -5 .\\movielens\\ratings.csv')


# <p style="font-family: Arial; font-size:1.75em;color:#2462C0; font-style:bold">
# Use Pandas to Read the Dataset<br>
# </p>
# <br>
# In this notebook, we will be using three CSV files:
# * **ratings.csv :** *userId*,*movieId*,*rating*, *timestamp*
# * **tags.csv :** *userId*,*movieId*, *tag*, *timestamp*
# * **movies.csv :** *movieId*, *title*, *genres* <br>
# 
# Using the *read_csv* function in pandas, we will ingest these three files.

# In[46]:


#movies = pd.read_csv('./movielens/movies.csv', encoding='latin-1')
print(type(movies))
movies.head()


# In[47]:


# Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970

tags = pd.read_csv('tags.csv', encoding='latin-1' )
tags.head()


# In[48]:


ratings = pd.read_csv('ratings.csv', sep=',', parse_dates=['timestamp'])
ratings.head()


# In[49]:


ratings.info()


# In[53]:


# For current analysis, we will remove timestamp (we will come back to it!)

del ratings['timestamp']
del tags['timestamp']


# <h1 style="font-size:2em;color:#2467C0">Data Structures </h1>

# <h1 style="font-size:1.5em;color:#2467C0">Series</h1>

# In[50]:


#Extract 0th row: notice that it is infact a Series

row_0 = tags.iloc[1]
type(row_0)


# In[51]:


print(row_0)


# In[52]:


row_0.index


# In[53]:


row_0['userId']


# In[54]:


'userId' in row_0


# In[118]:


row_0.name


# In[57]:


row_0 = row_0.rename('first_row')
row_0.name


# <h1 style="font-size:1.5em;color:#2467C0">DataFrames </h1>

# In[55]:


tags.head(10)


# In[56]:


tags.index


# In[57]:


tags.columns


# In[58]:


# Extract row 0, 11, 2000 from DataFrame

tags.iloc[ [10,11,200] ]


# <h1 style="font-size:2em;color:#2467C0">Descriptive Statistics</h1>
# 
# Let's look how the ratings are distributed! 

# In[59]:


ratings['movieId'].describe()


# In[60]:


ratings.describe()


# In[11]:


ratings.describe()


# In[61]:


ratings['rating'].mean()


# In[23]:


ratings.mean()


# In[62]:


ratings['rating'].min()


# In[63]:


ratings['rating'].max()


# In[64]:


ratings['rating'].std()


# In[65]:


ratings['rating'].mode()


# In[67]:


ratings.corr()


# In[11]:


filter_2 = ratings['rating'] > 0
filter_2.all()


# <h1 style="font-size:2em;color:#2467C0">Data Cleaning: Handling Missing Data</h1>

# In[68]:


movies.shape


# In[69]:


#is any row NULL ?

movies.isnull().any()


# Thats nice ! No NULL values !

# In[70]:


ratings.shape


# In[71]:


#is any row NULL ?

ratings.isnull().any()


# Thats nice ! No NULL values !

# In[72]:


tags.shape


# In[73]:


#is any row NULL ?

tags.isnull().any()


# We have some tags which are NULL.

# In[21]:


tags = tags.dropna()


# In[142]:


#Check again: is any row NULL ?

tags.isnull().any()


# In[143]:


tags.shape


# Thats nice ! No NULL values ! Notice the number of lines have reduced.

# <h1 style="font-size:2em;color:#2467C0">Data Visualization</h1>

# In[76]:


get_ipython().run_line_magic('matplotlib', 'inline')

ratings.hist(column='rating', figsize=(15,10))


# In[77]:


ratings.boxplot(column='rating', figsize=(20,25))


# <h1 style="font-size:2em;color:#2467C0">Slicing Out Columns</h1>
#  

# In[78]:


tags['tag'].head()


# In[79]:


movies[['title','genres']].head(20)


# In[85]:


ratings[-10:]


# In[86]:


movies_counts = movies['movieId'].value_counts()
movies_counts[-10:]


# In[88]:


movies_counts[:10].plot(kind='bar', figsize=(15,10))


# <h1 style="font-size:2em;color:#2467C0">Filters for Selecting Rows</h1>

# In[89]:


is_animation = movies['genres'].str.contains('Comedy', na=True)

movies[is_animation]


# In[90]:


is_animation = movies['genres'].str.contains('Animation', na=True)

movies[is_animation]


# In[91]:


movies[is_animation].head(15)


# <h1 style="font-size:2em;color:#2467C0">Group By and Aggregate </h1>

# In[94]:


import os

os.chdir('F:\Training Python\ml-latest-small\ml-latest-small')

ratings = pd.read_csv('ratings.csv', encoding='latin-1')






# In[95]:


ratings


# In[ ]:





# In[28]:


ratings.loc[1]


# In[ ]:





# In[97]:


average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()


# In[98]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.head()


# In[36]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.tail()


# <h1 style="font-size:2em;color:#2467C0">Merge Dataframes</h1>

# In[99]:


tags.head()


# In[100]:


movies.head()


# In[101]:


t = movies.merge(tags, on='movieId', how='inner')
t.head()


# More examples: http://pandas.pydata.org/pandas-docs/stable/merging.html

# Combine aggreagation, merging, and filters to get useful analytics

# In[102]:


avg_ratings = ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']
avg_ratings.head()


# In[103]:


box_office = movies.merge(avg_ratings, on='movieId', how='inner')
box_office.tail()


# In[104]:


is_highly_rated = box_office['rating'] >= 4.0

box_office[is_highly_rated][-5:]


# In[105]:


is_comedy = box_office['genres'].str.contains('Comedy', na=False)

box_office[is_comedy][:5]


# In[106]:


box_office[is_comedy & is_highly_rated][-5:]


# In[ ]:





# In[ ]:




