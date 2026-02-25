import pandas as pd

df = pd.read_csv('esportes_rj_amostra.csv')
print("\n--- Primeiras Linhas da Tabela ---\n")
print(df.head())
print("\n--- Informações da Tabela ---\n")
df.info()

esportes_niteroi = df[df['cidade'] == 'Niterói']
print("\n--- Cnetro esportivos de niteroi ---\n")

investimento_por_esporte = df.groupby('tipo_esporte')['investimento_mensal_reais'].sum().reset_index()
investimento_por_esporte = investimento_por_esporte.sort_values(by='investimento_mensal_reais', ascending=False)