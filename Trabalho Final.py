#!/usr/bin/env python
# coding: utf-8

# In[31]:


get_ipython().system('pip install yfinance')


# In[32]:


import yfinance as yf 
import pandas as pd
import numpy as np


# In[8]:


df = pd.read_csv('acoes.csv', index_col='Volume')

df_ordenado = df.sort_values(by=['Volume'], ascending = False)

print(df_ordenado.head(10))


# In[33]:


lista_ações = ['ALPA4.SA','ABEV3.SA','AMER3.SA','ASAI3.SA','AZUL4.SA','B3SA3.SA','BIDI4.SA','BIDI11.SA','BPAN4.SA','BBSE3.SA','BRML3.SA','BBDC3.SA','BBDC4.SA','BRAP4.SA','BBAS3.SA','BRKM5.SA','BRFS3.SA','BPAC11.SA','CRFB3.SA','CCRO3.SA','CMIG4.SA','CIEL3.SA','COGN3.SA','CPLE6.SA','CSAN3.SA','CPFE3.SA','CVCB3.SA','CYRE3.SA','DXCO3.SA','ECOR3.SA','ELET3.SA','ELET6.SA','IRBR3.SA','ENBR3.SA','ENGI11.SA','ENEV3.SA','EGIE3.SA','EQTL3.SA','EZTC3.SA','FLRY3.SA','GGBR4.SA','GOAU4.SA','GOLL4.SA','NTCO3.SA','SOMA3.SA','HAPV3.SA','HYPE3.SA','IGTA3.SA','GNDI3.SA','IRBR3.SA','ITSA4.SA','ITUB4.SA','JBSS3.SA','JHSF3.SA','KLBN11.SA','RENT3.SA','LCAM3.SA','LWSA3.SA','LAME4.SA','LREN3.SA','MGLU3.SA','MRFG3.SA','CASH3.SA','BEEF3.SA','MRVE3.SA','MULT3.SA','PCAR3.SA','PETR3.SA','PETR4.SA','BRDT3.SA','PRIO3.SA','PETZ3.SA','QUAL3.SA','RADL3.SA','RDOR3.SA','RAIL3.SA','SBSP3.SA','SANB11.SA','CSNA3.SA','SULA11.SA','SUZB3.SA','TAEE11.SA','VIVT3.SA','TIMS3.SA','TOTS3.SA','UGPA3.SA','USIM5.SA','VALE3.SA','VIIA3.SA','WEGE3.SA','YDUQ3.SA']
data_frame = list()

for ticker in lista_ações:
    data = yf.download(ticker, group_by='Ações', period='1d')
    data['Ações'] = ticker
    data_frame.append(data)

    
df = pd.concat(data_frame)
df.to_csv('acoes.csv')


# In[34]:


papeis = ['PETR4.SA', 'MGLU3.SA', 'CASH3.SA',
          'COGN3.SA', 'PRIO3.SA', 'BBDC4.SA', 
          'VIIA3.SA', 'ITUB4.SA', 'LAME4.SA',
          'PETR3.SA']


# In[35]:


compras = {'PETR4.SA':1000, 'MGLU3.SA':700, 'CASH3.SA':1500,
          'COGN3.SA':700, 'PRIO3.SA':200, 'BBDC4.SA':700, 
          'VIIA3.SA':1500, 'ITUB4.SA':2000, 'LAME4.SA':1500,
          'PETR3.SA':200}


# In[36]:


inicio = '2022-11-22'
fim = '2022-11-27'

precos = pd.DataFrame()
for i in papeis:
    precos[i] = yf.download(i,start = inicio, end = fim)['Adj Close']


# In[37]:


compras_df = pd.Series(data= compras, index=list(compras.keys()))

sum(compras.values())


# In[38]:


primeiro = precos.iloc[0]


# In[39]:


qtd_acoes = compras_df/primeiro


# In[40]:


PL = precos*qtd_acoes


# In[41]:


PL.head(5)


# In[42]:


PL['PL Total'] = PL.iloc[:].sum(axis = 1)


# In[43]:


PL.head(5)


# In[44]:


ibov = yf.download('^BVSP', start = inicio, end = fim)


# In[45]:


ibov.rename(columns = {'Adj Close':'IBOV'}, inplace = True)

ibov = ibov.drop(ibov.columns[[0,1,2,3,5]], axis = 1)


# In[46]:


ibov.index = pd.to_datetime(ibov.index)


# In[47]:


PL.index = pd.to_datetime(PL.index)


# In[48]:


novo_df = pd.merge(ibov, PL, how = 'inner', on = 'Date')


# In[49]:


PL_normalizado = novo_df/novo_df.iloc[0]


# In[50]:


PL_normalizado.head()


# In[51]:


PL_normalizado[['IBOV','PL Total']].plot(figsize=(10,10));


# In[ ]:




