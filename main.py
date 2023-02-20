import datetime
import numpy as np
import pandas as pd
# 1
# data = pd.read_csv("sp500hst.txt", sep=",",names=["date", "ticker", "open", "high", "low", "close", "volume"])
# print(data)
# # 2
# print(data[['open','high','low','close','volume']].mean())
# 3
# x=data['date']
# i=0
# data['New']=x
# for el in x:
#     el=str(el)
#     data['New'][i]=el[6:8]
#     i+=1
# print(data)
# 4
# data = pd.read_csv("sp500hst.txt", sep=",",names=["date", "ticker", "open", "high", "low", "close", "volume"])
# unigue1=data['ticker']
# els=unigue1.unique()
# for el in els:
#         print(data.loc[data['ticker'] == el, 'volume'].sum())
# .loc[df['col1'] == value]
# 5
# data = pd.read_csv("sp500hst.txt", sep=",",header=0)
# data1= pd.read_csv('sp_data2.csv', on_bad_lines='skip')
# unigue1=data['ticker']
# p=unigue1.unique()
# data['New1']=p
# i=0
# for el in p:
#     try:
#         if data1[data1[0] == el].index.values.astype(str):
#             data['New1'][i]=data1[2][data1[data1[0] == el].index.values.astype(str)]
#             i+=1
#     except KeyError:
#         data['New1'][i]=el
#         i+=1
# print(data)
# 1.1
# recipes = pd.read_csv("recipes_sample.csv",sep=',',header=0)
# print(recipes.to_string())
# print(recipes.head().to_string())
# reviews = pd.read_csv("reviews_sample.csv", sep=",",header=0)
# print(reviews.to_string())
# print(reviews.head())
# 1.2
# print(recipes.shape[0])
# print(recipes.shape[1])
# print(recipes.dtypes)
# print(reviews.shape[0])
# print(reviews.shape[1])
# print(reviews.dtypes)
# 1.3
# print(pd.isnull(recipes).sum(axis=1).to_string())
# print(recipes.shape[0]/len(pd.isnull(recipes).sum(axis=1).to_string()))
# print(pd.isnull(reviews).sum())
# 1.4
# print(recipes.mean())
# 1.5
# x=recipes['name'].sample(10)
# print(x)
# 1.6
# reviews= reviews.set_index(np.arange(0, len(reviews)))
# print(reviews)
# 1.7
# print(recipes.loc[((recipes['minutes']<20) & (recipes['n_ingredients']<5))])
# 2.1
# recipes['submitted'] = pd.to_datetime(recipes['submitted'])
# recipes = pd.read_csv('recipes_sample.csv', parse_dates=['submitted'])
# 2.2
# recipes['submitted'] = pd.to_datetime(recipes['submitted'])
# print(recipes.loc[recipes['submitted'] < datetime.datetime(2010, 1, 1)])
# 3.1
# y=recipes['description'].tolist()
# recipes['description_lenght']=y
# for i in range(len(y)):
#     try:
#         recipes['description_lenght'][i]=len(list(y[i]))
#     except TypeError:
#         break
# print(recipes)
# 3.2
# recipes['name']=recipes['name'].str.lower()
# print(recipes)
# 3.3
# recipes['name_word_count']=len(recipes['name'].value_counts())
# 4.1
# print(recipes['contributor_id'].value_counts().to_string())
# 4.2
# print(reviews[['rating', 'recipe_id']]. value_counts().reset_index(name='count'))
# 4.3
# print(recipes['submitted'].value_counts().to_string())
# 5.1
# data=pd.DataFrame()
# data['rating']=reviews['rating']
# data['id']=recipes['id']
# data['user_id']=reviews['user_id']
# data['name']=recipes['name']
# data = data.dropna(axis=0, how='any')
# writer = pd.ExcelWriter('dataframes.xlsx', engine='xlsxwriter')
# data.to_excel(writer,sheet_name='Рецепты с оценками')
# 5.2
# data=pd.DataFrame()
# review_count=reviews['recipe_id'].value_counts()
# data['review_count']=review_count
# data['recipe_id']=reviews['recipe_id']
# data['name']=recipes['name']
# data['review_count'] = data['review_count']. fillna(0)
# writer = pd.ExcelWriter('dataframes.xlsx', engine='xlsxwriter')
# data.to_excel(writer,sheet_name='Количество отзывов по рецептам')
# 5.3
# X=pd.DataFrame()
# X['rating']=reviews['rating']
# X['date']=reviews['date']
# print(X.groupby('date')['rating'].min ())
#6.1
# recipes=recipes.sort_values(by='name_word_count', ascending=False)
# recipes.to_csv('file.csv')




