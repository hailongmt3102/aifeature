# -*- coding: utf-8 -*-
"""Product Recommendations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17qUg6XbldNFYjKfbWwdIaOq6kSISQ87a

# Loading Dependencies
"""

import pandas as pd

"""# Loading Dataset"""
from sklearn.metrics.pairwise import cosine_similarity


def test() : 

    df = pd.read_excel('Online Retail.xlsx')

    """# Data Processing

    ### Eliminating data with item returns (negative quantity)
    """

    df = df.loc[df['Quantity'] > 0]

    """### Identify null components"""

    df.info()

    """### Handling Nan CustomerID"""

    df['CustomerID'].isna().sum()
    df = df.dropna(subset=['CustomerID'])

    """### Creating the customer-item matrix"""

    customer_item_matrix = df.pivot_table(
        index='CustomerID',
        columns='StockCode',
        values='Quantity',
        aggfunc='sum'
    )
    customer_item_matrix.loc[12481:].head()

    customer_item_matrix = customer_item_matrix.applymap(lambda x: 1 if x > 0 else 0)

    """# Collaborative Filtering"""


    """## User based collaborative filtering"""

    user_user_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix))
    user_user_sim_matrix.head()

    #Renaming index and column names

    user_user_sim_matrix.columns = customer_item_matrix.index

    user_user_sim_matrix['CustomerID'] = customer_item_matrix.index
    user_user_sim_matrix = user_user_sim_matrix.set_index('CustomerID')
    user_user_sim_matrix.head()

    user_user_sim_matrix.loc[12350.0].sort_values(ascending=False).head(10)

    """### Making Recommendations"""

    user_user_sim_matrix.loc[12350.0].sort_values(ascending=False)
    items_bought_by_A = customer_item_matrix.loc[12350.0][customer_item_matrix.loc[12350.0]>0]


    items_bought_by_B = customer_item_matrix.loc[17935.0][customer_item_matrix.loc[17935.0]>0]

    items_to_recommend_to_B = set(items_bought_by_A.index) - set(items_bought_by_B.index)

    df.loc[df['StockCode'].isin(items_to_recommend_to_B),['StockCode', 'Description']].drop_duplicates().set_index('StockCode')

    """## Item-based collaborative filtering"""

    item_item_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix.T))
    item_item_sim_matrix.columns = customer_item_matrix.T.index

    item_item_sim_matrix['StockCode'] = customer_item_matrix.T.index
    item_item_sim_matrix = item_item_sim_matrix.set_index('StockCode')


    """### Making Recommendations"""

    top_10_similar_items = list(item_item_sim_matrix.loc[23166].sort_values(ascending=False).iloc[:10].index)
    return top_10_similar_items

# print(top_10_similar_items)
# print()
# print(df.loc[
#     df['StockCode'].isin(top_10_similar_items),
#     ['StockCode', 'Description']
# ].drop_duplicates().set_index('StockCode').loc[top_10_similar_items])
