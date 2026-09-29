import pandas as pd

df_clientes = pd.read_csv(
    "P_crm/clientes_crm.csv",
    encoding="utf-8"
)
df_clientes_arrumado = df_clientes.copy()

df_clientes_arrumado["segmento cliente"] = df_clientes_arrumado["segmento cliente"].fillna("Não informado")
df_clientes_arrumado["email"] = df_clientes_arrumado["email"].fillna("Não informado")

df_interacoes = pd.read_excel(
    "P_crm/interacoes_clientes.xlsx"
    )

df_interacoes_arrumado = df_interacoes.copy()

df_interacoes_arrumado["duracao minutos"] = df_interacoes_arrumado["duracao minutos"].fillna(df_interacoes_arrumado["duracao minutos"].median())
df_interacoes_arrumado["satisfacao cliente"] = df_interacoes_arrumado["satisfacao cliente"].fillna(df_interacoes_arrumado["satisfacao cliente"].median())

##print(df_clientes_arrumado.isna().mean() * 100)
##print(df_interacoes_arrumado.isna().mean() * 100)

print("ANTES:")
print(df_clientes.isna().sum())

print("\nDEPOIS:")
print(df_clientes_arrumado.isna().sum())