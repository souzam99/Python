
# coding: utf-8

# ## Missão: Analisar o Comportamento de Compra de Consumidores.

# ## Nível de Dificuldade: Alto

# Você recebeu a tarefa de analisar os dados de compras de um web site! Os dados estão no formato JSON e disponíveis junto com este notebook.
# 
# No site, cada usuário efetua login usando sua conta pessoal e pode adquirir produtos à medida que navega pela lista de produtos oferecidos. Cada produto possui um valor de venda. Dados de idade e sexo de cada usuário foram coletados e estão fornecidos no arquivo JSON.
# 
# Seu trabalho é entregar uma análise de comportamento de compra dos consumidores. Esse é um tipo de atividade comum realizado por Cientistas de Dados e o resultado deste trabalho pode ser usado, por exemplo, para alimentar um modelo de Machine Learning e fazer previsões sobre comportamentos futuros.
# 
# Mas nesta missão você vai analisar o comportamento de compra dos consumidores usando o pacote Pandas da linguagem Python e seu relatório final deve incluir cada um dos seguintes itens:
# 
# ** Contagem de Consumidores **
# 
# * Número total de consumidores
# 
# 
# ** Análise Geral de Compras **
# 
# * Número de itens exclusivos
# * Preço médio de compra
# * Número total de compras
# * Rendimento total
# 
# 
# ** Informações Demográficas Por Gênero **
# 
# * Porcentagem e contagem de compradores masculinos
# * Porcentagem e contagem de compradores do sexo feminino
# * Porcentagem e contagem de outros / não divulgados
# 
# 
# ** Análise de Compras Por Gênero **
# 
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Compras for faixa etária
# 
# 
# ** Identifique os 5 principais compradores pelo valor total de compra e, em seguida, liste (em uma tabela): **
# 
# * Login
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Itens mais populares
# 
# 
# ** Identifique os 5 itens mais populares por contagem de compras e, em seguida, liste (em uma tabela): **
# 
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
# * Itens mais lucrativos
# 
# 
# ** Identifique os 5 itens mais lucrativos pelo valor total de compra e, em seguida, liste (em uma tabela): **
# 
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
# 
# 
# ** Como considerações finais: **
# 
# * Seu script deve funcionar para o conjunto de dados fornecido.
# * Você deve usar a Biblioteca Pandas e o Jupyter Notebook.
# 

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# In[ ]:


# Imports
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


# In[14]:


# Carrega o arquivo
load_file = "dados_compras.json"
purchase_file = pd.read_json(load_file, orient = "records")
purchase_file.head()

df = purchase_file


# In[16]:


df.info()


# In[117]:


df.head()


# ## Informações Sobre os Consumidores

# In[389]:


# Implemente aqui sua solução
df_unicos = df.drop_duplicates(["Login"])

#Número total de consumidores
print("\n=== Número total de consumidores ===")
usuarios = df_unicos["Login"].unique()
print("Número total de consumidores: " + str(len(usuarios)))


# ## Análise Geral de Compras

# In[565]:


print("Valor total das vendas: $ " + str(df["Valor"].sum()))
print()
print("Média dos valores das compras (dp): $ %.2f (%.2f)" %(df['Valor'].mean(), df['Valor'].std()))
print("Maior valor de compra: $ %s" %df['Valor'].max())
print("Menor valor de compra: $ %s" %df['Valor'].min())




df_unicos_itens = df.drop_duplicates(["Item ID"])


# Número de itens exclusivos

print("\n=== Número de itens exclusivos ===")
usuarios = df_unicos_itens["Item ID"].unique()
print("Número de itens exclusivos: " + str(len(usuarios)))





print("\n=== Análise de correlação ===")

compras_usuarios = df.groupby('Login')[['Valor']].sum()


for i in compras_usuarios.index:
    df_unicos.loc[df_unicos['Login'] == i, 'Valor'] = compras_usuarios.loc[i, "Valor"]

from scipy.stats.stats import pearsonr
correlacao = pearsonr(df_unicos["Idade"], df_unicos["Valor"])

print("Não há correlação significativa entre a Idade e o Valor (r = %.4f e p = %.4f )" %(correlacao[0],correlacao[1]))


# ## Informações Demográficas Por Gênero

# In[390]:


print("\n=== Sexo ===")
aux = pd.DataFrame(df_unicos["Sexo"].value_counts())
aux["Percentual"] = aux["Sexo"]/aux["Sexo"].sum()*100

print(aux)

plt.bar(aux.index,aux["Sexo"])
plt.title("Quantidade de clientes por genero")
plt.show()

plt.pie(aux["Percentual"], labels = aux.index, autopct='%1.1f%%')
plt.title("Percentual de clientes por genero")
plt.show()


# ## Análise de Compras Por Gênero

# In[397]:


#Número de compras
print("\n=== Número de compras por gênero ===")
contagem_compras_genero = df.groupby("Sexo")[["Valor"]].count()
contagem_compras_genero = contagem_compras_genero.sort_values("Valor", ascending=False)
print(contagem_compras_genero)

