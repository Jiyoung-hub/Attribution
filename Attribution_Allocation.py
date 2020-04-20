#!/usr/bin/env python
# coding: utf-8

# ### When it's useful
# 1.Last interaction : When sales cycle does not involve a consideration phase
# 
# 2.Position_based   : When you value touchpoints that introduced customers and resulted in sales
# 
# 3.Linear           : When your ads are designed to maintain contact throught entire cycle
# 
# 4.First interaction: When you are starting off/want to create initial awareness
# 
# 5.Last non-direct  : When you want to filter out direct traffic

# ## Read data

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('attribution_allocation_student_data.csv')


# In[3]:


df.head()


# In[4]:


df.convert_TF.value_counts()


# In[5]:


df_True = df[df.convert_TF == True]


# In[6]:


spending = pd.read_csv('channel_spend_student_data.csv')


# In[7]:


pd.set_option('display.max_colwidth', -1)


# In[8]:


spending


# ## Attribution: Allocate conversions by channel

# ### Calculate CAC for each of the channels

# ### (Method1) Last interaction

# In[9]:


from collections import defaultdict
dic1 = defaultdict(list)

for k in list(range(1,4)):    
    dic2 = defaultdict(int)
    for i, row in df_True[df_True.tier == k].iterrows():
        if pd.isnull(row.touch_5) != True:
            dic2[row.touch_5] += 1 
        elif pd.isnull(row.touch_5) == True:
            if pd.isnull(row.touch_4) != True:
                dic2[row.touch_4] += 1
            elif pd.isnull(row.touch_4) == True:
                if pd.isnull(row.touch_3) != True:
                    dic2[row.touch_3] += 1
                elif pd.isnull(row.touch_3) == True:
                    if pd.isnull(row.touch_2) != True:
                        dic2[row.touch_2] += 1
                    elif pd.isnull(row.touch_2) == True:
                        if pd.isnull(row.touch_1) != True:
                            dic2[row.touch_1] += 1
    dic1[k].append(dic2)


# In[10]:


dic1


# In[11]:


# Calculate total number of converions by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))


# In[12]:


# Calculate CACs by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  300 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = 0 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))


# ### (Method2) Position Based

# In[13]:


from collections import defaultdict
dic1 = defaultdict(list)

for k in list(range(1,4)):
    dic2 = defaultdict(int)
    for i, row in df_True[df_True.tier == k].iterrows():
        if pd.isnull(row.touch_5) != True:
            dic2[row.touch_1] += 0.4
            dic2[row.touch_2] += 0.2/3
            dic2[row.touch_3] += 0.2/3
            dic2[row.touch_4] += 0.2/3
            dic2[row.touch_5] += 0.4
        elif pd.isnull(row.touch_5) == True:
            if pd.isnull(row.touch_4) != True:
                dic2[row.touch_1] += 0.4
                dic2[row.touch_2] += 0.2/2
                dic2[row.touch_3] += 0.2/2
                dic2[row.touch_4] += 0.4
            elif pd.isnull(row.touch_4) == True:
                if pd.isnull(row.touch_3) != True:
                    dic2[row.touch_1] += 0.4
                    dic2[row.touch_2] += 0.2
                    dic2[row.touch_3] += 0.4
                elif pd.isnull(row.touch_3) == True:
                    if pd.isnull(row.touch_2) != True:
                        dic2[row.touch_1] += .5
                        dic2[row.touch_2] += .5
                    elif pd.isnull(row.touch_2) == True:
                        if pd.isnull(row.touch_1) != True:
                            dic2[row.touch_1] += 1
    dic1[k].append(dic2)          


# In[14]:


dic1


# In[15]:


# Calculate total number of converions by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))


# In[16]:


# Calculate CACs by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  300 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = 0 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))


# ### (Method3) Linear

# In[17]:


from collections import defaultdict
dic1 = defaultdict(list)

