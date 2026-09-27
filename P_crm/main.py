import pandas as pd

df_clientes = pd.read_csv("clientes_crm.csv", encoding="utf-8")
df_interacoes = pd.read_excel("interacoes_clientes.xlsx")

print (df_clientes)