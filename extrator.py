import pdfplumber
import pandas as pd

def extrair_tabela(caminhoPDF, paginaInicial, paginaFinal):
    with pdfplumber.open(caminhoPDF) as pdf:
        dados_por_pag = {}

        for numero_pag in range(paginaInicial - 1, paginaFinal):
            pagina = pdf.pages[numero_pag]
            tabela = pagina.extract_table()
            dados_por_pag[f'Página {numero_pag + 1}'] = tabela

    return dados_por_pag

def salvar_excel(dados_por_pag, nome_arquivo):
    with pd.ExcelWriter(nome_arquivo) as writer:
        for nomePag, dadosPag in dados_por_pag.items():
            df_pagina = pd.DataFrame(dadosPag[1:], columns=dadosPag[0])
            df_pagina = df_pagina.transpose()
            df_pagina.to_excel(writer, sheet_name=nomePag, index=True)