for k in list(range(1,4)):
    dic2 = defaultdict(int)
    for i, row in df_True[df_True.tier == k].iterrows():
        if pd.isnull(row.touch_5) != True:
            dic2[row.touch_1] += 1/5
            dic2[row.touch_2] += 1/5
            dic2[row.touch_3] += 1/5
            dic2[row.touch_4] += 1/5
            dic2[row.touch_5] += 1/5
        if pd.isnull(row.touch_5) == True:
            if pd.isnull(row.touch_4) != True:
                dic2[row.touch_1] += 1/4
                dic2[row.touch_2] += 1/4
                dic2[row.touch_3] += 1/4
                dic2[row.touch_4] += 1/4
            if pd.isnull(row.touch_4) == True:
                if pd.isnull(row.touch_3) != True:
                    dic2[row.touch_1] += 1/3
                    dic2[row.touch_2] += 1/3
                    dic2[row.touch_3] += 1/3
                if pd.isnull(row.touch_3) == True:
                    if pd.isnull(row.touch_2) != True:
                        dic2[row.touch_1] += .5
                        dic2[row.touch_2] += .5
                    if pd.isnull(row.touch_2) == True:
                        if pd.isnull(row.touch_1) != True:
                            dic2[row.touch_1] += 1
    dic1[k].append(dic2)   


# In[18]:


dic1


# In[19]:


# Calculate total number of converions by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))


# In[20]:


# Calculate CACs by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  300 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = 0 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))


# ### (Method4) First interaction

# In[21]:


from collections import defaultdict
dic1 = defaultdict(list)

for k in list(range(1,4)):
    dic2 = defaultdict(int)
    for i, row in df_True[df_True.tier == k].iterrows():
        if pd.isnull(row.touch_1) != True:
            dic2[row.touch_1] += 1
    dic1[k].append(dic2)   


# In[22]:


dic1


# In[23]:


# Calculate total number of converions by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))


# In[24]:


# Calculate CACs by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  300 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = 0 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))


# ### (Method5) Last non-direct interaction

# In[25]:


from collections import defaultdict
dic1 = defaultdict(list)

for k in list(range(1,4)):    
    dic2 = defaultdict(int)
    for i, row in df_True[df_True.tier == k].iterrows():
        if pd.isnull(row.touch_5) != True and row.touch_5 != 'direct':
            dic2[row.touch_5] += 1 
        elif (row.touch_5 == 'direct') or (pd.isnull(row.touch_5) == True):
            if pd.isnull(row.touch_4) != True and row.touch_4 != 'direct':
                dic2[row.touch_4] += 1
            elif (row.touch_4 == 'direct') or (pd.isnull(row.touch_4) == True):
                if pd.isnull(row.touch_3) != True and row.touch_3 != 'direct':
                    dic2[row.touch_3] += 1
                elif (row.touch_3 == 'direct') or (pd.isnull(row.touch_3) == True):
                    if pd.isnull(row.touch_2) != True and row.touch_2 != 'direct':
                        dic2[row.touch_2] += 1
                    elif (row.touch_2 == 'direct') or (pd.isnull(row.touch_2) == True):
                        if pd.isnull(row.touch_1) != True and row.touch_1 != 'direct':
                            dic2[row.touch_1] += 1
                        else:
                            dic2[row.touch_1] += 1
    dic1[k].append(dic2)


# In[26]:


dic1


# In[27]:


# Calculate total number of converions by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier]
        print(tier + "_conversions = "+ str(round(CAC,2)))


# In[28]:


# Calculate CACs by channel 
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['direct','organic_search']:
        CAC =  300 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))
    elif tier in ['direct','organic_search']:
        CAC = 0 / (dic1[1][0][tier] + dic1[2][0][tier] + dic1[3][0][tier])
        print(tier + "_CAC = "+ str(round(CAC,2)))


# # Visualization

# In[29]:


import seaborn as sns


# In[30]:


