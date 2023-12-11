import pandas as pd

# Carregue a planilha (CSV ou Excel)
# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo ou caminho
dados = pd.read_excel('Cópia de TABELA(1).xlsx')  # ou pd.read_excel('seu_arquivo.xlsx')

# Se você já sabe que os dados estão nas linhas 45 a 59
linhas_desejadas = dados.loc[43:57]

# Verifique se há dados nas linhas desejadas
if not linhas_desejadas.empty:
    print(linhas_desejadas)
else:
    print('Nenhuma linha encontrada nas posições especificadas.')