plt.bar(contagem_compras_genero.index, contagem_compras_genero["Valor"])
plt.title("Número de compras por gênero")
plt.show()


#Valor Total de Compra
print("\n=== Totla do valor de compras por gênero ===")
valor_compras_genero = df.groupby("Sexo")[["Valor"]].sum()
valor_compras_genero = valor_compras_genero.sort_values("Valor", ascending=False)
print(valor_compras_genero)

plt.bar(valor_compras_genero.index, valor_compras_genero["Valor"])
plt.title("Total do valor das compras por gênero ($)")
plt.show()



#Preço médio de compra
print("\n=== Preço médio de compras por gênero ===")
media = valor_compras_genero/contagem_compras_genero
media = media.sort_values('Valor', ascending=False)
print(media)

plt.bar(media.index, media["Valor"])
plt.title("Média de valor por gênero")
plt.show()




#Compras for faixa etária
print("\n=== Idade ===")
print("Média das idades (dp): %.2f (%.2f)" %(df_unicos['Idade'].mean(), df_unicos['Idade'].std()))
print("Maior idade: %s" %df_unicos['Idade'].max())
print("Menor idade: %s" %df_unicos['Idade'].min())


plt.hist(df_unicos["Idade"])
plt.title("Distribuição das idades do clientes")
plt.show()


# ## Consumidores Mais Populares (Top 5)

# In[564]:


consumidor_populares = df.groupby(["Login"]).agg({"Item ID": "count", "Valor": sum})
consumidor_populares.columns = ["Quantidade de compras","Valor Total"]
top_5_consumidor_populares = consumidor_populares.sort_values("Valor Total", ascending=False).head()
top_5_consumidor_populares =top_5_consumidor_populares.reset_index()
top_5_consumidor_populares["Valor médio de compra"] =     top_5_consumidor_populares["Valor Total"]/top_5_consumidor_populares["Quantidade de compras"] 


print(f'{"Top 5 consumidores mais populares":^50}')
print('============================================================================')
print(f'{"Login do consumidor":<20} {"Qtd de compras":>15} {"Receita total":>15} {"Valor médio de compra":>23}')
print('----------------------------------------------------------------------------')
for i in top_5_consumidor_populares.index:
    #print(top_5_itens_populares.loc[i])
    nome, quantidade, total, media = top_5_consumidor_populares.loc[i]
    print(f'{nome:<20} {quantidade:>14} {total:>15,.2f}{media:>23,.2f}')
print('============================================================================')


plt.bar(top_5_consumidor_populares["Login"], top_5_consumidor_populares["Quantidade de compras"])
plt.title("Top 5 consumidores mais populares")
plt.xticks(rotation=90)

plt.show()


# ## Itens Mais Populares

# In[506]:


itens_populares = df.groupby(["Nome do Item", "Item ID", "Valor"]).agg({"Item ID": "count", "Valor": sum})
itens_populares.columns = ["Quantidade de compras","Valor Total"]
top_5_itens_populares = itens_populares.sort_values("Quantidade de compras", ascending=False).head()
top_5_itens_populares =top_5_itens_populares.reset_index()


print(f'{"Top 5 itens mais populares":^80}')
print('=======================================================================================')
print(f'{"ID":>5} {"Nome do produto":<40} {"Valor":>5} {"Qtd vendida":>15} {"Receita total":>15}')
print('---------------------------------------------------------------------------------------')
for i in top_5_itens_populares.index:
    #print(top_5_itens_populares.loc[i])
    nome, item_id, valor, quantidade, total = top_5_itens_populares.loc[i]
    print(f'{item_id:>5} {nome:<40} {valor:>5,.2f} {quantidade:>14} {total:>15,.2f}')
print('=======================================================================================')


plt.bar(top_5_itens_populares["Nome do Item"], top_5_itens_populares["Quantidade de compras"])
plt.title("Top 5 itens mais populares")
plt.xticks(rotation=90)

plt.show()


# ## Itens Mais Lucrativos

# In[509]:


itens_populares = df.groupby(["Nome do Item", "Item ID", "Valor"]).agg({"Item ID": "count", "Valor": sum})
itens_populares.columns = ["Quantidade de compras","Valor Total"]
top_5_itens_populares = itens_populares.sort_values("Valor Total", ascending=False).head()
top_5_itens_populares =top_5_itens_populares.reset_index()


print(f'{"Top 5 itens mais lucrativos":^80}')
print('=======================================================================================')
print(f'{"ID":>5} {"Nome do produto":<40} {"Valor":>5} {"Qtd vendida":>15} {"Receita total":>15}')
print('---------------------------------------------------------------------------------------')
for i in top_5_itens_populares.index:
    #print(top_5_itens_populares.loc[i])
    nome, item_id, valor, quantidade, total = top_5_itens_populares.loc[i]
    print(f'{item_id:>5} {nome:<40} {valor:>5,.2f} {quantidade:>14} {total:>15,.2f}')
print('=======================================================================================')


plt.bar(top_5_itens_populares["Nome do Item"], top_5_itens_populares["Valor Total"])
plt.title("Top 5 itens mais lucrativos")
plt.xticks(rotation=90)

plt.show()