viz_dt = {'social_CAC':[.85,.86,.85,.88,.66],
         'organic_search_CAC':[0,0,0,0,0],
         'email_CAC':[.93,0.88,.89,.84,.7],
         'display_CAC':[.74,.72,.72,.69,.57],
         'direct_CAC':[0,0,0,0,0],
         'referral_CAC':[30.0,29.13,29.17,30.0,21.43],
         'paid_search_CAC':[25.0,26.71,28.39,25.0,21.43]}

viz= pd.DataFrame(viz_dt, index=['Last interaction','Position_based','Linear','First interaction','Last non-direct interaction'])

viz


# In[32]:


# plotting average CAC by attribution method
viz[['social_CAC','email_CAC', 'display_CAC', 'referral_CAC', 'paid_search_CAC']].plot(kind='bar',color=['lightslategray','steelblue','powderblue', 'lavender', 'lightskyblue']);


# In[33]:


# plotting average CAC by channel
viz[['social_CAC', 'email_CAC','display_CAC','referral_CAC', 'paid_search_CAC']].T.plot(kind='bar',color=['powderblue', 'lavender', 'lightskyblue', 'steelblue', 'lightslategray']);


# ## Allocation

# ### We chose 'last non-direct interation' method

# In[34]:


# calculate the marginal CAC by spending tier by channel

df_channels = pd.DataFrame()
tier_list = ['social', 'organic_search', 'email', 'display', 'direct', 'referral', 'paid_search']
for tier in tier_list:
    if tier not in ['organic_search','direct']:
        data = {'Cumulative spend':[50,100,150],
           'Cumulative number of conversions':[dic1[1][0][tier],dic1[2][0][tier],dic1[3][0][tier]],
           'Average CAC':[50/dic1[1][0][tier], 100/(dic1[2][0][tier]), 150/(dic1[3][0][tier])],
           'Marginal spend':[50,50,50],
           'Marginal conversions':[dic1[1][0][tier],dic1[2][0][tier]-dic1[1][0][tier],dic1[3][0][tier]-dic1[2][0][tier]],
           'Marginal CAC':[50/(dic1[1][0][tier]), 50/(dic1[2][0][tier]-dic1[1][0][tier]), 50/(dic1[3][0][tier]-dic1[2][0][tier])],
               'Channel':tier}
    elif tier in ['organic_search','direct']:
            data = {'Cumulative spend':[0,0,0],
           'Cumulative number of conversions':[dic1[1][0][tier],dic1[2][0][tier],dic1[3][0][tier]],
           'Average CAC':[0/dic1[1][0][tier], 0/(dic1[2][0][tier]), 0/dic1[3][0][tier]],
           'Marginal spend':[0,0,0],
           'Marginal conversions':[dic1[1][0][tier],dic1[2][0][tier]-dic1[1][0][tier],dic1[3][0][tier]-dic1[2][0][tier]],
           'Marginal CAC':[0/(dic1[1][0][tier]), 0/(dic1[2][0][tier]-dic1[1][0][tier]), 0/(dic1[3][0][tier]-dic1[2][0][tier])],
               'Channel':tier}

    df_channel = pd.DataFrame(data, index =['tier1','tier2','tier3'])
    df_channels = pd.concat([df_channels, df_channel])


# In[35]:


df_channels


# In[36]:


# create a pivot table (CAC)

Marginal_CAC_table = pd.pivot_table(df_channels, index=df_channels.index, columns='Channel', values='Marginal CAC')
Marginal_CAC_table


# In[37]:


# create a pivot table (# of converions)

Number_of_conversions = pd.DataFrame(50/Marginal_CAC_table.iloc[0])
Number_of_conversions = Number_of_conversions.join(50/Marginal_CAC_table.iloc[1])
Number_of_conversions = Number_of_conversions.join(50/Marginal_CAC_table.iloc[2])
Number_of_conversions = Number_of_conversions.T
round(Number_of_conversions,0)

