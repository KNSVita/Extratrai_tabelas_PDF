import pandas as pd
from PyPDF2 import PdfReader

def extrair_texto_do_pdf(caminho_pdf, inicio_pagina, fim_pagina):
    texto_extraido = ""

    with open(caminho_pdf, 'rb') as arquivo_pdf:
        pdf_reader = PdfReader(arquivo_pdf)
        
        for numero_pagina in range(inicio_pagina - 1, fim_pagina):
            pagina = pdf_reader.pages[numero_pagina]
            texto_extraido += pagina.extract_text()

    return texto_extraido

def salvar_texto_no_excel(texto, caminho_excel):
    # Dividir o texto em linhas e criar um DataFrame
    linhas = texto.split('\n')
    df = pd.DataFrame(linhas, columns=['Conteúdo'])

    # Salvar no Excel
    df.to_excel(caminho_excel, index=False, engine='openpyxl')

# Exemplo de uso
caminho_do_pdf = 'D:\\Python\\Leitor de PDF para excel\\JOEL MATEUS DAS NEVES.pdf'
inicio_pagina = 770
fim_pagina = 770
caminho_do_excel = 'D:\\Python\\Leitor de PDF para excel\\Cópia de TABELA(1).xlsx'

texto_extraido = extrair_texto_do_pdf(caminho_do_pdf, inicio_pagina, fim_pagina)
salvar_texto_no_excel(texto_extraido, caminho_do_excel)